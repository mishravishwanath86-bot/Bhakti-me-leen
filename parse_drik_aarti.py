import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\vishw\.gemini\antigravity-ide\brain\85d64534-ea39-4946-988b-be7eeefc13c3\.system_generated\steps\11602\content.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.split(r'<h3 class="dpMiddleTitle">([^<]+)</h3>', text)
print(f'Found {len(sections)//2} deity categories:\n')

aarti_categories = []

for i in range(1, len(sections), 2):
    cat_name = sections[i].strip()
    cat_content = sections[i+1]
    
    # Extract blocks
    blocks = re.findall(r'<div class="dpLyricsAnchorBlock[^"]*">([\s\S]*?)</div>\s*</div>\s*</div>', cat_content)
    
    # Also extract cards using simpler regex if blocks tricky
    card_matches = re.findall(
        r'<img\s+src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>[\s\S]*?<div class="dpFestivalTitle">([^<]+)</div>\s*<a href="([^"]+)" class="dpAnchorLink">([^<]+)</a><br>\s*<a href="([^"]+)" class="dpAnchorLink">([^<]+)</a>',
        cat_content
    )
    
    cat_data = {
        'category': cat_name,
        'count': len(card_matches),
        'items': []
    }
    
    for m in card_matches:
        img_src, alt_deity, fest_title, en_url, en_line, hi_url, hi_line = m
        cat_data['items'].append({
            'title': fest_title.strip(),
            'en_line': en_line.strip(),
            'hi_line': hi_line.strip(),
            'en_url': en_url.strip(),
            'hi_url': hi_url.strip(),
            'img_src': img_src.strip(),
            'alt_deity': alt_deity.strip()
        })
        
    aarti_categories.append(cat_data)
    print(f"• {cat_name} ({len(card_matches)} aartis):")
    for item in cat_data['items']:
        print(f"    - {item['title']} | {item['en_line']} | {item['hi_line']}")

with open('drik_aarti_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(aarti_categories, f, ensure_ascii=False, indent=2)

print("\n✓ Saved to drik_aarti_parsed.json")
