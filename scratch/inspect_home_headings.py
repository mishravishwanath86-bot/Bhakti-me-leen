import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx1 = html.find('id="page-home"')
idx2 = html.find('</section>', idx1)
home = html[idx1:idx2]

# Find all section headers in page-home
headers = re.findall(r'<h[2345][^>]*>([\s\S]*?)</h[2345]>', home)
print(f'Found {len(headers)} headings in page-home:')
for h in headers:
    clean_h = re.sub(r'<[^>]+>', '', h).strip()
    if clean_h:
        print('  •', clean_h)
