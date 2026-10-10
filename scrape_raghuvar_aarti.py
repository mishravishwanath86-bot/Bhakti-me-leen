import urllib.request
import re
from html.parser import HTMLParser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_url(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode('utf-8')

print("Fetching Hindi...")
url_hi = "https://www.drikpanchang.com/lyrics/aarti/shree-rama/shri-raghuvar-aarti.html?lang=hi&ck=1"
html_hi = fetch_url(url_hi)
with open('raghuvar_hi.html', 'w', encoding='utf-8') as f:
    f.write(html_hi)

print("Fetching English...")
url_en = "https://www.drikpanchang.com/lyrics/aarti/shree-rama/shri-raghuvar-aarti.html?lang=en&ck=1"
html_en = fetch_url(url_en)
with open('raghuvar_en.html', 'w', encoding='utf-8') as f:
    f.write(html_en)

print("Saved HTML files.")

# Extract title
m_title_hi = re.search(r'<title>(.*?)</title>', html_hi, re.I)
print("Title HI:", m_title_hi.group(1) if m_title_hi else "None")

m_title_en = re.search(r'<title>(.*?)</title>', html_en, re.I)
print("Title EN:", m_title_en.group(1) if m_title_en else "None")

# YouTube Video ID
yt_match = re.search(r'(?:youtube\.com\/(?:embed\/|watch\?v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', html_hi)
if yt_match:
    print("YouTube Video ID:", yt_match.group(1))
else:
    print("No direct YouTube match in html_hi")

# Extract lyrics block
# Drik Panchang typically has <div class="dpLyricsWrapper"> or <div class="dpLyrics"> or <div class="dpPageCard">
class LyricsExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_lyrics = False
        self.current_tag = None
        self.lyrics_text = []
        self.depth = 0
        self.target_depth = 0

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        classes = attr_dict.get('class', '')
        if 'dpLyrics' in classes or 'dpCardContent' in classes or 'dpVerse' in classes:
            self.in_lyrics = True
            self.target_depth = self.depth
        if tag == 'br' and self.in_lyrics:
            self.lyrics_text.append('\n')
        self.depth += 1

    def handle_endtag(self, tag):
        self.depth -= 1
        if self.in_lyrics and self.depth <= self.target_depth:
            # Maybe keep going if wrapper
            pass

    def handle_data(self, data):
        if self.in_lyrics:
            self.lyrics_text.append(data)

# Let's inspect using regex around <div class=".*lyrics.*"> or similar
div_matches = re.findall(r'<div[^>]*class="[^"]*(?:lyrics|Verse|dpLyrics)[^"]*"[^>]*>(.*?)</div>', html_hi, re.I | re.DOTALL)
print(f"Found {len(div_matches)} regex div matches for lyrics in HI")

# Let's write an inspector script to find the exact stanzas
