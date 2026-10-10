import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("OVERHAULING AUDIO PLAYER TO ROYAL CLASSIC VEDIC UI/UX (SPOTIFY + TEMPLE LUXURY)")
print("=" * 80)

# 1. Update Player HTML in index.html
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

classic_player_html = """  <!-- ═════════════════════════════════════════════════════════════════
       🎧 ROYAL CLASSIC DEVOTIONAL AUDIO PLAYER (FULL-SCREEN MODAL)
       ═════════════════════════════════════════════════════════════════ -->
  <div id="glass-full-player-modal" class="classic-player-modal" style="display:none !important;">
    <div class="classic-player-card">
      
      <!-- Top Bar -->
      <div class="classic-player-topbar">
        <button class="classic-topbar-btn" onclick="closeGlassPlayer()" title="छोटा करें">
          <span style="font-size:1.3rem; font-weight:900; line-height:1;">⌄</span>
        </button>
        <div class="classic-player-header-title">॥ अब बज रहा है ॥</div>
        <button class="classic-topbar-btn" onclick="triggerFlowerShower()" title="🌸 पुष्प वर्षा">
          <span>🌸</span>
        </button>
      </div>

      <!-- Deity Artwork Centerpiece -->
      <div class="classic-artwork-wrapper">
        <div class="classic-artwork-ring">
          <img src="assets/gallery/bal_ganesha.jpg" id="glass-modal-img" class="classic-artwork-img" alt="Deity Artwork" onerror="this.src='assets/app_logo_circle.png'" />
        </div>
      </div>

      <!-- Track Metadata & Favorite -->
      <div class="classic-track-info-row">
        <div class="classic-meta-text">
          <h2 id="glass-modal-title" class="classic-track-title">श्री गणेश आरती (जय गणेश देवा)</h2>
          <div id="glass-modal-sub" class="classic-track-sub">
            <span class="classic-live-wave"><span></span><span></span><span></span></span>
            <span id="glass-modal-deity-badge">श्री गणेश जी • दिव्य आरती</span>
          </div>
        </div>
        <button class="classic-fav-btn" onclick="toggleFavCurrent()" id="glass-modal-fav-btn" title="पसंदीदा">
          <span>🤍</span>
        </button>
      </div>

      <!-- ⏱️ Timeline Scrubber -->
      <div class="classic-scrub-container">
        <input type="range" class="classic-seekbar" id="glass-modal-seekbar" min="0" max="100" value="0" step="0.1" oninput="onSeekbarInput(this.value)" onchange="onSeekbarChange(this.value)">
        <div class="classic-timestamps">
          <span id="glass-modal-cur-time">00:00</span>
          <span id="glass-modal-tot-time">05:00</span>
        </div>
      </div>

      <!-- 🎮 Main Playback Controls (Perfect Non-Distorted Circular Sizing) -->
      <div class="classic-controls-primary">
        <button class="classic-ctrl-btn" onclick="skipAudioSeconds(-10)" title="10s पीछे">
          <span class="classic-skip-icon">↺</span>
          <span class="classic-skip-text">10s</span>
        </button>
        
        <button class="classic-ctrl-btn classic-ctrl-skip-step" onclick="prevTrack()" title="पिछला">
          <span>⏮</span>
        </button>

        <button class="classic-play-main-btn" onclick="togglePlayKatha()" id="glass-modal-play-btn" title="प्ले / पॉज">
          <span id="glass-modal-play-icon">▶</span>
        </button>

        <button class="classic-ctrl-btn classic-ctrl-skip-step" onclick="nextTrack()" title="अगला">
          <span>⏭</span>
        </button>

        <button class="classic-ctrl-btn" onclick="skipAudioSeconds(10)" title="10s आगे">
          <span class="classic-skip-icon">↻</span>
          <span class="classic-skip-text">10s</span>
        </button>
      </div>

      <!-- ⚙️ Secondary Toolbar (Shuffle, Speed, Repeat) -->
      <div class="classic-controls-secondary">
        <button class="classic-sec-btn" onclick="toggleShuffle()" id="glass-shuffle-btn" title="शफल">
          <span>🔀</span>
        </button>
        
        <button class="classic-speed-pill" onclick="cycleAudioSpeed()" id="glass-speed-btn" title="ऑडियो स्पीड">
          <span id="glass-speed-label">1.0x</span>
        </button>

        <button class="classic-sec-btn" onclick="toggleRepeat()" id="glass-repeat-btn" title="दोहराएं">
          <span>🔁</span>
        </button>
      </div>

      <!-- 📜 Lyrics & Katha Drawer Button -->
      <button class="classic-lyrics-toggle-btn" onclick="toggleLyricsDrawer()">
        <span>📜</span>
        <span id="glass-lyrics-tab-text">पाठ एवं भावार्थ देखें (Lyrics) ▴</span>
      </button>

      <!-- Lyrics / Full Text Drawer -->
      <div id="glass-lyrics-content" class="classic-lyrics-drawer" style="display:none;">
        <div id="glass-lyrics-body" class="classic-lyrics-text"></div>
      </div>

    </div>
  </div>"""

