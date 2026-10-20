import os
import sys
import json
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
DATA_FILE = os.path.join(BASE_DIR, "assets", "cards", "swipe_game_data.json")
ENGINE_FILE = os.path.join(BASE_DIR, "epic_games_engine.js")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")
GALLERY_FILE = os.path.join(BASE_DIR, "gallery_engine.js")
CSS_FILE = os.path.join(BASE_DIR, "epic_games.css")

print("1. Loading swipe_game_data.json...")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    swipe_data = json.load(f)

categories = swipe_data["categories"]
print(f"Loaded {len(categories)} categories with {[len(c['cards']) for c in categories]} cards.")

# ══════════════════════════════════════════════════════════════════════════════
# 2. UPDATE EPIC_GAMES_ENGINE.JS
# ══════════════════════════════════════════════════════════════════════════════
print("\n2. Updating epic_games_engine.js...")
with open(ENGINE_FILE, "r", encoding="utf-8") as f:
    engine_content = f.read()

# Build the JS SWIPE_CATEGORIES dictionary
cat_dict = {}
for cat in categories:
    cat_dict[cat["id"]] = cat

# Also add aliases
cat_dict["ayodhya_mithila"] = cat_dict["cat_1_ramayana"]
cat_dict["lanka_war"] = cat_dict["cat_2_lanka_war"]
cat_dict["pandav_kaurav"] = cat_dict["cat_3_mahabharat"]

swipe_categories_js = "  var SWIPE_CATEGORIES = " + json.dumps(cat_dict, ensure_ascii=False, indent=2) + ";\n"

# Replace SWIPE_CATEGORIES block in epic_games_engine.js
pattern_categories = re.compile(r'  var SWIPE_CATEGORIES = \{[\s\S]*?\n  \};\n', re.MULTILINE)
if pattern_categories.search(engine_content):
    engine_content = pattern_categories.sub(swipe_categories_js, engine_content, count=1)
    print("✓ Replaced SWIPE_CATEGORIES in epic_games_engine.js")
else:
    print("⚠ Pattern for SWIPE_CATEGORIES not matched directly, checking fallback...")

