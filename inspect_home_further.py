import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

home_idx = html.find('id="page-home"')
print(html[home_idx+6000:home_idx+11000])
