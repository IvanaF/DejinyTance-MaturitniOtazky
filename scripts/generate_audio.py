#!/usr/bin/env python3
"""
Generátor audio souborů z audio-scénářů pomocí Edge TTS (Microsoft)

Vytváří MP3 audio soubory z textových scénářů s použitím Microsoft Edge TTS.
Edge TTS je zcela zdarma, nevyžaduje API klíč a podporuje češtinu s přirozenými hlasy.
"""

import os
import sys
import asyncio
import re
import edge_tts
import json
from pathlib import Path
from typing import Optional

# Fix Windows console encoding for Czech characters
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except:
        pass

# Cesta k projektu
PROJECT_ROOT = Path(__file__).parent.parent
AUDIO_SCRIPTS_DIR = PROJECT_ROOT / "data" / "audio_scripts"
AUDIO_OUTPUT_DIR = PROJECT_ROOT / "assets" / "audio"

# České hlasy
CZECH_VOICES = {
    "female": "cs-CZ-VlastaNeural",  # Ženský hlas
    "male": "cs-CZ-AntoninNeural"    # Mužský hlas
}


async def list_czech_voices():
    """Vypíše seznam dostupných českých hlasů"""
    voices = await edge_tts.list_voices()
    czech_voices = [v for v in voices if v["Locale"].startswith("cs-CZ")]
    
    print("\nDostupne ceske hlasy:")
    for voice in czech_voices:
        gender = voice.get("Gender", "Unknown")
        name = voice.get("ShortName", "Unknown")
        friendly_name = voice.get("FriendlyName", name)
        print(f"  {name}: {friendly_name} ({gender})")
    print()
    
    return czech_voices


async def find_voice_by_name(search_name: str) -> Optional[str]:
    """
    Najde voice ID podle názvu hlasu (např. "Jana", "Vlasta", "Antonín")
    """
    voices = await edge_tts.list_voices()
    czech_voices = [v for v in voices if v["Locale"].startswith("cs-CZ")]
    
    search_lower = search_name.lower()
    for voice in czech_voices:
        friendly_name = voice.get("FriendlyName", "").lower()
        short_name = voice.get("ShortName", "").lower()
        
        if search_lower in friendly_name or search_lower in short_name:
            return voice.get("ShortName")
    
    return None


async def generate_audio_async(
    text: str,
    voice: str,
    output_path: Path,
    rate: str = "+0%",
    pitch: str = "+0Hz"
) -> bool:
    """
    Vygeneruje audio soubor z textu pomocí Edge TTS
    
    Args:
        text: Text k převedení na řeč
        voice: Název hlasu (např. "cs-CZ-VlastaNeural")
        output_path: Cesta pro uložení MP3 souboru
        rate: Rychlost řeči (např. "+10%" pro rychleji, "-10%" pro pomaleji)
        pitch: Výška hlasu (např. "+10Hz" pro vyšší, "-10Hz" pro nižší)
    
    Returns:
        True pokud bylo generování úspěšné, False jinak
    """
    try:
        print(f"Generuji audio... (delka textu: {len(text)} znaku)")
        print(f"Pouzivam hlas: {voice}")
        
        # Vytvoř výstupní adresář
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Vygeneruj audio
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await communicate.save(str(output_path))
        
        file_size = output_path.stat().st_size / 1024  # KB
        print(f"[OK] Audio uspesne vygenerovano: {output_path}")
        print(f"  Velikost souboru: {file_size:.1f} KB")
        return True
        
    except Exception as e:
        print(f"[ERROR] Chyba pri generovani audio: {e}")
        return False


def read_script(script_path: Path) -> Optional[str]:
    """Přečte text ze scénáře"""
    try:
        with open(script_path, "r", encoding="utf-8") as f:
            text = f.read().strip()
        return text
    except Exception as e:
        print(f"[ERROR] Chyba pri cteni scenare: {e}")
        return None


