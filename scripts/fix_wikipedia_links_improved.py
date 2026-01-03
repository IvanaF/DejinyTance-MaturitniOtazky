"""
Improved script to check Wikipedia links and find English equivalents
for Czech pages that don't exist
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from urllib.parse import urlparse, unquote

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

def check_url(url, timeout=5):
    """Check if a URL exists (returns True if status 200, False otherwise)"""
    try:
        # Normalize Wikipedia URLs - properly encode the page name
        parsed = urllib.parse.urlparse(url)
        if 'wikipedia.org' in parsed.netloc and '/wiki/' in parsed.path:
            # Extract the page name and encode it properly
            path_parts = parsed.path.split('/wiki/')
            if len(path_parts) == 2:
                page_name = path_parts[1]
                # Wikipedia URLs need proper UTF-8 encoding
                # Keep underscores as-is, encode everything else
                encoded_page = urllib.parse.quote(page_name, safe='_')
                normalized_path = '/wiki/' + encoded_page
                url = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, normalized_path, parsed.params, parsed.query, parsed.fragment))
        
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (compatible; LinkChecker/1.0)')
        # Follow redirects (Wikipedia often redirects)
        opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
        response = opener.open(req, timeout=timeout)
        status = response.getcode()
        response.close()
        # Accept 200 (OK) - redirects are handled automatically
        return status == 200
    except urllib.error.HTTPError as e:
        # 404 means page doesn't exist
        return e.code != 404
    except (urllib.error.URLError, Exception):
        return False

def to_english_wiki(cs_url):
    """Convert Czech Wikipedia URL to English"""
    if 'cs.wikipedia.org' not in cs_url:
        return cs_url
    return cs_url.replace('cs.wikipedia.org', 'en.wikipedia.org')

def get_page_name(url):
    """Extract page name from Wikipedia URL"""
    if '/wiki/' not in url:
        return None
    page_name = url.split('/wiki/')[1]
    return unquote(page_name)

def search_wikipedia_en(page_name):
    """Search for English Wikipedia page using API"""
    # Try direct page name first
    en_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(page_name)}"
    if check_url(en_url):
        return en_url
    
    # Try to use Wikipedia API to search
    try:
        search_url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(page_name)
        req = urllib.request.Request(search_url)
        req.add_header('User-Agent', 'Mozilla/5.0 (compatible; LinkChecker/1.0)')
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                return f"https://en.wikipedia.org/wiki/{urllib.parse.quote(page_name)}"
    except:
        pass
    
    return None

# Common Czech to English Wikipedia page name mappings
CZECH_TO_ENGLISH_MAPPINGS = {
    'Islám': 'Islam',
    'Křesťanství': 'Christianity',
    'Čína': 'China',
    'Šanghaj': 'Shanghai',
    'Višnu': 'Vishnu',
    'Šiva': 'Shiva',
    'Kálí': 'Kali',
    'Ganéša': 'Ganesha',
    'védy': 'Vedas',
    'Rgvéda': 'Rigveda',
    'Upanišady': 'Upanishads',
    'Mahabharáta': 'Mahabharata',
    'Bhagavadgita': 'Bhagavad_Gita',
    'Rámajána': 'Ramayana',
    'sitár': 'Sitar',
    'Nátjašastra': 'Natya_Shastra',
    'Tádž Mahal': 'Taj_Mahal',
    'stúpy': 'Stupa',
    'džinismus': 'Jainism',
    'Mahávíra': 'Mahavira',
    'nirvána': 'Nirvana',
    'Krišna': 'Krishna',
    'Ráma': 'Rama',
    'Síta': 'Sita',
    'Srí Lanka': 'Sri_Lanka',
    'Árjové': 'Indo-Aryan_peoples',
    'Védská kultura': 'Vedic_period',
    'Harappská kultura': 'Indus_Valley_Civilisation',
    'brahmáni': 'Brahmin',
    'kšatrijové': 'Kshatriya',
    'vaišjové': 'Vaishya',
    'šúdrové': 'Shudra',
    'Alexandr Veliký': 'Alexander_the_Great',
    'Ašóka': 'Ashoka',
    'Indický poloostrov': 'Indian_subcontinent',
    'Atharvavéda': 'Atharvaveda',
    'Jadžurvéda': 'Yajurveda',
    'Sámavéda': 'Samaveda',
    'Žlutá planina': 'Loess_Plateau',
    'dynastie Šang': 'Shang_dynasty',
    'dynastie Čchyn': 'Qin_dynasty',
    'Pekingská opera': 'Peking_opera',
    'Jang-c\'-ťiang': 'Yangtze',
    'Tao te ťing': 'Tao_Te_Ching',
    'I ťing': 'I_Ching',
    'Hrušňový sad': 'The_Pear_Orchard',
    'tibetský buddhismus': 'Tibetan_Buddhism',
    'šintoismus': 'Shinto',
    'Divadlo Nó': 'Noh',
    'Butó': 'Butoh',
    'Džómon': 'Jomon_period',
    'Edo': 'Edo_period',
    'Meidži': 'Meiji_period',
    'Gejša': 'Geisha',
    'Horjúdži': 'Horyuji',
    'Kazuo Óno': 'Kazuo_Ohno',
    'kjógen': 'Kyogen',
    'Vyprávění o starých věcech': 'Kojiki',
    'triphangy': 'Tribhanga',
    'dévadásí': 'Devadasi',
    'Harappská kultura': 'Indus_Valley_Civilisation',
    'Harappské kultury': 'Indus_Valley_Civilisation',
    'harappská kultura': 'Indus_Valley_Civilisation',
    'harappské kultury': 'Indus_Valley_Civilisation',
    'Harappské civilizace': 'Indus_Valley_Civilisation',
    'harappské civilizace': 'Indus_Valley_Civilisation',
    'Indický poloostrov': 'Indian_subcontinent',
    'Přední Indie': 'Indian_subcontinent',
    'poloostrov Přední Indie': 'Indian_subcontinent',
    'Védská kultura': 'Vedic_period',
    'védská kultura': 'Vedic_period',
    'Brahmán': 'Brahmin',
    'Kšatrijové': 'Kshatriya',
    'kšatrijové': 'Kshatriya',
    'Vaišjové': 'Vaishya',
    'vaišjové': 'Vaishya',
    'Šúdrové': 'Shudra',
    'šúdrové': 'Shudra',
    'Mahabhárata': 'Mahabharata',
    'Bhagavadgíta': 'Bhagavad_Gita',
    'Sitár': 'Sitar',
    'Stúpa': 'Stupa',
    'Džinismus': 'Jainism',
    'Nirvána': 'Nirvana',
    'Šang': 'Shang_dynasty',
    'Čchin': 'Qin_dynasty',
    'Pekingská_opera': 'Peking_opera',
    'Tao_te_ťing': 'Tao_Te_Ching',
    'I_ťing': 'I_Ching',
    'Tibetský_buddhismus': 'Tibetan_Buddhism',
    'Šintoismus': 'Shinto',
    'Nó': 'Noh',
    'Edo_(období)': 'Edo_period',
    'Období_Meidži': 'Meiji_period',
    'Kjógen': 'Kyogen',
    'Kodžiki': 'Kojiki',
    'Kazuo_Óno': 'Kazuo_Ohno',
}

def find_english_equivalent(cs_url):
    """Try to find English Wikipedia equivalent for a Czech URL"""
    page_name = get_page_name(cs_url)
    if not page_name:
        return None
    
    # Try direct mapping first
    if page_name in CZECH_TO_ENGLISH_MAPPINGS:
        en_page = CZECH_TO_ENGLISH_MAPPINGS[page_name]
        en_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(en_page)}"
        if check_url(en_url):
            return en_url
    
    # Try direct conversion (same page name)
    en_url = to_english_wiki(cs_url)
    if check_url(en_url):
        return en_url
    
    # Try Wikipedia API search
    en_url = search_wikipedia_en(page_name)
    if en_url:
        return en_url
    
    return None

def check_and_fix_link(original_url):
    """Check if link exists, try to find English version if Czech doesn't exist"""
    if 'wikipedia.org' not in original_url:
        return {'exists': True, 'url': original_url}
    
    # Check if original (Czech) link exists
    if check_url(original_url):
        return {'exists': True, 'url': original_url}
    
    # Try to find English equivalent
    en_url = find_english_equivalent(original_url)
    if en_url:
        return {'exists': True, 'url': en_url, 'replaced': True}
    
    return {'exists': False, 'url': original_url}

