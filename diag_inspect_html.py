import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', text)
print('Script sources:')
for s in scripts:
    print(' ', s)

print('\nPages in index.html:')
pages = re.findall(r'id=["\'](page-[^"\']+)["\']', text)
for p in set(pages):
    print(' ', p)

print('\nSearch terms in index.html:')
for term in ['gita', 'गीता', 'सुंदरकांड', 'सुन्दरकाण्ड', 'मंत्र', 'चालीसा', 'आरती', 'संग्रहालय']:
    matches = len(re.findall(re.escape(term), text, re.IGNORECASE))
    print(f' {term}: {matches} occurrences')
