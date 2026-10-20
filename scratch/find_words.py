import os, sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')

app_dir = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
print("Scanning files...")
for root, dirs, files in os.walk(app_dir):
    for f in files:
        if f.endswith(('.js', '.html', '.py', '.json')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                    if 'महारथी' in content and 'प्रारंभिक' in content:
                        print('Found BOTH in:', p)
                    elif '0 / 90' in content or '0/90' in content:
                        print('Found 0/90 in:', p)
            except Exception:
                pass
print("Scan done.")
