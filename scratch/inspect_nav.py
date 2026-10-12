import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Search for nav or menu or dock
dock_idx = html.find('class="bottom-nav"')
if dock_idx == -1:
    dock_idx = html.find('nav')
print('=== NAV / DOCK ===')
for m in re.finditer(r'<nav[^>]*>[\s\S]*?</nav>', html):
    print(m.group(0)[:800])
    print('...\n')

# Search for sidebar / drawer / menu
for m in re.finditer(r'<div[^>]*class="[^"]*(?:drawer|menu|sidebar|dock)[^"]*"[^>]*>[\s\S]*?</div>', html):
    print(m.group(0)[:600])
    print('...\n')

