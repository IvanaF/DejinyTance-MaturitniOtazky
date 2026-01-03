# PROMPT: Vytvoření audio-scénáře pro TTS (ElevenLabs)

## ÚKOL
Vytvoř finální audio-scénář pro TTS (text-to-speech) pro danou kapitolu z přiložených studijních podkladů (bodově psané materiály).

**Cíl:** Studijní audio pro maturitní přípravu v češtině – plynulé, přirozené, gramaticky správné, a přitom zachovávající 100 % obsahu.

---

## VSTUP

1. **Zdrojový text kapitoly** najdeš v projektu:
   - `data/materials/TXX_materials.json` (kde XX je číslo kapitoly)
   - Nebo v PDF / extrahovaných podkladech

2. **Rozdělení kapitoly na části:**
   - **VŽDY rozděl kapitolu na části, pokud materiály obsahují logicky oddělené sekce:**
     - Různé země nebo regiony (např. Pravek, Egypt, Mezopotamie)
     - Větší časové období nebo epochy
     - Výrazně odlišná témata nebo oblasti
   - Každá logická sekce = samostatný soubor (part1, part2, part3...)
   - Každá část by měla mít cca 7–12 minut poslechu (pokud je část příliš krátká, lze spojit s další)
   - Název souboru: `TXX_partY.txt` (např. `T01_part1.txt`, `T01_part2.txt`, `T01_part3.txt`)

---

## POVINNÉ POŽADAVKY

### 1) Obsah
- ✅ **Zachovej veškerý obsah:** žádný bod nesmí zmizet (jména, data, pojmy, souvislosti)
- ✅ **Nepřidávej nové informace** mimo podklady. Pouze převyprávěj přirozeně a propojuj věty
- ✅ **100% pokrytí** – všechny body z materiálů musí být zahrnuty

### 2) Formát pro TTS
- ✅ **Žádné odrážky** v hlavním textu
- ✅ **Žádné emoji** nebo speciální znaky
- ✅ **Spisovná čeština** – gramaticky správná, bez chyb
- ✅ **Klidný, neutrální tón učitele** – vhodný pro dlouhodobý poslech
- ✅ **Maturitní úroveň** – přiměřená složitost

### 3) Struktura textu
- ✅ **Jasně odděl témata** pomocí plynulých přechodů (Nyní… Dalším tématem… Přejdeme k…)
- ✅ **Pokud více částí:** jasně označ "ČÁST 1", "ČÁST 2" atd. na začátku každé části
- ✅ **Plynulé věty** – přirozeně mluvený text, ne seznamy

### 4) Gramatika a pravopis
- ✅ **Povinná kontrola gramatiky a pravopisu** – text musí být bez chyb
- ✅ **Správné skloňování** – všechny názvy, jména, data
- ✅ **Správná interpunkce** – čárky, tečky, uvozovky
- ✅ **Správné psaní čísel** – "před naším letopočtem", "našeho letopočtu"
- ✅ **Správné psaní vlastních jmen** – diakritika, velká písmena

### 5) Závěr
- ✅ **Kontrolní text na konci** – 3–8 vět stručně shrnujících, co bylo probráno
- ✅ **Formulace:** "Závěrem si připomeňme, co jsme v této části probrali..."
- ✅ **Bez přepisování odrážek** – pouze souvislý text

---

## VÝSTUP

### Formát souboru
- **Vždy jeden soubor pro každou logickou sekci:** `data/audio_scripts/TXX_partY.txt`
  - part1 = první logická sekce (např. Pravek)
  - part2 = druhá logická sekce (např. Egypt)
  - part3 = třetí logická sekce (např. Mezopotamie)
- **Pouze čistý mluvený text** – žádné nadpisy, komentáře, nebo markdown syntaxe
- **Připraveno přímo pro ElevenLabs** – lze okamžitě vložit

### Struktura souboru
```
[ČÁST 1 / ČÁST 2 - pokud je více částí]

[Plynulý mluvený text - celý obsah]

Závěrem si připomeňme, co jsme v této části probrali. [Kontrolní shrnutí 3-8 vět]
```

