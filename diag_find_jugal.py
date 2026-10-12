import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['app.js', 'index.html', 'drik_app_addon.js']:
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    matches = [m.start() for m in re.finditer(r'जुगल किशोर', text)]
    print(f'{fname}: {len(matches)} occurrences of जुगल किशोर')
    for m in matches[:5]:
        start = max(0, m - 150)
        end = min(len(text), m + 200)
        print(f'--- context in {fname} at {m} ---')
        print(text[start:end])
        print()
