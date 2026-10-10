import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the stray block between </section> (end of page-katha) and <!-- ══════════ DOWNLOADS ══════════ -->
s_pos = html.find('<!-- MINI PLAYER (shown when katha playing) -->')
e_pos = html.find('<!-- ══════════ DOWNLOADS ══════════ -->')

if s_pos != -1 and e_pos != -1:
    html = html[:s_pos] + "\n    " + html[e_pos:]
    print("✓ Successfully removed stray 'कथा पाठ / Lyrics' and broken player HTML from index.html")
else:
    print("Could not find exact marker, checking regex")
    html = re.sub(r'<!-- MINI PLAYER \(shown when katha playing\) -->[\s\S]*?<!-- ══════════ DOWNLOADS ══════════ -->', '<!-- ══════════ DOWNLOADS ══════════ -->', html)
    print("✓ Removed via Regex")

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ index.html cleaned and synchronized (v={ts})")
