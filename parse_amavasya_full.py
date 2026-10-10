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

clean = lambda t: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)).strip() if t else ""

def parse_full_cards(html, is_hi=False):
    blocks = re.split(r'(?=<div class="dpEventCard\s+dpFlexWrap)', html)
    results = []
    
    for b in blocks[1:]:
        if '<div class="dpEventDateTitle">' not in b:
            continue
            
        is_adhika = "dpLeapedMonthEventCard" in b[:80] or "dpAdhika" in b[:80]
        is_passed = "dpPassedEventCard" in b[:80]
        
        # Date
        m_date = re.search(r'<div class="dpEventDateTitle">(.*?)</div>', b)
        date_str = clean(m_date.group(1)) if m_date else ""
        
        # Vrats list - look inside dpEventCardLink
        m_link_div = re.search(r'<div class="dpEventCardLink">(.*?)</div>\s*</div>\s*</div>', b, re.DOTALL)
        vrats = []
        if m_link_div:
            # find all text in >text</a>
            vrat_matches = re.findall(r'>([^<]+)</a>', m_link_div.group(1))
            vrats = [clean(v) for v in vrat_matches if clean(v)]
            
        # Month & Tithi
        m_tithi = re.search(r'<div class="dpEventCardInfoTitle">(.*?)</div>', b)
        month_tithi = clean(m_tithi.group(1)) if m_tithi else ""
        
        # Begins & Ends
        # format: Begins - 12:03 <span class="dpTimeStamp">AM</span>, <span class="dpInlineBlock">Jan 18</span>
        m_beg = re.search(r'(?:Begins|प्रारम्भ)\s*-\s*([^<]+(?:<span[^>]*>[^<]+</span>)*[^<\n]*)', b)
        beg_str = clean(m_beg.group(0)) if m_beg else ""
        
        m_end = re.search(r'(?:Ends|समाप्त)\s*-\s*([^<]+(?:<span[^>]*>[^<]+</span>)*[^<\n]*)', b)
        end_str = clean(m_end.group(0)) if m_end else ""
        
        results.append({
            "isAdhika": is_adhika,
            "isPassed": is_passed,
            "date": date_str,
            "vrats": vrats,
            "monthTithi": month_tithi,
            "begins": beg_str,
            "ends": end_str
        })
    return results

en_parsed = parse_full_cards(en_html, False)
hi_parsed = parse_full_cards(hi_html, True)

print(f"EN Parsed ({len(en_parsed)}):")
for i, c in enumerate(en_parsed):
    print(f"[{i+1}] {c['date']} | Vrats: {c['vrats']} | {c['monthTithi']} | Adhika={c['isAdhika']} | {c['begins']} | {c['ends']}")

print(f"\nHI Parsed ({len(hi_parsed)}):")
for i, c in enumerate(hi_parsed):
    print(f"[{i+1}] {c['date']} | Vrats: {c['vrats']} | {c['monthTithi']} | Adhika={c['isAdhika']} | {c['begins']} | {c['ends']}")
