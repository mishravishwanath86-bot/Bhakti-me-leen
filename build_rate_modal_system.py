import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Add #rate-modal to index.html and wire drawer-rate
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update drawer-rate onclick
html = html.replace(
    '<button class="drawer-item" id="drawer-rate"><span class="di">⭐</span><span>रेट करें</span></button>',
    '<button class="drawer-item" id="drawer-rate" onclick="openRateModal()"><span class="di">⭐</span><span>रेट करें</span></button>'
)

# Update about page rate button
html = html.replace(
    'showToast(\'⭐ आपके आशीर्वाद व समर्थन हेतु आभार!\');',
    'openRateModal();'
)

# Rate Modal HTML
rate_modal_html = """
  <!-- ⭐ INTERACTIVE 5-STAR RATE APP MODAL (रेट करें) ⭐ -->
  <div id="rate-modal" style="display:none; position:fixed; inset:0; z-index:100150; background:rgba(10,2,18,0.94); backdrop-filter:blur(22px); -webkit-backdrop-filter:blur(22px); align-items:center; justify-content:center; padding:1.2rem;">
    <div style="width:100%; max-width:390px; background:linear-gradient(160deg, #2E104A 0%, #1A052E 60%, #0D0218 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.6rem 1.3rem; text-align:center; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease;">
      
      <!-- Close Button -->
      <button onclick="closeRateModal()" style="position:absolute; top:14px; right:14px; background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:32px; height:32px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>

      <!-- App Logo Emblem -->
      <div style="width:70px; height:70px; border-radius:50%; padding:3px; background:linear-gradient(135deg, #F8C83B, #D97706); margin:0 auto 10px; box-shadow:0 0 20px rgba(248,200,59,0.5);">
        <img src="assets/app_logo.jpg?v=1787490651276" alt="भक्ति में लीन" style="width:100%; height:100%; border-radius:50%; object-fit:cover;" onerror="this.src='assets/gallery/bal_ganesha_little.jpg'" />
      </div>

      <h3 style="font-size:1.3rem; font-weight:900; color:#FFFDF8; margin:0 0 4px 0;">
        'भक्ति में लीन' को रेट करें
      </h3>
      <p style="font-size:0.8rem; color:#CBD5E1; margin:0 0 16px 0;">
        आपका अनुभव हमारे लिए अत्यंत मूल्यवान है।
      </p>

      <!-- 5 Interactive Golden Stars -->
      <div id="rate-stars-container" style="display:flex; justify-content:center; gap:8px; margin-bottom:10px;">
        <span onclick="selectAppRating(1)" onmouseover="hoverAppRating(1)" class="rate-star" data-val="1" style="font-size:2.2rem; cursor:pointer; filter:drop-shadow(0 0 8px #F59E0B); transition:transform 0.15s ease;">⭐</span>
        <span onclick="selectAppRating(2)" onmouseover="hoverAppRating(2)" class="rate-star" data-val="2" style="font-size:2.2rem; cursor:pointer; filter:drop-shadow(0 0 8px #F59E0B); transition:transform 0.15s ease;">⭐</span>
        <span onclick="selectAppRating(3)" onmouseover="hoverAppRating(3)" class="rate-star" data-val="3" style="font-size:2.2rem; cursor:pointer; filter:drop-shadow(0 0 8px #F59E0B); transition:transform 0.15s ease;">⭐</span>
        <span onclick="selectAppRating(4)" onmouseover="hoverAppRating(4)" class="rate-star" data-val="4" style="font-size:2.2rem; cursor:pointer; filter:drop-shadow(0 0 8px #F59E0B); transition:transform 0.15s ease;">⭐</span>
        <span onclick="selectAppRating(5)" onmouseover="hoverAppRating(5)" class="rate-star" data-val="5" style="font-size:2.2rem; cursor:pointer; filter:drop-shadow(0 0 8px #F59E0B); transition:transform 0.15s ease;">⭐</span>
      </div>

      <div id="rate-mood-label" style="font-size:0.88rem; font-weight:900; color:#F8C83B; margin-bottom:14px; min-height:22px;">
        ⭐⭐⭐⭐⭐ अत्यंत दिव्य व उत्कृष्ट! 🙏
      </div>

      <!-- Feedback Comments Input -->
      <div style="margin-bottom:16px;">
        <textarea id="rate-feedback-input" rows="3" placeholder="💬 अपने विचार या सुझाव लिखें (वैकल्पिक)..." style="width:100%; background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.4); border-radius:16px; padding:10px 14px; color:#FFFDF8; font-size:0.85rem; outline:none; box-sizing:border-box; resize:none; font-family:inherit;"></textarea>
      </div>

      <!-- Action Buttons -->
      <div style="display:flex; flex-direction:column; gap:8px;">
        <button onclick="submitAppRating()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.95rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); display:flex; align-items:center; justify-content:center; gap:6px;">
          <span>⭐</span> रेटिंग सबमिट करें (+10 अंक) ➔
        </button>

        <button onclick="window.open('https://play.google.com/store', '_blank'); closeRateModal();" style="width:100%; background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); color:#FDE68A; font-size:0.82rem; font-weight:800; padding:10px 0; border-radius:14px; cursor:pointer;">
          🌐 Play Store पर 5-स्टार दें
        </button>
      </div>

    </div>
  </div>
"""

