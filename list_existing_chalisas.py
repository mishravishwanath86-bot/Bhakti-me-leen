import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', encoding='utf-8') as f:
    app_js = f.read()

# Find all keys starting with chalisa_ in CONTENT
chalisa_keys = re.findall(r'(chalisa_[a-zA-Z0-9_]+)\s*:\s*\{', app_js)
print(f"Total chalisa keys in CONTENT: {len(chalisa_keys)}")
for k in chalisa_keys:
    print("  ", k)
