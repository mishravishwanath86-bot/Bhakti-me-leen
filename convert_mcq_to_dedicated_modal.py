import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("CONVERTING HOME PAGE MCQ TO COMPACT CARD + DEDICATED FULL QUIZ MODAL")
print("=" * 80)

# 1. Update index.html
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Compact Home Page Banner
home_quiz_card_html = """      <!-- 🎯 SACRED KNOWLEDGE ZONE (QUIZ HUB ENTRY CARD) 🎯 -->
      <div onclick="openQuizHubModal()" style="margin: 0 1.2rem 1.4rem; background: radial-gradient(circle at 70% 30%, #3B1153 0%, #1F072C 60%, #120320 100%); border: 1.5px solid rgba(248,200,59,0.45); border-radius: 24px; padding: 1.2rem; cursor: pointer; box-shadow: 0 10px 30px rgba(0,0,0,0.5); position: relative; overflow: hidden; transition: transform 0.2s ease;">
        <div style="position:absolute; -right:15px; -bottom:15px; font-size:4.5rem; opacity:0.12; select-none; pointer-events:none;">🎯</div>
        
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
          <div style="font-size:0.75rem; font-weight:800; color:#FDE68A; background:rgba(248,200,59,0.2); border:1px solid rgba(248,200,59,0.4); padding:3px 10px; border-radius:12px; display:inline-flex; align-items:center; gap:5px;">
            <span>✨</span> दैनिक ज्ञान महाकुंभ
          </div>
          <span style="font-size:0.75rem; color:#34D399; font-weight:800; background:rgba(16,185,129,0.18); border:1px solid #10B981; padding:3px 8px; border-radius:10px;">
            +10 साधना अंक
          </span>
        </div>

        <h3 style="font-size:1.15rem; font-weight:900; color:#FFFDF8; margin:0 0 4px 0; display:flex; align-items:center; gap:6px;">
          <span>🎯</span> दैनिक दिव्य प्रश्नोत्तरी (MCQ Hub)
        </h3>
        <p style="font-size:0.8rem; color:#CBD5E1; margin:0 0 12px 0; line-height:1.4;">
          भारत के प्रमुख मंदिर, विश्व तीर्थ, चालीसा एवं श्रीमद्भगवद्गीता ज्ञान का परीक्षण करें
        </p>

        <div style="display:flex; align-items:center; justify-content:space-between;">
          <div style="display:flex; gap:6px; font-size:0.72rem; color:#FDE68A;">
            <span>🏛️ मंदिर</span> • <span>🌍 विश्व</span> • <span>📜 चालीसा</span> • <span>📖 गीता</span>
          </div>
          <button onclick="event.stopPropagation(); openQuizHubModal()" style="background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.82rem; font-weight:900; padding:8px 18px; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); display:flex; align-items:center; gap:5px;">
            <span>MCQ खेलें</span> ❯
          </button>
        </div>
      </div>"""

