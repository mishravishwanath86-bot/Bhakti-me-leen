import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

rich_quiz_modal_html = """  <!-- 🎯 DEDICATED SACRED MCQ QUIZ HUB MODAL 🎯 -->
  <div id="quiz-hub-modal" style="display:none; position:fixed; inset:0; z-index:100025; background:rgba(10,2,18,0.95); backdrop-filter:blur(30px); -webkit-backdrop-filter:blur(30px); align-items:center; justify-content:center; padding:1rem; overflow-y:auto;">
    <div id="quiz-hub-card" style="width:100%; max-width:460px; background:linear-gradient(160deg, #2A0948 0%, #150426 60%, #0B0116 100%); border:2px solid #F59E0B; border-radius:28px; padding:1.4rem 1.2rem; box-shadow:0 25px 70px rgba(0,0,0,0.9); position:relative; margin:auto 0; transition:all 0.3s ease;">
      
      <!-- Top Bar: Title, Theme Toggle, Timer, Question Badge, Close Button -->
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
        <div style="font-size:1.15rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
          <span>🎯</span> <span id="quiz-header-title">दिव्य प्रश्नोत्तरी</span>
        </div>
        <div style="display:flex; align-items:center; gap:6px;">
          <!-- 🌓 Theme Toggle Button -->
          <button id="quiz-theme-btn" onclick="toggleQuizTheme()" title="थीम बदलें (Dark / Light)" style="background:rgba(255,255,255,0.12); border:1.5px solid #F59E0B; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1.05rem; cursor:pointer; display:flex; align-items:center; justify-content:center; transition:transform 0.2s;">
            ☀️
          </button>
          
          <!-- ⏱️ 120s Timer Badge -->
          <div id="quiz-timer-badge" style="display:flex; align-items:center; gap:4px; font-size:0.8rem; font-weight:900; background:rgba(248,200,59,0.18); border:1.5px solid #F8C83B; color:#FDE68A; padding:4px 10px; border-radius:14px;">
            <span>⏱️</span> <span id="quiz-timer-text">120s</span>
          </div>

          <!-- Q Progress Badge -->
          <span id="quiz-progress-badge" style="font-size:0.78rem; font-weight:900; background:rgba(248,200,59,0.2); border:1.5px solid #F8C83B; color:#FDE68A; padding:4px 10px; border-radius:14px;">
            Q 1 / 10
          </span>

          <!-- Close Button -->
          <button onclick="closeQuizHubModal()" style="background:rgba(255,255,255,0.12); border:none; color:#FDE68A; width:32px; height:32px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
        </div>
      </div>

      <!-- 🎮 Quiz Length / Questions Count Selector -->
      <div style="display:flex; align-items:center; justify-content:space-between; background:rgba(0,0,0,0.25); padding:4px 8px; border-radius:14px; margin-bottom:10px; border:1px solid rgba(248,200,59,0.25);">
        <span style="font-size:0.72rem; font-weight:800; color:#FDE68A; display:flex; align-items:center; gap:4px;">
          <span>🔢</span> प्रश्न संख्या:
        </span>
        <div style="display:flex; gap:4px;">
          <button onclick="setQuizLength(10, this)" class="quiz-len-btn active" style="padding:3px 8px; font-size:0.72rem; font-weight:900; border-radius:8px; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer;">10</button>
          <button onclick="setQuizLength(25, this)" class="quiz-len-btn" style="padding:3px 8px; font-size:0.72rem; font-weight:800; border-radius:8px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer;">25</button>
          <button onclick="setQuizLength(50, this)" class="quiz-len-btn" style="padding:3px 8px; font-size:0.72rem; font-weight:800; border-radius:8px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer;">50</button>
          <button onclick="setQuizLength(0, this)" class="quiz-len-btn" title="डेटाबेस के सभी प्रश्न" style="padding:3px 8px; font-size:0.72rem; font-weight:800; border-radius:8px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer;">⚡ सभी (All 791)</button>
        </div>
      </div>

      <!-- Category Chips -->
      <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:12px; scrollbar-width:none;">
        <button onclick="switchQuizCategory('all', this)" class="quiz-cat-btn active" style="padding:6px 12px; font-size:0.78rem; font-weight:900; border-radius:14px; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; white-space:nowrap;">🎯 संपूर्ण (Mega)</button>
        <button onclick="switchQuizCategory('india', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🏛️ भारत मंदिर</button>
        <button onclick="switchQuizCategory('gita', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">📖 गीता</button>
        <button onclick="switchQuizCategory('ramayana', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🏹 रामायण</button>
        <button onclick="switchQuizCategory('chalisa', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">📜 चालीसा</button>
        <button onclick="switchQuizCategory('world', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🌍 विश्व मंदिर</button>
      </div>

      <!-- Main Question & Options Container -->
      <div id="quiz-main-view">
        <!-- Question Box -->
        <div id="quiz-question-box" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:14px; margin-bottom:12px;">
          <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px;">
            <h4 id="quiz-question-text" style="font-size:1.02rem; color:#FFFDF8; font-weight:900; line-height:1.45; margin:0 0 10px 0; flex:1;">
              प्रश्न लोड हो रहा है...
            </h4>
            <!-- 🎙️ AI Voice Read Aloud -->
            <button onclick="speakCurrentQuizQuestion()" title="🎙️ AI हिंदी वॉइस से सुनें" style="background:rgba(248,200,59,0.25); border:1.5px solid #F8C83B; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
              🔊
            </button>
          </div>

          <div id="quiz-options-list" style="display:flex; flex-direction:column; gap:9px;">
            <!-- Options rendered dynamically -->
          </div>

          <!-- Dynamic Feedback Area -->
          <div id="quiz-feedback-box" style="display:none; margin-top:12px; padding:12px; border-radius:14px; background:rgba(16,185,129,0.18); border:1.5px solid #10B981;">
            <div id="quiz-feedback-title" style="font-size:0.92rem; font-weight:900; color:#34D399; margin-bottom:4px;">
              🎉 शाबाश! सही जवाब! (+10 साधना अंक)
            </div>
            <p id="quiz-feedback-desc" style="font-size:0.84rem; color:#E2E8F0; margin:0 0 10px 0; line-height:1.45; font-weight:600;">
              स्पष्टीकरण
            </p>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <a id="quiz-map-link" href="#" target="_blank" style="font-size:0.78rem; color:#FDE68A; text-decoration:underline; font-weight:800;">📍 गूगल मैप पर देखें</a>
              <button onclick="nextQuizQuestion()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-size:0.82rem; font-weight:900; padding:7px 16px; border-radius:12px; cursor:pointer; box-shadow:0 3px 10px rgba(248,200,59,0.35);">अगला प्रश्न ❯</button>
            </div>
          </div>

        </div>
      </div>

      <!-- 🏆 Completion Result View (Hidden during gameplay) -->
      <div id="quiz-result-view" style="display:none; text-align:center; padding:1rem 0.5rem;">
        <div style="font-size:3.5rem; margin-bottom:8px;">🏆</div>
        <h3 style="font-size:1.35rem; font-weight:900; color:#FFFDF8; margin:0 0 4px 0;">॥ क्विज़ पूर्ण ॥</h3>
        <p style="font-size:0.85rem; color:#FDE68A; margin:0 0 16px 0;">पावन सनातन ज्ञान यात्रा</p>

        <div style="background:rgba(248,200,59,0.12); border:1.5px solid rgba(248,200,59,0.4); border-radius:20px; padding:1.2rem; margin-bottom:18px;">
          <div id="quiz-final-score" style="font-size:2.8rem; font-weight:900; color:#F8C83B; line-height:1;">
            10 / 10
          </div>
          <div style="font-size:0.82rem; color:#CBD5E1; margin-top:4px;">आज का आपका स्कोर</div>
          <div id="quiz-high-score-banner" style="font-size:0.85rem; color:#34D399; font-weight:800; margin-top:10px; padding-top:8px; border-top:1px solid rgba(255,255,255,0.1);">
            🌟 आपका सर्वश्रेष्ठ स्कोर: <span id="quiz-high-score-num">10</span>
          </div>
        </div>

        <!-- 📲 WhatsApp Share Button -->
        <button onclick="shareQuizScoreWhatsApp()" style="width:100%; padding:12px; background:#25D366; color:#FFF; border:none; border-radius:16px; font-weight:900; font-size:0.95rem; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:8px; box-shadow:0 4px 15px rgba(37,211,102,0.4); margin-bottom:10px;">
          <span>📲</span> WhatsApp पर उपलब्धि शेयर करें 🚩
        </button>

        <!-- 🔄 Play Again Button -->
        <button onclick="restartQuizCurrentCategory()" style="width:100%; padding:11px; background:rgba(255,255,255,0.1); color:#FDE68A; border:1.5px solid rgba(248,200,59,0.3); border-radius:16px; font-weight:800; font-size:0.9rem; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:6px;">
          <span>🔄</span> पुनः खेलें (नये प्रश्न)
        </button>
      </div>

    </div>
  </div>"""

