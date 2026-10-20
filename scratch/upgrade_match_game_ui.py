import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
INDEX_FILE = os.path.join(BASE_DIR, "index.html")
ENGINE_FILE = os.path.join(BASE_DIR, "epic_games_engine.js")
CSS_FILE = os.path.join(BASE_DIR, "epic_games.css")

print("=== 1. Updating match-level-hub-modal Structure in index.html ===")
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Locate match-level-hub-modal
hub_start = html.find('<!-- ══════════ 🎴 1. BHAKTI CARD MATCH - HOME & LEVEL SELECTION SCREEN')
if hub_start == -1:
    hub_start = html.find('id="match-level-hub-modal"')
    if hub_start != -1:
        hub_start = html.rfind('<div id="match-level-hub-modal"', 0, hub_start + 30)

hub_end = html.find('<!-- ══════════ 🎴 1. BHAKTI CARD MATCH GAMEPLAY ARENA', hub_start)

if hub_start != -1 and hub_end != -1:
    old_hub_html = html[hub_start:hub_end]
    print(f"✓ Found old match-level-hub-modal (length: {len(old_hub_html)})")
else:
    print("⚠ Could not locate exact boundaries of match-level-hub-modal in index.html")
    sys.exit(1)

new_hub_html = """<!-- ══════════ 🎴 1. BHAKTI CARD MATCH - HOME & LEVEL SELECTION SCREEN ══════════ -->
    <div id="match-level-hub-modal" class="epic-game-modal-overlay">
      <!-- Fixed Sticky Header with Safe-Area Notch Padding -->
      <div class="match-hub-header">
        <div class="match-hub-header-left">
          <button class="match-hub-back-btn" onclick="closeMatchLevelHub()" title="वापस जाएँ">←</button>
          <div class="match-hub-title-block">
            <h2 class="match-hub-title">
              <span class="match-hub-icon">🎴</span>
              <span>भक्ति कार्ड मिलान</span>
            </h2>
            <div class="match-hub-subtitle">३० पावन स्तर • १६ पावन भक्ति प्रतीक</div>
          </div>
        </div>
        <div class="match-hub-header-right">
          <div class="match-hub-star-pill">
            <span class="star-icon">⭐</span>
            <span id="match-hub-total-stars">0</span><span class="total-stars-max">/90</span>
          </div>
          <button class="match-hub-close-btn" onclick="closeMatchLevelHub()" title="बंद करें">✕</button>
        </div>
      </div>

      <!-- Dedicated Smooth Momentum-Scrolling Body -->
      <div class="match-hub-scroll-body" id="match-hub-scroll-body">
        <!-- 16 Sacred Symbols Showcase Strip -->
        <div class="match-symbols-showcase">
          <div class="symbols-strip-header">
            <div class="strip-header-title">
              <span>✨</span>
              <span>१६ पावन भक्ति प्रतीक (16 Sacred Symbols)</span>
            </div>
            <span class="strip-header-hint">स्लाइड करें ❯</span>
          </div>
          <div class="match-symbols-scroll" id="match-symbols-scroll-tray">
            <div id="match-symbols-strip" class="match-symbols-strip">
              <!-- Rendered dynamically by engine -->
            </div>
          </div>
        </div>

        <!-- Quick Resume / Progress Hero Banner -->
        <div class="match-progress-hero">
          <div class="progress-hero-info">
            <div class="progress-hero-h">🎯 स्तर चयन करें</div>
            <div class="progress-hero-sub">जोड़ी मिलाकर सभी ३० स्तर जीतें व सिक्के पाएँ</div>
          </div>
          <button class="progress-hero-btn" onclick="startMatchGameAtLevel(currentMatchLevel || 1)">
            <span>▶</span>
            <span>जारी रखें</span>
          </button>
        </div>

        <!-- Tier Tabs Indicator (Level 1-10, 11-20, 21-30) -->
        <div class="match-tier-pills-row">
          <span class="tier-pill-chip active">🌱 प्रारंभिक (१-१०)</span>
          <span class="tier-pill-chip">⚔️ महारथी (११-२०)</span>
          <span class="tier-pill-chip">🔱 दिव्य (२१-३०)</span>
        </div>

        <!-- 30 Levels Grid -->
        <div class="match-level-grid-wrap">
          <div id="match-level-hub-grid" class="match-level-grid">
            <!-- 30 Levels rendered dynamically with ZERO text truncation -->
          </div>
        </div>

        <!-- Extra safe bottom spacer so Level 30 is fully reachable on all phones -->
        <div class="match-hub-bottom-spacer"></div>
      </div>
    </div>

    """

