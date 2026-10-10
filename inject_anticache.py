import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"

with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Add anti-cache script in head
anticache_script = """  <script>
    // Automatic Cache Clear & ServiceWorker unregister
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.getRegistrations().then(function(registrations) {
        for(let registration of registrations) {
          registration.unregister();
        }
      });
    }
    if ('caches' in window) {
      caches.keys().then(function(names) {
        for (let name of names) caches.delete(name);
      });
    }
  </script>"""

if 'Automatic Cache Clear' not in html:
    html = html.replace('<head>', '<head>\n' + anticache_script)

# Bump cache buster
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Injected Cache Clear script and bumped ?v={ts} in index.html")
