import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:/Users/vishw/.gemini/antigravity-ide/scratch/bhakti-app/app.js', 'r', encoding='utf-8') as f:
    app_text = f.read()

# find CONTENT = {
c_pos = app_text.find("const CONTENT = {")
if c_pos == -1:
    c_pos = app_text.find("CONTENT = {")
print("CONTENT pos:", c_pos)

# find chalisa_ keys in CONTENT
matches = re.findall(r'(\bchalisa_[a-zA-Z0-9_]+)\s*:\s*\{', app_text)
print("Chalisa keys in app.js:", matches)
