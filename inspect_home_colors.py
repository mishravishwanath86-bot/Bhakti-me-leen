import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

home_idx = html.find('id="page-home"')
next_page = html.find('<section id="page-', home_idx + 20)
home_html = html[home_idx:next_page]

print(f"page-home length: {len(home_html)}")
# look for inline styles with colors in page-home
inline_colors = re.findall(r'color\s*:\s*([^;"]+)', home_html)
from collections import Counter
print("Colors in page-home:", Counter(inline_colors).most_common(10))
