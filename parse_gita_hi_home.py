import urllib.request
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

req = urllib.request.Request('https://bhagavadgita.com/hi', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print("Hindi homepage length:", len(html))

# Let's inspect chapter links or cards
cards = re.findall(r'<a[^>]*href="(/chapter/(\d+)/?)"[^>]*>([\s\S]*?)</a>', html)
print(f"Total cards on /hi: {len(cards)}")
seen = set()
for href, num, content in cards:
    if num in seen:
        continue
    seen.add(num)
    title = re.search(r'<h[23][^>]*>([\s\S]*?)</h[23]>', content)
    clean_title = re.sub(r'<[^>]+>', ' ', title.group(1)).strip() if title else ""
    p = re.search(r'<p[^>]*>([\s\S]*?)</p>', content)
    clean_p = re.sub(r'<[^>]+>', ' ', p.group(1)).strip() if p else ""
    v_match = re.search(r'(\d+)\s*(श्लोक|Verses)', content, re.I)
    v_count = v_match.group(1) if v_match else ""
    print(f"अध्याय {num}: {clean_title} | श्लोक: {v_count} | {clean_p[:100]}")
