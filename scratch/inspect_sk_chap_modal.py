import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('sundarkand_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('listContainer.innerHTML =')
print(text[idx:idx+1500])
