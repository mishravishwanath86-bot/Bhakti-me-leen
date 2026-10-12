import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'(?:window\.)?AARTI_COLLECTIONS\s*=', text)]
print(f'Total AARTI_COLLECTIONS = definitions: {len(matches)}')
for idx in matches:
    print(f'Index {idx}:')
    print(text[idx:idx+300])
    print('-'*50)
