#!/usr/bin/env python3
"""
Pomocný skript pro přidání pole 'image' do JSON souborů témat

Tento skript automaticky přidá pole 'image' do všech existujících JSON souborů témat,
které ho ještě nemají. Cesta k obrázku se automaticky vygeneruje na základě ID tématu.
"""

import json
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
TOPICS_DIR = PROJECT_ROOT / "data" / "topics"


def add_image_field_to_topic(file_path):
    """Přidá pole image do JSON souboru tématu, pokud ho nemá"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            topic = json.load(f)
        
        # Pokud už má image, přeskoč
        if 'image' in topic:
            return False, "Uz ma image pole"
        
        # Získat ID tématu
        topic_id = topic.get('id', file_path.stem)
        
        # Vytvořit cestu k obrázku (SVG)
        image_path = f"assets/images/topics/{topic_id}.svg"
        
        # Přidat pole image za title
        if 'title' in topic:
            # Vytvořit nový slovník s image na správném místě
            new_topic = {}
            for key, value in topic.items():
                new_topic[key] = value
                if key == 'title':
                    new_topic['image'] = image_path
            
            # Zapsat zpět do souboru
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(new_topic, f, ensure_ascii=False, indent=2)
            
            return True, f"Pridano image: {image_path}"
        else:
            return False, "Nema title pole"
            
    except json.JSONDecodeError as e:
        return False, f"Chyba JSON: {e}"
    except Exception as e:
        return False, f"Chyba: {e}"


def main():
    """Hlavní funkce"""
    if not TOPICS_DIR.exists():
        print(f"Adresar {TOPICS_DIR} neexistuje")
        return
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    # Projít všechny JSON soubory v adresáři topics
    for json_file in TOPICS_DIR.glob("T*.json"):
        # Přeskočit template
        if json_file.name == "_TEMPLATE.json":
            continue
        
        success, message = add_image_field_to_topic(json_file)
        
        if success:
            print(f"✓ {json_file.name}: {message}")
            updated_count += 1
        elif "Uz ma" in message:
            print(f"- {json_file.name}: {message}")
            skipped_count += 1
        else:
            print(f"✗ {json_file.name}: {message}")
            error_count += 1
    
    print(f"\nHotovo: {updated_count} aktualizovano, {skipped_count} preskoceno, {error_count} chyb")


if __name__ == "__main__":
    main()

