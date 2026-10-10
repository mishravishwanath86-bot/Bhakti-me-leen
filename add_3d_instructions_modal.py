import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Add 3D Instruction Modal & Top Bar Button to index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Info button in Top Glass Bar of 3D Mandir
old_top_actions = """      <!-- Right Actions: Day/Night & Sound -->
      <div style="display:flex; align-items:center; gap:6px;">
        <button id="mandir-lighting-toggle-btn" onclick="toggle3DMandirLighting()" title="प्रकाश बदलें (दिन / आरती रात्रि)" style="width:36px; height:36px; border-radius:50%; background:rgba(255,255,255,0.12); border:1.5px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
          🌙
        </button>
        <button id="mandir-sound-toggle-btn" onclick="toggle3DMandirSound()" title="मंत्र ध्वनि (Mute / Unmute)" style="width:36px; height:36px; border-radius:50%; background:rgba(255,255,255,0.12); border:1.5px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
          🔊
        </button>
      </div>"""

new_top_actions = """      <!-- Right Actions: Instructions, Day/Night & Sound -->
      <div style="display:flex; align-items:center; gap:6px;">
        <button onclick="open3DInstructionsModal()" title="3D दर्शन निर्देश (Instructions Guide)" style="width:36px; height:36px; border-radius:50%; background:rgba(248,200,59,0.2); border:1.5px solid #F8C83B; color:#FDE68A; font-size:1rem; font-weight:900; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 0 10px rgba(248,200,59,0.3);">
          ℹ️
        </button>
        <button id="mandir-lighting-toggle-btn" onclick="toggle3DMandirLighting()" title="प्रकाश बदलें (दिन / आरती रात्रि)" style="width:36px; height:36px; border-radius:50%; background:rgba(255,255,255,0.12); border:1.5px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
          🌙
        </button>
        <button id="mandir-sound-toggle-btn" onclick="toggle3DMandirSound()" title="मंत्र ध्वनि (Mute / Unmute)" style="width:36px; height:36px; border-radius:50%; background:rgba(255,255,255,0.12); border:1.5px solid rgba(248,200,59,0.4); color:#FDE68A; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
          🔊
        </button>
      </div>"""

if old_top_actions in html:
    html = html.replace(old_top_actions, new_top_actions)
    print("✓ Added Info Guide button to 3D Mandir top-bar")

# 3D Navigation Instructions Modal HTML
instructions_modal_html = """
    <!-- ℹ️ 3D MODEL & MANDIR NAVIGATION INSTRUCTIONS MODAL (दर्शन निर्देश) ℹ️ -->
    <div id="mandir-3d-instructions-modal" style="display:none; position:absolute; inset:0; z-index:100095; background:rgba(7,1,16,0.92); backdrop-filter:blur(22px); -webkit-backdrop-filter:blur(22px); align-items:center; justify-content:center; padding:1.2rem;">
      <div style="width:100%; max-width:380px; background:linear-gradient(165deg, #2D1047 0%, #1A052E 50%, #0D0218 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.4rem 1.2rem; text-align:left; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease;">
        
        <!-- Header & Close -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:14px; border-bottom:1px solid rgba(248,200,59,0.25); pb-2;">
          <div>
            <h3 style="font-size:1.15rem; font-weight:900; color:#FFFDF8; margin:0; display:flex; align-items:center; gap:6px;">
              <span>🏛️</span> 3D मंदिर दर्शन निर्देश
            </h3>
            <div style="font-size:0.72rem; color:#FDE68A; font-weight:700; margin-top:2px;">View & Navigate 3D Temple</div>
          </div>
          <button onclick="close3DInstructionsModal()" style="background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:32px; height:32px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
        </div>

        <!-- Instruction Card 1: Rotate View -->
        <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:10px 12px; margin-bottom:10px;">
          <div style="font-size:0.8rem; font-weight:900; color:#FDE68A; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
            <span>🔄</span> Rotate View / 360° परिक्रमा घुमाएं
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
            <div style="background:rgba(0,0,0,0.25); border-radius:12px; padding:6px; text-align:center;">
              <div style="font-size:1.4rem; margin-bottom:2px;">🖱️</div>
              <div style="font-size:0.68rem; color:#FFFDF8; font-weight:800;">Left-Click & Drag</div>
              <div style="font-size:0.62rem; color:#CBD5E1;">माउस बायां क्लिक</div>
            </div>
            <div style="background:rgba(0,0,0,0.25); border-radius:12px; padding:6px; text-align:center;">
              <div style="font-size:1.4rem; margin-bottom:2px;">👆</div>
              <div style="font-size:0.68rem; color:#FFFDF8; font-weight:800;">Press & Drag</div>
              <div style="font-size:0.62rem; color:#CBD5E1;">उंगली से स्वाइप</div>
            </div>
          </div>
        </div>

        <!-- Instruction Card 2: Pan / Move View -->
        <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:10px 12px; margin-bottom:10px;">
          <div style="font-size:0.8rem; font-weight:900; color:#FDE68A; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
            <span>↔️</span> Pan View / दृश्य इधर-उधर करें
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
            <div style="background:rgba(0,0,0,0.25); border-radius:12px; padding:6px; text-align:center;">
              <div style="font-size:1.4rem; margin-bottom:2px;">🖱️</div>
              <div style="font-size:0.68rem; color:#FFFDF8; font-weight:800;">Right-Click / Shift</div>
              <div style="font-size:0.62rem; color:#CBD5E1;">दायां क्लिक व ड्रैग</div>
            </div>
            <div style="background:rgba(0,0,0,0.25); border-radius:12px; padding:6px; text-align:center;">
              <div style="font-size:1.4rem; margin-bottom:2px;">✌️</div>
              <div style="font-size:0.68rem; color:#FFFDF8; font-weight:800;">Two-Finger Drag</div>
              <div style="font-size:0.62rem; color:#CBD5E1;">दो उंगलियों से स्वाइप</div>
            </div>
          </div>
        </div>

        <!-- Instruction Card 3: Zoom In / Out -->
        <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:10px 12px; margin-bottom:14px;">
          <div style="font-size:0.8rem; font-weight:900; color:#FDE68A; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
            <span>🔍</span> Zoom In / Out / निकट व दूर दर्शन
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
            <div style="background:rgba(0,0,0,0.25); border-radius:12px; padding:6px; text-align:center;">
              <div style="font-size:1.4rem; margin-bottom:2px;">🖲️</div>
              <div style="font-size:0.68rem; color:#FFFDF8; font-weight:800;">Scroll Wheel</div>
              <div style="font-size:0.62rem; color:#CBD5E1;">माउस व्हील घुमाएं</div>
            </div>
            <div style="background:rgba(0,0,0,0.25); border-radius:12px; padding:6px; text-align:center;">
              <div style="font-size:1.4rem; margin-bottom:2px;">🤏</div>
              <div style="font-size:0.68rem; color:#FFFDF8; font-weight:800;">Pinch In / Out</div>
              <div style="font-size:0.62rem; color:#CBD5E1;">पिंच ज़ूम इन/आउट</div>
            </div>
          </div>
        </div>

        <!-- OK / Got it Button -->
        <button onclick="close3DInstructionsModal()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.95rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); text-align:center; display:flex; align-items:center; justify-content:center; gap:6px;">
          <span>🙏</span> समझ गया (OK - Start Darshan)
        </button>

      </div>
    </div>
"""

