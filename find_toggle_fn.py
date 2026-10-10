import sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['index.html', 'app.js']:
    with open(r'C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\\' + fname, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    idx = content.find('toggleGlobalAppTheme')
    if idx != -1:
        print(f"Found in {fname} at {idx}:")
        print(content[idx-100:idx+400])
        print("="*40)
