import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

rich_8_thali_html = """      <!-- 🪔 8-ITEM INTERACTIVE DIGITAL PUJA THALI (अष्टोपचार पूजा थाली) 🪔 -->
      <div id="digital-puja-thali-card" style="margin: 0 1.2rem 1.4rem; background: linear-gradient(160deg, #2A0948 0%, #150426 60%, #0B0116 100%); border: 1.5px solid rgba(248,200,59,0.45); border-radius: 26px; padding: 1.3rem 1.1rem; text-align: center; box-shadow: 0 10px 35px rgba(0,0,0,0.7), 0 0 15px rgba(248,200,59,0.1) inset; position: relative; overflow: hidden;">
        
        <!-- Header: Title & 0/8 Counter Badge -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
          <div style="font-size:1.02rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
            <span style="font-size:1.25rem;">🪔</span>
            <span>डिजिटल पूजा थाली</span>
          </div>
          <span id="puja-thali-badge" style="font-size:0.75rem; font-weight:900; background:rgba(248,200,59,0.18); border:1.2px solid #F8C83B; color:#FDE68A; padding:3px 10px; border-radius:14px; transition:all 0.3s ease;">
            0/8 अर्पित
          </span>
        </div>

        <!-- 8-Item Circular Pooja Thali Layout -->
        <div style="position:relative; width:260px; height:260px; margin:0 auto; display:flex; align-items:center; justify-content:center;">
          
          <!-- Outer Rotating Golden Halo Ring -->
          <div style="position:absolute; width:256px; height:256px; border-radius:50%; border:2px dashed rgba(248,200,59,0.5); animation:spinSlow 25s linear infinite; pointer-events:none; box-shadow:0 0 20px rgba(248,200,59,0.15);"></div>

          <!-- Main Brass Thali Plate Disc -->
          <div style="position:absolute; width:240px; height:240px; border-radius:50%; background:radial-gradient(circle at 40% 40%, #D97706 0%, #B45309 60%, #78350F 100%); padding:4px; box-shadow:0 12px 35px rgba(0,0,0,0.8), inset 0 0 20px rgba(0,0,0,0.6); border:2px solid #FEF3C7;">
            <div style="width:100%; height:100%; border-radius:50%; background:radial-gradient(circle, #2D0B48 0%, #170428 75%, #0B0116 100%); border:1.5px solid rgba(248,200,59,0.4); position:relative; display:flex; align-items:center; justify-content:center;">
              
              <!-- Center Divine "ॐ" Reset Button -->
              <button onclick="resetPujaThali()" title="पुनः पूजन आरंभ करें (Reset)" style="width:68px; height:68px; border-radius:50%; background:radial-gradient(circle, #3D1360 0%, #1C0530 100%); border:2px solid #F8C83B; color:#FDE68A; font-size:2rem; font-weight:900; cursor:pointer; box-shadow:0 0 15px rgba(248,200,59,0.45); display:flex; align-items:center; justify-content:center; transition:transform 0.2s; z-index:10;">
                ॐ
              </button>

              <!-- 8 Circular Samagri Nodes (Positioned around 360 degrees) -->
              
              <!-- 1. Deep (Top, 0°) -->
              <div id="samagri-node-deep" onclick="offerSamagriItem(0)" class="puja-node" style="position:absolute; top:8px; left:calc(50% - 22px); width:44px; height:44px; border-radius:50%; background:#2E1C4E; border:1.5px solid #E89A3C; display:flex; flex-direction:column; align-items:center; justify-content:center; cursor:pointer; transition:all 0.25s ease; box-shadow:0 3px 10px rgba(0,0,0,0.4);">
                <span style="font-size:16px; line-height:1;">🪔</span>
                <span class="p-name" style="font-size:7.5px; color:#FFF; font-weight:800;">दीप</span>
              </div>

              <!-- 2. Ghanti (Top-Right, 45°) -->
              <div id="samagri-node-ghanti" onclick="offerSamagriItem(1)" class="puja-node" style="position:absolute; top:36px; right:20px; width:44px; height:44px; border-radius:50%; background:#2E1C4E; border:1.5px solid #E89A3C; display:flex; flex-direction:column; align-items:center; justify-content:center; cursor:pointer; transition:all 0.25s ease; box-shadow:0 3px 10px rgba(0,0,0,0.4);">
                <span style="font-size:16px; line-height:1;">🔔</span>
                <span class="p-name" style="font-size:7.5px; color:#FFF; font-weight:800;">घंटी</span>
              </div>

              <!-- 3. Shankh (Right, 90°) -->
              <div id="samagri-node-shankh" onclick="offerSamagriItem(2)" class="puja-node" style="position:absolute; top:calc(50% - 22px); right:6px; width:44px; height:44px; border-radius:50%; background:#2E1C4E; border:1.5px solid #E89A3C; display:flex; flex-direction:column; align-items:center; justify-content:center; cursor:pointer; transition:all 0.25s ease; box-shadow:0 3px 10px rgba(0,0,0,0.4);">
                <span style="font-size:16px; line-height:1;">🐚</span>
                <span class="p-name" style="font-size:7.5px; color:#FFF; font-weight:800;">शंख</span>
              </div>

              <!-- 4. Pushp (Bottom-Right, 135°) -->
              <div id="samagri-node-pushp" onclick="offerSamagriItem(3)" class="puja-node" style="position:absolute; bottom:36px; right:20px; width:44px; height:44px; border-radius:50%; background:#2E1C4E; border:1.5px solid #E89A3C; display:flex; flex-direction:column; align-items:center; justify-content:center; cursor:pointer; transition:all 0.25s ease; box-shadow:0 3px 10px rgba(0,0,0,0.4);">
                <span style="font-size:16px; line-height:1;">🌸</span>
                <span class="p-name" style="font-size:7.5px; color:#FFF; font-weight:800;">पुष्प</span>
              </div>

              <!-- 5. Dhoop (Bottom, 180°) -->
              <div id="samagri-node-dhoop" onclick="offerSamagriItem(4)" class="puja-node" style="position:absolute; bottom:8px; left:calc(50% - 22px); width:44px; height:44px; border-radius:50%; background:#2E1C4E; border:1.5px solid #E89A3C; display:flex; flex-direction:column; align-items:center; justify-content:center; cursor:pointer; transition:all 0.25s ease; box-shadow:0 3px 10px rgba(0,0,0,0.4);">
                <span style="font-size:16px; line-height:1;">💨</span>
                <span class="p-name" style="font-size:7.5px; color:#FFF; font-weight:800;">धूप</span>
              </div>

              <!-- 6. Gangajal (Bottom-Left, 225°) -->
              <div id="samagri-node-gangajal" onclick="offerSamagriItem(5)" class="puja-node" style="position:absolute; bottom:36px; left:20px; width:44px; height:44px; border-radius:50%; background:#2E1C4E; border:1.5px solid #E89A3C; display:flex; flex-direction:column; align-items:center; justify-content:center; cursor:pointer; transition:all 0.25s ease; box-shadow:0 3px 10px rgba(0,0,0,0.4);">
                <span style="font-size:16px; line-height:1;">🌊</span>
                <span class="p-name" style="font-size:7.5px; color:#FFF; font-weight:800;">गंगाजल</span>
              </div>

              <!-- 7. Tilak (Left, 270°) -->
              <div id="samagri-node-tilak" onclick="offerSamagriItem(6)" class="puja-node" style="position:absolute; top:calc(50% - 22px); left:6px; width:44px; height:44px; border-radius:50%; background:#2E1C4E; border:1.5px solid #E89A3C; display:flex; flex-direction:column; align-items:center; justify-content:center; cursor:pointer; transition:all 0.25s ease; box-shadow:0 3px 10px rgba(0,0,0,0.4);">
                <span style="font-size:16px; line-height:1;">🏵️</span>
                <span class="p-name" style="font-size:7.5px; color:#FFF; font-weight:800;">चंदन</span>
              </div>

              <!-- 8. Bhog (Top-Left, 315°) -->
              <div id="samagri-node-bhog" onclick="offerSamagriItem(7)" class="puja-node" style="position:absolute; top:36px; left:20px; width:44px; height:44px; border-radius:50%; background:#2E1C4E; border:1.5px solid #E89A3C; display:flex; flex-direction:column; align-items:center; justify-content:center; cursor:pointer; transition:all 0.25s ease; box-shadow:0 3px 10px rgba(0,0,0,0.4);">
                <span style="font-size:16px; line-height:1;">🥥</span>
                <span class="p-name" style="font-size:7.5px; color:#FFF; font-weight:800;">भोग</span>
              </div>

            </div>
          </div>

        </div>

        <!-- Bottom Dynamic Action/Blessing Message -->
        <div id="puja-action-message" style="margin-top:14px; font-size:0.82rem; font-weight:800; color:#FDE68A; transition:all 0.2s ease;">
          सामग्री पर स्पर्श करके प्रभु को अर्पित करें 🙏
        </div>

      </div>

      <!-- 🪔 PUJA COMPLETED CELEBRATION MODAL 🪔 -->
      <div id="puja-completed-modal" style="display:none; position:fixed; inset:0; z-index:100060; background:rgba(10,2,18,0.94); backdrop-filter:blur(25px); -webkit-backdrop-filter:blur(25px); align-items:center; justify-content:center; padding:1.2rem;">
        <div style="width:100%; max-width:380px; background:linear-gradient(160deg, #2D1047 0%, #1A052E 60%, #0F021B 100%); border:2px solid #F59E0B; border-radius:28px; padding:1.8rem 1.4rem; text-align:center; box-shadow:0 25px 70px rgba(0,0,0,0.9); position:relative; animation:fadeInUp 0.3s ease;">
          
          <div style="font-size:3.5rem; margin-bottom:8px; filter:drop-shadow(0 0 15px #F59E0B);">🪔</div>
          <h3 style="font-size:1.35rem; font-weight:900; color:#F8C83B; margin:0 0 6px 0;">
            🪔 नित्य पूजा संपन्न! 🕉️
          </h3>
          <p style="font-size:0.85rem; color:#FFFDF8; margin:0 0 14px 0; line-height:1.5;">
            प्रभु आपके सभी मनोरथ पूर्ण करें।<br>आज की दैनिक साधना में <strong>+10 अंक</strong> जुड़े!
          </p>

          <div style="background:rgba(248,200,59,0.18); border:1.5px solid #F8C83B; border-radius:14px; padding:8px 14px; display:inline-block; margin-bottom:20px;">
            <span style="font-size:0.88rem; font-weight:900; color:#FDE68A;">✨ 8/8 सामग्री समर्पित ✨</span>
          </div>

          <button onclick="closePujaCompletedModal()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.95rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 20px rgba(248,200,59,0.5);">
            प्रणाम स्वीकारें 🙏
          </button>
        </div>
      </div>"""

