import os, json, re, time, sys

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🌐 INTEGRATING COMPLETE DYNAMIC i18n ENGINE & LANGUAGE SELECTOR MODAL")
print("======================================================================")

# 1. Read all locale dictionaries to bundle inside i18n_engine.js
locales_dict = {}
for lang in ['hi', 'en', 'sa', 'gu', 'mr', 'bn', 'ta', 'te', 'kn']:
    with open(f'locales/{lang}.json', 'r', encoding='utf-8') as f:
        locales_dict[lang] = json.load(f)

# 2. Create i18n_engine.js
i18n_js_content = f"""// ══════════════════════════════════════════════════════════════════════════════
// 🌐 BHAKTI APP PRODUCTION i18n (LOCALIZATION) ENGINE
// Brand Name Lock: "Bhakti Me Leen" in Latin | "भक्ति में लीन" in Devanagari
// ══════════════════════════════════════════════════════════════════════════════

window.i18nLocales = {json.dumps(locales_dict, ensure_ascii=False, indent=2)};

window.currentAppLanguage = localStorage.getItem('bhakti_app_language') || 'hi';
window.selectedLanguageTemp = window.currentAppLanguage;

// Get nested translation value by key path, e.g. "home.visitsToday"
window.t = function(keyPath, defaultText) {{
  const lang = window.currentAppLanguage || 'hi';
  const dict = window.i18nLocales[lang] || window.i18nLocales['hi'];
  
  if (!keyPath) return defaultText || '';
  
  const parts = keyPath.split('.');
  let curr = dict;
  for (let i = 0; i < parts.length; i++) {{
    if (curr && typeof curr === 'object' && parts[i] in curr) {{
      curr = curr[parts[i]];
    }} else {{
      curr = null;
      break;
    }}
  }}
  
  if (curr !== null && curr !== undefined && typeof curr === 'string') {{
    return curr;
  }}
  
  // Fallback to Hindi if not found in target language
  if (lang !== 'hi' && window.i18nLocales['hi']) {{
    let hiCurr = window.i18nLocales['hi'];
    for (let i = 0; i < parts.length; i++) {{
      if (hiCurr && typeof hiCurr === 'object' && parts[i] in hiCurr) {{
        hiCurr = hiCurr[parts[i]];
      }} else {{
        hiCurr = null;
        break;
      }}
    }}
    if (hiCurr && typeof hiCurr === 'string') return hiCurr;
  }}
  
  return defaultText || keyPath;
}};

// Set and apply language across the entire application instantly
window.setAppLanguage = function(langCode, suppressToast) {{
  if (!window.i18nLocales[langCode]) {{
    console.warn(`Language ${{langCode}} not found, defaulting to 'hi'`);
    langCode = 'hi';
  }}
  
  window.currentAppLanguage = langCode;
  window.selectedLanguageTemp = langCode;
  try {{
    localStorage.setItem('bhakti_app_language', langCode);
  }} catch(e) {{}}
  
  const dict = window.i18nLocales[langCode];
  
  // 1. Translate all [data-i18n] elements
  document.querySelectorAll('[data-i18n]').forEach(el => {{
    const key = el.getAttribute('data-i18n');
    const translated = window.t(key);
    if (translated) {{
      el.textContent = translated;
    }}
  }});
  
  // 2. Translate all [data-i18n-placeholder] elements
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {{
    const key = el.getAttribute('data-i18n-placeholder');
    const translated = window.t(key);
    if (translated) {{
      el.placeholder = translated;
    }}
  }});
  
  // 3. Enforce Brand Name Lock across App Header, Splash, and Drawers
  const brandName = dict.appName || (langCode === 'en' ? 'Bhakti Me Leen' : 'भक्ति में लीन');
  
  document.querySelectorAll('.header-title, .splash-title, #auth-modal h2, .drawer-header h3').forEach(el => {{
    if (el) el.textContent = brandName;
  }});
  
  // 4. Translate Bottom Navigation Bar
  const navHome = document.querySelector('[data-page="page-home"] .nav-label, [data-page="page-home"] span:not(.nav-icon)');
  if (navHome) navHome.textContent = dict.nav.home;
  
  const navPanchang = document.querySelector('[data-page="page-panchang"] .nav-label, [data-page="page-panchang"] span:not(.nav-icon)');
  if (navPanchang) navPanchang.textContent = dict.nav.panchang;
  
  const navJar = document.querySelector('[data-page="page-jar"] .nav-label, [data-page="page-jar"] span:not(.nav-icon)');
  if (navJar) navJar.textContent = dict.nav.jar;
  
  const navKatha = document.querySelector('[data-page="page-katha"] .nav-label, [data-page="page-katha"] span:not(.nav-icon)');
  if (navKatha) navKatha.textContent = dict.nav.katha;
  
  const navProfile = document.querySelector('[data-page="page-profile"] .nav-label, [data-page="page-profile"] span:not(.nav-icon)');
  if (navProfile) navProfile.textContent = dict.nav.profile;
  
  // 5. Translate Category Cards on Home Page
  const catNames = {{
    'page-aarti': dict.categories.aarti,
    'page-chalisa': dict.categories.chalisa,
    'page-mantra': dict.categories.mantra,
    'page-stotra': dict.categories.stotra,
    'page-vrats': dict.categories.vrat,
    'page-top10': dict.categories.festival,
    'page-ramayana': dict.categories.ramayana,
    'page-katha': dict.categories.katha,
    'page-desh': dict.categories.desh,
    'page-panchang': dict.categories.panchang
  }};
  
  document.querySelectorAll('.cat-card').forEach(card => {{
    const pId = card.getAttribute('data-page');
    const nameEl = card.querySelector('.cat-name');
    if (nameEl && catNames[pId]) {{
      nameEl.textContent = catNames[pId];
    }}
  }});
  
  // 6. Update Settings Language Label
  const langLabelEl = document.getElementById('settings-current-lang-label');
  if (langLabelEl) {{
    const langNames = {{
      hi: '🟢 हिंदी (Hindi)',
      en: '🌐 English',
      sa: '🔱 संस्कृतम् (Sanskrit)',
      gu: '🪷 ગુજરાતી (Gujarati)',
      mr: '🚩 मराठी (Marathi)',
      bn: '🌸 বাংলা (Bengali)',
      ta: '🪔 தமிழ் (Tamil)',
      te: '☀️ తెలుగు (Telugu)',
      kn: '🌿 ಕನ್ನಡ (Kannada)'
    }};
    langLabelEl.textContent = langNames[langCode] || langCode.toUpperCase();
  }}
  
  // 7. Update Language Selector Radio Cards active state
  document.querySelectorAll('.lang-select-card').forEach(card => {{
    const cLang = card.getAttribute('data-lang');
    if (cLang === langCode) {{
      card.classList.add('selected');
      card.style.borderColor = '#F8C83B';
      card.style.background = 'linear-gradient(135deg, rgba(248,200,59,0.2) 0%, rgba(217,119,6,0.12) 100%)';
      const radio = card.querySelector('.lang-radio-dot');
      if (radio) {{
        radio.style.background = '#F8C83B';
        radio.innerHTML = '✓';
      }}
    }} else {{
      card.classList.remove('selected');
      card.style.borderColor = 'rgba(255,255,255,0.15)';
      card.style.background = 'rgba(255,255,255,0.06)';
      const radio = card.querySelector('.lang-radio-dot');
      if (radio) {{
        radio.style.background = 'transparent';
        radio.innerHTML = '';
      }}
    }}
  }});

  if (!suppressToast && typeof showToast === 'function') {{
    const msgs = {{
      hi: '🌐 ऐप भाषा हिंदी में सेट की गई!',
      en: '🌐 App language set to English!',
      sa: '🌐 संस्कृतभाषा प्रयुक्ता!',
      gu: '🌐 એપ ભાષા ગુજરાતી સેટ થઈ!',
      mr: '🌐 ॲप भाषा मराठी सेट झाली!',
      bn: '🌐 অ্যাপের ভাষা বাংলায় সেট করা হয়েছে!',
      ta: '🌐 பயன்பாட்டு மொழி தமிழுக்கு மாற்றப்பட்டது!',
      te: '🌐 యాప్ భాష తెలుగుగా సెట్ చేయబడింది!',
      kn: '🌐 ಅಪ್ಲಿಕೇಶನ್ ಭಾಷೆ ಕನ್ನಡಕ್ಕೆ ಹೊಂದಿಸಲಾಗಿದೆ!'
    }};
    showToast(msgs[langCode] || `🌐 Language: ${{langCode.toUpperCase()}}`);
  }}
}};

// Language Selector Modal Handlers
window.openLanguageSelectorModal = function() {{
  window.selectedLanguageTemp = window.currentAppLanguage;
  const modal = document.getElementById('language-selector-modal');
  if (modal) {{
    modal.style.display = 'flex';
  }}
  window.highlightSelectedLanguageCard(window.currentAppLanguage);
  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof playSoundEffect === 'function') playSoundEffect('click');
}};

window.closeLanguageSelectorModal = function() {{
  const modal = document.getElementById('language-selector-modal');
  if (modal) {{
    modal.style.display = 'none';
  }}
}};

window.chooseTempLanguage = function(langCode) {{
  window.selectedLanguageTemp = langCode;
  window.highlightSelectedLanguageCard(langCode);
  if (navigator.vibrate) navigator.vibrate(25);
  if (typeof playSoundEffect === 'function') playSoundEffect('click');
}};

window.highlightSelectedLanguageCard = function(langCode) {{
  document.querySelectorAll('.lang-select-card').forEach(card => {{
    const cLang = card.getAttribute('data-lang');
    const radio = card.querySelector('.lang-radio-dot');
    if (cLang === langCode) {{
      card.classList.add('selected');
      card.style.borderColor = '#F8C83B';
      card.style.background = 'linear-gradient(135deg, rgba(248,200,59,0.2) 0%, rgba(217,119,6,0.12) 100%)';
      card.style.boxShadow = '0 0 15px rgba(248,200,59,0.3)';
      if (radio) {{
        radio.style.background = '#F8C83B';
        radio.style.borderColor = '#FEF3C7';
        radio.innerHTML = '✓';
      }}
    }} else {{
      card.classList.remove('selected');
      card.style.borderColor = 'rgba(255,255,255,0.15)';
      card.style.background = 'rgba(255,255,255,0.06)';
      card.style.boxShadow = 'none';
      if (radio) {{
        radio.style.background = 'transparent';
        radio.style.borderColor = 'rgba(255,255,255,0.4)';
        radio.innerHTML = '';
      }}
    }}
  }});
}};

window.applySelectedLanguage = function() {{
  const targetLang = window.selectedLanguageTemp || window.currentAppLanguage || 'hi';
  window.setAppLanguage(targetLang);
  window.closeLanguageSelectorModal();
  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (typeof playSoundEffect === 'function') playSoundEffect('victory');
}};

// Auto-initialize language on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {{
  const savedLang = localStorage.getItem('bhakti_app_language') || 'hi';
  window.setAppLanguage(savedLang, true);
}});
"""

