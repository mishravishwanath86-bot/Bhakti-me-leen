import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

index_html_path = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\index.html")

with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print(f"Initial length: {len(html)}")

# Find the end of page-ramnavami
ramnavami_end = html.find('🥗 Kosambari</div>\n          </div>\n        </div>\n      </div>\n    </section>')
if ramnavami_end == -1:
    ramnavami_end = html.find('🥗 Kosambari</div>')
    # Find next </section>
    ramnavami_end = html.find('</section>', ramnavami_end) + len('</section>')

print(f"Ramnavami end position: {ramnavami_end}")

# Slice html up to the clean end of ramnavami
clean_sections_html = html[:ramnavami_end]

# Check inside clean_sections_html for any stray mini-players or scrubber boxes
clean_sections_html = re.sub(r'<div class="glass-mini-player"[\s\S]*?</div>\s*</div>', '', clean_sections_html)
clean_sections_html = re.sub(r'<div class="mini-player[^"]*" id="mini-player"[\s\S]*?</div>\s*</div>', '', clean_sections_html)
clean_sections_html = re.sub(r'<div class="glass-full-player hidden" id="full-player"[\s\S]*?</div>\s*</div>\s*</div>', '', clean_sections_html)

# Append clean closing elements
clean_tail = """
  </main>

  <!-- 🌟 FLOATING BOTTOM NAVIGATION (5 TABS) 🌟 -->
  <nav class="app-bottom-nav">
    <button class="nav-item active" data-page="page-home" onclick="showPage('page-home')">
      <span class="nav-icon">🏠</span>
      <span class="nav-label">होम</span>
    </button>
    <button class="nav-item" data-page="page-katha" onclick="showPage('page-katha')">
      <span class="nav-icon">🎧</span>
      <span class="nav-label">ऑडियो</span>
    </button>
    <button class="nav-item" data-page="page-mala" onclick="showPage('page-mala')">
      <span class="nav-icon">📿</span>
      <span class="nav-label">जाप माला</span>
    </button>
    <button class="nav-item" data-page="page-aarti-stage" onclick="showPage('page-aarti-stage')">
      <span class="nav-icon">🪔</span>
      <span class="nav-label">आरती दर्शन</span>
    </button>
    <button class="nav-item" data-page="page-panchang" onclick="showPage('page-panchang')">
      <span class="nav-icon">📅</span>
      <span class="nav-label">पंचांग</span>
    </button>
  </nav>

  <!-- ═════════════════════════════════════════════════════════════════════
       🎧 ON-DEMAND FULL SCREEN DEVOTIONAL PLAYER (HIDDEN BY DEFAULT)
       ═════════════════════════════════════════════════════════════════════ -->
  <div id="glass-full-player-modal" class="glass-full-player-modal" style="display:none !important;">
    <div class="glass-player-stage">
      
      <!-- Top Bar -->
      <div class="glass-player-topbar">
        <button class="glass-topbar-btn" onclick="closeGlassPlayer()" title="छोटा करें">⌵</button>
        <div class="glass-player-heading">॥ अब बज रहा है ॥</div>
        <button id="glass-mode-toggle-btn" class="glass-mode-toggle-btn" onclick="togglePlayerMediaView()" title="वीडियो देखें / छिपाएं">
          <span>🎬</span> <span id="glass-mode-toggle-text">वीडियो देखें</span>
        </button>
      </div>

      <!-- Video Container (Hidden in Audio Mode) -->
      <div id="glass-youtube-container" class="glass-youtube-container" style="display:none;"></div>

      <!-- Deity Artwork Centerpiece (Primary in Audio Mode) -->
      <div id="glass-artwork-container" class="glass-player-centerpiece">
        <div class="glass-disk-halo">
          <img src="assets/app_logo_circle.png" id="glass-modal-img" class="glass-artwork-img" alt="Deity" onerror="this.src='assets/app_logo_circle.png'" />
        </div>
      </div>

      <!-- Track Metadata -->
      <div class="glass-track-meta">
        <div style="flex:1; min-width:0; padding-right:12px;">
          <div class="glass-track-name" id="glass-modal-title">पावन भक्ति संकीर्तन</div>
          <div class="glass-track-artist" id="glass-modal-sub">
            <span class="live-eq-bars" style="margin-right:4px;"><span></span><span></span><span></span></span>
            <span id="glass-modal-deity-badge">✨ दिव्य पावन स्वर</span>
          </div>
        </div>
        <button class="glass-fav-btn" onclick="toggleFavCurrent()" id="glass-modal-fav-btn" title="पसंदीदा">🤍</button>
      </div>

      <!-- ⏱️ Timeline & Scrubber -->
      <div class="glass-scrub-box" id="glass-scrub-box">
        <div class="glass-time-row">
          <span id="glass-modal-cur-time">00:00</span>
          <span id="glass-modal-tot-time">05:00</span>
        </div>
        <input type="range" class="glass-seekbar" id="glass-modal-seekbar" min="0" max="100" value="0" step="0.1" oninput="onSeekbarInput(this.value)" onchange="onSeekbarChange(this.value)">
      </div>

      <!-- Playback Controls -->
      <div class="glass-controls-row">
        <button class="glass-ctrl-btn glass-ctrl-secondary" onclick="toggleShuffle()" id="glass-shuffle-btn" title="शफल">🔀</button>
        <button class="glass-ctrl-btn glass-ctrl-primary" onclick="prevTrack()" title="पिछला">⏮</button>
        <button class="glass-ctrl-btn glass-ctrl-skip" onclick="skipAudioSeconds(-10)" title="10s पीछे">↺ 10s</button>
        <button class="glass-main-play-btn" onclick="togglePlayKatha()" id="glass-modal-play-btn" title="प्ले / पॉज">
          <span id="glass-modal-play-icon">▶</span>
        </button>
        <button class="glass-ctrl-btn glass-ctrl-skip" onclick="skipAudioSeconds(10)" title="10s आगे">↻ 10s</button>
        <button class="glass-ctrl-btn glass-ctrl-primary" onclick="nextTrack()" title="अगला">⏭</button>
        <button class="glass-ctrl-btn glass-ctrl-secondary" onclick="toggleRepeat()" id="glass-repeat-btn" title="दोहराएं">🔁</button>
      </div>

      <!-- Lyrics Drawer -->
      <button class="glass-lyrics-tab-btn" onclick="toggleLyricsDrawer()">
        <span>📜</span>
        <span id="glass-lyrics-tab-text">पाठ एवं भावार्थ देखें (Lyrics) ⌃</span>
      </button>

      <div id="glass-lyrics-content" class="glass-lyrics-drawer" style="display:none;">
        <div id="glass-lyrics-body" style="color:#FFFDF8; font-size:0.95rem; line-height:1.8; text-align:center;"></div>
      </div>

    </div>
  </div>

</body>
</html>
"""

final_html = clean_sections_html.rstrip() + '\n' + clean_tail

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"✓ Deep cleaned index.html successfully! Final size: {len(final_html)} chars")
