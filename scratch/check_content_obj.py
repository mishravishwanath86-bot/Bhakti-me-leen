import sys
import codecs
import re

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# find const CONTENT = {
m = re.search(r'const CONTENT\s*=\s*(\{[\s\S]*?\n\};)', text)
if m:
    content_block = m.group(1)
    print(f"Found CONTENT object (len: {len(content_block)})")
    keys = re.findall(r'^\s*([a-zA-Z0-9_]+)\s*:\s*\{', content_block, re.MULTILINE)
    print(f"Keys in CONTENT ({len(keys)}): {keys[:20]}")
    for k in ['aarti_krishna', 'chalisa_hanuman', 'mantra_gayatri', 'sundarkand']:
        print(f"  Has {k}? {k in keys}")
else:
    print("CONTENT object not found!")
