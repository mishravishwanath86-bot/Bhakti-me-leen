import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# find showPage definition
matches = [m.start() for m in re.finditer(r'function\s+showPage\s*\(|window\.showPage\s*=\s*function', text)]
print('showPage definitions in app.js:', len(matches))
for m in matches:
    print(text[m:m+500])
    print('---')