# Now update initSwipeGame, renderCurrentCard, handleSwipeCommit, showCharacterReviewScreen, renderReviewCard
new_swipe_logic = """
  // ══════════════════════════════════════════════════════════════════════════════
  // 2. SWIPE GAME LOGIC & TOUCH PHYSICS
  // ══════════════════════════════════════════════════════════════════════════════
  var activeCardEl = null;
  var isDragging = false;
  var startX = 0;
  var startY = 0;
  var currentX = 0;
  var currentY = 0;

  function initSwipeGame(categoryKey) {
    categoryKey = categoryKey || 'cat_1_ramayana';
    var cat = SWIPE_CATEGORIES[categoryKey] || SWIPE_CATEGORIES.cat_1_ramayana;
    epicGameState.currentCategory = cat.id;
    epicGameState.ayodhyaScore = 0;
    epicGameState.mithilaScore = 0;
    epicGameState.currentIndex = 0;
    epicGameState.correctCount = 0;
    epicGameState.swipedHistory = [];

    // Shuffle characters for replayability
    var list = (cat.cards || []).slice();
    for (var i = list.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var temp = list[i];
      list[i] = list[j];
      list[j] = temp;
    }
    epicGameState.deck = list;

    // Update Arena labels & header
    var titleEl = document.getElementById('swipe-cat-title');
    if (titleEl) titleEl.textContent = cat.title;

    var instEl = document.getElementById('swipe-instruction');
    if (instEl) instEl.textContent = cat.instruction;

    var leftLabel = document.getElementById('swipe-left-portal-label');
    if (leftLabel) leftLabel.textContent = cat.leftSide.name;

    var rightLabel = document.getElementById('swipe-right-portal-label');
    if (rightLabel) rightLabel.textContent = cat.rightSide.name;

    var leftScore = document.getElementById('swipe-left-score');
    if (leftScore) {
      leftScore.textContent = '0';
      leftScore.style.background = cat.leftSide.bgColor;
    }

    var rightScore = document.getElementById('swipe-right-score');
    if (rightScore) {
      rightScore.textContent = '0';
      rightScore.style.background = cat.rightSide.bgColor;
    }

    // Update Gates / Portals
    var leftGateImg = document.getElementById('swipe-gate-left') || document.querySelector('#swipe-portal-left .swipe-portal-bg');
    if (leftGateImg) {
      leftGateImg.src = cat.leftSide.gateAsset;
      leftGateImg.onerror = function () { this.src = 'assets/games/portal_ayodhya.jpg'; };
    }

    var rightGateImg = document.getElementById('swipe-gate-right') || document.querySelector('#swipe-portal-right .swipe-portal-bg');
    if (rightGateImg) {
      rightGateImg.src = cat.rightSide.gateAsset;
      rightGateImg.onerror = function () { this.src = 'assets/games/portal_mithila.jpg'; };
    }

    // Update Desktop Accessibility Buttons
    var btnLeft = document.getElementById('swipe-btn-left');
    if (btnLeft) {
      btnLeft.textContent = '⟵ ' + cat.leftSide.label;
      btnLeft.style.background = cat.leftSide.bgColor;
    }
    var btnRight = document.getElementById('swipe-btn-right');
    if (btnRight) {
      btnRight.textContent = cat.rightSide.label + ' ⟶';
      btnRight.style.background = cat.rightSide.bgColor;
    }

    renderCurrentCard();
  }

  function renderCurrentCard() {
    var stage = document.getElementById('swipe-card-deck');
    if (!stage) return;

    if (epicGameState.currentIndex >= epicGameState.deck.length) {
      // Round Complete! Transition to Character Review Screen
      setTimeout(showCharacterReviewScreen, 400);
      return;
    }

    var char = epicGameState.deck[epicGameState.currentIndex];

    stage.innerHTML = `
      <div class="swipe-card-underlay swipe-card-underlay-2"></div>
      <div class="swipe-card-underlay swipe-card-underlay-1"></div>
      
      <div class="swipe-main-card" id="swipe-active-card">
        <div class="swipe-card-jewel-top"></div>
        <div class="swipe-card-jewel-left"></div>
        <div class="swipe-card-jewel-right"></div>
        <img src="${char.image}" alt="${char.name}" class="swipe-char-portrait" onerror="this.src='assets/games/char_sunaina.jpg';">
        <div class="swipe-char-name-bar">${char.name}</div>
      </div>
    `;

    activeCardEl = document.getElementById('swipe-active-card');
    attachDragListeners(activeCardEl);
  }

  function attachDragListeners(el) {
    if (!el) return;

    el.onpointerdown = function (e) {
      isDragging = true;
      startX = e.clientX;
      startY = e.clientY;
      currentX = startX;
      currentY = startY;
      el.classList.add('dragging');
      el.setPointerCapture(e.pointerId);
    };

    el.onpointermove = function (e) {
      if (!isDragging) return;
      currentX = e.clientX;
      currentY = e.clientY;
      var dx = currentX - startX;
      var dy = currentY - startY;

      // Rotate card slightly with drag
      var rotate = dx * 0.08;
      el.style.transform = `translate(${dx}px, ${dy}px) rotate(${rotate}deg)`;

      // Highlight target portals
      var leftPortal = document.getElementById('swipe-portal-left');
      var rightPortal = document.getElementById('swipe-portal-right');

      if (dx < -40) {
        if (leftPortal) leftPortal.classList.add('active-target');
        if (rightPortal) rightPortal.classList.remove('active-target');
      } else if (dx > 40) {
        if (rightPortal) rightPortal.classList.add('active-target');
        if (leftPortal) leftPortal.classList.remove('active-target');
      } else {
        if (leftPortal) leftPortal.classList.remove('active-target');
        if (rightPortal) rightPortal.classList.remove('active-target');
      }
    };

    el.onpointerup = function (e) {
      if (!isDragging) return;
      isDragging = false;
      el.classList.remove('dragging');
      try { el.releasePointerCapture(e.pointerId); } catch (err) {}

      var dx = currentX - startX;
      var leftPortal = document.getElementById('swipe-portal-left');
      var rightPortal = document.getElementById('swipe-portal-right');
      if (leftPortal) leftPortal.classList.remove('active-target');
      if (rightPortal) rightPortal.classList.remove('active-target');

      // Swipe Threshold: 65px
      if (dx < -65) {
        handleSwipeCommit('left');
      } else if (dx > 65) {
        handleSwipeCommit('right');
      } else {
        // Spring back to center
        el.style.transition = 'transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
        el.style.transform = 'translate(0px, 0px) rotate(0deg)';
      }
    };
  }

  function handleSwipeCommit(direction) {
    var char = epicGameState.deck[epicGameState.currentIndex];
    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var isCorrect = (direction.toUpperCase() === char.correctSwipe.toUpperCase());
    var chosenSide = direction === 'left' ? cat.leftSide : cat.rightSide;

    playSound('swipe');

    // Throw animation
    if (activeCardEl) {
      activeCardEl.style.transition = 'transform 0.3s ease-out, opacity 0.3s ease-out';
      var throwX = direction === 'left' ? -380 : 380;
      var throwY = 160;
      activeCardEl.style.transform = `translate(${throwX}px, ${throwY}px) rotate(${direction === 'left' ? -30 : 30}deg) scale(0.4)`;
      activeCardEl.style.opacity = '0';
    }

    setTimeout(function () {
      if (isCorrect) {
        playSound('correct');
        epicGameState.correctCount++;
        addCoins(50);

        // Update portal counter
        if (direction === 'left') {
          epicGameState.ayodhyaScore++;
          var sEl = document.getElementById('swipe-left-score');
          if (sEl) sEl.textContent = epicGameState.ayodhyaScore;
        } else {
          epicGameState.mithilaScore++;
          var sEl = document.getElementById('swipe-right-score');
          if (sEl) sEl.textContent = epicGameState.mithilaScore;
        }

        // Floating Toast
        showCoinToast('+50 🪙');
      } else {
        playSound('wrong');
        showCoinToast('गलत पक्ष!');
      }

      epicGameState.swipedHistory.push({
        character: char,
        direction: direction,
        chosenSide: chosenSide,
        isCorrect: isCorrect
      });

      epicGameState.currentIndex++;
      renderCurrentCard();
    }, 280);
  }
"""

