import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("REMOVING 432Hz OM SOUND THERAPY FLOATING BAR")
print("=" * 80)

# 1. Remove from index.html
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos_bar = html.find('id="sound-therapy-bar"')
if pos_bar != -1:
    pos_start = html.rfind('<!-- 🎵 PERSISTENT SOUND THERAPY', 0, pos_bar)
    if pos_start == -1:
        pos_start = pos_bar - 10
    pos_end = html.find('</div>', pos_bar) + 6
    html = html[:pos_start] + html[pos_end:]
    print("✓ Removed #sound-therapy-bar from index.html")

# Bump cache buster
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ Updated index.html")

# 2. Clean up in app.js
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

pos_js = js.find('// 7. Sound Therapy 432Hz Om Drone')
if pos_js != -1:
    end_js = js.find('};', pos_js)
    if end_js != -1:
        end_js = js.find('};', end_js + 2) + 2
        js = js[:pos_js] + "// Sound Therapy removed\n" + js[end_js:]
        print("✓ Removed toggleOmSoundTherapy from app.js")

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("=" * 80)
print("432Hz SOUND THERAPY REMOVED COMPLETELY")
print("=" * 80)
