import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🛠️ COMPREHENSIVE SADHANA GAMIFICATION & SANGHA MODALS FIX")
print("======================================================================")

# 1. Inspect and Fix z-index of all modals in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace low z-index (100085, 100095) with high z-index (100250) on child modals
html = html.replace('id="vedic-ranks-modal" style="display:none; position:fixed; inset:0; z-index:100085;', 'id="vedic-ranks-modal" style="display:none; position:fixed; inset:0; z-index:100250;')
html = html.replace('id="dedicate-jap-modal" style="display:none; position:fixed; inset:0; z-index:100085;', 'id="dedicate-jap-modal" style="display:none; position:fixed; inset:0; z-index:100250;')
html = html.replace('id="add-sangha-member-modal" style="display:none; position:fixed; inset:0; z-index:100085;', 'id="add-sangha-member-modal" style="display:none; position:fixed; inset:0; z-index:100250;')
html = html.replace('id="create-join-sangha-modal" style="display:none; position:fixed; inset:0; z-index:100085;', 'id="create-join-sangha-modal" style="display:none; position:fixed; inset:0; z-index:100250;')
html = html.replace('id="streak-rescue-celebration-modal" style="display:none; position:fixed; inset:0; z-index:100095;', 'id="streak-rescue-celebration-modal" style="display:none; position:fixed; inset:0; z-index:100260;')

# Also add Add Member Name Form into #add-sangha-member-modal
old_add_member_modal = """  <!-- ═══════════════════════════════════════════════════════════════════════════
       ➕ ADD SANGHA MEMBER MODAL (सदस्य जोड़ें) ➕
       ═══════════════════════════════════════════════════════════════════════════ -->
  <div id="add-sangha-member-modal" style="display:none; position:fixed; inset:0; z-index:100250; background:rgba(7,1,16,0.92); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); align-items:center; justify-content:center; padding:1.2rem;">
    <div style="width:100%; max-width:380px; background:linear-gradient(165deg, #2D1047 0%, #1A052E 50%, #0D0218 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.4rem 1.2rem; text-align:center; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease;">
      
      <div style="font-size:2.8rem; margin-bottom:8px;">👨‍👩‍👧‍👦</div>
      <h3 style="font-size:1.2rem; font-weight:900; color:#FFFDF8; margin:0 0 6px 0;">
        परिवार व मित्रों को जोड़ें
      </h3>
      <p style="font-size:0.78rem; color:#CBD5E1; margin:0 0 16px 0;">
        इस आमंत्रण कोड से परिवार के सदस्यों को महा-अनुष्ठान में शामिल करें:
      </p>

      <!-- Invite Code Box -->
      <div style="background:rgba(0,0,0,0.4); border:1.5px dashed #F8C83B; border-radius:16px; padding:14px; margin-bottom:14px;">
        <div style="font-size:0.7rem; color:#CBD5E1; margin-bottom:4px;">सामूहिक मंडल कोड (Invite Code)</div>
        <div style="font-size:1.6rem; font-weight:900; color:#F8C83B; letter-spacing:4px;">OM1008</div>
        <button onclick="copySanghaInviteCode()" style="margin-top:8px; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; font-size:0.75rem; font-weight:800; padding:5px 12px; border-radius:10px; cursor:pointer;">
          📋 कोड कॉपी करें
        </button>
      </div>

      <!-- Action Buttons -->
      <button onclick="shareSanghaProgressWhatsApp()" style="width:100%; background:linear-gradient(135deg, #25D366 0%, #128C7E 100%); color:#FFF; border:none; font-size:0.88rem; font-weight:900; padding:11px 0; border-radius:14px; cursor:pointer; box-shadow:0 4px 15px rgba(37,211,102,0.35); margin-bottom:8px; display:flex; align-items:center; justify-content:center; gap:6px;">
        <span>📲</span> WhatsApp पर निमंत्रण भेजें
      </button>

      <button onclick="closeAddMemberModal()" style="width:100%; background:rgba(255,255,255,0.1); border:none; color:#CBD5E1; font-weight:800; padding:10px 0; border-radius:14px; cursor:pointer;">
        बंद करें
      </button>

    </div>
  </div>"""

