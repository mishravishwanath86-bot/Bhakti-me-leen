import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    app = f.read()

with open('sundarkand_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    sundarkand = f.read()

with open('mantra_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    mantra = f.read()

print('=== renderDrikImage1CardHtml ===')
idx = app.find('renderDrikImage1CardHtml = function')
if idx != -1:
    print(app[idx:idx+1500])

print('\n=== renderDrikChalisaCardHtml ===')
idx = app.find('renderDrikChalisaCardHtml = function')
if idx != -1:
    print(app[idx:idx+1500])

print('\n=== Sundarkand Cards in renderFullSundarkandPage ===')
idx = sundarkand.find('filteredDohas.map(')
if idx == -1:
    idx = sundarkand.find('filteredDohas')
print(sundarkand[idx:idx+1500])

print('\n=== Mantra Play in renderFullDrikMantraPage ===')
idx = mantra.find('items.map((item, idx) => {')
print(mantra[idx+500:idx+2000])