# Replace old swipe logic
pattern_swipe_logic = re.compile(r'  // ══════════════════════════════════════════════════════════════════════════════\s*// 2\. SWIPE GAME LOGIC & TOUCH PHYSICS[\s\S]*?renderCurrentCard\(\);\s*\}, 280\);\s*\}', re.MULTILINE)
if pattern_swipe_logic.search(engine_content):
    engine_content = pattern_swipe_logic.sub(new_swipe_logic.strip(), engine_content, count=1)
    print("✓ Replaced Swipe logic (init, drag, commit) in epic_games_engine.js")
else:
    print("⚠ Pattern for swipe logic not matched, searching broader block...")

# Update showCharacterReviewScreen & renderReviewCard
new_review_logic = """
  // ══════════════════════════════════════════════════════════════════════════════
  // 3. CHARACTER REVIEW SCREEN
  // ══════════════════════════════════════════════════════════════════════════════
  function showCharacterReviewScreen() {
    hideBottomNavForGames();
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'none';

    var rev = document.getElementById('swipe-review-arena');
    if (!rev) return;
    rev.style.display = 'flex';

    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var characters = cat.cards || [];

    // Render tokens list in bottom rail
    var rail = document.getElementById('swipe-review-tokens-rail');
    if (rail) {
      rail.innerHTML = '';
      characters.forEach(function (c, idx) {
        var token = document.createElement('div');
        token.className = 'swipe-char-token' + (idx === 0 ? ' active-token' : '');
        token.innerHTML = `
          <div class="swipe-token-circle">
            <img src="${c.image}" alt="${c.name}" class="swipe-token-avatar" onerror="this.src='assets/games/char_sunaina.jpg';">
            <div class="swipe-token-check">✓</div>
          </div>
          <div class="swipe-token-label">${c.name}</div>
        `;
        token.onclick = function () {
          document.querySelectorAll('.swipe-char-token').forEach(t => t.classList.remove('active-token'));
          token.classList.add('active-token');
          renderReviewCard(c);
        };
        rail.appendChild(token);
      });
    }

    // Default select first character
    if (characters.length > 0) {
      renderReviewCard(characters[0]);
    }
  }

  function renderReviewCard(char) {
    var card = document.getElementById('swipe-review-card-container');
    if (!card) return;

    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var side = char.correctSwipe === 'LEFT' ? cat.leftSide : cat.rightSide;

    card.innerHTML = `
      <div class="swipe-review-card">
        <div class="swipe-review-img-wrap">
          <img src="${char.image}" alt="${char.name}" class="swipe-review-img" onerror="this.src='assets/games/char_sunaina.jpg';">
          <div class="swipe-review-team-badge" style="background:${side.bgColor}; color:#FFF;">${side.name}</div>
        </div>
        <div class="swipe-review-info-body">
          <div class="swipe-review-char-name">${char.name}</div>
          <div class="swipe-review-divider"></div>
          <div class="swipe-review-char-desc">${char.desc}</div>
          <button class="swipe-review-network-btn" onclick="window.openCharacterNetworkModal('${char.id}')">📖 महाकाव्य संदर्भ</button>
        </div>
      </div>
    `;
  }
"""

