import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Append Luxury Light Mode & Dark Mode CSS to styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

luxury_theme_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   🌓 GLOBAL LUXURY ROYAL DARK & VEDIC GOLDEN LIGHT THEME ENGINE
   ══════════════════════════════════════════════════════════════════════════════ */

/* Default Dark Theme Tokens */
:root {
  --bg-primary: #0C0219;
  --bg-secondary: #17042B;
  --card-surface: #1E0738;
  --text-main: #FFFDF8;
  --text-sub: #CBD5E1;
  --gold-accent: #F8C83B;
  --border-gold: rgba(248, 200, 59, 0.35);
  --header-bg: rgba(18, 3, 36, 0.88);
  --nav-bg: rgba(16, 2, 31, 0.92);
}

/* ☀️ DIVYA VEDIC GOLDEN LIGHT THEME ☀️ */
html[data-theme="light"], body.theme-light {
  --bg-primary: #FFFBF0 !important;
  --bg-secondary: #FFF6E0 !important;
  --card-surface: #FFFFFF !important;
  --text-main: #2D1400 !important;
  --text-sub: #653A10 !important;
  --gold-accent: #D97706 !important;
  --border-gold: rgba(217, 119, 6, 0.3) !important;
  --header-bg: rgba(255, 253, 247, 0.92) !important;
  --nav-bg: rgba(255, 252, 242, 0.95) !important;

  background: #FFFBF0 !important;
  color: #2D1400 !important;
}

body.theme-light .app-main,
body.theme-light .page {
  background: #FFFBF0 !important;
  color: #2D1400 !important;
}

body.theme-light .app-header {
  background: var(--header-bg) !important;
  border-bottom: 1.5px solid rgba(217, 119, 6, 0.25) !important;
  box-shadow: 0 4px 20px rgba(180, 83, 9, 0.08) !important;
}

body.theme-light .header-title {
  color: #3B1600 !important;
}

body.theme-light .bottom-nav {
  background: var(--nav-bg) !important;
  border-top: 1.5px solid rgba(217, 119, 6, 0.2) !important;
  box-shadow: 0 -4px 25px rgba(180, 83, 9, 0.08) !important;
}

body.theme-light .nav-tab {
  color: #78350F !important;
}

body.theme-light .nav-tab.active {
  color: #D97706 !important;
}

