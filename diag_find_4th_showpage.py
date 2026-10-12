import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

m = text.find("  // 1. Switch active page\n  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));")
if m != -1:
    print(text[m-200:m+1200])
else:
    print('Not found')