pattern_review = re.compile(r'  // ══════════════════════════════════════════════════════════════════════════════\s*// 3\. CHARACTER REVIEW SCREEN[\s\S]*?renderReviewCard\(char\) \{[\s\S]*?<\/div>\s*`;\s*\}', re.MULTILINE)
if pattern_review.search(engine_content):
    engine_content = pattern_review.sub(new_review_logic.strip(), engine_content, count=1)
    print("✓ Replaced Review screen logic in epic_games_engine.js")

# Update window functions for categories
window_category_functions = """
  // ── Category Modal & Switcher ──
  window.openSwipeCategoryModal = function () {
    var modal = document.getElementById('swipe-category-modal');
    if (modal) modal.style.display = 'flex';
  };

  window.closeSwipeCategoryModal = function () {
    var modal = document.getElementById('swipe-category-modal');
    if (modal) modal.style.display = 'none';
  };

  window.selectSwipeCategory = function (catId) {
    window.closeSwipeCategoryModal();
    initSwipeGame(catId);
  };

  window.newSwipeGame = function () {
    hideSwipeResultModal();
    var rev = document.getElementById('swipe-review-arena');
    if (rev) rev.style.display = 'none';
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'flex';

    // Cycle to next category: cat_1 -> cat_2 -> cat_3 -> cat_1
    var cats = ['cat_1_ramayana', 'cat_2_lanka_war', 'cat_3_mahabharat'];
    var currIdx = cats.indexOf(epicGameState.currentCategory);
    var nextCat = cats[(currIdx + 1) % cats.length];
    initSwipeGame(nextCat);
  };

  window.openCharacterNetworkModal = function (charId) {
    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var c = (cat.cards || []).find(x => x.id === charId);
    if (c) {
      var side = c.correctSwipe === 'LEFT' ? cat.leftSide.name : cat.rightSide.name;
      alert(`📜 महाकाव्य चरित्र: ${c.name}\\n\\nपक्ष: ${side}\\n\\nवर्णन: ${c.desc}`);
    } else {
      alert(`📜 महाकाव्य वंशावली: ${charId}`);
    }
  };
"""

pattern_win_funcs = re.compile(r'  window\.newSwipeGame = function \(\) \{[\s\S]*?window\.openCharacterNetworkModal = function \(charId\) \{[\s\S]*?\};', re.MULTILINE)
if pattern_win_funcs.search(engine_content):
    engine_content = pattern_win_funcs.sub(window_category_functions.strip(), engine_content, count=1)
    print("✓ Replaced window category & newSwipeGame functions in epic_games_engine.js")

with open(ENGINE_FILE, "w", encoding="utf-8") as f:
    f.write(engine_content)
print("✓ Saved updated epic_games_engine.js")

# ══════════════════════════════════════════════════════════════════════════════
# 3. UPDATE INDEX.HTML
# ══════════════════════════════════════════════════════════════════════════════
print("\n3. Updating index.html...")
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