# Replace in index.html
start_m = html.find('<!-- 🎯 DEDICATED SACRED MCQ QUIZ HUB MODAL 🎯 -->')
if start_m != -1:
    end_m = html.find('<!-- ═════════════════════════════════════════════════════════════════', start_m)
    html = html[:start_m] + rich_quiz_modal_html + "\n\n  " + html[end_m:]

# Cache bust
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Updated index.html modal with Question Count selector and crystal-clear layout")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

start_js = js.find('// ══════════════════════════════════════════════════════════════════════════════\n// 🎯 COMPLETE DYNAMIC SACRED MCQ QUIZ ENGINE')
if start_js == -1:
    start_js = js.find('// 4. MCQ Quiz Hub Logic')

end_js = js.find('// 5. Kalyan Kund Seva Daan Logic')

new_app_js = """// ══════════════════════════════════════════════════════════════════════════════
// 🎯 COMPLETE DYNAMIC SACRED MCQ QUIZ ENGINE (791+ Questions + Custom Length)
// ══════════════════════════════════════════════════════════════════════════════

window.ALL_MCQS_DATA = [];
window.ACTIVE_QUIZ_DECK = [];
window.currentQuizCategory = 'all';
window.currentQuizLength = 10; // 10, 25, 50, or 0 (All)
window.currentQuizIndex = 0;
window.quizScore = 0;
window.quizHighScore = parseInt(localStorage.getItem('sanatan_quiz_high_score') || '0', 10);
window.isQuizAnswered = false;
window.quizTimerInterval = null;
window.quizSecondsLeft = 120;
window.isQuizLightMode = localStorage.getItem('sanatan_quiz_theme') === 'light';

// Load all questions from all_sanatan_mcqs.json
window.loadAllMCQsData = async function() {
  if (window.ALL_MCQS_DATA.length > 0) return;
  try {
    const resp = await fetch('all_sanatan_mcqs.json');
    if (resp.ok) {
      window.ALL_MCQS_DATA = await resp.json();
      console.log(`✓ Loaded ${window.ALL_MCQS_DATA.length} Sanatan MCQs into memory`);
    }
  } catch(e) {
    console.warn("Could not fetch all_sanatan_mcqs.json:", e);
  }
};

window.loadAllMCQsData();

// Set Quiz Length (10, 25, 50, 0 for All)
window.setQuizLength = function(len, btnEl) {
  window.currentQuizLength = len;
  document.querySelectorAll('.quiz-len-btn').forEach(b => {
    b.classList.remove('active');
    b.style.background = window.isQuizLightMode ? '#F1F5F9' : 'rgba(255,255,255,0.08)';
    b.style.color = window.isQuizLightMode ? '#475569' : '#CBD5E1';
    b.style.border = window.isQuizLightMode ? '1px solid #CBD5E1' : '1px solid rgba(255,255,255,0.15)';
  });
  if (btnEl) {
    btnEl.classList.add('active');
    btnEl.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btnEl.style.color = '#1A0B2E';
    btnEl.style.border = 'none';
  }
  window.prepareActiveQuizDeck(window.currentQuizCategory);
  window.startQuizTimer();
  window.renderCurrentQuiz();
};

// Pick questions from the chosen category or entire database
window.prepareActiveQuizDeck = function(category) {
  category = category || window.currentQuizCategory || 'all';
  let pool = [];

  if (window.ALL_MCQS_DATA && window.ALL_MCQS_DATA.length > 0) {
    if (category === 'all' || category === 'mega') {
      pool = [...window.ALL_MCQS_DATA];
    } else {
      pool = window.ALL_MCQS_DATA.filter(q => q.category === category);
      if (pool.length < 5) {
        pool = [...window.ALL_MCQS_DATA];
      }
    }
  }

  // Shuffle pool using Fisher-Yates
  const shuffled = [...pool].sort(() => Math.random() - 0.5);
  
  // Choose count: if currentQuizLength == 0, take all; otherwise take slice
  const count = (window.currentQuizLength > 0) ? Math.min(window.currentQuizLength, shuffled.length) : shuffled.length;
  
  window.ACTIVE_QUIZ_DECK = shuffled.slice(0, count).map(item => ({
    q: item.question || item.q,
    opts: item.options || item.opts,
    correct: (typeof item.correct_answer === 'number') ? item.correct_answer : item.correct,
    desc: item.explanation || item.desc || 'पावन सनातन ज्ञान का दिव्य उत्तर।',
    map: item.map || (item.question.includes('मंदिर') ? `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(item.question.substring(0, 40))}` : null)
  }));

  window.currentQuizIndex = 0;
  window.quizScore = 0;
  window.isQuizAnswered = false;
};

// 🎯 CONTROLLER METHODS

window.openQuizHubModal = async function() {
  const modal = document.getElementById('quiz-hub-modal');
  if (modal) {
    modal.style.display = 'flex';
    if (window.ALL_MCQS_DATA.length === 0) {
      await window.loadAllMCQsData();
    }
    window.prepareActiveQuizDeck(window.currentQuizCategory);
    window.applyQuizTheme();
    window.startQuizTimer();
    window.renderCurrentQuiz();
    if (navigator.vibrate) navigator.vibrate(30);
  }
};

window.closeQuizHubModal = function() {
  const modal = document.getElementById('quiz-hub-modal');
  if (modal) modal.style.display = 'none';
  window.stopQuizTimer();
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
};

window.toggleQuizTheme = function() {
  window.isQuizLightMode = !window.isQuizLightMode;
  localStorage.setItem('sanatan_quiz_theme', window.isQuizLightMode ? 'light' : 'dark');
  window.applyQuizTheme();
  window.renderCurrentQuiz();
};

window.applyQuizTheme = function() {
  const card = document.getElementById('quiz-hub-card');
  const themeBtn = document.getElementById('quiz-theme-btn');
  const title = document.getElementById('quiz-header-title');
  const qBox = document.getElementById('quiz-question-box');
  const qText = document.getElementById('quiz-question-text');
  const timerBadge = document.getElementById('quiz-timer-badge');
  const progBadge = document.getElementById('quiz-progress-badge');

  if (!card) return;

  if (window.isQuizLightMode) {
    card.style.background = 'linear-gradient(160deg, #FFFDF8 0%, #FEF3C7 100%)';
    card.style.borderColor = '#D97706';
    card.style.color = '#1A0B2E';
    if (themeBtn) {
      themeBtn.textContent = '🌙';
      themeBtn.style.background = 'rgba(217, 119, 6, 0.15)';
      themeBtn.style.borderColor = '#D97706';
      themeBtn.style.color = '#78350F';
    }
    if (title) title.style.color = '#78350F';
    if (qBox) {
      qBox.style.background = '#FFFFFF';
      qBox.style.borderColor = '#F59E0B';
      qBox.style.boxShadow = '0 4px 15px rgba(217,119,6,0.08)';
    }
    if (qText) qText.style.color = '#1A0B2E';
    if (timerBadge) {
      timerBadge.style.background = '#FEF3C7';
      timerBadge.style.borderColor = '#D97706';
      timerBadge.style.color = '#78350F';
    }
    if (progBadge) {
      progBadge.style.background = '#FEF3C7';
      progBadge.style.borderColor = '#D97706';
      progBadge.style.color = '#78350F';
    }

    // Inactive category buttons in light mode
    document.querySelectorAll('.quiz-cat-btn:not(.active)').forEach(b => {
      b.style.background = '#FEF3C7';
      b.style.color = '#78350F';
      b.style.borderColor = 'rgba(217, 119, 6, 0.3)';
    });

    // Inactive length buttons in light mode
    document.querySelectorAll('.quiz-len-btn:not(.active)').forEach(b => {
      b.style.background = '#FEF3C7';
      b.style.color = '#78350F';
      b.style.borderColor = 'rgba(217, 119, 6, 0.3)';
    });
  } else {
    card.style.background = 'linear-gradient(160deg, #2A0948 0%, #150426 60%, #0B0116 100%)';
    card.style.borderColor = '#F59E0B';
    card.style.color = '#FFFDF8';
    if (themeBtn) {
      themeBtn.textContent = '☀️';
      themeBtn.style.background = 'rgba(255,255,255,0.12)';
      themeBtn.style.borderColor = '#F59E0B';
      themeBtn.style.color = '#FDE68A';
    }
    if (title) title.style.color = '#FFFDF8';
    if (qBox) {
      qBox.style.background = 'rgba(255,255,255,0.06)';
      qBox.style.borderColor = 'rgba(248,200,59,0.3)';
      qBox.style.boxShadow = 'none';
    }
    if (qText) qText.style.color = '#FFFDF8';
    if (timerBadge) {
      timerBadge.style.background = 'rgba(248,200,59,0.18)';
      timerBadge.style.borderColor = '#F8C83B';
      timerBadge.style.color = '#FDE68A';
    }
    if (progBadge) {
      progBadge.style.background = 'rgba(248,200,59,0.2)';
      progBadge.style.borderColor = '#F8C83B';
      progBadge.style.color = '#FDE68A';
    }

    // Inactive category buttons in dark mode
    document.querySelectorAll('.quiz-cat-btn:not(.active)').forEach(b => {
      b.style.background = 'rgba(255,255,255,0.08)';
      b.style.color = '#CBD5E1';
      b.style.borderColor = 'rgba(255,255,255,0.15)';
    });

    // Inactive length buttons in dark mode
    document.querySelectorAll('.quiz-len-btn:not(.active)').forEach(b => {
      b.style.background = 'rgba(255,255,255,0.08)';
      b.style.color = '#CBD5E1';
      b.style.borderColor = 'rgba(255,255,255,0.15)';
    });
  }
};

window.startQuizTimer = function() {
  window.stopQuizTimer();
  window.quizSecondsLeft = 120;
  window.updateTimerUI();

  window.quizTimerInterval = setInterval(() => {
    if (window.quizSecondsLeft > 0) {
      window.quizSecondsLeft--;
      window.updateTimerUI();
    } else {
      window.stopQuizTimer();
      window.handleQuizTimeout();
    }
  }, 1000);
};

window.stopQuizTimer = function() {
  if (window.quizTimerInterval) {
    clearInterval(window.quizTimerInterval);
    window.quizTimerInterval = null;
  }
};

window.updateTimerUI = function() {
  const timerText = document.getElementById('quiz-timer-text');
  const timerBadge = document.getElementById('quiz-timer-badge');
  if (timerText) timerText.textContent = `${window.quizSecondsLeft}s`;

  if (timerBadge) {
    if (window.quizSecondsLeft <= 15) {
      timerBadge.style.background = 'rgba(239, 68, 68, 0.25)';
      timerBadge.style.borderColor = '#EF4444';
      timerBadge.style.color = '#F87171';
    } else {
      timerBadge.style.background = window.isQuizLightMode ? '#FEF3C7' : 'rgba(248,200,59,0.18)';
      timerBadge.style.borderColor = window.isQuizLightMode ? '#D97706' : '#F8C83B';
      timerBadge.style.color = window.isQuizLightMode ? '#78350F' : '#FDE68A';
    }
  }
};

window.handleQuizTimeout = function() {
  if (window.isQuizAnswered) return;
  window.isQuizAnswered = true;
  if (typeof playSoundEffect === 'function') playSoundEffect('wrong');
  
  const qData = window.ACTIVE_QUIZ_DECK[window.currentQuizIndex];
  if (!qData) return;

  const btns = document.querySelectorAll('.quiz-opt-btn');
  btns.forEach((btn, i) => {
    btn.disabled = true;
    if (i === qData.correct) {
      btn.style.background = 'rgba(16, 185, 129, 0.25)';
      btn.style.borderColor = '#10B981';
      btn.style.color = '#059669';
    }
  });

  const fbBox = document.getElementById('quiz-feedback-box');
  const fbTitle = document.getElementById('quiz-feedback-title');
  const fbDesc = document.getElementById('quiz-feedback-desc');
  const mapLink = document.getElementById('quiz-map-link');

  if (fbBox) {
    fbBox.style.display = 'block';
    if (fbTitle) {
      fbTitle.textContent = '⏱️ समय समाप्त! सही उत्तर देखें:';
      fbTitle.style.color = '#EF4444';
    }
    if (fbDesc) {
      fbDesc.textContent = qData.desc;
      fbDesc.style.color = window.isQuizLightMode ? '#334155' : '#E2E8F0';
    }
    if (mapLink) {
      if (qData.map) {
        mapLink.href = qData.map;
        mapLink.style.display = 'inline';
      } else {
        mapLink.style.display = 'none';
      }
    }
  }
};

window.switchQuizCategory = function(cat, btnEl) {
  window.currentQuizCategory = cat;
  window.prepareActiveQuizDeck(cat);

  document.querySelectorAll('.quiz-cat-btn').forEach(b => {
    b.classList.remove('active');
    b.style.background = window.isQuizLightMode ? '#FEF3C7' : 'rgba(255,255,255,0.08)';
    b.style.color = window.isQuizLightMode ? '#78350F' : '#CBD5E1';
    b.style.border = window.isQuizLightMode ? '1px solid rgba(217, 119, 6, 0.3)' : '1px solid rgba(255,255,255,0.15)';
  });
  if (btnEl) {
    btnEl.classList.add('active');
    btnEl.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btnEl.style.color = '#1A0B2E';
    btnEl.style.border = 'none';
  }

  // Hide Result View & Show Main View
  const mainView = document.getElementById('quiz-main-view');
  const resultView = document.getElementById('quiz-result-view');
  if (mainView) mainView.style.display = 'block';
  if (resultView) resultView.style.display = 'none';

  window.startQuizTimer();
  window.renderCurrentQuiz();
};

window.renderCurrentQuiz = function() {
  window.isQuizAnswered = false;
  if (!window.ACTIVE_QUIZ_DECK || window.ACTIVE_QUIZ_DECK.length === 0) {
    window.prepareActiveQuizDeck(window.currentQuizCategory);
  }
  const qData = window.ACTIVE_QUIZ_DECK[window.currentQuizIndex];
  if (!qData) return;
  
  const qText = document.getElementById('quiz-question-text');
  if (qText) {
    qText.textContent = qData.q;
    qText.style.color = window.isQuizLightMode ? '#1A0B2E' : '#FFFDF8';
  }

  const pBadge = document.getElementById('quiz-progress-badge');
  if (pBadge) pBadge.textContent = `Q ${window.currentQuizIndex + 1} / ${window.ACTIVE_QUIZ_DECK.length}`;

  const fbBox = document.getElementById('quiz-feedback-box');
  if (fbBox) fbBox.style.display = 'none';

  const list = document.getElementById('quiz-options-list');
  if (list) {
    const letters = ['A', 'B', 'C', 'D'];
    const optBg = window.isQuizLightMode ? '#FFFFFF' : 'rgba(255,255,255,0.08)';
    const optBorder = window.isQuizLightMode ? '1.5px solid #FCD34D' : '1.5px solid rgba(255,255,255,0.18)';
    const optTextColor = window.isQuizLightMode ? '#1A0B2E' : '#FFFFFF';
    const badgeBg = window.isQuizLightMode ? '#FEF3C7' : 'rgba(248,200,59,0.25)';
    const badgeTextColor = window.isQuizLightMode ? '#92400E' : '#FDE68A';

    list.innerHTML = qData.opts.map((opt, i) => `
      <button onclick="selectQuizOption(${i})" class="quiz-opt-btn" style="width:100%; text-align:left; background:${optBg}; border:${optBorder}; color:${optTextColor}; padding:12px 14px; border-radius:14px; font-size:0.92rem; font-weight:800; cursor:pointer; display:flex; align-items:center; gap:10px; transition:transform 0.15s ease, box-shadow 0.15s ease; box-shadow:${window.isQuizLightMode ? '0 2px 8px rgba(0,0,0,0.05)' : 'none'};">
        <span style="background:${badgeBg}; color:${badgeTextColor}; width:28px; height:28px; border-radius:8px; display:inline-flex; align-items:center; justify-content:center; font-size:0.85rem; font-weight:900; flex-shrink:0; border:1px solid rgba(248,200,59,0.4);">${letters[i]}</span>
        <span style="flex:1; line-height:1.35; color:${optTextColor}; font-weight:800;">${opt}</span>
      </button>
    `).join('');
  }
};

window.selectQuizOption = function(idx) {
  if (window.isQuizAnswered) return;
  window.isQuizAnswered = true;
  window.stopQuizTimer();

  const qData = window.ACTIVE_QUIZ_DECK[window.currentQuizIndex];
  if (!qData) return;
  const isRight = (idx === qData.correct);

  if (isRight) {
    window.quizScore++;
  }

  const btns = document.querySelectorAll('.quiz-opt-btn');
  btns.forEach((btn, i) => {
    btn.disabled = true;
    if (i === qData.correct) {
      btn.style.background = window.isQuizLightMode ? '#DCFCE7' : 'rgba(16, 185, 129, 0.25)';
      btn.style.borderColor = '#10B981';
      btn.style.color = '#15803D';
      const sp = btn.querySelector('span:last-child');
      if (sp) sp.style.color = '#15803D';
    } else if (i === idx && !isRight) {
      btn.style.background = window.isQuizLightMode ? '#FEE2E2' : 'rgba(239, 68, 68, 0.25)';
      btn.style.borderColor = '#EF4444';
      btn.style.color = '#B91C1C';
      const sp = btn.querySelector('span:last-child');
      if (sp) sp.style.color = '#B91C1C';
    }
  });

  const fbBox = document.getElementById('quiz-feedback-box');
  const fbTitle = document.getElementById('quiz-feedback-title');
  const fbDesc = document.getElementById('quiz-feedback-desc');
  const mapLink = document.getElementById('quiz-map-link');

  if (fbBox) {
    fbBox.style.display = 'block';
    if (isRight) {
      if (fbTitle) {
        fbTitle.textContent = '🎉 शाबाश! सही जवाब! (+10 साधना अंक)';
        fbTitle.style.color = '#10B981';
      }
      if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
      if (typeof playSoundEffect === 'function') playSoundEffect('correct');
    } else {
      if (fbTitle) {
        fbTitle.textContent = '❌ गलत जवाब! सही उत्तर देखें:';
        fbTitle.style.color = '#EF4444';
      }
      if (typeof playSoundEffect === 'function') playSoundEffect('wrong');
    }
    if (fbDesc) {
      fbDesc.textContent = qData.desc;
      fbDesc.style.color = window.isQuizLightMode ? '#334155' : '#E2E8F0';
    }
    if (mapLink) {
      if (qData.map) {
        mapLink.href = qData.map;
        mapLink.style.display = 'inline';
      } else {
        mapLink.style.display = 'none';
      }
    }
  }
};

window.nextQuizQuestion = function() {
  if (window.currentQuizIndex < window.ACTIVE_QUIZ_DECK.length - 1) {
    window.currentQuizIndex++;
    window.startQuizTimer();
    window.renderCurrentQuiz();
  } else {
    window.showQuizCompletionView();
  }
};

window.showQuizCompletionView = function() {
  window.stopQuizTimer();

  if (window.quizScore > window.quizHighScore) {
    window.quizHighScore = window.quizScore;
    localStorage.setItem('sanatan_quiz_high_score', window.quizHighScore.toString());
  }

  const mainView = document.getElementById('quiz-main-view');
  const resultView = document.getElementById('quiz-result-view');
  const finalScoreEl = document.getElementById('quiz-final-score');
  const highScoreNumEl = document.getElementById('quiz-high-score-num');

  if (mainView) mainView.style.display = 'none';
  if (resultView) resultView.style.display = 'block';

  if (finalScoreEl) finalScoreEl.textContent = `${window.quizScore} / ${window.ACTIVE_QUIZ_DECK.length}`;
  if (highScoreNumEl) highScoreNumEl.textContent = `${window.quizHighScore}`;

  if (typeof triggerFlowerShower === 'function') {
    triggerFlowerShower();
    setTimeout(triggerFlowerShower, 500);
  }
};

window.restartQuizCurrentCategory = function() {
  const mainView = document.getElementById('quiz-main-view');
  const resultView = document.getElementById('quiz-result-view');
  if (mainView) mainView.style.display = 'block';
  if (resultView) resultView.style.display = 'none';

  // Load fresh questions from the database
  window.prepareActiveQuizDeck(window.currentQuizCategory);
  window.startQuizTimer();
  window.renderCurrentQuiz();
};

window.shareQuizScoreWhatsApp = function() {
  const catName = window.currentQuizCategory === 'india' ? 'भारत मंदिर' : (window.currentQuizCategory === 'world' ? 'विश्व मंदिर' : (window.currentQuizCategory === 'chalisa' ? 'चालीसा' : (window.currentQuizCategory === 'gita' ? 'गीता' : (window.currentQuizCategory === 'ramayana' ? 'रामायण' : 'संपूर्ण सनातन ज्ञान'))));
  const text = `🚩 *दिव्य प्रश्नोत्तरी (सनातन ज्ञान) में मेरी उपलब्धि!* 🚩\\nमैंने *${catName}* क्विज़ में *${window.quizScore} / ${window.ACTIVE_QUIZ_DECK.length}* अंक प्राप्त किए! 🏆\\nमेरा उच्च स्कोर: *${window.quizHighScore}* 🌟\\n\\nक्या आप मेरा रिकॉर्ड तोड़ सकते हैं? डाउनलोड करें 'भक्ति में लीन' ऐप और अपना ज्ञान परखें! 🕉️\\nhttp://localhost:8000`;
  
  if (navigator.share) {
    navigator.share({ title: 'सनातन ज्ञान क्विज़ उपलब्धि', text: text }).catch(() => {});
  } else {
    window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, '_blank');
  }
};

window.speakCurrentQuizQuestion = function() {
  if (!('speechSynthesis' in window)) {
    if (typeof showToast === 'function') showToast('ℹ️ आपका ब्राउज़र वॉइस सपोर्ट नहीं करता');
    return;
  }

  window.speechSynthesis.cancel();
  const qData = window.ACTIVE_QUIZ_DECK[window.currentQuizIndex];
  if (!qData) return;

  const speechText = `प्रश्न: ${qData.q}। विकल्प हैं: A: ${qData.opts[0]}। B: ${qData.opts[1]}। C: ${qData.opts[2]}। D: ${qData.opts[3]}।`;
  const utter = new SpeechSynthesisUtterance(speechText);
  utter.lang = 'hi-IN';
  utter.rate = 0.9;
  window.speechSynthesis.speak(utter);
};
"""

if start_js != -1 and end_js != -1:
    js = js[:start_js] + new_app_js + "\n\n" + js[end_js:]
else:
    js += "\n\n" + new_app_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Updated app.js with crystal-clear contrast and question count selection")
