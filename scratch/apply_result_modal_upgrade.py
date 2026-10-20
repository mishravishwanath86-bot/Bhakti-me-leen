import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
INDEX_FILE = os.path.join(BASE_DIR, "index.html")
ENGINE_FILE = os.path.join(BASE_DIR, "epic_games_engine.js")
CSS_FILE = os.path.join(BASE_DIR, "epic_games.css")

print("=== 1. Updating swipe-result-modal in index.html ===")
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html = f.read()

old_modal_regex = re.compile(
    r'<div id="swipe-result-modal" class="swipe-result-modal-overlay">[\s\S]*?</div>\s*</div>\s*<!-- ══════════ 🏹 SWIPE CATEGORY SELECTOR MODAL',
    re.MULTILINE
)

new_modal_html = """<div id="swipe-result-modal" class="swipe-result-modal-overlay">
      <div class="swipe-result-box">
        <!-- Image 2 Ornate Winged Frame Base -->
        <img src="assets/games/modal_result_frame.png" alt="Result Frame Base" class="swipe-result-frame-img">

        <!-- Top Red Ribbon Dynamic Header -->
        <div class="swipe-result-ribbon-wrapper">
          <div class="swipe-result-ribbon-dynamic" id="swipe-result-ribbon-text">बधाई हो!</div>
        </div>

        <!-- Center Parchment Content Area -->
        <div class="swipe-result-parchment-content">
          <!-- Big Coin / Star Icon Badge -->
          <div class="swipe-result-star-coin-badge">
            <span class="star-coin-icon">🪙</span>
            <div class="star-coin-label">अर्जित सिक्के</div>
            <div class="star-coin-val" id="swipe-result-coins-earned">+500</div>
          </div>

          <!-- Victory / Result Heading -->
          <div class="swipe-result-heading" id="swipe-result-heading">अद्भुत ज्ञान!</div>

          <!-- Score Summary Line -->
          <div class="swipe-result-score-text" id="swipe-result-score-text">आपने पूरे किए 10/12 पात्र</div>

          <!-- Stat Cards Row (Image 1 Style) -->
          <div class="swipe-result-stats-row">
            <div class="result-stat-chip">
              <span class="stat-chip-icon">⏱️</span>
              <div class="stat-chip-meta">
                <span class="stat-chip-label">समय</span>
                <span class="stat-chip-val" id="swipe-result-time-val">00:38</span>
              </div>
            </div>
            <div class="result-stat-chip">
              <span class="stat-chip-icon">🪙</span>
              <div class="stat-chip-meta">
                <span class="stat-chip-label">स्कोर</span>
                <span class="stat-chip-val" id="swipe-result-streak-count">10</span>
              </div>
            </div>
            <div class="result-stat-chip">
              <span class="stat-chip-icon">🎴</span>
              <div class="stat-chip-meta">
                <span class="stat-chip-label">पात्र</span>
                <span class="stat-chip-val" id="swipe-result-total-val">10/12</span>
              </div>
            </div>
          </div>

          <!-- Motivational Message -->
          <div class="swipe-result-message" id="swipe-result-message">आपने सभी पात्रों को उनके सही पक्ष में पहुँचाया।</div>
        </div>

        <!-- Bottom Built-in Pill Buttons (Fitted on Image 2's blue & gold button slots) -->
        <div class="swipe-result-pill-actions">
          <!-- Left Blue Pill Button: New Game -->
          <button class="result-pill-btn pill-btn-blue" onclick="newSwipeGame()" title="New Game">
            <span class="pill-btn-icon">▶</span>
            <span class="pill-btn-text" id="swipe-res-btn-new">नया खेल</span>
          </button>

          <!-- Right Gold Pill Button: Learn Lore / Review -->
          <button class="result-pill-btn pill-btn-gold" onclick="showCharacterReviewScreen(); hideSwipeResultModal();" title="Learn Lore">
            <span class="pill-btn-icon">📖</span>
            <span class="pill-btn-text" id="swipe-res-btn-lore">जानें</span>
          </button>
        </div>

        <!-- Footer Actions: Retry & Back to Home -->
        <div class="swipe-result-footer-row">
          <button class="swipe-result-retry-btn" onclick="retrySwipeRound()">
            <span>🔄</span> <span id="swipe-res-btn-retry">दोबारा</span>
          </button>
          <a class="swipe-result-home-link" onclick="hideSwipeResultModal(); closeSwipeGame(); showPage('page-epic-games');">होम पर वापस जाएँ</a>
        </div>
      </div>
    </div>

    <!-- ══════════ 🏹 SWIPE CATEGORY SELECTOR MODAL"""

