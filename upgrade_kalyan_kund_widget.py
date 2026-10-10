import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Kalyan Kund card on Home page
old_kk_card = """<!-- 🙏 KALYAN KUND (DIGITAL DAAN & SEVA TRACKER) 🙏 -->
      <div style="margin: 0 1.2rem 1.4rem; background: linear-gradient(145deg, #220A3E 0%, #120322 100%); border: 1.5px solid rgba(248,200,59,0.35); border-radius: 22px; padding: 1.2rem; box-shadow: 0 8px 25px rgba(0,0,0,0.45);">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
          <div style="font-size:0.95rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
            <span>🙏</span> कल्याण कुण्ड (सेवा संकल्प)
          </div>
          <span style="font-size:0.68rem; background:rgba(16,185,129,0.2); border:1px solid #10B981; color:#34D399; padding:2px 6px; border-radius:8px; font-weight:800;">
            ✓ 100% सत्यापित
          </span>
        </div>
        <p style="font-size:0.78rem; color:#CBD5E1; margin:0 0 10px 0; line-height:1.4;">
          नित्य गौ-सेवा, मंदिर भंडारा एवं दीप दान संकल्प लें:
        </p>
        <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:8px; margin-bottom:12px;">
          <button onclick="selectDaanAmount(11, this)" class="daan-pill active" style="padding:8px 0; border-radius:12px; font-weight:900; font-size:0.85rem; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer;">₹11</button>
          <button onclick="selectDaanAmount(21, this)" class="daan-pill" style="padding:8px 0; border-radius:12px; font-weight:900; font-size:0.85rem; background:rgba(255,255,255,0.08); color:#FDE68A; border:1px solid rgba(248,200,59,0.3); cursor:pointer;">₹21</button>
          <button onclick="selectDaanAmount(51, this)" class="daan-pill" style="padding:8px 0; border-radius:12px; font-weight:900; font-size:0.85rem; background:rgba(255,255,255,0.08); color:#FDE68A; border:1px solid rgba(248,200,59,0.3); cursor:pointer;">₹51</button>
          <button onclick="selectDaanAmount(101, this)" class="daan-pill" style="padding:8px 0; border-radius:12px; font-weight:900; font-size:0.85rem; background:rgba(255,255,255,0.08); color:#FDE68A; border:1px solid rgba(248,200,59,0.3); cursor:pointer;">₹101</button>
        </div>
        <button onclick="triggerUPIDaan()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.9rem; font-weight:900; padding:11px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4);">
          ₹11 दान संकल्प लें (Direct UPI) ❯
        </button>
      </div>"""

rich_kk_card = """<!-- 🙏 KALYAN KUND (DIGITAL DAAN & SEVA TRACKER) 🙏 -->
      <div style="margin: 0 1.2rem 1.4rem; background: linear-gradient(145deg, #2D1047 0%, #1A052E 60%, #120320 100%); border: 1.5px solid rgba(248,200,59,0.35); border-radius: 22px; padding: 1.2rem; box-shadow: 0 8px 25px rgba(0,0,0,0.55), 0 0 15px rgba(248,200,59,0.08) inset;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
          <div style="font-size:0.98rem; font-weight:900; color:#FFFDF8; display:flex; align-items:center; gap:6px;">
            <span>🙏</span> कल्याण कुण्ड (सेवा संकल्प)
          </div>
          <span style="font-size:0.7rem; background:rgba(16,185,129,0.22); border:1.2px solid #10B981; color:#34D399; padding:2px 8px; border-radius:10px; font-weight:900;">
            ✓ 100% सत्यापित सेवा
          </span>
        </div>
        <p style="font-size:0.78rem; color:#CBD5E1; margin:0 0 12px 0; line-height:1.4;">
          नित्य गौ-सेवा, मंदिर भंडारा एवं दीप दान संकल्प लें:
        </p>

        <!-- 4 Divine Seva Options Grid -->
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px;">
          
          <!-- Seva 1: Gau Gras -->
          <div onclick="selectSevaCard('गौ ग्रास सेवा', 11, this)" class="seva-option-card" style="padding:8px 10px; border-radius:14px; background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); cursor:pointer; display:flex; align-items:center; gap:8px; transition:all 0.2s ease;">
            <span style="font-size:1.5rem;">🐄</span>
            <div>
              <div style="font-size:0.8rem; font-weight:900; color:#FFFDF8;">गौ ग्रास सेवा</div>
              <div style="font-size:0.75rem; font-weight:900; color:#F8C83B;">₹11</div>
            </div>
          </div>

          <!-- Seva 2: Akhand Deep (Default Selected) -->
          <div onclick="selectSevaCard('अखंड दीप दान', 21, this)" class="seva-option-card active" style="padding:8px 10px; border-radius:14px; background:rgba(248,200,59,0.2); border:1.5px solid #F8C83B; cursor:pointer; display:flex; align-items:center; gap:8px; transition:all 0.2s ease; box-shadow:0 0 12px rgba(248,200,59,0.3);">
            <span style="font-size:1.5rem;">🪔</span>
            <div>
              <div style="font-size:0.8rem; font-weight:900; color:#FFFDF8;">अखंड दीप दान</div>
              <div style="font-size:0.75rem; font-weight:900; color:#F8C83B;">₹21</div>
            </div>
          </div>

          <!-- Seva 3: Annakshetra -->
          <div onclick="selectSevaCard('अन्नक्षेत्र सेवा', 51, this)" class="seva-option-card" style="padding:8px 10px; border-radius:14px; background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); cursor:pointer; display:flex; align-items:center; gap:8px; transition:all 0.2s ease;">
            <span style="font-size:1.5rem;">🍲</span>
            <div>
              <div style="font-size:0.8rem; font-weight:900; color:#FFFDF8;">अन्नक्षेत्र सेवा</div>
              <div style="font-size:0.75rem; font-weight:900; color:#F8C83B;">₹51</div>
            </div>
          </div>

          <!-- Seva 4: Pushpa Shringar -->
          <div onclick="selectSevaCard('पुष्प-श्रृंगार', 101, this)" class="seva-option-card" style="padding:8px 10px; border-radius:14px; background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); cursor:pointer; display:flex; align-items:center; gap:8px; transition:all 0.2s ease;">
            <span style="font-size:1.5rem;">🌸</span>
            <div>
              <div style="font-size:0.8rem; font-weight:900; color:#FFFDF8;">पुष्प-श्रृंगार</div>
              <div style="font-size:0.75rem; font-weight:900; color:#F8C83B;">₹101</div>
            </div>
          </div>

        </div>

        <!-- Call to Action Button -->
        <button id="kalyan-kund-cta-btn" onclick="openSankalpBottomSheet()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.92rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.45); display:flex; align-items:center; justify-content:center; gap:6px;">
          <span id="kalyan-kund-cta-text">₹21 का संकल्प लें (Direct UPI)</span> ➔
        </button>
      </div>"""

