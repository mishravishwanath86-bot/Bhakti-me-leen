import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_cache/2_shri-bajarang-baan_en.html', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's see the title and h1
m = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
if m:
    print('EN Title:', m.group(1).strip())

# Extract dpLyricsBlock
lyrics_block_match = re.search(r'<div class="dpLyricsBlock"[^>]*>(.*?)</div>\s*</div>\s*(?:<div class="dpAdCard"|<div class="dpSocialShare"|<div class="dpNextPrev")', html, re.S)
if lyrics_block_match:
    l_html = lyrics_block_match.group(1)
    cleaned = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'\n\n\1\n', l_html)
    cleaned = re.sub(r'</p>', '\n', cleaned)
    cleaned = re.sub(r'</div>', '\n', cleaned)
    cleaned = re.sub(r'<br\s*/?>', '\n', cleaned)
    cleaned = re.sub(r'<[^>]+>', '', cleaned)
    lines = [l.strip() for l in cleaned.splitlines() if l.strip()]
    print('--- EN EXTRACTED LYRICS (FIRST 20 LINES) ---')
    print('\n'.join(lines[:25]))
    print('--- TOTAL EN LINES ---', len(lines))
