import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\app.js', 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

idx = js.find('theme')
while idx != -1:
    print(js[idx-50:idx+250])
    print("="*40)
    idx = js.find('theme', idx+200)
    if idx > 3000: break
