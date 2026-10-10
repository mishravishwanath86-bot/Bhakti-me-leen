import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

for page_name in ['page-reader', 'page-chalisa', 'page-aarti', 'page-gita']:
    idx = html.find(f'id="{page_name}"')
    if idx != -1:
        print(f"=== {page_name} ===")
        print(html[idx:idx+800].replace('\n', ' ')[:400])
