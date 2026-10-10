import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

matches = re.findall(r'id="page-[^"]*"', html)
for m in matches:
    if 'audio' in m or 'bhajan' in m or 'music' in m or 'player' in m:
        print(m)
