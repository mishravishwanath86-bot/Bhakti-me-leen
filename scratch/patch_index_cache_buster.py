import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add cache-control meta tags in head
old_head = '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />'
new_head = """<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />"""

if old_head in html:
    html = html.replace(old_head, new_head, 1)
    print("SUCCESS: Injected cache-control headers in index.html head")
else:
    print("WARNING: old_head not found")

# 2. Update stylesheets
old_css = '<link rel="stylesheet" href="styles.css?v=1791671977" />\n  <link rel="stylesheet" href="ai_bhakti_player.css" />'
new_css = '<link rel="stylesheet" href="styles.css?v=1792000500" />\n  <link rel="stylesheet" href="ai_bhakti_player.css?v=1792000500" />'

if old_css in html:
    html = html.replace(old_css, new_css, 1)
    print("SUCCESS: Updated CSS version stamps in index.html")
else:
    print("WARNING: old_css not found")

# 3. Update scripts
old_scripts = """  <script src="mandir_3d_engine.js?v=1788372515"></script>
  <script src="amrit_kalash_3d_engine.js?v=1788504008"></script>
  <script src="i18n_engine.js?v=1788376135"></script>
  <script src="sadhana_gamification_engine.js?v=1788456689"></script>
  <script src="app.js?v=1791671977"></script>
  <script src="ai_bhakti_player.js"></script>
  <script src="mantra_engine.js?v=1789850000"></script>
  <script src="sundarkand_engine.js?v=1790000000"></script>
  <script src="gita_engine.js?v=1790000000"></script>
<script src="drik_app_addon.js?v=1789850000"></script>
<script src="gallery_engine.js?v=1791570000"></script>"""

new_scripts = """  <script src="mandir_3d_engine.js?v=1788372515"></script>
  <script src="amrit_kalash_3d_engine.js?v=1788504008"></script>
  <script src="i18n_engine.js?v=1788376135"></script>
  <script src="sadhana_gamification_engine.js?v=1788456689"></script>
  <script src="app.js?v=1792000500"></script>
  <script src="ai_bhakti_player.js?v=1792000500"></script>
  <script src="mantra_engine.js?v=1792000500"></script>
  <script src="sundarkand_engine.js?v=1792000500"></script>
  <script src="gita_engine.js?v=1792000500"></script>
<script src="drik_app_addon.js?v=1792000500"></script>
<script src="gallery_engine.js?v=1792000500"></script>"""

if old_scripts in html:
    html = html.replace(old_scripts, new_scripts, 1)
    print("SUCCESS: Updated JavaScript cache-busting query strings in index.html")
else:
    print("WARNING: old_scripts not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished patching index.html")
