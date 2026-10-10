import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

req = urllib.request.Request('https://www.drikpanchang.com/lyrics/ramcharitmanas/sundarkand/sundarkand-lyrics.html?page=2', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

l_start = html.find('class="dpMiddleTitle"')
next_div = html.find('class="dpFooter"', l_start)
content = html[l_start:next_div]

items = re.findall(r'(<h3[^>]*class="[^"]*dpLyricsType[^"]*"[^>]*>[\s\S]*?</h3>|<p[^>]*class="[^"]*dpGroup[^"]*"[^>]*>[\s\S]*?</p>)', content)
print(f"Total items in Page 2: {len(items)}")

current_heading = "START"
for item in items[:15]:
    if '<h3' in item:
        current_heading = re.sub(r'<[^>]+>', '', item).strip()
        print(f"\n--- {current_heading} ---")
    else:
        lines = re.findall(r'<span class="dpRow">([\s\S]*?)</span>', item)
        clean_lines = [re.sub(r'<[^>]+>', '', l).strip() for l in lines]
        for l in clean_lines:
            print("  ", l)
