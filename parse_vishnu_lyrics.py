import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('chalisa_cache/11_shri-vishnu-chalisa.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all headers and groups within dpPageContentWrapper or lyrics section
# Pattern for dpLyricsType or dpGroup
lyrics_section_start = text.find('class="dpLyricsTitle"')
if lyrics_section_start == -1:
    lyrics_section_start = text.find('॥ विष्णु चालीसा ॥')
lyrics_section_end = text.find('dpLyricsVideoWrapper', lyrics_section_start)
if lyrics_section_end == -1:
    lyrics_section_end = text.find('dpFooter', lyrics_section_start)

section = text[lyrics_section_start:lyrics_section_end]

# Extract all elements: headings and groups
items = re.findall(r'(<(?:h[23]|div|p)[^>]*>.*?</(?:h[23]|div|p)>)', section, re.DOTALL)
print(f"Total section length: {len(section)}")

# Let's extract clean lines
# In Drik Panchang, each verse group has <p class="dpGroup"><span class="dpRow">...</span>...</p>
groups = re.findall(r'<div class=\"dpLyricsChalisaGroup\">(.*?)</div>', section, re.DOTALL)
print(f"Total chalisa groups: {len(groups)}")

# Also look for headings like ॥ दोहा ॥, ॥ चौपाई ॥
elements = re.findall(r'(<h[23][^>]*>.*?<\/h[23]>|<div class=\"dpLyricsChalisaGroup\">.*?<\/div>)', section, re.DOTALL)
print(f"Total elements: {len(elements)}")

for idx, el in enumerate(elements):
    clean = re.sub(r'<span class=\"dpRow\">(.*?)</span>', r'\1 ', el)
    clean = re.sub(r'</p>', '\n', clean)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'[ \t]+', ' ', clean).strip()
    print(f"[{idx}] {clean}")
