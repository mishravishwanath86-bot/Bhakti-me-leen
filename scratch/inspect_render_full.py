import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fn in ['renderFullSundarkandPage', 'renderFullDrikMantraPage', 'renderFullDrikChalisaPage', 'renderFullDrikAartiPage']:
    print(f'=== SEARCHING FOR {fn} ===')
    for f in ['app.js', 'sundarkand_engine.js', 'mantra_engine.js', 'drik_app_addon.js', 'index.html']:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        matches = re.finditer(rf'(?:window\.)?{fn}\s*=\s*function', content)
        for m in matches:
            start = m.start()
            print(f'Found in {f} at index {start}')
            print(content[start:start+1200])
            print('...\n')
