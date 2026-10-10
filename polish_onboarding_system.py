import re, sys, time
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html = BASE_DIR / "index.html"
app_js = BASE_DIR / "app.js"

ts = int(time.time())

# 1. Update index.html cache busters
with open(index_html, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

html = re.sub(r'app\.js(\?v=\d+)?', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css(\?v=\d+)?', f'styles.css?v={ts}', html)

with open(index_html, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Updated index.html cache-buster to ?v={ts}")

# 2. Make finishOnboarding and nextOnboardingSlide ultra-smooth and reliable
with open(app_js, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# Make sure finishOnboarding seamlessly navigates to home page
smooth_finish_js = """
window.finishOnboarding = function() {
  try { localStorage.setItem('bhakti_onboarded', 'true'); } catch(e) {}
  const ob = document.getElementById('onboarding-overlay');
  if (ob) {
    ob.style.opacity = '0';
    ob.style.transition = 'opacity 0.3s ease';
    setTimeout(() => { 
      ob.style.display = 'none'; 
      ob.classList.add('hidden');
    }, 300);
  }
  if (typeof showPage === 'function') {
    showPage('page-home');
  }
};

window.nextOnboardingSlide = function() {
  if (currentOnboardingSlide < totalOnboardingSlides - 1) {
    currentOnboardingSlide++;
    updateOnboardingSlide();
  } else {
    finishOnboarding();
  }
};
"""

# Append / ensure finishOnboarding & nextOnboardingSlide override at end of app.js
js += "\n" + smooth_finish_js.strip() + "\n"

with open(app_js, 'w', encoding='utf-8') as f:
    f.write(js)
print("✓ Injected smooth finishOnboarding & nextOnboardingSlide handlers into app.js")
