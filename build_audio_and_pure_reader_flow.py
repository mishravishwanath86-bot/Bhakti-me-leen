import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("CONFIGURING PERFECT AUDIO TIMELINE PLAYER & PURE FULL-TEXT READER FLOW")
print("=" * 80)

with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# 1. Update playAudioLibraryIndex to automatically pop open the Glassmorphic Timeline Player
new_audio_handlers_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🎧 AUDIO LIBRARY ACTIONS: '▶ सुनें' -> FULL TIMELINE PLAYER & '📖 पाठ' -> PURE TEXT READER
// ══════════════════════════════════════════════════════════════════════════════

window.playAudioLibraryIndex = function(idx) {
  if (!window.AUDIO_LIBRARY_ITEMS || idx < 0 || idx >= window.AUDIO_LIBRARY_ITEMS.length) return;
  window.currentAudioIndex = idx;
  const item = window.AUDIO_LIBRARY_ITEMS[idx];
  if (!item) return;

  const thumb = (typeof getDeityArtwork === 'function') 
    ? getDeityArtwork(item.deity_id || item.deity_name_hi, item.title) 
    : 'assets/app_logo.jpg';

  // 1. Update Floating Mini Player
  const miniTitle = document.getElementById('glass-mini-title');
  if (miniTitle) miniTitle.textContent = item.title;
  const miniDeity = document.getElementById('glass-mini-deity');
  if (miniDeity) miniDeity.textContent = item.deity_name_hi || item.deity_id || 'भक्ति रस';
  const miniCover = document.getElementById('glass-mini-cover');
  if (miniCover) miniCover.src = thumb;

  // 2. Update Full Glass Timeline Player
  const modalTitle = document.getElementById('glass-modal-title');
  if (modalTitle) modalTitle.textContent = item.title;
  const modalSub = document.getElementById('glass-modal-sub');
  if (modalSub) modalSub.textContent = `${item.deity_name_hi || item.deity_id || 'सनातन'} • ${(typeof formatTypeBadge === 'function') ? formatTypeBadge(item.content_type) : 'भक्ति'}`;
  const modalImg = document.getElementById('glass-modal-img');
  if (modalImg) modalImg.src = thumb;

  const lyricsContent = document.getElementById('glass-lyrics-content');
  if (lyricsContent) {
    lyricsContent.innerHTML = `<div style="font-size:1rem; line-height:2; color:#FDE68A; white-space:pre-line; text-align:center;">${item.content || item.content_text || '॥ पावन भक्ति रस ॥'}\\n\\n<span style="color:#FFF; font-size:0.8rem;">📖 स्रोत: ${item.audio_url && item.audio_url.startsWith('assets/audio/') ? '💾 ऑफ़लाइन MP3' : '🎬 YouTube HD'}</span></div>`;
  }

  // 3. Play via unified MediaRouter
  if (window.MediaRouter) {
    window.MediaRouter.playRecord(item, 'glass');
  }

  // 4. Open Full Glassmorphic Timeline Scrubber Player Modal
  if (typeof window.openGlassPlayer === 'function') {
    window.openGlassPlayer();
  }
};

