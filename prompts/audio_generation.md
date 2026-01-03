# PROMPT: Generování audio souborů pro témata

## ÚKOL
Vygeneruj audio soubor(y) z audio-scénáře pro dané téma pomocí Edge TTS (zdarma, bez API klíče).

**Cíl:** Vytvořit MP3 audio soubor(y) s přirozeným českým hlasem pro studijní materiály. Skript automaticky detekuje jeden nebo více scénářů a vygeneruje odpovídající audio soubory se smysluplnými názvy založenými na obsahu.

---

## PŘED POUŽITÍM

### 1. Instalace závislostí
```powershell
pip install edge-tts
```

### 2. Ověření, že máte audio-scénář
- Audio-scénář může být buď:
  - **Jeden soubor:** `data/audio_scripts/TXX.txt`
  - **Více souborů:** `data/audio_scripts/TXX_part1.txt`, `TXX_part2.txt`, `TXX_part3.txt`, ...
- Scénář musí být připraven podle `prompts/audioscript.md`
- Skript automaticky detekuje, zda existuje jeden nebo více souborů

---

## POSTUP GENEROVÁNÍ AUDIA

### Krok 1: Spuštění skriptu

```powershell
python scripts/generate_audio.py TXX
```

Kde `TXX` je ID tématu (např. `T01`, `T02`, `T03`).

**Příklad:**
```powershell
python scripts/generate_audio.py T01
python scripts/generate_audio.py T02
```

### Krok 2: Co skript dělá automaticky

1. **Najde audio-scénáře** v `data/audio_scripts/`:
   - Nejdřív hledá `TXX.txt` (jeden soubor)
   - Pokud neexistuje, hledá `TXX_part*.txt` (více souborů)
2. **Načte informace o tématu** z `data/topics/TXX.json` (název, pořadí)
3. **Automaticky vybere hlas:**
   - T01, T03, T05, ... (lichá čísla) = **ženský hlas** (VlastaNeural)
   - T02, T04, T06, ... (sudá čísla) = **mužský hlas** (AntoninNeural)
4. **Vygeneruje audio soubory:**
   - **Jeden scénář:** `Otazka-X-nazev-tematu.mp3`
   - **Více scénářů:** `Otazka-X-nazev-tematu-cast-1.mp3`, `Otazka-X-nazev-tematu-cast-2.mp3`, ...
5. **Automaticky extrahuje smysluplné názvy** z obsahu každého scénáře (např. "Pravěk", "Egypt", "Mezopotámie")
6. **Automaticky aktualizuje** `data/topics/TXX.json` s novými názvy souborů a názvy částí založenými na obsahu

### Krok 3: Výstup

- **Jeden audio soubor:** `assets/audio/Otazka-X-nazev-tematu.mp3`
- **Nebo více audio souborů:** `assets/audio/Otazka-X-nazev-tematu-cast-1.mp3`, `cast-2.mp3`, ...
- **Aktualizovaný JSON:** `data/topics/TXX.json` (sekce `audio`)

---

## POKROČILÉ NASTAVENÍ

### Změna hlasu (přepsání automatického výběru)

```powershell
# Použít mužský hlas
$env:EDGE_TTS_VOICE='cs-CZ-AntoninNeural'

# Použít ženský hlas
$env:EDGE_TTS_VOICE='cs-CZ-VlastaNeural'

# Pak spusť skript
python scripts/generate_audio.py TXX
```

### Úprava rychlosti řeči

```powershell
# Rychleji (+10% až +20%)
$env:EDGE_TTS_RATE='+10%'

# Pomaleji (-10% až -20%)
$env:EDGE_TTS_RATE='-10%'

# Pak spusť skript
python scripts/generate_audio.py TXX
```

### Úprava výšky hlasu

```powershell
# Vyšší hlas
$env:EDGE_TTS_PITCH='+10Hz'

# Nižší hlas
$env:EDGE_TTS_PITCH='-10Hz'

# Pak spusť skript
python scripts/generate_audio.py TXX
```

