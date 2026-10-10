import json, sys

sys.stdout.reconfigure(encoding='utf-8')

user_hi_payload = {
  "appName": "भक्ति में लीन",
  "tagline": "दिव्य साधना एवं आत्मिक शांति का मार्ग",
  "nav": {
    "home": "होम",
    "audio": "ऑडियो",
    "japMala": "जाप माला",
    "aarti": "आरती दर्शन",
    "panchang": "पंचांग",
    "settings": "सेटिंग्स"
  },
  "home": {
    "welcome": "स्वागत है",
    "guestLogin": "अतिथि प्रवेश",
    "dailyTracker": "दैनिक साधना संज्ञान",
    "visitsToday": "आज का पावन प्रवेश",
    "times": "बार",
    "streak": "दिन स्ट्रीक",
    "streakShield": "कवच",
    "liveRadio": "24×7 लाइव भक्ति रेडियो",
    "parikrama": "दिव्य परिक्रमा संकल्प",
    "amritKalash": "भक्ति अमृत कलश",
    "radioNowPlaying": "वर्तमान प्रसारण"
  },
  "settings": {
    "title": "साधना नियंत्रण एवं सेटिंग्स",
    "haptics": "दिव्य अनुभूति एवं हैप्टिक्स",
    "brahmaMuhurta": "ब्रह्म मुहूर्त जागरण अलार्म",
    "bioAura": "क्वांटम बायो-एनर्जी व ऑरा विज़ुअलाइज़र",
    "vault": "साधना वॉल्ट व क्लाउड सिंक",
    "language": "ऐप की भाषा"
  }
}

# 1. Update locales/hi.json and src/locales/hi.json
with open('locales/hi.json', 'r', encoding='utf-8') as f:
    cur = json.load(f)

# Merge keys
for k, v in user_hi_payload.items():
    if isinstance(v, dict) and k in cur and isinstance(cur[k], dict):
        cur[k].update(v)
    else:
        cur[k] = v

with open('locales/hi.json', 'w', encoding='utf-8') as f:
    json.dump(cur, f, ensure_ascii=False, indent=2)

with open('src/locales/hi.json', 'w', encoding='utf-8') as f:
    json.dump(cur, f, ensure_ascii=False, indent=2)

print("✓ Updated locales/hi.json and src/locales/hi.json with exact payload!")

# 2. Update i18n_engine.js with new bundled dictionaries
locales_dict = {}
for lang in ['hi', 'en', 'sa', 'gu', 'mr', 'bn', 'ta', 'te', 'kn']:
    with open(f'locales/{lang}.json', 'r', encoding='utf-8') as f:
        locales_dict[lang] = json.load(f)

with open('i18n_engine.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
pattern = r'window\.i18nLocales\s*=\s*\{[\s\S]*?\n\};'
replacement = "window.i18nLocales = " + json.dumps(locales_dict, ensure_ascii=False, indent=2) + ";"

js = re.sub(pattern, lambda m: replacement, js, count=1)

with open('i18n_engine.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Synced window.i18nLocales inside i18n_engine.js!")