### Příklad názvu souboru
- `data/audio_scripts/T01_part1.txt` (Pravek)
- `data/audio_scripts/T01_part2.txt` (Egypt)
- `data/audio_scripts/T01_part3.txt` (Mezopotamie)
- Číslo tématu (T01) se vždy zachovává, části se označují part1, part2, part3...

---

## POSTUP PRACe

### Krok 1: Načtení materiálů
1. Načti `data/materials/TXX_materials.json`
2. Projdi všechny sekce a jejich obsah
3. Zjisti rozsah a složitost kapitoly

### Krok 2: Rozdělení na části (POVINNÉ pro logicky oddělené sekce)
- **VŽDY rozděl materiály na části podle logických sekcí v materiálech:**
  - Identifikuj hlavní sekce v materiálech (např. podle nadpisů "PRAVĚK", "EGYPT", "MEZOPOTÁMIE")
  - Každá logická sekce = samostatná část (part1, part2, part3...)
  - Pokud materiál obsahuje více zemí/regionů/témat, vytvoř pro každou část samostatný soubor
- Každá část by měla být logicky ucelená a obsahovat všechny související podsekce
- Příklad: T01 s sekcemi Pravek, Egypt, Mezopotamie → T01_part1.txt, T01_part2.txt, T01_part3.txt

### Krok 3: Tvorba textu
1. **Převeď všechny body na plynulý text:**
   - Odrážky → souvislé věty
   - Zkratky → plné názvy
   - Seznamy → přirozené výčty v textu

2. **Přidej plynulé přechody:**
   - "Nyní se zaměříme na..."
   - "Dalším tématem je..."
   - "Přejdeme k..."
   - "Důležité je také..."

3. **Zachovej všechny informace:**
   - Všechna data, jména, názvy
   - Všechny souvislosti a vztahy
   - Všechny technické termíny (s vysvětlením)

### Krok 4: Gramatická kontrola
**POVINNĚ zkontroluj:**
- ✅ Skloňování (všechny pády)
- ✅ Shoda podmětu s přísudkem
- ✅ Správné psaní čísel a dat
- ✅ Interpunkce (čárky, tečky)
- ✅ Velká písmena (vlastní jména)
- ✅ Diakritika (háčky, čárky)
- ✅ Správné tvary slov (např. "před naším letopočtem" vs "našeho letopočtu")

**Časté chyby k opravě:**
- "Harappská kultura" → správně podle kontextu
- "před naším letopočtem" vs "našeho letopočtu"
- Skloňování vlastních jmen (Ašóka, Ašóky, Ašókovi...)
- Shoda podmětu s přísudkem (kasty byly, kasta byla...)

### Krok 5: Závěr
- Přidej kontrolní shrnutí na konec
- Formulace: "Závěrem si připomeňme, co jsme v této části probrali..."
- 3–8 vět stručně, bez odrážek

### Krok 6: Systematická kontrola obsahu (POVINNÉ)

**PŘED uložením MUSÍŠ provést tuto systematickou kontrolu:**

**Používej nástroje k ověření:**
- Použij `grep` k vyhledání klíčových termínů v materiálech a jejich ověření ve skriptu
- Použij `read_file` k porovnání sekcí materiálů se skriptem
- Nezapomeň na detaily v závorkách, poznámkách a sekundárních informacích

1. **Kontrola pokrytí všech sekcí:**
   - [ ] Projdi každou sekci ze zdrojových materiálů (`TXX_materials.json`)
   - [ ] Pro každou sekci ověř pomocí grep/read_file, že všechny body jsou zahrnuty ve skriptu
   - [ ] Zkontroluj, že nechybí žádná podsekce, podbod nebo detail
   - [ ] Ověř všechny výčty (např. všechny druhy tanců, všechny typy pyramid, všichni bohové)

