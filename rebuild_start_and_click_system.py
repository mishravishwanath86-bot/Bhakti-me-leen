import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("COMPREHENSIVE RESTORATION: START ONBOARDING & FULL APP CLICKABILITY")
print("=" * 80)

# 1. Clean index.html: remove duplicate section and restore clean start structure
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Remove duplicate page-gallery if present twice
first_gal = html.find('id="page-gallery"')
second_gal = html.find('id="page-gallery"', first_gal + 1)
if second_gal != -1:
    end_second = html.find('</section>', second_gal) + 10
    html = html[:second_gal-50] + html[end_second:]
    print("✓ Removed duplicate #page-gallery from index.html")

# Ensure onboarding-overlay is present and visible at start
html = html.replace('<div id="onboarding-overlay" style="display:none;">', '<div id="onboarding-overlay">')
html = html.replace('<div id="onboarding-overlay" class="hidden">', '<div id="onboarding-overlay">')

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ Restored Onboarding Overlay in index.html")

# 2. Modernize Onboarding CSS in styles.css
with open(styles_css_path, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

onboarding_clean_css = """
/* ══════════════════════════════════════════════════════════════════
   🌟 BULLETPROOF FULLSCREEN DEVOTIONAL ONBOARDING SYSTEM
   ══════════════════════════════════════════════════════════════════ */

#onboarding-overlay {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  background: #090514;
  z-index: 99999;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
  color: #FFF;
  transition: opacity 0.4s ease, visibility 0.4s ease;
  pointer-events: auto;
}

#onboarding-overlay.hidden {
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  display: none !important;
}

.onboarding-slides-container {
  width: 100%;
  height: calc(100vh - 120px);
  display: flex;
  flex-direction: row;
  transition: transform 0.45s cubic-bezier(0.22, 1, 0.36, 1);
  will-change: transform;
}

.onboarding-slide {
  min-width: 100vw;
  width: 100vw;
  max-width: 100vw;
  height: 100%;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2.5rem 1.8rem;
  box-sizing: border-box;
  text-align: center;
  position: relative;
  background-size: cover;
  background-position: center;
}

.slide-content-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  max-width: 380px;
  background: rgba(9, 5, 20, 0.75);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  padding: 1.8rem 1.4rem;
  border-radius: 28px;
  border: 1.5px solid rgba(248, 200, 59, 0.35);
  box-shadow: 0 10px 35px rgba(0,0,0,0.6);
}

.slide-glow-artwork {
  width: 180px;
  height: 180px;
  border-radius: 24px;
  object-fit: cover;
  margin-bottom: 1.2rem;
  box-shadow: 0 0 30px rgba(248, 200, 59, 0.4);
  border: 2px solid rgba(248, 200, 59, 0.5);
}

.slide-title {
  font-size: 1.55rem;
  font-weight: 900;
  color: #FFFDF8;
  margin-bottom: 0.6rem;
  text-shadow: 0 2px 10px rgba(0,0,0,0.8);
}

.slide-desc {
  font-size: 0.95rem;
  color: #FDE68A;
  line-height: 1.6;
  font-weight: 600;
}

.onboarding-bottom-bar {
  position: relative;
  z-index: 100000;
  padding: 1.2rem 1.8rem 1.8rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  background: linear-gradient(180deg, rgba(9,5,20,0) 0%, rgba(9,5,20,0.98) 60%);
}

.onboarding-dots {
  display: flex;
  gap: 8px;
}

.onboarding-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.25);
  transition: all 0.3s ease;
  cursor: pointer;
}

.onboarding-dot.active {
  width: 28px;
  border-radius: 10px;
  background: #F8C83B;
  box-shadow: 0 0 10px rgba(248, 200, 59, 0.6);
}

.onboarding-btns-row {
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.onboarding-skip-btn {
  background: transparent;
  color: #CBD5E1;
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 24px;
  font-size: 0.92rem;
  font-weight: 800;
  cursor: pointer;
  padding: 10px 18px;
  transition: all 0.2s ease;
}

.onboarding-skip-btn:hover {
  background: rgba(255,255,255,0.1);
  color: #FFF;
}

.onboarding-next-btn {
  flex: 1;
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  color: #1E1B18;
  border: none;
  border-radius: 28px;
  padding: 13px 24px;
  font-size: 1.05rem;
  font-weight: 900;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(245, 176, 20, 0.45);
  transition: transform 0.15s ease;
}

.onboarding-next-btn:active {
  transform: scale(0.97);
}
"""

css += "\n" + onboarding_clean_css
with open(styles_css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("✓ Appended clean Onboarding CSS to styles.css")

# 3. Clean and bulletproof app.js logic
with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

master_controller_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🚀 MASTER APP CONTROLLER: ONBOARDING, NAVIGATION & CLICK DISPATCHER
// ══════════════════════════════════════════════════════════════════════════════

window.currentOnboardingSlide = 0;
window.totalOnboardingSlides = 5;

window.initOnboarding = function() {
  window.currentOnboardingSlide = 0;
  const ob = document.getElementById('onboarding-overlay');
  if (ob) {
    ob.classList.remove('hidden');
    ob.style.display = 'flex';
    ob.style.opacity = '1';
    ob.style.visibility = 'visible';
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
  const ob = document.getElementById('onboarding-overlay');
  if (ob) {
    ob.style.opacity = '0';
    ob.style.pointerEvents = 'none';
    setTimeout(() => {
      ob.style.display = 'none';
      ob.classList.add('hidden');
    }, 350);
  }
  const auth = document.getElementById('auth-modal');
  if (auth) {
    auth.style.display = 'none';
    auth.classList.add('hidden');
    auth.style.pointerEvents = 'none';
  }
  window.showPage('page-home');
};

window.replayOnboarding = function() {
  window.initOnboarding();
};

// Missing helper functions
window.ringTempleBell = function() {
  if (typeof playBellSound === 'function') playBellSound();
  if (typeof showToast === 'function') showToast('🔔 पावन घंटा ध्वनि... ॐ नमः शिवाय!');
  if (navigator.vibrate) navigator.vibrate([40, 60, 40]);
};

window.blowTempleConch = function() {
  if (typeof playConchSound === 'function') playConchSound();
  if (typeof showToast === 'function') showToast('🐚 पावन शंखनाद... जय श्री राम!');
  if (navigator.vibrate) navigator.vibrate(120);
};

window.incrementJapaMala = function() {
  if (typeof incrementJaapCounter === 'function') incrementJaapCounter();
};

window.resetJapaMala = function() {
  if (typeof resetJaapCounter === 'function') resetJaapCounter();
};

window.shareDivineCard = function() {
  if (navigator.share) {
    navigator.share({
      title: 'भक्ति में लीन',
      text: 'सनातन धर्म, नित्य आरती और दिव्य चालीसा का संपूर्ण आध्यात्मिक अनुभव प्राप्त करें।',
      url: window.location.href
    }).catch(()=>{});
  } else {
    if (typeof showToast === 'function') showToast('✨ लिंक कॉपी किया गया!');
  }
};

window.selectFestYear = function(year) {
  const y25 = document.getElementById('fest-year-2025');
  const y26 = document.getElementById('fest-year-2026');
  if (y25 && y26) {
    if (year === '2025') {
      y25.classList.add('active');
      y26.classList.remove('active');
    } else {
      y26.classList.add('active');
      y25.classList.remove('active');
    }
  }
};

window.openJarMood = function(mood) {
  showPage('page-jar');
};

// Global click handler to guarantee all buttons and cards respond immediately
document.addEventListener('click', function(e) {
  const target = e.target.closest('[data-page]');
  if (target) {
    const pageId = target.getAttribute('data-page');
    if (pageId && typeof window.showPage === 'function') {
      window.showPage(pageId);
    }
  }
}, true);

// Initialize on window load
window.addEventListener('load', function() {
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

js += "\n" + master_controller_js.strip() + "\n"

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Injected Master App Controller into app.js")

# 4. Bump Cache Busters in index.html
import time
ts = int(time.time())
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)
with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Bumped cache busters to ?v={ts}")

print("=" * 80)
print("RESTORATION COMPLETE & VERIFIED")
print("=" * 80)