# Replace in index.html
s_thali = html.find('<!-- Brass Thali Disc')
if s_thali == -1:
    s_thali = html.find('<span>🪔</span> डिजिटल पूजा थाली')
if s_thali != -1:
    start_box = html.rfind('<div style="margin: 0 1.2rem 1.2rem;', 0, s_thali)
    if start_box == -1:
        start_box = html.rfind('<div', 0, s_thali)
    end_box = html.find('<!-- 🌅 DAILY DHARMIK SUVICHAR', start_box)
    html = html[:start_box] + rich_8_thali_html + "\n\n      " + html[end_box:]

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Updated index.html with complete 8-Samagri Circular Puja Thali (v={ts})")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

puja_thali_controller_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 8-SAMAGRI DIGITAL PUJA THALI ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.pujaSamagriList = [
  { id: 'deep', name: 'दीप', emoji: '🪔', actionText: 'दीप ज्योति प्रज्वलित हुई! ✨', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'ghanti', name: 'घंटी', emoji: '🔔', actionText: 'दिव्य घंटा नाद... 🔔', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'shankh', name: 'शंख', emoji: '🐚', actionText: 'शुभ शंखनाद! 🕉️', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'pushp', name: 'पुष्प', emoji: '🌸', actionText: 'पुष्प वृष्टि प्रभु चरणों में! 🌺', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'dhoop', name: 'धूप', emoji: '💨', actionText: 'सुगंधित धूप अर्पित हुई! 🪔', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'gangajal', name: 'गंगाजल', emoji: '🌊', actionText: 'पवित्र गंगाजल से आचमन! 💧', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'tilak', name: 'चंदन', emoji: '🏵️', actionText: 'दिव्य हरिचंदन तिलक अर्पित! 🌟', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'bhog', name: 'भोग', emoji: '🥥', actionText: 'माखन-मिश्री व नैवेद्य अर्पित! 🍯', sound: 'assets/audio/correct.mp3', isOffered: false }
];

