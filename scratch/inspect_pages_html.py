import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pages = ['page-gita', 'page-sundarkand', 'page-mantra', 'page-chalisa', 'page-aarti', 'page-reader']
for p in pages:
    idx = html.find(f'id="{p}"')
    if idx == -1:
        idx = html.find(f"id='{p}'")
    print(f'=== {p} === (found at {idx})')
    if idx != -1:
        snippet = html[max(0, idx-20):idx+1200]
        print(snippet)
        print('...\n')
