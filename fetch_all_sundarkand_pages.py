import urllib.request
import re
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_url = 'https://www.drikpanchang.com/lyrics/ramcharitmanas/sundarkand/sundarkand-lyrics.html'

all_pages = {}

for p in range(1, 11):
    url = base_url if p == 1 else f"{base_url}?page={p}"
    print(f"Fetching page {p} from {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            all_pages[p] = html
            print(f" Page {p}: {len(html)} chars fetched.")
    except Exception as e:
        print(f" Error page {p}: {e}")
    time.sleep(0.5)

# Save raw pages to a json cache
with open('sundarkand_raw_pages.json', 'w', encoding='utf-8') as f:
    json.dump(all_pages, f, ensure_ascii=False)
print("Saved all 10 pages to sundarkand_raw_pages.json")
