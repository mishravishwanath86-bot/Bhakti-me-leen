import re

with open('raghuvar_hi.html', 'r', encoding='utf-8') as f:
    html_hi = f.read()

with open('raghuvar_en.html', 'r', encoding='utf-8') as f:
    html_en = f.read()

# Let's search inside body
body_hi = html_hi[html_hi.find('<body'):]
body_en = html_en[html_en.find('<body'):]

# Find matches of "आरती कीजै" in body
occurrences_hi = [m.start() for m in re.finditer(r'आरती\s*कीजै', body_hi)]

extracted_hi = []
for idx, pos in enumerate(occurrences_hi):
    snippet = body_hi[pos:pos+2000]
    extracted_hi.append(f"--- Occurrence {idx+1} ---\n{snippet}")

# In English
occurrences_en = [m.start() for m in re.finditer(r'Aarti\s*Kijai', body_en, re.I)]

extracted_en = []
for idx, pos in enumerate(occurrences_en):
    snippet = body_en[pos:pos+2000]
    extracted_en.append(f"--- Occurrence {idx+1} ---\n{snippet}")

with open('raghuvar_body_extract.txt', 'w', encoding='utf-8') as f:
    f.write("=== HINDI ===\n" + "\n\n".join(extracted_hi) + "\n\n=== ENGLISH ===\n" + "\n\n".join(extracted_en))

print("DONE: Saved extracts to raghuvar_body_extract.txt")