new_add_member_modal = """  <!-- ═══════════════════════════════════════════════════════════════════════════
       ➕ ADD SANGHA MEMBER MODAL (सदस्य जोड़ें) ➕
       ═══════════════════════════════════════════════════════════════════════════ -->
  <div id="add-sangha-member-modal" style="display:none; position:fixed; inset:0; z-index:100250; background:rgba(7,1,16,0.92); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); align-items:center; justify-content:center; padding:1.2rem;">
    <div style="width:100%; max-width:390px; background:linear-gradient(165deg, #2D1047 0%, #1A052E 50%, #0D0218 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.4rem 1.2rem; text-align:center; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease;">
      
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; border-bottom:1px solid rgba(248,200,59,0.25); padding-bottom:8px;">
        <h3 style="font-size:1.15rem; font-weight:900; color:#FFFDF8; margin:0; display:flex; align-items:center; gap:6px;">
          <span>👨‍👩‍👧‍👦</span> परिवार व साधक जोड़ें
        </h3>
        <button onclick="closeAddMemberModal()" style="background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:30px; height:30px; border-radius:50%; font-size:1rem; cursor:pointer;">✕</button>
      </div>

      <!-- Quick Add by Name -->
      <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:16px; padding:12px; margin-bottom:12px; text-align:left;">
        <div style="font-size:0.75rem; font-weight:800; color:#FDE68A; margin-bottom:6px;">
          ➕ सदस्य का नाम दर्ज करें (उदा. चाचा जी, प्रिया, मित्र):
        </div>
        <div style="display:flex; gap:6px;">
          <input type="text" id="add-sangha-member-name-input" placeholder="सदस्य का नाम..." style="flex:1; background:rgba(0,0,0,0.4); border:1px solid rgba(248,200,59,0.4); border-radius:12px; padding:8px 10px; color:#FFFDF8; font-size:0.82rem; outline:none;" />
          <button onclick="submitAddSanghaMember()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-size:0.8rem; font-weight:900; padding:8px 14px; border-radius:12px; cursor:pointer;">
            जोड़ें ➔
          </button>
        </div>
      </div>

      <!-- Invite Code Box -->
      <div style="background:rgba(0,0,0,0.4); border:1.5px dashed #F8C83B; border-radius:16px; padding:12px; margin-bottom:12px;">
        <div style="font-size:0.7rem; color:#CBD5E1; margin-bottom:2px;">सामूहिक मंडल कोड (Invite Code)</div>
        <div id="sangha-modal-invite-code-text" style="font-size:1.5rem; font-weight:900; color:#F8C83B; letter-spacing:4px;">OM1008</div>
        <button onclick="copySanghaInviteCode()" style="margin-top:6px; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; font-size:0.72rem; font-weight:800; padding:4px 10px; border-radius:10px; cursor:pointer;">
          📋 कोड कॉपी करें
        </button>
      </div>

      <!-- Action Buttons -->
      <button onclick="shareSanghaProgressWhatsApp()" style="width:100%; background:linear-gradient(135deg, #25D366 0%, #128C7E 100%); color:#FFF; border:none; font-size:0.85rem; font-weight:900; padding:11px 0; border-radius:14px; cursor:pointer; box-shadow:0 4px 15px rgba(37,211,102,0.35); margin-bottom:8px; display:flex; align-items:center; justify-content:center; gap:6px;">
        <span>📲</span> WhatsApp पर निमंत्रण भेजें
      </button>

      <button onclick="closeAddMemberModal()" style="width:100%; background:rgba(255,255,255,0.1); border:none; color:#CBD5E1; font-weight:800; padding:9px 0; border-radius:14px; cursor:pointer;">
        बंद करें
      </button>

    </div>
  </div>"""

# Replace in html
if old_add_member_modal in html:
    html = html.replace(old_add_member_modal, new_add_member_modal)
    print("✓ Enhanced #add-sangha-member-modal in index.html")
else:
    # Look for id="add-sangha-member-modal"
    pos = html.find('id="add-sangha-member-modal"')
    if pos != -1:
        end_pos = html.find('</div>\n  </div>', pos) + 15
        html = html[:pos-100] + new_add_member_modal + html[end_pos:]
        print("✓ Replaced #add-sangha-member-modal via position match")

