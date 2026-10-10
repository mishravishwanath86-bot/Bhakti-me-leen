import re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Define the Next-Gen Luxury Glass Full Player Modal HTML
luxury_player_modal = """
  <!-- ═════════════════════════════════════════════════════════════════════
       🎧 NEXT-GEN LUXURY DIVINE GLASS FULL PLAYER MODAL (APPLE MUSIC GRADE)
       ═════════════════════════════════════════════════════════════════════ -->
  <div id="glass-full-player-modal" class="glass-full-player-modal" style="display:none;">
    <div class="glass-player-stage">
      
      <!-- Top Bar: Minimize, Auspicious Heading, and Dedicated Audio/Video Toggle -->
      <div class="glass-player-topbar">
        <button class="glass-topbar-btn" onclick="closeGlassPlayer()" title="छोटा करें">⌵</button>
        <div class="glass-player-heading">॥ अब बज रहा है ॥</div>
        <button id="glass-mode-toggle-btn" class="glass-mode-toggle-btn" onclick="togglePlayerMediaView()" title="वीडियो देखें / छिपाएं">
          <span>🎬</span> <span id="glass-mode-toggle-text">वीडियो देखें</span>
        </button>
      </div>

      <!-- Video Container (Hidden by default in Audio Mode) -->
      <div id="glass-youtube-container" class="glass-youtube-container" style="display:none;">
        <!-- YouTube iframe injected here dynamically -->
      </div>

      <!-- Centerpiece Deity Artwork (Primary in Audio Mode) -->
      <div id="glass-artwork-container" class="glass-player-centerpiece">
        <div class="glass-disk-halo">
          <img src="assets/app_logo_circle.png" id="glass-modal-img" class="glass-artwork-img" alt="Deity Artwork" onerror="this.src='assets/app_logo_circle.png'" />
        </div>
      </div>

      <!-- Track Metadata Header -->
      <div class="glass-track-meta">
        <div style="flex:1; min-width:0; padding-right:12px;">
          <div class="glass-track-name" id="glass-modal-title">पावन भक्ति संकीर्तन</div>
          <div class="glass-track-artist" id="glass-modal-sub">
            <span class="live-eq-bars" style="margin-right:4px;"><span></span><span></span><span></span></span>
            <span id="glass-modal-deity-badge">✨ दिव्य पावन स्वर</span>
          </div>
        </div>
        <button class="glass-fav-btn" onclick="toggleFavCurrent()" id="glass-modal-fav-btn" title="पसंदीदा में जोड़ें">🤍</button>
      </div>

      <!-- ⏱️ FULL INTERACTIVE TIMELINE SCRUBBER (ALWAYS VISIBLE & WORKING) -->
      <div class="glass-scrub-box" id="glass-scrub-box">
        <div class="glass-time-row">
          <span id="glass-modal-cur-time">00:00</span>
          <span id="glass-modal-tot-time">05:00</span>
        </div>
        <input type="range" class="glass-seekbar" id="glass-modal-seekbar" min="0" max="100" value="0" step="0.1" oninput="onSeekbarInput(this.value)" onchange="onSeekbarChange(this.value)">
      </div>

      <!-- 🎮 LUXURY PLAYBACK CONTROLS ROW -->
      <div class="glass-controls-row">
        <!-- Shuffle -->
        <button class="glass-ctrl-btn glass-ctrl-secondary" onclick="toggleShuffle()" id="glass-shuffle-btn" title="शफल">🔀</button>
        
        <!-- Previous Track -->
        <button class="glass-ctrl-btn glass-ctrl-primary" onclick="prevTrack()" title="पिछला ट्रैक">⏮</button>
        
        <!-- Skip -10s -->
        <button class="glass-ctrl-btn glass-ctrl-skip" onclick="skipAudioSeconds(-10)" title="10 सेकंड पीछे">↺ 10s</button>
        
        <!-- Large Golden Play / Pause Button -->
        <button class="glass-main-play-btn" onclick="togglePlayKatha()" id="glass-modal-play-btn" title="प्ले / पॉज">
          <span id="glass-modal-play-icon">▶</span>
        </button>
        
        <!-- Skip +10s -->
        <button class="glass-ctrl-btn glass-ctrl-skip" onclick="skipAudioSeconds(10)" title="10 सेकंड आगे">↻ 10s</button>
        
        <!-- Next Track -->
        <button class="glass-ctrl-btn glass-ctrl-primary" onclick="nextTrack()" title="अगला ट्रैक">⏭</button>
        
        <!-- Repeat / Loop -->
        <button class="glass-ctrl-btn glass-ctrl-secondary" onclick="toggleRepeat()" id="glass-repeat-btn" title="दोहराएं">🔁</button>
      </div>

      <!-- 📜 EXPANDABLE LYRICS / PATH DRAWER -->
      <button class="glass-lyrics-tab-btn" onclick="toggleLyricsDrawer()">
        <span>📜</span>
        <span id="glass-lyrics-tab-text">पाठ एवं भावार्थ देखें (Lyrics) ⌃</span>
      </button>

      <div id="glass-lyrics-content" class="glass-lyrics-drawer" style="display:none;">
        <div id="glass-lyrics-body" style="color:#FFFDF8; font-size:0.95rem; line-height:1.8; text-align:center;">
          <!-- Lyrics content loaded dynamically -->
        </div>
      </div>

    </div>
  </div>
"""

# Replace all occurrences of old glass-full-player-modal in index.html
player_modal_regex = r'<div[^>]*id="glass-full-player-modal"[\s\S]*?</div>\s*</div>\s*(?=<!--|<div|<section|</body>)'

# Remove any duplicate/old glass-full-player-modal blocks
html_cleaned = re.sub(r'<div[^>]*class="glass-full-player-modal"[^>]*>[\s\S]*?</div>\s*</div>', '', html)
html_cleaned = re.sub(r'<div[^>]*id="glass-full-player-modal"[^>]*>[\s\S]*?</div>\s*</div>', '', html_cleaned)

# Inject the clean new player modal right before </body>
html_final = html_cleaned.replace('</body>', luxury_player_modal + '\n</body>')

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html_final)

print("✓ Updated index.html with Next-Gen Luxury Player Modal & Dedicated Video Switch")
