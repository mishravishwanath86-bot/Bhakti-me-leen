import re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_collection_raw.html', encoding='utf-8') as f:
    html = f.read()

# We need to associate cards with their section headings:
# देवताओं की चालीसा, देवियों की चालीसा, सन्तों की चालीसा, अन्य चालीसा

# Find sections
sections = []
sec_matches = list(re.finditer(r'<h[23][^>]*>(.*?)</h[23]>', html, re.DOTALL))
for i, sm in enumerate(sec_matches):
    title = re.sub(r'<[^>]+>', ' ', sm.group(1)).strip()
    if 'चालीसा' in title and 'सम्बन्धित' not in title:
        start = sm.end()
        end = sec_matches[i+1].start() if i + 1 < len(sec_matches) else len(html)
        sections.append((title, start, end))

print(f"Sections found: {[s[0] for s in sections]}")

chalisas = []
for sec_title, start_pos, end_pos in sections:
    sec_html = html[start_pos:end_pos]
    
    # Split by dpAnchorMultiLinksBlock or dpFestivalTitle
    # Each chalisa block typically has <div class="dpFestivalTitle">...</div>
    blocks = re.findall(r'<div class="dpFestivalTitle">(.*?)</div>\s*<a href="([^"]*lang=hi[^"]*)"[^>]*>(.*?)</a>\s*<br>\s*<a href="([^"]*lang=en[^"]*)"[^>]*>(.*?)</a>', sec_html, re.DOTALL)
    print(f"Section '{sec_title}': found {len(blocks)} chalisas")
    
    for title, hi_url, hi_line, en_url, en_line in blocks:
        clean_title = re.sub(r'<[^>]+>', ' ', title).strip()
        clean_hi_line = re.sub(r'<[^>]+>', ' ', hi_line).strip()
        clean_en_line = re.sub(r'<[^>]+>', ' ', en_line).strip()
        
        chalisas.append({
            'section': sec_title,
            'title': clean_title,
            'hi_line': clean_hi_line,
            'en_line': clean_en_line,
            'drik_url': 'https://www.drikpanchang.com' + hi_url.split('&')[0]
        })

print(f"\nTotal parsed Chalisas: {len(chalisas)}")
for idx, c in enumerate(chalisas):
    print(f"{idx+1}. [{c['section']}] {c['title']} | {c['hi_line']} | {c['drik_url']}")
