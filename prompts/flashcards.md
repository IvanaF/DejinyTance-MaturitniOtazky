# PROMPT: Vytváření flashcards pro studijní materiály

## ÚKOL
Vytvoř kvalitní flashcards (studijní kartičky) pro kapitolu z přiložených studijních materiálů.

**Cíl:** Studijní kartičky pro maturitní přípravu v češtině – faktické, konzistentní, založené výhradně na poskytnutých materiálech.

---

## VSTUP

1. **Zdrojový text kapitoly** najdeš v projektu:
   - `data/materials/TXX_materials.json` (kde XX je číslo kapitoly)
   - Tento soubor obsahuje sekce s obsahem kapitoly

2. **Výstupní soubor:**
   - `data/flashcards/TXX_flashcards.json`
   - Název souboru musí odpovídat formátu: `TXX_flashcards.json` (např. `T02_flashcards.json`)

---

## PŘÍSNÁ PRAVIDLA (MUSÍ BÝT DODRŽENA)

### 1) Obsah

- ✅ **POUZE informace z materiálů:** Každá faktická informace v kartičce MUSÍ být přímo přítomna v poskytnutých materiálech
- ❌ **NEPŘIDÁVEJ:** Žádné doplňování, vyvozování, interpretace, zjednodušování nebo obohacování obsahu
- ❌ **NEDOMAÝŠLEJ:** Pokud je něco v materiálech nejasné nebo nejednoznačné, NEVYTVÁŘEJ pro to kartičku
- ✅ **100% dohledatelnost:** Každý fakt v kartičce musí být přímo dohledatelný v materiálech

### 2) Jazyk a styl

- ✅ **Čeština:** Všechny kartičky v češtině
- ✅ **Faktický styl:** Vhodný pro zkoušky, stručný, jasný
- ✅ **Spisovná čeština:** Gramaticky správná, bez chyb

### 3) Formát JSON

**Struktura souboru:**
```json
{
  "flashcards": [
    {
      "q": "Text otázky?",
      "a": "Text odpovědi."
    }
  ]
}
```

