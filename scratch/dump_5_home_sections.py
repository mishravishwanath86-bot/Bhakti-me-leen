import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx1 = html.find('id="page-home"')
idx2 = html.find('</section>', idx1)
home = html[idx1:idx2]

sections = [
    ('Aarti Section', 'नित्य पावन आरती संग्रह'),
    ('Chalisa Section', 'नित्य पावन चालीसा संग्रह'),
    ('Mantra Section', 'वैदिक मन्त्र संग्रह'),
    ('Sundarkand Section', 'श्री सुन्दरकाण्ड दोहा संग्रह'),
    ('Gita Section', 'श्रीमद्भगवद्गीता (१८ अध्याय)')
]

for title, marker in sections:
    pos = home.find(marker)
    print(f'================ {title} (pos: {pos}) ================')
    if pos != -1:
        # print surrounding 1000 characters
        snippet = home[max(0, pos-100):pos+1200]
        print(snippet)
    print('\n')