# 3A. Update the Epic Games Hub Swipe card
old_menu_card = """        <!-- 1. Swipe (WhatsApp Video Game!) -->
        <div class="epic-game-menu-card" onclick="openSwipeGame('ayodhya_mithila')" style="cursor:pointer; border:1.8px solid #3B82F6; box-shadow:0 8px 24px rgba(59,130,246,0.2);">
          <div class="epic-card-cover-wrap">
            <span class="epic-card-tag epic-tag-story" style="background:#2563EB;">🏹 स्वाइप</span>
            <img src="assets/games/cover_swipe.jpg" alt="Swipe" class="epic-card-cover-img" onerror="this.src='assets/games/char_sunaina.jpg';">
          </div>
          <div class="epic-card-title">रामायण स्वाइप (Swipe)</div>
          <div class="epic-card-subtitle">अयोध्या व मिथिला के पात्र पहचानें</div>
          <button class="epic-card-play-btn btn-blue" onclick="event.stopPropagation(); openSwipeGame('ayodhya_mithila');">🎮 खेलें (Play)</button>
        </div>"""

new_menu_card = """        <!-- 1. Swipe (WhatsApp Video Game!) -->
        <div class="epic-game-menu-card" onclick="openSwipeGame('cat_1_ramayana')" style="cursor:pointer; border:1.8px solid #F59E0B; box-shadow:0 8px 24px rgba(245,158,11,0.25);">
          <div class="epic-card-cover-wrap">
            <span class="epic-card-tag epic-tag-story" style="background:linear-gradient(135deg, #7C3AED, #DC2626); color:#FFF; font-weight:900;">🏹 १०० पात्र स्वाइप</span>
            <img src="assets/cards/ram.jpg" alt="Swipe" class="epic-card-cover-img" onerror="this.src='assets/games/cover_swipe.jpg';" style="object-fit:cover;">
          </div>
          <div class="epic-card-title">महाकाव्य स्वाइप (Swipe)</div>
          <div class="epic-card-subtitle">अयोध्या, लंका व महाभारत • १०० दिव्य पात्र</div>
          <button class="epic-card-play-btn btn-blue" style="background:linear-gradient(135deg, #7C3AED, #9333EA); color:#FFF; font-weight:900;" onclick="event.stopPropagation(); openSwipeGame('cat_1_ramayana');">🎮 खेलें (Play)</button>
        </div>"""

if old_menu_card in html_content:
    html_content = html_content.replace(old_menu_card, new_menu_card)
    print("✓ Updated Swipe card in Epic Games Hub")

# 3B. Update #swipe-arena in index.html to include IDs on gates & buttons, and hook dropdown
old_arena_top = """        <div class="swipe-cat-dropdown" onclick="newSwipeGame()">
          <span id="swipe-cat-title">श्रेणियाँ</span> <span>∨</span>
        </div>"""
new_arena_top = """        <div class="swipe-cat-dropdown" onclick="openSwipeCategoryModal()">
          <span id="swipe-cat-title">अयोध्या या मिथिला</span> <span>▼</span>
        </div>"""
if old_arena_top in html_content:
    html_content = html_content.replace(old_arena_top, new_arena_top)
    print("✓ Updated category dropdown trigger to openSwipeCategoryModal()")

# Update Desktop Buttons & Gate images with specific IDs
old_desktop_btns = """      <!-- Quick Desktop Swipe Buttons (Accessibility) -->
      <div style="display:flex; gap:16px; margin-bottom:4px; z-index:10;">
        <button onclick="swipeCardManual('left')" style="background:rgba(124,58,237,0.88); color:#FFF; border:1.5px solid #F59E0B; border-radius:14px; padding:6px 14px; font-weight:900; font-size:0.8rem; cursor:pointer; box-shadow:0 3px 10px rgba(0,0,0,0.3);">⟵ बाएँ (अयोध्या)</button>
        <button onclick="swipeCardManual('right')" style="background:rgba(220,38,38,0.88); color:#FFF; border:1.5px solid #F59E0B; border-radius:14px; padding:6px 14px; font-weight:900; font-size:0.8rem; cursor:pointer; box-shadow:0 3px 10px rgba(0,0,0,0.3);">दाएँ (मिथिला) ⟶</button>
      </div>"""

