import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# find inline color styles that specify light colors
white_inline = re.findall(r'style="[^"]*color\s*:\s*(#[fF]{3,6}|#FFFDF8|#FFF9DB|#FDE68A|#E9D5FF|rgba\(255,\s*255,\s*255|white)[^"]*"', html)
print(f"Total inline light text colors in index.html: {len(white_inline)}")
from collections import Counter
counts = Counter(white_inline)
for color, count in counts.most_common(15):
    print(f"  {color}: {count} times")
