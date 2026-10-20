import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
INDEX_FILE = os.path.join(BASE_DIR, "index.html")
ENGINE_FILE = os.path.join(BASE_DIR, "epic_games_engine.js")
CSS_FILE = os.path.join(BASE_DIR, "epic_games.css")

print("=== STEP 1: Updating index.html ===")
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the desktop accessibility buttons circled in blue
# Find and remove:
# <div style="display:flex; gap:16px; margin-bottom:4px; z-index:10;">
#   <button id="swipe-btn-left" ...
#   <button id="swipe-btn-right" ...
# </div>
btn_block_regex = re.compile(
    r'<div style="display:flex;\s*gap:16px;\s*margin-bottom:4px;\s*z-index:10;">\s*'
    r'<button id="swipe-btn-left"[\s\S]*?</button>\s*'
    r'<button id="swipe-btn-right"[\s\S]*?</button>\s*'
    r'</div>',
    re.MULTILINE
)

if btn_block_regex.search(html):
    html = btn_block_regex.sub('', html, count=1)
    print("✓ Removed accessibility buttons from index.html")
else:
    print("⚠ Regex for accessibility buttons not matched, searching fallback...")
    # fallback string search
    btn_marker = '<button id="swipe-btn-left"'
    idx_btn = html.find(btn_marker)
    if idx_btn != -1:
        idx_div_start = html.rfind('<div', 0, idx_btn)
        idx_div_end = html.find('</div>', idx_btn)
        if idx_div_start != -1 and idx_div_end != -1:
            html = html[:idx_div_start] + html[idx_div_end + 6:]
            print("✓ Removed accessibility buttons via fallback")

# 2. Update the two portals markup with Image 4 (Left Sun Portal) & Image 3 (Right Demon Portal)
old_portals_regex = re.compile(
    r'<!-- Two Bottom Shrines/Portals -->[\s\S]*?<div class="swipe-portals-container">[\s\S]*?</div>\s*</div>\s*<!-- ══════════ 📜 CHARACTER REVIEW ARENA',
    re.MULTILINE
)

new_portals_html = """<!-- Two Bottom Shrines/Portals (Left Sun Portal & Right Demon Portal) -->
      <div class="swipe-portals-container">
        <!-- Left Portal (Sun Portal - Image 4) -->
        <div class="swipe-portal-shrine" id="swipe-portal-left" onclick="swipeCardManual('left')">
          <div class="swipe-portal-img-wrap">
            <img src="assets/games/portal_left_sun.png" alt="द्वार" class="swipe-portal-bg" id="swipe-gate-left" onerror="this.src='assets/games/portal_ayodhya.jpg';">
            <div class="swipe-portal-score-badge score-ayodhya" id="swipe-left-score">0</div>
            <div class="swipe-portal-label" id="swipe-left-portal-label">अयोध्या</div>
          </div>
        </div>

        <!-- Right Portal (Demon Portal - Image 3) -->
        <div class="swipe-portal-shrine" id="swipe-portal-right" onclick="swipeCardManual('right')">
          <div class="swipe-portal-img-wrap">
            <img src="assets/games/portal_right_demon.png" alt="द्वार" class="swipe-portal-bg" id="swipe-gate-right" onerror="this.src='assets/games/portal_mithila.jpg';">
            <div class="swipe-portal-score-badge score-mithila" id="swipe-right-score">0</div>
            <div class="swipe-portal-label" id="swipe-right-portal-label">मिथिला</div>
          </div>
        </div>
      </div>
    </div>

    <!-- ══════════ 📜 CHARACTER REVIEW ARENA"""

if old_portals_regex.search(html):
    html = old_portals_regex.sub(new_portals_html, html, count=1)
    print("✓ Updated portals markup with Image 4 & Image 3 in index.html")
else:
    print("⚠ Regex for portals not matched, checking fallback...")
    idx_p = html.find('class="swipe-portals-container"')
    if idx_p != -1:
        idx_p_start = html.rfind('<!-- Two Bottom Shrines/Portals', 0, idx_p)
        idx_rev = html.find('<!-- ══════════ 📜 CHARACTER REVIEW ARENA', idx_p)
        if idx_p_start != -1 and idx_rev != -1:
            html = html[:idx_p_start] + new_portals_html + html[idx_rev + len('<!-- ══════════ 📜 CHARACTER REVIEW ARENA'):]
            print("✓ Updated portals markup via fallback")

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html)
print("✓ Saved index.html successfully")

