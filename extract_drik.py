import re
import sys

with open('drik_ganesh_aarti.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find iframe or video
yt_matches = re.findall(r'youtube\.com/(?:embed/|watch\?v=)([a-zA-Z0-9_-]+)', html)
print('YouTube IDs:', yt_matches)

# Find title and breadcrumbs
pos = html.find('॥ श्री गणेशजी की आरती ॥')
if pos != -1:
    snippet = html[max(0, pos-200):pos+3500]
    # convert breaks to newlines
    snippet = re.sub(r'<br\s*/?>', '\n', snippet)
    snippet = re.sub(r'</?(?:p|div|span|h[1-6]|li|ul)[^>]*>', '\n', snippet)
    text = re.sub(r'<[^>]+>', '', snippet)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    with open('extracted_lyrics.txt', 'w', encoding='utf-8') as out:
        out.write('\n'.join(lines))
    print('Wrote extracted_lyrics.txt with', len(lines), 'lines')
