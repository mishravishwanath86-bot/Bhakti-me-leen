import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('sundarkand_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    sundarkand = f.read()

with open('mantra_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    mantra = f.read()

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    app = f.read()

print('=== SUNDARKAND CARD HTML ===')
idx = sundarkand.find('filteredDohas.map(')
if idx != -1:
    print(sundarkand[idx:idx+1500])

print('\n=== MANTRA CARD HTML ===')
idx = mantra.find('items.map((item, idx) =>')
if idx != -1:
    print(mantra[idx:idx+1500])

print('\n=== CHALISA CARD HTML ===')
idx = app.find('window.renderFullDrikChalisaPage = function')
idx2 = app.find('items.map(', idx)
if idx2 != -1:
    print(app[idx2:idx2+1500])

print('\n=== AARTI CARD HTML ===')
idx = app.find('window.renderFullDrikAartiPage = function')
idx2 = app.find('items.map(', idx)
if idx2 != -1:
    print(app[idx2:idx2+1500])