if 'id="rate-modal"' not in html:
    html = html.replace('<!-- ===== SPLASH SCREEN ===== -->', rate_modal_html + '\n  <!-- ===== SPLASH SCREEN ===== -->')
    print("✓ Added #rate-modal into index.html")

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Add Rate Modal JS Controller in app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

rate_js_code = """
// ══════════════════════════════════════════════════════════════════════════════
// ⭐ 5-STAR APP RATING & FEEDBACK CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.currentSelectedRating = 5;

window.openRateModal = function() {
  const drawer = document.querySelector('.app-drawer');
  if (drawer) drawer.classList.remove('open');
  const overlay = document.querySelector('.drawer-overlay');
  if (overlay) overlay.style.display = 'none';

  const modal = document.getElementById('rate-modal');
  if (modal) modal.style.display = 'flex';
  window.selectAppRating(5);
};

window.closeRateModal = function() {
  const modal = document.getElementById('rate-modal');
  if (modal) modal.style.display = 'none';
};

window.hoverAppRating = function(stars) {
  const labels = [
    '⭐ सुधार की आवश्यकता है',
    '⭐⭐ ठीक है (Average)',
    '⭐⭐⭐ अच्छा अनुभव (Good)',
    '⭐⭐⭐⭐ बहुत अच्छा (Very Good)',
    '⭐⭐⭐⭐⭐ अत्यंत दिव्य व उत्कृष्ट! 🙏'
  ];
  const lbl = document.getElementById('rate-mood-label');
  if (lbl) lbl.textContent = labels[stars - 1] || '';

  const starEls = document.querySelectorAll('.rate-star');
  starEls.forEach((el, idx) => {
    if (idx < stars) {
      el.style.opacity = '1';
      el.style.transform = 'scale(1.15)';
    } else {
      el.style.opacity = '0.35';
      el.style.transform = 'scale(1.0)';
    }
  });
};

window.selectAppRating = function(stars) {
  window.currentSelectedRating = stars;
  window.hoverAppRating(stars);
  if (navigator.vibrate) navigator.vibrate(30);
};

window.submitAppRating = function() {
  const stars = window.currentSelectedRating;
  const feedback = document.getElementById('rate-feedback-input')?.value || '';

  localStorage.setItem('sanatan_app_rating', stars.toString());
  if (feedback) {
    localStorage.setItem('sanatan_app_feedback', feedback);
  }

  // Award +10 Punya Points
  let pts = parseInt(localStorage.getItem('sanatan_sadhana_points') || '108');
  pts += 10;
  localStorage.setItem('sanatan_sadhana_points', pts.toString());

  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (typeof playSoundEffect === 'function') playSoundEffect('victory');

  window.closeRateModal();

  if (typeof showToast === 'function') {
    showToast(`⭐ ${stars}-स्टार रेटिंग व समीक्षा हेतु धन्यवाद! (+10 अंक अर्जित 🙏)`);
  }
};
"""

if '5-STAR APP RATING & FEEDBACK CONTROLLER' not in app_js:
    with open('app.js', 'a', encoding='utf-8') as f:
        f.write(rate_js_code)
    print("✓ Added Rate Modal JS Controller to app.js")
else:
    print("Rate Modal Controller already present in app.js")

print(f"✓ Rate Modal fully integrated and live (v={ts})")
