import sys, os, json

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect the data sources in apps/web/src/data and VRAT_PAGES_DATA in app.js
app_js_path = r"c:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\app.js"
with open(app_js_path, "r", encoding="utf-8") as f:
    content = f.read()

print("App.js length:", len(content))
print("Has renderDrikVinayaka:", "function renderDrikVinayaka" in content)