html = html[:hub_start] + new_hub_html + html[hub_end:]
with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html)
print("✓ Updated index.html with new clean scrollable match-level-hub-modal")

print("\n=== 2. Updating epic_games_engine.js with Complete Level Hub Logic ===")
with open(ENGINE_FILE, "r", encoding="utf-8") as f:
    engine = f.read()

# Add the level hub rendering and controller functions
match_hub_js = """
  /* ══════════════════════════════════════════════════════════════════════════════
     🎴 BHAKTI CARD MATCH LEVEL HUB (30 LEVELS CONTROLLER & SMOOTH SCROLL)
     ══════════════════════════════════════════════════════════════════════════════ */
  function openMatchLevelHub() {
    hideBottomNavForGames();
    var modal = document.getElementById('match-level-hub-modal');
    if (!modal) return;

    modal.style.setProperty('display', 'flex', 'important');
    modal.classList.add('active');

    // Update total stars in header
    var starsEl = document.getElementById('match-hub-total-stars');
    if (starsEl) starsEl.innerText = getMatchTotalStars();

    // Render 16 Sacred Symbols Strip
    renderMatchSymbolsStrip();

    // Render 30 Level Cards
    renderMatchLevelHubGrid();

    // Scroll to current active level smoothly
    setTimeout(function() {
      var scrollBody = document.getElementById('match-hub-scroll-body');
      var activeCard = document.querySelector('.match-level-card.is-current');
      if (scrollBody && activeCard) {
        var topPos = activeCard.offsetTop - 140;
        scrollBody.scrollTo({ top: Math.max(0, topPos), behavior: 'smooth' });
      }
    }, 120);
  }

  function closeMatchLevelHub() {
    var modal = document.getElementById('match-level-hub-modal');
    if (modal) {
      modal.classList.remove('active');
      modal.style.setProperty('display', 'none', 'important');
    }
    restoreBottomNavIfExited();
  }

  function renderMatchSymbolsStrip() {
    var strip = document.getElementById('match-symbols-strip');
    if (!strip || !bhaktiSymbols || !bhaktiSymbols.length) return;
    strip.innerHTML = '';

    bhaktiSymbols.forEach(function(sym) {
      var item = document.createElement('div');
      item.className = 'match-symbol-chip';
      item.onclick = function() {
        if (typeof showToast === 'function') {
          showToast('✨ पावन दर्शन: ' + sym.name);
        }
      };
      item.innerHTML = `
        <div class="symbol-chip-thumb-wrap">
          <img src="${sym.img}" alt="${sym.name}" class="symbol-chip-img" loading="lazy">
        </div>
        <span class="symbol-chip-label">${sym.name}</span>
      `;
      strip.appendChild(item);
    });
  }

  function renderMatchLevelHubGrid() {
    var grid = document.getElementById('match-level-hub-grid');
    if (!grid) return;
    grid.innerHTML = '';

    var totalStars = getMatchTotalStars();

    for (var lvl = 1; lvl <= 30; lvl++) {
      var cfg = getMatchLevelConfig(lvl);
      var starsEarned = savedMatchStars[lvl] || 0;
      var isBoss = (lvl % 10 === 0 || lvl === 30);

      // Unlock rule: Level 1 always unlocked. Level N unlocked if Level N-1 has >= 1 star OR totalStars >= (lvl-1)*2
      var prevWon = (lvl === 1) || (savedMatchStars[lvl - 1] && savedMatchStars[lvl - 1] > 0);
      var reqStars = (lvl - 1) * 2;
      var unlocked = (lvl === 1) || prevWon || (totalStars >= reqStars);
      var isCurrent = unlocked && (!savedMatchStars[lvl] || savedMatchStars[lvl] === 0) && (lvl === 1 || (savedMatchStars[lvl - 1] && savedMatchStars[lvl - 1] > 0));

      // Tier text & styling
      var tierName = '';
      var tierClass = '';
      if (lvl <= 10) {
        tierName = '🌱 प्रारंभिक';
        tierClass = 'tier-init';
      } else if (lvl <= 20) {
        tierName = '⚔️ महारथी';
        tierClass = 'tier-mid';
      } else {
        tierName = '🔱 दिव्य';
        tierClass = 'tier-divine';
      }

      var card = document.createElement('div');
      card.className = 'match-level-card' +
        (unlocked ? ' is-unlocked' : ' is-locked') +
        (isCurrent ? ' is-current' : '') +
        (isBoss ? ' is-boss' : '');

      card.setAttribute('data-level', lvl);

      // Card Header: Level Number (left) & Tier Badge (right)
      var bossBadgeHtml = isBoss ? `<span class="ml-boss-tag">👑 महा-स्तर</span>` : `<span class="ml-tier-tag ${tierClass}">${tierName}</span>`;

      // Footer: Stars or Play or Lock info
      var footerHtml = '';
      if (!unlocked) {
        footerHtml = `<div class="ml-status-locked"><span class="ml-lock-icon">🔒</span> <span>${reqStars} ⭐ चाहिए</span></div>`;
      } else if (starsEarned > 0) {
        var starsStr = '';
        for (var s = 1; s <= 5; s++) {
          starsStr += (s <= starsEarned) ? '⭐' : '☆';
        }
        footerHtml = `<div class="ml-stars-row"><span class="ml-stars-txt">${starsStr}</span></div>`;
      } else {
        footerHtml = `<div class="ml-status-play"><span class="ml-play-icon">▶</span> <span>खेलें</span></div>`;
      }

      card.innerHTML = `
        <div class="ml-card-header">
          <div class="ml-num-badge">${lvl}</div>
          ${bossBadgeHtml}
        </div>
        <div class="ml-card-body">
          <div class="ml-pairs-title">${cfg.pairs} जोड़ियाँ</div>
          <div class="ml-cards-sub">${cfg.pairs * 2} पावन कार्ड</div>
        </div>
        <div class="ml-card-footer">
          ${footerHtml}
        </div>
      `;

      // Click Handler
      (function(levelNum, isUnlocked, req) {
        card.onclick = function() {
          if (!isUnlocked) {
            showMatchLockAlert(req);
            return;
          }
          startMatchGameAtLevel(levelNum);
        };
      })(lvl, unlocked, reqStars);

      grid.appendChild(card);
    }
  }

  function startMatchGameAtLevel(lvl) {
    var hub = document.getElementById('match-level-hub-modal');
    if (hub) {
      hub.style.setProperty('display', 'none', 'important');
      hub.classList.remove('active');
    }

    var arena = document.getElementById('match-game-modal');
    if (arena) {
      arena.classList.add('active');
      arena.classList.add('is-open');
      arena.style.setProperty('display', 'flex', 'important');
      arena.style.setProperty('opacity', '1', 'important');
      arena.style.setProperty('pointer-events', 'auto', 'important');
      arena.style.setProperty('visibility', 'visible', 'important');
    }

    initMatchLevel(lvl);
  }

  function returnToMatchLevelHub() {
    var arena = document.getElementById('match-game-modal');
    if (arena) {
      arena.classList.remove('active');
      arena.classList.remove('is-open');
      arena.style.setProperty('display', 'none', 'important');
    }
    var winModal = document.getElementById('matchWinModal');
    if (winModal) winModal.style.display = 'none';

    openMatchLevelHub();
  }

  function closeMatchLevelArena() {
    returnToMatchLevelHub();
  }

  // Hook global functions
  window.openMatchLevelHub = openMatchLevelHub;
  window.closeMatchLevelHub = closeMatchLevelHub;
  window.renderMatchLevelHub = openMatchLevelHub;
  window.startMatchGameAtLevel = startMatchGameAtLevel;
  window.returnToMatchLevelHub = returnToMatchLevelHub;
  window.closeMatchLevelArena = closeMatchLevelArena;
"""