2. **Kontrola specifických detailů (sekce po sekci):**
   - [ ] Všechna data (roky, století, období) jsou uvedena správně - použij grep k ověření klíčových dat
   - [ ] Všechna jména osob (panovníci, umělci, bohové) jsou zahrnuta a správně skloňována - ověř každé jméno z materiálů
   - [ ] Všechna místa (města, regiony, řeky) jsou zmíněna - zkontroluj všechny geografické názvy
   - [ ] Všechna díla, stavby, artefakty jsou uvedena - ověř všechny konkrétní názvy děl/staveb
   - [ ] Všechny termíny a pojmy jsou vysvětleny nebo zahrnuty
   - [ ] Všechny druhy/třídy/kategorie (např. druhy tanců, typy pyramid) jsou kompletní - spočítej a ověř
   - [ ] Všechny detaily v závorkách nebo poznámkách jsou zahrnuty - nevynechávej žádné vedlejší informace

3. **Kontrola gramatiky a pravopisu:**
   - [ ] Správné skloňování všech vlastních jmen (např. Amenhotepa, Atona, Remislava Remislavského)
   - [ ] Správná shoda podmětu s přísudkem
   - [ ] Správné psaní čísel: "před naším letopočtem" vs "našeho letopočtu"
   - [ ] Opraveny chyby z materiálů (např. "palentologie" → "paleontologie", "jednotnou říší" → "jednotnou říši")
   - [ ] Diakritika u všech slov (háčky, čárky)
   - [ ] Velká písmena u vlastních jmen
   - [ ] Správná interpunkce (čárky před větami vedlejšími, tečky na konci vět)

