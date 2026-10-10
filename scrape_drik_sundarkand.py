import urllib.request
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect page 1 and page 2
url1 = 'https://www.drikpanchang.com/lyrics/ramcharitmanas/sundarkand/sundarkand-lyrics.html'
req = urllib.request.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print("Page 1 length:", len(html))

# Let's check sections in page 1
# Find all dpLyricsType and dpGroup
types = re.findall(r'<h3 class="dpLyricsType\s*">([\s\S]*?)</h3>', html)
print("dpLyricsType headings in page 1:")
for t in types:
    print(" -", re.sub(r'<[^>]+>', ' ', t).strip())

# Check how p.dpGroup and verses are structured
groups = re.findall(r'<p class="dpGroup">([\s\S]*?)</p>', html)
print(f"Total dpGroup paragraphs in page 1: {len(groups)}")
if groups:
    print("Sample group 0:")
    print(re.sub(r'<[^>]+>', '\n', groups[0]).strip()[:200])

# Check if meaning / भावार्थ is present on drik panchang or if there's any commentary
meanings = re.findall(r'<div class="dpLyricsMeaning">([\s\S]*?)</div>', html)
print("dpLyricsMeaning found:", len(meanings))

# Check for any english or hindi translation
trans = re.findall(r'<p class="dpMeaning">([\s\S]*?)</p>', html)
print("dpMeaning found:", len(trans))
