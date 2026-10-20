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
CSS_FILE = os.path.join(BASE_DIR, "epic_games.css")

print("1. Loading swipe_game_data.json...")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    swipe_data = json.load(f)

categories = swipe_data["categories"]
print(f"Loaded {len(categories)} categories with {[len(c['cards']) for c in categories]} cards.")

# ══════════════════════════════════════════════════════════════════════════════
# 1. PREPARE JAVASCRIPT CATEGORIES & UI STRINGS
# ══════════════════════════════════════════════════════════════════════════════
cat_dict = {}
for cat in categories:
    cat_dict[cat["id"]] = cat

# Aliases
cat_dict["ayodhya_mithila"] = cat_dict["cat_1_ramayana"]
cat_dict["lanka_war"] = cat_dict["cat_2_lanka_war"]
cat_dict["pandav_kaurav"] = cat_dict["cat_3_mahabharat"]

swipe_categories_js = "  var SWIPE_CATEGORIES = " + json.dumps(cat_dict, ensure_ascii=False, indent=2) + ";\n"

swipe_ui_i18n_js = """  var SWIPE_UI_I18N = {
    en: {
      chooseLanguage: "Choose Game Language",
      chooseCategory: "Choose Category",
      play: "Play",
      correct: "Correct Side! +50 🪙",
      wrong: "Wrong Side!",
      cardsLeft: "Cards Left",
      score: "Score",
      charReview: "Character Review",
      replay: "Play Again",
      nextCategory: "Next Category",
      close: "Close"
    },
    hi: {
      chooseLanguage: "खेल की भाषा चुनें",
      chooseCategory: "श्रेणी चुनें",
      play: "खेलें",
      correct: "सही पक्ष! +50 🪙",
      wrong: "गलत पक्ष!",
      cardsLeft: "शेष कार्ड",
      score: "स्कोर",
      charReview: "चरित्र समीक्षा",
      replay: "पुनः खेलें",
      nextCategory: "अगली श्रेणी",
      close: "बंद करें"
    },
    te: {
      chooseLanguage: "ఆట భాషను ఎంచుకోండి",
      chooseCategory: "వర్గాన్ని ఎంచుకోండి",
      play: "ఆడండి",
      correct: "సరైన వైపు! +50 🪙",
      wrong: "తప్పు వైపు!",
      cardsLeft: "మిగిలిన కార్డులు",
      score: "స్కోరు",
      charReview: "పాత్రల సమీక్ష",
      replay: "మళ్లీ ఆడండి",
      nextCategory: "తదుపరి వర్గం",
      close: "మూసివేయి"
    }
  };
"""

# ══════════════════════════════════════════════════════════════════════════════
# 2. UPDATE EPIC_GAMES_ENGINE.JS
# ══════════════════════════════════════════════════════════════════════════════
print("\n2. Updating epic_games_engine.js...")
with open(ENGINE_FILE, "r", encoding="utf-8") as f:
    engine_content = f.read()

# Replace SWIPE_CATEGORIES block
pattern_categories = re.compile(r'  var SWIPE_CATEGORIES = \{[\s\S]*?\n  \};\n', re.MULTILINE)
if pattern_categories.search(engine_content):
    engine_content = pattern_categories.sub(swipe_categories_js + "\n" + swipe_ui_i18n_js, engine_content, count=1)
    print("✓ Replaced SWIPE_CATEGORIES & added SWIPE_UI_I18N in epic_games_engine.js")
else:
    print("⚠ Pattern for SWIPE_CATEGORIES not matched, searching fallback...")

