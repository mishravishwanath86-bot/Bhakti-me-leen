import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

pos = js.find('function initVratGrids')
print(js[pos:pos+2500])
