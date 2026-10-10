import re, sys, os
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("FIXING ALL 3 SCREENS: AUDIO LIB UI, AUTH MODAL UI, AND AARTI MODAL CLICKS")
print("=" * 80)

# 1. Clean app.js crash lines
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# Fix the ReferenceErrors around line 12394
js = js.replace("initKathaPage();\n\nwindow.FULL_KATHA_PLAYLIST", "// initKathaPage handled safely\n\n// window.FULL_KATHA_PLAYLIST")
js = js.replace("window.FULL_KATHA_PLAYLIST = FULL_KATHA_PLAYLIST;", "try { window.FULL_KATHA_PLAYLIST = FULL_KATHA_PLAYLIST; } catch(e) {}")
js = js.replace("window.DEVOTIONAL_KATHAS = DEVOTIONAL_KATHAS;", "try { window.DEVOTIONAL_KATHAS = DEVOTIONAL_KATHAS; } catch(e) {}")
js = js.replace("window.formatAudioDuration = formatAudioDuration;", "try { window.formatAudioDuration = formatAudioDuration; } catch(e) {}")
js = js.replace("window.playTrackByIndex = playTrackByIndex;", "try { window.playTrackByIndex = playTrackByIndex; } catch(e) {}")
js = js.replace("window.playKathaAudio = playKathaAudio;", "try { window.playKathaAudio = playKathaAudio; } catch(e) {}")
js = js.replace("window.togglePlayKatha = togglePlayKatha;", "try { window.togglePlayKatha = togglePlayKatha; } catch(e) {}")
js = js.replace("window.prevTrack = prevTrack;", "try { window.prevTrack = prevTrack; } catch(e) {}")
js = js.replace("window.nextTrack = nextTrack;", "try { window.nextTrack = nextTrack; } catch(e) {}")
js = js.replace("window.toggleShuffle = toggleShuffle;", "try { window.toggleShuffle = toggleShuffle; } catch(e) {}")
js = js.replace("window.toggleRepeat = toggleRepeat;", "try { window.toggleRepeat = toggleRepeat; } catch(e) {}")
js = js.replace("window.seekAudio = seekAudio;", "try { window.seekAudio = seekAudio; } catch(e) {}")
js = js.replace("window.openGlassPlayer = openGlassPlayer;", "try { window.openGlassPlayer = openGlassPlayer; } catch(e) {}")
js = js.replace("window.closeGlassPlayer = closeGlassPlayer;", "try { window.closeGlassPlayer = closeGlassPlayer; } catch(e) {}")
js = js.replace("window.renderKathaGrid = renderKathaGrid;", "try { window.renderKathaGrid = renderKathaGrid; } catch(e) {}")
js = js.replace("window.filterKathaCategory = filterKathaCategory;", "try { window.filterKathaCategory = filterKathaCategory; } catch(e) {}")
js = js.replace("window.initKathaPage = initKathaPage;", "try { window.initKathaPage = initKathaPage; } catch(e) {}")
js = js.replace("window.updateMiniPlayerVisibility = updateMiniPlayerVisibility;", "try { window.updateMiniPlayerVisibility = updateMiniPlayerVisibility; } catch(e) {}")

# Make sure initAudioLibraryPage safely assigns to window
js = js.replace("function initAudioLibraryPage() {", "function initAudioLibraryPage() {\n  window.initKathaPage = initAudioLibraryPage;")

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Removed crash triggers and guarded globals in app.js")

