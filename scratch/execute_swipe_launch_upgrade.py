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

print("=== STEP 1: Reading swipe_game_data.json ===")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    swipe_data = json.load(f)

categories = swipe_data["categories"]
print(f"Loaded {len(categories)} categories.")

cat_dict = {}
for cat in categories:
    cat_dict[cat["id"]] = cat

# Map aliases
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

swipe_launcher_and_game_logic = """
  // ══════════════════════════════════════════════════════════════════════════════
  // 🏹 SWIPE GAME LAUNCHER SCREEN (Exact Match to Image 1)
  // ══════════════════════════════════════════════════════════════════════════════
  epicGameState.currentLanguage = localStorage.getItem('swipe_game_lang') || 'en';
  epicGameState.selectedLauncherCategory = 'cat_1_ramayana';

  var LAUNCHER_CATEGORY_LIST = ['cat_1_ramayana', 'cat_2_lanka_war', 'cat_3_mahabharat'];

  window.openSwipeLauncher = function(categoryKey) {
    if (categoryKey && SWIPE_CATEGORIES[categoryKey]) {
      epicGameState.selectedLauncherCategory = SWIPE_CATEGORIES[categoryKey].id;
    }
    hideBottomNavForGames();

    var launcher = document.getElementById('swipe-launcher-screen');
    if (launcher) {
      launcher.style.display = 'flex';
      launcher.classList.add('active');
    }

    // Hide gameplay arena and review screen while in launcher
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'none';
    var rev = document.getElementById('swipe-review-arena');
    if (rev) rev.style.display = 'none';

    // Synchronize UI
    updateLauncherLanguageUI();
    renderLauncherCarousel();
  };

  window.openSwipeGame = function(categoryKey) {
    window.openSwipeLauncher(categoryKey);
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
    try {
      localStorage.setItem('swipe_game_lang', langCode);
    } catch(e) {}

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

    function attach() {
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
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', attach);
    } else {
      attach();
    }
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

    // Update Quick Desktop Accessibility Buttons
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

  function attachCardSwipeListeners(el) {
    el.addEventListener('mousedown', onDragStart);
    document.addEventListener('mousemove', onDragMove);
    document.addEventListener('mouseup', onDragEnd);

    el.addEventListener('touchstart', onDragStart, { passive: false });
    document.addEventListener('touchmove', onDragMove, { passive: false });
    document.addEventListener('touchend', onDragEnd);
  }

  function onDragStart(e) {
    if (!activeCardEl) return;
    isDragging = true;
    var point = e.touches ? e.touches[0] : e;
    startX = point.clientX;
    startY = point.clientY;
    currentX = startX;
    currentY = startY;
    activeCardEl.style.transition = 'none';
  }

  function onDragMove(e) {
    if (!isDragging || !activeCardEl) return;
    var point = e.touches ? e.touches[0] : e;
    currentX = point.clientX;
    currentY = point.clientY;

    var deltaX = currentX - startX;
    var deltaY = currentY - startY;
    var rotation = deltaX * 0.08;

    activeCardEl.style.transform = `translate(${deltaX}px, ${deltaY}px) rotate(${rotation}deg)`;

    // Visual portal feedback highlight
    var leftPortal = document.getElementById('swipe-portal-left');
    var rightPortal = document.getElementById('swipe-portal-right');

    if (deltaX < -50) {
      if (leftPortal) leftPortal.classList.add('portal-pulse-active');
      if (rightPortal) rightPortal.classList.remove('portal-pulse-active');
    } else if (deltaX > 50) {
      if (rightPortal) rightPortal.classList.add('portal-pulse-active');
      if (leftPortal) leftPortal.classList.remove('portal-pulse-active');
    } else {
      if (leftPortal) leftPortal.classList.remove('portal-pulse-active');
      if (rightPortal) rightPortal.classList.remove('portal-pulse-active');
    }
  }

  function onDragEnd() {
    if (!isDragging || !activeCardEl) return;
    isDragging = false;

    var leftPortal = document.getElementById('swipe-portal-left');
    var rightPortal = document.getElementById('swipe-portal-right');
    if (leftPortal) leftPortal.classList.remove('portal-pulse-active');
    if (rightPortal) rightPortal.classList.remove('portal-pulse-active');

    var deltaX = currentX - startX;
    var threshold = window.innerWidth * 0.22;

    if (deltaX < -threshold) {
      handleSwipeCommit('left');
    } else if (deltaX > threshold) {
      handleSwipeCommit('right');
    } else {
      // Snap back with spring animation
      activeCardEl.style.transition = 'transform 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
      activeCardEl.style.transform = 'translate(0px, 0px) rotate(0deg)';
    }
  }

  window.swipeCardManual = function(direction) {
    handleSwipeCommit(direction);
  };

  function handleSwipeCommit(direction) {
    if (!activeCardEl) return;
    var char = epicGameState.deck[epicGameState.currentIndex];
    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var lang = epicGameState.currentLanguage || 'en';
    var i18n = SWIPE_UI_I18N[lang] || SWIPE_UI_I18N.en;

    var isLeft = direction === 'left';
    var chosenSide = isLeft ? 'LEFT' : 'RIGHT';
    var isCorrect = (char.correctSwipe === chosenSide);

    // Animate Card out towards Portal
    var flyX = isLeft ? -window.innerWidth * 1.2 : window.innerWidth * 1.2;
    var flyY = 220;
    var flyRot = isLeft ? -45 : 45;

    activeCardEl.style.transition = 'transform 0.32s ease-in, opacity 0.28s ease-in';
    activeCardEl.style.transform = `translate(${flyX}px, ${flyY}px) rotate(${flyRot}deg) scale(0.65)`;
    activeCardEl.style.opacity = '0';

    setTimeout(function () {
      if (isCorrect) {
        playSound('correct');
        epicGameState.correctCount++;
        addCoins(50);

        if (isLeft) {
          epicGameState.ayodhyaScore++;
          var sEl = document.getElementById('swipe-left-score');
          if (sEl) sEl.textContent = epicGameState.ayodhyaScore;
        } else {
          epicGameState.mithilaScore++;
          var sEl = document.getElementById('swipe-right-score');
          if (sEl) sEl.textContent = epicGameState.mithilaScore;
        }

        showCoinToast(i18n.correct);
      } else {
        playSound('wrong');
        showCoinToast(i18n.wrong);
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

  function showCoinToast(msg) {
    var toast = document.createElement('div');
    toast.textContent = msg;
    toast.style.position = 'fixed';
    toast.style.top = '40%';
    toast.style.left = '50%';
    toast.style.transform = 'translate(-50%, -50%)';
    toast.style.background = 'rgba(26, 11, 46, 0.9)';
    toast.style.color = '#FDE68A';
    toast.style.border = '1.5px solid #F59E0B';
    toast.style.borderRadius = '16px';
    toast.style.padding = '6px 16px';
    toast.style.fontSize = '1.1rem';
    toast.style.fontWeight = '900';
    toast.style.zIndex = '35000';
    toast.style.pointerEvents = 'none';
    toast.style.boxShadow = '0 6px 20px rgba(0,0,0,0.5)';
    toast.style.animation = 'coinPop 0.8s ease forwards';
    document.body.appendChild(toast);

    setTimeout(function () {
      if (toast.parentNode) toast.parentNode.removeChild(toast);
    }, 850);
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
      ((lang === 'te' && cat.leftSide.name_te) ? cat.leftSide.name_te : ((lang === 'en' && cat.leftSide.name_en) ? cat.leftSide.name_en : (cat.leftSide.name_hi || cat.leftSide.name))) :
      ((lang === 'te' && cat.rightSide.name_te) ? cat.rightSide.name_te : ((lang === 'en' && cat.rightSide.name_en) ? cat.rightSide.name_en : (cat.rightSide.name_hi || cat.rightSide.name)));
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

print("\n=== STEP 2: Updating epic_games_engine.js ===")
with open(ENGINE_FILE, "r", encoding="utf-8") as f:
    engine_content = f.read()

marker_start = "  // 1. SWIPE GAME: DATASETS"
marker_mid = "  // ── Bottom Navigation Bar Management for Epic Games ──"
marker_rev_start = "  // 3. CHARACTER REVIEW SCREEN"
marker_result = "  // 4. RESULT / TRY AGAIN MODAL"

idx_start = engine_content.find(marker_start)
idx_mid = engine_content.find(marker_mid)
idx_result = engine_content.find(marker_result)

if idx_start != -1 and idx_mid != -1 and idx_result != -1:
    print(f"Found markers: idx_start={idx_start}, idx_mid={idx_mid}, idx_result={idx_result}")
    
    # We replace from idx_start to idx_mid with swipe_categories_js + swipe_ui_i18n_js + swipe_launcher_and_game_logic
    # Then we keep from idx_mid (the bottom nav logic) until marker_rev_start (or replace from marker_rev_start to idx_result with empty since review is inside our new block)
    
    idx_rev_start = engine_content.find(marker_rev_start, idx_mid)
    if idx_rev_start != -1:
        bottom_nav_block = engine_content[idx_mid:idx_rev_start]
    else:
        bottom_nav_block = engine_content[idx_mid:idx_result]

    new_full_swipe_section = (
        marker_start + "\n" +
        swipe_categories_js + "\n" +
        swipe_ui_i18n_js + "\n" +
        swipe_launcher_and_game_logic + "\n\n" +
        bottom_nav_block + "\n"
    )

    new_engine_content = engine_content[:idx_start] + new_full_swipe_section + engine_content[idx_result:]
    with open(ENGINE_FILE, "w", encoding="utf-8") as f:
        f.write(new_engine_content)
    print("✓ Successfully replaced Swipe game & launcher module in epic_games_engine.js")
else:
    print(f"ERROR: Could not locate all markers: {idx_start}, {idx_mid}, {idx_result}")

print("\n=== STEP 3: Injecting Launcher HTML into index.html ===")
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

# Launcher HTML matching Image 1 exactly
launcher_html = """    <!-- ══════════ 🏹 SWIPE GAME LAUNCHER SCREEN (Exact Match to Image 1) ══════════ -->
    <div id="swipe-launcher-screen" class="swipe-launcher-screen" style="display:none;">
      <!-- Vedic Temple Background -->
      <img src="assets/games/swipe_launcher_bg.jpg" class="swipe-launcher-bg-img" alt="Temple Background" onerror="this.src='assets/games/bg_vedic_temple.jpg';">
      <div class="swipe-launcher-overlay"></div>

      <!-- Content Container -->
      <div class="swipe-launcher-content">
        <!-- Top Bar -->
        <div class="swipe-launch-topbar">
          <button class="swipe-launch-back-btn" onclick="closeSwipeLauncher()" title="Back">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          </button>
          
          <div class="swipe-launch-coins-badge">
            <span class="launch-coin-icon">🪙</span>
            <span class="launch-coin-amount epic-coins-val">1K</span>
          </div>
        </div>

        <!-- Main Title "Swipe" -->
        <div class="swipe-launch-title-wrap">
          <h1 class="swipe-launch-title">Swipe</h1>
        </div>

        <!-- Language Selection Section -->
        <div class="swipe-launch-section swipe-launch-lang-section">
          <!-- Ribbon Banner -->
          <div class="swipe-launch-ribbon">
            <div class="ribbon-tail-left"></div>
            <div class="ribbon-body">
              <span id="swipe-launch-lang-ribbon-text">Choose Game Language</span>
            </div>
            <div class="ribbon-tail-right"></div>
            <div class="ribbon-gem-bottom">
              <img src="assets/games/gem_blue.svg" alt="Gem" class="ribbon-gem-icon">
            </div>
          </div>

          <!-- Language Cards Grid -->
          <div class="swipe-lang-cards-grid">
            <!-- Telugu Card -->
            <div class="swipe-lang-card" data-lang="te" onclick="selectSwipeLanguage('te')">
              <div class="lang-wing-wrap wing-left">
                <img src="assets/games/wing_gold_left.svg" alt="Wing" class="lang-wing-img">
              </div>
              <div class="lang-card-inner">
                <div class="lang-gem-top"><img src="assets/games/gem_blue.svg" class="gem-micro"></div>
                <div class="lang-gem-bottom"><img src="assets/games/gem_blue.svg" class="gem-micro"></div>
                <div class="lang-gem-left"><img src="assets/games/gem_green.svg" class="gem-micro"></div>
                <div class="lang-gem-right"><img src="assets/games/gem_green.svg" class="gem-micro"></div>
                <span class="lang-card-text font-telugu">తెలుగు</span>
              </div>
              <div class="lang-wing-wrap wing-right">
                <img src="assets/games/wing_gold_right.svg" alt="Wing" class="lang-wing-img">
              </div>
            </div>

            <!-- Hindi Card -->
            <div class="swipe-lang-card" data-lang="hi" onclick="selectSwipeLanguage('hi')">
              <div class="lang-wing-wrap wing-left">
                <img src="assets/games/wing_gold_left.svg" alt="Wing" class="lang-wing-img">
              </div>
              <div class="lang-card-inner">
                <div class="lang-gem-top"><img src="assets/games/gem_blue.svg" class="gem-micro"></div>
                <div class="lang-gem-bottom"><img src="assets/games/gem_blue.svg" class="gem-micro"></div>
                <div class="lang-gem-left"><img src="assets/games/gem_green.svg" class="gem-micro"></div>
                <div class="lang-gem-right"><img src="assets/games/gem_green.svg" class="gem-micro"></div>
                <span class="lang-card-text font-hindi">हिन्दी</span>
              </div>
              <div class="lang-wing-wrap wing-right">
                <img src="assets/games/wing_gold_right.svg" alt="Wing" class="lang-wing-img">
              </div>
            </div>

            <!-- English Card -->
            <div class="swipe-lang-card active" data-lang="en" onclick="selectSwipeLanguage('en')">
              <div class="lang-wing-wrap wing-left">
                <img src="assets/games/wing_gold_left.svg" alt="Wing" class="lang-wing-img">
              </div>
              <div class="lang-card-inner">
                <div class="lang-gem-top"><img src="assets/games/gem_blue.svg" class="gem-micro"></div>
                <div class="lang-gem-bottom"><img src="assets/games/gem_blue.svg" class="gem-micro"></div>
                <div class="lang-gem-left"><img src="assets/games/gem_green.svg" class="gem-micro"></div>
                <div class="lang-gem-right"><img src="assets/games/gem_green.svg" class="gem-micro"></div>
                <span class="lang-card-text font-english">English</span>
              </div>
              <div class="lang-wing-wrap wing-right">
                <img src="assets/games/wing_gold_right.svg" alt="Wing" class="lang-wing-img">
              </div>
            </div>
          </div>
        </div>

        <!-- Category Header -->
        <div class="swipe-launch-cat-header">
          <div class="cat-header-gem"><img src="assets/games/gem_blue.svg" class="gem-micro"></div>
          <h2 class="swipe-launch-cat-title" id="swipe-launch-cat-header-text">Choose Category</h2>
          <div class="cat-header-gem"><img src="assets/games/gem_blue.svg" class="gem-micro"></div>
        </div>

        <!-- 3D Category Carousel / Slider Stage -->
        <div class="swipe-cat-carousel-stage" id="swipe-cat-carousel-stage">
          <!-- Navigation Arrow Left -->
          <button class="swipe-carousel-arrow arrow-left" onclick="prevSwipeCategory()" aria-label="Previous Category">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
          </button>

          <!-- Cards Track -->
          <div class="swipe-cat-carousel-track" id="swipe-cat-carousel-track">
            <!-- Card 1: Ayodhya vs Mithila -->
            <div class="swipe-cat-slide-card active" id="cat-card-1" onclick="selectSwipeCategory('cat_1_ramayana')">
              <div class="cat-card-frame">
                <!-- Gemstones -->
                <div class="cat-gem-crown"><img src="assets/games/gem_blue.svg" class="gem-card"></div>
                <div class="cat-gem-side left"><img src="assets/games/gem_green.svg" class="gem-card"></div>
                <div class="cat-gem-side right"><img src="assets/games/gem_green.svg" class="gem-card"></div>

                <!-- Split Image Art -->
                <div class="cat-card-art-wrap">
                  <img src="assets/games/cat_split_ayodhya.jpg" alt="Ayodhya vs Mithila" class="cat-card-split-img" onerror="this.src='assets/games/portal_ayodhya.jpg';">
                  <div class="cat-card-divider-line"></div>
                </div>

                <!-- Bottom Banner Ribbon (Left vs Right) -->
                <div class="cat-card-bottom-ribbon">
                  <span class="cat-side-name" id="vs-cat-1-left">Ayodhya</span>
                  <div class="cat-vs-badge">
                    <span class="vs-text">VS</span>
                  </div>
                  <span class="cat-side-name" id="vs-cat-1-right">Mithila</span>
                </div>
              </div>
            </div>

            <!-- Card 2: Lanka War (Rama vs Ravana) -->
            <div class="swipe-cat-slide-card peek-right" id="cat-card-2" onclick="selectSwipeCategory('cat_2_lanka_war')">
              <div class="cat-card-frame">
                <div class="cat-gem-crown"><img src="assets/games/gem_blue.svg" class="gem-card"></div>
                <div class="cat-gem-side left"><img src="assets/games/gem_green.svg" class="gem-card"></div>
                <div class="cat-gem-side right"><img src="assets/games/gem_green.svg" class="gem-card"></div>

                <div class="cat-card-art-wrap">
                  <img src="assets/games/cat_split_lanka.jpg" alt="Rama vs Ravana" class="cat-card-split-img" onerror="this.src='assets/games/portal_ayodhya.jpg';">
                  <div class="cat-card-divider-line"></div>
                </div>

                <div class="cat-card-bottom-ribbon">
                  <span class="cat-side-name" id="vs-cat-2-left">Rama Army</span>
                  <div class="cat-vs-badge">
                    <span class="vs-text">VS</span>
                  </div>
                  <span class="cat-side-name" id="vs-cat-2-right">Ravana Army</span>
                </div>
              </div>
            </div>

            <!-- Card 3: Mahabharata (Pandavas vs Kauravas) -->
            <div class="swipe-cat-slide-card peek-right" id="cat-card-3" onclick="selectSwipeCategory('cat_3_mahabharat')">
              <div class="cat-card-frame">
                <div class="cat-gem-crown"><img src="assets/games/gem_blue.svg" class="gem-card"></div>
                <div class="cat-gem-side left"><img src="assets/games/gem_green.svg" class="gem-card"></div>
                <div class="cat-gem-side right"><img src="assets/games/gem_green.svg" class="gem-card"></div>

                <div class="cat-card-art-wrap">
                  <img src="assets/games/cat_split_mahabharata.jpg" alt="Pandavas vs Kauravas" class="cat-card-split-img" onerror="this.src='assets/games/portal_ayodhya.jpg';">
                  <div class="cat-card-divider-line"></div>
                </div>

                <div class="cat-card-bottom-ribbon">
                  <span class="cat-side-name" id="vs-cat-3-left">Pandavas</span>
                  <div class="cat-vs-badge">
                    <span class="vs-text">VS</span>
                  </div>
                  <span class="cat-side-name" id="vs-cat-3-right">Kauravas</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Navigation Arrow Right -->
          <button class="swipe-carousel-arrow arrow-right" onclick="nextSwipeCategory()" aria-label="Next Category">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>
          </button>
        </div>

        <!-- Big Royal-Blue Play Button with Golden Wings -->
        <div class="swipe-launch-play-container">
          <div class="swipe-play-wing play-wing-left">
            <img src="assets/games/wing_gold_left.svg" alt="Golden Wing" class="play-wing-img">
          </div>

          <button class="swipe-launch-play-btn" onclick="startSwipeGameFromLauncher()">
            <!-- Top & Bottom Gold Filigree Jewels -->
            <div class="play-btn-crown-top"><img src="assets/games/gem_blue.svg" class="gem-micro"></div>
            <div class="play-btn-crown-bottom"><img src="assets/games/gem_blue.svg" class="gem-micro"></div>
            
            <span class="play-triangle-icon">▶</span>
            <span class="play-text" id="swipe-launch-play-btn-text">Play</span>
          </button>

          <div class="swipe-play-wing play-wing-right">
            <img src="assets/games/wing_gold_right.svg" alt="Golden Wing" class="play-wing-img">
          </div>
        </div>
      </div>
    </div>\n\n"""

# Check if launcher already in html
if "swipe-launcher-screen" not in html_content:
    target_marker = '    <!-- ══════════ 🏹 SWIPE GAME ARENA (The Exact Video Screen) ══════════ -->'
    if target_marker in html_content:
        html_content = html_content.replace(target_marker, launcher_html + target_marker, 1)
        print("✓ Injected swipe-launcher-screen right above swipe-arena in index.html")
    else:
        # Fallback to before <div id="swipe-arena"
        target_arena = '<div id="swipe-arena"'
        idx_arena = html_content.find(target_arena)
        if idx_arena != -1:
            html_content = html_content[:idx_arena] + launcher_html + html_content[idx_arena:]
            print("✓ Injected swipe-launcher-screen before swipe-arena in index.html (fallback)")
        else:
            print("ERROR: Could not find swipe-arena in index.html")

# Update swipe-close-btn to return to launcher screen
html_content = html_content.replace('onclick="closeSwipeGame()"', 'onclick="openSwipeLauncher()"')
html_content = html_content.replace('onclick="openSwipeCategoryModal()"', 'onclick="openSwipeLauncher()"')
html_content = html_content.replace('class="swipe-lang-btn"', 'class="swipe-lang-btn" onclick="openSwipeLauncher()"')

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)
print("✓ Updated index.html successfully.")

print("\n=== STEP 4: Appending Swipe Launcher CSS to epic_games.css ===")
with open(CSS_FILE, "r", encoding="utf-8") as f:
    css_content = f.read()

launcher_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   🏹 SWIPE GAME LAUNCHER SCREEN (Exact Match to Image 1)
   ══════════════════════════════════════════════════════════════════════════════ */
.swipe-launcher-screen {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  z-index: 29999;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  user-select: none;
  touch-action: pan-y;
  overflow: hidden;
  background-color: #E6D2B5;
}

.swipe-launcher-bg-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 20%;
  z-index: 1;
}

.swipe-launcher-overlay {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 35%, rgba(255, 248, 230, 0.25) 0%, rgba(210, 160, 90, 0.45) 70%, rgba(80, 40, 10, 0.75) 100%);
  pointer-events: none;
  z-index: 2;
}

.swipe-launcher-content {
  position: relative;
  z-index: 10;
  width: 100%;
  max-width: 480px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: env(safe-area-inset-top, 12px) 16px env(safe-area-inset-bottom, 20px) 16px;
  box-sizing: border-box;
}

/* ── Top Bar ── */
.swipe-launch-topbar {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 6px;
}

.swipe-launch-back-btn {
  background: rgba(255, 255, 255, 0.85);
  border: 1.8px solid #D4AF37;
  color: #5D2E0C;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  transition: all 0.2s ease;
}

.swipe-launch-back-btn:active {
  transform: scale(0.92);
}

.swipe-launch-coins-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 50%, #FDE68A 100%);
  border: 2px solid #D4AF37;
  border-radius: 9999px;
  padding: 4px 14px 4px 10px;
  box-shadow: 0 4px 14px rgba(212, 175, 55, 0.35), inset 0 1px 2px rgba(255, 255, 255, 0.9);
}

.launch-coin-icon {
  font-size: 1.15rem;
  filter: drop-shadow(0 2px 4px rgba(217, 119, 6, 0.5));
}

.launch-coin-amount {
  font-family: 'Cinzel', serif, system-ui;
  font-size: 1.05rem;
  font-weight: 900;
  color: #451A03;
  letter-spacing: 0.5px;
}

/* ── Main Title "Swipe" ── */
.swipe-launch-title-wrap {
  margin-top: 2px;
  margin-bottom: 2px;
  text-align: center;
}

.swipe-launch-title {
  margin: 0;
  font-family: 'Cinzel Decorative', 'Cinzel', 'Georgia', serif;
  font-size: clamp(2.8rem, 8vw, 3.6rem);
  font-weight: 900;
  line-height: 1.05;
  letter-spacing: 1.5px;
  background: linear-gradient(180deg, #F97316 0%, #DC2626 40%, #991B1B 80%, #7F1D1D 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 2px 0 #FFFBEB) drop-shadow(0 5px 12px rgba(0, 0, 0, 0.45));
}

/* ── Ribbon Banner: Choose Game Language ── */
.swipe-launch-lang-section {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.swipe-launch-ribbon {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
}

.ribbon-body {
  background: linear-gradient(180deg, #FFFDF8 0%, #F9F1E0 50%, #EFE1C3 100%);
  border: 1.8px solid #B8860B;
  border-radius: 18px;
  padding: 5px 24px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15), inset 0 1px 2px rgba(255, 255, 255, 0.9);
}

.ribbon-body span {
  font-family: 'Cinzel', 'Georgia', serif;
  font-size: 0.92rem;
  font-weight: 800;
  color: #381E0D;
  letter-spacing: 0.5px;
}

.ribbon-gem-bottom {
  position: absolute;
  bottom: -9px;
  left: 50%;
  transform: translateX(-50%);
  width: 16px;
  height: 16px;
  z-index: 3;
}

.ribbon-gem-icon {
  width: 100%;
  height: 100%;
  filter: drop-shadow(0 2px 4px rgba(37, 99, 235, 0.5));
}

/* ── 3 Language Cards Grid (Image 1 Exact) ── */
.swipe-lang-cards-grid {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  width: 100%;
  padding: 6px 0;
}

.swipe-lang-card {
  position: relative;
  width: 86px;
  height: 86px;
  cursor: pointer;
  transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.swipe-lang-card:active {
  transform: scale(0.95);
}

.lang-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #FFFDF8 0%, #F7EBD2 50%, #EFE1C3 100%);
  border: 2px solid #C89D3C;
  border-radius: 16px;
  box-shadow: 0 6px 14px rgba(0, 0, 0, 0.15), inset 0 0 8px rgba(200, 157, 60, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  transition: all 0.3s ease;
}

.lang-card-text {
  font-size: 1.1rem;
  font-weight: 900;
  color: #2D1400;
  letter-spacing: 0.3px;
  text-align: center;
}

.font-telugu {
  font-family: 'Gautami', 'Nirmala UI', system-ui;
  font-size: 1.15rem;
}

.font-hindi {
  font-family: 'Rozha One', 'Yatra One', 'Nirmala UI', system-ui;
  font-size: 1.2rem;
}

.font-english {
  font-family: 'Cinzel', 'Georgia', serif;
  font-size: 1.1rem;
}

/* Micro Gemstones on Language Card Frame */
.gem-micro {
  width: 10px;
  height: 10px;
  display: block;
  filter: drop-shadow(0 1px 3px rgba(0,0,0,0.4));
}

.lang-gem-top {
  position: absolute;
  top: -5px;
  left: 50%;
  transform: translateX(-50%);
}

.lang-gem-bottom {
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
}

.lang-gem-left {
  position: absolute;
  left: -5px;
  top: 50%;
  transform: translateY(-50%);
}

.lang-gem-right {
  position: absolute;
  right: -5px;
  top: 50%;
  transform: translateY(-50%);
}

/* Golden Wings on Language Card */
.lang-wing-wrap {
  position: absolute;
  top: 50%;
  width: 38px;
  height: 48px;
  pointer-events: none;
  opacity: 0;
  transform: translateY(-50%) scale(0.6);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  z-index: 5;
}

.lang-wing-wrap.wing-left {
  left: -26px;
}

.lang-wing-wrap.wing-right {
  right: -26px;
}

.lang-wing-img {
  width: 100%;
  height: 100%;
  filter: drop-shadow(0 3px 6px rgba(0, 0, 0, 0.35));
}

/* 🌟 ACTIVE LANGUAGE CARD HIGHLIGHT (Image 1 Exact) 🌟 */
.swipe-lang-card.active .lang-card-inner {
  border: 2.5px solid #38BDF8 !important;
  background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 50%, #BAE6FD 100%) !important;
  box-shadow: 0 0 18px rgba(56, 189, 248, 0.75), inset 0 0 10px rgba(56, 189, 248, 0.35) !important;
}

.swipe-lang-card.active .lang-card-text {
  color: #03446A;
  font-weight: 900;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
}

.swipe-lang-card.active .lang-wing-wrap {
  opacity: 1;
  transform: translateY(-50%) scale(1);
}

/* ── Category Header: Choose Category ── */
.swipe-launch-cat-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-top: 4px;
  margin-bottom: 2px;
}

.swipe-launch-cat-title {
  margin: 0;
  font-family: 'Cinzel', 'Georgia', serif;
  font-size: 1.05rem;
  font-weight: 900;
  color: #2F1706;
  letter-spacing: 0.6px;
  text-shadow: 0 1px 2px rgba(255, 248, 230, 0.9);
}

.cat-header-gem {
  width: 14px;
  height: 14px;
}

/* ── 3D Category Carousel / Slider Stage (Image 1 Exact) ── */
.swipe-cat-carousel-stage {
  position: relative;
  width: 100%;
  height: 290px;
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 1000px;
  margin-top: 2px;
  margin-bottom: 4px;
}

.swipe-carousel-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(255, 250, 240, 0.85);
  border: 2px solid #D4AF37;
  color: #5D2E0C;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 25;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
  transition: all 0.2s ease;
}

.swipe-carousel-arrow:active {
  transform: translateY(-50%) scale(0.92);
}

.swipe-carousel-arrow.arrow-left {
  left: 2px;
}

.swipe-carousel-arrow.arrow-right {
  right: 2px;
}

.swipe-cat-carousel-track {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Category Slide Card */
.swipe-cat-slide-card {
  position: absolute;
  width: 220px;
  height: 275px;
  transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
  cursor: pointer;
}

/* Active Center Card */
.swipe-cat-slide-card.active {
  z-index: 15;
  transform: translateX(0) scale(1);
  opacity: 1;
  pointer-events: auto;
}

/* Left Peeking Card */
.swipe-cat-slide-card.peek-left {
  z-index: 8;
  transform: translateX(-145px) scale(0.82);
  opacity: 0.65;
  filter: brightness(0.9);
}

/* Right Peeking Card */
.swipe-cat-slide-card.peek-right {
  z-index: 8;
  transform: translateX(145px) scale(0.82);
  opacity: 0.65;
  filter: brightness(0.9);
}

/* Card Ornate Golden Frame */
.cat-card-frame {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 18px;
  border: 3.5px solid #C89D3C;
  background: #2D1400;
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45), 0 0 0 1px #FDE047, inset 0 0 6px rgba(255, 215, 0, 0.4);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

/* Gemstones on Category Card */
.gem-card {
  width: 14px;
  height: 14px;
  display: block;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.5));
}

.cat-gem-crown {
  position: absolute;
  top: 4px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
}

.cat-gem-side.left {
  position: absolute;
  left: 3px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
}

.cat-gem-side.right {
  position: absolute;
  right: 3px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
}

/* Split Artwork */
.cat-card-art-wrap {
  position: relative;
  width: 100%;
  height: 228px;
  overflow: hidden;
}

.cat-card-split-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.cat-card-divider-line {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 2.5px;
  background: linear-gradient(180deg, #FDE68A 0%, #D4AF37 50%, #996515 100%);
  box-shadow: 0 0 6px rgba(255, 215, 0, 0.8);
  transform: translateX(-50%);
  z-index: 5;
}

/* Bottom Ribbon Banner: Left VS Right */
.cat-card-bottom-ribbon {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 46px;
  background: linear-gradient(180deg, #FFFDF8 0%, #F5E8CB 50%, #E7D1A5 100%);
  border-top: 2px solid #C89D3C;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 0 8px;
  box-sizing: border-box;
  z-index: 8;
  box-shadow: inset 0 1px 2px rgba(255, 255, 255, 0.9);
}

.cat-side-name {
  font-family: 'Cinzel', 'Georgia', serif;
  font-size: 0.86rem;
  font-weight: 900;
  color: #381E0D;
  text-align: center;
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cat-vs-badge {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 6px;
}

.vs-text {
  font-family: 'Cinzel Decorative', 'Cinzel', serif;
  font-size: 0.92rem;
  font-weight: 900;
  font-style: italic;
  background: linear-gradient(180deg, #EA580C 0%, #DC2626 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 1px 1px rgba(0, 0, 0, 0.3));
}

/* ── Big Royal-Blue Play Button with Golden Wings (Image 1 Exact) ── */
.swipe-launch-play-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin-top: 6px;
  margin-bottom: 8px;
}

.swipe-play-wing {
  position: absolute;
  top: 50%;
  width: 58px;
  height: 68px;
  pointer-events: none;
  z-index: 5;
  transition: transform 0.2s ease;
}

.swipe-play-wing.play-wing-left {
  left: calc(50% - 146px);
  transform: translateY(-50%);
}

.swipe-play-wing.play-wing-right {
  right: calc(50% - 146px);
  transform: translateY(-50%);
}

.play-wing-img {
  width: 100%;
  height: 100%;
  filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.45));
}

.swipe-launch-play-btn {
  position: relative;
  z-index: 10;
  width: 230px;
  height: 56px;
  border-radius: 9999px;
  background: linear-gradient(180deg, #2563EB 0%, #1D4ED8 50%, #1E40AF 100%);
  border: 3.5px solid #F59E0B;
  box-shadow: 0 0 0 1.5px #FEF08A, 0 8px 24px rgba(29, 78, 216, 0.6), inset 0 2px 4px rgba(255, 255, 255, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.swipe-launch-play-btn:hover {
  transform: scale(1.03);
  box-shadow: 0 0 0 2px #FEF08A, 0 12px 30px rgba(29, 78, 216, 0.75), inset 0 2px 6px rgba(255, 255, 255, 0.6);
}

.swipe-launch-play-btn:active {
  transform: scale(0.96);
}

.play-btn-crown-top {
  position: absolute;
  top: -8px;
  left: 50%;
  transform: translateX(-50%);
}

.play-btn-crown-bottom {
  position: absolute;
  bottom: -8px;
  left: 50%;
  transform: translateX(-50%);
}

.play-triangle-icon {
  color: #FFFFFF;
  font-size: 1.4rem;
  line-height: 1;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.4));
}

.play-text {
  font-family: 'Cinzel', 'Georgia', serif;
  font-size: 1.42rem;
  font-weight: 900;
  color: #FFFFFF;
  letter-spacing: 1px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

/* ── Screen Height Adjustments ── */
@media (max-height: 700px) {
  .swipe-launch-title { font-size: 2.3rem; }
  .swipe-lang-card { width: 76px; height: 76px; }
  .swipe-cat-carousel-stage { height: 250px; }
  .swipe-cat-slide-card { width: 195px; height: 245px; }
  .cat-card-art-wrap { height: 200px; }
  .swipe-launch-play-btn { width: 210px; height: 50px; }
  .swipe-play-wing.play-wing-left { left: calc(50% - 132px); width: 50px; height: 60px; }
  .swipe-play-wing.play-wing-right { right: calc(50% - 132px); width: 50px; height: 60px; }
}
"""

if ".swipe-launcher-screen" not in css_content:
    css_content += "\n" + launcher_css
    with open(CSS_FILE, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("✓ Appended swipe launcher CSS to epic_games.css successfully.")
else:
    print("⚠ swipe-launcher-screen styles already present in epic_games.css")

print("\n=== All Upgrade Steps Complete! ===")
