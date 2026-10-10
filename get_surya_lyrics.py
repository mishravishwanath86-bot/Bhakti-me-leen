import re

with open("chalisa_cache/10_surya-deva-chalisa.html", "r", encoding="utf-8") as f:
    html = f.read()

pos = html.find("जय सविता जय जयति दिवाकर", 1000)
print("Position after 1000:", pos)

if pos != -1:
    snippet = html[max(0, pos-2000):pos+12000]
    s = re.sub(r'<br\s*/?>', '\n', snippet)
    s = re.sub(r'</(p|div|h\d)>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    lines = [l.strip() for l in s.split('\n') if l.strip()]
    with open("c10_extracted_lyrics.txt", "w", encoding="utf-8") as out:
        for l in lines:
            out.write(l + "\n")
    print(f"Extracted {len(lines)} lines from HTML")
