import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

idx = html.find('function applyGlobalTheme')
if idx != -1:
    print(html[idx-100:idx+600])
else:
    idx2 = html.find('applyGlobalTheme')
    print("Found applyGlobalTheme at:", idx2)
    print(html[idx2-100:idx2+600])
