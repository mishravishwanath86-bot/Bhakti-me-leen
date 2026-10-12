import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('sundarkand_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    sundarkand = f.read()

with open('mantra_engine.js', 'r', encoding='utf-8', errors='ignore') as f:
    mantra = f.read()

with open('app.js', 'r', encoding='utf-8', errors='ignore') as f:
    app = f.read()

print('=== SUNDARKAND CARD ONCLICK ===')
idx = sundarkand.find('window.renderFullSundarkandPage = function')
print(sundarkand[idx+500:idx+2500])

print('\n=== MANTRA CARD ONCLICK ===')
idx = mantra.find('window.renderFullDrikMantraPage = function')
print(mantra[idx+500:idx+2500])

print('\n=== CHALISA CARD ONCLICK ===')
idx = app.find('window.renderFullDrikChalisaPage = function')
print(app[idx+500:idx+2500])

print('\n=== AARTI CARD ONCLICK ===')
idx = app.find('window.renderFullDrikAartiPage = function')
print(app[idx+500:idx+2500])

