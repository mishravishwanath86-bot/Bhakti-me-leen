import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'जुगल किशोर', text)]
for idx, m in enumerate(matches):
    start = max(0, m - 100)
    end = min(len(text), m + 150)
    print(f'=== Occurrence {idx+1} at byte {m} ===')
    print(text[start:end])
    print()
