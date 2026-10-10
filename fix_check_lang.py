import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

fns = ['chooseTempLanguage', 'closeLanguageSelectorModal', 'applySelectedLanguage', 'openLanguageSelectorModal']
print("=== app.js ===")
for fn in fns:
    idx = js.find(fn)
    status = f"FOUND at {idx}" if idx != -1 else "MISSING"
    print(f"  {fn}: {status}")

print("\n=== index.html ===")
for fn in fns:
    idx = html.find(fn)
    status = f"FOUND at {idx}" if idx != -1 else "MISSING"
    print(f"  {fn}: {status}")
