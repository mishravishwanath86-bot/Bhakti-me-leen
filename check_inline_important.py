import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

inline_important = re.findall(r'style="[^"]*!important[^"]*"', html)
print(f"Total inline styles with !important in index.html: {len(inline_important)}")
for s in inline_important[:10]:
    print(s)
