import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

import re
targets = ['today-panchang-card', 'sadhana-home', 'divine-gift', 'home-promo']
for t in targets:
    m = re.findall(r'([^{}]*' + t + r'[^{}]*\{[^}]*\})', css)
    print(f"=== {t}: {len(m)} matches ===")
    for rule in m:
        if 'margin' in rule:
            print(" ", rule.strip().replace('\n', ' '))
