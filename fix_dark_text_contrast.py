import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Nitya Aarti Collection Header
old_aarti_header = """      <!-- 🪔 NITYA AARTI COLLECTION CARDS (GANESH & HANUMAN) 🪔 -->
      <div style="margin: 0 1.2rem 1.4rem;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.8rem;">
          <h2 style="font-size:1.1rem; font-weight:900; color:#2A0D4E; margin:0; display:flex; align-items:center; gap:6px;">
            <span style="font-size:1.25rem;">🪔</span> नित्य पावन आरती संग्रह
          </h2>
          <span style="font-size:0.8rem; color:#C2410C; font-weight:800; cursor:pointer; background:rgba(217,119,6,0.12); padding:3px 10px; border-radius:12px; border:1px solid rgba(217,119,6,0.3);" onclick="showPage('page-aarti')">सभी देखें ❯</span>
        </div>"""

new_aarti_header = """      <!-- 🪔 NITYA AARTI COLLECTION CARDS (GANESH & HANUMAN) 🪔 -->
      <div style="margin: 0 1.2rem 1.4rem;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.8rem;">
          <h2 style="font-size:1.1rem; font-weight:900; color:#FFFDF8; margin:0; display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.35rem; filter:drop-shadow(0 0 8px #F59E0B);">🪔</span>
            <span>नित्य पावन आरती संग्रह</span>
          </h2>
          <span style="font-size:0.8rem; color:#FDE68A; font-weight:800; cursor:pointer; background:rgba(248,200,59,0.18); padding:4px 12px; border-radius:14px; border:1.2px solid rgba(248,200,59,0.45); box-shadow:0 0 10px rgba(248,200,59,0.2);" onclick="showPage('page-aarti')">सभी देखें ❯</span>
        </div>"""

if old_aarti_header in html:
    html = html.replace(old_aarti_header, new_aarti_header, 1)
    print("✓ Successfully replaced Aarti collection header with bright white & gold text!")
else:
    # Regex replacement for safety
    html = re.sub(
        r'<h2 style="[^"]*color:#2A0D4E;[^"]*">\s*<span[^>]*>🪔<\/span>\s*नित्य पावन आरती संग्रह\s*<\/h2>',
        """<h2 style="font-size:1.1rem; font-weight:900; color:#FFFDF8; margin:0; display:flex; align-items:center; gap:8px;">
            <span style="font-size:1.35rem; filter:drop-shadow(0 0 8px #F59E0B);">🪔</span>
            <span>नित्य पावन आरती संग्रह</span>
          </h2>""",
        html
    )
    print("✓ Replaced via Regex")

# Scan for any other headings with dark color #2A0D4E or similar
html = html.replace('color:#2A0D4E', 'color:#FFFDF8')
html = html.replace('color: #2A0D4E', 'color: #FFFDF8')

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Saved index.html with crystal-clear high contrast headers (v={ts})")
