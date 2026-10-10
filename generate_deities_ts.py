import json
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\deities_saptavara_full.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Metadata mappings
meta = {
    "bhairava-ravivara": {
        "planetEn": "Sun (Surya Deva)",
        "planetHi": "सूर्य देव",
        "color": "Black, Dark Red / काला, गहरा लाल",
        "accentColor": "#b91c1c",
        "durationEn": "21, 31 or 51 Sundays",
        "durationHi": "21, 31 अथवा 51 रविवार",
        "mantra": "ॐ कालभैरवाय नमः। (Om Kalabhairavaya Namah।)",
        "benefitsEn": "Destroys fear of enemies, removes tantric obstacles, alleviates chronic diseases, pacifies Rahu, Ketu and Shani afflictions.",
        "benefitsHi": "शत्रु भय नाश, तंत्र-मंत्र व नकारात्मक ऊर्जा से रक्षा, असाध्य रोगों से मुक्ति, राहु-केतु व शनि ग्रहदोष निवारण।"
    },
    "shiva-somavara": {
        "planetEn": "Moon (Chandra Deva)",
        "planetHi": "चन्द्र देव",
        "color": "White / श्वेत",
        "accentColor": "#0284c7",
        "durationEn": "1 year, 14 years, or 16 Mondays (Solah Somvar)",
        "durationHi": "1 वर्ष, 14 वर्ष अथवा 16 सोमवार (सोलह सोमवार)",
        "mantra": "ॐ नमः शिवाय। / ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम्। उर्वारुकमिव बन्धनान्मृत्योर्मुक्षीय मामृतात्॥",
        "benefitsEn": "Marital harmony, suitable life partner, mental peace, health, longevity, and liberation.",
        "benefitsHi": "वैवाहिक कष्टों का निवारण, सुयोग्य जीवनसाथी, मानसिक शांति, आरोग्य, संतान सुख एवं अखंड सौभाग्य।"
    },
    "hanumana-mangalavara": {
        "planetEn": "Mars (Mangala Deva)",
        "planetHi": "मङ्गल देव",
        "color": "Red, Vermilion / लाल, सिंदूरी",
        "accentColor": "#ea580c",
        "durationEn": "21 or 45 Tuesdays",
        "durationHi": "21 अथवा 45 मङ्गलवार",
        "mantra": "ॐ हनुमते नमः। / ॐ हं हनुमते रुद्रात्मकाय हुं फट्॥",
        "benefitsEn": "Courage, strength, elimination of fear, ghosts, evil spirits, debt relief, and Mangal Dosha pacification.",
        "benefitsHi": "साहस व शक्ति की प्राप्ति, भय व भूत-पिशाच बाधा से मुक्ति, कर्ज मुक्ति, रक्त विकार व मंगल दोष निवारण।"
    },
    "murugan-mangalavara": {
        "planetEn": "Mars (Mangala Deva)",
        "planetHi": "मङ्गल देव (सेनापति)",
        "color": "Red, Yellow / लाल, पीला",
        "accentColor": "#d97706",
        "durationEn": "6, 9 or 21 Tuesdays (or Sashti Vrat)",
        "durationHi": "6, 9 अथवा 21 मङ्गलवार (अथवा षष्ठी व्रत)",
        "mantra": "ॐ शरवणभवाय नमः। (Om Sharavanabhavaya Namah।)",
        "benefitsEn": "Victory in legal/property disputes, wisdom, leadership, protection from enemies, and success in competitive exams.",
        "benefitsHi": "शत्रुओं पर विजय, वाद-विवाद व भूमि विवाद में सफलता, तीक्ष्ण बुद्धि, नेतृत्व क्षमता व मंगल दोष शान्ति।"
    },
    "ganesha-budhavara": {
        "planetEn": "Mercury (Budha Deva)",
        "planetHi": "बुध देव",
        "color": "Green / हरा",
        "accentColor": "#16a34a",
        "durationEn": "7, 21 or 45 Wednesdays",
        "durationHi": "7, 21 अथवा 45 बुधवार",
        "mantra": "ॐ गं गणपतये नमः। / ॐ वक्रतुण्डाय हुम्॥",
        "benefitsEn": "Removes all obstacles (Vighnaharta), enhances intellect, speech, business growth, and auspicious new beginnings.",
        "benefitsHi": "समस्त विघ्नों का नाश, बुद्धि, विद्या व वाणी में प्रखरता, व्यापार में उन्नति, बुध ग्रह दोष शान्ति।"
    },
    "vishnu-brihaspativara": {
        "planetEn": "Jupiter (Brihaspati Deva)",
        "planetHi": "बृहस्पति देव",
        "color": "Yellow / पीला",
        "accentColor": "#ca8a04",
        "durationEn": "16 Thursdays (Solah Brihaspativar)",
        "durationHi": "16 बृहस्पतिवार (सोलह बृहस्पतिवार)",
        "mantra": "ॐ नमो भगवते वासुदेवाय। / ॐ बृं बृहस्पतये नमः॥",
        "benefitsEn": "Happy married life, early marriage, child birth, wealth, spiritual wisdom, and career advancement.",
        "benefitsHi": "शीघ्र विवाह, सुखी दाम्पत्य, पुत्र व संतान प्राप्ति, धन-धान्य, ज्ञान व गुरु ग्रह की कृपा।"
    },
    "santoshi-mata-shukravara": {
        "planetEn": "Venus (Shukra Deva)",
        "planetHi": "शुक्र देव",
        "color": "Red, Pink / लाल, गुलाबी",
        "accentColor": "#e11d48",
        "durationEn": "16 Fridays (Solah Shukravar)",
        "durationHi": "16 शुक्रवार (सोलह शुक्रवार)",
        "mantra": "ॐ श्री सन्तोषी महालक्ष्म्यै नमः। / जय माता दी॥",
        "benefitsEn": "Mental peace, contentment, familial joy, wish fulfillment, and relief from distress. (Strict rule: No sour/citrus food).",
        "benefitsHi": "मनोकामना पूर्ति, परिवार में सुख-शांति, कलह मुक्ति, संतोष व समृद्धि। (विशेष नियम: खटाई का पूर्ण निषेध)।"
    },
    "vaibhava-lakshmi-shukravara": {
        "planetEn": "Venus (Shukra Deva)",
        "planetHi": "शुक्र देव",
        "color": "Golden, Red / स्वर्णिम, लाल",
        "accentColor": "#db2777",
        "durationEn": "11, 21 or 51 Fridays",
        "durationHi": "11, 21 अथवा 51 शुक्रवार",
        "mantra": "ॐ श्रीं ह्रीं क्लीं श्री सिद्ध लक्ष्म्यै नमः।",
        "benefitsEn": "Infinite wealth, prosperity, removal of poverty, business profits, debt clearance, and household luxury.",
        "benefitsHi": "अष्टलक्ष्मी कृपा, धन-ऐश्वर्य, दरिद्रता व कर्ज से मुक्ति, व्यापारिक लाभ, यश व सुख-समृद्धि की प्राप्ति।"
    },
    "maa-kali-shanivara": {
        "planetEn": "Saturn (Shani Deva)",
        "planetHi": "शनि देव",
        "color": "Black, Blue / काला, नीला",
        "accentColor": "#4338ca",
        "durationEn": "9 Saturdays",
        "durationHi": "9 शनिवार",
        "mantra": "ॐ क्रीं कालिकायै नमः। / ॐ क्रीं क्रीं क्रीं ह्रीं ह्रीं खं खं श्मशान कालिके क्रीं क्रीं क्रीं ह्रीं ह्रीं खं खं स्वाहा॥",
        "benefitsEn": "Shield against black magic, evil eye, planetary doshas (Sade Sati, Dhaiya), fear of death, and ultimate spiritual liberation.",
        "benefitsHi": "शत्रु व दुष्ट ग्रहों का शमन, शनि साढ़ेसाती व ढैय्या से रक्षा, अकाल मृत्यु भय निवारण, तांत्रिक बाधा नाश।"
    }
}

