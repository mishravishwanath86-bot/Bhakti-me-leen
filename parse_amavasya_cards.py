import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

en_file = r'C:\Users\vishw\.gemini\antigravity-ide\brain\85d64534-ea39-4946-988b-be7eeefc13c3\.system_generated\steps\8203\content.md'
hi_file = r'C:\Users\vishw\.gemini\antigravity-ide\brain\85d64534-ea39-4946-988b-be7eeefc13c3\.system_generated\steps\8205\content.md'

with open(en_file, 'r', encoding='utf-8') as f:
    en_html = f.read()

with open(hi_file, 'r', encoding='utf-8') as f:
    hi_html = f.read()

# Header titles
m_title_en = re.search(r'<div class="dpTableCardHeaderTitle">(.*?)</div>', en_html)
m_sub_en = re.search(r'<div class="dpTableCardHeaderSubTitle">(.*?)</div>', en_html)
print("EN Header Title:", clean := lambda t: re.sub(r'<[^>]+>', ' ', t).strip() if t else "", clean(m_title_en.group(1)) if m_title_en else "")
print("EN Header SubTitle:", clean(m_sub_en.group(1)) if m_sub_en else "")

# Regex for each card block
card_regex = re.compile(r'<div class="dpEventCard\s+dpFlexWrap([^"]*)"[^>]*>(.*?)</div>\s*</div>\s*</div>', re.DOTALL)

def parse_cards(html):
    cards = []
    # Find each card
    matches = re.finditer(r'<div class="dpEventCard\s+dpFlexWrap([^"]*)"[^>]*>(.*?)(?=<div class="dpEventCard\s+dpFlexWrap|\Z)', html, re.DOTALL)
    for m in matches:
        classes = m.group(1)
        body = m.group(2)
        
        is_adhika = "dpAdhika" in classes
        is_passed = "dpPassed" in classes
        
        # Date title
        date_m = re.search(r'<div class="dpEventDateTitle">(.*?)</div>', body)
        date_title = clean(date_m.group(1)) if date_m else ""
        
        # Links / Vrats
        links = re.findall(r'<a [^>]*>([^<]+)</a>', body)
        # remove empty or weird links
        vrats = [clean(l) for l in links if clean(l) and not "Panchang" in l]
        
        # Lunar month & tithi
        month_m = re.search(r'<div class="dpEventCardInfoTitle">(.*?)</div>', body)
        month_tithi = clean(month_m.group(1)) if month_m else ""
        
        # Begins and ends
        begins_m = re.search(r'Begins\s*-\s*([^<]+(?:<span[^>]*>[^<]+</span>)*[^<]*)', body)
        begins = clean(begins_m.group(0)) if begins_m else ""
        
        ends_m = re.search(r'Ends\s*-\s*([^<]+(?:<span[^>]*>[^<]+</span>)*[^<]*)', body)
        ends = clean(ends_m.group(0)) if ends_m else ""
        
        # Hindi begins / ends
        if not begins:
            begins_m_hi = re.search(r'प्रारम्भ\s*-\s*([^<]+(?:<span[^>]*>[^<]+</span>)*[^<]*)', body)
            begins = clean(begins_m_hi.group(0)) if begins_m_hi else ""
        if not ends:
            ends_m_hi = re.search(r'समाप्त\s*-\s*([^<]+(?:<span[^>]*>[^<]+</span>)*[^<]*)', body)
            ends = clean(ends_m_hi.group(0)) if ends_m_hi else ""
            
        cards.append({
            "classes": classes.strip(),
            "isAdhika": is_adhika,
            "isPassed": is_passed,
            "dateTitle": date_title,
            "vrats": vrats,
            "monthTithi": month_tithi,
            "begins": begins,
            "ends": ends
        })
    return cards

en_cards = parse_cards(en_html)
hi_cards = parse_cards(hi_html)

print(f"\nTotal EN Cards: {len(en_cards)}")
for i, c in enumerate(en_cards):
    print(f"[{i+1}] {c['dateTitle']} | {c['vrats']} | {c['monthTithi']} | Adhika={c['isAdhika']} | {c['begins']} | {c['ends']}")

print(f"\nTotal HI Cards: {len(hi_cards)}")
for i, c in enumerate(hi_cards):
    print(f"[{i+1}] {c['dateTitle']} | {c['vrats']} | {c['monthTithi']} | Adhika={c['isAdhika']} | {c['begins']} | {c['ends']}")
