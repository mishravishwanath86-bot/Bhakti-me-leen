import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    app_text = f.read()

for name in ['AARTI_COLLECTIONS', 'CHALISA_COLLECTIONS', 'MANTRA_COLLECTIONS', 'SUNDARKAND_DATA']:
    matches = [m.start() for m in re.finditer(rf'(?:window\.)?{name}\s*=', app_text)]
    print(f'=== {name}: {len(matches)} occurrences in app.js ===')
    for idx in matches:
        print(f'  Index {idx}: {app_text[idx:idx+120].strip()}')

for fname in ['mantra_engine.js', 'sundarkand_engine.js', 'chalisa_engine.js', 'gita_engine.js']:
    try:
        with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
            eng_text = f.read()
        for name in ['AARTI_COLLECTIONS', 'CHALISA_COLLECTIONS', 'MANTRA_COLLECTIONS', 'SUNDARKAND_DATA', 'GITA_DATA']:
            matches = [m.start() for m in re.finditer(rf'(?:window\.)?{name}\s*=', eng_text)]
            if matches:
                print(f'=== {fname} -> {name}: {len(matches)} occurrences ===')
                for idx in matches:
                    print(f'  Index {idx}: {eng_text[idx:idx+120].strip()}')
    except Exception as e:
        pass
