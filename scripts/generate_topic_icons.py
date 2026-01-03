#!/usr/bin/env python3
"""
Generátor SVG ikon pro témata dějin tance a baletu

Vytváří jednoduché, esteticky příjemné SVG ikony pro každé téma.
Ikony jsou malé, čitelné, s minimem barev a konzistentním stylem.
"""

import os
import csv
from pathlib import Path

# Cesta k projektu
PROJECT_ROOT = Path(__file__).parent.parent
TOPICS_CSV = PROJECT_ROOT / "data" / "topics" / "_TOPICS.csv"
OUTPUT_DIR = PROJECT_ROOT / "assets" / "images" / "topics"

# Paleta barev - ladící s fialovou/zelenou, různé odstíny
# Základ: fialová (#7c3aed z design-tokens) a zelená (#059669 z materials-heading)
COLORS = {
    "violet_1": "#7c3aed",     # Hlavní fialová (z design-tokens secondary)
    "violet_2": "#8b5cf6",     # Světlejší fialová
    "violet_3": "#6d28d9",     # Tmavší fialová
    "violet_4": "#a78bfa",     # Pastelová fialová
    "violet_5": "#5b21b6",     # Hluboká fialová
    "purple_1": "#9333ea",     # Fialovorůžová
    "purple_2": "#c084fc",     # Světle fialovorůžová
    "green_1": "#059669",      # Zelená (z materials-heading)
    "green_2": "#10b981",      # Světlejší zelená
    "green_3": "#047857",      # Tmavší zelená
    "green_4": "#34d399",      # Pastelová zelená
    "teal_1": "#0d9488",       # Modrozelená
    "teal_2": "#14b8a6",       # Světlejší modrozelená
    "indigo_1": "#6366f1",     # Indigo (mezi modrou a fialovou)
    "indigo_2": "#818cf8",     # Světlejší indigo
    "slate_1": "#64748b",      # Šedomodrá (neutrální)
}

# Definice ikon pro každé téma - s relevantními symboly a rozmanitými barvami
ICON_DESIGN = {
    "T00": {  # Úvod
        "symbol": "star",
        "color": COLORS["violet_1"]  # Hlavní fialová
    },
    "T01": {  # Pravěk, Egypt, Mezopotámie - pyramidy
        "symbol": "triangle",
        "color": COLORS["green_3"]  # Tmavší zelená (písek, starověk)
    },
    "T02": {  # Indie, Čína, Japonsko - pagody, vrstvy
        "symbol": "layers",
        "color": COLORS["violet_2"]  # Světlejší fialová
    },
    "T03": {  # Antika (Řecko, Řím) - sloupy
        "symbol": "pillar",
        "color": COLORS["indigo_1"]  # Indigo (klasická barva)
    },
    "T04": {  # Středověk (Feudalismus) - hrady, věže
        "symbol": "tower",
        "color": COLORS["slate_1"]  # Šedá (středověk)
    },
    "T05": {  # Renesance - květ, rozkvět
        "symbol": "petals",
        "color": COLORS["purple_1"]  # Fialovorůžová (renesanční eleganci)
    },
    "T06": {  # Počátky baletu - Dvorský balet - koruna
        "symbol": "crown",
        "color": COLORS["violet_3"]  # Tmavší fialová (dvořanstvo)
    },
    "T07": {  # Baroko a Rokoko - ornamenty, svitky
        "symbol": "scroll",
        "color": COLORS["violet_4"]  # Pastelová fialová (ozdobnost)
    },
    "T08": {  # Klasicismus - chrám, arch
        "symbol": "temple",
        "color": COLORS["indigo_2"]  # Světlejší indigo (klasická jasnost)
    },
    "T09": {  # Preromantismus - měsíc
        "symbol": "crescent",
        "color": COLORS["purple_2"]  # Světle fialovorůžová (mystika)
    },
    "T10": {  # Romantismus - květ
        "symbol": "flower",
        "color": COLORS["green_2"]  # Světlejší zelená (příroda, cit)
    },
    "T11": {  # Významní choreografové a tanečnice v období romantismu - figura
        "symbol": "figure",
        "color": COLORS["violet_5"]  # Hluboká fialová (důležitost)
    },
    "T12": {  # Vývoj baletu v Rusku - kupole
        "symbol": "dome",
        "color": COLORS["green_1"]  # Zelená (příroda Ruska)
    },
    "T13": {  # Soubor Ruské balety Sergeje Ďagileva - skupina
        "symbol": "group",
        "color": COLORS["violet_1"]  # Hlavní fialová (důležitost souboru)
    },
    "T14": {  # Významní choreografové souboru Ruské balety - medaile
        "symbol": "medal",
        "color": COLORS["purple_1"]  # Fialovorůžová (výjimečnost)
    },
    "T15": {  # Vývoj baletu v USA - pruhy (vlajka)
        "symbol": "lines",
        "color": COLORS["teal_1"]  # Modrozelená (USA)
    },
    "T16": {  # Vývoj moderního tance v Evropě - křivka
        "symbol": "curve",
        "color": COLORS["green_4"]  # Pastelová zelená (moderna, pohyb)
    },
    "T17": {  # Vývoj moderního tance v USA - vlna
        "symbol": "wave",
        "color": COLORS["teal_2"]  # Světlejší modrozelená (dynamika)
    },
    "T18": {  # Vývoj baletu v Anglii - štít
        "symbol": "shield",
        "color": COLORS["violet_2"]  # Světlejší fialová (království)
    },
    "T19": {  # Významní světoví choreografové - zeměkoule
        "symbol": "world",
        "color": COLORS["indigo_1"]  # Indigo (světovost)
    },
    "T20": {  # Počátky tance v Čechách - srdce (lidové)
        "symbol": "heart",
        "color": COLORS["green_3"]  # Tmavší zelená (česká tradice)
    },
    "T21": {  # Baletní mistři ND do roku 1945 - budova (divadlo)
        "symbol": "building",
        "color": COLORS["slate_1"]  # Šedá (historické období)
    },
    "T22": {  # Zakladatelé české choreografické tvorby - strom (růst, kořeny)
        "symbol": "tree",
        "color": COLORS["green_2"]  # Světlejší zelená (růst, zakořenění)
    },
    "T23": {  # Významní čeští choreografové - hvězdy
        "symbol": "stars",
        "color": COLORS["violet_3"]  # Tmavší fialová (česká výjimečnost)
    },
    "T24": {  # Baletní mistři a reperotár ND od r. 1959 - moderní symbol
        "symbol": "modern",
        "color": COLORS["green_1"]  # Zelená (současnost, růst)
    },
}


