import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('sundarkand_raw_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

print(f"Loaded {len(pages)} pages.")

# Let's inspect headings in each page
for p_num in range(1, 11):
    html = pages[str(p_num)]
    l_start = html.find('class="dpMiddleTitle"')
    next_div = html.find('class="dpFooter"', l_start)
    if next_div == -1:
        next_div = len(html)
    content = html[l_start:next_div]
    
    headings = re.findall(r'<h3[^>]*class="[^"]*dpLyricsType[^"]*"[^>]*>([\s\S]*?)</h3>', content)
    clean_headings = [re.sub(r'<[^>]+>', '', h).strip() for h in headings]
    print(f"Page {p_num}: {len(clean_headings)} headings -> {', '.join(clean_headings)}")
