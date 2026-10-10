import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pages = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', html)
print(f"Total pages found: {len(pages)}")
for p in pages:
    print(f" - {p}")
