# Jak funguje formátování sekcí v T01 (PRAVĚK, EGYPT, MEZOPOTÁMIE)

## Přehled

T01 používá systém **automatického seskupování sekcí** založený na názvu tématu, který vytváří modré hlavičky a rozděluje materiály do logických skupin.

## 1. Struktura v JSON souborech

### `data/topics/T01.json`
```json
{
  "title": "PRAVĚK, EGYPT, MEZOPOTÁMIE"
}
```
**Důležité:** Název je **oddělený čárkami** (ne závorkami jako "ANTIKA (Řecko, Řím)").

### `data/materials/T01_materials.json`
Sekce jsou uspořádány tak, že **hlavní sekce mají nadpisy, které přesně odpovídají názvům v title**:

```json
{
  "sections": [
    {
      "heading": "PRAVĚK",     // ← Odpovídá první části v title
      "content": "..."
    },
    {
      "heading": "UMĚNÍ",      // ← Podsekce pod PRAVĚK
      "content": "..."
    },
    {
      "heading": "HUDBA",      // ← Podsekce pod PRAVĚK
      "content": "..."
    },
    {
      "heading": "TANEC",      // ← Podsekce pod PRAVĚK
      "content": "..."
    },
    {
      "heading": "EGYPT",      // ← Odpovídá druhé části v title
      "content": "..."
    },
    {
      "heading": "UMĚNÍ",      // ← Podsekce pod EGYPT
      "content": "..."
    },
    // ... další podsekce EGYPT
    {
      "heading": "MEZOPOTÁMIE", // ← Odpovídá třetí části v title
      "content": "..."
    },
    // ... další podsekce MEZOPOTÁMIE
  ]
}
```

## 2. JavaScript logika seskupování

### `scripts/app.js` - Funkce `groupSectionsBySubtopics()`

**Krok 1:** Rozdělení názvu na části
```javascript
// Řádek 418
const titleParts = topic.title.split(',').map(part => part.trim().toUpperCase());
// Výsledek: ["PRAVĚK", "EGYPT", "MEZOPOTÁMIE"]
```

**Krok 2:** Seskupení sekcí
Funkce `groupSectionsBySubtopics()` projde všechny sekce a:
- Porovnává `section.heading` (např. "PRAVĚK") s `titleParts` (case-insensitive)
- Když najde shodu, vytvoří novou skupinu (group) pro tento subtopic
- Všechny následující sekce (do dalšího matchu) se přidají do této skupiny jako podsekce

**Příklad procesu:**
1. Najde sekci s `heading: "PRAVĚK"` → vytvoří skupinu pro "PRAVĚK"
2. Sekce "UMĚNÍ", "HUDBA", "TANEC" se přidají jako podsekce do skupiny "PRAVĚK"
3. Najde sekci s `heading: "EGYPT"` → vytvoří novou skupinu pro "EGYPT"
4. Sekce "UMĚNÍ", "NÁBOŽENSTVÍ", atd. se přidají jako podsekce do skupiny "EGYPT"
5. A tak dále...

## 3. Vykreslování HTML

### `scripts/app.js` - Funkce `renderTopicContent()`

**Řádky 427-446:**
```javascript
groupedSections.forEach(group => {
  if (group.subtopic) {
    // Vytvoří modrou hlavičku
    html += `<div class="materials-subtopic-group">`;
    html += `<h2 class="materials-subtopic-heading">${escapeHtml(group.subtopic)}</h2>`;
    
    // Vykreslí všechny sekce v této skupině
    group.sections.forEach((section, sectionIndex) => {
      // Pokud je první sekce a má stejný název jako subtopic, 
      // nadpis se přeskočí (už je vykreslený jako modrá hlavička)
      const shouldSkipHeading = sectionIndex === 0 && 
        section.heading.toUpperCase() === group.subtopic.toUpperCase();
      
      html += `
        <div class="materials-section">
          ${section.heading && !shouldSkipHeading ? 
            `<h3 class="materials-heading">${escapeHtml(section.heading)}</h3>` : ''}
          <div class="materials-content">${markdownToHtml(section.content || '')}</div>
        </div>
      `;
    });
    
    html += `</div>`;
  }
});
```