def generate_svg_icon(topic_id, design):
    """Vygeneruje SVG ikonu podle designu"""
    color = design["color"]
    symbol_type = design["symbol"]
    
    # Jednoduché SVG s viewBox 0 0 100 100 pro snadné škálování
    svg_parts = []
    
    if symbol_type == "star":
        svg_parts = [
            f'<polygon points="50,15 55,35 75,35 60,47 65,67 50,57 35,67 40,47 25,35 45,35" fill="{color}" stroke="none"/>'
        ]
    elif symbol_type == "triangle":
        svg_parts = [
            f'<polygon points="50,20 75,75 25,75" fill="{color}" stroke="none"/>'
        ]
    elif symbol_type == "layers":
        svg_parts = [
            f'<rect x="25" y="50" width="50" height="12" rx="3" fill="{color}"/>',
            f'<rect x="30" y="38" width="40" height="12" rx="3" fill="{color}" opacity="0.8"/>',
            f'<rect x="35" y="26" width="30" height="12" rx="3" fill="{color}" opacity="0.6"/>',
        ]
    elif symbol_type == "pillar":
        svg_parts = [
            f'<rect x="40" y="20" width="20" height="60" fill="{color}"/>',
            f'<rect x="35" y="15" width="30" height="8" rx="2" fill="{color}" opacity="0.8"/>',
        ]
    elif symbol_type == "tower":
        svg_parts = [
            f'<rect x="35" y="40" width="30" height="45" fill="{color}"/>',
            f'<polygon points="50,20 65,40 35,40" fill="{color}" opacity="0.9"/>',
        ]
    elif symbol_type == "petals":
        svg_parts = [
            f'<circle cx="50" cy="50" r="8" fill="{color}"/>',
            f'<ellipse cx="50" cy="35" rx="6" ry="12" fill="{color}" opacity="0.8"/>',
            f'<ellipse cx="65" cy="50" rx="12" ry="6" fill="{color}" opacity="0.8"/>',
            f'<ellipse cx="50" cy="65" rx="6" ry="12" fill="{color}" opacity="0.8"/>',
            f'<ellipse cx="35" cy="50" rx="12" ry="6" fill="{color}" opacity="0.8"/>',
        ]
    elif symbol_type == "crown":
        svg_parts = [
            f'<path d="M 30 60 L 30 45 L 40 50 L 50 35 L 60 50 L 70 45 L 70 60 Z" fill="{color}"/>',
        ]
    elif symbol_type == "scroll":
        svg_parts = [
            f'<path d="M 35 30 Q 35 25 40 25 L 60 25 Q 65 25 65 30 L 65 70 Q 65 75 60 75 L 40 75 Q 35 75 35 70 Z" fill="{color}"/>',
            f'<path d="M 40 25 L 45 20 L 55 20 L 60 25" fill="{color}" opacity="0.7"/>',
        ]
    elif symbol_type == "crescent":
        svg_parts = [
            f'<path d="M 50 30 A 20 20 0 0 1 50 70 A 15 15 0 0 0 50 30 Z" fill="{color}"/>',
        ]
    elif symbol_type == "flower":
        svg_parts = [
            f'<circle cx="50" cy="50" r="6" fill="{color}"/>',
            f'<ellipse cx="50" cy="35" rx="5" ry="10" fill="{color}" opacity="0.85"/>',
            f'<ellipse cx="65" cy="50" rx="10" ry="5" fill="{color}" opacity="0.85"/>',
            f'<ellipse cx="50" cy="65" rx="5" ry="10" fill="{color}" opacity="0.85"/>',
            f'<ellipse cx="35" cy="50" rx="10" ry="5" fill="{color}" opacity="0.85"/>',
        ]
    elif symbol_type == "figure":
        svg_parts = [
            f'<circle cx="50" cy="30" r="8" fill="{color}"/>',
            f'<rect x="43" y="38" width="14" height="20" rx="3" fill="{color}"/>',
            f'<rect x="40" y="38" width="6" height="25" rx="2" fill="{color}" opacity="0.8"/>',
            f'<rect x="54" y="38" width="6" height="25" rx="2" fill="{color}" opacity="0.8"/>',
        ]
    elif symbol_type == "dome":
        svg_parts = [
            f'<path d="M 30 70 L 30 50 Q 30 30 50 30 Q 70 30 70 50 L 70 70 Z" fill="{color}"/>',
            f'<circle cx="50" cy="40" r="4" fill="{color}" opacity="0.6"/>',
        ]
    elif symbol_type == "group":
        svg_parts = [
            f'<circle cx="40" cy="45" r="6" fill="{color}" opacity="0.9"/>',
            f'<circle cx="50" cy="40" r="7" fill="{color}"/>',
            f'<circle cx="60" cy="45" r="6" fill="{color}" opacity="0.9"/>',
            f'<rect x="36" y="53" width="8" height="15" rx="2" fill="{color}" opacity="0.9"/>',
            f'<rect x="45" y="50" width="10" height="18" rx="2" fill="{color}"/>',
            f'<rect x="56" y="53" width="8" height="15" rx="2" fill="{color}" opacity="0.9"/>',
        ]
    elif symbol_type == "lines":
        svg_parts = [
            f'<rect x="25" y="30" width="50" height="6" fill="{color}"/>',
            f'<rect x="25" y="47" width="50" height="6" fill="{color}"/>',
            f'<rect x="25" y="64" width="50" height="6" fill="{color}"/>',
        ]
    elif symbol_type == "curve":
        svg_parts = [
            f'<path d="M 25 60 Q 50 30 75 60" stroke="{color}" stroke-width="5" fill="none" stroke-linecap="round"/>',
        ]
    elif symbol_type == "wave":
        svg_parts = [
            f'<path d="M 20 50 Q 35 30 50 50 T 80 50" stroke="{color}" stroke-width="5" fill="none" stroke-linecap="round"/>',
        ]
    elif symbol_type == "world":
        svg_parts = [
            f'<circle cx="50" cy="50" r="25" fill="none" stroke="{color}" stroke-width="3"/>',
            f'<line x1="50" y1="25" x2="50" y2="75" stroke="{color}" stroke-width="2"/>',
            f'<path d="M 25 50 Q 35 40 50 50 Q 65 40 75 50 Q 65 60 50 50 Q 35 60 25 50" fill="{color}" opacity="0.3"/>',
        ]
    elif symbol_type == "building":
        svg_parts = [
            f'<rect x="30" y="35" width="40" height="40" fill="{color}"/>',
            f'<rect x="35" y="40" width="8" height="12" fill="{color}" opacity="0.3"/>',
            f'<rect x="47" y="40" width="8" height="12" fill="{color}" opacity="0.3"/>',
            f'<rect x="57" y="40" width="8" height="12" fill="{color}" opacity="0.3"/>',
            f'<polygon points="50,25 65,35 35,35" fill="{color}" opacity="0.9"/>',
        ]
    elif symbol_type == "tree":
        svg_parts = [
            f'<rect x="47" y="50" width="6" height="25" fill="{color}"/>',
            f'<circle cx="50" cy="45" r="12" fill="{color}"/>',
        ]
    elif symbol_type == "stars":
        svg_parts = [
            f'<polygon points="50,20 52,26 58,26 53,30 55,36 50,32 45,36 47,30 42,26 48,26" fill="{color}"/>',
            f'<polygon points="35,60 36,63 39,63 37,65 38,68 35,66 32,68 33,65 31,63 34,63" fill="{color}" opacity="0.8"/>',
            f'<polygon points="65,60 66,63 69,63 67,65 68,68 65,66 62,68 63,65 61,63 64,63" fill="{color}" opacity="0.8"/>',
        ]
    elif symbol_type == "modern":
        svg_parts = [
            f'<path d="M 30 45 Q 50 25 70 45 Q 50 65 30 45" fill="{color}" opacity="0.6"/>',
            f'<path d="M 50 25 L 50 75" stroke="{color}" stroke-width="3" stroke-linecap="round"/>',
        ]
    elif symbol_type == "temple":
        svg_parts = [
            f'<rect x="35" y="50" width="30" height="30" fill="{color}"/>',
            f'<polygon points="50,30 65,50 35,50" fill="{color}" opacity="0.9"/>',
            f'<rect x="42" y="55" width="6" height="20" fill="{color}" opacity="0.4"/>',
            f'<rect x="52" y="55" width="6" height="20" fill="{color}" opacity="0.4"/>',
        ]
    elif symbol_type == "medal":
        svg_parts = [
            f'<circle cx="50" cy="50" r="20" fill="{color}"/>',
            f'<circle cx="50" cy="50" r="12" fill="none" stroke="{color}" stroke-width="2" opacity="0.5"/>',
            f'<path d="M 50 30 L 52 38 L 60 38 L 54 42 L 56 50 L 50 46 L 44 50 L 46 42 L 40 38 L 48 38 Z" fill="white" opacity="0.8"/>',
        ]
    elif symbol_type == "shield":
        svg_parts = [
            f'<path d="M 50 25 Q 30 25 30 40 Q 30 55 50 75 Q 70 55 70 40 Q 70 25 50 25" fill="{color}"/>',
            f'<path d="M 50 35 L 50 60" stroke="white" stroke-width="2" opacity="0.6"/>',
        ]
    elif symbol_type == "heart":
        svg_parts = [
            f'<path d="M 50 55 C 50 50, 40 40, 35 45 C 30 50, 30 60, 50 75 C 70 60, 70 50, 65 45 C 60 40, 50 50, 50 55 Z" fill="{color}"/>',
        ]
    else:
        # Výchozí: jednoduchý kruh
        svg_parts = [
            f'<circle cx="50" cy="50" r="25" fill="{color}"/>'
        ]
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" width="100" height="100">
  {' '.join(svg_parts)}
</svg>'''
    
    return svg


def main():
    """Hlavní funkce pro generování ikon"""
    # Vytvoř výstupní adresář, pokud neexistuje
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Načti témata z CSV
    topics = {}
    if TOPICS_CSV.exists():
        with open(TOPICS_CSV, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                topics[row['id']] = row
    
    try:
        print("Generovani SVG ikon pro temata...")
        print(f"Vystupni adresar: {OUTPUT_DIR}")
    except:
        pass  # Ignore encoding errors in console output
    
    generated_count = 0
    for topic_id, design in ICON_DESIGN.items():
        svg_content = generate_svg_icon(topic_id, design)
        output_file = OUTPUT_DIR / f"{topic_id}.svg"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        generated_count += 1
        try:
            print(f"  {topic_id}.svg created")
        except:
            pass
    
    try:
        print(f"\nCelkem vygenerovano {generated_count} ikon.")
        print(f"\nIkony jsou ulozeny v: {OUTPUT_DIR}")
    except:
        pass


if __name__ == "__main__":
    main()

