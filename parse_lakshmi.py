import re

with open('lakshmi_mata_hi.html', 'r', encoding='utf-8') as f:
    hi_html = f.read()

# 1. YouTube Video ID
iframes = re.findall(r'<iframe[^>]*src=["\']([^"\']+)["\']', hi_html)
print('HI iframes:', iframes)

yt_matches = re.findall(r'(?:youtube\.com/embed/|youtu\.be/|data-yt-id=["\'])([a-zA-Z0-9_-]{11})', hi_html)
print('YT matches:', yt_matches)

# 2. Extract lyrics block
idx = hi_html.find('id="dpLyricsBlockId"')
if idx == -1:
    idx = hi_html.find("dpLyricsBlock")
snippet = hi_html[idx:]
comments_idx = snippet.find('id="commentsSection"')
if comments_idx != -1:
    snippet = snippet[:comments_idx]

groups = re.findall(r'<div class="dpLyricsAartiGroup">(.*?)</div>', snippet, re.DOTALL)
print(f'Total groups in HI: {len(groups)}')

with open('lakshmi_parsed_lyrics.txt', 'w', encoding='utf-8') as out:
    out.write(f'Total groups: {len(groups)}\n')
    for i, g in enumerate(groups):
        rows = re.findall(r'<span class="dpRow[^"]*">(.*?)</span>', g, re.DOTALL)
        if rows:
            clean_rows = [re.sub(r'<[^>]+>', '', r).strip() for r in rows if r.strip()]
            out.write(f"\nGroup {i+1}:\n" + "\n".join(clean_rows) + "\n")
        else:
            clean = re.sub(r'<[^>]+>', ' ', g).strip()
            out.write(f"\nGroup {i+1} (raw):\n{clean}\n")

with open('lakshmi_mata_en.html', 'r', encoding='utf-8') as f:
    en_html = f.read()

idx_en = en_html.find('id="dpLyricsBlockId"')
if idx_en == -1:
    idx_en = en_html.find("dpLyricsBlock")
snippet_en = en_html[idx_en:]
comments_idx_en = snippet_en.find('id="commentsSection"')
if comments_idx_en != -1:
    snippet_en = snippet_en[:comments_idx_en]

groups_en = re.findall(r'<div class="dpLyricsAartiGroup">(.*?)</div>', snippet_en, re.DOTALL)
with open('lakshmi_en_parsed.txt', 'w', encoding='utf-8') as out:
    out.write(f'Total groups in EN: {len(groups_en)}\n')
    for i, g in enumerate(groups_en):
        rows = re.findall(r'<span class="dpRow[^"]*">(.*?)</span>', g, re.DOTALL)
        if rows:
            clean_rows = [re.sub(r'<[^>]+>', '', r).strip() for r in rows if r.strip()]
            out.write(f"\nGroup {i+1}:\n" + "\n".join(clean_rows) + "\n")

print("Wrote lakshmi_parsed_lyrics.txt and lakshmi_en_parsed.txt successfully.")
