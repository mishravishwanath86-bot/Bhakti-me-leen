import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for el_id in [
    'gita-chapter-reader-modal', 'gita-chapter-options-modal',
    'sundarkand-reader-modal', 'sundarkand-options-modal',
    'mantra-options-modal',
    'aarti-options-modal',
    'chalisa-options-modal',
    'page-reader', 'reader-cosmic-content', 'reader-content'
]:
    found = el_id in text
    print(f'{el_id}: {"FOUND" if found else "NOT FOUND"}')
