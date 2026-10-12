import sys
import codecs
import json

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in app.js: {len(lines)}")
for i, line in enumerate(lines):
    if "window.AARTI_COLLECTIONS =" in line:
        print(f"Line {i+1}: {line.strip()[:60]}")
    if "window.CHALISA_COLLECTIONS =" in line:
        print(f"Line {i+1}: {line.strip()[:60]}")
