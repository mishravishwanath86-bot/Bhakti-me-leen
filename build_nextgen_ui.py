import re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("BUILDING NEXT-GEN LUXURY BHAKTI APP UI/UX")
print("=" * 80)

# ==============================================================================
# 1. ENHANCE styles.css WITH NEXT-GEN LUXURY STYLING
# ==============================================================================
with open(styles_css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css_content = f.read()

luxury_css_addon = """
/* ══════════════════════════════════════════════════════════════════
   🌟 NEXT-GEN DIVINE LUXURY UI/UX DESIGN SYSTEM (APPLE MUSIC / SPOTIFY GRADE)
   ══════════════════════════════════════════════════════════════════ */
@import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Outfit:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&family=Rozha+One&display=swap');

:root {
  --bg-deep-canvas: #090314;
  --bg-midnight-amethyst: #140728;
  --gold-primary: #F8C83B;
  --gold-shimmer: #FDE68A;
  --gold-glow: rgba(248, 200, 59, 0.4);
  --saffron-sacred: #FF6B00;
  --vermilion-divine: #E11D48;
  --glass-surface: rgba(25, 10, 48, 0.72);
  --glass-card: rgba(35, 14, 66, 0.65);
  --glass-border: rgba(248, 200, 59, 0.28);
  --glass-border-hover: rgba(248, 200, 59, 0.6);
  --font-display: 'Rozha One', 'Cinzel Decorative', 'Tiro Devanagari Hindi', serif;
  --font-modern: 'Outfit', 'Inter', 'Noto Sans Devanagari', sans-serif;
}

/* 🌟 GLOBAL LUXURY AMBIENCE */
body {
  font-family: var(--font-modern);
  background: radial-gradient(circle at 50% 0%, #2A0D52 0%, #130526 40%, #080212 100%) !important;
  color: #FFFDF8 !important;
  min-height: 100vh;
  overflow-x: hidden;
}

/* 🌟 FLOATING GLASS HEADER */
.app-header {
  background: rgba(18, 6, 36, 0.85) !important;
  backdrop-filter: blur(20px) !important;
  -webkit-backdrop-filter: blur(20px) !important;
  border-bottom: 1px solid rgba(248, 200, 59, 0.22) !important;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.5) !important;
  position: sticky;
  top: 0;
  z-index: 999;
}
.header-title {
  font-family: var(--font-display) !important;
  background: linear-gradient(135deg, #FFFDF8 0%, #FDE68A 50%, #F8C83B 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  letter-spacing: 0.5px;
  font-size: 1.35rem !important;
  text-shadow: 0 0 25px rgba(248, 200, 59, 0.3);
}

/* 🌟 FLOATING CAPSULE BOTTOM NAVIGATION BAR */
.app-bottom-nav {
  position: fixed !important;
  bottom: 14px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: calc(100% - 24px) !important;
  max-width: 480px !important;
  height: 68px !important;
  background: rgba(20, 8, 40, 0.92) !important;
  backdrop-filter: blur(24px) !important;
  -webkit-backdrop-filter: blur(24px) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.35) !important;
  border-radius: 34px !important;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.75), 0 0 20px rgba(248, 200, 59, 0.15) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-around !important;
  padding: 0 8px !important;
  z-index: 1000 !important;
}

.nav-item {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  background: transparent !important;
  border: none !important;
  color: rgba(253, 230, 138, 0.65) !important;
  padding: 6px 12px !important;
  border-radius: 20px !important;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
  cursor: pointer !important;
  position: relative !important;
}

.nav-item.active {
  color: #1A0B2E !important;
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%) !important;
  box-shadow: 0 4px 18px rgba(248, 200, 59, 0.45) !important;
  transform: translateY(-3px) scale(1.05) !important;
}

.nav-item .nav-icon {
  font-size: 1.25rem !important;
  line-height: 1 !important;
  margin-bottom: 2px !important;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3)) !important;
}

.nav-item .nav-label {
  font-size: 0.68rem !important;
  font-weight: 800 !important;
  letter-spacing: 0.3px !important;
}

/* 🌟 PERSISTENT FLOATING GLASS MINI-PLAYER */
#floating-mini-player {
  position: fixed;
  bottom: 88px;
  left: 50%;
  transform: translateX(-50%);
  width: calc(100% - 24px);
  max-width: 480px;
  background: rgba(25, 9, 50, 0.94);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1.5px solid rgba(248, 200, 59, 0.4);
  border-radius: 22px;
  padding: 10px 14px;
  box-shadow: 0 14px 35px rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 999;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  animation: slideUpMini 0.35s ease-out;
}

@keyframes slideUpMini {
  from { opacity: 0; transform: translate(-50%, 20px); }
  to { opacity: 1; transform: translate(-50%, 0); }
}

.mini-track-info {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
  min-width: 0;
  cursor: pointer;
}

.mini-disc-art {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  border: 1.5px solid #F8C83B;
  object-fit: cover;
  animation: spinDisc 12s linear infinite;
  box-shadow: 0 0 12px rgba(248, 200, 59, 0.4);
}

@keyframes spinDisc {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.mini-text-box {
  min-width: 0;
}

.mini-track-title {
  font-size: 0.88rem;
  font-weight: 800;
  color: #FFFDF8;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.mini-track-deity {
  font-size: 0.74rem;
  color: #FDE68A;
  display: flex;
  align-items: center;
  gap: 4px;
}

/* 🌟 LIVE SOUND EQUALIZER ANIMATION */
.live-eq-bars {
  display: inline-flex;
  align-items: flex-end;
  gap: 2.5px;
  height: 14px;
}

.live-eq-bars span {
  width: 3px;
  background: #F8C83B;
  border-radius: 2px;
  animation: eqPulse 1s ease-in-out infinite alternate;
}

.live-eq-bars span:nth-child(1) { height: 60%; animation-delay: 0.1s; }
.live-eq-bars span:nth-child(2) { height: 100%; animation-delay: 0.3s; }
.live-eq-bars span:nth-child(3) { height: 40%; animation-delay: 0.2s; }
.live-eq-bars span:nth-child(4) { height: 80%; animation-delay: 0.4s; }

@keyframes eqPulse {
  0% { height: 25%; }
  100% { height: 100%; }
}

/* 🌟 LUXURY AUDIO CARDS */
.katha-card {
  background: linear-gradient(145deg, rgba(32, 12, 60, 0.85) 0%, rgba(18, 6, 36, 0.9) 100%) !important;
  border: 1.5px solid rgba(248, 200, 59, 0.25) !important;
  border-radius: 20px !important;
  padding: 1.1rem !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4) !important;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
  position: relative !important;
  overflow: hidden !important;
}

.katha-card:hover {
  transform: translateY(-4px) scale(1.01) !important;
  border-color: rgba(248, 200, 59, 0.65) !important;
  box-shadow: 0 14px 35px rgba(248, 200, 59, 0.2), 0 8px 30px rgba(0,0,0,0.6) !important;
}

.katha-play-btn {
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%) !important;
  color: #1A0B2E !important;
  font-weight: 900 !important;
  font-size: 0.88rem !important;
  padding: 8px 20px !important;
  border-radius: 18px !important;
  border: none !important;
  cursor: pointer !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  box-shadow: 0 4px 14px rgba(248, 200, 59, 0.35) !important;
  transition: all 0.2s ease !important;
}

.katha-play-btn:hover {
  transform: scale(1.06) !important;
  box-shadow: 0 6px 20px rgba(248, 200, 59, 0.6) !important;
}

/* 🌟 FILTER PILLS (SILKY SMOOTH) */
.katha-tab-btn {
  background: rgba(35, 14, 66, 0.6) !important;
  border: 1px solid rgba(248, 200, 59, 0.3) !important;
  color: #FDE68A !important;
  padding: 8px 16px !important;
  border-radius: 20px !important;
  font-weight: 700 !important;
  font-size: 0.84rem !important;
  white-space: nowrap !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}

.katha-tab-btn.active {
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%) !important;
  color: #1A0B2E !important;
  border-color: #F8C83B !important;
  box-shadow: 0 4px 16px rgba(248, 200, 59, 0.4) !important;
}

/* 🌟 JAPA MALA & AARTI STAGE CARDS */
.mala-ring-container {
  position: relative;
  width: 240px;
  height: 240px;
  margin: 1.5rem auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.mala-bead-svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.mala-bead-circle-bg {
  fill: none;
  stroke: rgba(248, 200, 59, 0.15);
  stroke-width: 10;
}

.mala-bead-circle-prog {
  fill: none;
  stroke: url(#goldGradient);
  stroke-width: 10;
  stroke-linecap: round;
  stroke-dasharray: 660;
  stroke-dashoffset: 660;
  transition: stroke-dashoffset 0.25s ease;
}

.mala-center-count {
  position: absolute;
  text-align: center;
}

.mala-num {
  font-size: 3.2rem;
  font-weight: 900;
  font-family: var(--font-display);
  background: linear-gradient(135deg, #FFFDF8 0%, #FDE68A 50%, #F8C83B 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1;
}

.mala-target {
  font-size: 0.85rem;
  color: #FBCFE8;
  font-weight: 700;
  margin-top: 4px;
}
"""

if "NEXT-GEN DIVINE LUXURY UI/UX DESIGN SYSTEM" not in css_content:
    with open(styles_css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + luxury_css_addon)
    print("✓ Appended Next-Gen Luxury CSS tokens to styles.css")
else:
    print("styles.css already contains luxury design tokens.")

# ==============================================================================
# 2. UPDATE index.html (NAVBAR, JAPA MALA PAGE, AARTI STAGE, MINI PLAYER DOCK)
# ==============================================================================
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Update bottom navigation to 5 modern items: Home, Audio, Japa Mala, Aarti, Panchang
old_nav_pattern = r'<nav class="app-bottom-nav">[\s\S]*?</nav>'

new_bottom_nav = """<nav class="app-bottom-nav">
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
  </nav>"""

if re.search(old_nav_pattern, html):
    html = re.sub(old_nav_pattern, new_bottom_nav, html, count=1)
    print("✓ Modernized bottom navigation bar in index.html")

# Add Japa Mala and Virtual Aarti pages before </main>
japa_mala_page_html = """
    <!-- 📿 INTERACTIVE DIGITAL JAPA MALA (108 COUNTER) 📿 -->
    <section id="page-mala" class="page">
      <div class="page-header-bar">
        <button class="back-btn" onclick="showPage('page-home')">←</button>
        <h2>📿 डिजिटल नाम जाप माला</h2>
        <button class="katha-search-btn" onclick="resetJapaMala()">🔄</button>
      </div>

      <div style="background:linear-gradient(135deg, #1C0A35 0%, #3B1259 50%, #150628 100%); border-radius:24px; padding:1.5rem 1.2rem; margin-bottom:1.2rem; border:1.5px solid rgba(248, 200, 59, 0.4); text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.6);">
        <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(248,200,59,0.18); border:1px solid rgba(248,200,59,0.4); padding:4px 14px; border-radius:20px; font-size:0.8rem; font-weight:800; color:#FDE68A; margin-bottom:0.8rem;">
          <span>🕉️</span> 108 पावन मनका साधना
        </div>

        <!-- Mantra Selector -->
        <div style="margin-bottom:1rem;">
          <label style="font-size:0.8rem; color:#FBCFE8; display:block; margin-bottom:4px;">पावन महामंत्र चुनें:</label>
          <select id="japa-mantra-select" onchange="changeJapaMantra(this.value)" style="background:rgba(30,10,55,0.9); color:#FDE68A; border:1.5px solid rgba(248,200,59,0.4); border-radius:14px; padding:8px 16px; font-size:0.92rem; font-weight:700; width:100%; max-width:320px; outline:none; text-align:center;">
            <option value="हरे कृष्ण हरे कृष्ण कृष्ण कृष्ण हरे हरे । हरे राम हरे राम राम राम हरे हरे ॥">हरे कृष्ण महामंत्र</option>
            <option value="॥ ॐ नमः शिवाय ॥">ॐ नमः शिवाय</option>
            <option value="॥ श्री राम जय राम जय जय राम ॥">श्री राम जय राम जय जय राम</option>
            <option value="॥ ॐ गं गणपतये नमः ॥">ॐ गं गणपतये नमः</option>
            <option value="॥ ॐ नमो भगवते वासुदेवाय ॥">ॐ नमो भगवते वासुदेवाय</option>
            <option value="॥ ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात् ॥">गायत्री महामंत्र</option>
            <option value="॥ ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम् उर्वारुकमिव बन्धनान्मृत्योर्मुक्षीय माऽमृतात् ॥">महामृत्युंजय मंत्र</option>
          </select>
        </div>

        <div id="japa-mantra-text" style="font-size:1.1rem; font-weight:800; color:#FFFDF8; min-height:2.6rem; display:flex; align-items:center; justify-content:center; text-shadow:0 0 15px rgba(248,200,59,0.3); margin-bottom:0.5rem;">
          हरे कृष्ण हरे कृष्ण कृष्ण कृष्ण हरे हरे । हरे राम हरे राम राम राम हरे हरे ॥
        </div>

        <!-- Circular 108 Progress Counter -->
        <div class="mala-ring-container" onclick="incrementJapaMala()">
          <svg class="mala-bead-svg" viewBox="0 0 240 240">
            <defs>
              <linearGradient id="goldGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#FDE68A" />
                <stop offset="50%" stop-color="#F8C83B" />
                <stop offset="100%" stop-color="#D97706" />
              </linearGradient>
            </defs>
            <circle class="mala-bead-circle-bg" cx="120" cy="120" r="105"></circle>
            <circle class="mala-bead-circle-prog" id="mala-circle-bar" cx="120" cy="120" r="105"></circle>
          </svg>
          <div class="mala-center-count">
            <div class="mala-num" id="mala-count-display">0</div>
            <div class="mala-target">/ 108 मनके</div>
          </div>
        </div>

        <!-- Mala Count & Completed Malas -->
        <div style="display:flex; justify-content:center; gap:16px; margin-bottom:1.2rem;">
          <div style="background:rgba(248,200,59,0.12); border:1px solid rgba(248,200,59,0.3); border-radius:14px; padding:6px 16px;">
            <span style="font-size:0.75rem; color:#FDE68A;">पूर्ण मालाएं: </span>
            <strong id="mala-completed-total" style="font-size:1.1rem; color:#FFFDF8;">0</strong>
          </div>
          <div style="background:rgba(236,72,153,0.15); border:1px solid rgba(236,72,153,0.3); border-radius:14px; padding:6px 16px;">
            <span style="font-size:0.75rem; color:#FBCFE8;">कुल जाप: </span>
            <strong id="mala-total-chants" style="font-size:1.1rem; color:#FFFDF8;">0</strong>
          </div>
        </div>

        <!-- Chanting Tap Button -->
        <button onclick="incrementJapaMala()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-weight:900; font-size:1.15rem; padding:16px 42px; border-radius:30px; border:none; cursor:pointer; box-shadow:0 6px 24px rgba(248,200,59,0.5); width:100%; max-width:320px; transition:transform 0.1s ease;" onmousedown="this.style.transform='scale(0.96)'" onmouseup="this.style.transform='scale(1)'">
          📿 जाप करें (Tap to Chant)
        </button>
      </div>
      <div style="height:6rem"></div>
    </section>

    <!-- 🪔 VIRTUAL AARTI & TEMPLE DARSHAN STAGE 🪔 -->
    <section id="page-aarti-stage" class="page">
      <div class="page-header-bar">
        <button class="back-btn" onclick="showPage('page-home')">←</button>
        <h2>🪔 दिव्य आरती व मंदिर दर्शन</h2>
        <button class="katha-search-btn" onclick="triggerFlowerShower()">🌸</button>
      </div>

      <div style="background:linear-gradient(135deg, #1A0730 0%, #350E4F 50%, #120324 100%); border-radius:24px; padding:1.5rem 1.2rem; margin-bottom:1.2rem; border:1.5px solid rgba(248,200,59,0.4); text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.6); position:relative; overflow:hidden;">
        <div style="display:inline-flex; align-items:center; gap:6px; background:rgba(248,200,59,0.18); border:1px solid rgba(248,200,59,0.4); padding:4px 14px; border-radius:20px; font-size:0.8rem; font-weight:800; color:#FDE68A; margin-bottom:0.8rem;">
          <span>🪔</span> अखंड पावन आरती दर्शन
        </div>

        <h3 style="color:#FFFDF8; font-size:1.3rem; margin-bottom:0.4rem;">॥ जय अम्बे गौरी मैया जय श्यामा गौरी ॥</h3>
        <p style="color:#FDE68A; font-size:0.84rem; margin-bottom:1.2rem;">घंटी, शंख एवं दीप प्रज्वलित कर प्रभु के चरणों में दीपदान करें</p>

        <!-- Interactive Diya & Thali Stage -->
        <div style="position:relative; width:220px; height:220px; margin:0 auto 1.4rem; display:flex; align-items:center; justify-content:center;">
          <div style="width:200px; height:200px; border-radius:50%; background:radial-gradient(circle, #F8C83B 0%, #D97706 60%, #78350F 100%); border:4px solid #FFFDF8; box-shadow:0 0 40px rgba(248,200,59,0.6); display:flex; align-items:center; justify-content:center; animation:spinDisc 30s linear infinite;">
            <div style="font-size:3.5rem;">🪔</div>
          </div>
        </div>

        <!-- Interactive Temple Instruments -->
        <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap; margin-bottom:1.4rem;">
          <button onclick="ringTempleBell()" style="background:rgba(248,200,59,0.18); border:1.5px solid #F8C83B; color:#FDE68A; font-weight:800; font-size:0.88rem; padding:10px 18px; border-radius:20px; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
            <span>🔔</span> घंटी बजाएं
          </button>
          <button onclick="blowTempleConch()" style="background:rgba(236,72,153,0.18); border:1.5px solid #F472B6; color:#FBCFE8; font-weight:800; font-size:0.88rem; padding:10px 18px; border-radius:20px; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
            <span>🐚</span> शंख ध्वनि
          </button>
          <button onclick="triggerFlowerShower()" style="background:rgba(16,185,129,0.18); border:1.5px solid #34D399; color:#A7F3D0; font-weight:800; font-size:0.88rem; padding:10px 18px; border-radius:20px; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
            <span>🌸</span> पुष्प वर्षा
          </button>
        </div>

        <!-- Direct Play Aarti Button -->
        <button onclick="playRandomAudioItem()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-weight:900; font-size:1rem; padding:12px 30px; border-radius:24px; border:none; cursor:pointer; box-shadow:0 4px 20px rgba(248,200,59,0.4); display:inline-flex; align-items:center; gap:8px;">
          <span>▶</span> पावन महाआरती सुनें
        </button>
      </div>
      <div style="height:6rem"></div>
    </section>
"""

if 'id="page-mala"' not in html:
    html = html.replace('</main>', japa_mala_page_html + '\n  </main>')
    print("✓ Added Interactive Japa Mala and Virtual Aarti pages to index.html")

# Add Floating Mini Player Dock before </body>
mini_player_html = """
  <!-- 🎧 PERSISTENT FLOATING GLASS MINI-PLAYER DOCK 🎧 -->
  <div id="floating-mini-player" style="display:none;">
    <div class="mini-track-info" onclick="openGlassPlayer()">
      <img src="assets/app_logo_circle.png" class="mini-disc-art" id="mini-player-img" alt="Track Art">
      <div class="mini-text-box">
        <div class="mini-track-title" id="mini-player-title">भक्ति अमृत वाणी</div>
        <div class="mini-track-deity" id="mini-player-deity">
          <div class="live-eq-bars">
            <span></span><span></span><span></span><span></span>
          </div>
          <span id="mini-player-deity-name">दिव्य संकीर्तन</span>
        </div>
      </div>
    </div>
    <div style="display:flex; align-items:center; gap:10px;">
      <button onclick="prevTrack()" style="background:none; border:none; color:#FDE68A; font-size:1.3rem; cursor:pointer;">⏮</button>
      <button id="mini-player-play-btn" onclick="toggleGlobalAudioPlay()" style="background:linear-gradient(135deg,#F8C83B,#D97706); color:#1A0B2E; width:38px; height:38px; border-radius:50%; border:none; font-size:1rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 2px 10px rgba(248,200,59,0.4);">▶</button>
      <button onclick="nextTrack()" style="background:none; border:none; color:#FDE68A; font-size:1.3rem; cursor:pointer;">⏭</button>
    </div>
  </div>
"""

if 'id="floating-mini-player"' not in html:
    html = html.replace('</body>', mini_player_html + '\n</body>')
    print("✓ Injected Floating Glass Mini-Player Dock into index.html")

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# ==============================================================================
# 3. ENHANCE app.js WITH JAPA MALA, AARTI STAGE, MINI PLAYER LOGIC
# ==============================================================================
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js_content = f.read()

japa_mala_and_mini_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 📿 DIGITAL JAPA MALA & INTERACTIVE SPIRITUAL UTILITIES
// ══════════════════════════════════════════════════════════════════════════════

let japaMalaState = {
  currentCount: 0,
  completedMalas: 0,
  totalChants: 0,
  target: 108
};

function incrementJapaMala() {
  japaMalaState.currentCount++;
  japaMalaState.totalChants++;

  if (japaMalaState.currentCount >= japaMalaState.target) {
    japaMalaState.currentCount = 0;
    japaMalaState.completedMalas++;
    if (typeof showToast === 'function') {
      showToast("🎉 पावन 108 जाप की 1 माला पूर्ण हुई! प्रभु की असीम कृपा बनी रहे।");
    }
    triggerFlowerShower();
  }

  updateJapaMalaUI();

  // Haptic feedback if supported on mobile
  if (navigator.vibrate) {
    navigator.vibrate(25);
  }
}

function updateJapaMalaUI() {
  const display = document.getElementById('mala-count-display');
  if (display) display.textContent = japaMalaState.currentCount;

  const malasTotal = document.getElementById('mala-completed-total');
  if (malasTotal) malasTotal.textContent = japaMalaState.completedMalas;

  const totalDisplay = document.getElementById('mala-total-chants');
  if (totalDisplay) totalDisplay.textContent = japaMalaState.totalChants;

  const circleBar = document.getElementById('mala-circle-bar');
  if (circleBar) {
    const totalLength = 660; // 2 * PI * 105
    const progress = japaMalaState.currentCount / japaMalaState.target;
    const offset = totalLength - (progress * totalLength);
    circleBar.style.strokeDashoffset = offset;
  }
}

function resetJapaMala() {
  japaMalaState.currentCount = 0;
  updateJapaMalaUI();
  if (typeof showToast === 'function') showToast("🔄 जाप माला 0 पर रीसेट हुई");
}

function changeJapaMantra(mantra) {
  const mantraBox = document.getElementById('japa-mantra-text');
  if (mantraBox) mantraBox.textContent = mantra;
  if (typeof showToast === 'function') showToast("✨ पावन महामंत्र चयनित");
}

// 🪔 VIRTUAL AARTI INSTRUMENTS & FLOWER SHOWER
function ringTempleBell() {
  try {
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(880, audioCtx.currentTime); // High Bell Note A5
    osc.frequency.exponentialRampToValueAtTime(440, audioCtx.currentTime + 1.2);
    gain.gain.setValueAtTime(0.35, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 1.2);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 1.2);
  } catch (e) {
    console.log("AudioContext bell chime triggered");
  }
  if (typeof showToast === 'function') showToast("🔔 ॥ पावन घंटा नाद ॥");
}

