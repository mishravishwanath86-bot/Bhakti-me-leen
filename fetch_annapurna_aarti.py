import urllib.request
import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://www.drikpanchang.com/lyrics/aarti/annapurna-mata/annapurna-mata-aarti.html?lang=hi&ck=1'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='replace')
    print("Fetched OK, len:", len(html))
    with open('annapurna_raw.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Saved to annapurna_raw.html")

    # Find the aarti section using danda markers
    danda = '॥'
    positions = [m.start() for m in re.finditer(re.escape(danda), html)]
    print(f"Found {len(positions)} danda occurrences")
    for pos in positions[:8]:
        snippet = html[pos:pos+200]
        clean = re.sub(r'<[^>]+>', '', snippet)
        clean = re.sub(r'\s+', ' ', clean).strip()
        print(f"  At {pos}: {repr(clean[:120])}")

except Exception as e:
    print("Error:", type(e).__name__, e)