window.openReaderFromAudioLib = async function(idx) {
  if (!window.AUDIO_LIBRARY_ITEMS || idx < 0 || idx >= window.AUDIO_LIBRARY_ITEMS.length) return;
  const item = window.AUDIO_LIBRARY_ITEMS[idx];
  if (!item) return;

  // Fetch complete text if content is abbreviated
  let fullContent = item.content || item.content_text || '';
  if (!fullContent || fullContent.length < 50) {
    try {
      const resp = await fetch(`/api/content?id=${item.id}`);
      if (resp.ok) {
        const fullData = await resp.json();
        if (fullData && fullData.content) {
          fullContent = fullData.content;
        }
      }
    } catch(e) {
      console.warn("Could not fetch full content via API:", e);
    }
  }

  if (!fullContent) {
    fullContent = `॥ ${item.title} ॥\\n\\nपावन भक्ति रस एवं नित्य आराधना।`;
  }

  const thumb = (typeof getDeityArtwork === 'function') 
    ? getDeityArtwork(item.deity_id || item.deity_name_hi, item.title) 
    : 'assets/app_logo.jpg';

  // Set Back Button target
  window.readerBackPage = 'page-katha';
  const backBtn = document.querySelector('#page-reader .back-btn');
  if (backBtn) {
    backBtn.setAttribute('data-back', 'page-katha');
    backBtn.onclick = () => window.showPage('page-katha');
  }

  // 1. Set Header Title
  const titleEl = document.getElementById('reader-page-title') || document.querySelector('#page-reader .header-title');
  if (titleEl) titleEl.textContent = item.title;

  // 2. Set Deity Image & Subtitle
  const readerDeityImg = document.getElementById('reader-deity-img');
  if (readerDeityImg) readerDeityImg.src = thumb;

  const aTitleEl = document.getElementById('reader-audio-title');
  if (aTitleEl) aTitleEl.textContent = item.title;
  
  const aSubEl = document.getElementById('reader-audio-sub');
  if (aSubEl) aSubEl.textContent = `${item.deity_name_hi || item.deity_id || 'सनातन'} • पावन स्वाध्याय`;

  // 3. Render Pure, Complete, Beautiful Devanagari Text
  const readerContent = document.getElementById('reader-content');
  if (readerContent) {
    readerContent.innerHTML = `
      <div class="pure-reader-wrapper" style="padding: 1.2rem 0 2.5rem; text-align: center;">
        <div style="font-size: 1.25rem; color: #D97706; font-weight: 900; margin-bottom: 0.5rem;">
          ॥ ${item.title} ॥
        </div>
        <div style="font-size: 0.88rem; color: #78350F; font-weight: 700; margin-bottom: 1.5rem; background: rgba(248, 200, 59, 0.15); display: inline-block; padding: 4px 16px; border-radius: 14px; border: 1px solid rgba(248, 200, 59, 0.3);">
          🪔 ${item.deity_name_hi || item.deity_id || 'सनातन धर्म'} • ${(typeof formatTypeBadge === 'function') ? formatTypeBadge(item.content_type) : 'पाठ'}
        </div>
        
        <div class="pure-reader-text" style="font-family: 'Tiro Devanagari Hindi', serif; font-size: 1.18rem; line-height: 2.3; color: #1A0B2E; font-weight: 700; white-space: pre-line; text-shadow: 0 0 1px rgba(0,0,0,0.1); max-width: 680px; margin: 0 auto;">
${fullContent}
        </div>

        <div style="margin-top: 2rem; display: flex; justify-content: center; gap: 12px;">
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

  // 4. Switch to Reader Page
  window.showPage('page-reader');
};
"""

js += "\n\n" + new_audio_handlers_js.strip() + "\n"

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Injected Audio Timeline and Pure Reader handlers in app.js")

# 2. Add Pure Reader styling in styles.css
pure_reader_css = """
/* ══════════════════════════════════════════════════════════════════
   📖 PURE FULL-TEXT SACRED READER STYLING
   ══════════════════════════════════════════════════════════════════ */

#page-reader {
  background: radial-gradient(circle at 50% 10%, #FFFDF8 0%, #FFF8E7 45%, #FEF3C7 100%) !important;
  color: #1A0B2E !important;
  min-height: 100vh;
}

.pure-reader-wrapper {
  animation: fadeIn 0.3s ease;
}

.pure-reader-text {
  font-family: 'Tiro Devanagari Hindi', 'Inter', serif !important;
  color: #1A0B2E !important;
  letter-spacing: 0.3px;
  word-spacing: 1px;
}
"""

with open(styles_css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + pure_reader_css)
print("✓ Appended Pure Reader CSS in styles.css")

# 3. Bump cache buster in index.html
import time
ts = int(time.time())
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)
with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Updated cache buster ?v={ts} in index.html")

print("=" * 80)
print("AUDIO AND READER FLOW CONFIGURED SUCCESSFULLY")
print("=" * 80)
