import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("☀️ FIXING LIGHT THEME CONTRAST & TYPOGRAPHY VISIBILITY")
print("======================================================================")

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

light_contrast_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   ☀️ HIGH-CONTRAST VEDIC LIGHT THEME TYPOGRAPHY & CARD ENGINE ☀️
   ══════════════════════════════════════════════════════════════════════════════ */

body.theme-light,
body.light-mode,
html[data-theme="light"] {
  --app-bg: #FFFBF0 !important;
  --app-card-bg: #FFFFFF !important;
  --app-card-border: rgba(217, 119, 6, 0.28) !important;
  --app-text-primary: #2D1400 !important;
  --app-text-secondary: #653A10 !important;
  --app-text-gold: #B45309 !important;
  --app-gold-accent: #D97706 !important;
  --text-dark: #2D1400 !important;
  --text-mid: #653A10 !important;
  --cream: #FFFBF0 !important;
  --cream-warm: #FFF6E0 !important;
  --card-bg: #FFFFFF !important;
  --card-border: rgba(217, 119, 6, 0.28) !important;

  color: #2D1400 !important;
}

/* All Headings & Section Titles in Light Mode */
body.theme-light .home-grid-title,
body.theme-light .home-section-title,
body.theme-light .section-header,
body.theme-light .section-title,
body.theme-light .page-title,
body.theme-light .drawer-title,
body.theme-light h1,
body.theme-light h2,
body.theme-light h3,
body.theme-light h4,
body.theme-light h5,
body.theme-light h6 {
  color: #3B1600 !important;
  font-weight: 900 !important;
  text-shadow: none !important;
}

/* Card Titles & Names in Light Mode */
body.theme-light .vrat-name,
body.theme-light .vrat-title,
body.theme-light .fest-name,
body.theme-light .grid-card-title,
body.theme-light .card-title,
body.theme-light .deity-name,
body.theme-light .item-title,
body.theme-light .item-name,
body.theme-light .slide-title,
body.theme-light .panchang-val,
body.theme-light .muh-tab-title,
body.theme-light .sk-date-title {
  color: #2D1400 !important;
  font-weight: 800 !important;
  text-shadow: none !important;
}

body.theme-light .vrat-sub,
body.theme-light .vrat-desc,
body.theme-light .fest-sub,
body.theme-light .card-desc,
body.theme-light .item-sub,
body.theme-light .slide-desc,
body.theme-light .panchang-lbl,
body.theme-light p,
body.theme-light span {
  text-shadow: none !important;
}

/* Sub-titles & Secondary Text */
body.theme-light .home-grid-header,
body.theme-light .home-section-row {
  color: #3B1600 !important;
}

/* See All ("सब देखें") Badges / Buttons in Light Mode */
body.theme-light .see-all-toggle-btn,
body.theme-light .see-all-btn,
body.theme-light .cat-see-all,
body.theme-light #toggle-vrats-btn,
body.theme-light #toggle-fest-btn {
  background: linear-gradient(135deg, #FDE68A 0%, #F59E0B 100%) !important;
  color: #1A0B2E !important;
  font-weight: 900 !important;
  border: 1.2px solid #D97706 !important;
  box-shadow: 0 2px 8px rgba(217, 119, 6, 0.22) !important;
  text-shadow: none !important;
}

/* Vrat, Festival & Feature Cards in Light Mode */
body.theme-light .vrat-card,
body.theme-light .fest-card,
body.theme-light .grid-card,
body.theme-light .gallery-card-item,
body.theme-light .amrit-mood-card,
body.theme-light .panchang-card,
body.theme-light .top10-card,
body.theme-light .setting-card,
body.theme-light .katha-card,
body.theme-light .bhajan-card,
body.theme-light .sk-date-card {
  background: #FFFFFF !important;
  border: 1.5px solid rgba(217, 119, 6, 0.28) !important;
  box-shadow: 0 4px 16px rgba(180, 83, 9, 0.09) !important;
  color: #2D1400 !important;
}

body.theme-light .vrat-card:hover,
body.theme-light .fest-card:hover,
body.theme-light .grid-card:hover {
  border-color: #D97706 !important;
  box-shadow: 0 8px 24px rgba(217, 119, 6, 0.2) !important;
}

/* Icon Rings in Light Mode */
body.theme-light .vrat-img-wrap,
body.theme-light .vrat-icon-wrapper {
  background: #FFFBF0 !important;
  border: 2.5px solid #F59E0B !important;
  box-shadow: 0 0 10px rgba(245, 158, 11, 0.3) !important;
}
"""

if 'HIGH-CONTRAST VEDIC LIGHT THEME TYPOGRAPHY & CARD ENGINE' in css:
    css = re.sub(r'/\* ══════════════════════════════════════════════════════════════════════════════\s*☀️ HIGH-CONTRAST VEDIC LIGHT THEME TYPOGRAPHY[\s\S]*', '', css)

css += '\n\n' + light_contrast_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✓ Appended High-Contrast Light Theme CSS to styles.css")

ts = int(time.time())
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Synchronized styles.css cache buster in index.html (v={ts})")
