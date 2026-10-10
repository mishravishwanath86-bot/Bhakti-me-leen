import re
import os
import sys
import urllib.request
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

en_file = r'C:\Users\vishw\.gemini\antigravity-ide\brain\85d64534-ea39-4946-988b-be7eeefc13c3\.system_generated\steps\8057\content.md'
hi_file = r'C:\Users\vishw\.gemini\antigravity-ide\brain\85d64534-ea39-4946-988b-be7eeefc13c3\.system_generated\steps\8061\content.md'

with open(en_file, 'r', encoding='utf-8') as f:
    en_text = f.read()

with open(hi_file, 'r', encoding='utf-8') as f:
    hi_text = f.read()

m_en = re.search(r'<p class="dpContent ">(.*?)</p>', en_text, re.DOTALL)
m_hi = re.search(r'<p class="dpContent ">(.*?)</p>', hi_text, re.DOTALL)

clean_en = re.sub(r'<[^>]+>', '', m_en.group(1)) if m_en else ''
clean_hi = re.sub(r'<[^>]+>', '', m_hi.group(1)) if m_hi else ''

print("EN Intro:", clean_en)
print("\nHI Intro:", clean_hi)

card_pat = re.compile(r'<div class="dpEventAnchorBlock[^"]*"><a href="([^"]+)".*?<img src="([^"]+)".*?<div class="dpAnchorBlockTitle">(.*?)</div>', re.DOTALL)

en_cards = card_pat.findall(en_text)
hi_cards = card_pat.findall(hi_text)

print(f"\nEN Cards count: {len(en_cards)}")
for href, img, title in en_cards:
    t = re.sub(r'<[^>]+>', ' ', title).strip()
    print(f"EN: {t} -> {href} | {img}")

print(f"\nHI Cards count: {len(hi_cards)}")
for href, img, title in hi_cards:
    t = re.sub(r'<[^>]+>', ' ', title).strip()
    print(f"HI: {t} -> {href} | {img}")