if 'id="mandir-3d-instructions-modal"' not in html:
    html = html.replace('<div id="mandir-3d-loader"', instructions_modal_html + '\n    <div id="mandir-3d-loader"')
    print("✓ Added Instructions Modal inside mandir-3d-modal in index.html")

# Bump cache buster
ts = int(time.time())
html = re.sub(r'mandir_3d_engine\.js\?v=\d+', f'mandir_3d_engine.js?v={ts}', html)
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update mandir_3d_engine.js with open3DInstructionsModal logic
with open('mandir_3d_engine.js', 'r', encoding='utf-8') as f:
    engine_js = f.read()

instructions_js = """
// ══════════════════════════════════════════════════════════════════════════════
// ℹ️ 3D MODEL & MANDIR NAVIGATION INSTRUCTIONS GUIDE
// ══════════════════════════════════════════════════════════════════════════════

window.open3DInstructionsModal = function() {
  const modal = document.getElementById('mandir-3d-instructions-modal');
  if (modal) modal.style.display = 'flex';
};

window.close3DInstructionsModal = function() {
  const modal = document.getElementById('mandir-3d-instructions-modal');
  if (modal) modal.style.display = 'none';
  localStorage.setItem('sanatan_3d_guide_shown', 'true');
};

// Check and trigger for first time visitor
window.checkAndShowFirstTime3DGuide = function() {
  const isSeen = localStorage.getItem('sanatan_3d_guide_shown');
  if (!isSeen) {
    setTimeout(() => {
      window.open3DInstructionsModal();
    }, 1200);
  }
};
"""

if 'open3DInstructionsModal' not in engine_js:
    engine_js += "\n" + instructions_js

# Hook checkAndShowFirstTime3DGuide inside executeCameraWalkInTransition complete
if 'checkAndShowFirstTime3DGuide' in engine_js and 'window.checkAndShowFirstTime3DGuide()' not in engine_js:
    engine_js = engine_js.replace(
        "showToast('🕉️ भव्य गर्भग्रह में प्रवेश पूर्ण — 360° परिक्रमा आरंभ करें!');",
        "showToast('🕉️ भव्य गर्भग्रह में प्रवेश पूर्ण — 360° परिक्रमा आरंभ करें!');\n        window.checkAndShowFirstTime3DGuide();"
    )

with open('mandir_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(engine_js)

print("✓ Updated mandir_3d_engine.js with instruction modal controllers")