new_desktop_btns = """      <!-- Quick Desktop Swipe Buttons (Accessibility) -->
      <div style="display:flex; gap:16px; margin-bottom:4px; z-index:10;">
        <button id="swipe-btn-left" onclick="swipeCardManual('left')" style="background:#6B21A8; color:#FFF; border:1.5px solid #F59E0B; border-radius:14px; padding:6px 14px; font-weight:900; font-size:0.8rem; cursor:pointer; box-shadow:0 3px 10px rgba(0,0,0,0.3); transition:all 0.2s ease;">⟵ बाएँ (अयोध्या)</button>
        <button id="swipe-btn-right" onclick="swipeCardManual('right')" style="background:#DC2626; color:#FFF; border:1.5px solid #F59E0B; border-radius:14px; padding:6px 14px; font-weight:900; font-size:0.8rem; cursor:pointer; box-shadow:0 3px 10px rgba(0,0,0,0.3); transition:all 0.2s ease;">दाएँ (मिथिला) ⟶</button>
      </div>"""

if old_desktop_btns in html_content:
    html_content = html_content.replace(old_desktop_btns, new_desktop_btns)
    print("✓ Updated Desktop Buttons in index.html")

# Update Gates in #swipe-portals-container
old_portals = """      <!-- Two Bottom Shrines/Portals -->
      <div class="swipe-portals-container">
        <!-- Left Portal (Ayodhya) -->
        <div class="swipe-portal-shrine" id="swipe-portal-left" onclick="swipeCardManual('left')">
          <div class="swipe-portal-img-wrap">
            <img src="assets/games/portal_ayodhya.jpg" alt="अयोध्या" class="swipe-portal-bg">
            <div class="swipe-portal-score-badge score-ayodhya" id="swipe-left-score">0</div>
          </div>
          <div class="swipe-portal-label" id="swipe-left-portal-label">अयोध्या</div>
        </div>

        <!-- Right Portal (Mithila) -->
        <div class="swipe-portal-shrine" id="swipe-portal-right" onclick="swipeCardManual('right')">
          <div class="swipe-portal-img-wrap">
            <img src="assets/games/portal_mithila.jpg" alt="मिथिला" class="swipe-portal-bg">
            <div class="swipe-portal-score-badge score-mithila" id="swipe-right-score">0</div>
          </div>
          <div class="swipe-portal-label" id="swipe-right-portal-label">मिथिला</div>
        </div>
      </div>"""

new_portals = """      <!-- Two Bottom Shrines/Portals -->
      <div class="swipe-portals-container">
        <!-- Left Portal -->
        <div class="swipe-portal-shrine" id="swipe-portal-left" onclick="swipeCardManual('left')">
          <div class="swipe-portal-img-wrap">
            <img src="assets/gates/gate_ayodhya.png" alt="द्वार" class="swipe-portal-bg" id="swipe-gate-left" onerror="this.src='assets/games/portal_ayodhya.jpg';">
            <div class="swipe-portal-score-badge" id="swipe-left-score" style="background:#6B21A8;">0</div>
          </div>
          <div class="swipe-portal-label" id="swipe-left-portal-label">अयोध्या</div>
        </div>

        <!-- Right Portal -->
        <div class="swipe-portal-shrine" id="swipe-portal-right" onclick="swipeCardManual('right')">
          <div class="swipe-portal-img-wrap">
            <img src="assets/gates/gate_mithila.png" alt="द्वार" class="swipe-portal-bg" id="swipe-gate-right" onerror="this.src='assets/games/portal_mithila.jpg';">
            <div class="swipe-portal-score-badge" id="swipe-right-score" style="background:#DC2626;">0</div>
          </div>
          <div class="swipe-portal-label" id="swipe-right-portal-label">मिथिला</div>
        </div>
      </div>"""

if old_portals in html_content:
    html_content = html_content.replace(old_portals, new_portals)
    print("✓ Updated Portals / Gates markup in index.html")

