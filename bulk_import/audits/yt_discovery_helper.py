import urllib.request, urllib.parse, json, time, re, ssl, sqlite3, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def search_youtube_videos(query, max_results=5):
    encoded = urllib.parse.quote_plus(query)
    url = f"https://www.youtube.com/results?search_query={encoded}"
    req = urllib.request.Request(url, headers=HEADERS)
    results = []
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
            html = response.read().decode('utf-8', errors='ignore')
            # Extract initial data JSON
            m = re.search(r'var ytInitialData\s*=\s*({.+?});</script>', html)
            if not m:
                m = re.search(r'window\["ytInitialData"\]\s*=\s*({.+?});', html)
            
            if m:
                data = json.loads(m.group(1))
                contents = []
                try:
                    section = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents']
                    for s in section:
                        if 'itemSectionRenderer' in s:
                            contents.extend(s['itemSectionRenderer']['contents'])
                except Exception:
                    pass
                
                for item in contents:
                    if 'videoRenderer' in item:
                        vr = item['videoRenderer']
                        vid = vr.get('videoId')
                        title = vr.get('title', {}).get('runs', [{}])[0].get('text', '')
                        channel = vr.get('ownerText', {}).get('runs', [{}])[0].get('text', '')
                        length_text = vr.get('lengthText', {}).get('simpleText', '')
                        if vid and title:
                            results.append({
                                "youtube_id": vid,
                                "youtube_url": f"https://www.youtube.com/watch?v={vid}",
                                "title": title,
                                "channel": channel,
                                "duration": length_text
                            })
                            if len(results) >= max_results:
                                break
    except Exception as e:
        print(f"Error searching '{query}': {e}", file=sys.stderr)
    return results

def verify_oembed(vid):
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=8, context=ctx) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return {
                    "live": True,
                    "title": data.get("title", ""),
                    "channel": data.get("author_name", "")
                }
    except Exception:
        pass
    return {"live": False, "title": "", "channel": ""}

print("Search & OEmbed helper loaded successfully.")
