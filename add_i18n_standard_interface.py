import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('i18n_engine.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update initial load check
js = js.replace("localStorage.getItem('bhakti_app_language') || 'hi';", "localStorage.getItem('user_app_language') || localStorage.getItem('bhakti_app_language') || 'hi';")

# Update localStorage set inside setAppLanguage
old_set = """  try {
    localStorage.setItem('bhakti_app_language', langCode);
  } catch(e) {}"""

new_set = """  try {
    localStorage.setItem('user_app_language', langCode);
    localStorage.setItem('bhakti_app_language', langCode);
  } catch(e) {}"""

if old_set in js:
    js = js.replace(old_set, new_set)

# Append window.i18n object definition
i18n_obj_def = """
// ══════════════════════════════════════════════════════════════════════════════
// 🌐 STANDARD i18n INTERFACE CONTRACT
// ══════════════════════════════════════════════════════════════════════════════

window.i18n = {
  changeLanguage: function(lang) {
    return window.setAppLanguage(lang);
  },
  t: function(key, defaultVal) {
    return window.t(key, defaultVal);
  },
  get language() {
    return window.currentAppLanguage || localStorage.getItem('user_app_language') || localStorage.getItem('bhakti_app_language') || 'hi';
  },
  set language(val) {
    window.setAppLanguage(val);
  },
  languages: ['hi', 'en', 'sa', 'gu', 'mr', 'bn', 'ta', 'te', 'kn'],
  locales: window.i18nLocales
};

// Aliases
window.changeLanguage = function(lang) {
  return window.i18n.changeLanguage(lang);
};
"""

if 'window.i18n =' not in js:
    js += '\n' + i18n_obj_def

with open('i18n_engine.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Updated i18n_engine.js with standard window.i18n contract!")
