import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'readAartiItemDirect' in l and ('function' in l or '=' in l):
        print(f'Line {i+1}: {l.strip()[:100]}')
        for j in range(i, min(len(lines), i+25)):
            print(f'  {j+1}: {lines[j].rstrip()[:120]}')
        print('-'*60)
