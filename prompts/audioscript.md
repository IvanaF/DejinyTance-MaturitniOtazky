# PROMPT: Vytvoření audio-scénáře pro TTS (ElevenLabs)

## ÚKOL
Vytvoř finální audio-scénář pro TTS (text-to-speech) pro danou kapitolu z přiložených studijních podkladů (bodově psané materiály).

**Cíl:** Studijní audio pro maturitní přípravu v češtině – plynulé, přirozené, gramaticky správné, a přitom zachovávající 100 % obsahu.

---

## VSTUP

1. **Zdrojový text kapitoly** najdeš v projektu:
   - `data/materials/TXX_materials.json` (kde XX je číslo kapitoly)
   - Nebo v PDF / extrahovaných podkladech

2. **Pokud je kapitola dlouhá nebo obsahuje více témat:**
   - Rozděl ji na části (ČÁST 1/2/3) tak, aby každá část měla cca 7–12 minut poslechu
   - Každá část = samostatný soubor

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
- **Jeden soubor** pro každou část: `data/audio_scripts/TXX_partY.txt`
- Pokud je jen jedna část: `data/audio_scripts/TXX.txt`
- **Pouze čistý mluvený text** – žádné nadpisy, komentáře, nebo markdown syntaxe
- **Připraveno přímo pro ElevenLabs** – lze okamžitě vložit

### Struktura souboru
```
[ČÁST 1 / ČÁST 2 - pokud je více částí]

[Plynulý mluvený text - celý obsah]

Závěrem si připomeňme, co jsme v této části probrali. [Kontrolní shrnutí 3-8 vět]
```

### Příklad názvu souboru
- `data/audio_scripts/T02_part1.txt` (pokud je rozděleno)
- `data/audio_scripts/T02.txt` (pokud je jedna část)

---

## POSTUP PRACe

### Krok 1: Načtení materiálů
1. Načti `data/materials/TXX_materials.json`
2. Projdi všechny sekce a jejich obsah
3. Zjisti rozsah a složitost kapitoly

### Krok 2: Rozdělení (pokud potřeba)
- Pokud text bude delší než ~12 minut poslechu → rozděl na části
- Každá část by měla být logicky ucelená (např. podle zemí, období, témat)

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

### Krok 6: Finální kontrola
- ✅ Je text plynulý a přirozený?
- ✅ Jsou všechny informace zahrnuty?
- ✅ Je text gramaticky správný?
- ✅ Je vhodný pro TTS (žádné odrážky, emoji)?
- ✅ Má správnou délku (7–12 minut na část)?

---

## PŘÍKLAD STRUKTURY

### Pro jednu část:
```
Vítejte u audio-lekce o [téma]. [Úvodní věta].

[Plynulý text s veškerým obsahem - přirozeně propojené věty, žádné odrážky]

Závěrem si připomeňme, co jsme v této lekci probrali. [Shrnutí 3-8 vět].
```

### Pro více částí:
**Soubor 1: `TXX_part1.txt`**
```
Vítejte u audio-lekce o [téma]. Tato lekce je rozdělena do [počet] částí. V první části se zaměříme na [téma části 1].

[Obsah části 1]

Závěrem si připomeňme, co jsme v této části probrali. [Shrnutí].
```

**Soubor 2: `TXX_part2.txt`**
```
Vítejte u druhé části audio-lekce o [téma]. V této části se zaměříme na [téma části 2].

[Obsah části 2]

Závěrem si připomeňme, co jsme v této části probrali. [Shrnutí].
```

---

## DŮLEŽITÉ POZNÁMKY

1. **Jeden soubor = jeden text pro ElevenLabs**
   - Není potřeba vytvářet separátní MD a TXT soubory
   - Jeden TXT soubor obsahuje vše

2. **Gramatická kontrola je součástí procesu**
   - Neukládej text s chybami
   - Vždy zkontroluj před uložením

3. **Zachovej všechny informace**
   - Pokud něco chybí, vrať se k materiálům
   - Lepší delší text než chybějící informace

4. **Přirozenost před formálností**
   - Text má znít jako mluvené slovo
   - Ale stále spisovně a gramaticky správně

---

## KONTROLA KVALITY

Před uložením zkontroluj:
- [ ] Všechny body z materiálů jsou zahrnuty
- [ ] Text je plynulý (žádné odrážky v hlavním textu)
- [ ] Gramatika a pravopis jsou správné
- [ ] Interpunkce je správná
- [ ] Vlastní jména jsou správně napsaná (diakritika, velká písmena)
- [ ] Data jsou správně formulovaná
- [ ] Text má přirozené přechody mezi tématy
- [ ] Závěr obsahuje kontrolní shrnutí
- [ ] Délka je vhodná (7–12 minut na část)
- [ ] Text je připraven pro TTS (žádné emoji, markdown syntaxe)

---

## PŘÍKLAD POUŽITÍ

**Vstup:** `data/materials/T03_materials.json`

**Výstup:** 
- `data/audio_scripts/T03.txt` (pokud jedna část)
- NEBO `data/audio_scripts/T03_part1.txt` a `data/audio_scripts/T03_part2.txt` (pokud rozděleno)

**Obsah souboru:** Pouze čistý mluvený text, připravený pro ElevenLabs, gramaticky správný, s kontrolním shrnutím na konci.

---

**Konec promptu**