if old_kk_card in html:
    html = html.replace(old_kk_card, rich_kk_card, 1)

# Add Sankalp Bottom Sheet Modal at the bottom of index.html
sankalp_modal_html = """  <!-- ═════════════════════════════════════════════════════════════════
       🕉️ SANKALP BOTTOM SHEET (YAZMAN & GOTRA SEVA MODAL) 🕉️
       ═════════════════════════════════════════════════════════════════ -->
  <div id="sankalp-bottom-sheet-modal" style="display:none; position:fixed; inset:0; z-index:100050; background:rgba(10,2,18,0.92); backdrop-filter:blur(25px); -webkit-backdrop-filter:blur(25px); align-items:flex-end; justify-content:center; padding:0;">
    <div style="width:100%; max-width:480px; background:linear-gradient(160deg, #2D1047 0%, #1A052E 60%, #0F021B 100%); border-top:2px solid #F59E0B; border-left:1px solid rgba(248,200,59,0.3); border-right:1px solid rgba(248,200,59,0.3); border-radius:28px 28px 0 0; padding:1.5rem 1.4rem 2rem; box-shadow:0 -10px 40px rgba(0,0,0,0.85); position:relative; animation:slideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);">
      
      <!-- Close Button -->
      <button onclick="closeSankalpBottomSheet()" style="position:absolute; top:16px; right:16px; background:rgba(255,255,255,0.12); border:none; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>

      <!-- Header -->
      <div style="text-align:center; margin-bottom:14px;">
        <div style="font-size:1.6rem; margin-bottom:2px;">🕉️</div>
        <h3 id="sankalp-modal-title" style="font-size:1.2rem; font-weight:900; color:#F8C83B; margin:0 0 4px 0;">
          अखंड दीप दान संकल्प (₹21)
        </h3>
        <p style="font-size:0.78rem; color:#CBD5E1; margin:0;">
          आपके नाम व गोत्र से यह पावन सेवा समर्पित की जाएगी
        </p>
      </div>

      <!-- Sankalp Form Fields -->
      <div style="display:flex; flex-direction:column; gap:11px; margin-bottom:16px;">
        
        <!-- Field 1: Yajman Name -->
        <div>
          <label style="font-size:0.75rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            यजमान का नाम: <span style="color:#EF4444;">*</span>
          </label>
          <input type="text" id="sankalp-yajman-name" placeholder="उदा. राहुल शर्मा" style="width:100%; background:#1F0933; border:1.5px solid rgba(248,200,59,0.3); color:#FFFDF8; font-size:0.9rem; font-weight:700; padding:10px 14px; border-radius:12px; outline:none;" />
        </div>

        <!-- Field 2: Gotra / Location -->
        <div>
          <label style="font-size:0.75rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            गोत्र / स्थान (ऐच्छिक):
          </label>
          <input type="text" id="sankalp-gotra" placeholder="उदा. कश्यप गोत्र, दिल्ली" style="width:100%; background:#1F0933; border:1.5px solid rgba(248,200,59,0.3); color:#FFFDF8; font-size:0.9rem; font-weight:700; padding:10px 14px; border-radius:12px; outline:none;" />
        </div>

        <!-- Field 3: Sankalp Purpose -->
        <div>
          <label style="font-size:0.75rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            संकल्प उद्देश्य:
          </label>
          <div style="display:flex; gap:6px;">
            <label style="flex:1; background:rgba(255,255,255,0.06); border:1px solid rgba(248,200,59,0.25); border-radius:10px; padding:6px 8px; font-size:0.72rem; color:#FFF; font-weight:700; display:flex; align-items:center; gap:4px; cursor:pointer;">
              <input type="radio" name="sankalp_purpose" value="स्वास्थ्य" checked style="accent-color:#F8C83B;" />
              स्वास्थ्य व दीर्घायु
            </label>
            <label style="flex:1; background:rgba(255,255,255,0.06); border:1px solid rgba(248,200,59,0.25); border-radius:10px; padding:6px 8px; font-size:0.72rem; color:#FFF; font-weight:700; display:flex; align-items:center; gap:4px; cursor:pointer;">
              <input type="radio" name="sankalp_purpose" value="परिवार शांति" style="accent-color:#F8C83B;" />
              परिवार शांति व समृद्धि
            </label>
          </div>
        </div>

      </div>

      <!-- Submit & UPI Trigger Button -->
      <button onclick="submitSankalpSeva()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.95rem; font-weight:900; padding:13px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 20px rgba(248,200,59,0.5); display:flex; align-items:center; justify-content:center; gap:8px;">
        <span id="sankalp-pay-btn-text">₹21 का संकल्प लें (Pay via UPI)</span> ➔
      </button>

    </div>
  </div>"""

