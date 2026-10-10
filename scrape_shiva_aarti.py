import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_url(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode('utf-8')

url_hi = "https://www.drikpanchang.com/lyrics/aarti/lord-shiva/shiva-aarti.html?lang=hi&ck=1"
url_en = "https://www.drikpanchang.com/lyrics/aarti/lord-shiva/shiva-aarti.html?lang=en&ck=1"

html_hi = fetch_url(url_hi)
with open('shiva_hi.html', 'w', encoding='utf-8') as f:
    f.write(html_hi)

html_en = fetch_url(url_en)
with open('shiva_en.html', 'w', encoding='utf-8') as f:
    f.write(html_en)

print("Saved HTML files.")

# Extract title
m_title_hi = re.search(r'<title>(.*?)</title>', html_hi, re.I)
title_hi = m_title_hi.group(1) if m_title_hi else ""

m_title_en = re.search(r'<title>(.*?)</title>', html_en, re.I)
title_en = m_title_en.group(1) if m_title_en else ""

# Extract YouTube Video ID
m_video = re.search(r'id="dpYoutubeVideoId"\s+src="[^"]*(?:embed\/|v=)([a-zA-Z0-9_-]{11})', html_hi)
if not m_video:
    m_all_yt = re.findall(r'(?:youtube\.com\/(?:embed\/|watch\?v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', html_hi)
    video_id = m_all_yt[-1] if m_all_yt else ""
else:
    video_id = m_video.group(1)

def extract_aarti_text(html):
    start = html.find('dpLyricsContent')
    if start != -1:
        end = html.find('</article>', start)
        content_html = html[start:end]
    else:
        content_html = html

    p_tags = re.findall(r'<p>(.*?)</p>', content_html, re.DOTALL)
    cleaned_paragraphs = []
    for p in p_tags:
        lines = re.findall(r'<span class="dpRow[^"]*">(.*?)</span>', p, re.DOTALL)
        if not lines:
            clean_text = re.sub(r'<[^>]+>', '', p).strip()
            if clean_text:
                cleaned_paragraphs.append(clean_text)
        else:
            clean_lines = [re.sub(r'<[^>]+>', '', line).strip() for line in lines if line.strip()]
            if clean_lines:
                cleaned_paragraphs.append("\n".join(clean_lines))
    return cleaned_paragraphs

hi_paras = extract_aarti_text(html_hi)
en_paras = extract_aarti_text(html_en)

data = {
    "title_hi": title_hi,
    "title_en": title_en,
    "video_id": video_id,
    "hi_paras": hi_paras,
    "en_paras": en_paras
}

with open('shiva_clean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Extracted clean data successfully.")
