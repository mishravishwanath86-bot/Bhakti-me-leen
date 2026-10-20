# -*- coding: utf-8 -*-
"""
Patch epic_games.css and epic_games_engine.js with complete PadaBandham game engine,
5 sacred levels, live stopwatch, hint system, and butter-smooth touch scroll.
"""

import os

APP_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"

def patch_epic_games_css():
    css_path = os.path.join(APP_DIR, "epic_games.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    pada_css_override = """

/* ══════════════════════════════════════════════════════════════════════════════
   🌟 SUPREME DIVINE OVERHAUL: PADABANDHAM (वैदिक शब्द संधान) UI/UX & SCROLL
   ══════════════════════════════════════════════════════════════════════════════ */

#padabandham-game-modal {
  position: fixed !important;
  inset: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  height: 100dvh !important;
  z-index: 100250 !important;
  background: rgba(10, 3, 22, 0.96) !important;
  backdrop-filter: blur(20px) !important;
  -webkit-backdrop-filter: blur(20px) !important;
  display: none;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: flex-start !important; /* CRITICAL: Never center overflowing container */
  overflow-y: auto !important;
  -webkit-overflow-scrolling: touch !important;
  overscroll-behavior-y: contain !important;
  touch-action: pan-y !important;
  padding: max(16px, env(safe-area-inset-top)) 12px calc(90px + env(safe-area-inset-bottom)) !important;
  box-sizing: border-box !important;
}

#padabandham-game-modal.active,
#padabandham-game-modal.is-open {
  display: flex !important;
}

.pada-card {
  width: 100% !important;
  max-width: 420px !important;
  background: radial-gradient(circle at 50% 10%, #2D0F47 0%, #150624 55%, #220836 100%) !important;
  border: 2px solid #F59E0B !important;
  border-radius: 26px !important;
  padding: 16px 14px 20px !important;
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.9), 0 0 25px rgba(245, 158, 11, 0.25) inset !important;
  color: #FFFDF8 !important;
  text-align: center !important;
  box-sizing: border-box !important;
  position: relative !important;
  margin: 0 auto !important;
  flex-shrink: 0 !important;
}

.pada-close-btn {
  position: absolute !important;
  top: 12px !important;
  right: 12px !important;
  width: 34px !important;
  height: 34px !important;
  border-radius: 50% !important;
  background: rgba(255, 255, 255, 0.12) !important;
  border: 1.5px solid rgba(245, 158, 11, 0.5) !important;
  color: #FDE68A !important;
  font-size: 1.15rem !important;
  font-weight: 900 !important;
  cursor: pointer !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  z-index: 10 !important;
  transition: all 0.2s ease !important;
}

.pada-close-btn:hover,
.pada-close-btn:active {
  transform: scale(1.1) !important;
  background: rgba(255, 255, 255, 0.25) !important;
}

.pada-title-row {
  font-size: 1.25rem !important;
  font-weight: 900 !important;
  color: #FFFDF8 !important;
  margin-bottom: 3px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  text-shadow: 0 0 12px rgba(245, 158, 11, 0.45) !important;
}

.pada-title-icon {
  font-size: 1.3rem !important;
}

.pada-subtitle {
  font-size: 0.8rem !important;
  color: #FDE68A !important;
  margin-bottom: 12px !important;
  font-weight: 600 !important;
  line-height: 1.3 !important;
}

.pada-hud-bar {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 6px !important;
  background: rgba(0, 0, 0, 0.45) !important;
  border: 1.5px solid rgba(245, 158, 11, 0.35) !important;
  border-radius: 16px !important;
  padding: 6px 10px !important;
  margin-bottom: 12px !important;
}

.pada-nav-btn {
  background: rgba(245, 158, 11, 0.2) !important;
  border: 1px solid rgba(245, 158, 11, 0.5) !important;
  color: #FDE68A !important;
  font-size: 0.85rem !important;
  padding: 4px 10px !important;
  border-radius: 8px !important;
  cursor: pointer !important;
  font-weight: 900 !important;
  transition: all 0.15s ease !important;
  flex-shrink: 0 !important;
}