items = []
for p in raw_data:
    pid = p["id"]
    m = meta.get(pid, {})
    
    # Extract clean text sections
    en_sec = p.get("sectionsEn", {})
    hi_sec = p.get("sectionsHi", {})
    
    # Overview
    overview_en = ""
    overview_hi = ""
    for k, v in en_sec.items():
        if "Vrat" in k and "Food" not in k and "Vidhi" not in k and "Udyapana" not in k and "Other" not in k and "pageTitle" not in k:
            overview_en = v
            break
    if not overview_en:
        overview_en = list(en_sec.values())[1] if len(en_sec) > 1 else ""

    for k, v in hi_sec.items():
        if "व्रत" in k and "आहार" not in k and "विधि" not in k and "उद्यापन" not in k and "अन्य" not in k and "pageTitle" not in k:
            overview_hi = v
            break
    if not overview_hi:
        overview_hi = list(hi_sec.values())[1] if len(hi_sec) > 1 else ""

    # Fasting food
    food_en = ""
    food_hi = ""
    for k, v in en_sec.items():
        if "Fasting Food" in k or "Food" in k:
            food_en = v
            break
    for k, v in hi_sec.items():
        if "आहार" in k:
            food_hi = v
            break

    # Vidhi
    vidhi_en = ""
    vidhi_hi = ""
    for k, v in en_sec.items():
        if "Vidhi" in k or "Sankshipta" in k:
            vidhi_en = v
            break
    for k, v in hi_sec.items():
        if "विधि" in k and "उद्यापन" not in k:
            vidhi_hi = v
            break

    # Udyapan
    udyapan_en = ""
    udyapan_hi = ""
    for k, v in en_sec.items():
        if "Udyapana" in k or "Udyapan" in k:
            # strip trailing tweet/follow if any
            clean_u = re.split(r'Tweet\s+Follow|Other pages', v)[0].strip()
            udyapan_en = clean_u
            break
    for k, v in hi_sec.items():
        if "उद्यापन" in k:
            clean_u = re.split(r'Tweet\s+Follow|अन्य पृष्ठ', v)[0].strip()
            udyapan_hi = clean_u
            break

    # Related / Katha summary
    katha_en = ""
    katha_hi = ""
    for k, v in en_sec.items():
        if "Other" in k:
            m_k = re.search(r'Vrat Katha\s+(.*?)(?=\d+\s+[A-Za-z]+|\Z)', v, re.DOTALL)
            katha_en = m_k.group(1).strip() if m_k else v[:300]
            break
    for k, v in hi_sec.items():
        if "अन्य" in k or "सम्बन्धित" in k:
            m_k = re.search(r'व्रत कथा\s+(.*?)(?=\d+\.|\Z)', v, re.DOTALL)
            katha_hi = m_k.group(1).strip() if m_k else v[:300]
            break

    item = {
        "id": pid,
        "nameEn": p["nameEn"],
        "nameHi": p["nameHi"],
        "dayEn": p["dayEn"],
        "dayHi": p["dayHi"],
        "dayNum": p["dayNum"],
        "deityEn": p["deityEn"],
        "deityHi": p["deityHi"],
        "planetEn": m.get("planetEn", ""),
        "planetHi": m.get("planetHi", ""),
        "color": m.get("color", ""),
        "accentColor": m.get("accentColor", "#d97706"),
        "durationEn": m.get("durationEn", ""),
        "durationHi": m.get("durationHi", ""),
        "mantra": m.get("mantra", ""),
        "benefitsEn": m.get("benefitsEn", ""),
        "benefitsHi": m.get("benefitsHi", ""),
        "image": p["image"],
        "fallbackImage": p["fallbackImage"],
        "url": p["urlEn"],
        "overviewEn": overview_en,
        "overviewHi": overview_hi,
        "fastingFoodEn": food_en,
        "fastingFoodHi": food_hi,
        "vidhiEn": vidhi_en,
        "vidhiHi": vidhi_hi,
        "udyapanEn": udyapan_en,
        "udyapanHi": udyapan_hi,
        "kathaEn": katha_en,
        "kathaHi": katha_hi
    }
    items.append(item)

