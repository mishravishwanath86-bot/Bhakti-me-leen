import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Find all home section headings or markers
home_idx = html.find('id="page-home"')
next_page_idx = html.find('id="page-vrats-all"', home_idx)
home_content = html[home_idx:next_page_idx]

headings = re.findall(r'(<!--\s*[^>]+-->|<h2[^>]*>.*?</h2>|<div class="home-grid-title">.*?</div>)', home_content)
for h in headings[:30]:
    print(h.strip().replace('\n', ' '))