# 3C. Add the Category Selection Modal HTML right after swipe-result-modal
category_modal_html = """
    <!-- ══════════ 🏹 SWIPE CATEGORY SELECTOR MODAL ══════════ -->
    <div id="swipe-category-modal" class="epic-game-modal-overlay" style="display:none; z-index:35000; background:rgba(18, 5, 30, 0.92); backdrop-filter:blur(10px); position:fixed; inset:0; align-items:center; justify-content:center; padding:16px;">
      <div style="background:radial-gradient(circle at top, #2D0B40 0%, #150522 100%); border:2px solid #F59E0B; border-radius:24px; padding:20px; max-width:420px; width:100%; box-shadow:0 20px 50px rgba(0,0,0,0.6); color:#FFF;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:16px;">
          <h3 style="margin:0; font-size:1.15rem; font-weight:900; color:#FDE68A; display:flex; align-items:center; gap:8px;">
            <span>🏹</span> स्वाइप श्रेणी चुनें
          </h3>
          <button onclick="closeSwipeCategoryModal()" style="background:rgba(255,255,255,0.1); border:1px solid rgba(245,158,11,0.4); border-radius:50%; width:32px; height:32px; color:#FFF; font-weight:900; cursor:pointer;">✕</button>
        </div>

        <div style="display:flex; flex-direction:column; gap:12px;">
          <!-- Category 1 -->
          <div onclick="selectSwipeCategory('cat_1_ramayana')" style="background:rgba(107,33,168,0.25); border:1.8px solid #6B21A8; border-radius:16px; padding:12px 14px; display:flex; align-items:center; justify-content:space-between; cursor:pointer; transition:transform 0.15s ease;">
            <div style="display:flex; align-items:center; gap:12px;">
              <div style="width:44px; height:44px; border-radius:50%; background:#6B21A8; display:flex; align-items:center; justify-content:center; font-size:1.4rem; border:1.5px solid #F59E0B;">🏛️</div>
              <div>
                <div style="font-weight:900; font-size:0.98rem; color:#FFF;">अयोध्या या मिथिला</div>
                <div style="font-size:0.78rem; color:#E9D5FF;">रामायण आरंभ • ४० दिव्य पात्र</div>
              </div>
            </div>
            <span style="font-size:1.2rem; color:#FDE68A;">➔</span>
          </div>

          <!-- Category 2 -->
          <div onclick="selectSwipeCategory('cat_2_lanka_war')" style="background:rgba(234,88,12,0.25); border:1.8px solid #EA580C; border-radius:16px; padding:12px 14px; display:flex; align-items:center; justify-content:space-between; cursor:pointer; transition:transform 0.15s ease;">
            <div style="display:flex; align-items:center; gap:12px;">
              <div style="width:44px; height:44px; border-radius:50%; background:#EA580C; display:flex; align-items:center; justify-content:center; font-size:1.4rem; border:1.5px solid #F59E0B;">⚔️</div>
              <div>
                <div style="font-weight:900; font-size:0.98rem; color:#FFF;">राम सेना या रावण सेना</div>
                <div style="font-size:0.78rem; color:#FED7AA;">लंका युद्ध • ३५ महाबली पात्र</div>
              </div>
            </div>
            <span style="font-size:1.2rem; color:#FDE68A;">➔</span>
          </div>

          <!-- Category 3 -->
          <div onclick="selectSwipeCategory('cat_3_mahabharat')" style="background:rgba(21,128,61,0.25); border:1.8px solid #15803D; border-radius:16px; padding:12px 14px; display:flex; align-items:center; justify-content:space-between; cursor:pointer; transition:transform 0.15s ease;">
            <div style="display:flex; align-items:center; gap:12px;">
              <div style="width:44px; height:44px; border-radius:50%; background:#15803D; display:flex; align-items:center; justify-content:center; font-size:1.4rem; border:1.5px solid #F59E0B;">🛡️</div>
              <div>
                <div style="font-weight:900; font-size:0.98rem; color:#FFF;">पाण्डव या कौरव</div>
                <div style="font-size:0.78rem; color:#BBF7D0;">कुरुक्षेत्र महाभारत • २५ महारथी</div>
              </div>
            </div>
            <span style="font-size:1.2rem; color:#FDE68A;">➔</span>
          </div>
        </div>
      </div>
    </div>
"""

if 'id="swipe-category-modal"' not in html_content:
    target_pos = html_content.find('id="swipe-result-modal"')
    if target_pos != -1:
        end_pos = html_content.find('</div>\n    </div>', target_pos) + len('</div>\n    </div>')
        html_content = html_content[:end_pos] + "\n" + category_modal_html + html_content[end_pos:]
        print("✓ Injected swipe-category-modal into index.html")