ts_content = """/* ─────────────────────────────────────────────────────────────
   DEITIES SAPTAVARA VRAT (देवी-देवता सप्तवार व्रत)
   Source: drikpanchang.com/vrats/weekdays/deities-weekdays-fasting.html
   Canonical reference: Vrat Ratnakara, Skanda Purana, Bhavishya Purana
───────────────────────────────────────────────────────────── */

export interface DeitySaptavaraVrat {
  id: string;
  nameEn: string;
  nameHi: string;
  dayEn: string;
  dayHi: string;
  dayNum: number;
  deityEn: string;
  deityHi: string;
  planetEn: string;
  planetHi: string;
  color: string;
  accentColor: string;
  durationEn: string;
  durationHi: string;
  mantra: string;
  benefitsEn: string;
  benefitsHi: string;
  image: string;
  fallbackImage: string;
  url: string;
  overviewEn: string;
  overviewHi: string;
  fastingFoodEn: string;
  fastingFoodHi: string;
  vidhiEn: string;
  vidhiHi: string;
  udyapanEn: string;
  udyapanHi: string;
  kathaEn: string;
  kathaHi: string;
}

export const DEITIES_SAPTAVARA_INTRO = {
  en: "Different types of Vrat and Upavasa are prevalent in Hinduism. Devotees observe these fasts for the fulfillment of their specific wishes. Saptavara Vrat dedicated to various Gods and Goddesses, are very popular among the people. Saptavara Vrat means fasts observed according to the weekdays such as Ravivara Vrat, Somavara Vrat, Mangalavara Vrat etc. According to the Vrat Ratnakara, these weekday fasts should ideally be started in the months of Vaishakha, Margashirsha and Magha. By observing these fasts, one not only attains spiritual benefits but also experiences physical and mental well-being. Here, the weekday fasts dedicated to the Gods and Goddesses are described, including their fasting food, Puja Vidhi, and the ritual of conclusion, i.e. Udyapana Vidhi.",
  hi: "हिन्दु धर्म में विभिन्न प्रकार के व्रत एवं उपवास प्रचलित हैं। भक्तगण अपने विशेष मनोरथों की सिद्धि हेतु इन व्रतों का पालन करते हैं। जन साधारण में विभिन्न देवी-देवताओं को समर्पित सप्तवार व्रत अत्यन्त लोकप्रिय हैं। सप्तवार व्रत अर्थात् सप्ताह के दिनों के अनुसार किये जाने वाले व्रत जैसे रविवार व्रत, सोमवार व्रत, मङ्गलवार व्रत आदि। व्रत रत्नाकर के अनुसार, वार के व्रत का आरम्भ मुख्यतः वैशाख, मार्गशीर्ष तथा माघ माह में किया जाना चाहिये। इन व्रतों को करने से व्यक्ति को आध्यात्मिक लाभ तो होता ही है साथ ही शारीरिक एवं मानसिक लाभ की अनुभूति भी होती है। यहाँ देवी-देवताओं को समर्पित सप्ताह के सभी दिनों के व्रत, उनका आहार-विचार, पूजन विधि एवं उद्यापन विधि का वर्णन किया गया है।"
};

export const DEITIES_SAPTAVARA_VRATS: DeitySaptavaraVrat[] = """ + json.dumps(items, ensure_ascii=False, indent=2) + ";\n"

out_ts_file = r'd:\FabricQ_OSHub\NewsHub\NewsGraphic02\bhakti-platform\apps\web\src\data\deitiesSaptavaraData.ts'
os.makedirs(os.path.dirname(out_ts_file), exist_ok=True)
with open(out_ts_file, 'w', encoding='utf-8') as f:
    f.write(ts_content)

print(f"TypeScript data written to {out_ts_file} successfully! Total records: {len(items)}")
