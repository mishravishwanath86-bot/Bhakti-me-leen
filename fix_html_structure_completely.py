import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"

with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Fix the broken cut-off in page-ramnavami
broken_chunk = """            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍹 Panakam</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🥛 Neer Mor</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🥄 Panchamrit</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍮 Halwa</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍚 Kheer</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">

  
    <!-- ═════════════════════════════════════════════════════════════════
         🖼️ DIVINE GALLERY PAGE (BAL ROOP & DIVYA ROOP - 60+ GODS)
         ═════════════════════════════════

  </main>"""

clean_chunk = """            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍹 Panakam</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🥛 Neer Mor</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🥄 Panchamrit</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍮 Halwa</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍚 Kheer</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🥥 Kosambari</div>
          </div>
        </div>
      </div>
    </section>

  </main>"""

if broken_chunk in html:
    html = html.replace(broken_chunk, clean_chunk)
    print("✓ Successfully patched broken page-ramnavami cut-off in index.html")
else:
    print("Broken chunk pattern did not match directly, applying regex patch...")
    # Find pos of "🍹 Panakam"
    p1 = html.find('🍹 Panakam')
    if p1 != -1:
        p2 = html.find('</main>', p1)
        if p2 != -1:
            html = html[:p1-75] + clean_chunk + html[p2+7:]
            print("✓ Successfully replaced cut-off with clean_chunk via index slice")

# Remove duplicate mini-play id if present
html = html.replace('id="mini-play"', 'id="mini-play-btn"', 1)

# Bump cache buster
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Saved updated index.html with new cache buster ?v={ts}")
