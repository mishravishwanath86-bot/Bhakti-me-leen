import re
import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('ekadashi_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the start of the aarti
start_marker = '॥ \u090f\u0915\u093e\u0926\u0936\u0940 \u092e\u093e\u0924\u093e \u0915\u0940 \u0906\u0930\u0924\u0940 ॥'  # ॥ एकादशी माता की आरती ॥
idx = html.find(start_marker)
print(f"Start at: {idx}")

# Extract a large chunk
chunk = html[idx:idx+15000]

# Find all dpLyricsAartiGroup divs
groups = re.findall(r'<div class="dpLyricsAartiGroup">(.*?)</div>', chunk, re.DOTALL)
print(f"Found {len(groups)} lyric groups")

# Also get the h3 title
h3 = re.search(r'<h3[^>]*>(.*?)</h3>', chunk, re.DOTALL)
if h3:
    title = re.sub(r'<[^>]+>', '', h3.group(1)).strip()
    print(f"Title: {title}")

# Now extract all text from the groups
full_lyrics = []

# Add title
full_lyrics.append('॥ एकादशी माता की आरती ॥')
full_lyrics.append('')

for group in groups:
    # Extract all span text
    spans = re.findall(r'<span[^>]*>(.*?)</span>', group, re.DOTALL)
    if spans:
        group_lines = []
        for span in spans:
            text = re.sub(r'<[^>]+>', '', span).strip()
            if text:
                group_lines.append(text)
        if group_lines:
            full_lyrics.extend(group_lines)
            full_lyrics.append('')  # blank line between groups

# Print the extracted lyrics
print("\n=== EXTRACTED AARTI LYRICS ===")
for line in full_lyrics:
    print(line)

# Save as clean text
lyrics_text = '\n'.join(full_lyrics).strip()
with open('ekadashi_aarti_lyrics.txt', 'w', encoding='utf-8') as f:
    f.write(lyrics_text)
print(f"\nSaved to ekadashi_aarti_lyrics.txt ({len(lyrics_text)} chars)")