# Complete Swipe Engine Logic with Image 1 Launcher Screen, Carousel, Language Highlights & Multilingual Base
new_swipe_launcher_logic = """
  // ══════════════════════════════════════════════════════════════════════════════
  // 🏹 SWIPE GAME LAUNCHER SCREEN (Exact Match to Image 1)
  // ══════════════════════════════════════════════════════════════════════════════
  epicGameState.currentLanguage = localStorage.getItem('swipe_game_lang') || 'en';
  epicGameState.selectedLauncherCategory = 'cat_1_ramayana';

  var LAUNCHER_CATEGORY_LIST = ['cat_1_ramayana', 'cat_2_lanka_war', 'cat_3_mahabharat'];

  window.openSwipeGame = function(categoryKey) {
    if (categoryKey && SWIPE_CATEGORIES[categoryKey]) {
      epicGameState.selectedLauncherCategory = SWIPE_CATEGORIES[categoryKey].id;
    }
    hideBottomNavForGames();

    var launcher = document.getElementById('swipe-launcher-screen');
    if (launcher) {
      launcher.style.display = 'flex';
      launcher.classList.add('active');
    }

    // Hide gameplay arenas while in launcher
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'none';
    var rev = document.getElementById('swipe-review-arena');
    if (rev) rev.style.display = 'none';

    // Synchronize UI
    updateLauncherLanguageUI();
    renderLauncherCarousel();
  };

  window.closeSwipeLauncher = function() {
    var launcher = document.getElementById('swipe-launcher-screen');
    if (launcher) {
      launcher.style.display = 'none';
      launcher.classList.remove('active');
    }
    restoreBottomNavIfExited();
  };

  window.selectSwipeLanguage = function(langCode) {
    if (!['en', 'hi', 'te'].includes(langCode)) langCode = 'en';
    epicGameState.currentLanguage = langCode;
    localStorage.setItem('swipe_game_lang', langCode);

    playSound('click');
    if (navigator.vibrate) navigator.vibrate(20);

    updateLauncherLanguageUI();
    renderLauncherCarousel();
  };

  function updateLauncherLanguageUI() {
    var lang = epicGameState.currentLanguage || 'en';
    var i18n = SWIPE_UI_I18N[lang] || SWIPE_UI_I18N.en;

    // Update active highlight and wings on language cards
    document.querySelectorAll('.swipe-lang-card').forEach(function(card) {
      var cardLang = card.getAttribute('data-lang');
      if (cardLang === lang) {
        card.classList.add('active');
      } else {
        card.classList.remove('active');
      }
    });

    // Update ribbon texts
    var langRibbon = document.getElementById('swipe-launch-lang-ribbon-text');
    if (langRibbon) langRibbon.textContent = i18n.chooseLanguage;

    var catHeader = document.getElementById('swipe-launch-cat-header-text');
    if (catHeader) catHeader.textContent = i18n.chooseCategory;

    var playText = document.getElementById('swipe-launch-play-btn-text');
    if (playText) playText.textContent = i18n.play;

    // Update coins
    var coinVals = document.querySelectorAll('.epic-coins-val');
    coinVals.forEach(function(el) {
      el.textContent = (epicGameState.coins >= 1000) ? Math.floor(epicGameState.coins / 1000) + 'K' : epicGameState.coins;
    });
  }

  function renderLauncherCarousel() {
    var lang = epicGameState.currentLanguage || 'en';
    var currentCat = epicGameState.selectedLauncherCategory || 'cat_1_ramayana';

    // Update Category VS texts
    LAUNCHER_CATEGORY_LIST.forEach(function(cid, idx) {
      var cat = SWIPE_CATEGORIES[cid];
      if (!cat) return;
      var num = idx + 1;
      var leftEl = document.getElementById('vs-cat-' + num + '-left');
      var rightEl = document.getElementById('vs-cat-' + num + '-right');
      if (leftEl) {
        leftEl.textContent = (lang === 'te' && cat.leftSide.name_te) ? cat.leftSide.name_te : ((lang === 'en' && cat.leftSide.name_en) ? cat.leftSide.name_en : (cat.leftSide.name_hi || cat.leftSide.name));
      }
      if (rightEl) {
        rightEl.textContent = (lang === 'te' && cat.rightSide.name_te) ? cat.rightSide.name_te : ((lang === 'en' && cat.rightSide.name_en) ? cat.rightSide.name_en : (cat.rightSide.name_hi || cat.rightSide.name));
      }
    });

    // Update 3D carousel position & active classes
    var track = document.getElementById('swipe-cat-carousel-track');
    var cards = document.querySelectorAll('.swipe-cat-slide-card');
    var activeIdx = LAUNCHER_CATEGORY_LIST.indexOf(currentCat);
    if (activeIdx === -1) activeIdx = 0;

    cards.forEach(function(card, idx) {
      card.classList.remove('active', 'peek-left', 'peek-right');
      if (idx === activeIdx) {
        card.classList.add('active');
      } else if (idx < activeIdx) {
        card.classList.add('peek-left');
      } else {
        card.classList.add('peek-right');
      }
    });
  }

  window.selectSwipeCategory = function(catId) {
    if (epicGameState.selectedLauncherCategory === catId) return;
    epicGameState.selectedLauncherCategory = catId;
    playSound('click');
    if (navigator.vibrate) navigator.vibrate(15);
    renderLauncherCarousel();
  };

  window.nextSwipeCategory = function() {
    var currIdx = LAUNCHER_CATEGORY_LIST.indexOf(epicGameState.selectedLauncherCategory);
    var nextIdx = (currIdx + 1) % LAUNCHER_CATEGORY_LIST.length;
    selectSwipeCategory(LAUNCHER_CATEGORY_LIST[nextIdx]);
  };

  window.prevSwipeCategory = function() {
    var currIdx = LAUNCHER_CATEGORY_LIST.indexOf(epicGameState.selectedLauncherCategory);
    var prevIdx = (currIdx - 1 + LAUNCHER_CATEGORY_LIST.length) % LAUNCHER_CATEGORY_LIST.length;
    selectSwipeCategory(LAUNCHER_CATEGORY_LIST[prevIdx]);
  };

  // Add Touch Gestures for Category Carousel Slider
  (function initCarouselSwipeGestures() {
    var startX = 0;
    var startY = 0;
    var isMoving = false;

    document.addEventListener('DOMContentLoaded', function() {
      var stage = document.getElementById('swipe-cat-carousel-stage');
      if (!stage) return;

      stage.addEventListener('touchstart', function(e) {
        if (!e.touches || e.touches.length === 0) return;
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        isMoving = true;
      }, { passive: true });

      stage.addEventListener('touchend', function(e) {
        if (!isMoving || !e.changedTouches || e.changedTouches.length === 0) return;
        isMoving = false;
        var diffX = e.changedTouches[0].clientX - startX;
        var diffY = e.changedTouches[0].clientY - startY;

        if (Math.abs(diffX) > 40 && Math.abs(diffX) > Math.abs(diffY)) {
          if (diffX < 0) {
            window.nextSwipeCategory();
          } else {
            window.prevSwipeCategory();
          }
        }
      }, { passive: true });
    });
  })();

  window.startSwipeGameFromLauncher = function() {
    playSound('select');
    if (navigator.vibrate) navigator.vibrate(30);

    // Close Launcher
    var launcher = document.getElementById('swipe-launcher-screen');
    if (launcher) {
      launcher.style.display = 'none';
      launcher.classList.remove('active');
    }

    // Open Arena
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'flex';
    hideBottomNavForGames();

    // Start Game with chosen category and chosen language
    initSwipeGame(epicGameState.selectedLauncherCategory, epicGameState.currentLanguage);
  };

  // ══════════════════════════════════════════════════════════════════════════════
  // 2. SWIPE GAME LOGIC & MULTILINGUAL BASE PHYSICS
  // ══════════════════════════════════════════════════════════════════════════════
  var activeCardEl = null;
  var isDragging = false;
  var startX = 0;
  var startY = 0;
  var currentX = 0;
  var currentY = 0;

  function initSwipeGame(categoryKey, langCode) {
    categoryKey = categoryKey || epicGameState.selectedLauncherCategory || 'cat_1_ramayana';
    var cat = SWIPE_CATEGORIES[categoryKey] || SWIPE_CATEGORIES.cat_1_ramayana;
    epicGameState.currentCategory = cat.id;

    var lang = langCode || epicGameState.currentLanguage || 'en';
    epicGameState.currentLanguage = lang;

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

    // Multilingual Category Title & Instructions
    var titleText = (lang === 'te' && cat.title_te) ? cat.title_te : ((lang === 'en' && cat.title_en) ? cat.title_en : (cat.title_hi || cat.title));
    var instText = (lang === 'te' && cat.instruction_te) ? cat.instruction_te : ((lang === 'en' && cat.instruction_en) ? cat.instruction_en : (cat.instruction_hi || cat.instruction));
    var leftName = (lang === 'te' && cat.leftSide.name_te) ? cat.leftSide.name_te : ((lang === 'en' && cat.leftSide.name_en) ? cat.leftSide.name_en : (cat.leftSide.name_hi || cat.leftSide.name));
    var rightName = (lang === 'te' && cat.rightSide.name_te) ? cat.rightSide.name_te : ((lang === 'en' && cat.rightSide.name_en) ? cat.rightSide.name_en : (cat.rightSide.name_hi || cat.rightSide.name));

    // Update Arena labels & header
    var titleEl = document.getElementById('swipe-cat-title');
    if (titleEl) titleEl.textContent = titleText;

    var instEl = document.getElementById('swipe-instruction');
    if (instEl) instEl.textContent = instText;

    var leftLabel = document.getElementById('swipe-left-portal-label');
    if (leftLabel) leftLabel.textContent = leftName;

    var rightLabel = document.getElementById('swipe-right-portal-label');
    if (rightLabel) rightLabel.textContent = rightName;

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
      btnLeft.textContent = '⟵ ' + leftName;
      btnLeft.style.background = cat.leftSide.bgColor;
    }
    var btnRight = document.getElementById('swipe-btn-right');
    if (btnRight) {
      btnRight.textContent = rightName + ' ⟶';
      btnRight.style.background = cat.rightSide.bgColor;
    }

    renderCurrentCard();
  }

  function renderCurrentCard() {
    var stage = document.getElementById('swipe-card-deck');
    if (!stage) return;

    if (epicGameState.currentIndex >= epicGameState.deck.length) {
      setTimeout(showCharacterReviewScreen, 400);
      return;
    }

    var char = epicGameState.deck[epicGameState.currentIndex];
    var lang = epicGameState.currentLanguage || 'en';
    var charName = (lang === 'te' && char.name_te) ? char.name_te : ((lang === 'en' && char.name_en) ? char.name_en : (char.name_hi || char.name));

    stage.innerHTML = `
      <div class="swipe-card-underlay swipe-card-underlay-2"></div>
      <div class="swipe-card-underlay swipe-card-underlay-1"></div>
      
      <div class="swipe-main-card" id="swipe-active-card">
        <div class="swipe-card-jewel-top"></div>
        <div class="swipe-card-jewel-left"></div>
        <div class="swipe-card-jewel-right"></div>
        <img src="${char.image}" alt="${charName}" class="swipe-char-portrait" onerror="this.src='assets/games/char_sunaina.jpg';">
        <div class="swipe-char-name-bar">${charName}</div>
      </div>
    `;

    activeCardEl = document.getElementById('swipe-active-card');
    if (activeCardEl) {
      attachCardSwipeListeners(activeCardEl);
    }
  }

  function showCharacterReviewScreen() {
    hideBottomNavForGames();
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'none';

    var rev = document.getElementById('swipe-review-arena');
    if (!rev) return;
    rev.style.display = 'flex';

    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var characters = cat.cards || [];
    var lang = epicGameState.currentLanguage || 'en';

    // Render tokens list in bottom rail
    var rail = document.getElementById('swipe-review-tokens-rail');
    if (rail) {
      rail.innerHTML = '';
      characters.forEach(function (c, idx) {
        var token = document.createElement('div');
        token.className = 'swipe-char-token' + (idx === 0 ? ' active-token' : '');
        var tokenName = (lang === 'te' && c.name_te) ? c.name_te : ((lang === 'en' && c.name_en) ? c.name_en : (c.name_hi || c.name));
        token.innerHTML = `
          <div class="swipe-token-circle">
            <img src="${c.image}" alt="${tokenName}" class="swipe-token-avatar" onerror="this.src='assets/games/char_sunaina.jpg';">
            <div class="swipe-token-check">✓</div>
          </div>
          <div class="swipe-token-label">${tokenName}</div>
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
    var lang = epicGameState.currentLanguage || 'en';
    var isLeft = char.correctSwipe === 'LEFT';
    var sideName = isLeft ? 
      ((lang === 'te' && cat.leftSide.name_te) ? cat.leftSide.name_te : ((lang === 'en' && cat.leftSide.name_en) ? cat.leftSide.name_en : cat.leftSide.name)) :
      ((lang === 'te' && cat.rightSide.name_te) ? cat.rightSide.name_te : ((lang === 'en' && cat.rightSide.name_en) ? cat.rightSide.name_en : cat.rightSide.name));
    var sideBg = isLeft ? cat.leftSide.bgColor : cat.rightSide.bgColor;

    var charName = (lang === 'te' && char.name_te) ? char.name_te : ((lang === 'en' && char.name_en) ? char.name_en : (char.name_hi || char.name));
    var charDesc = (lang === 'te' && char.desc_te) ? char.desc_te : ((lang === 'en' && char.desc_en) ? char.desc_en : (char.desc_hi || char.desc));

    card.innerHTML = `
      <div class="swipe-review-card">
        <div class="swipe-review-img-wrap">
          <img src="${char.image}" alt="${charName}" class="swipe-review-img" onerror="this.src='assets/games/char_sunaina.jpg';">
          <div class="swipe-review-team-badge" style="background:${sideBg}; color:#FFF;">${sideName}</div>
        </div>
        <div class="swipe-review-info-body">
          <div class="swipe-review-char-name">${charName}</div>
          <div class="swipe-review-divider"></div>
          <div class="swipe-review-char-desc">${charDesc}</div>
          <button class="swipe-review-network-btn" onclick="window.openCharacterNetworkModal('${char.id}')">📖 ${lang === 'te' ? 'వివరాలు' : (lang === 'en' ? 'Context' : 'महाकाव्य संदर्भ')}</button>
        </div>
      </div>
    `;
  }
"""