4. **Kontrola formátu pro TTS:**
   - [ ] Žádné odrážky (•, -, a), b), c)) v hlavním textu
   - [ ] Žádné emoji nebo speciální znaky
   - [ ] Žádné markdown syntaxe (**, *, #, [])
   - [ ] Pouze plynulý mluvený text
   - [ ] Přirozené přechody mezi tématy

5. **Kontrola struktury:**
   - [ ] Úvodní věta je přítomna
   - [ ] Závěrečné shrnutí obsahuje 3–8 vět
   - [ ] Závěr začíná formulací: "Závěrem si připomeňme..."
   - [ ] Pokud více částí: každá část má označení "ČÁST 1", "ČÁST 2" atd.

6. **Finální cross-checking:**
   - [ ] Porovnej každou sekci materiálů se skriptem pomocí grep nebo ruční kontroly
   - [ ] Ověř klíčové detaily: všechna data, jména, místa, díla
   - [ ] Zkontroluj, že v závěru je zmíněno alespoň jedno klíčové téma z každé hlavní sekce

### Krok 7: Finální validace
- ✅ Je text plynulý a přirozený?
- ✅ Jsou všechny informace zahrnuty? (100% pokrytí ověřeno systematicky)
- ✅ Je text gramaticky správný? (všechny chyby opraveny)
- ✅ Je vhodný pro TTS? (žádné odrážky, emoji, markdown)
- ✅ Má správnou délku? (7–12 minut na část, cca 1500–2500 slov)

---

## PŘÍKLAD STRUKTURY

### Pro jednu část:
```
Vítejte u audio-lekce o [téma]. [Úvodní věta].

[Plynulý text s veškerým obsahem - přirozeně propojené věty, žádné odrážky]

Závěrem si připomeňme, co jsme v této lekci probrali. [Shrnutí 3-8 vět].
```

### Pro více částí:
**Soubor 1: `TXX_part1.txt` (např. Pravek)**
```
Vítejte u první části audio-lekce o [hlavní téma tématu]. V této části se zaměříme na [téma části 1, např. pravěk].

[Obsah části 1 - všechny sekce související s částí 1]

Závěrem si připomeňme, co jsme v této části probrali. [Shrnutí pouze obsahu části 1].
```

**Soubor 2: `TXX_part2.txt` (např. Egypt)**
```
Vítejte u druhé části audio-lekce o [hlavní téma tématu]. V této části se zaměříme na [téma části 2, např. Egypt].

[Obsah části 2 - všechny sekce související s částí 2]

Závěrem si připomeňme, co jsme v této části probrali. [Shrnutí pouze obsahu části 2].
```

**Soubor 3: `TXX_part3.txt` (např. Mezopotamie)**
```
Vítejte u třetí části audio-lekce o [hlavní téma tématu]. V této části se zaměříme na [téma části 3, např. Mezopotámii].

[Obsah části 3 - všechny sekce související s částí 3]

Závěrem si připomeňme, co jsme v této části probrali. [Shrnutí pouze obsahu části 3].
```

---

## DŮLEŽITÉ POZNÁMKY

1. **Systematická kontrola je POVINNÁ před uložením**
   - ❌ NEUkládej skript bez provedení systematické kontroly (Krok 6)
   - ✅ Skript musí být perfektní na první pokus - žádné chybějící informace, žádné gramatické chyby
   - ✅ Projdi každou sekci materiálů a ověř 100% pokrytí
   - ✅ Zkontroluj všechny specifické detaily (jména, data, místa, díla)

2. **Jeden soubor = jeden text pro ElevenLabs**
   - Není potřeba vytvářet separátní MD a TXT soubory
   - Jeden TXT soubor obsahuje vše

3. **Gramatická kontrola je součástí procesu**
   - Neukládej text s chybami
   - Oprav všechny chyby nalezené v materiálech (např. "palentologie" → "paleontologie")
   - Správné skloňování je kritické

4. **Zachovej všechny informace**
   - Pokud něco chybí, vrať se k materiálům a doplň
   - Lepší delší text než chybějící informace
   - Všechny detaily v závorkách nebo poznámkách musí být zahrnuty

5. **Přirozenost před formálností**
   - Text má znít jako mluvené slovo
   - Ale stále spisovně a gramaticky správně

---

## KONTROLA KVALITY

**Tato kontrola MUSÍ být provedena před uložením souboru.**

Postupuj podle systematické kontroly v Kroku 6 a ověř:

### Obsahová kontrola
- [ ] Projdi každou sekci materiálů a ověř, že všechny body jsou zahrnuty
- [ ] Zkontroluj všechny data, jména, místa, díla, termíny
- [ ] Ověř, že nechybí žádné detaily z poznámek nebo závorek
- [ ] Použij grep nebo podobný nástroj k ověření klíčových termínů

### Gramatická a formátová kontrola
- [ ] Gramatika a pravopis jsou správné (všechny chyby opraveny)
- [ ] Skloňování všech vlastních jmen je správné
- [ ] Interpunkce je správná
- [ ] Vlastní jména mají správnou diakritiku a velká písmena
- [ ] Data jsou správně formulovaná ("před naším letopočtem" vs "našeho letopočtu")

### Formát pro TTS
- [ ] Text je plynulý (žádné odrážky v hlavním textu)
- [ ] Žádné emoji nebo speciální znaky
- [ ] Žádné markdown syntaxe
- [ ] Text má přirozené přechody mezi tématy

### Struktura
- [ ] Úvodní věta je přítomna
- [ ] Závěr obsahuje kontrolní shrnutí (3–8 vět)
- [ ] Závěr začíná "Závěrem si připomeňme..."
- [ ] Délka je vhodná (7–12 minut na část, cca 1500–2500 slov)

**⚠️ NEPOKRAČUJ k uložení, dokud všechny body nejsou splněny!**

---

## PŘÍKLAD POUŽITÍ

**Vstup:** `data/materials/T01_materials.json` (obsahuje sekce: PRAVĚK, EGYPT, MEZOPOTÁMIE)

**Výstup:** 
- `data/audio_scripts/T01_part1.txt` (obsahuje všechny sekce související s pravěkem)
- `data/audio_scripts/T01_part2.txt` (obsahuje všechny sekce související s Egyptem)
- `data/audio_scripts/T01_part3.txt` (obsahuje všechny sekce související s Mezopotámií)

**Obsah každého souboru:** Pouze čistý mluvený text, připravený pro ElevenLabs, gramaticky správný, s kontrolním shrnutím na konci pouze obsahu dané části.

---

**Konec promptu**

