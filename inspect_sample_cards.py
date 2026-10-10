import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's inspect typical cards on Home page, Bhajan page, Gita page, Aarti page, Panchang page
sample_cards = re.findall(r'<div[^>]*class="[^"]*(?:card|box|item|row|banner|tile)[^"]*"[^>]*>', html)
print(f"Total card/box elements found: {len(sample_cards)}")
for c in sample_cards[:10]:
    print(c)
