import sys
import urllib.request
import re
import html

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.drikpanchang.com/lyrics/aarti/shri-parashurama/shri-parashurama-aarti.html?lang=hi&ck=1"
req = urllib.request.Request(
    url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'hi,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
)

try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='replace')
        with open('parashurama_raw.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Downloaded parashurama_raw.html, size:", len(content))
        
        # Check YouTube links
        yt_links = re.findall(r'https?://[^\s"\'<>]+youtube[^\s"\'<>]+', content)
        print("YouTube links:", yt_links)
        
        # Check video embed
        dp_video = re.findall(r'dpYoutubeVideoId.*?src="([^"]+)"', content)
        print("dpYoutubeVideoId:", dp_video)
        
        # Check title
        m_title = re.search(r'<title>(.*?)</title>', content)
        print("Title:", m_title.group(1) if m_title else "No title")
except Exception as e:
    print("Error:", e)
