import urllib.request, re, sys, json

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

# Fetch English transliteration
url_en = 'https://www.drikpanchang.com/lyrics/chalisa/lord-hanuman/bajarang-baan/shri-bajarang-baan.html?lang=en'
try:
    req = urllib.request.Request(url_en, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as res:
        en_html = res.read().decode('utf-8')
    with open('chalisa_cache/2_shri-bajarang-baan_en.html', 'w', encoding='utf-8') as f:
        f.write(en_html)
    print("Successfully fetched English page, length:", len(en_html))
except Exception as e:
    print("Error fetching English page:", e)

# Also let's check what YouTube video is best for Bajrang Baan.
# Popular verified Bajrang Baan YouTube videos:
# 1. Hariharan / Gulshan Kumar / T-Series Bajrang Baan:
# Let's search YouTube for Bajrang Baan T-Series / Hariharan / Rasraj
# Let's test a couple of well-known Bajrang Baan video IDs via noembed
test_vids = [
    'fO_X4fCgq1A', # T-Series Bajrang Baan Hariharan
    'X4oUjN2l2L8', 
    'p7vKqZ7uK-M',
    'aOQhX5yKaLU', # The one on Drik Panchang
    'qEa8K3P6-pE'
]

for vid in test_vids:
    try:
        url = f'https://noembed.com/embed?url=https://www.youtube.com/watch?v={vid}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        data = json.loads(res.read().decode('utf-8'))
        print(f"Video {vid}: {data.get('title')} ({data.get('author_name')})")
    except Exception as e:
        pass
