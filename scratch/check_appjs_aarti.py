import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('window.AARTI_COLLECTIONS =')
if idx != -1:
    print('Found window.AARTI_COLLECTIONS = at index:', idx)
    print(text[idx:idx+400])
else:
    print('NOT FOUND window.AARTI_COLLECTIONS =')
    # search for AARTI_COLLECTIONS
    idx2 = text.find('AARTI_COLLECTIONS')
    print('Found AARTI_COLLECTIONS at:', idx2, text[idx2:idx2+200])
