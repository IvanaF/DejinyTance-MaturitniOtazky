# Průvodce škálováním - Přidávání nových témat

Tento dokument popisuje, jak přidat nová témata do studijní platformy.

## Struktura souboru tématu

Každé téma má vlastní JSON soubor v `data/topics/` s názvem `TXX.json`, kde `XX` je číslo tématu (např. `T01.json`, `T02.json`).

### Šablona souboru

Použijte `data/topics/_TEMPLATE.json` jako základ pro nové téma.

## Povinná pole

- `id` - Unikátní identifikátor (např. "T01", "T02")
- `order` - Pořadové číslo pro řazení (1, 2, 3, ...)
- `title` - Název tématu
- `materials` - Studijní materiály

## Volitelná pole

- `image` - Cesta k obrázku tématu (doporučeno)
- `summary` - Shrnutí (1-2 odstavce) - zobrazuje se v sekci "Shrnutí"
- `audio` - Podcast audio soubor
- `resources` - Dodatečné zdroje
- `flashcards` - Kartičky pro učení
- `quiz` - Kvízové otázky
- `mindmap` - Myšlenková mapa
- `objectives` - Výukové cíle (nyní nepoužíváno v UI, ale lze ponechat)

## Přidání nového tématu - Postup

### 1. Vytvoření JSON souboru

1. Zkopírujte `_TEMPLATE.json` do `data/topics/TXX.json` (kde XX je číslo)
2. Vyplňte všechna pole podle šablony
3. Zkontrolujte JSON syntax (žádné chyby v JSON validátoru)

### 2. Struktura kvízových otázek

```json
"quiz": {
  "questions": [
    {
      "question": "Text otázky?",
      "answers": [
        "Odpověď 1",
        "Odpověď 2",
        "Odpověď 3",
        "Odpověď 4"
      ],
      "correct": 0
    }
  ]
}
```

**Pravidla:**
- `correct` je index (0-3) správné odpovědi v poli `answers`
- Minimálně 2 odpovědi, doporučeno 4
- Otázky se automaticky promíchají při načtení stránky

### 3. Struktura flashcards

```json
"flashcards": [
  {
    "q": "Text otázky?",
    "a": "Text odpovědi."
  }
]
```

**Pravidla:**
- Minimálně 1 kartička
- Kartičky se automaticky promíchají při načtení
- Podporuje základní Markdown: `**tučné**` a `\n` pro nové řádky

### 4. Obrázky

**Umístění:**
- Obrázky tématu: `assets/images/topics/TXX.jpg` (doporučená velikost: 200x200px nebo větší, čtvercový formát)
- Myšlenkové mapy: `assets/images/mindmaps/TXX.png`

**Názvy souborů:**
- Musí odpovídat ID tématu (např. T01.jpg, T02.png)
- Podporované formáty: JPG, PNG, WebP

### 5. Audio soubory

**Umístění:** `assets/audio/TXX.mp3`

**Pravidla:**
- Formát: MP3 (doporučeno)
- Doporučená kvalita: 128 kbps nebo vyšší
- Název souboru musí odpovídat ID tématu

## Kontrolní seznam před publikováním

- [ ] JSON soubor je validní (zkontrolujte na jsonlint.com)
- [ ] `id` a `order` jsou správně nastavené
- [ ] Všechny texty jsou v češtině
- [ ] Obrázky existují a mají správné názvy
- [ ] Audio soubor existuje (pokud je použit)
- [ ] Kvíz má alespoň 1 otázku s 2+ odpověďmi
- [ ] Správná odpověď v kvízu má správný index (0-3)
- [ ] Flashcards mají alespoň 1 kartičku
- [ ] Shrnutí má 1-2 odstavce
- [ ] Studijní materiály jsou kompletní

## Automatické funkce

Po přidání nového tématu se automaticky:

- ✅ Zobrazí v seznamu všech témat (index stránka)
- ✅ Zobrazí v sidebar navigaci
- ✅ Použije správné pořadové číslo
- ✅ Zobrazí obrázek (pokud existuje)
- ✅ Promíchá kvízové otázky při každém načtení
- ✅ Promíchá flashcards při každém načtení
- ✅ Použije správné české skloňování v počtech

## Testování nového tématu

1. Otevřete `index.html` v prohlížeči
2. Zkontrolujte, že se téma zobrazuje v seznamu
3. Klikněte na téma
4. Ověřte všechny sekce:
   - Shrnutí
   - Studijní text
   - Podcast (pokud je)
   - Myšlenková mapa (pokud je)
   - Kartičky
   - Kvíz
   - Další zdroje
5. Otestujte navigaci (Předchozí/Následující)
6. Otestujte funkčnost kvízu (výběr odpovědi, navigace)
7. Otestujte funkčnost flashcards (otočení, navigace)

## Hromadné přidávání témat

Pro přidání více témat najednou:

1. Vytvořte všechny JSON soubory
2. Zkontrolujte, že `order` pole jsou jedinečná a postupná
3. Zkontrolujte, že `id` jsou jedinečná
4. Nahrajte všechny soubory najednou
5. Testujte každé téma zvlášť

## Tipy pro obsah

- **Otázky v kvízu:** Používejte konkrétní, jednoznačné otázky
- **Odpovědi:** Jedna správná, ostatní věrohodné ale nesprávné
- **Flashcards:** Stručné, výstižné otázky a odpovědi
- **Shrnutí:** 1-2 odstavce, klíčové informace z materiálů
- **Studijní text:** Použijte `\n\n` pro odstavce

## Problémy a řešení

### Téma se nezobrazuje
- Zkontrolujte JSON syntax
- Zkontrolujte, že soubor je v `data/topics/`
- Zkontrolujte konzoli prohlížeče na chyby

### Kvíz nefunguje
- Zkontrolujte strukturu `quiz.questions`
- Zkontrolujte, že `correct` index existuje v `answers`
- Zkontrolujte, že máte alespoň 1 otázku

### Obrázek se nezobrazuje
- Zkontrolujte cestu k souboru
- Zkontrolujte název souboru (musí odpovídat ID)
- Zkontrolujte, že soubor existuje

### Flashcards nefungují
- Zkontrolujte strukturu (pole `q` a `a`)
- Zkontrolujte, že máte alespoň 1 kartičku

