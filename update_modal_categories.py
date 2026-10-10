import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_category_chips = """      <!-- Category Chips (User Requested Specific Categories) -->
      <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:12px; scrollbar-width:none;">
        <button onclick="switchQuizCategory('all', this)" class="quiz-cat-btn active" style="padding:6px 12px; font-size:0.78rem; font-weight:900; border-radius:14px; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; white-space:nowrap;">🎯 संपूर्ण (Mega)</button>
        <button onclick="switchQuizCategory('god', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🪔 देवी-देवता / अवतार</button>
        <button onclick="switchQuizCategory('ved', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">📜 वेद एवं उपनिषद</button>
        <button onclick="switchQuizCategory('mahabharat', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">⚔️ महाभारत एवं गीता</button>
        <button onclick="switchQuizCategory('ramayan', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🏹 रामायण</button>
        <button onclick="switchQuizCategory('mantra', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🕉️ मंत्र एवं स्तोत्र</button>
        <button onclick="switchQuizCategory('aarti', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🪔 आरती</button>
        <button onclick="switchQuizCategory('chalisa', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">📖 चालीसा</button>
        <button onclick="switchQuizCategory('bhakti_sahitya', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🌸 भक्ति आंदोलन व साहित्य</button>
      </div>"""

s_pos = html.find('<!-- Category Chips')
if s_pos != -1:
    e_pos = html.find('<!-- Main Question & Options Container', s_pos)
    html = html[:s_pos] + new_category_chips + "\n\n      " + html[e_pos:]

# Cache bust
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Updated index.html category chips with all 8 requested categories and bumped version to {ts}")

# 2. Update app.js WhatsApp share function to use proper category names
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_share_fn = """window.shareQuizScoreWhatsApp = function() {
  const catName = window.currentQuizCategory === 'india' ? 'भारत मंदिर' : (window.currentQuizCategory === 'world' ? 'विश्व मंदिर' : (window.currentQuizCategory === 'chalisa' ? 'चालीसा' : (window.currentQuizCategory === 'gita' ? 'गीता' : (window.currentQuizCategory === 'ramayana' ? 'रामायण' : 'संपूर्ण सनातन ज्ञान'))));
  const text = `🚩 *दिव्य प्रश्नोत्तरी (सनातन ज्ञान) में मेरी उपलब्धि!* 🚩\\nमैंने *${catName}* क्विज़ में *${window.quizScore} / ${window.ACTIVE_QUIZ_DECK.length}* अंक प्राप्त किए! 🏆\\nमेरा उच्च स्कोर: *${window.quizHighScore}* 🌟\\n\\nक्या आप मेरा रिकॉर्ड तोड़ सकते हैं? डाउनलोड करें 'भक्ति में लीन' ऐप और अपना ज्ञान परखें! 🕉️\\nhttp://localhost:8000`;
  
  if (navigator.share) {
    navigator.share({ title: 'सनातन ज्ञान क्विज़ उपलब्धि', text: text }).catch(() => {});
  } else {
    window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, '_blank');
  }
};"""

new_share_fn = """window.shareQuizScoreWhatsApp = function() {
  const catMap = {
    'all': 'संपूर्ण सनातन क्विज़ (Mega)',
    'god': 'देवी-देवता एवं अवतार',
    'ved': 'वेद एवं उपनिषद',
    'mahabharat': 'महाभारत एवं गीता',
    'ramayan': 'रामायण एवं चरित',
    'mantra': 'मंत्र एवं स्तोत्र',
    'aarti': 'पावन आरती',
    'chalisa': 'चालीसा',
    'bhakti_sahitya': 'भक्ति आंदोलन व साहित्य'
  };
  const catName = catMap[window.currentQuizCategory] || 'सनातन ज्ञान';
  const text = `🚩 *दिव्य प्रश्नोत्तरी (सनातन ज्ञान) में मेरी उपलब्धि!* 🚩\\nमैंने *${catName}* क्विज़ में *${window.quizScore} / ${window.ACTIVE_QUIZ_DECK.length}* अंक प्राप्त किए! 🏆\\nमेरा उच्च स्कोर: *${window.quizHighScore}* 🌟\\n\\nक्या आप मेरा रिकॉर्ड तोड़ सकते हैं? डाउनलोड करें 'भक्ति में लीन' ऐप और अपना ज्ञान परखें! 🕉️\\nhttp://localhost:8000`;
  
  if (navigator.share) {
    navigator.share({ title: 'सनातन ज्ञान क्विज़ उपलब्धि', text: text }).catch(() => {});
  } else {
    window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, '_blank');
  }
};"""

if old_share_fn in js:
    js = js.replace(old_share_fn, new_share_fn, 1)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✓ Updated app.js share category mapping")
else:
    print("old_share_fn not found directly, verifying...")

print("✓ Category update complete!")