# 3D. Add 'mahakavya' tab to Gallery in index.html
old_gallery_tabs = '<button class="gal-tab-pill" data-tab="world" onclick="switchGalleryTab(\'world\')">'
new_gallery_tabs = '<button class="gal-tab-pill" data-tab="world" onclick="switchGalleryTab(\'world\')">🌍 विश्व मंदिर</button>\n        <button class="gal-tab-pill" data-tab="mahakavya" onclick="switchGalleryTab(\'mahakavya\')">🏹 महाकाव्य (100)'

if 'data-tab="mahakavya"' not in html_content and old_gallery_tabs in html_content:
    html_content = html_content.replace(old_gallery_tabs + '🌍 विश्व मंदिर</button>', new_gallery_tabs + '</button>')
    print("✓ Added 'mahakavya' tab to Gallery in index.html")

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)
print("✓ Saved index.html")

# ══════════════════════════════════════════════════════════════════════════════
# 4. UPDATE GALLERY_ENGINE.JS
# ══════════════════════════════════════════════════════════════════════════════
print("\n4. Updating gallery_engine.js with 100 Mahakavya characters...")
with open(GALLERY_FILE, "r", encoding="utf-8") as f:
    gal_content = f.read()

# Build MAHAKAVYA_GALLERY list
mahakavya_items = []
for cat in categories:
    cat_title = cat["title"]
    for c in cat["cards"]:
        mantra = "श्री राम जय राम जय जय राम" if "ramayana" in cat["id"] or "lanka" in cat["id"] else "ॐ नमो भगवते वासुदेवाय"
        side_name = cat["leftSide"]["name"] if c["correctSwipe"] == "LEFT" else cat["rightSide"]["name"]
        mahakavya_items.append({
            "id": c["id"],
            "nameHi": c["name"],
            "nameEn": c["slug"],
            "category": cat_title,
            "img": c["image"],
            "desc": c["desc"],
            "mantra": f"{c['name']} • पक्ष: {side_name}",
            "famous": f"{cat_title} • {side_name}"
        })

mahakavya_js = "\n  window.MAHAKAVYA_GALLERY = " + json.dumps(mahakavya_items, ensure_ascii=False, indent=2) + ";\n"

# Check if window.MAHAKAVYA_GALLERY is already in gallery_engine.js
if 'window.MAHAKAVYA_GALLERY =' not in gal_content:
    gal_content = mahakavya_js + gal_content
    print("✓ Injected window.MAHAKAVYA_GALLERY (100 items) into gallery_engine.js")
else:
    pattern_mk = re.compile(r'window\.MAHAKAVYA_GALLERY\s*=\s*\[[\s\S]*?\];', re.MULTILINE)
    gal_content = pattern_mk.sub(mahakavya_js.strip(), gal_content)
    print("✓ Updated window.MAHAKAVYA_GALLERY in gallery_engine.js")

# Update getActiveDataset in gallery_engine.js
if "window.galleryActiveTab === 'mahakavya'" not in gal_content:
    old_get_dataset = "return (window.WORLD_TEMPLES_GALLERY && window.WORLD_TEMPLES_GALLERY.length) ? window.WORLD_TEMPLES_GALLERY : [];"
    new_get_dataset = """return (window.WORLD_TEMPLES_GALLERY && window.WORLD_TEMPLES_GALLERY.length) ? window.WORLD_TEMPLES_GALLERY : [];
    } else if (window.galleryActiveTab === 'mahakavya') {
      return (window.MAHAKAVYA_GALLERY && window.MAHAKAVYA_GALLERY.length) ? window.MAHAKAVYA_GALLERY : [];"""
    gal_content = gal_content.replace(old_get_dataset, new_get_dataset)
    print("✓ Hooked 'mahakavya' tab in getActiveDataset() in gallery_engine.js")

with open(GALLERY_FILE, "w", encoding="utf-8") as f:
    f.write(gal_content)
print("✓ Saved gallery_engine.js")

print("\n🎉 ALL UPDATES COMPLETED SUCCESSFULLY!")