# Dedicated Full Quiz Modal (Placed before </body>)
dedicated_quiz_modal_html = """  <!-- 🎯 DEDICATED SACRED MCQ QUIZ HUB MODAL 🎯 -->
  <div id="quiz-hub-modal" style="display:none; position:fixed; inset:0; z-index:100025; background:rgba(10,2,18,0.94); backdrop-filter:blur(30px); -webkit-backdrop-filter:blur(30px); align-items:center; justify-content:center; padding:1.2rem; overflow-y:auto;">
    <div style="width:100%; max-width:420px; background:linear-gradient(160deg, #2A0948 0%, #150426 60%, #0B0116 100%); border:2px solid rgba(248,200,59,0.45); border-radius:32px; padding:1.6rem 1.4rem; box-shadow:0 20px 60px rgba(0,0,0,0.85); position:relative; margin:auto 0;">
      
      <!-- Top Bar -->
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px;">
        <div style="font-size:1.1rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
          <span>🎯</span> दिव्य प्रश्नोत्तरी
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
          <span id="quiz-progress-badge" style="font-size:0.75rem; font-weight:800; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; padding:3px 8px; border-radius:10px;">
            Q 1 / 4
          </span>
          <button onclick="closeQuizHubModal()" style="background:rgba(255,255,255,0.12); border:none; color:#FDE68A; width:32px; height:32px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
        </div>
      </div>

      <!-- Category Chips -->
      <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:14px; scrollbar-width:none;">
        <button onclick="switchQuizCategory('india', this)" class="quiz-cat-btn active" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; white-space:nowrap;">🏛️ भारत मंदिर</button>
        <button onclick="switchQuizCategory('world', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🌍 विश्व मंदिर</button>
        <button onclick="switchQuizCategory('chalisa', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">📜 चालीसा</button>
        <button onclick="switchQuizCategory('gita', this)" class="quiz-cat-btn" style="padding:6px 12px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">📖 गीता</button>
      </div>

      <!-- Question Box -->
      <div id="quiz-question-box" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(248,200,59,0.25); border-radius:20px; padding:16px; margin-bottom:12px;">
        <h4 id="quiz-question-text" style="font-size:1rem; color:#FFFDF8; font-weight:800; line-height:1.45; margin:0 0 14px 0;">
          विश्व में 1200 से अधिक नक्काशीदार खंभों वाला सबसे लंबा गलियारा किस मंदिर में है?
        </h4>

        <div id="quiz-options-list" style="display:flex; flex-direction:column; gap:9px;">
          <!-- Options rendered dynamically -->
        </div>

        <!-- Dynamic Feedback Area -->
        <div id="quiz-feedback-box" style="display:none; margin-top:14px; padding:12px; border-radius:14px; background:rgba(16,185,129,0.15); border:1px solid #10B981;">
          <div id="quiz-feedback-title" style="font-size:0.9rem; font-weight:900; color:#34D399; margin-bottom:4px;">
            🎉 शाबाश! सही जवाब! (+10 साधना अंक)
          </div>
          <p id="quiz-feedback-desc" style="font-size:0.8rem; color:#E2E8F0; margin:0 0 10px 0; line-height:1.45;">
            रामेश्वरम का रामनाथस्वामी मंदिर 1,220 मीटर लंबे विश्व के सबसे भव्य खंभों वाले गलियारे के लिए प्रसिद्ध है।
          </p>
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <a id="quiz-map-link" href="https://www.google.com/maps/search/?api=1&query=Ramanathaswamy+Temple+Rameswaram" target="_blank" style="font-size:0.75rem; color:#FDE68A; text-decoration:underline; font-weight:800;">📍 गूगल मैप पर देखें</a>
            <button onclick="nextQuizQuestion()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-size:0.8rem; font-weight:900; padding:6px 14px; border-radius:12px; cursor:pointer;">अगला प्रश्न ❯</button>
          </div>
        </div>

      </div>

    </div>
  </div>"""

# Replace the embedded large quiz on #page-home with the clean compact Entry Card
pos_old_quiz = html.find('<!-- 🎯 INTERACTIVE SACRED KNOWLEDGE ZONE (MCQ & GITA QUIZ HUB) 🎯 -->')
if pos_old_quiz != -1:
    pos_next_sec = html.find('<!-- 🙏 KALYAN KUND', pos_old_quiz)
    html = html[:pos_old_quiz] + home_quiz_card_html + "\n\n" + html[pos_next_sec:]
    print("✓ Replaced embedded home quiz with clean compact Entry Card")

# Insert Dedicated Full Quiz Modal before </body>
if 'id="quiz-hub-modal"' not in html:
    pos_body = html.find('</body>')
    html = html[:pos_body] + dedicated_quiz_modal_html + "\n\n" + html[pos_body:]
    print("✓ Inserted #quiz-hub-modal before </body>")

# Bump cache buster
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ Updated index.html")

# 2. Update app.js modal open/close functions
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

quiz_modal_js = """
// 🎯 Dedicated Quiz Hub Modal Controller
window.openQuizHubModal = function() {
  const modal = document.getElementById('quiz-hub-modal');
  if (modal) {
    modal.style.display = 'flex';
    window.renderCurrentQuiz();
    if (navigator.vibrate) navigator.vibrate(30);
  }
};

window.closeQuizHubModal = function() {
  const modal = document.getElementById('quiz-hub-modal');
  if (modal) modal.style.display = 'none';
};
"""

if 'window.openQuizHubModal' not in js:
    js += "\n\n" + quiz_modal_js.strip() + "\n"
    with open(app_js_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("✓ Added openQuizHubModal and closeQuizHubModal in app.js")

print("=" * 80)
print("CONVERSION TO DEDICATED QUIZ MODAL COMPLETED SUCCESSFULLY")
print("=" * 80)
