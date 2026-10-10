import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace category chips to include Bookmarks chip
new_category_chips = """      <!-- Category Chips (User Requested Specific Categories + Bookmarks Revision) -->
      <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:12px; scrollbar-width:none;">
        <button onclick="switchQuizCategory('all', this)" class="quiz-cat-btn active" style="padding:6px 12px; font-size:0.78rem; font-weight:900; border-radius:14px; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; white-space:nowrap;">🎯 संपूर्ण (Mega)</button>
        <button onclick="switchQuizCategory('bookmarks', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">⭐ सहेजे गए (Bookmarks)</button>
        <button onclick="switchQuizCategory('god', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🪔 देवी-देवता / अवतार</button>
        <button onclick="switchQuizCategory('ved', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">📜 वेद एवं उपनिषद</button>
        <button onclick="switchQuizCategory('mahabharat', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">⚔️ महाभारत एवं गीता</button>
        <button onclick="switchQuizCategory('ramayan', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🏹 रामायण</button>
        <button onclick="switchQuizCategory('mantra', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🕉️ मंत्र एवं स्तोत्र</button>
        <button onclick="switchQuizCategory('aarti', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🪔 आरती</button>
        <button onclick="switchQuizCategory('chalisa', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">📖 चालीसा</button>
        <button onclick="switchQuizCategory('bhakti_sahitya', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🌸 भक्ति आंदोलन व साहित्य</button>
      </div>"""

# Replace in index.html
s_chip = html.find('<!-- Category Chips')
if s_chip != -1:
    e_chip = html.find('<!-- Main Question & Options Container', s_chip)
    html = html[:s_chip] + new_category_chips + "\n\n      " + html[e_chip:]

# Update Question Box Header with Bookmark Button
old_qbox_header = """          <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px;">
            <h4 id="quiz-question-text" style="font-size:1.02rem; color:#FFFDF8; font-weight:900; line-height:1.45; margin:0 0 10px 0; flex:1;">
              प्रश्न लोड हो रहा है...
            </h4>
            <!-- 🎙️ AI Voice Read Aloud -->
            <button onclick="speakCurrentQuizQuestion()" title="🎙️ AI हिंदी वॉइस से सुनें" style="background:rgba(248,200,59,0.25); border:1.5px solid #F8C83B; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
              🔊
            </button>
          </div>"""

new_qbox_header = """          <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px;">
            <h4 id="quiz-question-text" style="font-size:1.02rem; color:#FFFDF8; font-weight:900; line-height:1.45; margin:0 0 10px 0; flex:1;">
              प्रश्न लोड हो रहा है...
            </h4>
            <div style="display:flex; align-items:center; gap:6px; flex-shrink:0;">
              <!-- 🔖 Bookmark Question Button -->
              <button id="quiz-bookmark-btn" onclick="toggleCurrentQuestionBookmark()" title="प्रश्न सहेजें / बुकमार्क करें" style="background:rgba(248,200,59,0.2); border:1.5px solid #F8C83B; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center; transition:transform 0.15s ease;">
                🔖
              </button>
              <!-- 🎙️ AI Voice Read Aloud -->
              <button onclick="speakCurrentQuizQuestion()" title="🎙️ AI हिंदी वॉइस से सुनें" style="background:rgba(248,200,59,0.2); border:1.5px solid #F8C83B; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
                🔊
              </button>
            </div>
          </div>"""

if old_qbox_header in html:
    html = html.replace(old_qbox_header, new_qbox_header, 1)