pos_player = html.find('id="glass-full-player-modal"')
if pos_player != -1:
    pos_end = html.find('</div>\n  </div>', pos_player)
    # Find outer closing div
    outer_end = html.find('</div>', pos_end + 10) + 6
    html = html[:pos_player-10] + classic_player_html[7:] + html[outer_end:]
    print("✓ Replaced player markup with Royal Classic design in index.html")

# 2. Append Royal Classic Player CSS in styles.css
classic_player_css = """
/* ══════════════════════════════════════════════════════════════════
   🌟 ROYAL CLASSIC DEVOTIONAL AUDIO PLAYER STYLES (SPOTIFY + VEDIC)
   ══════════════════════════════════════════════════════════════════ */

.classic-player-modal {
  position: fixed !important;
  inset: 0 !important;
  z-index: 100020 !important;
  background: radial-gradient(circle at 50% 20%, rgba(32, 10, 60, 0.98) 0%, rgba(14, 4, 28, 0.99) 60%, rgba(6, 1, 14, 1) 100%) !important;
  backdrop-filter: blur(35px) !important;
  -webkit-backdrop-filter: blur(35px) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 1.2rem 1.4rem !important;
  box-sizing: border-box !important;
  overflow-y: auto !important;
}

.classic-player-card {
  width: 100% !important;
  max-width: 390px !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: space-between !important;
  margin: auto 0 !important;
}

/* Topbar */
.classic-player-topbar {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  width: 100% !important;
  margin-bottom: 1.2rem !important;
}

.classic-topbar-btn {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1px solid rgba(248, 200, 59, 0.25) !important;
  color: #FDE68A !important;
  width: 40px !important;
  height: 40px !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}

.classic-topbar-btn:active {
  transform: scale(0.92) !important;
}

.classic-player-header-title {
  font-size: 0.95rem !important;
  font-weight: 800 !important;
  color: #FDE68A !important;
  letter-spacing: 0.8px !important;
  text-shadow: 0 0 15px rgba(248, 200, 59, 0.4) !important;
}

/* Artwork Canvas */
.classic-artwork-wrapper {
  margin: 0.5rem 0 1.2rem !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100% !important;
}

.classic-artwork-ring {
  width: 220px !important;
  height: 220px !important;
  border-radius: 28px !important;
  padding: 5px !important;
  background: linear-gradient(135deg, rgba(248, 200, 59, 0.7) 0%, rgba(217, 119, 6, 0.4) 50%, rgba(248, 200, 59, 0.8) 100%) !important;
  box-shadow: 0 15px 45px rgba(0, 0, 0, 0.75), 0 0 30px rgba(248, 200, 59, 0.25) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.classic-artwork-img {
  width: 100% !important;
  height: 100% !important;
  border-radius: 24px !important;
  object-fit: cover !important;
  display: block !important;
}

/* Metadata */
.classic-track-info-row {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  width: 100% !important;
  margin-bottom: 1.2rem !important;
}

.classic-meta-text {
  flex: 1 !important;
  min-width: 0 !important;
  padding-right: 10px !important;
}

.classic-track-title {
  font-size: 1.18rem !important;
  font-weight: 900 !important;
  color: #FFFDF8 !important;
  margin: 0 0 4px 0 !important;
  line-height: 1.3 !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  text-shadow: 0 2px 8px rgba(0,0,0,0.5) !important;
}

.classic-track-sub {
  font-size: 0.86rem !important;
  color: #FDE68A !important;
  font-weight: 700 !important;
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
}

.classic-live-wave {
  display: inline-flex !important;
  align-items: flex-end !important;
  gap: 2px !important;
  height: 12px !important;
}

.classic-live-wave span {
  width: 2.5px !important;
  height: 100% !important;
  background: #F8C83B !important;
  border-radius: 2px !important;
  animation: waveAnim 1s ease-in-out infinite alternate !important;
}
.classic-live-wave span:nth-child(2) { animation-delay: 0.2s !important; }
.classic-live-wave span:nth-child(3) { animation-delay: 0.4s !important; }

@keyframes waveAnim {
  0% { height: 3px; }
  100% { height: 12px; }
}

.classic-fav-btn {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.3) !important;
  color: #FFF !important;
  width: 44px !important;
  height: 44px !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-size: 1.15rem !important;
  cursor: pointer !important;
  flex-shrink: 0 !important;
  transition: all 0.2s ease !important;
}

.classic-fav-btn:active {
  transform: scale(0.9) !important;
}

/* ⏱️ Scrubber Timeline */
.classic-scrub-container {
  width: 100% !important;
  margin-bottom: 1.2rem !important;
}

.classic-seekbar {
  width: 100% !important;
  height: 6px !important;
  border-radius: 3px !important;
  background: rgba(255, 255, 255, 0.18) !important;
  accent-color: #F8C83B !important;
  outline: none !important;
  cursor: pointer !important;
  margin-bottom: 6px !important;
}

.classic-timestamps {
  display: flex !important;
  justify-content: space-between !important;
  font-size: 0.78rem !important;
  font-weight: 700 !important;
  color: #CBD5E1 !important;
  font-family: monospace !important;
}

/* 🎮 Primary Controls (Perfect Circles, No Squishing!) */
.classic-controls-primary {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  width: 100% !important;
  max-width: 360px !important;
  margin: 0 auto 1.2rem !important;
}

.classic-ctrl-btn {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1px solid rgba(248, 200, 59, 0.25) !important;
  color: #FDE68A !important;
  width: 44px !important;
  height: 44px !important;
  border-radius: 50% !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  flex-shrink: 0 !important;
  transition: all 0.2s ease !important;
}

.classic-ctrl-skip-step {
  font-size: 1.15rem !important;
  color: #FFF !important;
}

.classic-skip-icon {
  font-size: 0.95rem !important;
  line-height: 1 !important;
}

.classic-skip-text {
  font-size: 0.65rem !important;
  font-weight: 800 !important;
  line-height: 1 !important;
  margin-top: 1px !important;
}

.classic-ctrl-btn:active {
  transform: scale(0.9) !important;
  background: rgba(248, 200, 59, 0.25) !important;
}

.classic-play-main-btn {
  width: 66px !important;
  height: 66px !important;
  border-radius: 50% !important;
  background: linear-gradient(135deg, #FDE68A 0%, #F59E0B 50%, #D97706 100%) !important;
  border: 3px solid #FEF3C7 !important;
  color: #1A0B2E !important;
  font-size: 1.6rem !important;
  font-weight: 900 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  flex-shrink: 0 !important;
  box-shadow: 0 8px 30px rgba(245, 158, 11, 0.6), 0 0 20px rgba(248, 200, 59, 0.4) !important;
  transition: all 0.2s ease !important;
}

.classic-play-main-btn:active {
  transform: scale(0.92) !important;
}

/* Secondary Toolbar */
.classic-controls-secondary {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 20px !important;
  width: 100% !important;
  margin-bottom: 1.2rem !important;
}

.classic-sec-btn {
  background: rgba(255, 255, 255, 0.06) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  color: #CBD5E1 !important;
  width: 36px !important;
  height: 36px !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-size: 1rem !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}

.classic-sec-btn.active {
  background: rgba(248, 200, 59, 0.25) !important;
  border-color: #F8C83B !important;
  color: #FDE68A !important;
}

.classic-speed-pill {
  background: rgba(248, 200, 59, 0.12) !important;
  border: 1px solid rgba(248, 200, 59, 0.35) !important;
  color: #FDE68A !important;
  font-size: 0.8rem !important;
  font-weight: 800 !important;
  padding: 4px 12px !important;
  border-radius: 12px !important;
  cursor: pointer !important;
}

/* Lyrics Toggle */
.classic-lyrics-toggle-btn {
  width: 100% !important;
  background: rgba(255, 255, 255, 0.07) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.3) !important;
  color: #FDE68A !important;
  font-size: 0.86rem !important;
  font-weight: 800 !important;
  padding: 10px 16px !important;
  border-radius: 18px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}

.classic-lyrics-toggle-btn:hover {
  background: rgba(248, 200, 59, 0.18) !important;
  border-color: #F8C83B !important;
}

.classic-lyrics-drawer {
  width: 100% !important;
  background: rgba(18, 6, 36, 0.95) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.35) !important;
  border-radius: 20px !important;
  padding: 1.2rem !important;
  margin-top: 10px !important;
  max-height: 250px !important;
  overflow-y: auto !important;
  box-shadow: 0 10px 30px rgba(0,0,0,0.6) !important;
}

.classic-lyrics-text {
  font-family: 'Tiro Devanagari Hindi', serif !important;
  color: #FFFDF8 !important;
  font-size: 0.98rem !important;
  line-height: 2 !important;
  text-align: center !important;
  white-space: pre-line !important;
}
"""