### Zobrazení dostupných hlasů

```powershell
python scripts/generate_audio.py TXX --list-voices
```

---

## STRUKTURA NÁZVŮ SOUBORŮ

### Formát názvu audio souboru:

**Jeden soubor:**
```
Otazka-{poradi}-{nazev-tematu}.mp3
```

**Více souborů:**
```
Otazka-{poradi}-{nazev-tematu}-cast-{cislo}.mp3
```

**Příklady:**
- Jeden soubor: `Otazka-1-pravek-egypt-mezopotamie.mp3`
- Více souborů:
  - `Otazka-1-pravek-egypt-mezopotamie-cast-1.mp3`
  - `Otazka-1-pravek-egypt-mezopotamie-cast-2.mp3`
  - `Otazka-1-pravek-egypt-mezopotamie-cast-3.mp3`

### Aktualizace v topic JSON:

Skript automaticky aktualizuje `data/topics/TXX.json`:

**Jeden audio soubor:**
```json
{
  "audio": {
    "title": "Otázka 1 - PRAVĚK, EGYPT, MEZOPOTÁMIE",
    "src": "assets/audio/Otazka-1-pravek-egypt-mezopotamie.mp3",
    "transcript": "..."
  }
}
```

**Více audio souborů:**
```json
{
  "audio": {
    "title": "Otázka 1 - PRAVĚK, EGYPT, MEZOPOTÁMIE",
    "src": "assets/audio/Otazka-1-pravek-egypt-mezopotamie-cast-1.mp3",
    "files": [
      {
        "src": "assets/audio/Otazka-1-pravek-egypt-mezopotamie-cast-1.mp3",
        "title": "Otázka 1 - Pravěk",
        "part": 1,
        "transcript": "Transcript for part 1 (optional)."
      },
      {
        "src": "assets/audio/Otazka-1-pravek-egypt-mezopotamie-cast-2.mp3",
        "title": "Otázka 1 - Egypt",
        "part": 2,
        "transcript": "Transcript for part 2 (optional)."
      },
      {
        "src": "assets/audio/Otazka-1-pravek-egypt-mezopotamie-cast-3.mp3",
        "title": "Otázka 1 - Mezopotámie",
        "part": 3,
        "transcript": "Transcript for part 3 (optional)."
      }
    ]
  }
}
```

**Poznámka k názvům částí:**
- Názvy částí jsou automaticky extrahovány z obsahu scénáře
- Skript hledá fráze jako "zaměříme na", "části se zaměříme na" a extrahuje téma
- Namísto generických názvů "(část 1)", "(část 2)" se používají smysluplné názvy založené na obsahu
- Příklady: "Pravěk", "Egypt", "Mezopotámie", "Indie", atd.

---

## STŘÍDÁNÍ HLASŮ

Skript automaticky střídá hlasy mezi tématy:

| Téma | Pořadí | Hlas | Voice ID |
|------|--------|------|----------|
| T01  | 1      | Ženský | cs-CZ-VlastaNeural |
| T02  | 2      | Mužský | cs-CZ-AntoninNeural |
| T03  | 3      | Ženský | cs-CZ-VlastaNeural |
| T04  | 4      | Mužský | cs-CZ-AntoninNeural |
| ...  | ...    | ...   | ... |

**Logika:** Lichá čísla = ženský hlas, sudá čísla = mužský hlas

---

## KONTROLA KVALITY

Po vygenerování audio zkontrolujte:

- [ ] Audio soubor byl vytvořen v `assets/audio/`
- [ ] Název souboru odpovídá formátu `Otazka-X-nazev-tematu.mp3`
- [ ] Topic JSON byl aktualizován (`audio.src` a `audio.title`)
- [ ] Audio přehrává správně v prohlížeči
- [ ] Hlas odpovídá očekávání (střídá se podle čísla tématu)

---

## ŘEŠENÍ PROBLÉMŮ