if 'id="sankalp-bottom-sheet-modal"' not in html:
    html = html.replace('</body>', sankalp_modal_html + "\n</body>")

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Updated index.html with Kalyan Kund Widget & Sankalp Bottom Sheet (v={ts})")

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

sankalp_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🕉️ KALYAN KUND SEVA SANKALP CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.currentSelectedSevaTitle = "अखंड दीप दान";
window.currentSelectedSevaAmount = 21;

window.selectSevaCard = function(title, amount, el) {
  window.currentSelectedSevaTitle = title;
  window.currentSelectedSevaAmount = amount;

  document.querySelectorAll('.seva-option-card').forEach(card => {
    card.classList.remove('active');
    card.style.background = 'rgba(255,255,255,0.06)';
    card.style.borderColor = 'rgba(255,255,255,0.15)';
    card.style.boxShadow = 'none';
  });

  if (el) {
    el.classList.add('active');
    el.style.background = 'rgba(248,200,59,0.2)';
    el.style.borderColor = '#F8C83B';
    el.style.boxShadow = '0 0 12px rgba(248,200,59,0.3)';
  }

  const ctaText = document.getElementById('kalyan-kund-cta-text');
  if (ctaText) {
    ctaText.textContent = `₹${amount} का संकल्प लें (Direct UPI)`;
  }
};

window.openSankalpBottomSheet = function() {
  const modal = document.getElementById('sankalp-bottom-sheet-modal');
  const titleEl = document.getElementById('sankalp-modal-title');
  const payBtnText = document.getElementById('sankalp-pay-btn-text');

  if (titleEl) {
    titleEl.textContent = `🕉️ ${window.currentSelectedSevaTitle} संकल्प (₹${window.currentSelectedSevaAmount})`;
  }
  if (payBtnText) {
    payBtnText.textContent = `₹${window.currentSelectedSevaAmount} का संकल्प लें (Pay via UPI)`;
  }

  if (modal) {
    modal.style.display = 'flex';
  }
};

window.closeSankalpBottomSheet = function() {
  const modal = document.getElementById('sankalp-bottom-sheet-modal');
  if (modal) {
    modal.style.display = 'none';
  }
};

window.submitSankalpSeva = function() {
  const yajman = document.getElementById('sankalp-yajman-name')?.value?.trim() || 'भक्त जन';
  const gotra = document.getElementById('sankalp-gotra')?.value?.trim() || 'कश्यप / सर्वगोत्र';
  const purpose = document.querySelector('input[name="sankalp_purpose"]:checked')?.value || 'परिवार शांति';

  const upiLink = `upi://pay?pa=bhaktisankalp@upi&pn=BhaktiSeva&am=${window.currentSelectedSevaAmount}&cu=INR&tn=${encodeURIComponent(`${window.currentSelectedSevaTitle} - ${yajman} (${gotra})`)}`;

  window.closeSankalpBottomSheet();

  if (typeof showToast === 'function') {
    showToast(`🚩 ${yajman} जी का ₹${window.currentSelectedSevaAmount} का संकल्प दर्ज हुआ!`);
  }
  if (typeof triggerFlowerShower === 'function') {
    triggerFlowerShower();
  }

  // Attempt to open UPI intent or fallback
  window.open(upiLink, '_blank');
};
"""

# Replace in app.js
if 'window.openSankalpBottomSheet' in js:
    js = re.sub(r'// ══════════════════════════════════════════════════════════════════════════════\s*// 🕉️ KALYAN KUND[\s\S]*?window\.closeSankalpBottomSheet[\s\S]*?\}', sankalp_js, js)
else:
    js += "\n\n" + sankalp_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Updated app.js with complete Kalyan Kund Seva Sankalp Controller")