# 2. Add Universal Toast Container to index.html if not present
toast_container_html = """  <!-- 🍞 UNIVERSAL ULTRA-LUXURY TOAST NOTIFICATION CONTAINER 🍞 -->
  <div id="universal-toast-container" style="position:fixed; top:24px; left:50%; transform:translateX(-50%); z-index:999999; display:flex; flex-direction:column; align-items:center; gap:8px; pointer-events:none; width:90%; max-width:380px;"></div>
"""

if 'id="universal-toast-container"' not in html:
    html = html.replace('</body>', toast_container_html + '\n</body>')
    print("✓ Added #universal-toast-container to index.html")

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'sadhana_gamification_engine\.js\?v=\d+', f'sadhana_gamification_engine.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Updated index.html")

# 3. Update sadhana_gamification_engine.js with full functionality, toast, member adding, haptics, and shield logic
with open('sadhana_gamification_engine.js', 'r', encoding='utf-8') as f:
    engine_js = f.read()

# Add universal showToast function if not already globally defined
toast_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🍞 UNIVERSAL TOAST NOTIFICATION ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.showToast = function(msg, duration = 3200) {
  let container = document.getElementById('universal-toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'universal-toast-container';
    container.style.cssText = 'position:fixed; top:24px; left:50%; transform:translateX(-50%); z-index:999999; display:flex; flex-direction:column; align-items:center; gap:8px; pointer-events:none; width:90%; max-width:380px;';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.style.cssText = 'background:radial-gradient(circle at 50% 30%, #3B1259 0%, #17042B 100%); border:1.8px solid #F8C83B; border-radius:20px; padding:11px 18px; color:#FFFDF8; font-size:0.86rem; font-weight:900; box-shadow:0 12px 35px rgba(0,0,0,0.9), 0 0 15px rgba(248,200,59,0.3) inset; text-align:center; animation:fadeInDown 0.3s ease; pointer-events:auto; backdrop-filter:blur(15px); -webkit-backdrop-filter:blur(15px); display:flex; align-items:center; justify-content:center; gap:8px; line-height:1.35;';
  toast.innerHTML = `<span>✨</span><span>${msg}</span>`;

  container.appendChild(toast);

  if (navigator.vibrate) navigator.vibrate(30);

  setTimeout(() => {
    toast.style.transition = 'opacity 0.35s ease, transform 0.35s ease';
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(-15px) scale(0.95)';
    setTimeout(() => {
      if (toast.parentNode) toast.parentNode.removeChild(toast);
    }, 360);
  }, duration);
};
"""

if 'UNIVERSAL TOAST NOTIFICATION ENGINE' not in engine_js:
    engine_js = toast_js + '\n\n' + engine_js

# Add submitAddSanghaMember
add_member_func_js = """
window.submitAddSanghaMember = function() {
  const input = document.getElementById('add-sangha-member-name-input');
  const name = input ? input.value.trim() : '';

  if (!name) {
    if (typeof showToast === 'function') showToast('कृपया सदस्य का नाम दर्ज करें!');
    return;
  }

  // Add new member to contributors list
  const avatars = ['🌸', '🌿', '🪷', '🌻', '🌺', '🕉️', '🚩'];
  const randomAvatar = avatars[Math.floor(Math.random() * avatars.length)];

  window.ActiveSanghaCircle.contributors.push({
    name: name,
    count: 0,
    isSelf: false,
    avatar: randomAvatar
  });

  window.ActiveSanghaCircle.recent_feed.unshift({
    text: `${randomAvatar} ${name} जी महा-अनुष्ठान में शामिल हुए`,
    time: 'अभी-अभी'
  });

  window.saveSanghaCircleState();
  window.renderSanghaCircleUI();

  if (input) input.value = '';
  window.closeAddMemberModal();

  if (navigator.vibrate) navigator.vibrate([40, 30, 70]);
  if (typeof playSoundEffect === 'function') playSoundEffect('click');

  if (typeof showToast === 'function') {
    showToast(`👥 ${name} जी सामूहिक महा-अनुष्ठान में जुड़ गए! 🚩`);
  }
};
"""

if 'submitAddSanghaMember' not in engine_js:
    engine_js += '\n\n' + add_member_func_js

with open('sadhana_gamification_engine.js', 'w', encoding='utf-8') as f:
    f.write(engine_js)

print("✓ Updated sadhana_gamification_engine.js")