**Výsledná HTML struktura:**
```html
<div class="materials-subtopic-group">
  <h2 class="materials-subtopic-heading">PRAVĚK</h2>  <!-- Modrá hlavička -->
  
  <div class="materials-section">
    <!-- Název "PRAVĚK" se přeskočí, protože je první a shoduje se s hlavičkou -->
    <div class="materials-content">...</div>
  </div>
  
  <div class="materials-section">
    <h3 class="materials-heading">UMĚNÍ</h3>  <!-- Běžný nadpis -->
    <div class="materials-content">...</div>
  </div>
  
  <!-- ... další podsekce -->
</div>

<div class="materials-subtopic-group">
  <h2 class="materials-subtopic-heading">EGYPT</h2>  <!-- Modrá hlavička -->
  <!-- ... sekce EGYPT -->
</div>
```

## 4. CSS styling

### `assets/styles/components.css`

**Modrá hlavička (Řádek 668):**
```css
.materials-subtopic-heading {
  font-size: var(--font-size-xl);
  margin-bottom: var(--spacing-md);
  margin-top: 0;
  color: var(--color-primary);        /* Modrá barva */
  font-weight: var(--font-weight-bold);
  padding-bottom: var(--spacing-xs);
  border-bottom: 1px solid var(--color-border);  /* Čára pod hlavičkou */
}
```

**Běžné nadpisy sekcí:**
```css
.materials-heading {
  /* Styl pro h3 nadpisy podsekce (UMĚNÍ, HUDBA, atd.) */
}
```

## 5. Formátování obsahu

### Obsah v JSON
V `content` poli se používá **markdown-like formátování**:
- `\n\n` = nový odstavec
- `\n` = nový řádek (v rámci odstavce)
- `-` na začátku řádku = odrážka
- `a)`, `b)`, `1.)`, `2.)` = číslování
- `•` = bullet pointy

**Příklad:**
```
"- období dějin lidstva\n\n- zahrnuje vznik a vývoj\n\na) archeologie\n\nb) geologie"
```

### Konverze na HTML
Funkce `markdownToHtml()` (`scripts/app.js`, řádky 1180-1206):
1. Escapuje HTML znaky
2. Konvertuje `\n\n` → `</p><p>` (nové odstavce)
3. Konvertuje `\n` → `<br>` (nové řádky)
4. Konvertuje `**text**` → `<strong>text</strong>` (bold)
5. Přidává hyperlinky na termíny (z `term_links` souborů)

## Shrnutí procesu

1. **Název tématu** (`T01.json`) → `"PRAVĚK, EGYPT, MEZOPOTÁMIE"`
2. **Sekce v materiálech** (`T01_materials.json`) → Nadpisy "PRAVĚK", "EGYPT", "MEZOPOTÁMIE" jako hlavní sekce
3. **JavaScript grouping** (`app.js`) → Porovnává názvy a seskupuje sekce
4. **HTML vykreslování** → Vytvoří `<div class="materials-subtopic-group">` s modrou hlavičkou
5. **CSS styling** → `.materials-subtopic-heading` aplikuje modrou barvu a čáru
6. **Obsah** → `markdownToHtml()` konvertuje markdown-like text na HTML

## Důležité poznámky

- **Název musí být oddělený čárkami** (ne závorkami)
- **Hlavní sekce musí mít nadpisy přesně odpovídající názvům v title** (case-insensitive)
- **Formátování obsahu je v JSON** (markdown-like syntax), HTML se generuje automaticky
- **Modrá hlavička se vytvoří automaticky** pro každou hlavní sekci, která odpovídá názvu v title

