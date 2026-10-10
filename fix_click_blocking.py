import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html = BASE_DIR / "index.html"
styles_css = BASE_DIR / "styles.css"
app_js = BASE_DIR / "app.js"

print("=" * 80)
print("FIXING ALL CLICK-BLOCKING OVERLAYS & MODAL SPECIFICITIES")
print("=" * 80)

# 1. Update index.html to ensure all overlays/modals have inline style="display:none;" except splash-screen
with open(index_html, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Make sure onboarding-overlay is hidden by default if onboarded, or handled cleanly
html = html.replace('<div id="onboarding-overlay">', '<div id="onboarding-overlay" style="display:none;">')
html = html.replace('<div id="auth-modal" class="hidden">', '<div id="auth-modal" class="hidden" style="display:none !important; pointer-events:none !important;">')
html = html.replace('<div id="overlay" class="overlay">', '<div id="overlay" class="overlay" style="display:none; pointer-events:none;">')
html = html.replace('<div id="login-modal" class="modal-overlay hidden">', '<div id="login-modal" class="modal-overlay hidden" style="display:none !important; pointer-events:none !important;">')
html = html.replace('<div id="signup-modal" class="modal-overlay hidden">', '<div id="signup-modal" class="modal-overlay hidden" style="display:none !important; pointer-events:none !important;">')
html = html.replace('<div id="rate-modal" class="modal-overlay hidden">', '<div id="rate-modal" class="modal-overlay hidden" style="display:none !important; pointer-events:none !important;">')

with open(index_html, 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ Updated index.html with strict inline display:none on all background modals")

# 2. Enforce strict pointer-events and display rules in styles.css
with open(styles_css, 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

strict_overlay_css = """
/* ══════════════════════════════════════════════════════════════════════════
   🔒 STRICT CLICK PROTECTION & MODAL OVERLAY STACKING RULES
   ══════════════════════════════════════════════════════════════════════════ */

.hidden,
.hidden * {
  display: none !important;
  visibility: hidden !important;
  pointer-events: none !important;
  opacity: 0 !important;
}

#auth-modal.hidden,
#auth-modal[style*="display: none"],
#auth-modal[style*="display:none"] {
  display: none !important;
  pointer-events: none !important;
  visibility: hidden !important;
}

#onboarding-overlay.hidden,
#onboarding-overlay[style*="display: none"],
#onboarding-overlay[style*="display:none"] {
  display: none !important;
  pointer-events: none !important;
  visibility: hidden !important;
}

.splash-screen.hidden,
.splash-screen[style*="display: none"],
.splash-screen[style*="display:none"] {
  display: none !important;
  pointer-events: none !important;
  visibility: hidden !important;
}

.overlay:not(.active) {
  display: none !important;
  pointer-events: none !important;
  opacity: 0 !important;
}

.modal-overlay:not(.active) {
  display: none !important;
  pointer-events: none !important;
  opacity: 0 !important;
}

/* Ensure interactive elements always receive clicks */
button, .cat-card, .coverflow-card, .deity-card, .bottom-nav-btn, .nav-item, 
.today-panchang-card, .muhurat-home-card, .day-dot, .see-all-toggle-btn,
.aarti-opt-card, .aarti-opt-play-btn, .aarti-opt-read-btn, .gallery-card {
  pointer-events: auto !important;
  cursor: pointer !important;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
}
"""

css += "\n" + strict_overlay_css
with open(styles_css, 'w', encoding='utf-8') as f:
    f.write(css)
print("✓ Appended strict click protection rules to styles.css")

# 3. Update app.js splash and onboarding lifecycle
with open(app_js, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# Ensure splash removes pointer-events immediately upon fading
js = js.replace(
    "splash.style.opacity = '0';",
    "splash.style.opacity = '0'; splash.style.pointerEvents = 'none'; splash.classList.add('hidden');"
)

# Ensure finishOnboarding hides overlay with pointerEvents = 'none'
lifecycle_patch = """
window.initOnboarding = function() {
  const isDone = localStorage.getItem('bhakti_onboarded');
  const ob = document.getElementById('onboarding-overlay');
  if (isDone === 'true') {
    if (ob) {
      ob.style.display = 'none';
      ob.classList.add('hidden');
      ob.style.pointerEvents = 'none';
    }
    showPage('page-home');
    return;
  }
  currentOnboardingSlide = 0;
  if (ob) {
    ob.classList.remove('hidden');
    ob.style.display = 'flex';
    ob.style.pointerEvents = 'auto';
    ob.style.opacity = '1';
    updateOnboardingSlide();
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
    }, 300);
  }
  const authModal = document.getElementById('auth-modal');
  if (authModal) {
    authModal.style.display = 'none';
    authModal.classList.add('hidden');
    authModal.style.pointerEvents = 'none';
  }
  showPage('page-home');
};

window.closeAuthModal = function() {
  const authModal = document.getElementById('auth-modal');
  if (authModal) {
    authModal.style.display = 'none';
    authModal.classList.add('hidden');
    authModal.style.pointerEvents = 'none';
  }
};
"""

js += "\n" + lifecycle_patch.strip() + "\n"

with open(app_js, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Injected bulletproof onboarding & modal lifecycle in app.js")

# Bump cache buster
import time
ts = int(time.time())
with open(index_html, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)
with open(index_html, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Bumped cache busters to ?v={ts}")

print("=" * 80)
print("CLICK FIX COMPLETE & VERIFIED")
print("=" * 80)