# Update window.openMatchGame to open level hub by default
old_open_match_regex = re.compile(
    r'window\.openMatchGame\s*=\s*function\s*\([^\)]*\)\s*\{[\s\S]*?initMatchLevel\([^\)]*\);\s*\};',
    re.MULTILINE
)

new_open_match_js = """window.openMatchGame = function (lvlIdx) {
    if (typeof lvlIdx === 'number' && lvlIdx >= 1) {
      startMatchGameAtLevel(lvlIdx);
    } else {
      openMatchLevelHub();
    }
  };"""

if old_open_match_regex.search(engine):
    engine = old_open_match_regex.sub(new_open_match_js, engine, count=1)
    print("✓ Replaced window.openMatchGame to launch Level Hub by default")

# Insert match_hub_js into epic_games_engine.js
if "openMatchLevelHub" not in engine:
    engine += "\n" + match_hub_js
    print("✓ Appended Match Level Hub Controller logic to epic_games_engine.js")
else:
    # Replace existing block if needed
    print("✓ openMatchLevelHub already referenced, appending updated logic block")
    engine += "\n" + match_hub_js

with open(ENGINE_FILE, "w", encoding="utf-8") as f:
    f.write(engine)
print("✓ Saved epic_games_engine.js")

print("\n=== 3. Updating epic_games.css with Stunning UI/UX & Smooth Scrolling Styles ===")
with open(CSS_FILE, "r", encoding="utf-8") as f:
    css = f.read()

