with open('styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

import re
matches = re.findall(r'(\.today-panchang-card[^{]*\{[^}]*\})', css)
for m in matches:
    print(m)
