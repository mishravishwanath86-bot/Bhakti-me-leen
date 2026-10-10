import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🌓 IMPLEMENTING GLOBAL DARK & LIGHT THEME ENGINE")
print("======================================================================")

# 1. Append complete theme CSS to styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

luxury_theme_css = """
/* ══════════════════════════════════════════════════════════════════════════════
   🌓 DIVINE VEDIC GLOBAL DARK & LIGHT THEME SYSTEM
   ══════════════════════════════════════════════════════════════════════════════ */

/* Default / Dark Theme Variables */
:root {
  --app-bg: #0A0118;
  --app-card-bg: #1B062E;
  --app-card-border: rgba(248, 200, 59, 0.35);
  --app-text-primary: #FFFDF8;
  --app-text-secondary: #CBD5E1;
  --app-text-gold: #FDE68A;
  --app-gold-accent: #F8C83B;
  --app-header-bg: rgba(18, 3, 36, 0.92);
  --app-nav-bg: rgba(16, 2, 31, 0.94);
}

/* ☀️ DIVINE VEDIC GOLDEN LIGHT THEME ☀️ */
html[data-theme="light"],
body.theme-light,
body.light-mode {
  --app-bg: #FFFBF0 !important;
  --app-card-bg: #FFFFFF !important;
  --app-card-border: rgba(217, 119, 6, 0.28) !important;
  --app-text-primary: #2D1400 !important;
  --app-text-secondary: #653A10 !important;
  --app-text-gold: #92400E !important;
  --app-gold-accent: #D97706 !important;
  --app-header-bg: rgba(255, 252, 245, 0.94) !important;
  --app-nav-bg: rgba(255, 250, 238, 0.96) !important;

  background-color: #FFFBF0 !important;
  color: #2D1400 !important;
}

body.theme-light .app-main,
body.theme-light .page,
body.theme-light .page-content {
  background: #FFFBF0 !important;
  color: #2D1400 !important;
}

/* Header & Nav in Light Mode */
body.theme-light .app-header {
  background: rgba(255, 252, 245, 0.94) !important;
  border-bottom: 1.5px solid rgba(217, 119, 6, 0.25) !important;
  box-shadow: 0 4px 20px rgba(180, 83, 9, 0.08) !important;
}

body.theme-light .header-title {
  color: #3B1600 !important;
}

body.theme-light .bottom-nav {
  background: rgba(255, 250, 238, 0.96) !important;
  border-top: 1.5px solid rgba(217, 119, 6, 0.22) !important;
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

/* Hero & Coverflow in Light Mode */
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

/* Cards & Surfaces in Light Mode */
body.theme-light .grid-card,
body.theme-light .fest-card,
body.theme-light .gallery-card-item,
body.theme-light .amrit-mood-card,
body.theme-light .panchang-card,
body.theme-light .top10-card,
body.theme-light .vrat-card,
body.theme-light .setting-card,
body.theme-light .katha-card,
body.theme-light .bhajan-card {
  background: #FFFFFF !important;
  color: #2D1400 !important;
  border: 1.5px solid rgba(217, 119, 6, 0.22) !important;
  box-shadow: 0 6px 20px rgba(180, 83, 9, 0.08) !important;
}

body.theme-light .page-header-bar {
  background: rgba(255, 252, 245, 0.94) !important;
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

/* Modals in Light Mode */
body.theme-light .reader-body {
  background: #FFFDF8 !important;
  color: #2D1400 !important;
}

body.theme-light .side-drawer {
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
body, .app-header, .bottom-nav, .page, .grid-card, .fest-card, .setting-card, .side-drawer {
  transition: background 0.25s ease, color 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
}
"""

if 'DIVINE VEDIC GLOBAL DARK & LIGHT THEME SYSTEM' in css:
    css = re.sub(r'/\* ══════════════════════════════════════════════════════════════════════════════\s*🌓 DIVINE VEDIC GLOBAL DARK & LIGHT THEME SYSTEM[\s\S]*', '', css)

css += '\n\n' + luxury_theme_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✓ Updated styles.css with complete Theme styling")

# 2. Add Theme Card to page-settings in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

settings_theme_card_html = """        <!-- 🌓 THEME SELECTION (DARK / LIGHT MODE) ROW 🌓 -->
        <div id="settings-theme-card" style="background:rgba(255,255,255,0.05); border:1.3px solid rgba(248,200,59,0.3); border-radius:22px; padding:1.2rem; margin-bottom:1.2rem; box-shadow:0 8px 25px rgba(0,0,0,0.4);">
          <div style="display:flex; align-items:center; justify-content:space-between;">
            <div style="display:flex; align-items:center; gap:10px;">
              <span id="settings-theme-icon" style="font-size:1.4rem;">🌙</span>
              <div>
                <div style="font-size:0.95rem; font-weight:900; color:#FFFDF8;">ऐप थीम (App Theme)</div>
                <div id="settings-theme-label" style="font-size:0.75rem; color:#FDE68A; font-weight:700; margin-top:2px;">
                  🌙 रॉयल वेल्वेट डार्क मोड
                </div>
              </div>
            </div>
            <button onclick="toggleGlobalAppTheme()" id="settings-theme-btn" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-size:0.8rem; font-weight:900; padding:7px 14px; border-radius:12px; cursor:pointer; box-shadow:0 3px 12px rgba(248,200,59,0.35); display:flex; align-items:center; gap:4px;">
              <span>🌓</span> थीम बदलें ❯
            </button>
          </div>
        </div>
"""

