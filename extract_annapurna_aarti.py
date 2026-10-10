import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('annapurna_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the aarti start
start_marker = '॥ \u0936\u094d\u0930\u0940 \u0905\u0928\u094d\u0928\u092a\u0942\u0930\u094d\u0923\u093e \u092e\u093e\u0924\u093e \u091c\u0940 \u0915\u0940 \u0906\u0930\u0924\u0940 ॥'  # ॥ श्री अन्नपूर्णा माता जी की आरती ॥
idx = html.find(start_marker)
print(f"Start marker at: {idx}")

if idx < 0:
    # Try alternate
    start_marker = '\u0936\u094d\u0930\u0940 \u0905\u0928\u094d\u0928\u092a\u0942\u0930\u094d\u0923\u093e \u092e\u093e\u0924\u093e'
    idx = html.find(start_marker)
    print(f"Alt marker at: {idx}")

# Extract chunk
chunk = html[idx:idx+10000]

# Find end - look for font resize button or other end marker
end_markers = ['dpFontResizeButton', 'dpContentComments', 'dpAdsWidget', 'dpLyricsFooter']
end_pos = len(chunk)
for em in end_markers:
    ep = chunk.find(em)
    if ep > 0 and ep < end_pos:
        end_pos = ep
        print(f"End marker '{em}' at relative pos: {ep}")

aarti_html = chunk[:end_pos]

# Find all dpLyricsAartiGroup divs
groups = re.findall(r'<div class="dpLyricsAartiGroup">(.*?)</div>', aarti_html, re.DOTALL)
print(f"Found {len(groups)} lyric groups")

# Get h3 title
h3 = re.search(r'<h3[^>]*>(.*?)</h3>', aarti_html, re.DOTALL)
title = ''
if h3:
    title = re.sub(r'<[^>]+>', '', h3.group(1)).strip()
    print(f"Title: {title}")

# Extract all text
full_lyrics = []
full_lyrics.append('॥ श्री अन्नपूर्णा माता जी की आरती ॥')
full_lyrics.append('')

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

# Print the result
print("\n=== ANNAPURNA AARTI LYRICS ===")
for line in full_lyrics:
    print(line)

# Save
lyrics_text = '\n'.join(full_lyrics).strip()
with open('annapurna_aarti_lyrics.txt', 'w', encoding='utf-8') as f:
    f.write(lyrics_text)
print(f"\nSaved ({len(lyrics_text)} chars, {len(full_lyrics)} lines)")
