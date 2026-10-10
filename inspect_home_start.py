import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's search for typical sections in index.html and see their text elements
print("=== CHECKING HOME PAGE ELEMENTS ===")
home_idx = html.find('id="page-home"')
home_part = html[home_idx:home_idx+4000]
print(home_part[:1500])
