import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

s_marker = "if(id === 'page-mantra' && typeof window.renderFullDrikMantraPage === 'function') {"
if s_marker in js:
    print("Found mantra handler in showPage")
    replacement = """if(id === 'page-sundarkand' && typeof window.renderFullSundarkandPage === 'function') {
    window.renderFullSundarkandPage('all', '');
  }

  """ + s_marker
    if "if(id === 'page-sundarkand'" not in js:
        js = js.replace(s_marker, replacement, 1)
        with open('app.js', 'w', encoding='utf-8') as f:
            f.write(js)
        print("✓ Successfully injected page-sundarkand into showPage in app.js!")
    else:
        print("page-sundarkand handler already present in app.js")
else:
    print("✗ s_marker not found in app.js")