with open('i18n_engine.js', 'w', encoding='utf-8') as f:
    f.write(i18n_js_content)

print("✓ Created i18n_engine.js with all 9 bundled languages!")


# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add script tag in index.html if not present
ts = int(time.time())
script_tag = f'  <script src="i18n_engine.js?v={ts}"></script>'

if 'i18n_engine.js' not in html:
    html = html.replace('  <script src="sadhana_gamification_engine.js', script_tag + '\n  <script src="sadhana_gamification_engine.js')
    print("✓ Added i18n_engine.js script tag to index.html")

# Add Language Selector Row inside #page-settings right after Profile Card
language_setting_row = """
        <!-- 🌐 MULTI-LANGUAGE (i18n) SELECTION ROW 🌐 -->
        <div style="background:rgba(255,255,255,0.05); border:1.3px solid rgba(248,200,59,0.3); border-radius:22px; padding:1.2rem; margin-bottom:1.2rem; box-shadow:0 8px 25px rgba(0,0,0,0.4);">
          <div style="display:flex; align-items:center; justify-content:space-between;">
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:1.4rem;">🌐</span>
              <div>
                <div style="font-size:0.95rem; font-weight:900; color:#FFFDF8;">भाषा चयन (App Language)</div>
                <div id="settings-current-lang-label" style="font-size:0.75rem; color:#FDE68A; font-weight:700; margin-top:2px;">
                  🟢 हिंदी (Hindi)
                </div>
              </div>
            </div>
            <button onclick="openLanguageSelectorModal()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-size:0.8rem; font-weight:900; padding:7px 14px; border-radius:12px; cursor:pointer; box-shadow:0 3px 12px rgba(248,200,59,0.35); display:flex; align-items:center; gap:4px;">
              <span>🌐</span> भाषा बदलें ❯
            </button>
          </div>
        </div>
"""

