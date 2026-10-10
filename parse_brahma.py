import sys
import re
import html

sys.stdout.reconfigure(encoding='utf-8')

with open('brahma_raw.html', 'r', encoding='utf-8') as f:
    raw = f.read()

# Find the lyrics container
start_idx = raw.find('॥ आरती श्री ब्रह्मा जी ॥')
if start_idx == -1:
    start_idx = raw.find('पितु मातु सहायक')

end_idx = raw.find('dpCardInfoWrapper', start_idx)
if end_idx == -1:
    end_idx = raw.find('dpNavigationWrapper', start_idx)

snippet = raw[start_idx:end_idx] if start_idx != -1 and end_idx != -1 else raw[start_idx:start_idx+10000]

# Split by dpLyricsAartiGroup or paragraphs
groups = re.findall(r'<div class="dpLyricsAartiGroup">(.*?)</div>', snippet, re.DOTALL)
print(f"Total groups found: {len(groups)}")

parsed_groups = []
for i, g in enumerate(groups):
    rows = re.findall(r'<span class="dpRow">(.*?)</span>', g)
    clean_rows = [html.unescape(r).strip() for r in rows if r.strip()]
    if clean_rows:
        parsed_groups.append(clean_rows)

print("\n--- EXTRACTED AARTI ---")
full_text_stanzas = []
for g in parsed_groups:
    stanza = "\n".join(g)
    full_text_stanzas.append(stanza)
    print(stanza)
    print()

full_formatted = "॥ आरती श्री ब्रह्मा जी ॥\n(पितु मातु सहायक स्वामी सखा)\n\n" + "\n\n".join(full_text_stanzas)
with open('brahma_aarti_formatted.txt', 'w', encoding='utf-8') as out:
    out.write(full_formatted)

print("\n--- FORMATTED SAVED ---")
print(full_formatted)
