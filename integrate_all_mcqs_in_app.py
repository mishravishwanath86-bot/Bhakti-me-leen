import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the Quiz logic in app.js with the dynamic 800+ Questions engine
start_idx = js.find('// 4. MCQ Quiz Hub Logic')
if start_idx == -1:
    start_idx = js.find('// 🎯 COMPLETE SACRED MCQ QUIZ ENGINE')

end_idx = js.find('// 5. Kalyan Kund Seva Daan Logic')

dynamic_quiz_js = """// ══════════════════════════════════════════════════════════════════════════════
// 🎯 COMPLETE DYNAMIC SACRED MCQ QUIZ ENGINE (791+ Questions from Database)
// ══════════════════════════════════════════════════════════════════════════════

window.ALL_MCQS_DATA = [];
window.ACTIVE_QUIZ_DECK = [];
window.currentQuizCategory = 'all';
window.currentQuizIndex = 0;
window.quizScore = 0;
window.quizHighScore = parseInt(localStorage.getItem('sanatan_quiz_high_score') || '0', 10);
window.isQuizAnswered = false;
window.quizTimerInterval = null;
window.quizSecondsLeft = 120;
window.isQuizLightMode = localStorage.getItem('sanatan_quiz_theme') === 'light';

// Fetch all 791+ questions on app init
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

// Pick 10 fresh random questions from the chosen category or entire database
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

  // Fallback if network was slow
  if (pool.length === 0 && window.QUIZ_DECK) {
    const staticList = window.QUIZ_DECK[category] || window.QUIZ_DECK.india || [];
    pool = staticList.map((q, i) => ({
      id: i + 1,
      question: q.q,
      options: q.opts,
      correct_answer: q.correct,
      explanation: q.desc,
      map: q.map
    }));
  }

  // Shuffle pool using Fisher-Yates
  const shuffled = [...pool].sort(() => Math.random() - 0.5);
  // Pick 10 questions (or all if < 10)
  window.ACTIVE_QUIZ_DECK = shuffled.slice(0, 10).map(item => ({
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
};

window.applyQuizTheme = function() {
  const card = document.getElementById('quiz-hub-card');
  const themeBtn = document.getElementById('quiz-theme-btn');
  const title = document.getElementById('quiz-header-title');
  const qBox = document.getElementById('quiz-question-box');
  const qText = document.getElementById('quiz-question-text');

  if (!card) return;

  if (window.isQuizLightMode) {
    card.style.background = 'linear-gradient(160deg, #FFFDF8 0%, #FEF3C7 100%)';
    card.style.borderColor = '#D97706';
    card.style.color = '#1A0B2E';
    if (themeBtn) themeBtn.textContent = '🌙';
    if (title) title.style.color = '#78350F';
    if (qBox) {
      qBox.style.background = 'rgba(255,255,255,0.85)';
      qBox.style.borderColor = '#F59E0B';
    }
    if (qText) qText.style.color = '#1A0B2E';
  } else {
    card.style.background = 'linear-gradient(160deg, #2A0948 0%, #150426 60%, #0B0116 100%)';
    card.style.borderColor = 'rgba(248,200,59,0.5)';
    card.style.color = '#FFFDF8';
    if (themeBtn) themeBtn.textContent = '☀️';
    if (title) title.style.color = '#FFFDF8';
    if (qBox) {
      qBox.style.background = 'rgba(255,255,255,0.06)';
      qBox.style.borderColor = 'rgba(248,200,59,0.25)';
    }
    if (qText) qText.style.color = '#FFFDF8';
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
      timerBadge.style.background = 'rgba(248,200,59,0.18)';
      timerBadge.style.borderColor = '#F8C83B';
      timerBadge.style.color = '#FDE68A';
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
      btn.style.color = '#34D399';
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
      fbTitle.style.color = '#F87171';
    }
    if (fbDesc) fbDesc.textContent = qData.desc;
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
    b.style.background = 'rgba(255,255,255,0.08)';
    b.style.color = '#CBD5E1';
    b.style.border = '1px solid rgba(255,255,255,0.15)';
  });
  if (btnEl) {
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
  if (qText) qText.textContent = qData.q;

  const pBadge = document.getElementById('quiz-progress-badge');
  if (pBadge) pBadge.textContent = `Q ${window.currentQuizIndex + 1} / ${window.ACTIVE_QUIZ_DECK.length}`;

  const fbBox = document.getElementById('quiz-feedback-box');
  if (fbBox) fbBox.style.display = 'none';

  const list = document.getElementById('quiz-options-list');
  if (list) {
    const letters = ['A', 'B', 'C', 'D'];
    list.innerHTML = qData.opts.map((opt, i) => `
      <button onclick="selectQuizOption(${i})" class="quiz-opt-btn" style="width:100%; text-align:left; background:rgba(255,255,255,0.08); border:1.5px solid rgba(255,255,255,0.15); color:${window.isQuizLightMode ? '#1A0B2E' : '#FFF'}; padding:11px 14px; border-radius:14px; font-size:0.88rem; font-weight:700; cursor:pointer; display:flex; align-items:center; gap:10px; transition:transform 0.15s ease;">
        <span style="background:rgba(248,200,59,0.25); color:#FDE68A; width:26px; height:26px; border-radius:8px; display:inline-flex; align-items:center; justify-content:center; font-size:0.8rem; font-weight:900; flex-shrink:0;">${letters[i]}</span>
        <span style="flex:1;">${opt}</span>
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
      btn.style.background = 'rgba(16, 185, 129, 0.25)';
      btn.style.borderColor = '#10B981';
      btn.style.color = '#34D399';
    } else if (i === idx && !isRight) {
      btn.style.background = 'rgba(239, 68, 68, 0.25)';
      btn.style.borderColor = '#EF4444';
      btn.style.color = '#F87171';
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
        fbTitle.style.color = '#34D399';
      }
      if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
      if (typeof playSoundEffect === 'function') playSoundEffect('correct');
    } else {
      if (fbTitle) {
        fbTitle.textContent = '❌ गलत जवाब! सही उत्तर देखें:';
        fbTitle.style.color = '#F87171';
      }
      if (typeof playSoundEffect === 'function') playSoundEffect('wrong');
    }
    if (fbDesc) fbDesc.textContent = qData.desc;
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

  // Load a brand new set of 10 random questions from the database!
  window.prepareActiveQuizDeck(window.currentQuizCategory);
  window.startQuizTimer();
  window.renderCurrentQuiz();
};

window.shareQuizScoreWhatsApp = function() {
  const catName = window.currentQuizCategory === 'india' ? 'भारत मंदिर' : (window.currentQuizCategory === 'world' ? 'विश्व मंदिर' : (window.currentQuizCategory === 'chalisa' ? 'चालीसा' : (window.currentQuizCategory === 'gita' ? 'गीता' : 'संपूर्ण सनातन ज्ञान')));
  const text = `🚩 *दिव्य प्रश्नोत्तरी (सनातन ज्ञान) में मेरी उपलब्धि!* 🚩\nमैंने *${catName}* क्विज़ में *${window.quizScore} / ${window.ACTIVE_QUIZ_DECK.length}* अंक प्राप्त किए! 🏆\nमेरा उच्च स्कोर: *${window.quizHighScore}* 🌟\n\nक्या आप मेरा रिकॉर्ड तोड़ सकते हैं? डाउनलोड करें 'भक्ति में लीन' ऐप और अपना ज्ञान परखें! 🕉️\nhttp://localhost:8000`;
  
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

if start_idx != -1 and end_idx != -1:
    js = js[:start_idx] + dynamic_quiz_js + "\n\n" + js[end_idx:]
    print("✓ Replaced with dynamic 791+ MCQ Engine in app.js")
else:
    js += "\n\n" + dynamic_quiz_js
    print("✓ Appended dynamic 791+ MCQ Engine in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Update version in index.html
import time
ts = int(time.time())
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Updated app.js and bumped index.html version to {ts}")
