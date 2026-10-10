import re
import json

def extract_info(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Title
    title_match = re.search(r'<h1 class="dpPageTitle">(.*?)</h1>', html, re.DOTALL)
    title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip() if title_match else ''
    
    # Video ID
    video_match = re.search(r'id="dpYoutubeVideoId"[^>]*src="[^"]*embed/([a-zA-Z0-9_-]+)', html)
    video_id = video_match.group(1) if video_match else ''
    
    # Lyrics block
    lyrics_match = re.search(r'<div class="dpLyricsDevanagariFontWrapper">(.*?)</div>\s*</div>\s*</article>', html, re.DOTALL)
    paras = []
    if lyrics_match:
        block = lyrics_match.group(1)
        groups = re.findall(r'<div class="dpLyricsAartiGroup">(.*?)</div>', block, re.DOTALL)
        for g in groups:
            p_matches = re.findall(r'<p>(.*?)</p>', g, re.DOTALL)
            g_lines = []
            for p in p_matches:
                spans = re.findall(r'<span class="dpRow[^"]*">(.*?)</span>', p, re.DOTALL)
                if spans:
                    cleaned_spans = [re.sub(r'<[^>]+>', '', s).strip() for s in spans if s.strip()]
                    if cleaned_spans:
                        g_lines.append('\n'.join(cleaned_spans))
                else:
                    clean_p = re.sub(r'<[^>]+>', '', p).strip()
                    if clean_p:
                        g_lines.append(clean_p)
            if g_lines:
                paras.append('\n'.join(g_lines))
    return title, video_id, paras

hi_title, hi_vid, hi_paras = extract_info('kailasavasi_hi.html')
en_title, en_vid, en_paras = extract_info('kailasavasi_en.html')

result = {
    'title_hi': hi_title,
    'title_en': en_title,
    'video_id': hi_vid or en_vid,
    'hi_paras': hi_paras,
    'en_paras': en_paras
}

with open('kailasavasi_clean.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print('Saved kailasavasi_clean.json')
print('Video ID:', result['video_id'])
print('Paras count:', len(result['hi_paras']))