# Insert before language selection row in page-settings if not present
if 'id="settings-theme-card"' not in html:
    html = html.replace('<!-- 🌐 MULTI-LANGUAGE (i18n) SELECTION ROW 🌐 -->', settings_theme_card_html + '\n        <!-- 🌐 MULTI-LANGUAGE (i18n) SELECTION ROW 🌐 -->')
    print("✓ Added Theme Selection Card to page-settings in index.html")

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Add Theme Controller to app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

theme_controller_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 🌓 GLOBAL DARK & LIGHT THEME CONTROLLER ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.isGlobalLightMode = localStorage.getItem('sanatan_app_theme') === 'light';

window.applyGlobalTheme = function() {
  const isLight = window.isGlobalLightMode;
  const headerBtn = document.getElementById('global-theme-toggle-btn');
  const settingsIcon = document.getElementById('settings-theme-icon');
  const settingsLabel = document.getElementById('settings-theme-label');

  if (isLight) {
    document.documentElement.setAttribute('data-theme', 'light');
    document.body.classList.remove('theme-dark', 'dark-mode');
    document.body.classList.add('theme-light', 'light-mode');

    if (headerBtn) {
      headerBtn.innerHTML = '☀️';
      headerBtn.title = 'डार्क मोड सक्रिय करें (Switch to Dark Mode)';
      headerBtn.style.background = 'rgba(217, 119, 6, 0.2)';
      headerBtn.style.borderColor = '#D97706';
      headerBtn.style.color = '#78350F';
      headerBtn.style.boxShadow = '0 0 12px rgba(217, 119, 6, 0.4)';
    }

    if (settingsIcon) settingsIcon.textContent = '☀️';
    if (settingsLabel) settingsLabel.textContent = '☀️ वैदिक स्वर्णिम लाइट मोड';

  } else {
    document.documentElement.setAttribute('data-theme', 'dark');
    document.body.classList.remove('theme-light', 'light-mode');
    document.body.classList.add('theme-dark', 'dark-mode');

    if (headerBtn) {
      headerBtn.innerHTML = '🌙';
      headerBtn.title = 'लाइट मोड सक्रिय करें (Switch to Light Mode)';
      headerBtn.style.background = 'rgba(248, 200, 59, 0.18)';
      headerBtn.style.borderColor = '#F8C83B';
      headerBtn.style.color = '#FDE68A';
      headerBtn.style.boxShadow = '0 0 12px rgba(248, 200, 59, 0.25)';
    }

    if (settingsIcon) settingsIcon.textContent = '🌙';
    if (settingsLabel) settingsLabel.textContent = '🌙 रॉयल वेल्वेट डार्क मोड';
  }
};

window.toggleGlobalAppTheme = function() {
  window.isGlobalLightMode = !window.isGlobalLightMode;
  localStorage.setItem('sanatan_app_theme', window.isGlobalLightMode ? 'light' : 'dark');
  window.applyGlobalTheme();

  if (navigator.vibrate) navigator.vibrate(35);
  if (typeof playSoundEffect === 'function') playSoundEffect('click');

  if (typeof showToast === 'function') {
    showToast(window.isGlobalLightMode ? '☀️ वैदिक स्वर्णिम लाइट मोड सक्रिय' : '🌙 रॉयल वेल्वेट डार्क मोड सक्रिय');
  }
};

window.setAppTheme = function(themeName) {
  window.isGlobalLightMode = (themeName === 'light');
  localStorage.setItem('sanatan_app_theme', themeName);
  window.applyGlobalTheme();
};

// Auto-run theme initializer immediately
window.applyGlobalTheme();
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', window.applyGlobalTheme);
}
"""

if 'GLOBAL DARK & LIGHT THEME CONTROLLER ENGINE' in app_js:
    app_js = re.sub(r'/\* ══════════════════════════════════════════════════════════════════════════════\s*🌓 GLOBAL DARK & LIGHT THEME CONTROLLER ENGINE[\s\S]*', '', app_js)
    app_js = re.sub(r'// ══════════════════════════════════════════════════════════════════════════════\s*// 🌓 GLOBAL DARK & LIGHT THEME CONTROLLER ENGINE[\s\S]*', '', app_js)

app_js += '\n\n' + theme_controller_code

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("✓ Added Theme Controller to app.js")
print("✓ Complete Theme Engine synchronized successfully!")
