import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="curved-fluid-bottom-nav"')
print(html[idx:idx+1500])
