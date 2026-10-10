import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

head_idx = html.find('</head>')
head = html[:head_idx]
links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', head)
for l in links:
    print(l)
