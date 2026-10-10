import re
import json

def extract_aarti_text(html):
    # Find all dpRow spans inside dpLyricsAartiGroup or the main lyrics container
    # Or find the article/div containing lyrics
    lyrics_blocks = []
    
    # Let's find groups <div class="dpLyricsAartiGroup">
    groups = re.findall(r'<div class="dpLyricsAartiGroup">(.*?)</div>', html, re.DOTALL)
    
    # Note: the first stanza might be right before the first dpLyricsAartiGroup
    # Let's inspect the entire container between <div class="dpLyricsContent"> and </article>
    start = html.find('dpLyricsContent')
    if start != -1:
        end = html.find('</article>', start)
        content_html = html[start:end]
    else:
        content_html = html

    # Extract all paragraphs <p>...</p>
    p_tags = re.findall(r'<p>(.*?)</p>', content_html, re.DOTALL)
    cleaned_paragraphs = []
    for p in p_tags:
        # extract lines
        lines = re.findall(r'<span class="dpRow[^"]*">(.*?)</span>', p, re.DOTALL)
        if not lines:
            # maybe without span
            clean_text = re.sub(r'<[^>]+>', '', p).strip()
            if clean_text:
                cleaned_paragraphs.append(clean_text)
        else:
            clean_lines = [re.sub(r'<[^>]+>', '', line).strip() for line in lines if line.strip()]
            if clean_lines:
                cleaned_paragraphs.append("\n".join(clean_lines))
    return cleaned_paragraphs

with open('raghuvar_hi.html', 'r', encoding='utf-8') as f:
    hi_html = f.read()

with open('raghuvar_en.html', 'r', encoding='utf-8') as f:
    en_html = f.read()

hi_paras = extract_aarti_text(hi_html)
en_paras = extract_aarti_text(en_html)

result = {
    "hi_paras": hi_paras,
    "en_paras": en_paras
}

with open('raghuvar_clean_lyrics.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("Saved clean lyrics to raghuvar_clean_lyrics.json")