def extract_content_title(text: str) -> Optional[str]:
    """
    Extrahuje smysluplný název z obsahu scénáře.
    Hledá fráze jako "zaměříme na", "části se zaměříme na", atd.
    """
    if not text:
        return None
    
    # Najdi první větu nebo část textu, která obsahuje informaci o tématu
    # Hledej různé varianty: "zaměříme na", "zaměříme se na", "části o", atd.
    patterns = [
        r'části se zaměříme na ([^.,]+?)[.,]',
        r'části zaměříme na ([^.,]+?)[.,]',
        r'zaměříme (?:se )?na ([^.,]+?)[.,]',
        r'zaměřujeme (?:se )?na ([^.,]+?)[.,]',
        r'část o ([^.,]+?)[.,]',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            title = match.group(1).strip()
            
            # Normalizuj běžné výrazy a převeď z 4. pádu na 1. pád
            title_normalizations = {
                'egyptskou civilizaci': 'Egypt',
                'egyptské civilizace': 'Egypt',
                'egyptskou': 'Egypt',
                'egypt': 'Egypt',
                'mezopotámii': 'Mezopotámie',
                'mezopotámie': 'Mezopotámie',
                'pravěk': 'Pravěk',
                # Převod z 4. pádu na 1. pád pro běžné názvy zemí
                'indii': 'Indie',
                'čínu': 'Čína',
                'japonsko': 'Japonsko',  # už je v 1. pádě
            }
            
            # Zkus najít normalizovaný výraz (case-insensitive)
            title_lower = title.lower()
            for key, value in title_normalizations.items():
                if key in title_lower:
                    return value
            
            # Pokud není normalizovaný výraz, vezmi první 1-3 významná slova
            words = title.split()
            # Odstraň články a předložky na začátku
            stop_words = ['na', 'o', 'v', 'z', 'ze', 'do', 'od']
            while words and words[0].lower() in stop_words:
                words.pop(0)
            
            if words:
                # Vezmi první 1-3 slova (max 25 znaků)
                result = ' '.join(words[:3])
                if len(result) > 25:
                    result = ' '.join(words[:2])
                if len(result) > 25:
                    result = words[0]
                
                # Zajisti správnou velikost písmen (velké první písmeno)
                if result:
                    result = result[0].upper() + result[1:] if len(result) > 1 else result.upper()
                    return result
    
    return None


def find_audio_scripts(topic_id: str) -> list[Path]:
    """
    Najde všechny audio-scénáře pro dané téma.
    Podporuje buď jeden soubor (T01.txt) nebo více souborů (T01_part1.txt, T01_part2.txt, ...)
    
    Returns:
        Seznam cest k souborům se scénáři, seřazený podle názvu
    """
    scripts = []
    
    # Nejdřív zkus najít jeden soubor (T01.txt)
    single_script = AUDIO_SCRIPTS_DIR / f"{topic_id}.txt"
    if single_script.exists():
        return [single_script]
    
    # Pokud neexistuje, hledej více souborů (T01_part1.txt, T01_part2.txt, ...)
    pattern = f"{topic_id}_part*.txt"
    part_scripts = sorted(AUDIO_SCRIPTS_DIR.glob(pattern))
    
    if part_scripts:
        return part_scripts
    
    # Pokud ani to nefunguje, zkus najít jakékoli soubory začínající na topic_id
    all_scripts = sorted(AUDIO_SCRIPTS_DIR.glob(f"{topic_id}*.txt"))
    if all_scripts:
        return all_scripts
    
    return []


def get_topic_info(topic_id: str):
    """Načte informace o tématu z JSON souboru"""
    topic_json_path = PROJECT_ROOT / "data" / "topics" / f"{topic_id}.json"
    
    if not topic_json_path.exists():
        return None
    
    try:
        import json
        with open(topic_json_path, "r", encoding="utf-8") as f:
            topic_data = json.load(f)
        return topic_data
    except Exception as e:
        print(f"[WARNING] Nepodarilo se nacist topic JSON: {e}")
        return None


def get_voice_for_topic(topic_id: str) -> str:
    """
    Určí hlas pro téma - střídá ženský a mužský hlas
    T01 = female, T02 = male, T03 = female, atd.
    """
    try:
        # Extrahuj číslo z topic_id (např. "T01" -> 1)
        topic_num = int(topic_id[1:])
        # Sudá čísla = mužský, lichá = ženský
        # T01 (1) = female, T02 (2) = male, T03 (3) = female, atd.
        if topic_num % 2 == 1:
            return CZECH_VOICES["female"]
        else:
            return CZECH_VOICES["male"]
    except:
        # Pokud se nepodaří určit, použij ženský hlas jako výchozí
        return CZECH_VOICES["female"]


def sanitize_filename(text: str) -> str:
    """Vytvoří bezpečný název souboru z textu"""
    # Převeď na malá písmena
    text = text.lower()
    # Nahraď problematické znaky
    replacements = {
        'ě': 'e', 'š': 's', 'č': 'c', 'ř': 'r', 'ž': 'z',
        'ý': 'y', 'á': 'a', 'í': 'i', 'é': 'e', 'ó': 'o',
        'ú': 'u', 'ů': 'u', 'ň': 'n', 'ť': 't', 'ď': 'd',
        ' ': '-', ',': '', '.': '', ':': '', ';': '',
        '/': '-', '\\': '-', '?': '', '!': '', '(': '', ')': '',
        '„': '', '"': '', "'": '', '–': '-', '—': '-'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Odstraň všechny ostatní ne-ASCII znaky (ponechá jen alfanumerické a pomlčky)
    text = ''.join(c if (c.isalnum() or c == '-') else '' for c in text)
    # Odstraň vícenásobné pomlčky
    while '--' in text:
        text = text.replace('--', '-')
    # Odstraň pomlčky na začátku a konci
    text = text.strip('-')
    return text


async def main_async():
    """Hlavní asynchronní funkce"""
    # Získej název souboru z argumentů nebo použij T01
    if len(sys.argv) > 1:
        topic_id = sys.argv[1].upper()
        if not topic_id.startswith("T"):
            topic_id = f"T{topic_id}"
    else:
        topic_id = "T01"
    
    # Najdi všechny audio-scénáře pro toto téma
    script_paths = find_audio_scripts(topic_id)
    
    if not script_paths:
        print(f"[ERROR] Zadny scenar nenalezen pro tema {topic_id}")
        print(f"  Hledano v: {AUDIO_SCRIPTS_DIR}")
        print(f"  Ocekavane soubory: {topic_id}.txt nebo {topic_id}_part*.txt")
        sys.exit(1)
    
    print(f"[OK] Nalezeno {len(script_paths)} scenar(u) pro tema {topic_id}")
    for i, path in enumerate(script_paths, 1):
        print(f"  {i}. {path.name}")
    
    # Načti informace o tématu
    topic_info = get_topic_info(topic_id)
    topic_title = topic_info.get("title", topic_id) if topic_info else topic_id
    topic_order = topic_info.get("order", int(topic_id[1:]) if len(topic_id) > 1 else 1) if topic_info else int(topic_id[1:]) if len(topic_id) > 1 else 1
    
    # Získej hlas - střídá se podle čísla tématu
    voice = os.getenv("EDGE_TTS_VOICE")
    
    if not voice:
        # Automaticky urči hlas podle čísla tématu
        voice = get_voice_for_topic(topic_id)
        voice_gender = "zeny" if voice == CZECH_VOICES["female"] else "muzsky"
        print(f"\n[OK] Automaticky vybrany hlas ({voice_gender}): {voice}")
    else:
        print(f"\n[OK] Pouzivam hlas z prostredi: {voice}")
    
    # Pokud uživatel chce vidět seznam hlasů
    if "--list-voices" in sys.argv:
        await list_czech_voices()
        return
    
    # Nastavení rychlosti a výšky hlasu (lze upravit podle potřeby)
    # Rychlost: +10% = rychleji, -10% = pomaleji
    # Výška: +10Hz = vyšší, -10Hz = nižší
    rate = os.getenv("EDGE_TTS_RATE", "+0%")
    pitch = os.getenv("EDGE_TTS_PITCH", "+0Hz")
    
    print(f"\nNastaveni:")
    print(f"  Hlas: {voice}")
    print(f"  Rychlost: {rate}")
    print(f"  Vyska: {pitch}")
    print()
    
    # Vytvoř bezpečný název tématu pro soubory
    safe_title = sanitize_filename(topic_title)
    
    # Vygeneruj audio pro každý scénář
    audio_files = []
    
    for i, script_path in enumerate(script_paths, 1):
        print(f"\n{'='*60}")
        print(f"Zpracovavani scenare {i}/{len(script_paths)}: {script_path.name}")
        print(f"{'='*60}")
        
        # Přečti scénář
        text = read_script(script_path)
        if not text:
            print(f"[WARNING] Preskakuji scenar {script_path.name} kvuli chybe")
            continue
        
        print(f"Text nacten ({len(text)} znaku, ~{len(text.split())} slov)")
        
        # Urči název souboru
        if len(script_paths) == 1:
            # Jeden soubor: "Otazka-X-Nazev-tematu.mp3"
            audio_filename = f"Otazka-{topic_order}-{safe_title}.mp3"
            audio_title = f"Otázka {topic_order} - {topic_title}"
            part_number = None
        else:
            # Více souborů: "Otazka-X-Nazev-tematu-cast-Y.mp3"
            # Zkus extrahovat číslo části z názvu souboru (např. "part1" -> 1)
            part_match = None
            if "_part" in script_path.stem.lower():
                try:
                    # Najdi číslo za "_part"
                    match = re.search(r'_part(\d+)', script_path.stem, re.IGNORECASE)
                    if match:
                        part_number = int(match.group(1))
                    else:
                        part_number = i
                except:
                    part_number = i
            else:
                part_number = i
            
            # Zkus extrahovat smysluplný název z obsahu
            content_title = extract_content_title(text)
            if content_title:
                # Použij extrahovaný název z obsahu
                audio_title = f"Otázka {topic_order} - {content_title}"
            else:
                # Fallback na generický název s číslem části
                audio_title = f"Otázka {topic_order} - {topic_title} (část {part_number})"
            
            audio_filename = f"Otazka-{topic_order}-{safe_title}-cast-{part_number}.mp3"
        
        output_path = AUDIO_OUTPUT_DIR / audio_filename
        
        # Vygeneruj audio
        success = await generate_audio_async(text, voice, output_path, rate, pitch)
        
        if success:
            print(f"[OK] Audio soubor vytvoren: {output_path}")
            audio_files.append({
                "src": f"assets/audio/{audio_filename}",
                "title": audio_title,
                "part": part_number if len(script_paths) > 1 else None
            })
        else:
            print(f"[ERROR] Nepodarilo se vygenerovat audio pro {script_path.name}")
    
    # Aktualizuj topic JSON s novými názvy souborů
    if audio_files and topic_info:
        update_topic_audio_reference(topic_id, topic_info, audio_files, topic_title, topic_order)
    
    # Shrnutí
    print(f"\n{'='*60}")
    if audio_files:
        print(f"[OK] Hotovo! Vytvoreno {len(audio_files)} audio souboru pro tema {topic_id}")
        for audio_file in audio_files:
            print(f"  - {audio_file['src']}")
    else:
        print(f"[ERROR] Nepodarilo se vytvorit zadne audio soubory")
        sys.exit(1)
    
    print(f"\nTip: Chcete-li pouzit jiny hlas, spustte:")
    print(f"  python scripts/generate_audio.py {topic_id} --list-voices")
    print(f"  A pak nastavte: $env:EDGE_TTS_VOICE='cs-CZ-JmenoNeural'")


def update_topic_audio_reference(topic_id: str, topic_info: dict, audio_files: list[dict], topic_title: str, topic_order: int):
    """
    Aktualizuje referenci na audio soubory v topic JSON
    
    Args:
        topic_id: ID tématu (např. "T01")
        topic_info: Data z topic JSON
        audio_files: Seznam slovníků s klíči "src", "title", "part" (volitelné)
        topic_title: Název tématu
        topic_order: Pořadí tématu
    """
    topic_json_path = PROJECT_ROOT / "data" / "topics" / f"{topic_id}.json"
    
    try:
        # Aktualizuj audio sekci
        if "audio" not in topic_info:
            topic_info["audio"] = {}
        
        # Pokud je jen jeden soubor, použij starý formát pro kompatibilitu
        if len(audio_files) == 1:
            topic_info["audio"]["src"] = audio_files[0]["src"]
            topic_info["audio"]["title"] = audio_files[0]["title"]
            if "transcript" in audio_files[0]:
                topic_info["audio"]["transcript"] = audio_files[0]["transcript"]
        else:
            # Pro více souborů použij pole
            topic_info["audio"]["files"] = audio_files
            topic_info["audio"]["title"] = f"Otázka {topic_order} - {topic_title}"
            # Pro kompatibilitu nastav první soubor jako hlavní
            if audio_files:
                topic_info["audio"]["src"] = audio_files[0]["src"]
        
        # Ulož aktualizovaný JSON
        with open(topic_json_path, "w", encoding="utf-8") as f:
            json.dump(topic_info, f, ensure_ascii=False, indent=2)
        
        print(f"[OK] Topic JSON aktualizovan: {topic_json_path}")
        if len(audio_files) == 1:
            print(f"  Audio src: {topic_info['audio']['src']}")
            print(f"  Audio title: {topic_info['audio']['title']}")
        else:
            print(f"  Pocet audio souboru: {len(audio_files)}")
            for i, audio_file in enumerate(audio_files, 1):
                part_info = f" (cast {audio_file.get('part', i)})" if audio_file.get('part') else ""
                print(f"    {i}. {audio_file['title']}{part_info}")
    except Exception as e:
        print(f"[WARNING] Nepodarilo se aktualizovat topic JSON: {e}")


def main():
    """Hlavní funkce - wrapper pro asynchronní kód"""
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\n\n[ERROR] Preruseno uzivatelem")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Neocekavana chyba: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

