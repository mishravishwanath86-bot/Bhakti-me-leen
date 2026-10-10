import urllib.request
import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://www.drikpanchang.com/lyrics/aarti/sharda-mata/sharda-mata-aarti.html?lang=hi&ck=1'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='replace')
    print("Fetched OK, len:", len(html))
    with open('sharda_raw.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Saved.")

    # Find danda positions
    danda = '॥'
    positions = [m.start() for m in re.finditer(re.escape(danda), html)]
    print(f"Found {len(positions)} danda occurrences")
    for pos in positions[:10]:
        snippet = html[pos:pos+200]
        clean = re.sub(r'<[^>]+>', '', snippet)
        clean = re.sub(r'\s+', ' ', clean).strip()
        print(f"  At {pos}: {repr(clean[:130])}")

    # Now extract lyrics
    # Find the aarti title
    search_terms = ['\u0936\u093e\u0930\u0926\u093e \u092e\u093e\u0924\u093e', '\u0936\u093e\u0930\u0926\u0947', '\u0936\u093e\u0930\u0926\u093e']
    for term in search_terms:
        idx = html.find('॥')
        # Find the first danda that has sharda content nearby
        for pos in positions:
            snippet = html[pos:pos+300]
            clean = re.sub(r'<[^>]+>', '', snippet)
            if '\u0936\u093e\u0930\u0926' in clean and '\u0906\u0930\u0924\u0940' in clean:
                print(f"\nFound aarti section at {pos}")
                break

except Exception as e:
    print("Error:", type(e).__name__, e)
