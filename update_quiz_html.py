import re, sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html modal markup
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

rich_quiz_modal_html = """  <!-- 🎯 DEDICATED SACRED MCQ QUIZ HUB MODAL 🎯 -->
  <div id="quiz-hub-modal" style="display:none; position:fixed; inset:0; z-index:100025; background:rgba(10,2,18,0.94); backdrop-filter:blur(30px); -webkit-backdrop-filter:blur(30px); align-items:center; justify-content:center; padding:1.2rem; overflow-y:auto;">
    <div id="quiz-hub-card" style="width:100%; max-width:440px; background:linear-gradient(160deg, #2A0948 0%, #150426 60%, #0B0116 100%); border:2px solid rgba(248,200,59,0.5); border-radius:32px; padding:1.5rem 1.3rem; box-shadow:0 20px 60px rgba(0,0,0,0.85); position:relative; margin:auto 0; transition:all 0.3s ease;">
      
      <!-- Top Bar: Title, Theme Toggle, Timer, Question Badge, Close Button -->
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
        <div style="font-size:1.15rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
          <span>🎯</span> <span id="quiz-header-title">दिव्य प्रश्नोत्तरी</span>
        </div>
        <div style="display:flex; align-items:center; gap:6px;">
          <!-- 🌓 Theme Toggle Button -->
          <button id="quiz-theme-btn" onclick="toggleQuizTheme()" title="थीम बदलें (Dark / Light)" style="background:rgba(255,255,255,0.1); border:1px solid rgba(248,200,59,0.3); color:#FDE68A; width:32px; height:32px; border-radius:50%; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
            ☀️
          </button>
          
          <!-- ⏱️ 120s Timer Badge -->
          <div id="quiz-timer-badge" style="display:flex; align-items:center; gap:4px; font-size:0.78rem; font-weight:800; background:rgba(248,200,59,0.18); border:1px solid #F8C83B; color:#FDE68A; padding:4px 9px; border-radius:12px;">
            <span>⏱️</span> <span id="quiz-timer-text">120s</span>
          </div>

          <!-- Q Progress Badge -->
          <span id="quiz-progress-badge" style="font-size:0.75rem; font-weight:800; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; padding:4px 9px; border-radius:12px;">
            Q 1 / 10
          </span>

          <!-- Close Button -->
          <button onclick="closeQuizHubModal()" style="background:rgba(255,255,255,0.12); border:none; color:#FDE68A; width:32px; height:32px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
        </div>
      </div>

      <!-- Category Chips -->
      <div style="display:flex; gap:6px; overflow-x:auto; padding-bottom:8px; margin-bottom:12px; scrollbar-width:none;">
        <button onclick="switchQuizCategory('india', this)" class="quiz-cat-btn active" style="padding:6px 14px; font-size:0.78rem; font-weight:800; border-radius:14px; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; white-space:nowrap;">🏛️ भारत मंदिर</button>
        <button onclick="switchQuizCategory('world', this)" class="quiz-cat-btn" style="padding:6px 14px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">🌍 विश्व मंदिर</button>
        <button onclick="switchQuizCategory('chalisa', this)" class="quiz-cat-btn" style="padding:6px 14px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">📜 चालीसा</button>
        <button onclick="switchQuizCategory('gita', this)" class="quiz-cat-btn" style="padding:6px 14px; font-size:0.78rem; font-weight:800; border-radius:14px; background:rgba(255,255,255,0.08); color:#CBD5E1; border:1px solid rgba(255,255,255,0.15); cursor:pointer; white-space:nowrap;">📖 गीता</button>
      </div>

      <!-- Main Question & Options Container -->
      <div id="quiz-main-view">
        <!-- Question Box -->
        <div id="quiz-question-box" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(248,200,59,0.25); border-radius:20px; padding:14px; margin-bottom:12px;">
          <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:10px;">
            <h4 id="quiz-question-text" style="font-size:1.02rem; color:#FFFDF8; font-weight:800; line-height:1.45; margin:0 0 10px 0; flex:1;">
              प्रश्न लोड हो रहा है...
            </h4>
            <!-- 🎙️ AI Voice Read Aloud -->
            <button onclick="speakCurrentQuizQuestion()" title="🎙️ AI हिंदी वॉइस से सुनें" style="background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
              🔊
            </button>
          </div>

          <div id="quiz-options-list" style="display:flex; flex-direction:column; gap:9px;">
            <!-- Options rendered dynamically -->
          </div>

          <!-- Dynamic Feedback Area -->
          <div id="quiz-feedback-box" style="display:none; margin-top:12px; padding:12px; border-radius:14px; background:rgba(16,185,129,0.15); border:1px solid #10B981;">
            <div id="quiz-feedback-title" style="font-size:0.92rem; font-weight:900; color:#34D399; margin-bottom:4px;">
              🎉 शाबाश! सही जवाब! (+10 साधना अंक)
            </div>
            <p id="quiz-feedback-desc" style="font-size:0.82rem; color:#E2E8F0; margin:0 0 10px 0; line-height:1.45;">
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

# Replace quiz-hub-modal in index.html
old_modal_start = html.find('<!-- 🎯 DEDICATED SACRED MCQ QUIZ HUB MODAL 🎯 -->')
if old_modal_start != -1:
    old_modal_end = html.find('<!-- ═════════════════════════════════════════════════════════════════', old_modal_start)
    html = html[:old_modal_start] + rich_quiz_modal_html + "\n\n  " + html[old_modal_end:]
    print("✓ Updated #quiz-hub-modal in index.html")
else:
    print("old_modal_start not found in index.html")

# Bump version in index.html
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Saved index.html")
