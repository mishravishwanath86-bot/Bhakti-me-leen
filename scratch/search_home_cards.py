import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's search inside page-home
p_home_idx = html.find('id="page-home"')
p_home_end = html.find('</section>', p_home_idx)
home_html = html[p_home_idx:p_home_end]

for kw in ['sundarkand', 'mantra', 'chalisa', 'aarti', 'gita', 'संग्रहालय']:
    print(f'=== KW: {kw} in page-home ===')
    matches = re.findall(rf'onclick="[^"]*{kw}[^"]*"', home_html, re.I)
    for m in set(matches):
        print('  ', m)
    
    # Also find text mentions
    card_matches = re.findall(rf'<div[^>]*onclick="[^"]*"[^>]*>[\s\S]*?{kw}[\s\S]*?</div>', home_html, re.I)
    print(f'   Cards with {kw}: {len(card_matches)}')

