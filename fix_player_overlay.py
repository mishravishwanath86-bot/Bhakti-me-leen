import re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html = BASE_DIR / "index.html"
styles_css = BASE_DIR / "styles.css"
app_js = BASE_DIR / "app.js"

print("=" * 80)
print("FIXING BOTTOM PLAYER OVERLAY — HIDING COMPLETELY ACROSS ALL PAGES")
print("=" * 80)

# 1. Clean styles.css
with open(styles_css, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Fix .glass-full-player-modal in styles.css to be hidden by default
fix_css = """
/* ══════════════════════════════════════════════════════════════════
   🎧 GLASS FULL-SCREEN PLAYER MODAL (HIDDEN BY DEFAULT, OPENS ONLY ON DEMAND)
   ══════════════════════════════════════════════════════════════════ */
.glass-full-player-modal {
  display: none !important;
  position: fixed !important;
  inset: 0 !important;
  z-index: 100000 !important;
  background: radial-gradient(circle at 50% 20%, rgba(35, 10, 68, 0.98) 0%, rgba(15, 4, 30, 0.99) 55%, rgba(6, 1, 14, 1) 100%) !important;
  backdrop-filter: blur(35px) !important;
  -webkit-backdrop-filter: blur(35px) !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start !important;
  overflow-y: auto !important;
  padding: 1.2rem 1.4rem 2.5rem !important;
  opacity: 0 !important;
  pointer-events: none !important;
  transform: translateY(100%) !important;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease !important;
}

.glass-full-player-modal.open {
  display: flex !important;
  opacity: 1 !important;
  pointer-events: auto !important;
  transform: translateY(0) !important;
}

/* Hide any persistent floating mini-players */
#floating-mini-player,
#glass-mini-player,
#mini-player,
.glass-mini-player,
.mini-player {
  display: none !important;
}
"""

with open(styles_css, 'a', encoding='utf-8') as f:
    f.write("\n" + fix_css)
print("✓ Fixed styles.css: Player modal is hidden by default and only opens when .open is present")

# 2. Clean index.html
with open(index_html, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Ensure any floating mini player is hidden or removed from HTML
html = re.sub(r'<div[^>]*id="floating-mini-player"[\s\S]*?</div>\s*</div>\s*</div>', '', html)
html = re.sub(r'<div[^>]*id="glass-mini-player"[\s\S]*?</div>\s*</div>', '', html)
html = re.sub(r'<div class="mini-player[^"]*" id="mini-player"[\s\S]*?</div>\s*</div>', '', html)

# Make sure #glass-full-player-modal has class="glass-full-player-modal" and style="display:none !important;"
html = re.sub(
    r'<div[^>]*id="glass-full-player-modal"[^>]*>',
    '<div id="glass-full-player-modal" class="glass-full-player-modal" style="display:none !important;">',
    html
)

with open(index_html, 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ Cleaned index.html: Removed sticky bottom mini players and hid full player modal")

# 3. Update app.js openGlassPlayer & closeGlassPlayer
with open(app_js, 'r', encoding='utf-8', errors='ignore') as f:
    js_code = f.read()

open_close_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🎧 SAFE FULL-SCREEN PLAYER OPEN / CLOSE CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

function openGlassPlayer() {
  const modal = document.getElementById('glass-full-player-modal');
  if (modal) {
    modal.classList.add('open');
    modal.style.setProperty('display', 'flex', 'important');
    modal.style.opacity = '1';
    modal.style.pointerEvents = 'auto';
    modal.style.transform = 'translateY(0)';
  }
}

function closeGlassPlayer() {
  const modal = document.getElementById('glass-full-player-modal');
  if (modal) {
    modal.classList.remove('open');
    modal.style.setProperty('display', 'none', 'important');
    modal.style.opacity = '0';
    modal.style.pointerEvents = 'none';
    modal.style.transform = 'translateY(100%)';
  }
}
"""

with open(app_js, 'a', encoding='utf-8') as f:
    f.write("\n" + open_close_js)
print("✓ Updated app.js: openGlassPlayer and closeGlassPlayer enforce strict show/hide")

print("=" * 80)
print("PLAYER OVERLAY REMOVAL COMPLETE")
print("=" * 80)