if old_modal_regex.search(html):
    html = old_modal_regex.sub(new_modal_html, html, count=1)
    print("✓ Successfully replaced swipe-result-modal with Image 2 base in index.html")
else:
    print("⚠ Regex for swipe-result-modal not matched, using fallback...")
    idx_m = html.find('id="swipe-result-modal"')
    if idx_m != -1:
        idx_start = html.rfind('<div id="swipe-result-modal"', 0, idx_m + 30)
        idx_end = html.find('<!-- ══════════ 🏹 SWIPE CATEGORY SELECTOR MODAL', idx_start)
        if idx_start != -1 and idx_end != -1:
            html = html[:idx_start] + new_modal_html + html[idx_end + len('<!-- ══════════ 🏹 SWIPE CATEGORY SELECTOR MODAL'):]
            print("✓ Replaced swipe-result-modal via fallback in index.html")

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html)
print("✓ Saved index.html")

print("\n=== 2. Updating showSwipeResultModal in epic_games_engine.js ===")
with open(ENGINE_FILE, "r", encoding="utf-8") as f:
    engine = f.read()

old_show_modal_regex = re.compile(
    r'function showSwipeResultModal\(\)\s*\{[\s\S]*?modal\.style\.display = \'flex\';\s*\}',
    re.MULTILINE
)

new_show_modal_js = """function showSwipeResultModal() {
    hideBottomNavForGames();
    var modal = document.getElementById('swipe-result-modal');
    if (!modal) return;

    var total = epicGameState.deck.length;
    var correct = epicGameState.correctCount;
    var isVictory = correct >= Math.floor(total * 0.7);

    if (isVictory) playSound('victory');

    var lang = epicGameState.currentLanguage || 'en';

    // Dynamic Ribbon text
    var ribbonText = isVictory ? (lang === 'te' ? 'విజయవంతమైనది!' : (lang === 'en' ? 'VICTORY!' : 'बधाई हो!')) : 'TRY AGAIN';
    var ribbonEl = document.getElementById('swipe-result-ribbon-text');
    if (ribbonEl) ribbonEl.textContent = ribbonText;

    // Coins Earned
    var coinsEarnedEl = document.getElementById('swipe-result-coins-earned');
    if (coinsEarnedEl) coinsEarnedEl.textContent = `+${correct * 50}`;

    // Heading
    var headEl = document.getElementById('swipe-result-heading');
    if (headEl) headEl.textContent = isVictory ? 
      (lang === 'te' ? 'అద్భుతమైన జ్ఞానం!' : (lang === 'en' ? 'Brilliant Knowledge!' : 'अद्भुत ज्ञान!')) : 
      (lang === 'te' ? 'మంచి ప్రయత్నం!' : (lang === 'en' ? 'Good Effort!' : 'बढ़िया प्रयास!'));

    // Score text
    var scoreTextEl = document.getElementById('swipe-result-score-text');
    if (scoreTextEl) scoreTextEl.textContent = (lang === 'te') ? 
      `మీరు ${correct}/${total} పాత్రలను పూర్తి చేసారు` : 
      ((lang === 'en') ? `Completed ${correct}/${total} characters` : `आपने पूरे किए ${correct}/${total} पात्र`);

    // Stat chips
    var streakEl = document.getElementById('swipe-result-streak-count');
    if (streakEl) streakEl.textContent = correct * 50;

    var totalEl = document.getElementById('swipe-result-total-val');
    if (totalEl) totalEl.textContent = `${correct}/${total}`;

    // Motivational Message
    var msgEl = document.getElementById('swipe-result-message');
    if (msgEl) msgEl.textContent = isVictory ? 
      (lang === 'te' ? 'మీరు అన్ని పాత్రలను సరైన వైపు చేర్చారు.' : (lang === 'en' ? 'You guided all characters to their true side!' : 'आपने सभी पात्रों को उनके सही पक्ष में पहुँचाया।')) : 
      (lang === 'te' ? 'కొన్ని पात्रలకి మరో ప్రయత్నం అవసరం.' : (lang === 'en' ? 'Some characters need another try.' : 'कुछ पात्रों को एक और कोशिश चाहिए।'));

    // Buttons Multilingual Text
    var btnNew = document.getElementById('swipe-res-btn-new');
    if (btnNew) btnNew.textContent = (lang === 'te') ? 'కొత్త ఆట' : ((lang === 'en') ? 'Play Again' : 'नया खेल');

    var btnLore = document.getElementById('swipe-res-btn-lore');
    if (btnLore) btnLore.textContent = (lang === 'te') ? 'తెలుసుకోండి' : ((lang === 'en') ? 'Learn Lore' : 'जानें');

    var btnRetry = document.getElementById('swipe-res-btn-retry');
    if (btnRetry) btnRetry.textContent = (lang === 'te') ? 'మళ్లీ' : ((lang === 'en') ? 'Retry' : 'दोबारा');

    modal.style.display = 'flex';
  }"""

