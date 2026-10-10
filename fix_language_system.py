import sys, re, shutil, time
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 70)
print("🌐 LANGUAGE SYSTEM FIX — Adding All Missing Language Functions")
print("=" * 70)

ts = int(time.time())
shutil.copy('app.js', f'app.js.bak_lang_{ts}')
print(f"✅ Backup: app.js.bak_lang_{ts}")

# The complete Language System JS to inject into app.js
LANGUAGE_SYSTEM_JS = """

// ══════════════════════════════════════════════════════════════════════════════
// 🌐 COMPLETE LANGUAGE SELECTOR SYSTEM
// Functions: openLanguageSelectorModal, closeLanguageSelectorModal,
//            chooseTempLanguage, applySelectedLanguage
// ══════════════════════════════════════════════════════════════════════════════

window._tempSelectedLang = null;

// Open the language selector modal
window.openLanguageSelectorModal = function() {
  const modal = document.getElementById('language-selector-modal');
  if (!modal) return;
  modal.style.display = 'flex';

  // Pre-select current language
  const savedLang = localStorage.getItem('bhakti_app_language') || 'hi';
  window._tempSelectedLang = savedLang;
  _updateLangCardUI(savedLang);
};

// Close the language selector modal
window.closeLanguageSelectorModal = function() {
  const modal = document.getElementById('language-selector-modal');
  if (modal) {
    modal.style.display = 'none';
  }
  window._tempSelectedLang = null;
};

// Temp select a language (highlights the card, stores selection)
window.chooseTempLanguage = function(langCode) {
  window._tempSelectedLang = langCode;
  _updateLangCardUI(langCode);
  // Haptic feedback
  if (navigator.vibrate) navigator.vibrate(18);
};

// Update visual selection state of all lang cards
function _updateLangCardUI(selectedCode) {
  const cards = document.querySelectorAll('.lang-select-card');
  cards.forEach(function(card) {
    const lang = card.getAttribute('data-lang');
    const dot = card.querySelector('.lang-radio-dot');
    if (lang === selectedCode) {
      // Active card style
      card.style.background = 'linear-gradient(135deg, rgba(248,200,59,0.25) 0%, rgba(217,119,6,0.15) 100%)';
      card.style.border = '1.8px solid #F8C83B';
      card.style.boxShadow = '0 4px 16px rgba(248,200,59,0.35)';
      if (dot) {
        dot.style.background = '#F8C83B';
        dot.style.border = '2px solid #FEF3C7';
        dot.style.color = '#1A0B2E';
        dot.innerHTML = '✓';
      }
    } else {
      // Inactive card style
      card.style.background = 'rgba(255,255,255,0.06)';
      card.style.border = '1.5px solid rgba(255,255,255,0.15)';
      card.style.boxShadow = 'none';
      if (dot) {
        dot.style.background = 'transparent';
        dot.style.border = '1.5px solid rgba(255,255,255,0.4)';
        dot.style.color = 'transparent';
        dot.innerHTML = '';
      }
    }
  });
}

// Apply the selected language and close modal
window.applySelectedLanguage = function() {
  const langCode = window._tempSelectedLang;
  if (!langCode) {
    if (typeof showToast === 'function') {
      showToast('⚠️ कृपया पहले एक भाषा चुनें');
    }
    return;
  }

  // Apply language translation
  if (typeof changeAppLanguage === 'function') {
    changeAppLanguage(langCode);
  } else {
    // Fallback: just save
    localStorage.setItem('bhakti_app_language', langCode);
  }

  // Update the settings label
  const langNames = {
    'hi': '🟢 हिंदी (Hindi)',
    'en': '🟢 English',
    'sa': '🟢 संस्कृतम् (Sanskrit)',
    'gu': '🟢 ગુજરાતી (Gujarati)',
    'mr': '🟢 मराठी (Marathi)',
    'bn': '🟢 বাংলা (Bengali)',
    'ta': '🟢 தமிழ் (Tamil)',
    'te': '🟢 తెలుగు (Telugu)',
    'kn': '🟢 ಕನ್ನಡ (Kannada)',
    'pa': '🟢 ਪੰਜਾਬੀ (Punjabi)',
    'or': '🟢 ଓଡ଼ିଆ (Odia)',
    'ml': '🟢 മലയാളം (Malayalam)',
    'ur': '🟢 اردو (Urdu)'
  };
  const settingsLangLabel = document.getElementById('settings-current-lang-label');
  if (settingsLangLabel) {
    settingsLangLabel.textContent = langNames[langCode] || ('🟢 ' + langCode.toUpperCase());
  }

  // Close modal
  window.closeLanguageSelectorModal();

  // Haptic + toast
  if (navigator.vibrate) navigator.vibrate([30, 20, 30]);
  if (typeof showToast === 'function') {
    const names = {
      'hi': 'हिंदी', 'en': 'English', 'sa': 'संस्कृतम्',
      'gu': 'ગુજરાતી', 'mr': 'मराठी', 'bn': 'বাংলা',
      'ta': 'தமிழ்', 'te': 'తెలుగు', 'kn': 'ಕನ್ನಡ',
      'pa': 'ਪੰਜਾਬੀ', 'or': 'ଓଡ଼ିଆ', 'ml': 'മലയാളം', 'ur': 'اردو'
    };
    showToast('🌐 भाषा बदली: ' + (names[langCode] || langCode.toUpperCase()));
  }

  window._tempSelectedLang = null;
};

// Auto-restore saved language on page load
(function _restoreLanguageOnLoad() {
  const savedLang = localStorage.getItem('bhakti_app_language');
  if (savedLang && savedLang !== 'hi') {
    // Delay slightly to allow DOM to fully load
    setTimeout(function() {
      if (typeof changeAppLanguage === 'function') {
        changeAppLanguage(savedLang);
      }
    }, 500);
  }
})();

// Close language modal when clicking on overlay background
document.addEventListener('DOMContentLoaded', function() {
  const modal = document.getElementById('language-selector-modal');
  if (modal) {
    modal.addEventListener('click', function(e) {
      if (e.target === modal) {
        window.closeLanguageSelectorModal();
      }
    });
  }
});

"""

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Check if already exists
if 'COMPLETE LANGUAGE SELECTOR SYSTEM' in js:
    print("⚠️  Language system already exists — replacing...")
    start = js.find('// ══════════════════════════════════════════════════════════════════════════════\n// 🌐 COMPLETE LANGUAGE SELECTOR SYSTEM')
    end = js.find('\n\n\n', start + 100)
    if end == -1:
        end = len(js)
    js = js[:start] + LANGUAGE_SYSTEM_JS + js[end:]
    print("✅ Replaced existing language system")
else:
    # Append at end of file
    js = js + "\n" + LANGUAGE_SYSTEM_JS
    print("✅ Appended new language system to app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f"\n✅ app.js updated — total size: {len(js)} chars")

# Verify
with open('app.js', 'r', encoding='utf-8') as f:
    js_verify = f.read()

for fn in ['openLanguageSelectorModal', 'closeLanguageSelectorModal', 'chooseTempLanguage', 'applySelectedLanguage']:
    found = fn in js_verify
    print(f"  {'✅' if found else '❌'} {fn}: {'FOUND' if found else 'MISSING'}")

print("\n✅ LANGUAGE SYSTEM FIXED!")
print("=" * 70)
