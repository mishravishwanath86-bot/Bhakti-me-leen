import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('sharda_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the aarti start
start_marker = '॥ \u0936\u094d\u0930\u0940 \u0936\u093e\u0930\u0926\u093e \u092e\u093e\u0924\u093e \u091c\u0940 \u0915\u0940 \u0906\u0930\u0924\u0940 ॥'  # ॥ श्री शारदा माता जी की आरती ॥
idx = html.find(start_marker)
print(f"Start marker at: {idx}")

# Extract chunk
chunk = html[idx:idx+12000]

# Find end
end_markers = ['dpFontResizeButton', 'dpContentComments', 'dpAdsWidget', 'dpLyricsFooter']
end_pos = len(chunk)
for em in end_markers:
    ep = chunk.find(em)
    if ep > 0 and ep < end_pos:
        end_pos = ep
        print(f"End marker '{em}' at: {ep}")

aarti_html = chunk[:end_pos]

# Find all dpLyricsAartiGroup divs
groups = re.findall(r'<div class="dpLyricsAartiGroup">(.*?)</div>', aarti_html, re.DOTALL)
print(f"Found {len(groups)} lyric groups")

# Extract text
full_lyrics = ['॥ श्री शारदा माता जी की आरती ॥', '']

for group in groups:
    spans = re.findall(r'<span[^>]*>(.*?)</span>', group, re.DOTALL)
    if spans:
        group_lines = []
        for span in spans:
            text = re.sub(r'<[^>]+>', '', span).strip()
            if text:
                group_lines.append(text)
        if group_lines:
            full_lyrics.extend(group_lines)
            full_lyrics.append('')

print("\n=== SHARDA MATA AARTI LYRICS ===")
for line in full_lyrics:
    print(line)

lyrics_text = '\n'.join(full_lyrics).strip()
with open('sharda_aarti_lyrics.txt', 'w', encoding='utf-8') as f:
    f.write(lyrics_text)
print(f"\nSaved ({len(lyrics_text)} chars, {len(full_lyrics)} lines)")
