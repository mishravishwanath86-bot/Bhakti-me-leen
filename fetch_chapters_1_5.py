import urllib.request
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for ch in [1, 2, 3, 4, 5]:
    for lang in ['', '/hi']:
        url = f"https://bhagavadgita.com/chapter/{ch}{lang}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as res:
                html = res.read().decode('utf-8', errors='ignore')
                suffix = '_hi' if lang else '_en'
                fn = f"chapter_{ch}{suffix}.html"
                with open(fn, 'w', encoding='utf-8') as out:
                    out.write(html)
                # Count verses
                v_ids = re.findall(r'<div id="verse-([^"]+)"', html)
                print(f"Chapter {ch}{suffix} fetched ({len(html)} bytes). Verses listed: {len(v_ids)}: {v_ids[:5]}...")
        except Exception as e:
            print(f"Error fetching {url}: {e}")
