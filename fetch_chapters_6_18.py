import urllib.request
import re
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for ch in range(6, 19):
    url = f"https://bhagavadgita.com/chapter/{ch}/hi"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as res:
            html = res.read().decode('utf-8', errors='ignore')
            fn = f"chapter_{ch}_hi.html"
            with open(fn, 'w', encoding='utf-8') as out:
                out.write(html)
            
            # Extract intro paragraph
            m = re.search(r'<p class="text-justify font-serif text-lg leading-loose text-foreground/90">(.*?)</p>', html, re.DOTALL)
            intro_len = len(re.sub(r'<[^>]+>', '', m.group(1)).strip()) if m else 0
            print(f"Chapter {ch}_hi fetched ({len(html)} bytes). Intro length: {intro_len} chars.")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    time.sleep(0.5)

print("\nAll chapters 6-18 fetch completed.")
