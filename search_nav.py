import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# search for nav or bottom-nav
matches = re.findall(r'(<(?:nav|div)[^>]*class="[^"]*nav[^"]*"[^>]*>)', html)
for m in matches[:10]:
    print(m)
