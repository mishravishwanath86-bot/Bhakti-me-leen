import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

en_file = r'C:\Users\vishw\.gemini\antigravity-ide\brain\85d64534-ea39-4946-988b-be7eeefc13c3\.system_generated\steps\8203\content.md'

with open(en_file, 'r', encoding='utf-8') as f:
    html = f.read()

# find all card divs
# Each card is <div class="dpEventCard ...">...</div> that precedes another dpEventCard or end of container
card_blocks = re.split(r'(?=<div class="dpEventCard\s+dpFlexWrap)', html)
print(f"Total blocks: {len(card_blocks)}")

clean = lambda t: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)).strip() if t else ""

cards = []
for b in card_blocks[1:]:
    # stop at comments or ads or end of cards
    if not '<div class="dpEventDateTitle">' in b:
        continue
    # isolate this card
    card_html = b[:b.find('</div></div></div>') + 18] if '</div></div></div>' in b else b[:1500]
    
    # Adhika?
    is_adhika = 'dpAdhika' in b[:60]
    is_passed = 'dpPassed' in b[:60]
    
    # date
    m_date = re.search(r'<div class="dpEventDateTitle">(.*?)</div>', b)
    date_str = clean(m_date.group(1)) if m_date else ""
    
    # vrats inside dpEventCardLink
    m_links = re.search(r'<div class="dpEventCardLink">(.*?)</div>\s*</div>', b, re.DOTALL)
    vrats = []
    if m_links:
        vrats = re.findall(r'<a [^>]*>([^<]+)</a>', m_links.group(1))
        vrats = [clean(v) for v in vrats if clean(v)]
        
    # tithi title
    m_tithi = re.search(r'<div class="dpEventCardInfoTitle">(.*?)</div>', b)
    tithi_title = clean(m_tithi.group(1)) if m_tithi else ""
    
    # begins / ends
    # e.g. Begins - 12:03 <span class="dpTimeStamp">AM</span>, <span class="dpInlineBlock">Jan 18</span>
    m_begins = re.search(r'Begins\s*-\s*([^<]+<span[^>]*>[^<]+</span>,\s*<span[^>]*>[^<]+</span>)', b)
    if not m_begins:
        m_begins = re.search(r'Begins\s*-\s*([^<]+,\s*[^<]+)', b)
    begins_str = clean(m_begins.group(0)) if m_begins else ""
    
    m_ends = re.search(r'Ends\s*-\s*([^<]+<span[^>]*>[^<]+</span>,\s*<span[^>]*>[^<]+</span>)', b)
    if not m_ends:
        m_ends = re.search(r'Ends\s*-\s*([^<]+,\s*[^<]+)', b)
    ends_str = clean(m_ends.group(0)) if m_ends else ""
    
    cards.append({
        "date": date_str,
        "isAdhika": is_adhika,
        "isPassed": is_passed,
        "vrats": vrats,
        "monthTithi": tithi_title,
        "begins": begins_str,
        "ends": ends_str
    })

print(f"Parsed {len(cards)} cards:")
for i, c in enumerate(cards):
    print(f"{i+1}. {c['date']} | Vrats: {c['vrats']} | {c['monthTithi']} | Adhika: {c['isAdhika']} | {c['begins']} | {c['ends']}")