if old_show_modal_regex.search(engine):
    engine = old_show_modal_regex.sub(new_show_modal_js, engine, count=1)
    print("✓ Updated showSwipeResultModal in epic_games_engine.js")
else:
    print("⚠ Regex for showSwipeResultModal not matched directly, checking fallback...")
    idx_sm = engine.find("function showSwipeResultModal()")
    if idx_sm != -1:
        idx_end_sm = engine.find("modal.style.display = 'flex';", idx_sm)
        if idx_end_sm != -1:
            idx_close_brace = engine.find("}", idx_end_sm)
            engine = engine[:idx_sm] + new_show_modal_js + engine[idx_close_brace + 1:]
            print("✓ Updated showSwipeResultModal via fallback in epic_games_engine.js")

with open(ENGINE_FILE, "w", encoding="utf-8") as f:
    f.write(engine)
print("✓ Saved epic_games_engine.js")

print("\n=== 3. Updating epic_games.css with Image 2 Modal Frame Styles ===")
with open(CSS_FILE, "r", encoding="utf-8") as f:
    css = f.read()

modal_frame_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   SWIPE RESULT MODAL (Exact Base Image 2: Winged Gold Frame with Blue Sapphires)
   ══════════════════════════════════════════════════════════════════════════════ */
.swipe-result-modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 35000;
  background: rgba(0, 0, 0, 0.78);
  backdrop-filter: blur(8px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 10px;
  box-sizing: border-box;
}

.swipe-result-box {
  position: relative;
  width: min(345px, 92vw) !important;
  aspect-ratio: 571 / 1024 !important;
  height: auto !important;
  max-height: 90vh !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: space-between !important;
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
  animation: resultModalSpring 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) forwards !important;
  user-select: none;
}

@keyframes resultModalSpring {
  0% { transform: scale(0.65); opacity: 0; }
  70% { transform: scale(1.04); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}

.swipe-result-frame-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: fill;
  pointer-events: none;
  z-index: 1;
  filter: drop-shadow(0 16px 36px rgba(0, 0, 0, 0.7));
}

.swipe-result-ribbon-wrapper {
  position: absolute;
  top: 8.8%;
  left: 50%;
  transform: translateX(-50%);
  width: 75%;
  height: 6.8%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 5;
  pointer-events: none;
}

.swipe-result-ribbon-dynamic {
  font-family: 'Cinzel Decorative', 'Cinzel', 'Georgia', serif;
  font-size: clamp(1.2rem, 4.2vw, 1.55rem);
  font-weight: 900;
  letter-spacing: 1px;
  color: #FFFDF0;
  text-transform: uppercase;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8), 0 0 8px rgba(254, 240, 138, 0.6);
  text-align: center;
  white-space: nowrap;
}

.swipe-result-parchment-content {
  position: absolute;
  top: 19%;
  left: 16%;
  width: 68%;
  height: 53%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  z-index: 5;
  padding: 4px 6px;
  box-sizing: border-box;
  text-align: center;
}

.swipe-result-star-coin-badge {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle, #FFFBEB 0%, #FEF3C7 60%, #FDE68A 100%);
  border: 2px solid #D4AF37;
  border-radius: 50%;
  width: 72px;
  height: 72px;
  box-shadow: 0 4px 14px rgba(212, 175, 55, 0.4), inset 0 2px 4px rgba(255, 255, 255, 0.9);
  margin-bottom: 2px;
}