new_match_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   🎴 UPGRADED BHAKTI CARD MATCH LEVEL SELECTOR UI/UX & SMOOTH SCROLL SYSTEM
   ══════════════════════════════════════════════════════════════════════════════ */
#match-level-hub-modal {
  position: fixed !important;
  inset: 0 !important;
  z-index: 100240 !important;
  background: radial-gradient(circle at 50% 0%, #250B3B 0%, #0D0316 65%, #180628 100%) !important;
  color: #FFFFFF !important;
  display: none;
  flex-direction: column !important;
  overflow: hidden !important; /* Outer container locks screen; inner body scrolls smoothly */
  user-select: none;
}

#match-level-hub-modal.active {
  display: flex !important;
}

/* ── Fixed Sticky Header with Safe-Area Top Padding ── */
.match-hub-header {
  flex-shrink: 0 !important;
  z-index: 100 !important;
  background: rgba(22, 6, 36, 0.98) !important;
  backdrop-filter: blur(18px) !important;
  -webkit-backdrop-filter: blur(18px) !important;
  border-bottom: 1.5px solid rgba(245, 158, 11, 0.45) !important;
  padding: 10px 14px !important;
  padding-top: max(10px, env(safe-area-inset-top)) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6) !important;
}

.match-hub-header-left {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
}

.match-hub-back-btn {
  background: rgba(255, 255, 255, 0.12) !important;
  border: 1.5px solid rgba(245, 158, 11, 0.5) !important;
  border-radius: 50% !important;
  width: 36px !important;
  height: 36px !important;
  font-size: 1.25rem !important;
  font-weight: 900 !important;
  color: #FDE68A !important;
  cursor: pointer !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: transform 0.15s ease !important;
}

.match-hub-back-btn:active {
  transform: scale(0.92) !important;
}

.match-hub-title-block {
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
}

.match-hub-title {
  margin: 0 !important;
  font-size: 1.15rem !important;
  font-weight: 900 !important;
  color: #FFFDF8 !important;
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
  letter-spacing: 0.3px !important;
}

.match-hub-icon {
  font-size: 1.25rem !important;
}

.match-hub-subtitle {
  font-size: 0.72rem !important;
  color: #FDE68A !important;
  font-weight: 700 !important;
  margin-top: 1px !important;
}

.match-hub-header-right {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
}

.match-hub-star-pill {
  background: rgba(245, 158, 11, 0.22) !important;
  border: 1.2px solid #F59E0B !important;
  border-radius: 18px !important;
  padding: 4px 10px !important;
  font-size: 0.85rem !important;
  font-weight: 900 !important;
  color: #FDE68A !important;
  display: flex !important;
  align-items: center !important;
  gap: 4px !important;
  box-shadow: 0 2px 8px rgba(245, 158, 11, 0.25) !important;
}

.total-stars-max {
  font-size: 0.72rem !important;
  opacity: 0.85 !important;
}

.match-hub-close-btn {
  background: rgba(255, 255, 255, 0.08) !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-radius: 50% !important;
  width: 32px !important;
  height: 32px !important;
  color: #E2E8F0 !important;
  font-size: 1.1rem !important;
  font-weight: 800 !important;
  cursor: pointer !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 0 !important;
}

/* ── Dedicated Smooth Scrolling Body ── */
.match-hub-scroll-body {
  flex: 1 !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  -webkit-overflow-scrolling: touch !important; /* Smooth iOS/Android Momentum Scroll */
  overscroll-behavior-y: contain !important;
  touch-action: pan-y !important;
  padding: 10px 14px 40px !important;
  max-width: 640px !important;
  width: 100% !important;
  margin: 0 auto !important;
  box-sizing: border-box !important;
}

/* ── 16 Sacred Symbols Strip ── */
.match-symbols-showcase {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(245, 158, 11, 0.25);
  border-radius: 18px;
  padding: 10px 12px;
  margin-bottom: 12px;
}

