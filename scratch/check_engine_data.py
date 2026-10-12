import sys
import codecs
import json
import re

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Parse window.AARTI_COLLECTIONS at line 26244
m_aarti = re.search(r'window\.AARTI_COLLECTIONS\s*=\s*(\{[\s\S]*?\n\};)', text[text.find('window.AARTI_COLLECTIONS =', 26000*50):])
if m_aarti:
    print(f"Found AARTI_COLLECTIONS definition (length: {len(m_aarti.group(1))})")

m_chalisa = re.search(r'window\.CHALISA_COLLECTIONS\s*=\s*(\{[\s\S]*?\n\};)', text)
if m_chalisa:
    print(f"Found CHALISA_COLLECTIONS definition (length: {len(m_chalisa.group(1))})")

with open('mantra_engine.js', 'r', encoding='utf-8') as f:
    m_text = f.read()
m_mantra = re.search(r'window\.MANTRA_COLLECTIONS\s*=\s*(\{[\s\S]*?\n\};)', m_text)
if m_mantra:
    print(f"Found MANTRA_COLLECTIONS definition (length: {len(m_mantra.group(1))})")

with open('sundarkand_engine.js', 'r', encoding='utf-8') as f:
    s_text = f.read()
m_sundar = re.search(r'window\.SUNDARKAND_DATA\s*=\s*(\{[\s\S]*?\n\};)', s_text)
if m_sundar:
    print(f"Found SUNDARKAND_DATA definition (length: {len(m_sundar.group(1))})")
