import re, sys, os
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("UNIFYING SHOWPAGE, ONBOARDING, AUTH MODAL & FULL APP INITIALIZATION")
print("=" * 80)

with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# 1. Master showPage implementation
master_showpage_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🚀 MASTER UNIFIED NAVIGATION ROUTER (WINDOW.SHOWPAGE)
// ══════════════════════════════════════════════════════════════════════════════

window.showPage = function(pageId) {
  if (!pageId) return;
  
  // Normalize pageId
  if (!pageId.startsWith('page-')) {
    pageId = 'page-' + pageId;
  }

  const targetPage = document.getElementById(pageId);
  if (!targetPage) {
    console.warn('Page element not found:', pageId);
    return;
  }

  // 1. Switch active page
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  targetPage.classList.add('active');
  window.currentPage = pageId;

  // 2. Update Bottom Nav active state
  document.querySelectorAll('.bottom-nav .nav-item, .bottom-nav-btn').forEach(btn => {
    const p = btn.dataset.page || btn.getAttribute('data-page');
    if (p === pageId) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // 3. Update Header title if applicable
  const titles = {
    'page-home': 'भक्ति में लीन',
    'page-bhajan': 'भजन संग्रह',
    'page-aarti': 'नित्य आरती',
    'page-mantra': 'दिव्य मंत्र',
    'page-chalisa': 'श्री चालीसा',
    'page-desh': 'देशभक्ति',
    'page-ramayana': 'रामायण',
    'page-profile': 'प्रोफ़ाइल',
    'page-settings': 'सेटिंग्स',
    'page-about': 'हमारे बारे में',
    'page-downloads': 'डाउनलोड्स',
    'page-reader': 'पावन पाठ',
    'page-calendar': 'हिन्दी कैलेंडर',
    'page-english-calendar': 'अंग्रेजी कैलेंडर',
    'page-katha': 'ऑडियो लाइब्रेरी',
    'page-achievements': 'उपलब्धियां',
    'page-panchang': 'दैनिक पंचांग',
    'page-month-panchang': 'मासिक पंचांग',
    'page-muhurat': 'शुभ मुहूर्त',
    'page-vrat-detail': 'व्रत विवरण',
    'page-jar': 'भक्ति अमृत कलश',
    'page-mala': 'जाप माला',
    'page-gallery': 'पावन दिव्य गैलरी',
    'page-top10': 'शीर्ष 10 भक्ति'
  };
  const headerTitleEl = document.querySelector('.header-title');
  if (headerTitleEl && titles[pageId]) {
    headerTitleEl.textContent = titles[pageId];
  }

  // 4. Scroll to top
  window.scrollTo(0, 0);

  // 5. Page specific hooks
  if (pageId === 'page-gallery' && typeof renderDivineGallery === 'function') {
    setTimeout(renderDivineGallery, 20);
  }
  if (pageId === 'page-katha' && typeof initKathaPage === 'function') {
    initKathaPage();
  }
  if (pageId === 'page-calendar' && typeof renderCalGrid === 'function' && typeof calYear !== 'undefined' && typeof calMonth !== 'undefined') {
    renderCalGrid(calYear, calMonth);
  }
  if (typeof updateMiniPlayerVisibility === 'function') {
    updateMiniPlayerVisibility(pageId);
  }

  // 6. Dispatch page change event
  document.dispatchEvent(new CustomEvent('bhakti-page-change', { detail: pageId }));
};

window.navigateTo = window.showPage;
"""

# 2. Master Onboarding & Auth Lifecycle
master_onboarding_auth_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🌟 BULLETPROOF ONBOARDING & AUTH CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.currentOnboardingSlide = 0;
window.totalOnboardingSlides = 5;
window.currentAuthTab = 'login';

window.initOnboarding = function() {
  const isDone = localStorage.getItem('bhakti_onboarded');
  const ob = document.getElementById('onboarding-overlay');
  
  if (isDone === 'true') {
    if (ob) {
      ob.style.display = 'none';
      ob.classList.add('hidden');
    }
    window.showPage('page-home');
    return;
  }

  window.currentOnboardingSlide = 0;
  if (ob) {
    ob.classList.remove('hidden');
    ob.style.display = 'flex';
    ob.style.opacity = '1';
    ob.style.pointerEvents = 'auto';
    window.updateOnboardingSlide();
  }
};

window.updateOnboardingSlide = function() {
  const track = document.getElementById('onboarding-track');
  const dots = document.querySelectorAll('.onboarding-dot');
  const nextBtn = document.getElementById('onboarding-next-btn');

  if (track) {
    track.style.transform = `translateX(-${window.currentOnboardingSlide * 100}vw)`;
  }

  dots.forEach((d, i) => {
    if (i === window.currentOnboardingSlide) d.classList.add('active');
    else d.classList.remove('active');
  });

  if (nextBtn) {
    nextBtn.textContent = window.currentOnboardingSlide === window.totalOnboardingSlides - 1 ? 'आरंभ करें ❯' : 'आगे बढ़ें ❯';
  }
};

window.nextOnboardingSlide = function() {
  if (window.currentOnboardingSlide < window.totalOnboardingSlides - 1) {
    window.currentOnboardingSlide++;
    window.updateOnboardingSlide();
  } else {
    window.finishOnboarding();
  }
};

window.finishOnboarding = function() {
  try { localStorage.setItem('bhakti_onboarded', 'true'); } catch(e) {}
  
  // Fade out onboarding overlay
  const ob = document.getElementById('onboarding-overlay');
  if (ob) {
    ob.style.opacity = '0';
    ob.style.pointerEvents = 'none';
    setTimeout(() => {
      ob.style.display = 'none';
      ob.classList.add('hidden');
    }, 300);
  }

  // Open Auth Modal (Login / Signup Screen)
  window.openAuthModal();
};

window.openAuthModal = function() {
  const authModal = document.getElementById('auth-modal');
  if (authModal) {
    authModal.classList.remove('hidden');
    authModal.style.display = 'flex';
    authModal.style.opacity = '1';
    authModal.style.pointerEvents = 'auto';
  }
};

window.closeAuthModal = function() {
  const authModal = document.getElementById('auth-modal');
  if (authModal) {
    authModal.style.opacity = '0';
    authModal.style.pointerEvents = 'none';
    setTimeout(() => {
      authModal.style.display = 'none';
      authModal.classList.add('hidden');
    }, 300);
  }
  window.showPage('page-home');
};

window.switchAuthTab = function(tab) {
  window.currentAuthTab = tab;
  const loginBtn = document.getElementById('tab-login');
  const signupBtn = document.getElementById('tab-signup');
  const nameInput = document.getElementById('auth-name');
  const submitBtn = document.getElementById('auth-submit-btn');

  if (tab === 'login') {
    if (loginBtn) loginBtn.classList.add('active');
    if (signupBtn) signupBtn.classList.remove('active');
    if (nameInput) nameInput.style.display = 'none';
    if (submitBtn) submitBtn.textContent = 'प्रवेश करें';
  } else {
    if (signupBtn) signupBtn.classList.add('active');
    if (loginBtn) loginBtn.classList.remove('active');
    if (nameInput) nameInput.style.display = 'block';
    if (submitBtn) submitBtn.textContent = 'खाता बनाएं';
  }
};

window.submitAuth = function() {
  const emailInput = document.getElementById('auth-email');
  const nameInput = document.getElementById('auth-name');
  const email = emailInput ? emailInput.value : '';
  const name = nameInput && nameInput.value ? nameInput.value : 'भक्त जन';

  const user = { name, email: email || 'bhakt@bhakti.app', isLoggedIn: true };
  try { localStorage.setItem('bhakti_user', JSON.stringify(user)); } catch(e) {}
  
  if (typeof updateProfileUI === 'function') updateProfileUI();
  if (typeof showToast === 'function') showToast(`🙏 स्वागत है, ${name}!`);
  
  window.closeAuthModal();
};

window.continueAsGuest = function() {
  const user = { name: 'अतिथि भक्त', email: 'guest@bhakti.app', isGuest: true };
  try { localStorage.setItem('bhakti_user', JSON.stringify(user)); } catch(e) {}
  
  if (typeof updateProfileUI === 'function') updateProfileUI();
  if (typeof showToast === 'function') showToast('🙏 जय श्री राम! आपका स्वागत है।');
  
  window.closeAuthModal();
};

window.continueWithGoogle = function() {
  const user = { name: 'Google भक्त', email: 'user@gmail.com', isGoogle: true };
  try { localStorage.setItem('bhakti_user', JSON.stringify(user)); } catch(e) {}
  
  if (typeof updateProfileUI === 'function') updateProfileUI();
  if (typeof showToast === 'function') showToast('✅ Google खाता सफलतापूर्वक जुड़ा!');
  
  window.closeAuthModal();
};

window.replayOnboarding = function() {
  const ob = document.getElementById('onboarding-overlay');
  if (ob) {
    ob.classList.remove('hidden');
    ob.style.display = 'flex';
    ob.style.opacity = '1';
    ob.style.pointerEvents = 'auto';
    window.currentOnboardingSlide = 0;
    window.updateOnboardingSlide();
  }
};
"""

# 3. Master Initialization Function
master_init_js = """
// ══════════════════════════════════════════════════════════════════════════════
// ⚡ MASTER INSTANT APPLICATION INITIALIZER
// ══════════════════════════════════════════════════════════════════════════════

window.initAllAppModules = function() {
  console.log("⚡ Initializing Bhakti App Modules...");
  
  const inits = [
    initNavigation, initDeityGrids, initPanchang, initCoverflow3D, 
    initFestivals, initCalendar, initMuhuratPage, initReader, 
    initDrawer, initPanchangPage, initKathaPage
  ];

  inits.forEach(fn => {
    try {
      if (typeof fn === 'function') fn();
    } catch(err) {
      console.warn('Module init warning:', err);
    }
  });

  // Ensure Panchang data is populated immediately
  if (typeof renderTodayPanchang === 'function') {
    renderTodayPanchang();
  }
  if (typeof updatePanchangCard === 'function') {
    updatePanchangCard();
  }
};

// Global Delegation for all clickable elements
document.addEventListener('click', function(e) {
  // Check for data-page
  const pageTarget = e.target.closest('[data-page]');
  if (pageTarget) {
    const pageId = pageTarget.getAttribute('data-page');
    if (pageId) {
      window.showPage(pageId);
      return;
    }
  }

  // Check for back-btn
  const backTarget = e.target.closest('.back-btn, [data-back]');
  if (backTarget) {
    const backPage = backTarget.dataset.back || window.readerBackPage || 'page-home';
    window.showPage(backPage);
    return;
  }
}, true);

// Execute on DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', window.initAllAppModules);
} else {
  window.initAllAppModules();
}

window.addEventListener('load', function() {
  window.initAllAppModules();
  
  const splash = document.getElementById('splash-screen');
  setTimeout(function() {
    if (splash) {
      splash.style.opacity = '0';
      splash.style.pointerEvents = 'none';
      setTimeout(function() {
        splash.style.display = 'none';
        splash.classList.add('hidden');
      }, 400);
    }
    window.initOnboarding();
  }, 1000);
});
"""

# Append Master components at the very end of app.js
js += "\n\n" + master_showpage_js.strip() + "\n\n" + master_onboarding_auth_js.strip() + "\n\n" + master_init_js.strip() + "\n"

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Injected Master Navigation Router, Onboarding/Auth & Initializer in app.js")

# 4. Clean index.html for auth modal buttons
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Make sure auth-modal has a clean close button and guest button
auth_modal_pattern = r'<div id="auth-modal"[\s\S]*?</div>\s*</div>'
auth_modal_clean_html = """  <!-- 🔐 GLASSMORPHIC AUTH SCREEN (LOGIN & SIGN UP) 🔐 -->
  <div id="auth-modal" class="hidden" style="display:none;">
    <div class="auth-card" style="position:relative;">
      
      <!-- Close Button -->
      <button onclick="closeAuthModal()" style="position:absolute; top:12px; right:12px; background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:32px; height:32px; border-radius:50%; font-size:1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>

      <!-- Unique Glowing Divine Emblem Logo -->
      <div class="auth-top-logo">
        <img src="assets/app_logo_circle.png?v=1787492434224" class="auth-logo-img" alt="Bhakti App Logo">
      </div>
      
      <div class="auth-tabs">
        <button class="auth-tab-btn active" id="tab-login" onclick="switchAuthTab('login')">लॉग इन</button>
        <button class="auth-tab-btn" id="tab-signup" onclick="switchAuthTab('signup')">साइन अप</button>
      </div>

      <div class="auth-input-group">
        <input type="text" class="auth-input" id="auth-name" placeholder="आपका शुभ नाम" style="display:none;" />
        <input type="email" class="auth-input" id="auth-email" placeholder="ईमेल अथवा मोबाइल नंबर" />
        <input type="password" class="auth-input" id="auth-pass" placeholder="पासवर्ड (वैकल्पिक)" />
      </div>

      <button class="auth-submit-btn" id="auth-submit-btn" onclick="submitAuth()">प्रवेश करें</button>

      <div class="auth-divider">
        <span>अथवा</span>
      </div>

      <div class="auth-social-row">
        <button class="auth-social-btn" onclick="continueWithGoogle()">
          <span style="font-size:1.2rem;">🌐</span> Google से जारी रखें
        </button>
        <button class="auth-guest-btn" onclick="continueAsGuest()" style="margin-top:8px;">
          👤 अतिथि के रूप में जारी रखें (Guest)
        </button>
      </div>

    </div>
  </div>"""

# Replace auth modal
pos_auth = html.find('id="auth-modal"')
if pos_auth != -1:
    pos_card = html.find('class="auth-card"', pos_auth)
    # Find matching closing div
    end_auth = html.find('</div>\n  </div>', pos_card) + 12
    html = html[:pos_auth-10] + auth_modal_clean_html[7:] + html[end_auth:]
    print("✓ Cleaned and modernized #auth-modal in index.html")

# Bump cache buster
import time
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Updated index.html with new cache buster ?v={ts}")

print("=" * 80)
print("CORE ENGINE UNIFICATION COMPLETE")
print("=" * 80)
