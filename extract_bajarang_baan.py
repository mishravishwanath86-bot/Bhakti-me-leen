import sys, re, urllib.request, json

sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_cache/2_shri-bajarang-baan.html', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's extract the entire dpLyricsBlock
lyrics_block_match = re.search(r'<div class="dpLyricsBlock"[^>]*>(.*?)</div>\s*</div>\s*(?:<div class="dpAdCard"|<div class="dpSocialShare"|<div class="dpNextPrev")', html, re.S)
if not lyrics_block_match:
    lyrics_block_match = re.search(r'<div class="dpLyricsBlock"[^>]*>(.*?)<!-- end dpLyricsBlock -->', html, re.S)

lyrics_html = lyrics_block_match.group(1) if lyrics_block_match else html[36800:46000]

print('Lyrics block HTML length:', len(lyrics_html))

# Let's extract clean lines
# Replace headings, paragraphs, spans
cleaned = lyrics_html
# Convert headings
cleaned = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'\n\n\1\n', cleaned)
# Convert </p> and </div> to newline
cleaned = re.sub(r'</p>', '\n', cleaned)
cleaned = re.sub(r'</div>', '\n', cleaned)
cleaned = re.sub(r'<br\s*/?>', '\n', cleaned)
# Remove all other tags
cleaned = re.sub(r'<[^>]+>', '', cleaned)
# Clean up spaces and multiple blank lines
lines = [l.strip() for l in cleaned.splitlines()]
clean_lyrics = []
for l in lines:
    if l:
        clean_lyrics.append(l)

final_text = '\n'.join(clean_lyrics)
print('--- CLEAN EXTRACTED DEVANGARI LYRICS ---')
print(final_text)

# Let's check YouTube videos with noembed
for vid in ['xcVv68gwc5Y', 'aOQhX5yKaLU']:
    try:
        url = f'https://noembed.com/embed?url=https://www.youtube.com/watch?v={vid}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        data = json.loads(res.read().decode('utf-8'))
        print(f"Video {vid}: {data.get('title')} (Author: {data.get('author_name')})")
    except Exception as e:
        print(f"Video {vid} check error:", e)