window.offerSamagriItem = function(index) {
  const item = window.pujaSamagriList[index];
  if (!item) return;

  item.isOffered = true;

  // Haptic feedback if available
  if (navigator.vibrate) navigator.vibrate(30);

  // Play Bell sound
  if (typeof playSoundEffect === 'function') {
    playSoundEffect('correct');
  }

  // Update UI node
  const node = document.getElementById(`samagri-node-${item.id}`);
  if (node) {
    node.style.background = 'rgba(16, 185, 129, 0.35)';
    node.style.borderColor = '#10B981';
    node.style.boxShadow = '0 0 14px rgba(16, 185, 129, 0.6)';
    const nameSpan = node.querySelector('.p-name');
    if (nameSpan) {
      nameSpan.style.color = '#34D399';
    }
  }

  // Update Message
  const msgEl = document.getElementById('puja-action-message');
  if (msgEl) {
    msgEl.textContent = item.actionText;
    msgEl.style.color = '#34D399';
  }

  // Update Count
  const offeredCount = window.pujaSamagriList.filter(s => s.isOffered).length;
  const badge = document.getElementById('puja-thali-badge');
  if (badge) {
    badge.textContent = `${offeredCount}/8 अर्पित`;
    if (offeredCount === 8) {
      badge.style.background = 'rgba(16, 185, 129, 0.25)';
      badge.style.borderColor = '#10B981';
      badge.style.color = '#34D399';
    }
  }

  // 8/8 Complete Check
  if (offeredCount === 8) {
    if (typeof triggerFlowerShower === 'function') {
      triggerFlowerShower();
    }
    if (typeof playSoundEffect === 'function') {
      playSoundEffect('victory');
    }
    setTimeout(() => {
      window.showPujaCompletedModal();
    }, 400);
  }
};