def process_terms_file(file_path):
    """Process a terms JSON file"""
    print(f"\nProcessing {os.path.basename(file_path)}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    terms = data.get('terms', {})
    
    results = {
        'total': len(terms),
        'fixed': 0,
        'removed': 0,
        'unchanged': 0
    }
    
    new_terms = {}
    
    for term, url in terms.items():
        print(f"Checking: {term} -> {url}")
        result = check_and_fix_link(url)
        
        if result['exists']:
            if result.get('replaced'):
                print(f"  [FIXED] {url} -> {result['url']}")
                new_terms[term] = result['url']
                results['fixed'] += 1
            else:
                new_terms[term] = url
                results['unchanged'] += 1
        else:
            print(f"  [REMOVE] {term} (page doesn't exist)")
            results['removed'] += 1
        
        # Small delay to avoid overwhelming Wikipedia servers
        time.sleep(0.1)
    
    # Write updated file
    data['terms'] = new_terms
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    
    print(f"\nResults for {os.path.basename(file_path)}:")
    print(f"  Total: {results['total']}")
    print(f"  Fixed: {results['fixed']}")
    print(f"  Removed: {results['removed']}")
    print(f"  Unchanged: {results['unchanged']}")
    
    return results

def main():
    """Main function"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    term_links_dir = os.path.join(script_dir, '..', 'data', 'term_links')
    
    files = [f for f in os.listdir(term_links_dir) if f.endswith('.json')]
    print(f"Found {len(files)} term files to process")
    
    all_results = {
        'total': 0,
        'fixed': 0,
        'removed': 0,
        'unchanged': 0
    }
    
    for file in files:
        file_path = os.path.join(term_links_dir, file)
        results = process_terms_file(file_path)
        
        all_results['total'] += results['total']
        all_results['fixed'] += results['fixed']
        all_results['removed'] += results['removed']
        all_results['unchanged'] += results['unchanged']
    
    print(f"\n=== SUMMARY ===")
    print(f"Total terms: {all_results['total']}")
    print(f"Fixed (Czech -> English): {all_results['fixed']}")
    print(f"Removed (non-existent): {all_results['removed']}")
    print(f"Unchanged: {all_results['unchanged']}")

if __name__ == '__main__':
    main()