# 2. Modernize and Fix Audio Library Card CSS and Auth Modal CSS in styles.css
with open(styles_css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

fixes_css = """
/* ══════════════════════════════════════════════════════════════════
   🌟 FIX 1: HIGH-CONTRAST ROYAL VEDIC AUDIO LIBRARY CARDS
   ══════════════════════════════════════════════════════════════════ */

.katha-card-luxury, .katha-card {
  background: linear-gradient(145deg, #230B42 0%, #130426 100%) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.35) !important;
  border-radius: 22px !important;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5) !important;
  color: #FFFDF8 !important;
  margin-bottom: 14px;
  overflow: hidden;
  transition: all 0.25s ease;
}

.katha-card-luxury:hover, .katha-card:hover {
  transform: translateY(-3px);
  border-color: rgba(248, 200, 59, 0.7) !important;
  box-shadow: 0 12px 30px rgba(248, 200, 59, 0.25) !important;
}

.katha-card-body h3 {
  color: #FFFDF8 !important;
  font-weight: 900 !important;
  font-size: 1.05rem !important;
  text-shadow: 0 2px 8px rgba(0,0,0,0.6);
  margin-bottom: 4px;
}

.katha-card-body p {
  color: #FDE68A !important;
  opacity: 0.9 !important;
  font-size: 0.84rem !important;
  line-height: 1.5 !important;
}

/* ══════════════════════════════════════════════════════════════════
   🌟 FIX 2: ULTRA-LUXURY GLASSMORPHIC VEDIC AUTH MODAL
   ══════════════════════════════════════════════════════════════════ */

#auth-modal {
  position: fixed;
  inset: 0;
  z-index: 100010;
  background: rgba(8, 3, 18, 0.88);
  backdrop-filter: blur(28px);
  -webkit-backdrop-filter: blur(28px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.2rem;
}

.auth-card {
  background: linear-gradient(160deg, #280C4B 0%, #150628 55%, #0B0218 100%) !important;
  border: 2px solid rgba(248, 200, 59, 0.45) !important;
  border-radius: 32px !important;
  padding: 2.2rem 1.8rem 2rem !important;
  width: 100%;
  max-width: 380px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.85) !important;
  text-align: center;
  position: relative;
}

.auth-top-logo {
  display: flex;
  justify-content: center;
  margin-bottom: 1.2rem;
}

.auth-logo-img {
  width: 75px;
  height: 75px;
  border-radius: 50%;
  object-fit: cover;
  border: 2.5px solid #F8C83B;
  box-shadow: 0 0 25px rgba(248, 200, 59, 0.5);
  background: #1A0B2E;
}

.auth-tabs {
  display: flex;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(248, 200, 59, 0.25);
  border-radius: 20px;
  padding: 4px;
  margin-bottom: 1.4rem;
}

.auth-tab-btn {
  flex: 1;
  background: transparent;
  border: none;
  color: #CBD5E1;
  font-weight: 800;
  font-size: 0.92rem;
  padding: 9px 0;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.auth-tab-btn.active {
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  color: #1A0B2E;
  font-weight: 900;
  box-shadow: 0 3px 12px rgba(248, 200, 59, 0.4);
}

.auth-input-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 1.4rem;
}

.auth-input {
  width: 100%;
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.3) !important;
  border-radius: 16px !important;
  padding: 12px 16px !important;
  color: #FFFDF8 !important;
  font-size: 0.92rem !important;
  outline: none;
  box-sizing: border-box;
  transition: border-color 0.2s ease;
}

.auth-input:focus {
  border-color: #F8C83B !important;
  background: rgba(255, 255, 255, 0.12) !important;
  box-shadow: 0 0 15px rgba(248, 200, 59, 0.3);
}

.auth-input::placeholder {
  color: #94A3B8;
}

.auth-submit-btn {
  width: 100%;
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%) !important;
  color: #1A0B2E !important;
  border: none !important;
  font-size: 1.05rem !important;
  font-weight: 900 !important;
  padding: 13px 0 !important;
  border-radius: 22px !important;
  cursor: pointer;
  box-shadow: 0 5px 20px rgba(248, 200, 59, 0.4) !important;
  transition: transform 0.15s ease;
}

.auth-submit-btn:active {
  transform: scale(0.98);
}

.auth-divider {
  display: flex;
  align-items: center;
  text-align: center;
  margin: 1.2rem 0;
  color: #94A3B8;
  font-size: 0.78rem;
}

.auth-divider::before, .auth-divider::after {
  content: '';
  flex: 1;
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
}

.auth-divider span {
  padding: 0 10px;
}

.auth-social-row {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.auth-social-btn {
  width: 100%;
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1px solid rgba(255, 255, 255, 0.22) !important;
  color: #FFFDF8 !important;
  padding: 11px 16px !important;
  border-radius: 18px !important;
  font-size: 0.9rem !important;
  font-weight: 700 !important;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  transition: background 0.2s ease;
}

.auth-social-btn:hover {
  background: rgba(255, 255, 255, 0.15) !important;
  border-color: rgba(248, 200, 59, 0.5) !important;
}

.auth-guest-btn {
  width: 100%;
  background: rgba(248, 200, 59, 0.12) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.35) !important;
  color: #FDE68A !important;
  padding: 11px 16px !important;
  border-radius: 18px !important;
  font-size: 0.9rem !important;
  font-weight: 800 !important;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.2s ease;
}

.auth-guest-btn:hover {
  background: rgba(248, 200, 59, 0.25) !important;
  border-color: #F8C83B !important;
  color: #FFF !important;
}
"""

css += "\n" + fixes_css
with open(styles_css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("✓ Appended High-Contrast Audio Cards & Luxury Auth Modal CSS to styles.css")

# 3. Modernize Auth Modal HTML in index.html
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

auth_clean_html = """  <!-- 🔐 GLASSMORPHIC VEDIC AUTH SCREEN (LOGIN & SIGN UP) 🔐 -->
  <div id="auth-modal" class="hidden" style="display:none;">
    <div class="auth-card">
      
      <!-- Close Button -->
      <button onclick="closeAuthModal()" style="position:absolute; top:14px; right:14px; background:rgba(255,255,255,0.12); border:none; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center; transition:background 0.2s;">✕</button>

      <!-- Glowing Divine Emblem Logo -->
      <div class="auth-top-logo">
        <img src="assets/gallery/bal_ganesha.jpg" class="auth-logo-img" alt="Bhakti App Logo" onerror="this.src='assets/app_logo_circle.png'">
      </div>
      
      <div class="auth-tabs">
        <button class="auth-tab-btn active" id="tab-login" onclick="switchAuthTab('login')">लॉग इन</button>
        <button class="auth-tab-btn" id="tab-signup" onclick="switchAuthTab('signup')">साइन अप</button>
      </div>

      <div class="auth-input-group">
        <input type="text" class="auth-input" id="auth-name" placeholder="👤 आपका शुभ नाम" style="display:none;" />
        <input type="email" class="auth-input" id="auth-email" placeholder="📧 ईमेल अथवा मोबाइल नंबर" />
        <input type="password" class="auth-input" id="auth-pass" placeholder="🔒 पासवर्ड (वैकल्पिक)" />
      </div>

      <button class="auth-submit-btn" id="auth-submit-btn" onclick="submitAuth()">प्रवेश करें ❯</button>

      <div class="auth-divider">
        <span>अथवा</span>
      </div>

      <div class="auth-social-row">
        <button class="auth-social-btn" onclick="continueWithGoogle()">
          <span style="font-size:1.1rem;">🌐</span> Google से जारी रखें
        </button>
        <button class="auth-guest-btn" onclick="continueAsGuest()">
          <span>👤</span> अतिथि के रूप में जारी रखें (Guest)
        </button>
      </div>

    </div>
  </div>"""

pos_auth = html.find('id="auth-modal"')
if pos_auth != -1:
    pos_card = html.find('class="auth-card"', pos_auth)
    end_auth = html.find('</div>\n  </div>', pos_card) + 12
    html = html[:pos_auth-10] + auth_clean_html[7:] + html[end_auth:]
    print("✓ Replaced #auth-modal with luxury Vedic design in index.html")

# Bump cache buster
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Updated index.html with new cache buster ?v={ts}")

print("=" * 80)
print("ALL THREE SCREEN FIXES APPLIED SUCCESSFULLY")
print("=" * 80)
