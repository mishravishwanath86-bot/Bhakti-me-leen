import urllib.request
import re
import json

url = 'https://www.drikpanchang.com/lyrics/aarti/ekadashi/ekadashi-aarti.html?lang=hi&ck=1'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='replace')
    print("Fetched OK, len:", len(html))
    
    # Save for inspection
    with open('ekadashi_raw.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Saved to ekadashi_raw.html")
    
    # Try to find the lyrics div
    # DrikPanchang typically uses dpLyricsText class
    match = re.search(r'class="dpLyricsText[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)
    if match:
        print("Found dpLyricsText:", match.group(1)[:500])
    else:
        print("dpLyricsText not found, trying other patterns...")
    
    # Find all devanagari text blocks
    lines = html.split('\n')
    deva_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped and re.search(r'[\u0900-\u097F]', stripped) and len(stripped) > 5:
            # Remove HTML tags
            clean = re.sub(r'<[^>]+>', '', stripped)
            clean = clean.strip()
            if clean and len(clean) > 3 and re.search(r'[\u0900-\u097F]', clean):
                deva_lines.append(clean)
    
    print(f"\nFound {len(deva_lines)} devanagari lines")
    for l in deva_lines[:50]:
        print(repr(l))

except Exception as e:
    print("Error:", e)