print("\n=== STEP 2: Updating epic_games_engine.js ===")
with open(ENGINE_FILE, "r", encoding="utf-8") as f:
    engine = f.read()

# Update renderCurrentCard in epic_games_engine.js to use Image 2 (Winged Gold Frame with Sapphires)
old_card_deck_regex = re.compile(
    r'stage\.innerHTML = `[\s\S]*?<div class="swipe-main-card" id="swipe-active-card">[\s\S]*?</div>\s*`;',
    re.MULTILINE
)

new_card_deck_js = """stage.innerHTML = `
      <div class="swipe-card-underlay swipe-card-underlay-2"></div>
      <div class="swipe-card-underlay swipe-card-underlay-1"></div>
      
      <div class="swipe-main-card" id="swipe-active-card">
        <div class="swipe-char-portrait-container">
          <img src="${char.image}" alt="${charName}" class="swipe-char-portrait" onerror="this.src='assets/games/char_sunaina.jpg';">
        </div>
        <img src="assets/games/card_gold_winged_frame.png" alt="Frame" class="swipe-card-winged-overlay">
        <div class="swipe-char-name-bar">${charName}</div>
      </div>
    `;"""

if old_card_deck_regex.search(engine):
    engine = old_card_deck_regex.sub(new_card_deck_js, engine, count=1)
    print("✓ Updated renderCurrentCard with Image 2 Winged Gold Frame in epic_games_engine.js")
else:
    print("⚠ Could not match old card deck HTML in epic_games_engine.js")

# Update gate default image paths in initSwipeGame
engine = engine.replace(
    "leftGateImg.src = cat.leftSide.gateAsset;",
    "leftGateImg.src = 'assets/games/portal_left_sun.png';"
)
engine = engine.replace(
    "rightGateImg.src = cat.rightSide.gateAsset;",
    "rightGateImg.src = 'assets/games/portal_right_demon.png';"
)

with open(ENGINE_FILE, "w", encoding="utf-8") as f:
    f.write(engine)
print("✓ Saved epic_games_engine.js successfully")

print("\n=== STEP 3: Updating epic_games.css ===")
with open(CSS_FILE, "r", encoding="utf-8") as f:
    css = f.read()

# Update swipe-game-arena background to swipe_arena_bg.jpg (Image 5)
css = re.sub(
    r'\.swipe-game-arena\s*\{[\s\S]*?background:[\s\S]*?;',
    """.swipe-game-arena {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  z-index: 30000;
  display: none;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  background: #2D1400 url('assets/games/swipe_arena_bg.jpg') no-repeat center center;
  background-size: cover;""",
    css,
    count=1
)

# Append new styles for Image 2 (Winged Gold Frame) and Image 4/3 Portals
new_arena_custom_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   SWIPE ARENA UPGRADE: Image 5 (Background), Image 2 (Frame), Image 4 & 3 (Portals)
   ══════════════════════════════════════════════════════════════════════════════ */
.swipe-game-arena {
  background: #2D1400 url('assets/games/swipe_arena_bg.jpg') no-repeat center center !important;
  background-size: cover !important;
  padding: env(safe-area-inset-top, 6px) 10px env(safe-area-inset-bottom, 12px) 10px !important;
}

.swipe-card-deck-stage {
  position: relative;
  width: 275px;
  height: 368px;
  perspective: 1000px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  z-index: 5;
}

.swipe-main-card {
  position: relative;
  width: 275px;
  height: 368px;
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
  border-radius: 20px;
  cursor: grab;
  touch-action: none;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 3;
}

/* Character Portrait inside Image 2 Frame Window */
.swipe-char-portrait-container {
  position: absolute;
  top: 13.5%;
  left: 16.2%;
  width: 67.6%;
  height: 70%;
  overflow: hidden;
  border-radius: 8px;
  z-index: 1;
  background: #1A0B2E;
}

.swipe-char-portrait {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 15%;
  display: block;
}

/* Golden Winged Sapphire Frame Overlay (Image 2) */
.swipe-card-winged-overlay {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: fill;
  pointer-events: none;
  z-index: 3;
  filter: drop-shadow(0 8px 20px rgba(0, 0, 0, 0.5));
}

