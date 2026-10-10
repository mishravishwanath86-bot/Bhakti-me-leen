import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\app.js', 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

idx = js.find('window.applyGlobalTheme = function()')
print(js[idx+900:idx+2000])
