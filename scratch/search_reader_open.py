import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['app.js', 'index.html', 'drik_app_addon.js', 'mantra_engine.js', 'sundarkand_engine.js', 'chalisa_engine.js']:
    try:
        with open(fname, 'r', encoding='utf-8', errors='ignore') as fp:
            lines = fp.readlines()
        
        for i, l in enumerate(lines):
            if 'page-reader' in l and ('showPage' in l or 'href' in l or 'data-back' in l):
                print(f'{fname}:{i+1} -> {l.strip()[:110]}')
    except Exception as e:
        print(f'{fname}: {e}')