with open(styles_css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + classic_player_css)
print("✓ Appended Royal Classic Audio Player CSS to styles.css")

# 3. Add cycleAudioSpeed function in app.js
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

speed_helper_js = """
// Audio Playback Speed Controller (1.0x -> 1.25x -> 1.5x -> 0.75x -> 1.0x)
window.audioPlaybackSpeed = 1.0;
window.cycleAudioSpeed = function() {
  const speeds = [1.0, 1.25, 1.5, 0.75];
  let curIdx = speeds.indexOf(window.audioPlaybackSpeed);
  if (curIdx === -1) curIdx = 0;
  window.audioPlaybackSpeed = speeds[(curIdx + 1) % speeds.length];
  
  const lbl = document.getElementById('glass-speed-label');
  if (lbl) lbl.textContent = window.audioPlaybackSpeed + 'x';
  
  if (window.coreAudioElement) {
    window.coreAudioElement.playbackRate = window.audioPlaybackSpeed;
  }
};
"""

if 'window.cycleAudioSpeed' not in js:
    js += "\n\n" + speed_helper_js.strip() + "\n"
    with open(app_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("✓ Added cycleAudioSpeed helper to app.js")

# 4. Bump Cache Buster in index.html
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Saved updated index.html with new cache buster ?v={ts}")

print("=" * 80)
print("ROYAL CLASSIC AUDIO PLAYER OVERHAUL COMPLETE!")
print("=" * 80)