### Chyba: "Zadny scenar nenalezen"
- Ověřte, že existuje buď:
  - `data/audio_scripts/TXX.txt` (jeden soubor), nebo
  - `data/audio_scripts/TXX_part*.txt` (více souborů)
- Zkontrolujte, že ID tématu je správné (např. `T01`, ne `T1`)
- Ujistěte se, že soubory mají správné názvy (např. `T01_part1.txt`, ne `T01-part1.txt`)

### Chyba: "Nepodarilo se nacist topic JSON"
- Ověřte, že existuje `data/topics/TXX.json`
- Zkontrolujte, že JSON je validní

### Audio zní špatně nebo příliš rychle/pomalu
- Upravte rychlost pomocí `$env:EDGE_TTS_RATE`
- Zkuste jiný hlas pomocí `$env:EDGE_TTS_VOICE`

### Chcete použít jiný hlas než automaticky vybraný
- Nastavte `$env:EDGE_TTS_VOICE` před spuštěním skriptu
- Nebo upravte logiku v `scripts/generate_audio.py` (funkce `get_voice_for_topic`)

---

## PŘÍKLADY POUŽITÍ

### Základní použití:
```powershell
# Vygeneruj audio pro T01
python scripts/generate_audio.py T01

# Vygeneruj audio pro T02
python scripts/generate_audio.py T02
```

### S vlastním nastavením:
```powershell
# Použij mužský hlas a rychlejší řeč
$env:EDGE_TTS_VOICE='cs-CZ-AntoninNeural'
$env:EDGE_TTS_RATE='+15%'
python scripts/generate_audio.py T01
```

### Hromadné generování (PowerShell):
```powershell
# Vygeneruj audio pro T01 až T05
1..5 | ForEach-Object {
    $topicId = "T{0:D2}" -f $_
    python scripts/generate_audio.py $topicId
}
```

---

## TECHNICKÉ DETAILY

- **Knihovna:** edge-tts (Microsoft Edge TTS)
- **Formát výstupu:** MP3
- **Kvalita:** Vysoká, přirozený český hlas
- **Náklady:** Zcela zdarma, bez API klíče
- **Rychlost:** ~1-2 minuty pro 2000 slov

---

## POZNÁMKY

1. **Edge TTS je zdarma** - nevyžaduje API klíč ani registraci
2. **Automatické střídání hlasů** - zajišťuje variaci mezi tématy
3. **Automatická aktualizace JSON** - skript sám aktualizuje referenci v topic JSON
4. **Podpora diakritiky** - správně zpracovává české znaky v názvech souborů
5. **Podpora více scénářů** - automaticky detekuje a zpracuje více audio-scénářů pro jedno téma
6. **Číslování částí** - automaticky extrahuje čísla částí z názvů souborů (např. `_part1`, `_part2`)
7. **Smysluplné názvy částí** - automaticky extrahuje názvy z obsahu scénáře (např. "Pravěk", "Egypt", "Mezopotámie") místo generických názvů "(část 1)", "(část 2)"
8. **Podpora přepisů pro každou část** - každá část může mít svůj vlastní přepis (transcript) zobrazený na webu
7. **Smysluplné názvy částí** - automaticky extrahuje názvy z obsahu scénáře (např. "Pravěk", "Egypt", "Mezopotámie") místo generických názvů "(část 1)", "(část 2)"
8. **Podpora přepisů pro každou část** - každá část může mít svůj vlastní přepis (transcript) zobrazený na webu

---

## DALŠÍ KROKY PO VYGENEROVÁNÍ

1. **Ověřte audio** - přehrajte si ho a zkontrolujte kvalitu
2. **Přidejte přepis** - pokud chcete, můžete přidat přepis do `audio.transcript` v topic JSON
3. **Testujte na webu** - otevřete topic stránku a ověřte, že audio přehrává správně

---

**Vytvořeno:** 2025-01-03  
**Poslední aktualizace:** 2025-01-03  
**Verze:** 2.0 (podpora více scénářů)