.star-coin-icon {
  font-size: 1.5rem;
  line-height: 1;
}

.star-coin-label {
  font-size: 0.62rem;
  font-weight: 800;
  color: #78350F;
  line-height: 1.1;
}

.star-coin-val {
  font-size: 0.92rem;
  font-weight: 900;
  color: #451A03;
  line-height: 1;
}

.swipe-result-heading {
  font-family: 'Rozha One', 'Cinzel', system-ui;
  font-size: clamp(1.15rem, 3.8vw, 1.4rem);
  font-weight: 900;
  color: #1E3A8A;
  margin: 0;
  line-height: 1.1;
  text-shadow: 0 1px 1px rgba(255,255,255,0.8);
}

.swipe-result-score-text {
  font-size: 0.82rem;
  font-weight: 800;
  color: #5A381E;
  margin: 0;
}

.swipe-result-stats-row {
  display: flex;
  gap: 6px;
  width: 100%;
  justify-content: center;
  margin: 2px 0;
}

.result-stat-chip {
  background: rgba(255, 255, 255, 0.82);
  border: 1.2px solid #D4AF37;
  border-radius: 10px;
  padding: 3px 6px;
  display: flex;
  align-items: center;
  gap: 4px;
  flex: 1;
  justify-content: center;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.stat-chip-icon {
  font-size: 0.85rem;
}

.stat-chip-meta {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}

.stat-chip-label {
  font-size: 0.58rem;
  font-weight: 800;
  color: #78350F;
  line-height: 1;
}

.stat-chip-val {
  font-size: 0.78rem;
  font-weight: 900;
  color: #1E1B18;
  line-height: 1.1;
}

.swipe-result-message {
  font-size: 0.75rem;
  color: #5C4332;
  line-height: 1.2;
  margin: 0;
  padding: 0 4px;
}

.swipe-result-pill-actions {
  position: absolute;
  top: 74.2%;
  left: 14%;
  width: 72%;
  height: 6.8%;
  display: flex;
  gap: 8px;
  justify-content: space-between;
  align-items: center;
  z-index: 6;
}

.result-pill-btn {
  flex: 1;
  height: 100%;
  border-radius: 9999px;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
  transition: transform 0.2s ease, filter 0.2s ease;
  font-weight: 900;
  font-size: 0.88rem;
  box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

.result-pill-btn:active {
  transform: scale(0.94);
}

.pill-btn-blue {
  background: linear-gradient(180deg, #2563EB 0%, #1D4ED8 100%);
  color: #FFFFFF;
  border: 1.5px solid #93C5FD;
  text-shadow: 0 1px 2px rgba(0,0,0,0.5);
}

.pill-btn-gold {
  background: linear-gradient(180deg, #FDE68A 0%, #F59E0B 100%);
  color: #451A03;
  border: 1.5px solid #FEF08A;
  text-shadow: 0 1px 1px rgba(255,255,255,0.7);
}

.swipe-result-footer-row {
  position: absolute;
  bottom: 3.5%;
  left: 50%;
  transform: translateX(-50%);
  width: 85%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  z-index: 6;
}

.swipe-result-retry-btn {
  background: rgba(255, 255, 255, 0.88);
  border: 1.2px solid #D4AF37;
  border-radius: 12px;
  padding: 3px 16px;
  font-size: 0.78rem;
  font-weight: 800;
  color: #451A03;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
  transition: all 0.2s ease;
  box-shadow: 0 2px 6px rgba(0,0,0,0.15);
}

.swipe-result-retry-btn:active {
  transform: scale(0.95);
}

.swipe-result-home-link {
  font-size: 0.74rem;
  font-weight: 800;
  color: #FFFDF0;
  text-decoration: underline;
  cursor: pointer;
  text-shadow: 0 1px 3px rgba(0,0,0,0.85);
}
"""

if ".swipe-result-frame-img" not in css:
    css += "\n" + modal_frame_css
    with open(CSS_FILE, "w", encoding="utf-8") as f:
        f.write(css)
    print("✓ Appended Image 2 Modal Frame styles to epic_games.css")
else:
    print("⚠ Image 2 Modal Frame styles already in epic_games.css")

print("\n=== Upgrade Script Completed Successfully ===")