body.theme-light .nav-tab.active .nav-icon-wrap {
  background: linear-gradient(135deg, #FDE68A, #F59E0B) !important;
  color: #1A0B2E !important;
}

/* Light Theme Cards & Containers */
body.theme-light .bhakti-leen-hero {
  background: radial-gradient(circle at 50% 30%, #FFEFC2 0%, #FFF5D6 50%, #FFFBF0 100%) !important;
  border-bottom: 1.5px solid rgba(217, 119, 6, 0.2) !important;
}

body.theme-light .bhakti-leen-title {
  color: #451A03 !important;
  text-shadow: 0 1px 4px rgba(245, 158, 11, 0.3) !important;
}

body.theme-light .bhakti-leen-sub {
  color: #78350F !important;
}

body.theme-light .bhakti-shloka-bar {
  background: rgba(245, 158, 11, 0.15) !important;
  color: #92400E !important;
  border: 1px solid rgba(217, 119, 6, 0.3) !important;
}

/* Grid & Action Cards in Light Mode */
body.theme-light .grid-card,
body.theme-light .fest-card,
body.theme-light .gallery-card-item,
body.theme-light .amrit-mood-card,
body.theme-light .panchang-card,
body.theme-light .top10-card,
body.theme-light .vrat-card {
  background: #FFFFFF !important;
  color: #2D1400 !important;
  border: 1.5px solid rgba(217, 119, 6, 0.22) !important;
  box-shadow: 0 6px 20px rgba(180, 83, 9, 0.08) !important;
}

body.theme-light .grid-card:hover,
body.theme-light .fest-card:hover {
  box-shadow: 0 10px 25px rgba(217, 119, 6, 0.18) !important;
  border-color: #D97706 !important;
}

body.theme-light .setting-row {
  background: #FFFFFF !important;
  border: 1px solid rgba(217, 119, 6, 0.2) !important;
  color: #2D1400 !important;
}

body.theme-light .setting-row span {
  color: #2D1400 !important;
}

body.theme-light .page-header-bar {
  background: var(--header-bg) !important;
  border-bottom: 1.5px solid rgba(217, 119, 6, 0.2) !important;
  color: #2D1400 !important;
}

body.theme-light .page-header-bar h2 {
  color: #2D1400 !important;
}

body.theme-light .back-btn {
  background: rgba(217, 119, 6, 0.12) !important;
  color: #78350F !important;
}

/* Live Radio Bar in Light Mode */
body.theme-light #home-live-radio-card {
  background: linear-gradient(135deg, #FFF6E0 0%, #FFE9B8 100%) !important;
  border: 1.5px solid rgba(217, 119, 6, 0.35) !important;
  box-shadow: 0 8px 25px rgba(180, 83, 9, 0.12) !important;
}

body.theme-light #radio-live-subtitle {
  color: #78350F !important;
}

body.theme-light .radio-chan-btn {
  background: rgba(255, 255, 255, 0.75) !important;
  color: #78350F !important;
  border: 1px solid rgba(217, 119, 6, 0.25) !important;
}

body.theme-light .radio-chan-btn.active {
  background: linear-gradient(135deg, #F59E0B, #D97706) !important;
  color: #FFFFFF !important;
  border: none !important;
}

/* Navigation Drawer in Light Mode */
body.theme-light .app-drawer {
  background: #FFFBF2 !important;
  border-right: 1.5px solid rgba(217, 119, 6, 0.25) !important;
  box-shadow: 8px 0 35px rgba(180, 83, 9, 0.12) !important;
}

body.theme-light .drawer-header {
  background: linear-gradient(135deg, #FFEEC4 0%, #FFDF94 100%) !important;
  border-bottom: 1.5px solid rgba(217, 119, 6, 0.25) !important;
}

body.theme-light .drawer-title {
  color: #3B1600 !important;
}

body.theme-light .drawer-item {
  color: #3B1600 !important;
}

body.theme-light .drawer-item:hover {
  background: rgba(245, 158, 11, 0.15) !important;
}

/* Smooth Transition for Global Theme Toggle */
body, .app-header, .bottom-nav, .page, .grid-card, .fest-card, .setting-row {
  transition: background 0.3s ease, color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}
"""

if 'GLOBAL LUXURY ROYAL DARK & VEDIC GOLDEN LIGHT THEME ENGINE' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write(luxury_theme_css)
    print("✓ Appended Global Theme CSS to styles.css")
else:
    print("Theme CSS already present in styles.css")

# 2. Update index.html to add Theme Toggle in Header and in Settings
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Theme Toggle Button to Top App Header
old_header = """  <!-- TOP HEADER -->
  <header class="app-header">
    <button id="hamburger-btn" class="icon-btn" aria-label="मेनू">
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
    </button>
    <h1 class="header-title">भक्ति में लीन</h1>
    <img src="assets/app_logo.jpg?v=1787490651276" alt="लोगो" class="header-logo" />
  </header>"""

new_header = """  <!-- TOP HEADER -->
  <header class="app-header">
    <button id="hamburger-btn" class="icon-btn" aria-label="मेनू">
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
      <span class="hamburger-line"></span>
    </button>
    <h1 class="header-title">भक्ति में लीन</h1>
    <div style="display:flex; align-items:center; gap:8px;">
      <button id="global-theme-toggle-btn" onclick="toggleGlobalAppTheme()" title="थीम बदलें (Dark / Light Mode)" style="background:rgba(248,200,59,0.18); border:1.3px solid #F8C83B; color:#FDE68A; width:34px; height:34px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center; box-shadow:0 0 12px rgba(248,200,59,0.25); transition:transform 0.2s ease;">
        🌙
      </button>
      <img src="assets/app_logo.jpg?v=1787490651276" alt="लोगो" class="header-logo" />
    </div>
  </header>"""

if old_header in html:
    html = html.replace(old_header, new_header)
    print("✓ Added Global Theme Toggle Button to App Header in index.html")

# Update Settings Page with Interactive Dark/Light Theme Row
old_settings_dark = """        <div class="setting-row"><span data-i18n="dark_mode">🌙 डार्क मोड</span>
          <label class="toggle-switch"><input type="checkbox" id="dark-mode-toggle"/><span class="toggle-slider"></span></label>
        </div>"""

new_settings_dark = """        <div class="setting-row" style="display:flex; align-items:center; justify-content:space-between; padding:12px 14px;">
          <div>
            <div style="font-weight:800; font-size:0.92rem; display:flex; align-items:center; gap:6px;">
              <span id="settings-theme-icon">🌙</span> <span id="settings-theme-label">डार्क मोड (Dark Mode)</span>
            </div>
            <div style="font-size:0.72rem; color:var(--text-sub, #CBD5E1); margin-top:2px;">
              रॉयल डार्क एवं वैदिक स्वर्णिम लाइट मोड
            </div>
          </div>
          <button onclick="toggleGlobalAppTheme()" id="settings-theme-btn" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-size:0.75rem; font-weight:900; padding:6px 14px; border-radius:12px; cursor:pointer; box-shadow:0 2px 10px rgba(248,200,59,0.3);">
            थीम बदलें 🌓
          </button>
        </div>"""

if old_settings_dark in html:
    html = html.replace(old_settings_dark, new_settings_dark)
    print("✓ Updated Settings Page Theme Controls in index.html")

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Add Global Theme System in app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

theme_js_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 🌓 GLOBAL DARK & LIGHT THEME CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.isGlobalLightMode = localStorage.getItem('sanatan_app_theme') === 'light';

window.applyGlobalTheme = function() {
  const isLight = window.isGlobalLightMode;
  const headerBtn = document.getElementById('global-theme-toggle-btn');
  const settingsIcon = document.getElementById('settings-theme-icon');
  const settingsLabel = document.getElementById('settings-theme-label');

  if (isLight) {
    document.documentElement.setAttribute('data-theme', 'light');
    document.body.classList.remove('theme-dark');
    document.body.classList.add('theme-light');

    if (headerBtn) {
      headerBtn.textContent = '☀️';
      headerBtn.title = 'डार्क मोड सक्रिय करें';
      headerBtn.style.background = 'rgba(217, 119, 6, 0.18)';
      headerBtn.style.borderColor = '#D97706';
      headerBtn.style.color = '#78350F';
    }

    if (settingsIcon) settingsIcon.textContent = '☀️';
    if (settingsLabel) settingsLabel.textContent = 'लाइट मोड (Vedic Light)';

  } else {
    document.documentElement.setAttribute('data-theme', 'dark');
    document.body.classList.remove('theme-light');
    document.body.classList.add('theme-dark');

    if (headerBtn) {
      headerBtn.textContent = '🌙';
      headerBtn.title = 'लाइट मोड सक्रिय करें';
      headerBtn.style.background = 'rgba(248, 200, 59, 0.18)';
      headerBtn.style.borderColor = '#F8C83B';
      headerBtn.style.color = '#FDE68A';
    }

    if (settingsIcon) settingsIcon.textContent = '🌙';
    if (settingsLabel) settingsLabel.textContent = 'डार्क मोड (Royal Dark)';
  }
};

window.toggleGlobalAppTheme = function() {
  window.isGlobalLightMode = !window.isGlobalLightMode;
  localStorage.setItem('sanatan_app_theme', window.isGlobalLightMode ? 'light' : 'dark');
  window.applyGlobalTheme();

  if (navigator.vibrate) navigator.vibrate(40);

  if (typeof showToast === 'function') {
    showToast(window.isGlobalLightMode ? '☀️ वैदिक स्वर्णिम लाइट मोड सक्रिय' : '🌙 रॉयल वेल्वेट डार्क मोड सक्रिय');
  }
};

// Initialize theme on start
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', window.applyGlobalTheme);
} else {
  window.applyGlobalTheme();
}
"""

if 'GLOBAL DARK & LIGHT THEME CONTROLLER' not in app_js:
    with open('app.js', 'a', encoding='utf-8') as f:
        f.write(theme_js_code)
    print("✓ Added Global Theme Controller to app.js")
else:
    print("Theme Controller already present in app.js")

print(f"✓ Global Theme Engine fully built and synchronized (v={ts})")
