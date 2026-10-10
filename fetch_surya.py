import urllib.request
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://www.drikpanchang.com/lyrics/aarti/lord-surya/surya-deva-aarti.html?lang=hi&ck=1'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Language': 'hi,en;q=0.9'
})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

groups = re.findall(r'class="dpLyricsAartiGroup">(.*?)</div>', html, re.DOTALL)
lines = []
for g in groups:
    spans = re.findall(r'class="dpRow[^"]*">(.*?)</span>', g)
    lines.append(' '.join(spans))

result = '\n'.join(lines)
with open('surya_lyrics.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print("Done. Lines:", len(lines))
print(result)
