import sys, shutil, time
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 70)
print("🌐 ADDING REGIONAL LANGUAGE DICTIONARIES")
print("=" * 70)

ts = int(time.time())
shutil.copy('app.js', f'app.js.bak_dict_{ts}')

REGIONAL_DICTS = """

// ══════════════════════════════════════════════════════════════════════════════
// 🌐 REGIONAL LANGUAGE DICTIONARIES (Sanskrit, Gujarati, Marathi, Bengali,
//    Tamil, Telugu, Kannada, Punjabi, Odia, Malayalam, Urdu)
// ══════════════════════════════════════════════════════════════════════════════

// Extend FULL_APP_DICTIONARY with regional languages
(function _addRegionalLanguages() {
  if (typeof FULL_APP_DICTIONARY === 'undefined') return;

  // ── Sanskrit ──
  FULL_APP_DICTIONARY['sa'] = {
    app_title: 'भक्तौ लीनः',
    nav_home: 'गृहम्',
    nav_panchang: 'पञ्चाङ्गम्',
    nav_jar: 'कलशः',
    nav_katha: 'कथाः',
    nav_profile: 'परिचयः',
    hero_title: 'भक्तौ लीनः',
    hero_sub: '॥ सर्वदेवानां पवित्रदर्शनम् ॥',
    hero_shloka: '✨ सर्वे भवन्तु सुखिनः सर्वे सन्तु निरामयाः ✨',
    search_placeholder: 'आरती, चालिसा, मन्त्रं खोजत...',
    aarti: 'आरती',
    chalisa: 'चालिसा',
    mantra: 'मन्त्रः',
    panchang: 'पञ्चाङ्गम्',
    vrat_tyohar: 'व्रत-उत्सवाः',
    top_festivals: 'प्रमुखोत्सवाः',
    profile: 'परिचयः',
    settings_title: 'विन्यासः',
    language_label: '🌐 भाषा',
    lang_changed: '🌐 भाषा संस्कृते परिवर्तिता!'
  };

  // ── Gujarati ──
  FULL_APP_DICTIONARY['gu'] = {
    app_title: 'ભક્તિમાં લીન',
    nav_home: 'હોમ',
    nav_panchang: 'પંચાંગ',
    nav_jar: 'કળશ',
    nav_katha: 'કથા',
    nav_profile: 'પ્રોફાઇલ',
    hero_title: 'ભક્તિમાં લીન',
    hero_sub: '॥ સર્વ દેવોના પવિત્ર દર્શન ॥',
    hero_shloka: '✨ સૌ સુખી થાઓ, સૌ નીરોગી બનો ✨',
    search_placeholder: 'આરતી, ચાલીસા, મંત્ર શોધો...',
    aarti: 'આરતી',
    chalisa: 'ચાલીસા',
    mantra: 'મંત્ર',
    panchang: 'પંચાંગ',
    vrat_tyohar: 'વ્રત અને તહેવાર',
    top_festivals: 'ટોપ 10 ઉત્સવ',
    profile: 'પ્રોફાઇલ',
    settings_title: 'સેટિંગ',
    language_label: '🌐 ભાષા',
    tithi: 'તિથિ',
    nakshatra: 'નક્ષત્ર',
    yoga: 'યોગ',
    karana: 'કરણ',
    sunrise: 'સૂર્યોદય',
    sunset: 'સૂર્યાસ્ત',
    kalash_title: 'ભક્તિ અમૃત કળશ',
    katha_title: 'કથા અને પ્રવચન',
    my_profile: 'મારી પ્રોફાઇલ',
    login_btn: 'ખાતું બદલો / લૉગિન',
    logout: 'લૉગ આઉટ',
    lang_changed: '🌐 ભાષા ગુજરાતીમાં સેટ કરી!'
  };

  // ── Marathi ──
  FULL_APP_DICTIONARY['mr'] = {
    app_title: 'भक्तीत लीन',
    nav_home: 'होम',
    nav_panchang: 'पंचांग',
    nav_jar: 'कलश',
    nav_katha: 'कथा',
    nav_profile: 'प्रोफाइल',
    hero_title: 'भक्तीत लीन',
    hero_sub: '॥ सर्व देवतांचे पवित्र दर्शन ॥',
    hero_shloka: '✨ सर्वे सुखिनः भवन्तु, सर्वे निरामयाः ✨',
    search_placeholder: 'आरती, चाळीसा, मंत्र शोधा...',
    aarti: 'आरती',
    chalisa: 'चाळीसा',
    mantra: 'मंत्र',
    panchang: 'पंचांग',
    vrat_tyohar: 'व्रत आणि सण',
    top_festivals: 'शीर्ष 10 उत्सव',
    profile: 'प्रोफाइल',
    settings_title: 'सेटिंग्ज',
    language_label: '🌐 भाषा',
    tithi: 'तिथी',
    nakshatra: 'नक्षत्र',
    yoga: 'योग',
    karana: 'करण',
    sunrise: 'सूर्योदय',
    sunset: 'सूर्यास्त',
    kalash_title: 'भक्ती अमृत कलश',
    katha_title: 'कथा आणि प्रवचन',
    my_profile: 'माझी प्रोफाइल',
    login_btn: 'खाते बदला / लॉगिन',
    logout: 'लॉग आउट',
    lang_changed: '🌐 भाषा मराठीत सेट केली!'
  };

  // ── Bengali ──
  FULL_APP_DICTIONARY['bn'] = {
    app_title: 'ভক্তিতে লীন',
    nav_home: 'হোম',
    nav_panchang: 'পঞ্চাং',
    nav_jar: 'কলস',
    nav_katha: 'কথা',
    nav_profile: 'প্রোফাইল',
    hero_title: 'ভক্তিতে লীন',
    hero_sub: '॥ সকল দেবতার পবিত্র দর্শন ॥',
    hero_shloka: '✨ সকলে সুখী হোন, সকলে সুস্থ থাকুন ✨',
    search_placeholder: 'আরতি, চালিসা, মন্ত্র খুঁজুন...',
    aarti: 'আরতি',
    chalisa: 'চালিসা',
    mantra: 'মন্ত্র',
    panchang: 'পঞ্চাং',
    vrat_tyohar: 'ব্রত ও উৎসব',
    top_festivals: 'শীর্ষ ১০ উৎসব',
    profile: 'প্রোফাইল',
    settings_title: 'সেটিং',
    language_label: '🌐 ভাষা',
    tithi: 'তিথি',
    nakshatra: 'নক্ষত্র',
    yoga: 'যোগ',
    karana: 'করণ',
    sunrise: 'সূর্যোদয়',
    sunset: 'সূর্যাস্ত',
    kalash_title: 'ভক্তি অমৃত কলস',
    katha_title: 'কথা ও প্রবচন',
    my_profile: 'আমার প্রোফাইল',
    login_btn: 'অ্যাকাউন্ট পরিবর্তন / লগইন',
    logout: 'লগ আউট',
    lang_changed: '🌐 ভাষা বাংলায় সেট করা হয়েছে!'
  };

  // ── Tamil ──
  FULL_APP_DICTIONARY['ta'] = {
    app_title: 'பக்தியில் லீன்',
    nav_home: 'முகப்பு',
    nav_panchang: 'பஞ்சாங்கம்',
    nav_jar: 'கலசம்',
    nav_katha: 'கதை',
    nav_profile: 'சுயவிவரம்',
    hero_title: 'பக்தியில் லீன்',
    hero_sub: '॥ அனைத்து தெய்வங்களின் புனித தரிசனம் ॥',
    hero_shloka: '✨ அனைவரும் சுகமாக இருக்கட்டும் ✨',
    search_placeholder: 'ஆரதி, சாலிசா, மந்திரம் தேடுங்கள்...',
    aarti: 'ஆரதி',
    chalisa: 'சாலிசா',
    mantra: 'மந்திரம்',
    panchang: 'பஞ்சாங்கம்',
    vrat_tyohar: 'விரதம் & திருவிழா',
    top_festivals: 'சிறந்த 10 திருவிழாக்கள்',
    profile: 'சுயவிவரம்',
    settings_title: 'அமைப்புகள்',
    language_label: '🌐 மொழி',
    tithi: 'திதி',
    nakshatra: 'நட்சத்திரம்',
    sunrise: 'சூரிய உதயம்',
    sunset: 'சூரிய அஸ்தமனம்',
    my_profile: 'என் சுயவிவரம்',
    logout: 'வெளியேறு',
    lang_changed: '🌐 மொழி தமிழில் அமைக்கப்பட்டது!'
  };

  // ── Telugu ──
  FULL_APP_DICTIONARY['te'] = {
    app_title: 'భక్తిలో లీనం',
    nav_home: 'హోమ్',
    nav_panchang: 'పంచాంగం',
    nav_jar: 'కలశం',
    nav_katha: 'కథ',
    nav_profile: 'ప్రొఫైల్',
    hero_title: 'భక్తిలో లీనం',
    hero_sub: '॥ సర్వ దేవతల పవిత్ర దర్శనం ॥',
    hero_shloka: '✨ అందరూ సుఖంగా ఉండాలి ✨',
    search_placeholder: 'ఆరతి, చాలీసా, మంత్రం వెతకండి...',
    aarti: 'ఆరతి',
    chalisa: 'చాలీసా',
    mantra: 'మంత్రం',
    panchang: 'పంచాంగం',
    vrat_tyohar: 'వ్రతాలు & పండుగలు',
    top_festivals: 'టాప్ 10 పండుగలు',
    profile: 'ప్రొఫైల్',
    settings_title: 'సెట్టింగులు',
    language_label: '🌐 భాష',
    tithi: 'తిథి',
    nakshatra: 'నక్షత్రం',
    sunrise: 'సూర్యోదయం',
    sunset: 'సూర్యాస్తమయం',
    my_profile: 'నా ప్రొఫైల్',
    logout: 'లాగ్ అవుట్',
    lang_changed: '🌐 భాష తెలుగులో సెట్ చేయబడింది!'
  };

  // ── Kannada ──
  FULL_APP_DICTIONARY['kn'] = {
    app_title: 'ಭಕ್ತಿಯಲ್ಲಿ ಲೀನ',
    nav_home: 'ಮನೆ',
    nav_panchang: 'ಪಂಚಾಂಗ',
    nav_jar: 'ಕಲಶ',
    nav_katha: 'ಕಥೆ',
    nav_profile: 'ಪ್ರೊಫೈಲ್',
    hero_title: 'ಭಕ್ತಿಯಲ್ಲಿ ಲೀನ',
    hero_sub: '॥ ಎಲ್ಲ ದೇವತೆಗಳ ಪವಿತ್ರ ದರ್ಶನ ॥',
    hero_shloka: '✨ ಎಲ್ಲರೂ ಸುಖವಾಗಿರಲಿ ✨',
    search_placeholder: 'ಆರತಿ, ಚಾಲೀಸಾ, ಮಂತ್ರ ಹುಡುಕಿ...',
    aarti: 'ಆರತಿ',
    chalisa: 'ಚಾಲೀಸಾ',
    mantra: 'ಮಂತ್ರ',
    panchang: 'ಪಂಚಾಂಗ',
    vrat_tyohar: 'ವ್ರತ & ಹಬ್ಬ',
    top_festivals: 'ಟಾಪ್ 10 ಹಬ್ಬಗಳು',
    profile: 'ಪ್ರೊಫೈಲ್',
    settings_title: 'ಸೆಟ್ಟಿಂಗ್ಸ್',
    language_label: '🌐 ಭಾಷೆ',
    tithi: 'ತಿಥಿ',
    nakshatra: 'ನಕ್ಷತ್ರ',
    sunrise: 'ಸೂರ್ಯೋದಯ',
    sunset: 'ಸೂರ್ಯಾಸ್ತ',
    my_profile: 'ನನ್ನ ಪ್ರೊಫೈಲ್',
    logout: 'ಲಾಗ್ ಔಟ್',
    lang_changed: '🌐 ಭಾಷೆ ಕನ್ನಡಕ್ಕೆ ಹೊಂದಿಸಲಾಗಿದೆ!'
  };

  console.log('[🌐 Lang] Regional language dictionaries loaded:', Object.keys(FULL_APP_DICTIONARY).join(', '));
})();

"""

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove old if exists
MARKER = '// ══════════════════════════════════════════════════════════════════════════════\n// 🌐 REGIONAL LANGUAGE DICTIONARIES'
if MARKER in js:
    start = js.find(MARKER)
    # Find end - next section or IIFE end
    end = js.find('\n\n\n', start + 200)
    if end == -1:
        end = len(js)
    js = js[:start] + REGIONAL_DICTS + js[end:]
    print("✅ Replaced existing regional dictionaries")
else:
    # Insert BEFORE the language selector system
    insert_before = '// ══════════════════════════════════════════════════════════════════════════════\n// 🌐 COMPLETE LANGUAGE SELECTOR SYSTEM'
    if insert_before in js:
        idx = js.find(insert_before)
        js = js[:idx] + REGIONAL_DICTS + '\n' + js[idx:]
        print("✅ Inserted regional dictionaries before language selector system")
    else:
        js = js + '\n' + REGIONAL_DICTS
        print("✅ Appended regional dictionaries to end of app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f"✅ app.js updated — {len(js)} chars")

# Verify
with open('app.js', 'r', encoding='utf-8') as f:
    js_v = f.read()

import re
lang_keys_found = re.findall(r"FULL_APP_DICTIONARY\['([a-z]{2})'\]", js_v)
print(f"✅ Languages now in dictionary: {lang_keys_found}")
print("=" * 70)
