import codecs
import re
import sys

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Find window.AARTI_COLLECTIONS at line 26244
idx26244 = text.find('window.AARTI_COLLECTIONS =', 26000 * 50)
if idx26244 == -1:
    idx26244 = text.rfind('window.AARTI_COLLECTIONS =')

print("Found AARTI_COLLECTIONS at pos:", idx26244)
block = text[idx26244:idx26244+300000]

# Check krishna items
k_idx = block.find('"krishna"')
if k_idx != -1:
    k_block = block[k_idx:k_idx+50000]
    print("Found krishna block:", k_block[:500])
    # check item 2
    drik_k3 = k_block.find('drik_krishna_3')
    if drik_k3 != -1:
        print("drik_krishna_3 block:", k_block[drik_k3:drik_k3+1000])
    else:
        print("drik_krishna_3 NOT found in krishna block!")
else:
    print("krishna NOT found in block!")