.symbols-strip-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.strip-header-title {
  font-size: 0.82rem;
  font-weight: 900;
  color: #FDE68A;
  display: flex;
  align-items: center;
  gap: 5px;
}

.strip-header-hint {
  font-size: 0.65rem;
  color: #E9D5FF;
  font-weight: 700;
}

.match-symbols-scroll {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
  padding-bottom: 2px;
}

.match-symbols-scroll::-webkit-scrollbar {
  display: none;
}

.match-symbols-strip {
  display: flex;
  gap: 10px;
}

.match-symbol-chip {
  flex: 0 0 62px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  cursor: pointer;
  transition: transform 0.15s ease;
}

.match-symbol-chip:active {
  transform: scale(0.92);
}

.symbol-chip-thumb-wrap {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #2D0B40;
  border: 1.5px solid #F59E0B;
  box-shadow: 0 2px 8px rgba(245, 158, 11, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  margin-bottom: 4px;
}

.symbol-chip-img {
  width: 90%;
  height: 90%;
  object-fit: contain;
}

.symbol-chip-label {
  font-size: 0.58rem;
  font-weight: 800;
  color: #F5E8C7;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;
}

/* ── Progress Resume Banner ── */
.match-progress-hero {
  background: linear-gradient(135deg, rgba(88, 28, 135, 0.35) 0%, rgba(245, 158, 11, 0.15) 100%);
  border: 1.2px solid rgba(245, 158, 11, 0.35);
  border-radius: 16px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.progress-hero-h {
  font-size: 0.88rem;
  font-weight: 900;
  color: #FFFDF8;
}

.progress-hero-sub {
  font-size: 0.68rem;
  color: #E9D5FF;
  margin-top: 1px;
}

.progress-hero-btn {
  background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
  color: #1A0B2E;
  border: 1px solid #FEF08A;
  border-radius: 14px;
  font-weight: 900;
  font-size: 0.82rem;
  padding: 6px 14px;
  cursor: pointer;
  box-shadow: 0 3px 10px rgba(245, 158, 11, 0.45);
  display: flex;
  align-items: center;
  gap: 5px;
  transition: transform 0.15s ease;
}

.progress-hero-btn:active {
  transform: scale(0.94);
}

/* ── Tier Tabs Row ── */
.match-tier-pills-row {
  display: flex;
  gap: 6px;
  margin-bottom: 10px;
  overflow-x: auto;
  scrollbar-width: none;
}

.tier-pill-chip {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(245, 158, 11, 0.25);
  color: #E9D5FF;
  font-size: 0.68rem;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: 10px;
  white-space: nowrap;
}

.tier-pill-chip.active {
  background: rgba(245, 158, 11, 0.25);
  border-color: #F59E0B;
  color: #FDE68A;
}

/* ── 30 Levels Grid (No Truncation, Clean Cards) ── */
.match-level-grid {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 10px !important;
  width: 100% !important;
}

@media (min-width: 520px) {
  .match-level-grid {
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 12px !important;
  }
}

.match-level-card {
  background: linear-gradient(135deg, rgba(40, 14, 60, 0.85) 0%, rgba(20, 6, 32, 0.95) 100%) !important;
  border: 1.4px solid rgba(245, 158, 11, 0.35) !important;
  border-radius: 16px !important;
  padding: 10px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  min-height: 98px !important;
  cursor: pointer !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4) !important;
  transition: transform 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease !important;
  position: relative !important;
  overflow: hidden !important;
  box-sizing: border-box !important;
}

.match-level-card:active {
  transform: scale(0.96) !important;
}

.match-level-card.is-unlocked {
  border-color: rgba(245, 158, 11, 0.65) !important;
  background: linear-gradient(135deg, rgba(50, 18, 75, 0.9) 0%, rgba(26, 8, 40, 0.95) 100%) !important;
}

.match-level-card.is-current {
  border: 2px solid #F59E0B !important;
  box-shadow: 0 0 16px rgba(245, 158, 11, 0.5), 0 4px 14px rgba(0,0,0,0.6) !important;
  animation: currentLevelPulse 2s infinite ease-in-out !important;
}

@keyframes currentLevelPulse {
  0%, 100% { border-color: #F59E0B; box-shadow: 0 0 12px rgba(245, 158, 11, 0.4); }
  50% { border-color: #FEF08A; box-shadow: 0 0 22px rgba(245, 158, 11, 0.8); }
}

.match-level-card.is-locked {
  opacity: 0.55 !important;
  filter: grayscale(0.2) !important;
  border-color: rgba(255, 255, 255, 0.12) !important;
  background: rgba(255, 255, 255, 0.03) !important;
}

.match-level-card.is-boss {
  background: linear-gradient(135deg, rgba(88, 28, 135, 0.95) 0%, rgba(45, 10, 45, 0.98) 100%) !important;
  border: 1.8px solid #F59E0B !important;
  box-shadow: 0 4px 16px rgba(245, 158, 11, 0.35) !important;
}

/* Card Header: Level Number + Tier Tag */
.ml-card-header {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  width: 100% !important;
  margin-bottom: 4px !important;
}

.ml-num-badge {
  width: 28px !important;
  height: 28px !important;
  border-radius: 9px !important;
  background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
  color: #1A0B2E !important;
  font-weight: 900 !important;
  font-size: 0.88rem !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important;
}

.match-level-card.is-locked .ml-num-badge {
  background: #334155 !important;
  color: #94A3B8 !important;
  box-shadow: none !important;
}

.match-level-card.is-boss .ml-num-badge {
  background: linear-gradient(135deg, #EF4444 0%, #B91C1C 100%) !important;
  color: #FFF !important;
  border: 1px solid #FDE68A !important;
}

.ml-tier-tag {
  font-size: 0.58rem !important;
  font-weight: 800 !important;
  padding: 2px 6px !important;
  border-radius: 6px !important;
  line-height: 1 !important;
}

.tier-init { background: rgba(34, 197, 94, 0.2); color: #86EFAC; border: 0.8px solid rgba(34, 197, 94, 0.4); }
.tier-mid { background: rgba(59, 130, 246, 0.2); color: #93C5FD; border: 0.8px solid rgba(59, 130, 246, 0.4); }
.tier-divine { background: rgba(168, 85, 247, 0.25); color: #E9D5FF; border: 0.8px solid rgba(168, 85, 247, 0.5); }

.ml-boss-tag {
  font-size: 0.58rem !important;
  font-weight: 900 !important;
  padding: 2px 6px !important;
  border-radius: 6px !important;
  background: linear-gradient(135deg, #DC2626, #991B1B) !important;
  color: #FEF08A !important;
  border: 0.8px solid #FDE68A !important;
  line-height: 1 !important;
}

/* Card Body: Pairs and Cards (NO TRUNCATION!) */
.ml-card-body {
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  margin: 3px 0 !important;
  width: 100% !important;
}

.ml-pairs-title {
  font-size: 0.88rem !important;
  font-weight: 900 !important;
  color: #FFFDF8 !important;
  line-height: 1.15 !important;
  white-space: nowrap !important;
}

.ml-cards-sub {
  font-size: 0.65rem !important;
  color: #D8B4FE !important;
  font-weight: 700 !important;
  margin-top: 1px !important;
  white-space: nowrap !important;
}

/* Card Footer: Stars or Play or Lock status */
.ml-card-footer {
  width: 100% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  margin-top: 2px !important;
}

.ml-stars-row {
  display: flex !important;
  align-items: center !important;
  font-size: 0.76rem !important;
  color: #FBBF24 !important;
  letter-spacing: -1px !important;
}

.ml-status-play {
  display: inline-flex !important;
  align-items: center !important;
  gap: 4px !important;
  background: linear-gradient(135deg, #F59E0B, #D97706) !important;
  color: #1A0B2E !important;
  font-size: 0.62rem !important;
  font-weight: 900 !important;
  padding: 2px 8px !important;
  border-radius: 6px !important;
}

.ml-status-locked {
  display: inline-flex !important;
  align-items: center !important;
  gap: 3px !important;
  color: #94A3B8 !important;
  font-size: 0.62rem !important;
  font-weight: 700 !important;
}

.ml-lock-icon {
  font-size: 0.72rem !important;
}

/* Safe bottom spacer */
.match-hub-bottom-spacer {
  height: 100px !important;
  width: 100% !important;
  pointer-events: none !important;
}
"""

css += "\n" + new_match_css
with open(CSS_FILE, "w", encoding="utf-8") as f:
    f.write(css)
print("✓ Appended upgraded Match Level UI & Smooth Scroll CSS to epic_games.css")

print("\n=== Match Game UI/UX Upgrade Completed Successfully ===")