.pada-nav-btn:hover,
.pada-nav-btn:active {
  background: #F59E0B !important;
  color: #1A0B2E !important;
}

.pada-level-chip {
  font-size: 0.92rem !important;
  font-weight: 900 !important;
  color: #FFFDF8 !important;
  background: linear-gradient(135deg, #FFFDF8 0%, #FDE68A 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  flex: 1 1 auto !important;
  white-space: nowrap !important;
  overflow: visible !important;
  text-align: center !important;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4) !important;
}

.pada-timer-chip {
  font-size: 0.82rem !important;
  font-weight: 800 !important;
  color: #00FFCC !important;
  background: rgba(0, 255, 204, 0.14) !important;
  border: 1px solid rgba(0, 255, 204, 0.4) !important;
  padding: 3px 8px !important;
  border-radius: 10px !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
}

.pada-score-chip {
  font-size: 0.82rem !important;
  font-weight: 900 !important;
  color: #FBBF24 !important;
  background: rgba(245, 158, 11, 0.18) !important;
  border: 1px solid rgba(245, 158, 11, 0.45) !important;
  padding: 3px 8px !important;
  border-radius: 10px !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
}

.pada-targets-container {
  display: flex !important;
  justify-content: center !important;
  gap: 6px !important;
  flex-wrap: wrap !important;
  margin-bottom: 12px !important;
  padding: 2px !important;
}

.pada-word-badge {
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  background: rgba(255, 255, 255, 0.08) !important;
  color: #FDE68A !important;
  border: 1.5px solid rgba(245, 158, 11, 0.35) !important;
  padding: 4px 10px !important;
  border-radius: 14px !important;
  font-weight: 800 !important;
  font-size: 0.82rem !important;
  transition: all 0.25s ease !important;
}

