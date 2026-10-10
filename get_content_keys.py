import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

content_idx = text.find('const CONTENT = {')
content_end = text.find('\n};', content_idx)

content_block = text[content_idx:content_end]
keys = re.findall(r'\n  ([a-zA-Z0-9_]+):\s*\{', content_block)
print("Keys in CONTENT:", keys)

# Check if any key mentions shani
for k in keys:
    if 'shani' in k.lower():
        print("Found shani key:", k)
