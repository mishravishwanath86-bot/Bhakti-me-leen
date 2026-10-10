import re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

index_html = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html")
with open(index_html, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find all blocks of id="glass-full-player-modal"
matches = list(re.finditer(r'<div[^>]*id="glass-full-player-modal"[\s\S]*?</div>\s*</div>', html))
print(f"Found {len(matches)} player modal blocks.")

if len(matches) > 1:
    # Keep the last one, remove the earlier one(s)
    first_match = matches[0]
    html = html[:first_match.start()] + html[first_match.end():]
    with open(index_html, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Removed duplicate player modal block from index.html")
