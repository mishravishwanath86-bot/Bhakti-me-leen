import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

funcs = [
    'renderFullSundarkandPage',
    'renderFullDrikMantraPage',
    'renderFullDrikChalisaPage',
    'renderFullDrikAartiPage',
    'openSundarkandChapterModal',
    'openMantraCollectionModal',
    'openChalisaCollectionModal',
    'openAartiCollectionModal',
    'openSundarkandDohaReader',
    'readMantraItemDirect',
    'readChalisaItemDirect',
    'readAartiItemDirect'
]

files = ['app.js', 'sundarkand_engine.js', 'mantra_engine.js', 'chalisa_engine.js', 'drik_app_addon.js']

for fn in funcs:
    print(f'================ {fn} ================')
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
                lines = fp.readlines()
            for i, line in enumerate(lines):
                if f'{fn} = function' in line or f'function {fn}' in line:
                    print(f'  Found in {f}:{i+1}')
                    # print first 15 lines of the function
                    for j in range(i, min(len(lines), i+20)):
                        print(f'    {lines[j].rstrip()[:120]}')
                    break
        except Exception as e:
            pass
    print()