function blowTempleConch() {
  try {
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(220, audioCtx.currentTime);
    osc.frequency.linearRampToValueAtTime(293.66, audioCtx.currentTime + 0.8);
    osc.frequency.linearRampToValueAtTime(220, audioCtx.currentTime + 2.0);
    gain.gain.setValueAtTime(0.4, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 2.0);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 2.0);
  } catch (e) {
    console.log("AudioContext conch triggered");
  }
  if (typeof showToast === 'function') showToast("🐚 ॥ पावन शंख ध्वनि ॥");
}

function triggerFlowerShower() {
  const petals = ['🌸', '🌺', '🌼', '🌹', '✨'];
  for (let i = 0; i < 24; i++) {
    const el = document.createElement('div');
    el.textContent = petals[Math.floor(Math.random() * petals.length)];
    el.style.cssText = `
      position: fixed;
      top: -20px;
      left: ${Math.random() * 100}vw;
      font-size: ${18 + Math.random() * 18}px;
      z-index: 99999;
      pointer-events: none;
      animation: fallDownPetal ${2 + Math.random() * 2.5}s ease-in forwards;
    `;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 4500);
  }
}

// Add animation to document
if (!document.getElementById('petal-anim-style')) {
  const style = document.createElement('style');
  style.id = 'petal-anim-style';
  style.textContent = `
    @keyframes fallDownPetal {
      0% { transform: translateY(0) rotate(0deg); opacity: 1; }
      100% { transform: translateY(105vh) rotate(360deg); opacity: 0; }
    }
  `;
  document.head.appendChild(style);
}