# Replace the existing swipe game logic in epic_games_engine.js
pattern_logic = re.compile(r'  // 2\. SWIPE GAME LOGIC & TOUCH PHYSICS[\s\S]*?function renderReviewCard\(char\) \{[\s\S]*?\n  \}', re.MULTILINE)
if pattern_logic.search(engine_content):
    engine_content = pattern_logic.sub(new_swipe_launcher_logic, engine_content, count=1)
    print("✓ Replaced Swipe logic with complete Launcher & Multilingual engine in epic_games_engine.js")
else:
    print("⚠ Pattern for swipe logic not matched directly, checking alternative replacement...")
    # Find start of // 2. SWIPE GAME LOGIC
    idx_start = engine_content.find("// 2. SWIPE GAME LOGIC")
    if idx_start != -1:
        idx_end = engine_content.find("// 4. RESULT / TRY AGAIN MODAL", idx_start)
        if idx_end != -1:
            engine_content = engine_content[:idx_start] + new_swipe_launcher_logic + "\n\n  " + engine_content[idx_end:]
            print("✓ Spliced Swipe Launcher logic into epic_games_engine.js")

with open(ENGINE_FILE, "w", encoding="utf-8") as f:
    f.write(engine_content)
print("✓ Saved epic_games_engine.js successfully.")
