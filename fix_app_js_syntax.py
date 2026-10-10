import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
app_js = BASE_DIR / "app.js"

with open(app_js, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# Replace duplicate const declarations with safe window-scoped wrapper pattern or unique names
# 1. First originalShowPage around 316598
js = js.replace('const originalShowPage = window.showPage;', 'var _prevShowPage1 = window.showPage;')
js = js.replace('if (typeof originalShowPage === \'function\') {\n    originalShowPage(pageId);', 'if (typeof _prevShowPage1 === \'function\') {\n    _prevShowPage1(pageId);')
js = js.replace('if (typeof originalShowPage === \'function\') {\r\n    originalShowPage(pageId);', 'if (typeof _prevShowPage1 === \'function\') {\r\n    _prevShowPage1(pageId);')

# 2. Second originalShowPage around 385704
js = js.replace('const originalShowPage = window.showPage;', 'var _prevShowPage2 = window.showPage;')
js = js.replace('if (originalShowPage) originalShowPage(pageId);', 'if (typeof _prevShowPage2 === \'function\') _prevShowPage2(pageId);')

# 3. originalNavigateTo
js = js.replace('const originalNavigateTo = window.navigateTo;', 'var _prevNavTo1 = window.navigateTo;')
js = js.replace('if (typeof originalNavigateTo === \'function\') {\n    originalNavigateTo(pageId);', 'if (typeof _prevNavTo1 === \'function\') {\n    _prevNavTo1(pageId);')
js = js.replace('if (typeof originalNavigateTo === \'function\') {\r\n    originalNavigateTo(pageId);', 'if (typeof _prevNavTo1 === \'function\') {\r\n    _prevNavTo1(pageId);')

# 4. originalBuildDeityGrid
js = js.replace('const originalBuildDeityGrid = window.buildDeityGrid;', 'var _prevBuildDeityGrid = window.buildDeityGrid;')

with open(app_js, 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Fixed all duplicate const declarations in app.js")
