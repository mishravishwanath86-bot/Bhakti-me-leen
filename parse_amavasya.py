import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

en_file = r'C:\Users\vishw\.gemini\antigravity-ide\brain\85d64534-ea39-4946-988b-be7eeefc13c3\.system_generated\steps\8203\content.md'
hi_file = r'C:\Users\vishw\.gemini\antigravity-ide\brain\85d64534-ea39-4946-988b-be7eeefc13c3\.system_generated\steps\8205\content.md'

with open(en_file, 'r', encoding='utf-8') as f:
    en_html = f.read()

with open(hi_file, 'r', encoding='utf-8') as f:
    hi_html = f.read()

# Extract intro paragraphs
m_intro_en = re.search(r'<div class="dpPageContentWrapper ">(.*?)</div>', en_html, re.DOTALL)
m_intro_hi = re.search(r'<div class="dpPageContentWrapper ">(.*?)</div>', hi_html, re.DOTALL)

def clean(t):
    if not t: return ""
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

print("EN Intro:", clean(m_intro_en.group(1)) if m_intro_en else "None")
print("\nHI Intro:", clean(m_intro_hi.group(1)) if m_intro_hi else "None")

# Find table or list elements for amavasya dates
# Let's inspect what containers contain the dates
date_blocks = re.findall(r'<div class="[^"]*dpTableCard[^"]*"[^>]*>(.*?)</div>\s*</div>', en_html, re.DOTALL)
if not date_blocks:
    # search for card rows
    rows = re.findall(r'(<div class="[^"]*dp(?:Date|Table|Card|Calendar)[^"]*".*?)(?=<div class="[^"]*dp(?:Date|Table|Card|Calendar)|\Z)', en_html, re.DOTALL)
    print("Found potential rows:", len(rows))

# Let's search for "January 18, 2026"
idx = en_html.find("January 18, 2026")
if idx != -1:
    print("\nSnippet around January 18, 2026:")
    print(en_html[idx-200:idx+800])
else:
    print("Could not find January 18, 2026 directly")
