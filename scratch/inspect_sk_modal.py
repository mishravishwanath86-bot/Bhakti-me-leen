import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="sundarkand-reader-modal"')
if idx != -1:
    print('Found sundarkand-reader-modal at:', idx)
    print(text[idx:idx+2500])
else:
    print('sundarkand-reader-modal NOT FOUND in index.html!')
