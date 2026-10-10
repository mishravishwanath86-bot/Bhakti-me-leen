import re
import json

with open('raghuvar_hi.html', 'r', encoding='utf-8') as f:
    html_hi = f.read()

with open('raghuvar_en.html', 'r', encoding='utf-8') as f:
    html_en = f.read()

# YouTube Video ID
yt_match = re.search(r'(?:youtube\.com\/(?:embed\/|watch\?v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', html_hi)
video_id = yt_match.group(1) if yt_match else ""

# Extract title
m_title_hi = re.search(r'<title>(.*?)</title>', html_hi, re.I)
title_hi = m_title_hi.group(1) if m_title_hi else ""

m_title_en = re.search(r'<title>(.*?)</title>', html_en, re.I)
title_en = m_title_en.group(1) if m_title_en else ""

# Extract lyrics in Drik Panchang
# Drik Panchang typically formats lyrics in <div class="dpLyricsContent"> or <div class="dpVerse"> or has <p class="dpVerse">
# Let's inspect where "आरती कीजै श्री रघुवर" occurs
pos_hi = html_hi.find('आरती कीजै श्री रघुवर')
context_hi = html_hi[max(0, pos_hi - 200):min(len(html_hi), pos_hi + 3000)]

# Also in English
pos_en = html_en.find('Aarti')
# Let's find "Raghuvar" in en
pos_en = html_en.find('Raghuvar')
if pos_en == -1:
    pos_en = html_en.find('raghuvar')
context_en = html_en[max(0, pos_en - 200):min(len(html_en), pos_en + 3000)] if pos_en != -1 else ""

result = {
    "title_hi": title_hi,
    "title_en": title_en,
    "video_id": video_id,
    "context_hi_sample": context_hi[:1500],
    "context_en_sample": context_en[:1500]
}

with open('raghuvar_debug.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("Parsed and saved to raghuvar_debug.json")
