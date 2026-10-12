import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['app.js', 'index.html', 'drik_app_addon.js', 'mantra_engine.js', 'sundarkand_engine.js', 'chalisa_engine.js', 'gita_engine.js']:
    try:
        with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        matches = re.findall(r'[\'\"`]/api/[^\'\"`]+[\'\"`]', content)
        print(f'=== {fname}: {len(matches)} api calls ===')
        for m in set(matches):
            print('  ', m)
    except Exception as e:
        print(f'{fname}: {e}')
