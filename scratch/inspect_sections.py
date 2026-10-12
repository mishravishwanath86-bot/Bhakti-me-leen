import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def search_file(filepath, pattern):
    with open(filepath, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, 1):
            if re.search(pattern, line):
                print(f"{filepath}:{idx}: {line.strip()[:110]}")

print("=== Search in index.html ===")
search_file('index.html', r'id=[\'"]page-(aarti|chalisa|mantra|sundarkand)')
search_file('index.html', r'AiBhaktiPlayer|ai_bhakti_player')

print("\n=== Search in app.js for old aarti/chalisa readers ===")
search_file('app.js', r'readAartiItemDirect|readChalisaItemDirect')