target_profile_card = """              <span id="settings-user-streak">🔥 21 दिन नित्य साधना स्ट्रीक</span>
              <span>•</span>
              <span id="settings-user-points">⭐ 1,475 साधना अंक</span>
            </div>
          </div>
        </div>"""

if target_profile_card in html and 'id="settings-current-lang-label"' not in html:
    html = html.replace(target_profile_card, target_profile_card + '\n' + language_setting_row, 1)
    print("✓ Added Language Selection Card into #page-settings in index.html")

# Add Language Selector Modal (#language-selector-modal)
language_modal_html = """
  <!-- ═══════════════════════════════════════════════════════════════════════════
       🌐 MULTI-LANGUAGE (i18n) SELECTION MODAL 🌐
       ═══════════════════════════════════════════════════════════════════════════ -->
  <div id="language-selector-modal" style="display:none; position:fixed; inset:0; z-index:100190; background:rgba(7,1,16,0.95); backdrop-filter:blur(25px); -webkit-backdrop-filter:blur(25px); align-items:center; justify-content:center; padding:1.2rem; overflow-y:auto;">
    <div style="width:100%; max-width:420px; background:linear-gradient(165deg, #2D1047 0%, #1A052E 50%, #0D0218 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.4rem 1.3rem; text-align:left; box-shadow:0 25px 80px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease; max-height:92vh; overflow-y:auto;">
      
      <!-- Top Bar -->
      <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; border-bottom:1px solid rgba(248,200,59,0.25); padding-bottom:10px;">
        <div>
          <h3 style="font-size:1.15rem; font-weight:900; color:#FFFDF8; margin:0; display:flex; align-items:center; gap:6px;">
            <span>🌐</span> भाषा चयन (Select Language)
          </h3>
          <div style="font-size:0.72rem; color:#CBD5E1; margin-top:2px;">अपनी पसंदीदा भाषा चुनें / Choose Preferred Language</div>
        </div>
        <button onclick="closeLanguageSelectorModal()" style="background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:32px; height:32px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>
      </div>

      <!-- POPULAR LANGUAGES SECTION -->
      <div style="margin-bottom:12px;">
        <div style="font-size:0.75rem; font-weight:900; color:#FDE68A; margin-bottom:8px;">🌟 प्रमुख भाषाएं (Popular Languages)</div>
        
        <!-- 1. Hindi -->
        <div onclick="chooseTempLanguage('hi')" class="lang-select-card" data-lang="hi" style="background:linear-gradient(135deg, rgba(248,200,59,0.2) 0%, rgba(217,119,6,0.12) 100%); border:1.8px solid #F8C83B; border-radius:16px; padding:10px 14px; margin-bottom:8px; display:flex; align-items:center; justify-content:space-between; cursor:pointer; transition:all 0.2s ease;">
          <div style="display:flex; align-items:center; gap:10px;">
            <span style="font-size:1.4rem;">🕉️</span>
            <div>
              <div style="color:#FFFDF8; font-size:0.92rem; font-weight:900;">हिंदी (Hindi)</div>
              <div style="color:#CBD5E1; font-size:0.68rem;">मूल भाषा • सनातन धर्म</div>
            </div>
          </div>
          <div class="lang-radio-dot" style="width:22px; height:22px; border-radius:50%; border:2px solid #FEF3C7; background:#F8C83B; display:flex; align-items:center; justify-content:center; color:#1A0B2E; font-size:0.75rem; font-weight:900;">✓</div>
        </div>

        <!-- 2. English -->
        <div onclick="chooseTempLanguage('en')" class="lang-select-card" data-lang="en" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); border-radius:16px; padding:10px 14px; margin-bottom:8px; display:flex; align-items:center; justify-content:space-between; cursor:pointer; transition:all 0.2s ease;">
          <div style="display:flex; align-items:center; gap:10px;">
            <span style="font-size:1.4rem;">🌐</span>
            <div>
              <div style="color:#FFFDF8; font-size:0.92rem; font-weight:900;">English</div>
              <div style="color:#CBD5E1; font-size:0.68rem;">Global Devotional Access</div>
            </div>
          </div>
          <div class="lang-radio-dot" style="width:22px; height:22px; border-radius:50%; border:2px solid rgba(255,255,255,0.4); background:transparent; display:flex; align-items:center; justify-content:center; color:#1A0B2E; font-size:0.75rem; font-weight:900;"></div>
        </div>

        <!-- 3. Sanskrit -->
        <div onclick="chooseTempLanguage('sa')" class="lang-select-card" data-lang="sa" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); border-radius:16px; padding:10px 14px; margin-bottom:8px; display:flex; align-items:center; justify-content:space-between; cursor:pointer; transition:all 0.2s ease;">
          <div style="display:flex; align-items:center; gap:10px;">
            <span style="font-size:1.4rem;">🔱</span>
            <div>
              <div style="color:#FFFDF8; font-size:0.92rem; font-weight:900;">संस्कृतम् (Sanskrit)</div>
              <div style="color:#CBD5E1; font-size:0.68rem;">देववाणी • वैदिक रूप</div>
            </div>
          </div>
          <div class="lang-radio-dot" style="width:22px; height:22px; border-radius:50%; border:2px solid rgba(255,255,255,0.4); background:transparent; display:flex; align-items:center; justify-content:center; color:#1A0B2E; font-size:0.75rem; font-weight:900;"></div>
        </div>
      </div>

      <!-- REGIONAL INDIAN LANGUAGES GRID -->
      <div style="margin-bottom:16px;">
        <div style="font-size:0.75rem; font-weight:900; color:#FDE68A; margin-bottom:8px;">🇮🇳 भारतीय प्रांतीय भाषाएं (Regional Languages)</div>
        
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
          
          <!-- Gujarati -->
          <div onclick="chooseTempLanguage('gu')" class="lang-select-card" data-lang="gu" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); border-radius:14px; padding:8px 10px; cursor:pointer; display:flex; align-items:center; justify-content:space-between;">
            <div>
              <div style="color:#FFFDF8; font-size:0.85rem; font-weight:900;">ગુજરાતી</div>
              <div style="color:#CBD5E1; font-size:0.65rem;">Gujarati</div>
            </div>
            <div class="lang-radio-dot" style="width:18px; height:18px; border-radius:50%; border:1.5px solid rgba(255,255,255,0.4); display:flex; align-items:center; justify-content:center; font-size:0.65rem;"></div>
          </div>

          <!-- Marathi -->
          <div onclick="chooseTempLanguage('mr')" class="lang-select-card" data-lang="mr" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); border-radius:14px; padding:8px 10px; cursor:pointer; display:flex; align-items:center; justify-content:space-between;">
            <div>
              <div style="color:#FFFDF8; font-size:0.85rem; font-weight:900;">मराठी</div>
              <div style="color:#CBD5E1; font-size:0.65rem;">Marathi</div>
            </div>
            <div class="lang-radio-dot" style="width:18px; height:18px; border-radius:50%; border:1.5px solid rgba(255,255,255,0.4); display:flex; align-items:center; justify-content:center; font-size:0.65rem;"></div>
          </div>

          <!-- Bengali -->
          <div onclick="chooseTempLanguage('bn')" class="lang-select-card" data-lang="bn" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); border-radius:14px; padding:8px 10px; cursor:pointer; display:flex; align-items:center; justify-content:space-between;">
            <div>
              <div style="color:#FFFDF8; font-size:0.85rem; font-weight:900;">বাংলা</div>
              <div style="color:#CBD5E1; font-size:0.65rem;">Bengali</div>
            </div>
            <div class="lang-radio-dot" style="width:18px; height:18px; border-radius:50%; border:1.5px solid rgba(255,255,255,0.4); display:flex; align-items:center; justify-content:center; font-size:0.65rem;"></div>
          </div>

          <!-- Tamil -->
          <div onclick="chooseTempLanguage('ta')" class="lang-select-card" data-lang="ta" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); border-radius:14px; padding:8px 10px; cursor:pointer; display:flex; align-items:center; justify-content:space-between;">
            <div>
              <div style="color:#FFFDF8; font-size:0.85rem; font-weight:900;">தமிழ்</div>
              <div style="color:#CBD5E1; font-size:0.65rem;">Tamil</div>
            </div>
            <div class="lang-radio-dot" style="width:18px; height:18px; border-radius:50%; border:1.5px solid rgba(255,255,255,0.4); display:flex; align-items:center; justify-content:center; font-size:0.65rem;"></div>
          </div>

          <!-- Telugu -->
          <div onclick="chooseTempLanguage('te')" class="lang-select-card" data-lang="te" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); border-radius:14px; padding:8px 10px; cursor:pointer; display:flex; align-items:center; justify-content:space-between;">
            <div>
              <div style="color:#FFFDF8; font-size:0.85rem; font-weight:900;">తెలుగు</div>
              <div style="color:#CBD5E1; font-size:0.65rem;">Telugu</div>
            </div>
            <div class="lang-radio-dot" style="width:18px; height:18px; border-radius:50%; border:1.5px solid rgba(255,255,255,0.4); display:flex; align-items:center; justify-content:center; font-size:0.65rem;"></div>
          </div>

          <!-- Kannada -->
          <div onclick="chooseTempLanguage('kn')" class="lang-select-card" data-lang="kn" style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.15); border-radius:14px; padding:8px 10px; cursor:pointer; display:flex; align-items:center; justify-content:space-between;">
            <div>
              <div style="color:#FFFDF8; font-size:0.85rem; font-weight:900;">ಕನ್ನಡ</div>
              <div style="color:#CBD5E1; font-size:0.65rem;">Kannada</div>
            </div>
            <div class="lang-radio-dot" style="width:18px; height:18px; border-radius:50%; border:1.5px solid rgba(255,255,255,0.4); display:flex; align-items:center; justify-content:center; font-size:0.65rem;"></div>
          </div>

        </div>
      </div>

      <!-- Action Button: Apply Language -->
      <button onclick="applySelectedLanguage()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.95rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 18px rgba(248,200,59,0.45); display:flex; align-items:center; justify-content:center; gap:6px;">
        <span>🚩</span> भाषा लागू करें (Apply Language) ➔
      </button>

    </div>
  </div>
"""

if 'id="language-selector-modal"' not in html:
    html = html.replace('<!-- ═══════════════════════════════════════════════════════════════════════════\n       🏆 VEDIC RANKS & BADGES MODAL', language_modal_html + '\n\n  <!-- ═══════════════════════════════════════════════════════════════════════════\n       🏆 VEDIC RANKS & BADGES MODAL')
    print("✓ Inserted #language-selector-modal into index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ index.html saved!")
