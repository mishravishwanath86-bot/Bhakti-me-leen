import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('banke_bihari_hi.html', 'r', encoding='utf-8') as f:
    hi_html = f.read()

with open('banke_bihari_en.html', 'r', encoding='utf-8') as f:
    en_html = f.read()

# Title
title_hi = re.search(r'<title>(.*?)</title>', hi_html)
print('HI Title:', title_hi.group(1) if title_hi else '')

title_en = re.search(r'<title>(.*?)</title>', en_html)
print('EN Title:', title_en.group(1) if title_en else '')

# Video
video_m = re.search(r'(?:youtube\.com/embed/|youtu\.be/|watch\?v=)([a-zA-Z0-9_-]{11})', hi_html)
print('Video ID:', video_m.group(1) if video_m else 'None')

def clean_html_text(raw_html):
    t = re.sub(r'<br\s*/?>', '\n', raw_html)
    t = re.sub(r'</(?:p|div)>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    lines = [l.strip() for l in t.split('\n')]
    res = []
    prev_blank = False
    for l in lines:
        if not l:
            if not prev_blank:
                res.append('')
            prev_blank = True
        else:
            res.append(l)
            prev_blank = False
    return '\n'.join(res).strip()

# Extract from dpLyricsDevanagariFontWrapper or dpLyricsAartiGroup
hi_wrapper = re.findall(r'<div class="dpLyricsDevanagariFontWrapper">(.*?)</div>\s*</div>', hi_html, re.DOTALL)
if hi_wrapper:
    print('--- HI LYRICS FULL ---')
    print(clean_html_text(hi_wrapper[0]))
else:
    # fallback
    groups = re.findall(r'<div class="dpLyricsAartiGroup">(.*?)</div>', hi_html, re.DOTALL)
    print(f'HI Groups found: {len(groups)}')
    for i, g in enumerate(groups):
        print(f'Group {i+1}:\n{clean_html_text(g)}\n')

# English wrapper
en_wrapper = re.findall(r'<div class="dpLyricsDevanagariFontWrapper">(.*?)</div>\s*</div>', en_html, re.DOTALL)
if not en_wrapper:
    en_wrapper = re.findall(r'<div class="dpLyricsWrapper">(.*?)</div>\s*</div>', en_html, re.DOTALL)
if en_wrapper:
    print('--- EN LYRICS FULL ---')
    print(clean_html_text(en_wrapper[0]))
