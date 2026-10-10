import os, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_collection_raw.html', encoding='utf-8') as f:
    html = f.read()

# Load deity config
from build_chalisa_config import DEITY_CONFIG

# Parse all 54 items from collection page
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

print(f"Total raw chalisas: {len(raw_chalisas)}")

cache_dir = 'chalisa_cache'
parsed_items = []

for idx, c in enumerate(raw_chalisas):
    slug = f"{idx+1}_{c['url'].split('/')[-1].replace('.html', '')}"
    cache_path = os.path.join(cache_dir, f"{slug}.html")
    
    content_text = ""
    yt_id = ""
    if os.path.exists(cache_path):
        with open(cache_path, encoding='utf-8') as f:
            ch_html = f.read()
        
        # YouTube iframe
        yt = re.findall(r'youtube\.com/embed/([a-zA-Z0-9_-]+)', ch_html)
        if yt:
            yt_id = yt[0]
            
        # P tags for lyrics
        p_tags = re.findall(r'<p[^>]*>(.*?)</p>', ch_html, re.DOTALL)
        verses = []
        for p in p_tags:
            clean = re.sub(r'<[^>]+>', ' ', p).strip()
            clean = re.sub(r'\s+', ' ', clean)
            # Skip promotional or nav text
            if any(skip in clean for skip in ['आरती संग्रह', 'चालीसा संग्रह', 'डाउनलोड', 'टिप्पणी', 'गूगल', 'Drik Panchang', 'कॉपीराइट', 'Privacy', 'Terms']):
                continue
            if '॥' in clean or 'दोहा' in clean or 'चौपाई' in clean or 'सोरठा' in clean or 'छन्द' in clean:
                verses.append(clean)
            elif len(clean) > 15 and ('जय' in clean or 'नमो' in clean or 'कृपा' in clean or 'प्रभु' in clean or 'दीन' in clean or 'सुमिरौं' in clean):
                verses.append(clean)
        
        content_text = f"॥ {c['title']} ॥\n\n" + "\n\n".join(verses)
    
    parsed_items.append({
        'num': idx + 1,
        'id': f"drik_chalisa_{idx+1}",
        'title': c['title'],
        'hi_line': c['hi_line'],
        'en_line': c['en_line'],
        'section': c['section'],
        'drik_url': c['url'] + "?lang=hi",
        'video_id': yt_id,
        'audio_url': f"https://www.youtube.com/watch?v={yt_id}" if yt_id else "",
        'verse_count': len(content_text.split('\n\n')) - 1,
        'content': content_text,
        'raw_url': c['url']
    })

print(f"Parsed {len(parsed_items)} items successfully!")
print("Sample item 1:", parsed_items[0]['title'], "verses:", parsed_items[0]['verse_count'])
print("Sample item 35:", parsed_items[34]['title'], "verses:", parsed_items[34]['verse_count'])