/* Character Name Bar Overlay */
.swipe-char-name-bar {
  position: absolute;
  bottom: 17%;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(180deg, rgba(255, 253, 248, 0.96) 0%, rgba(247, 235, 210, 0.96) 100%);
  border: 1.8px solid #D4AF37;
  padding: 3px 20px;
  border-radius: 9999px;
  font-family: 'Rozha One', 'Cinzel', system-ui;
  font-size: 1.05rem;
  font-weight: 900;
  color: #2D1400;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
  z-index: 5;
  white-space: nowrap;
  letter-spacing: 0.3px;
  text-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);
}

/* Stack Underlay Cards */
.swipe-card-underlay {
  position: absolute;
  width: 250px;
  height: 335px;
  background: rgba(200, 157, 60, 0.2);
  border: 2px solid rgba(212, 175, 55, 0.4);
  border-radius: 20px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.3);
  pointer-events: none;
}

/* Bottom Portals: Left Sun (Image 4) & Right Demon (Image 3) */
.swipe-portals-container {
  width: 100%;
  max-width: 440px;
  display: flex;
  align-items: flex-end;
  justify-content: space-around;
  padding: 0 8px 12px !important;
  z-index: 10;
  box-sizing: border-box;
}

.swipe-portal-shrine {
  width: 145px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  cursor: pointer;
  transition: transform 0.22s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.22s ease;
}

.swipe-portal-shrine:active {
  transform: scale(0.95);
}

.swipe-portal-img-wrap {
  width: 145px !important;
  height: 195px !important;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.swipe-portal-bg {
  width: 100% !important;
  height: 100% !important;
  object-fit: contain !important;
  filter: drop-shadow(0 8px 18px rgba(0, 0, 0, 0.45));
}

/* Portal Live Score Badge (Centered in the Orb of Image 4 & Image 3) */
.swipe-portal-score-badge {
  position: absolute;
  top: 57.5% !important;
  left: 50% !important;
  transform: translate(-50%, -50%) !important;
  width: 36px !important;
  height: 36px !important;
  border-radius: 50% !important;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Cinzel', system-ui;
  font-weight: 900;
  font-size: 1.2rem;
  color: #FFFFFF;
  border: 2px solid #FDE047 !important;
  box-shadow: 0 0 14px rgba(253, 224, 71, 0.7), inset 0 2px 4px rgba(255, 255, 255, 0.5);
  z-index: 5;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
}

.score-ayodhya {
  background: radial-gradient(circle, #8B5CF6 0%, #6D28D9 60%, #4C1D95 100%) !important;
}

.score-mithila {
  background: radial-gradient(circle, #EF4444 0%, #DC2626 60%, #991B1B 100%) !important;
}

/* Portal Name Label (Centered in the bottom banner of Image 4 & Image 3) */
.swipe-portal-label {
  position: absolute;
  top: 74% !important;
  left: 50% !important;
  transform: translate(-50%, -50%) !important;
  width: 78% !important;
  text-align: center;
  font-family: 'Cinzel', 'Georgia', serif;
  font-size: 0.88rem;
  font-weight: 900;
  color: #381E0D !important;
  letter-spacing: 0.5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-shadow: 0 1px 1px rgba(255, 255, 255, 0.9);
  z-index: 5;
  pointer-events: none;
  margin-top: 0 !important;
}

/* Drag Pulse on Portal */
.swipe-portal-shrine.portal-pulse-active {
  transform: scale(1.1) !important;
  filter: drop-shadow(0 0 22px rgba(245, 158, 11, 0.95)) brightness(1.2) !important;
}

@media (max-height: 720px) {
  .swipe-card-deck-stage { width: 245px; height: 328px; }
  .swipe-main-card { width: 245px; height: 328px; }
  .swipe-card-underlay { width: 230px; height: 308px; }
  .swipe-portal-shrine { width: 125px; }
  .swipe-portal-img-wrap { width: 125px !important; height: 168px !important; }
  .swipe-portal-score-badge { width: 30px !important; height: 30px !important; font-size: 1rem !important; }
  .swipe-portal-label { font-size: 0.78rem !important; }
}
"""

css += "\n" + new_arena_custom_css
with open(CSS_FILE, "w", encoding="utf-8") as f:
    f.write(css)
print("✓ Appended new arena styles to epic_games.css successfully.")

print("\n=== Upgrades to index.html, epic_games_engine.js, and epic_games.css Complete! ===")
