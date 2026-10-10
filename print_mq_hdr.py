import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = 526463
print(text[idx-1200:idx-400])
