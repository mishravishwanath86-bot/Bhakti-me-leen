import sys, re
sys.stdout.reconfigure(encoding="utf-8")
with open(r"index.html", "r", encoding="utf-8") as f:
    text = f.read()

idx1 = text.find('id="page-home"')
idx2 = text.find('id="page-', idx1 + 20)
home_html = text[idx1:idx2]

print("page-home length:", len(home_html))
for line in home_html.splitlines():
    s = line.strip()
    if s.startswith('<!--') and len(s) > 8:
        print("SECTION:", s[:70])
