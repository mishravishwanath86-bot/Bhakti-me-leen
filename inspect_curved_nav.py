import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="curved-bottom-nav"')
if idx != -1:
    print("Found curved-bottom-nav at index:", idx)
    print(html[idx-100:idx+800])
else:
    print("curved-bottom-nav not found")
