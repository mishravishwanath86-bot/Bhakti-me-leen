import urllib.request, re, json, time, os, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_collection_raw.html', encoding='utf-8') as f:
    html = f.read()

# 1. Parse all 54 Chalisas from collection HTML
sec_matches = list(re.finditer(r'<h[23][^>]*>(.*?)</h[23]>', html, re.DOTALL))
sections = []
for i, sm in enumerate(sec_matches):
    title = re.sub(r'<[^>]+>', ' ', sm.group(1)).strip()
    if 'चालीसा' in title and 'सम्बन्धित' not in title:
        start = sm.end()
        end = sec_matches[i+1].start() if i + 1 < len(sec_matches) else len(html)
        sections.append((title, start, end))

raw_chalisas = []
for sec_title, start_pos, end_pos in sections:
    sec_html = html[start_pos:end_pos]
    blocks = re.findall(r'<div class="dpFestivalTitle">(.*?)</div>\s*<a href="([^"]*lang=hi[^"]*)"[^>]*>(.*?)</a>\s*<br>\s*<a href="([^"]*lang=en[^"]*)"[^>]*>(.*?)</a>', sec_html, re.DOTALL)
    for title, hi_url, hi_line, en_url, en_line in blocks:
        raw_chalisas.append({
            'section': sec_title,
            'title': re.sub(r'<[^>]+>', ' ', title).strip(),
            'hi_line': re.sub(r'<[^>]+>', ' ', hi_line).strip(),
            'en_line': re.sub(r'<[^>]+>', ' ', en_line).strip(),
            'url': 'https://www.drikpanchang.com' + hi_url.split('&')[0].split('?')[0]
        })

print(f"Total to fetch: {len(raw_chalisas)}")

os.makedirs('chalisa_cache', exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

fetched_count = 0
for idx, c in enumerate(raw_chalisas):
    slug = f"{idx+1}_{c['url'].split('/')[-1].replace('.html', '')}"
    cache_path = os.path.join('chalisa_cache', f"{slug}.html")
    if not os.path.exists(cache_path):
        try:
            req = urllib.request.Request(c['url'] + '?lang=hi&ck=1', headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = resp.read().decode('utf-8', errors='ignore')
            with open(cache_path, 'w', encoding='utf-8') as f:
                f.write(data)
            fetched_count += 1
            print(f"[{idx+1}/{len(raw_chalisas)}] Fetched {c['title']} ({slug})")
            time.sleep(0.08)
        except Exception as e:
            print(f"[{idx+1}/{len(raw_chalisas)}] ERR fetching {c['title']}: {e}")

print(f"Done! Newly fetched: {fetched_count}")
