import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("FIXING AARTI READER TEXT TO SHOW COMPLETE AUTHENTIC LYRICS (GANESH & HANUMAN)")
print("=" * 80)

# 1. Update index.html to have both id="reader-cosmic-content" and id="reader-content"
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

html = html.replace('id="reader-cosmic-content"', 'id="reader-cosmic-content" data-alias="reader-content"')
with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ Updated index.html reader-cosmic-content")

# 2. Update readAartiItemDirect & openAartiItemDirect in app.js
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

robust_aarti_handlers = """
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 GUARANTEED BULLETPROOF AARTI ITEM READER & PLAYER CONTROLLERS
// ══════════════════════════════════════════════════════════════════════════════

window.readAartiItemDirect = function(deityKey, idx) {
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items || !coll.items[idx]) {
    console.warn("Aarti item not found:", deityKey, idx);
    return;
  }
  const item = coll.items[idx];
  
  if (typeof window.closeAartiOptionsModal === 'function') {
    window.closeAartiOptionsModal();
  }

  // 1. Set Header Title
  const titleEl = document.getElementById('reader-page-title');
  if (titleEl) titleEl.textContent = item.title;

  // 2. Set Deity Image & Audio Titles
  const deityImg = document.getElementById('reader-deity-img');
  if (deityImg) deityImg.src = coll.img || coll.fallbackImg || 'assets/deity_ganesh.jpg';

  const aTitleEl = document.getElementById('reader-audio-title');
  if (aTitleEl) aTitleEl.textContent = item.title;

  const aSubEl = document.getElementById('reader-audio-sub');
  if (aSubEl) aSubEl.textContent = `${coll.deity || 'सनातन'} • ${item.sub || 'पावन नित्य आरती'}`;

  // 3. Set Back Button Target to page-home
  window.readerBackPage = 'page-home';
  const backBtn = document.querySelector('#page-reader .back-btn');
  if (backBtn) {
    backBtn.setAttribute('data-back', 'page-home');
    backBtn.onclick = () => window.showPage('page-home');
  }

  // 4. Render Pure, Complete, Authentic Devanagari Lyrics
  const readerContent = document.getElementById('reader-cosmic-content') || document.getElementById('reader-content');
  if (readerContent) {
    readerContent.innerHTML = `
      <div class="pure-reader-wrapper" style="padding: 1.2rem 0 2.5rem; text-align: center;">
        <div style="font-size: 1.3rem; color: #D97706; font-weight: 900; margin-bottom: 0.5rem;">
          ॥ ${item.title} ॥
        </div>
        <div style="font-size: 0.88rem; color: #78350F; font-weight: 700; margin-bottom: 1.5rem; background: rgba(248, 200, 59, 0.15); display: inline-block; padding: 4px 16px; border-radius: 14px; border: 1px solid rgba(248, 200, 59, 0.3);">
          🪔 ${coll.deity} • ${item.sub || 'पावन आरती'}
        </div>
        
        <div class="pure-reader-text" style="font-family: 'Tiro Devanagari Hindi', 'Inter', serif; font-size: 1.2rem; line-height: 2.3; color: #1A0B2E; font-weight: 700; white-space: pre-line; max-width: 680px; margin: 0 auto;">
${item.content}
        </div>

        <div style="margin-top: 2rem; display: flex; justify-content: center; gap: 12px; flex-wrap: wrap;">
          <button onclick="triggerFlowerShower()" style="background: linear-gradient(135deg, #F8C83B, #D97706); color: #1A0B2E; border: none; font-weight: 900; font-size: 0.9rem; padding: 10px 22px; border-radius: 24px; cursor: pointer; box-shadow: 0 4px 15px rgba(248,200,59,0.4); display: inline-flex; align-items: center; gap: 6px;">
            🌸 पुष्प वर्षा करें
          </button>
          <button onclick="shareDivineCard()" style="background: rgba(26, 11, 46, 0.08); color: #1A0B2E; border: 1.5px solid rgba(26, 11, 46, 0.25); font-weight: 800; font-size: 0.9rem; padding: 10px 20px; border-radius: 24px; cursor: pointer; display: inline-flex; align-items: center; gap: 6px;">
            📤 शेयर करें
          </button>
        </div>
      </div>
    `;
  }

  // 5. Open Reader Page
  window.showPage('page-reader');
};

window.playAartiItemDirect = function(deityKey, idx) {
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items || !coll.items[idx]) return;
  const item = coll.items[idx];

  if (typeof window.closeAartiOptionsModal === 'function') {
    window.closeAartiOptionsModal();
  }

  const record = {
    title: item.title,
    deity_name_hi: coll.deity,
    deity_id: deityKey,
    content_type: 'aarti',
    audio_url: item.audio_url || '',
    content: item.content
  };

  // 1. Update Floating Mini Player
  const miniTitle = document.getElementById('glass-mini-title');
  if (miniTitle) miniTitle.textContent = item.title;
  const miniDeity = document.getElementById('glass-mini-deity');
  if (miniDeity) miniDeity.textContent = coll.deity;
  const miniCover = document.getElementById('glass-mini-cover');
  if (miniCover) miniCover.src = coll.img || coll.fallbackImg || 'assets/deity_ganesh.jpg';

  // 2. Update Full Glass Player
  const modalTitle = document.getElementById('glass-modal-title');
  if (modalTitle) modalTitle.textContent = item.title;
  const modalSub = document.getElementById('glass-modal-sub');
  if (modalSub) modalSub.textContent = `${coll.deity} • पावन आरती`;
  const modalImg = document.getElementById('glass-modal-img');
  if (modalImg) modalImg.src = coll.img || coll.fallbackImg || 'assets/deity_ganesh.jpg';

  const lyricsContent = document.getElementById('glass-lyrics-body');
  if (lyricsContent) {
    lyricsContent.textContent = item.content;
  }

  // 3. Play via unified MediaRouter
  if (window.MediaRouter) {
    window.MediaRouter.playRecord(record, 'glass');
  }

  // 4. Open Full Glassmorphic Player
  if (typeof window.openGlassPlayer === 'function') {
    window.openGlassPlayer();
  }
};
"""

js += "\n\n" + robust_aarti_handlers.strip() + "\n"

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Injected robust readAartiItemDirect and playAartiItemDirect handlers in app.js")

# 3. Bump cache buster in index.html
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Updated cache buster ?v={ts} in index.html")

print("=" * 80)
print("AARTI READER TEXT FIX APPLIED SUCCESSFULLY")
print("=" * 80)
