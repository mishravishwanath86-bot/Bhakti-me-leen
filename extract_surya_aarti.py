import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('surya_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the aarti start - ॥ आरती श्री सूर्य जी ॥
start_marker = '॥ \u0906\u0930\u0924\u0940 \u0936\u094d\u0930\u0940 \u0938\u0942\u0930\u094d\u092f \u091c\u0940 ॥'
idx = html.find(start_marker)
print(f"Start marker at: {idx}")

chunk = html[idx:idx+12000]

# Find end
end_markers = ['dpFontResizeButton', 'dpContentComments', 'dpAdsWidget']
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

# Extract
full_lyrics = ['॥ आरती श्री सूर्य जी ॥', '']

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

print("\n=== SURYA DEV AARTI LYRICS ===")
for line in full_lyrics:
    print(line)

lyrics_text = '\n'.join(full_lyrics).strip()
with open('surya_aarti_lyrics.txt', 'w', encoding='utf-8') as f:
    f.write(lyrics_text)
print(f"\nSaved ({len(lyrics_text)} chars)")