**Důležité:**
- Pole `q` = otázka (question)
- Pole `a` = odpověď (answer)
- Celý soubor musí být validní JSON
- Uvozovky v textu musí být escapovány pomocí `\"` (ne Unicode uvozovky „")

---

## PRAVIDLA PRO TVORBU KARTIČEK

### Počet kartiček

- **Minimum:** 15 kartiček na kapitolu
- **Doporučeno:** 20–30 kartiček na kapitolu
- **Maximum:** 35 kartiček na kapitolu (podle hustoty obsahu)

Počet závisí na:
- Hustotě informací v kapitole
- Důležitosti faktů pro zkoušku
- Komplexitě tématu

### Typy kartiček

Každá kartička musí reprezentovat **JEDEN fakt** nebo těsně související sadu faktů.

**Povolené typy:**
1. **Definition (definice)** – "Co je X?", "Co znamená X?"
2. **List (seznam)** – "Jaké jsou čtyři kasty?", "Jaké jsou druhy tance?"
3. **Timeline (časová osa)** – "Kdy vznikl X?", "V kterém období probíhal Y?"
4. **Person (osoba)** – "Kdo byl X?", "Kdo vytvořil Y?"
5. **Concept (pojem)** – "Co jsou mudry?", "Co znamená natya?"
6. **Classification (klasifikace)** – "Jaké jsou typy X?", "Do jakých kategorií se dělí Y?"

### Formulace otázek

✅ **DOBRÉ příklady:**
- "Kdy vznikla Harappská kultura a kdy byl její rozkvět?"
- "Jaké jsou čtyři základní kasty v indické společnosti?"
- "Kdo byl nejvýznamnější indický panovník a co začal šířit?"
- "Co jsou mudry v indickém tanci?"
- "Kdy vznikl žánr Pekingská (Čínská) opera a kde?"

❌ **ŠPATNÉ příklady (vyvaruj se):**
- Složené nebo vícedílné otázky, které se ptají na nesouvisející fakta
- Otázky, které vyžadují vyvozování nebo interpretaci
- Otázky na nejasné nebo nejednoznačné informace z materiálů

### Formulace odpovědí

- ✅ **Stručné a úplné:** Odpověď by měla být stručná, ale obsahovat všechny relevantní informace
- ✅ **Přímo z materiálů:** Používej přesně formulace z materiálů
- ✅ **Pro víceřádkové odpovědi:** Používej `\n` pro nové řádky (např. v seznamech)
- ✅ **Zachovej čísla a data:** Přesně jak jsou v materiálech

**Příklady správných odpovědí:**

Jednoduchá odpověď:
```json
{
  "q": "Jaký je nejznámější indický hudební nástroj?",
  "a": "Sitár."
}
```

Seznam (víceřádkový):
```json
{
  "q": "Jaké jsou čtyři základní kasty v indické společnosti?",
  "a": "1. brahmáni – kněží, intelektuálové\n2. kšatrijové – panovníci, bojovníci\n3. vaišjové – zemědělci, rolníci\n4. šúdrové – sluhové, dělníci"
}
```

Komplexní odpověď:
```json
{
  "q": "Kdo tančil v Pekingské opeře a jaká jsou témata her?",
  "a": "Tanečníci pouze muži. Témata: a) občanská – společenská, rodinná\nb) vojenská – válečná, loupežnická\nVšechny hry končí šťastně."
}
```

---

## POSTUP PŘI VYTVÁŘENÍ FLASHCARDS

### Krok 1: Prostudování materiálů

1. Přečti si celý soubor `data/materials/TXX_materials.json`
2. Identifikuj klíčové informace:
   - **Data a časové údaje** (kdy vzniklo, kdy probíhalo)
   - **Osoby** (kdo byl, kdo vytvořil)
   - **Pojmy a definice** (co je, co znamená)
   - **Místa a geografie** (kde se nachází, odkud pochází)
   - **Seznamy a klasifikace** (jaké jsou typy, jak se dělí)
   - **Charakteristiky a popisy** (co charakterizuje, co je typické)

### Krok 2: Vytvoření seznamu témat

Vytvoř seznam hlavních témat pro kartičky podle sekcí v materiálech:
- Historie (období, letopočty, události)
- Náboženství (druhy, zakladatelé, hlavní myšlenky)
- Umění (druhy, představitelé, charakteristiky)
- Literatura (díla, autoři, význam)
- Hudba (nástroje, druhy, charakteristiky)
- Tanec (druhy, představitelé, techniky, školy)
- Architektura (stavební prvky, významné památky)
- Divadlo (druhy, charakteristiky, představitelé)

### Krok 3: Vytváření kartiček

Pro každé téma vytvoř 2–5 kartiček různých typů:

**Prioritní fakta:**
- Data a časové údaje (kdy vzniklo, kdy probíhalo)
- Osoby a jejich význam (kdo, co vytvořil)
- Definice a pojmy (co je, co znamená)
- Seznamy (jaké jsou typy, kategorie)
- Charakteristiky (co je typické, co charakterizuje)

**Doporučený rozklad:**
- 30–40% kartiček: Data a časové údaje
- 20–30% kartiček: Pojmy a definice
- 15–25% kartiček: Osoby
- 15–25% kartiček: Seznamy a klasifikace
- 10–15% kartiček: Charakteristiky a popisy

### Krok 4: Kontrola kvality

Pro každou kartičku zkontroluj:

- ✅ **Je otázka jasně formulována?** – Jednoduchá, srozumitelná, vhodná pro samostudium
- ✅ **Je odpověď přímo v materiálech?** – Můžeš najít přesně tuto informaci v `TXX_materials.json`?
- ✅ **Je kartička faktická?** – Žádné vyvozování, pouze fakta
- ✅ **Je kartička užitečná pro zkoušku?** – Pokrývá důležitou informaci?
- ✅ **Je JSON formát správný?** – Validní JSON syntax, escapované uvozovky

### Krok 5: Vytvoření souboru

1. Vytvoř soubor `data/flashcards/TXX_flashcards.json`
2. Použij správnou JSON strukturu s polem `flashcards`
3. Ověř validitu JSON (např. pomocí JSON validátoru)

---

## PŘÍKLADY KVALITNÍCH FLASHCARDS

### Příklad 1: Otázka na datum a časové období
```json
{
  "q": "Kdy vznikla Harappská kultura a kdy byl její rozkvět?",
  "a": "Vznik kolem roku 3000 př. n. l., rozkvět 2600–1900 př. n. l."
}
```

### Příklad 2: Otázka na osobu
```json
{
  "q": "Kdo byl nejvýznamnější indický panovník a co začal šířit?",
  "a": "Král Ašóka, začal šířit a propagovat buddhismus."
}
```

### Příklad 3: Otázka na seznam
```json
{
  "q": "Jaké jsou čtyři základní kasty v indické společnosti?",
  "a": "1. brahmáni – kněží, intelektuálové\n2. kšatrijové – panovníci, bojovníci\n3. vaišjové – zemědělci, rolníci\n4. šúdrové – sluhové, dělníci"
}
```

### Příklad 4: Otázka na pojem/definici
```json
{
  "q": "Co jsou mudry v indickém tanci?",
  "a": "Složité pohyby a gesta rukou, paží."
}
```

### Příklad 5: Otázka na charakteristiku
```json
{
  "q": "Kdo tančil v Pekingské opeře a jaká jsou témata her?",
  "a": "Tanečníci pouze muži. Témata: a) občanská – společenská, rodinná\nb) vojenská – válečná, loupežnická\nVšechny hry končí šťastně."
}
```

### Příklad 6: Otázka na časové období s charakteristikou
```json
{
  "q": "Které období se nazývá \"zlatý věk Číny\"?",
  "a": "Dynastie Tchang (7.–10. stol. n. l.)."
}
```

---

## FINÁLNÍ KONTROLA (POVINNĚ PŘED VÝSTUPEM)

Před vytvořením finálního souboru zkontroluj:

### Kontrola obsahu
- ✅ **Jsou VŠECHNY odpovědi 100% přítomny v materiálech?**
- ✅ **Nejsou v kartičkách žádné externí fakta?**
- ✅ **Pokrývají kartičky klíčové informace z kapitoly?**

### Kontrola formátu
- ✅ **Je JSON validní?** (ověř pomocí JSON validátoru)
- ✅ **Jsou uvozovky správně escapovány?** (použití `\"` místo Unicode uvozovek)
- ✅ **Je struktura správná?** (pole `flashcards` obsahuje pole objektů s `q` a `a`)
- ✅ **Je počet kartiček vhodný?** (15–35 kartiček)

### Kontrola jazyka
- ✅ **Jsou všechny kartičky v češtině?**
- ✅ **Je gramatika správná?**
- ✅ **Je styl faktický a vhodný pro zkoušku?**

### Kontrola kvality
- ✅ **Jsou otázky jasné a srozumitelné?**
- ✅ **Jsou odpovědi úplné a přesné?**
- ✅ **Reprezentuje každá kartička jeden fakt nebo těsně související fakta?**

---

## TECHNICKÉ POZNÁMKY

### Umístění souboru
- Soubor musí být uložen v: `data/flashcards/TXX_flashcards.json`
- Název souboru musí přesně odpovídat formátu (např. `T02_flashcards.json`)

### Integrace s projektem
- Flashcardy se načítají automaticky pomocí `topic-loader.js`
- V souboru tématu (`data/topics/TXX.json`) se flashcards odkazují pomocí pole `flashcardSource`
- Formát: `"flashcardSource": "data/flashcards/TXX_flashcards.json"`

### Escapování v JSON
- Uvozovky v textu musí být escapovány: `\"`
- Nové řádky v textu: `\n`
- Příklad: `"Které období se nazývá \"zlatý věk Číny\"?"`

---

## SHRNUTÍ KLÍČOVÝCH PRAVIDEL

1. ✅ **POUZE fakta z materiálů** – žádné doplňování nebo vyvozování
2. ✅ **15–35 kartiček** na kapitolu (podle hustoty obsahu)
3. ✅ **Jeden fakt na kartičku** (nebo těsně související fakta)
4. ✅ **Čeština, faktický styl** – vhodné pro zkoušky
5. ✅ **Validní JSON formát** – správná struktura, escapované uvozovky
6. ✅ **Přímo dohledatelné** – každý fakt musí být přímo v materiálech

---

**POZOR:** Pokud máš pochybnosti o jakémkoli faktu, NEVYTVÁŘEJ pro něj kartičku. Lepší méně kartiček, ale všechny 100% založené na materiálech.

