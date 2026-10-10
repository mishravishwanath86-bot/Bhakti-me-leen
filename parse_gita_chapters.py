import urllib.request
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

req = urllib.request.Request('https://bhagavadgita.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Check script tags
scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', html)
print(f"Total script tags: {len(scripts)}")
for s in scripts:
    if 'Arjun' in s or 'Sānkhya' in s or 'chapter' in s:
        print("Script with chapter data found! Length:", len(s))
        if len(s) < 1000:
            print(s)
        else:
            print(s[:300])

# Parse chapters from the HTML cards directly
# Look for cards with Chapter X
cards = re.findall(r'<a[^>]*href="(/chapter/(\d+)/?)"[^>]*>([\s\S]*?)</a>', html)
print(f"Total cards found: {len(cards)}")
seen = set()
for href, chap_num, content in cards:
    if chap_num in seen:
        continue
    seen.add(chap_num)
    # clean content
    title = re.search(r'<h[23][^>]*>([\s\S]*?)</h[23]>', content)
    clean_title = re.sub(r'<[^>]+>', ' ', title.group(1)).strip() if title else ""
    # summary
    p = re.search(r'<p[^>]*>([\s\S]*?)</p>', content)
    clean_p = re.sub(r'<[^>]+>', ' ', p.group(1)).strip() if p else ""
    # verses count
    v_match = re.search(r'(\d+)\s*Verses', content, re.I)
    v_count = v_match.group(1) if v_match else ""
    print(f"Chapter {chap_num}: {clean_title} | Verses: {v_count} | {clean_p[:80]}")