window.resetPujaThali = function() {
  window.pujaSamagriList.forEach((item, index) => {
    item.isOffered = false;
    const node = document.getElementById(`samagri-node-${item.id}`);
    if (node) {
      node.style.background = '#2E1C4E';
      node.style.borderColor = '#E89A3C';
      node.style.boxShadow = '0 3px 10px rgba(0,0,0,0.4)';
      const nameSpan = node.querySelector('.p-name');
      if (nameSpan) {
        nameSpan.style.color = '#FFF';
      }
    }
  });

  const badge = document.getElementById('puja-thali-badge');
  if (badge) {
    badge.textContent = '0/8 अर्पित';
    badge.style.background = 'rgba(248,200,59,0.18)';
    badge.style.borderColor = '#F8C83B';
    badge.style.color = '#FDE68A';
  }

  const msgEl = document.getElementById('puja-action-message');
  if (msgEl) {
    msgEl.textContent = 'पुनः सामग्री स्पर्श करके पूजन आरंभ करें 🙏';
    msgEl.style.color = '#FDE68A';
  }

  if (typeof showToast === 'function') {
    showToast('🔄 पूजा थाली पुनः तैयार की गई');
  }
};

window.showPujaCompletedModal = function() {
  const modal = document.getElementById('puja-completed-modal');
  if (modal) {
    modal.style.display = 'flex';
  }
};

window.closePujaCompletedModal = function() {
  const modal = document.getElementById('puja-completed-modal');
  if (modal) {
    modal.style.display = 'none';
  }
};
"""

# Replace in app.js
if 'window.tapPujaItem' in js or 'window.offerSamagriItem' in js:
    js = re.sub(r'// ══════════════════════════════════════════════════════════════════════════════\s*// 🪔 DIGITAL PUJA THALI[\s\S]*?window\.tapPujaItem[\s\S]*?\}', puja_thali_controller_js, js)
else:
    js += "\n\n" + puja_thali_controller_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f"✓ Updated app.js with complete 8-Samagri Puja Thali Controller (v={ts})")