// 🎧 MINI PLAYER DOCK INTEGRATION
function updateMiniPlayerDock(record, isPlaying) {
  const dock = document.getElementById('floating-mini-player');
  if (!dock) return;

  if (record) {
    dock.style.display = 'flex';
    const titleEl = document.getElementById('mini-player-title');
    if (titleEl) titleEl.textContent = record.title || 'भक्ति अमृत वाणी';

    const deityEl = document.getElementById('mini-player-deity-name');
    if (deityEl) deityEl.textContent = record.deity_name_hi || record.deity_id || 'पावन संकीर्तन';

    const playBtn = document.getElementById('mini-player-play-btn');
    if (playBtn) playBtn.textContent = isPlaying ? '⏸' : '▶';
  }
}

function toggleGlobalAudioPlay() {
  if (window.MediaRouter.activeMode === 'local' && window.coreAudioElement) {
    if (window.coreAudioElement.paused) {
      window.coreAudioElement.play();
      updateMiniPlayerDock(window.activeAudioRecord, true);
    } else {
      window.coreAudioElement.pause();
      updateMiniPlayerDock(window.activeAudioRecord, false);
    }
  } else {
    openGlassPlayer();
  }
}
"""

if "DIGITAL JAPA MALA & INTERACTIVE SPIRITUAL UTILITIES" not in js_content:
    with open(app_js_path, 'a', encoding='utf-8') as f:
        f.write("\n" + japa_mala_and_mini_js)
    print("✓ Injected Digital Japa Mala, Aarti Stage & Mini-Player logic into app.js")

# Patch MediaRouter.playRecord in app.js to call updateMiniPlayerDock
old_mr_play = "if (typeof updateAllPlayButtons === 'function') updateAllPlayButtons(true);"
new_mr_play = """if (typeof updateAllPlayButtons === 'function') updateAllPlayButtons(true);
        window.activeAudioRecord = record;
        if (typeof updateMiniPlayerDock === 'function') updateMiniPlayerDock(record, true);"""

if old_mr_play in js_content and "window.activeAudioRecord = record;" not in js_content:
    js_content = js_content.replace(old_mr_play, new_mr_play)
    with open(app_js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("✓ Linked MediaRouter to updateMiniPlayerDock")

print("=" * 80)
print("NEXT-GEN UI/UX MODERNIZATION COMPLETE")
print("=" * 80)
