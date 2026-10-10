import urllib.request, urllib.parse, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Let's search YouTube search query or check video IDs
url = 'https://www.youtube.com/results?search_query=Tulsi+Chalisa+T-Series'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    vids = re.findall(r'/watch\?v=([a-zA-Z0-9_-]{11})', html)
    seen = set()
    found = []
    for v in vids:
        if v not in seen:
            seen.add(v)
            found.append(v)
    print("Found vids:", found[:8])
    for v in found[:5]:
        try:
            o_url = f'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={v}&format=json'
            with urllib.request.urlopen(o_url) as o_resp:
                data = json.loads(o_resp.read().decode('utf-8'))
                print(f"{v}: {data.get('title')} | {data.get('author_name')}")
        except Exception as e:
            pass
except Exception as e:
    print("Error:", e)
