import sys
import urllib.request
import re
import html

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.drikpanchang.com/lyrics/aarti/yamuna-mata/yamuna-mata-aarti.html?lang=en&ck=1"
req = urllib.request.Request(
    url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
)

try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='replace')
        with open('yamuna_en.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Downloaded yamuna_en.html, size:", len(content))
        
        start_idx = content.find('class="dpLyricsEnglishFontWrapper"')
        if start_idx == -1:
            start_idx = content.find('class="dpLyricsDevanagariFontWrapper"')
        end_idx = content.find('</article>', start_idx)
        print("English snippet found:", start_idx != -1)
        if start_idx != -1:
            snippet = content[start_idx:end_idx]
            groups = re.findall(r'<div class="dpLyricsAartiGroup">(.*?)</div>', snippet, re.DOTALL)
            for g in groups[:3]:
                rows = re.findall(r'<span class="dpRow[^"]*">(.*?)</span>', g)
                print("Row:", [html.unescape(r).strip() for r in rows if r.strip()])
except Exception as e:
    print("Error:", e)
