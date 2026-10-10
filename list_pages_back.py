import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pages = re.findall(r'<section\s+id="(page-[^"]+)"[^>]*>', html)
print(f"Total pages: {len(pages)}")

for p in pages:
    m = re.search(r'<section\s+id="' + p + r'"[^>]*>(.*?)(?:</section>|<section\s+id="page-)', html, re.DOTALL)
    if m:
        content = m.group(1)[:1200]
        back_btns = re.findall(r'<button[^>]*class="[^"]*back-btn[^"]*"[^>]*>', content)
        if back_btns:
            print(f"{p}: {back_btns[0][:100]}")
        else:
            # check for any back button
            any_back = re.findall(r'<button[^>]*onclick="[^"]*showPage[^"]*"[^>]*>.*?←.*?</button>', content, re.DOTALL)
            if any_back:
                print(f"{p} (custom back): {any_back[0][:100]}")
            else:
                print(f"{p}: NO back button found in first 1200 chars")
