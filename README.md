# Dance History Study Platform

A modern, responsive self-study platform for learning dance history. Built as a static website with client-side functionality.

## Project Structure

```
/
├── index.html                 # Topics overview/index page
├── topic.html                 # Topic detail page template
├── assets/
│   ├── audio/                 # Audio files (placeholder for now)
│   ├── images/                # Images (if needed)
│   └── styles/
│       ├── design-tokens.css  # CSS variables (colors, spacing, typography)
│       ├── base.css           # Base/reset styles
│       ├── layout.css         # Layout components (sidebar, main content)
│       └── components.css     # UI components (topic cards, flashcards, etc.)
├── data/
│   └── topics/
│       ├── _TEMPLATE.json    # Template for new topics
│       ├── T01.json          # Individual topic files
│       ├── T02.json
│       └── ...                # More topics to be added
├── docs/
│   └── SCALING_GUIDE.md      # Guide for adding new topics
├── scripts/
│   ├── topic-loader.js        # Handles loading topic data
│   ├── progress.js            # Progress tracking (abstracted storage)
│   ├── flashcards.js          # Flashcard interactions
│   └── app.js                 # Main application logic
└── README.md                  # This file
```

## How to Run Locally

### Option 1: Using Python (Recommended)

```bash
# Python 3
python -m http.server 8000

# Then open http://localhost:8000 in your browser
```

### Option 2: Using Node.js (http-server)

```bash
# Install http-server globally (if not already installed)
npm install -g http-server

# Run the server
http-server -p 8000

# Then open http://localhost:8000 in your browser
```

### Option 3: Using VS Code Live Server

1. Install the "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

**Note:** The site must be served via HTTP (not opened directly as `file://`) because it uses `fetch()` to load JSON files.

## Přidávání nových témat

Pro detailní návod, jak přidat nová témata, viz **[Průvodce škálováním (SCALING_GUIDE.md)](docs/SCALING_GUIDE.md)**.

### Rychlý přehled

1. Vytvořte JSON soubor v `data/topics/` (např. `T03.json`)
2. Použijte `data/topics/_TEMPLATE.json` jako šablonu
3. Vyplňte všechna pole podle struktury
4. Přidejte obrázky do `assets/images/topics/`
5. Přidejte audio soubory do `assets/audio/` (volitelné)
6. Témata se automaticky zobrazí v seznamu

### Šablona

Pro rychlý start použijte: `data/topics/_TEMPLATE.json`

### Podporované funkce

- ✅ Studijní materiály (sekce s nadpisy)
- ✅ Shrnutí (automaticky generované 1-2 odstavce)
- ✅ Podcast (audio soubory)
- ✅ Kvízové otázky (po jedné, náhodné pořadí)
- ✅ Flashcards (po jedné, náhodné pořadí)
- ✅ Myšlenková mapa
- ✅ Dodatečné zdroje
- ✅ Obrázky témat

## Features

### ✅ Implemented

- Responsive layout (desktop sidebar, mobile drawer)
- Topic index page
- Topic detail pages
- Navigation (next/previous topics with numbers)
- Flashcard interactions (one-by-one, random order)
- Quiz functionality (one-by-one, random order, immediate feedback)
- Audio player with transcript toggle
- Mindmap support
- Summary section
- Quick navigation bar
- Modern CSS variable-based design system
- Image support for topics

### 📋 Backlog

- Progress tracking (localStorage) - removed from UI, architecture ready for future implementation
- Notes functionality - architecture ready, UI disabled for MVP
- Automatic topic scanning from directory (currently hardcoded in topic-loader.js)

## Design Customization

All design tokens are centralized in `assets/styles/design-tokens.css`. To customize:

- **Colors**: Modify `--color-*` variables
- **Typography**: Modify `--font-*` and `--font-size-*` variables
- **Spacing**: Modify `--spacing-*` variables
- **Layout**: Modify `--container-max-width`, `--sidebar-width`, etc.

Changes to these variables will update the entire site automatically.

## Browser Support

Targets modern browsers (last 2 versions of Chrome, Firefox, Safari, Edge). Uses:
- ES6+ JavaScript
- CSS Custom Properties (variables)
- Fetch API
- LocalStorage

## Development Notes

- **No build step required** - works as static files
- **No backend needed** - all functionality is client-side
- **Progress storage**: Currently localStorage (can be swapped for API-based storage later)
- **Content format**: JSON files (Markdown supported in content strings)

## Next Steps (Phase B)

1. Extract content from PDF → create topic JSON files
2. Test with 2 real topics
3. Verify all features work with real content
4. Proceed to Phase C for scaling to ~30 topics

## Time Tracker

Pro sledování času stráveného na projektu, počtu promptů a použitých nástrojů viz [PROJECT_TIME_TRACKER.md](PROJECT_TIME_TRACKER.md).

## License

Private project - all rights reserved.