else:
    # Try regex replace
    html = re.sub(r'<div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px;">[\s\S]*?<!-- 🎙️ AI Voice Read Aloud -->[\s\S]*?</button>\s*</div>', new_qbox_header, html, count=1)

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Updated index.html with Bookmark button and Bookmark Category Chip (v={ts})")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Bookmark logic in app.js
bookmark_js_methods = """
// 🔖 BOOKMARKS (SAVED QUESTIONS) SYSTEM
window.quizBookmarks = JSON.parse(localStorage.getItem('sanatan_quiz_bookmarks') || '[]');

window.isCurrentQuestionBookmarked = function() {
  if (!window.ACTIVE_QUIZ_DECK || window.ACTIVE_QUIZ_DECK.length === 0) return false;
  const qData = window.ACTIVE_QUIZ_DECK[window.currentQuizIndex];
  if (!qData) return false;
  return window.quizBookmarks.some(b => b.q === qData.q);
};

window.toggleCurrentQuestionBookmark = function() {
  if (!window.ACTIVE_QUIZ_DECK || window.ACTIVE_QUIZ_DECK.length === 0) return;
  const qData = window.ACTIVE_QUIZ_DECK[window.currentQuizIndex];
  if (!qData) return;

  const existingIdx = window.quizBookmarks.findIndex(b => b.q === qData.q);
  const btn = document.getElementById('quiz-bookmark-btn');

  if (existingIdx !== -1) {
    window.quizBookmarks.splice(existingIdx, 1);
    if (typeof showToast === 'function') showToast('✗ प्रश्न बुकमार्क से हटाया गया');
  } else {
    window.quizBookmarks.push(qData);
    if (typeof showToast === 'function') showToast('✓ प्रश्न बुकमार्क में सहेजा गया! 🔖');
    if (navigator.vibrate) navigator.vibrate(40);
  }

  localStorage.setItem('sanatan_quiz_bookmarks', JSON.stringify(window.quizBookmarks));
  window.updateBookmarkBtnUI();
};

window.updateBookmarkBtnUI = function() {
  const btn = document.getElementById('quiz-bookmark-btn');
  if (!btn) return;
  const isSaved = window.isCurrentQuestionBookmarked();

  if (isSaved) {
    btn.textContent = '⭐';
    btn.title = 'सहेजा गया (बुकमार्क से हटाएं)';
    btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btn.style.color = '#1A0B2E';
    btn.style.borderColor = '#F59E0B';
    btn.style.boxShadow = '0 0 10px rgba(248, 200, 59, 0.6)';
  } else {
    btn.textContent = '🔖';
    btn.title = 'प्रश्न सहेजें (बुकमार्क करें)';
    btn.style.background = window.isQuizLightMode ? '#FEF3C7' : 'rgba(248,200,59,0.2)';
    btn.style.color = window.isQuizLightMode ? '#78350F' : '#FDE68A';
    btn.style.borderColor = window.isQuizLightMode ? '#D97706' : '#F8C83B';
    btn.style.boxShadow = 'none';
  }
};
"""

# Insert bookmark methods before prepareActiveQuizDeck
target_fn = "window.prepareActiveQuizDeck = function(category) {"
if target_fn in js:
    js = js.replace(target_fn, bookmark_js_methods + "\n" + target_fn, 1)

# In prepareActiveQuizDeck, handle 'bookmarks' category
old_prepare = """  if (window.ALL_MCQS_DATA && window.ALL_MCQS_DATA.length > 0) {
    if (category === 'all' || category === 'mega') {
      pool = [...window.ALL_MCQS_DATA];
    } else {
      pool = window.ALL_MCQS_DATA.filter(q => q.category === category);
      if (pool.length < 5) {
        pool = [...window.ALL_MCQS_DATA];
      }
    }
  }"""

new_prepare = """  if (category === 'bookmarks') {
    if (window.quizBookmarks && window.quizBookmarks.length > 0) {
      pool = [...window.quizBookmarks];
    } else {
      // Empty bookmarks state
      window.ACTIVE_QUIZ_DECK = [{
        q: 'आपने अभी तक कोई प्रश्न सहेजा (Bookmark) नहीं है।\\n\\n💡 किसी भी प्रश्न को हल करते समय ऊपर दिए गए 🔖 बटन पर टैप करके उसे यहाँ सहेजें!',
        opts: ['संपूर्ण क्विज़ खेलें', 'रामायण क्विज़ खेलें', 'गीता क्विज़ खेलें', 'वेद क्विज़ खेलें'],
        correct: 0,
        desc: 'बुकमार्क किए गए कठिन प्रश्नों का आप यहाँ कभी भी दोहराव (Revision) कर सकते हैं।'
      }];
      window.currentQuizIndex = 0;
      window.quizScore = 0;
      window.isQuizAnswered = false;
      return;
    }
  } else if (window.ALL_MCQS_DATA && window.ALL_MCQS_DATA.length > 0) {
    if (category === 'all' || category === 'mega') {
      pool = [...window.ALL_MCQS_DATA];
    } else {
      pool = window.ALL_MCQS_DATA.filter(q => q.category === category);
      if (pool.length === 0) {
        pool = [...window.ALL_MCQS_DATA];
      }
    }
  }"""

if old_prepare in js:
    js = js.replace(old_prepare, new_prepare, 1)

# In renderCurrentQuiz, add updateBookmarkBtnUI() call
old_render = "window.renderCurrentQuiz = function() {"
new_render = """window.renderCurrentQuiz = function() {
  window.updateBookmarkBtnUI();"""

if old_render in js:
    js = js.replace(old_render, new_render, 1)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Updated app.js with complete Bookmark persistence & Revision Deck")
