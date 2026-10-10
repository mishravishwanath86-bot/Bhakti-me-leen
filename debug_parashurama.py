import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('parashurama_raw.html', 'r', encoding='utf-8') as f:
    raw = f.read()

# Find occurrences of 'परशुधारी'
for m in re.finditer(r'परशुधारी', raw):
    s = max(0, m.start() - 150)
    e = min(len(raw), m.end() + 250)
    print(raw[s:e])
    print("="*50)