.pada-word-badge.is-found {
  background: linear-gradient(135deg, #10B981, #059669) !important;
  color: #FFFFFF !important;
  border-color: #6EE7B7 !important;
  box-shadow: 0 0 12px rgba(16, 185, 129, 0.6) !important;
  transform: scale(1.04) !important;
}

.pada-badge-avatar {
  width: 22px !important;
  height: 22px !important;
  border-radius: 50% !important;
  object-fit: cover !important;
  border: 1.2px solid #FDE68A !important;
  flex-shrink: 0 !important;
}

.pada-preview-bar {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 8px !important;
  background: rgba(0, 0, 0, 0.5) !important;
  border: 1.5px solid rgba(245, 158, 11, 0.4) !important;
  border-radius: 14px !important;
  padding: 6px 12px !important;
  margin-bottom: 12px !important;
  min-height: 42px !important;
  box-sizing: border-box !important;
}

.pada-preview-text {
  font-size: 0.95rem !important;
  font-weight: 800 !important;
  color: #4ADE80 !important;
  flex: 1 !important;
  text-align: left !important;
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  white-space: nowrap !important;
}

.pada-selected-tile {
  background: linear-gradient(135deg, #F59E0B, #D97706) !important;
  color: #1A0B2E !important;
  padding: 2px 8px !important;
  border-radius: 6px !important;
  font-weight: 900 !important;
  font-size: 0.92rem !important;
}

.pada-preview-actions {
  display: flex !important;
  gap: 6px !important;
  flex-shrink: 0 !important;
}

.pada-backspace-btn,
.pada-clear-btn {
  background: rgba(255, 255, 255, 0.12) !important;
  border: 1px solid rgba(255, 255, 255, 0.3) !important;
  color: #FDE68A !important;
  border-radius: 8px !important;
  padding: 4px 10px !important;
  font-size: 0.95rem !important;
  font-weight: 900 !important;
  cursor: pointer !important;
  transition: all 0.15s ease !important;
}

.pada-backspace-btn:active,
.pada-clear-btn:active {
  background: rgba(239, 68, 68, 0.4) !important;
  color: #FFF !important;
  border-color: #EF4444 !important;
}

.pada-grid-wrap {
  display: flex !important;
  justify-content: center !important;
  margin-bottom: 14px !important;
}

.pada-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 8px !important;
  max-width: 320px !important;
  width: 100% !important;
  margin: 0 auto !important;
}

.pada-cell, .padabandham-cell {
  background: radial-gradient(circle at 35% 30%, #3B145E 0%, #1A052E 100%) !important;
  border: 2px solid rgba(245, 158, 11, 0.4) !important;
  color: #FFFDF8 !important;
  font-family: 'Tiro Devanagari Hindi', 'Noto Sans Devanagari', serif !important;
  font-size: 1.35rem !important;
  font-weight: 900 !important;
  height: 54px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 14px !important;
  cursor: pointer !important;
  user-select: none !important;
  -webkit-user-select: none !important;
  touch-action: manipulation !important;
  transition: transform 0.12s ease, background 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.2) !important;
}

.pada-cell:active, .padabandham-cell:active {
  transform: scale(0.92) !important;
}

.pada-cell.is-selected, .padabandham-cell.is-selected {
  background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
  border-color: #FFFDF8 !important;
  color: #1A0B2E !important;
  box-shadow: 0 0 18px rgba(245, 158, 11, 0.85), inset 0 2px 4px rgba(255, 255, 255, 0.6) !important;
  transform: scale(1.05) !important;
}

.pada-cell.is-solved, .padabandham-cell.is-solved {
  background: radial-gradient(circle at 35% 30%, #154A38 0%, #0D281E 100%) !important;
  border-color: #34D399 !important;
  color: #A7F3D0 !important;
  box-shadow: 0 0 10px rgba(16, 185, 129, 0.4) inset !important;
}

.pada-cell.has-hint {
  animation: padaHintPulse 1.2s infinite alternate ease-in-out !important;
  border-color: #FEF08A !important;
}

@keyframes padaHintPulse {
  0% { transform: scale(1); box-shadow: 0 0 6px #F59E0B; }
  100% { transform: scale(1.08); box-shadow: 0 0 20px #FEF08A; }
}

.pada-actions-row {
  display: flex !important;
  gap: 10px !important;
}

.pada-btn-hint {
  flex: 1 !important;
  background: rgba(245, 158, 11, 0.22) !important;
  border: 1.5px solid #F59E0B !important;
  color: #FDE68A !important;
  padding: 10px 0 !important;
  border-radius: 14px !important;
  font-weight: 900 !important;
  font-size: 0.9rem !important;
  cursor: pointer !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 6px !important;
  transition: all 0.15s ease !important;
}

.pada-btn-reset {
  flex: 1.2 !important;
  background: linear-gradient(135deg, #F59E0B, #D97706) !important;
  color: #1A0B2E !important;
  border: 1px solid #FDE68A !important;
  padding: 10px 0 !important;
  border-radius: 14px !important;
  font-weight: 900 !important;
  font-size: 0.9rem !important;
  cursor: pointer !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 6px !important;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.4) !important;
  transition: all 0.15s ease !important;
}
"""
    if "/* 🌟 SUPREME DIVINE OVERHAUL: PADABANDHAM" not in css:
        css += pada_css_override
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css)
        print("Appended supreme divine overhaul to epic_games.css.")
    else:
        print("epic_games.css already contains supreme divine overhaul.")

def patch_epic_games_engine():
    js_path = os.path.join(APP_DIR, "epic_games_engine.js")
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()

    # Replace old PadaBandham implementation with our complete multi-level engine
    old_start = js.find("  // ── Game 4: PadaBandham (Word Grid) ──")
    old_end = js.find("  // ══════════════════════════════════════════════════════════════════════════════\n  // 6. GLOBAL NAVIGATION & EXPOSURE TO WINDOW")

    new_engine = """  // ══════════════════════════════════════════════════════════════════════════════
  // 🔤 GAME 4: PADABANDHAM (वैदिक शब्द संधान) 5 SACRED LEVELS ENGINE
  // ══════════════════════════════════════════════════════════════════════════════
  var PADA_LEVELS = [
    {
      level: 1,
      title: "स्तर १: प्रमुख देव",
      words: [
        { word: 'राम', chars: ['रा', 'म'], deity: 'श्री राम', img: 'assets/deity_ram.jpg' },
        { word: 'कृष्ण', chars: ['कृ', 'ष्ण'], deity: 'श्री कृष्ण', img: 'assets/deity_krishna.jpg' },
        { word: 'शिव', chars: ['शि', 'व'], deity: 'महादेव शिव', img: 'assets/deity_shiva.jpg' },
        { word: 'गणेश', chars: ['ग', 'णे', 'श'], deity: 'श्री गणेश', img: 'assets/deity_ganesh.jpg' },
        { word: 'हनुमान', chars: ['ह', 'नु', 'मा', 'न'], deity: 'श्री हनुमान', img: 'assets/deity_hanuman.jpg' },
        { word: 'दुर्गा', chars: ['दु', 'र्गा'], deity: 'माँ दुर्गा', img: 'assets/deity_durga_hd.jpg' },
        { word: 'ॐ', chars: ['ॐ'], deity: 'प्रणव ॐ', img: 'assets/symbols/cards/symbol_om.webp' }
      ],
      // 16 letters in 4x4 grid (exact layout matching user device screenshot)
      grid: [
        'रा', 'म', 'कृ', 'ष्ण',
        'शि', 'व', 'ग', 'णे',
        'श', 'ह', 'नु', 'मा',
        'न', 'दु', 'र्गा', 'ॐ'
      ]
    },
    {
      level: 2,
      title: "स्तर २: पावन धाम",
      words: [
        { word: 'अयोध्या', chars: ['अ', 'यो', 'ध्या'], deity: 'राम लला', img: 'assets/deity_ram.jpg' },
        { word: 'काशी', chars: ['का', 'शी'], deity: 'विश्वनाथ', img: 'assets/deity_shiva.jpg' },
        { word: 'मथुरा', chars: ['म', 'थु', 'रा'], deity: 'गोपाल', img: 'assets/deity_krishna.jpg' },
        { word: 'केदार', chars: ['के', 'दा', 'र'], deity: 'केदारनाथ', img: 'assets/deity_shiva.jpg' },
        { word: 'बद्री', chars: ['ब', 'द्री'], deity: 'बद्रीनाथ', img: 'assets/deity_vishnu.jpg' },
        { word: 'प्रयाग', chars: ['प्र', 'या', 'ग'], deity: 'त्रिवेणी', img: 'assets/symbols/cards/symbol_ganga.webp' }
      ],
      grid: [
        'अ', 'यो', 'ध्या', 'का',
        'शी', 'म', 'थु', 'रा',
        'के', 'दा', 'र', 'ब',
        'द्री', 'प्र', 'या', 'ग'
      ]
    },
    {
      level: 3,
      title: "स्तर ३: दिव्य अवतार",
      words: [
        { word: 'नरसिंह', chars: ['न', 'र', 'सिं', 'ह'], deity: 'प्रह्लाद रक्षक', img: 'assets/deity_vishnu.jpg' },
        { word: 'वामन', chars: ['वा', 'म', 'न'], deity: 'त्रिविक्रम', img: 'assets/deity_vishnu.jpg' },
        { word: 'वराह', chars: ['व', 'रा', 'ह'], deity: 'धरणीधर', img: 'assets/deity_vishnu.jpg' },
        { word: 'परशुराम', chars: ['प', 'र', 'शु', 'रा', 'म'], deity: 'भार्गव', img: 'assets/deity_vishnu.jpg' }
      ],
      grid: [
        'न', 'र', 'सिं', 'ह',
        'वा', 'म', 'न', 'व',
        'रा', 'ह', 'प', 'र',
        'शु', 'रा', 'म', 'ॐ'
      ]
    },
    {
      level: 4,
      title: "स्तर ४: पवित्र प्रतीक",
      words: [
        { word: 'त्रिशूल', chars: ['त्रि', 'शू', 'ल'], deity: 'शिव अस्त्र', img: 'assets/symbols/cards/symbol_trishul.webp' },
        { word: 'डमरू', chars: ['ड', 'म', 'रू'], deity: 'नाद ब्रह्म', img: 'assets/symbols/cards/symbol_damru.webp' },
        { word: 'शंख', chars: ['शं', 'ख'], deity: 'पाञ्चजन्य', img: 'assets/symbols/cards/symbol_shankh.webp' },
        { word: 'चक्र', chars: ['च', 'क्र'], deity: 'सुदर्शन', img: 'assets/symbols/cards/symbol_chakra.webp' },
        { word: 'गदा', chars: ['ग', 'दा'], deity: 'कौमोदकी', img: 'assets/symbols/cards/symbol_gadda.webp' },
        { word: 'पद्म', chars: ['प', 'द्म'], deity: 'कमल दल', img: 'assets/symbols/cards/symbol_lotus.webp' }
      ],
      grid: [
        'त्रि', 'शू', 'ल', 'ड',
        'म', 'रू', 'शं', 'ख',
        'च', 'क्र', 'ग', 'दा',
        'प', 'द्म', 'श्री', 'ॐ'
      ]
    },
    {
      level: 5,
      title: "स्तर ५: पावन तीर्थ",
      words: [
        { word: 'हरिद्वार', chars: ['ह', 'रि', 'द्वा', 'र'], deity: 'गंगा द्वार', img: 'assets/symbols/cards/symbol_ganga.webp' },
        { word: 'उज्जैन', chars: ['उ', 'ज्जै', 'न'], deity: 'महाकाल', img: 'assets/deity_shiva.jpg' },
        { word: 'गोकुल', chars: ['गो', 'कु', 'ल'], deity: 'नंदग्राम', img: 'assets/deity_krishna.jpg' },
        { word: 'द्वारका', chars: ['द्वा', 'र', 'का'], deity: 'द्वारकाधीश', img: 'assets/deity_krishna.jpg' },
        { word: 'ऋषिकेश', chars: ['ऋ', 'षि', 'के', 'श'], deity: 'तपोभूमि', img: 'assets/deity_shiva.jpg' }
      ],
      grid: [
        'ह', 'रि', 'द्वा', 'र',
        'उ', 'ज्जै', 'न', 'गो',
        'कु', 'ल', 'द्वा', 'र',
        'का', 'ऋ', 'षि', 'केश'
      ]
    }
  ];

  var currentPadaLevelIdx = 0;
  var foundWords = [];
  var currentSelectedCells = [];
  var solvedCellIndices = [];
  var padaTimerInterval = null;
  var padaTimerSeconds = 0;
  var padaHintsRemaining = 3;

  function startPadaTimer() {
    stopPadaTimer();
    padaTimerSeconds = 0;
    updatePadaTimerDisplay();
    padaTimerInterval = setInterval(function () {
      padaTimerSeconds++;
      updatePadaTimerDisplay();
    }, 1000);
  }

  function stopPadaTimer() {
    if (padaTimerInterval) {
      clearInterval(padaTimerInterval);
      padaTimerInterval = null;
    }
  }

  function updatePadaTimerDisplay() {
    var timerEl = document.getElementById('pada-timer');
    if (!timerEl) return;
    var mins = Math.floor(padaTimerSeconds / 60);
    var secs = padaTimerSeconds % 60;
    var mm = mins < 10 ? '0' + mins : '' + mins;
    var ss = secs < 10 ? '0' + secs : '' + secs;
    timerEl.textContent = '⏱️ ' + mm + ':' + ss;
  }

  function initPadabandhamGame(lvlIdx) {
    if (typeof lvlIdx === 'number' && lvlIdx >= 0 && lvlIdx < PADA_LEVELS.length) {
      currentPadaLevelIdx = lvlIdx;
    }
    foundWords = [];
    currentSelectedCells = [];
    solvedCellIndices = [];
    padaHintsRemaining = 3;

    var curLvl = PADA_LEVELS[currentPadaLevelIdx];
    var titleEl = document.getElementById('pada-level-name');
    if (titleEl) titleEl.textContent = curLvl.title;

    var hintTextEl = document.getElementById('pada-hint-text');
    if (hintTextEl) hintTextEl.textContent = 'संकेत (Hint: ' + padaHintsRemaining + ')';

    var statusEl = document.getElementById('padabandham-status');
    if (statusEl) statusEl.textContent = 'अक्षरों को क्रम में स्पर्श करें...';

    renderPadabandham();
    startPadaTimer();
  }

  function renderPadabandham() {
    var curLvl = PADA_LEVELS[currentPadaLevelIdx];

    // 1. Level Name without Truncation
    var titleEl = document.getElementById('pada-level-name');
    if (titleEl) titleEl.textContent = curLvl.title;

    // 2. Score Counter
    var scoreEl = document.getElementById('pada-score-counter');
    if (scoreEl) {
      scoreEl.textContent = '🌸 ' + foundWords.length + '/' + curLvl.words.length;
    }

    // 3. Targets Tray
    var targetsEl = document.getElementById('padabandham-word-targets') || document.getElementById('padabandham-word-list');
    if (targetsEl) {
      targetsEl.innerHTML = curLvl.words.map(function (item) {
        var isFound = foundWords.includes(item.word);
        return `<span class="pada-word-badge ${isFound ? 'is-found' : ''}"><img src="${item.img}" class="pada-badge-avatar" onerror="this.src='assets/symbols/cards/symbol_om.webp';"> ${item.word} ${isFound ? '✓' : ''}</span>`;
      }).join(' ');
    }

    // 4. Grid Cells
    var gridEl = document.getElementById('padabandham-grid');
    if (gridEl) {
      gridEl.innerHTML = '';
      curLvl.grid.forEach(function (char, idx) {
        var cell = document.createElement('div');
        var isSel = currentSelectedCells.includes(idx);
        var isSolved = solvedCellIndices.includes(idx);
        cell.className = 'pada-cell' + (isSel ? ' is-selected' : '') + (isSolved ? ' is-solved' : '');
        cell.setAttribute('data-idx', idx);
        cell.textContent = char;
        cell.onclick = function () { handlePadabandhamTap(idx); };
        gridEl.appendChild(cell);
      });
    }
  }

  function handlePadabandhamTap(idx) {
    var curLvl = PADA_LEVELS[currentPadaLevelIdx];

    // Remove any active hint pulse on click
    document.querySelectorAll('.pada-cell.has-hint').forEach(function (el) {
      el.classList.remove('has-hint');
    });

    if (currentSelectedCells.includes(idx)) {
      // Toggle off if tapping an already selected cell
      currentSelectedCells = currentSelectedCells.filter(function (i) { return i !== idx; });
    } else {
      currentSelectedCells.push(idx);
    }

    var formedStr = currentSelectedCells.map(function (i) { return curLvl.grid[i]; }).join('');
    var statusEl = document.getElementById('padabandham-status');

    if (currentSelectedCells.length === 0) {
      if (statusEl) statusEl.textContent = 'अक्षरों को क्रम में स्पर्श करें...';
    } else {
      if (statusEl) {
        statusEl.innerHTML = 'चयनित: <span class="pada-selected-tile">' + formedStr + '</span>';
      }
    }

    // Check if formed string matches any unsolved word
    var matched = curLvl.words.find(function (w) {
      return (w.chars.join('') === formedStr || w.word === formedStr);
    });

    if (matched && !foundWords.includes(matched.word)) {
      foundWords.push(matched.word);
      // Mark selected cells as solved
      currentSelectedCells.forEach(function (i) {
        if (!solvedCellIndices.includes(i)) solvedCellIndices.push(i);
      });
      currentSelectedCells = [];

      if (typeof playSound === 'function') playSound('correct');
      if (statusEl) statusEl.textContent = '🎉 अद्भुत! खोजा: ' + matched.word + ' (' + matched.deity + ')';
      renderPadabandham();

      // Check Level Victory Condition
      if (foundWords.length === curLvl.words.length) {
        stopPadaTimer();
        setTimeout(function () {
          if (typeof playSound === 'function') playSound('victory');
          if (typeof addCoins === 'function') addCoins(150);
          showPadabandhamWinDialog();
        }, 400);
      }
    } else {
      renderPadabandham();
      if (currentSelectedCells.length > 0 && statusEl) {
        statusEl.innerHTML = 'चयनित: <span class="pada-selected-tile">' + formedStr + '</span>';
      }
    }
  }

  function backspacePadabandham() {
    if (currentSelectedCells.length > 0) {
      currentSelectedCells.pop();
      var curLvl = PADA_LEVELS[currentPadaLevelIdx];
      var formedStr = currentSelectedCells.map(function (i) { return curLvl.grid[i]; }).join('');
      var statusEl = document.getElementById('padabandham-status');
      if (currentSelectedCells.length === 0) {
        if (statusEl) statusEl.textContent = 'अक्षरों को क्रम में स्पर्श करें...';
      } else {
        if (statusEl) {
          statusEl.innerHTML = 'चयनित: <span class="pada-selected-tile">' + formedStr + '</span>';
        }
      }
      renderPadabandham();
    }
  }

  function clearPadabandhamSelection() {
    currentSelectedCells = [];
    var statusEl = document.getElementById('padabandham-status');
    if (statusEl) statusEl.textContent = 'अक्षरों को क्रम में स्पर्श करें...';
    renderPadabandham();
  }

  function usePadabandhamHint() {
    if (padaHintsRemaining <= 0) {
      if (typeof showToast === 'function') showToast('💡 इस स्तर के सभी संकेत उपयोग हो चुके हैं!');
      return;
    }

    var curLvl = PADA_LEVELS[currentPadaLevelIdx];
    var firstUnfound = curLvl.words.find(function (w) { return !foundWords.includes(w.word); });
    if (!firstUnfound) return;

    var firstChar = firstUnfound.chars[0];
    var targetIdx = curLvl.grid.indexOf(firstChar);

    if (targetIdx !== -1) {
      var gridEl = document.getElementById('padabandham-grid');
      if (gridEl && gridEl.children[targetIdx]) {
        gridEl.children[targetIdx].classList.add('has-hint');
        padaHintsRemaining--;
        var hintTextEl = document.getElementById('pada-hint-text');
        if (hintTextEl) hintTextEl.textContent = 'संकेत (Hint: ' + padaHintsRemaining + ')';
        if (typeof showToast === 'function') {
          showToast('💡 संकेत: "' + firstUnfound.word + '" का प्रथम अक्षर "' + firstChar + '" चमक रहा है!');
        }
      }
    }
  }

  function nextPadabandhamLevel() {
    var winDlg = document.getElementById('pada-level-win-dialog');
    if (winDlg) winDlg.style.display = 'none';

    if (currentPadaLevelIdx < PADA_LEVELS.length - 1) {
      initPadabandhamGame(currentPadaLevelIdx + 1);
    } else {
      if (typeof showToast === 'function') showToast('🏆 बधाई! आपने सभी ५ पावन स्तर पूर्ण कर लिए हैं!');
      initPadabandhamGame(0);
    }
  }

  function prevPadabandhamLevel() {
    if (currentPadaLevelIdx > 0) {
      initPadabandhamGame(currentPadaLevelIdx - 1);
    } else {
      initPadabandhamGame(PADA_LEVELS.length - 1);
    }
  }

  function replayCurrentPadabandhamLevel() {
    var winDlg = document.getElementById('pada-level-win-dialog');
    if (winDlg) winDlg.style.display = 'none';
    initPadabandhamGame(currentPadaLevelIdx);
  }

  function showPadabandhamWinDialog() {
    var curLvl = PADA_LEVELS[currentPadaLevelIdx];
    var winDlg = document.getElementById('pada-level-win-dialog');
    var winMsg = document.getElementById('pada-win-message');
    if (winMsg) {
      winMsg.textContent = 'आपने ' + curLvl.title + ' के सभी ' + curLvl.words.length + ' पावन नाम खोज लिए हैं!';
    }
    if (winDlg) {
      winDlg.style.display = 'flex';
      winDlg.classList.add('active');
    }
  }

  // Hook global functions to window
  window.initPadabandhamGame = initPadabandhamGame;
  window.nextPadabandhamLevel = nextPadabandhamLevel;
  window.prevPadabandhamLevel = prevPadabandhamLevel;
  window.replayCurrentPadabandhamLevel = replayCurrentPadabandhamLevel;
  window.backspacePadabandham = backspacePadabandham;
  window.clearPadabandhamSelection = clearPadabandhamSelection;
  window.usePadabandhamHint = usePadabandhamHint;
  window.handlePadabandhamTap = handlePadabandhamTap;

  window.openPadabandhamGame = function () {
    var modal = document.getElementById('padabandham-game-modal');
    if (modal) {
      modal.classList.add('active');
      modal.classList.add('is-open');
      modal.style.setProperty('display', 'flex', 'important');
      modal.style.setProperty('opacity', '1', 'important');
      modal.style.setProperty('pointer-events', 'auto', 'important');
      modal.style.setProperty('visibility', 'visible', 'important');
    }
    document.body.classList.add('game-modal-open');
    var appHeader = document.querySelector('.app-header');
    if (appHeader) appHeader.style.setProperty('display', 'none', 'important');
    hideBottomNavForGames();
    initPadabandhamGame(0);
  };

  window.closePadabandhamGame = function () {
    stopPadaTimer();
    var modal = document.getElementById('padabandham-game-modal');
    if (modal) {
      modal.classList.remove('active');
      modal.classList.remove('is-open');
      modal.style.setProperty('display', 'none', 'important');
      modal.style.setProperty('opacity', '0', 'important');
      modal.style.setProperty('pointer-events', 'none', 'important');
    }
    var winDlg = document.getElementById('pada-level-win-dialog');
    if (winDlg) winDlg.style.display = 'none';

    document.body.classList.remove('game-modal-open');
    var appHeader = document.querySelector('.app-header');
    if (appHeader) appHeader.style.removeProperty('display');
    restoreBottomNavIfExited();
  };
"""

    if old_start != -1 and old_end != -1:
        # Also check where openPadabandhamGame was in file
        open_old = js.find("  window.openPadabandhamGame = function () {")
        close_old = js.find("  window.closePadabandhamGame = function () {")
        if open_old != -1 and close_old != -1:
            end_close = js.find("  };", close_old) + 4
            # Remove old open/close handlers as they are now part of new_engine
            js = js[:open_old] + js[end_close:]

        # Recalculate start and end
        old_start = js.find("  // ── Game 4: PadaBandham (Word Grid) ──")
        old_end = js.find("  // ══════════════════════════════════════════════════════════════════════════════\n  // 6. GLOBAL NAVIGATION & EXPOSURE TO WINDOW")

        js = js[:old_start] + new_engine + "\n\n" + js[old_end:]

        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js)
        print("Patched epic_games_engine.js with full PadaBandham engine.")
    else:
        print("Warning: PadaBandham section anchor not found in epic_games_engine.js.")

if __name__ == "__main__":
    patch_epic_games_css()
    patch_epic_games_engine()
