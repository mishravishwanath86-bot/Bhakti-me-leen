import re
import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')

en_file = r'C:\Users\vishw\.gemini\antigravity-ide\brain\85d64534-ea39-4946-988b-be7eeefc13c3\.system_generated\steps\8203\content.md'
hi_file = r'C:\Users\vishw\.gemini\antigravity-ide\brain\85d64534-ea39-4946-988b-be7eeefc13c3\.system_generated\steps\8205\content.md'

with open(en_file, 'r', encoding='utf-8') as f:
    en_html = f.read()

with open(hi_file, 'r', encoding='utf-8') as f:
    hi_html = f.read()

clean = lambda t: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)).strip() if t else ""

def clean_vrat_text(raw):
    if '>' in raw:
        raw = raw.split('>')[-1]
    return raw.strip()

def clean_time(raw):
    # remove comma spacing
    raw = clean(raw)
    raw = re.sub(r'\s*,\s*', ', ', raw)
    return raw.strip()

def parse_full_clean(html, is_hi=False):
    blocks = re.split(r'(?=<div class="dpEventCard\s+dpFlexWrap)', html)
    results = []
    
    for b in blocks[1:]:
        if '<div class="dpEventDateTitle">' not in b:
            continue
            
        is_adhika = "dpLeapedMonthEventCard" in b[:80] or "dpAdhika" in b[:80]
        is_passed = "dpPassedEventCard" in b[:80]
        
        # Date
        m_date = re.search(r'<div class="dpEventDateTitle">(.*?)</div>', b)
        date_str = clean(m_date.group(1)) if m_date else ""
        
        # Vrats
        m_link_div = re.search(r'<div class="dpEventCardLink">(.*?)</div>\s*</div>\s*</div>', b, re.DOTALL)
        vrats = []
        if m_link_div:
            vrat_matches = re.findall(r'>([^<]+)</a>', m_link_div.group(1))
            vrats = [clean_vrat_text(clean(v)) for v in vrat_matches if clean(v)]
            
        # Month & Tithi
        m_tithi = re.search(r'<div class="dpEventCardInfoTitle">(.*?)</div>', b)
        month_tithi = clean(m_tithi.group(1)) if m_tithi else ""
        
        # Begins & Ends
        # Extract between Begins/प्रारम्भ - and </div>
        m_beg = re.search(r'(?:Begins|प्रारम्भ)\s*-\s*(.*?)(?=</div>|<br|$)', b)
        beg_str = clean_time(m_beg.group(1)) if m_beg else ""
        
        m_end = re.search(r'(?:Ends|समाप्त)\s*-\s*(.*?)(?=</div>|<br|$)', b)
        end_str = clean_time(m_end.group(1)) if m_end else ""
        
        results.append({
            "isAdhika": is_adhika,
            "isPassed": is_passed,
            "date": date_str,
            "vrats": vrats,
            "monthTithi": month_tithi,
            "begins": beg_str,
            "ends": end_str
        })
    return results

en_list = parse_full_clean(en_html, False)
hi_list = parse_full_clean(hi_html, True)

month_map = {
    'January': ('01', 'Magha', 'माघ'),
    'February': ('02', 'Phalguna', 'फाल्गुन'),
    'March': ('03', 'Chaitra', 'चैत्र'),
    'April': ('04', 'Vaishakha', 'वैशाख'),
    'May': ('05', 'Jyeshtha', 'ज्येष्ठ'),
    'June': ('06', 'Jyeshtha (Adhika)', 'ज्येष्ठ (अधिक)'),
    'July': ('07', 'Ashadha', 'आषाढ़'),
    'August': ('08', 'Shravana', 'श्रावण'),
    'September': ('09', 'Bhadrapada', 'भाद्रपद'),
    'October': ('10', 'Ashwina', 'आश्विन'),
    'November': ('11', 'Kartika', 'कार्तिक'),
    'December': ('12', 'Margashirsha', 'मार्गशीर्ष')
}

special_meta = {
    "2026-01-18": {
        "specialLabelEn": "Mauni Amavasya",
        "specialLabelHi": "मौनी अमावस्या",
        "significanceEn": "Most sacred day for taking a holy dip at Prayagraj Triveni Sangam. Observing Mauna (silence) and Til-Daan yields spiritual merits equivalent to Ashwamedha Yajna.",
        "significanceHi": "प्रयागराज त्रिवेणी संगम में पावन स्नान का परम पुण्य दिवस। मौन व्रत, तिल दान व पितृ तर्पण से अश्वमेध यज्ञ तुल्य फल प्राप्त होता है।"
    },
    "2026-02-17": {
        "specialLabelEn": "Bhaumvati Amavasya",
        "specialLabelHi": "भौमवती अमावस्या",
        "significanceEn": "Amavasya falling on Tuesday (Bhaumvara) is dedicated to Lord Hanuman and Mars pacification. Ideal for debt relief and land dispute remedies.",
        "significanceHi": "मङ्गलवार को पड़ने वाली अमावस्या भौमवती अमावस्या कहलाती है। कर्ज मुक्ति, ऋण मोचन व मंगल दोष निवारण हेतु विशेष फलदायी।"
    },
    "2026-03-18": {
        "specialLabelEn": "Darsha Amavasya (Chaitra)",
        "specialLabelHi": "दर्श अमावस्या (चैत्र)",
        "significanceEn": "Day of moonlessness preceding the Hindu New Year (Chaitra Shukla Pratipada). Dedicated to ancestors' Shraddha.",
        "significanceHi": "नव संवत्सरारम्भ से पूर्व चन्द्र दर्शन रहित दर्श अमावस्या। पितृ श्राद्ध व तर्पण का श्रेष्ठ दिन।"
    },
    "2026-03-19": {
        "specialLabelEn": "Chaitra Amavasya",
        "specialLabelHi": "चैत्र अमावस्या",
        "significanceEn": "Concludes the month of Chaitra Krishna Paksha. Auspicious for sacred dips, charitable gifts, and pitru puja.",
        "significanceHi": "चैत्र कृष्ण पक्ष की समाप्ति तिथि। पवित्र नदी स्नान, अन्न-दान एवं पितरों की प्रसन्नता हेतु पूजा।"
    },
    "2026-04-17": {
        "specialLabelEn": "Vaishakha Amavasya / Sattu Amavasya",
        "specialLabelHi": "वैशाख अमावस्या (सत्तू अमावस्या)",
        "significanceEn": "Water pots (Ghat-Daan), umbrellas, fan and roasted gram (Sattu) donation are highly commended in summer.",
        "significanceHi": "ग्रीष्म ऋतु में जलपात्र (घट दान), पंखा, छाता, सत्तू व खरबूजा दान का महापर्व।"
    },
    "2026-05-16": {
        "specialLabelEn": "Shani Amavasya • Vat Savitri Vrat",
        "specialLabelHi": "शनि अमावस्या • वट सावित्री व्रत",
        "significanceEn": "Doubly auspicious! Falling on Saturday makes it Shani Jayanti / Shani Amavasya. Married women observe Vat Savitri Vrat for husband's longevity.",
        "significanceHi": "अति दुर्लभ महायोग! शनिवार पड़ने से शनि अमावस्या (शनि जयन्ती) तथा सुहागिनों द्वारा अखण्ड सौभाग्य हेतु वट सावित्री व्रत।"
    },
    "2026-06-14": {
        "specialLabelEn": "Adhika Darsha Amavasya (Extra Jyeshtha)",
        "specialLabelHi": "अधिक दर्श अमावस्या (मलमास/पुरुषोत्तम)",
        "significanceEn": "Falling in Adhika (intercalary) Jyeshtha month. Dedicated to Lord Purushottama (Vishnu) and ancestor redemption.",
        "significanceHi": "अधिक (पुरुषोत्तम) मास की दर्श अमावस्या। भगवान श्री हरि विष्णु की विशेष आराधना व पितृ दोष मुक्ति।"
    },
    "2026-06-15": {
        "specialLabelEn": "Somvati Adhika Amavasya (Adhika Maas)",
        "specialLabelHi": "सोमवती अधिक अमावस्या (सोमवार)",
        "significanceEn": "Extremely rare combination of Somvati (Monday) + Adhika Maas! 108 parikrama of Peepal tree brings inexhaustible merits.",
        "significanceHi": "अति दुर्लभ महासंयोग! सोमवार + अधिक मास (पुरुषोत्तम मास)। पीपल वृक्ष की 108 परिक्रमा से अक्षय पुण्य फल प्राप्त होता है।"
    },
    "2026-07-14": {
        "specialLabelEn": "Bhaumvati Amavasya (Ashadha)",
        "specialLabelHi": "भौमवती अमावस्या (आषाढ़)",
        "significanceEn": "Precedes the holy Shravana month. Tuesday Amavasya brings relief from blood disorders and debt.",
        "significanceHi": "पवित्र श्रावण मास से पूर्व आषाढ़ अमावस्या। मंगलवार के योग से ऋण मुक्ति व रक्त विकार शान्ति।"
    },
    "2026-08-12": {
        "specialLabelEn": "Hariyali Amavasya (Shravana)",
        "specialLabelHi": "हरियाली अमावस्या (श्रावण)",
        "significanceEn": "Celebrates nature, green foliage, Lord Shiva worship in Sawan, tree plantation and ancestral blessings.",
        "significanceHi": "प्रकृति पूजन, पौधरोपण, सावन में भगवान शिव-पार्वती की असीम कृपा व पितृ तर्पण का पावन पर्व।"
    },
    "2026-09-10": {
        "specialLabelEn": "Darsha Amavasya (Pitru Paksha)",
        "specialLabelHi": "दर्श अमावस्या (पितृ पक्ष)",
        "significanceEn": "Commencement of the culminating new moon of Pitru Paksha. Shraddha and Tarpan performed for all deceased souls.",
        "significanceHi": "पितृ पक्ष की दर्श अमावस्या। समस्त ज्ञात-अज्ञात पितरों के निमित्त पिण्डदान व तर्पण।"
    },
    "2026-09-11": {
        "specialLabelEn": "Sarva Pitru Amavasya (Mahalaya)",
        "specialLabelHi": "सर्वपितृ अमावस्या (महालया)",
        "significanceEn": "The paramount ancestor ritual day of the year. Shraddha for all ancestors whose death tithi is unknown. Concludes Pitru Paksha.",
        "significanceHi": "वर्ष की सर्वाधिक महत्त्वपूर्ण पितृ तिथि! समस्त ज्ञात-अज्ञात पूर्वजों का श्राद्ध, पिण्डदान एवं महालया विसर्जन।"
    },
    "2026-10-10": {
        "specialLabelEn": "Shani Amavasya (Ashwina)",
        "specialLabelHi": "शनि अमावस्या (आश्विन)",
        "significanceEn": "Amavasya falling on Saturday. Pacifies Sade Sati, Dhaiya and Shani Mahadasha through mustard oil and sesame offerings.",
        "significanceHi": "शनिवार की अमावस्या। काले तिल, सरसों के तेल के दीपक व शमी पूजन से शनि की साढ़ेसाती व ढैय्या के कष्टों से मुक्ति।"
    },
    "2026-11-08": {
        "specialLabelEn": "Diwali Lakshmi Puja (Kartika Amavasya)",
        "specialLabelHi": "दीपावली लक्ष्मी पूजा (कार्तिक अमावस्या)",
        "significanceEn": "The grand festival of lights! Goddess Lakshmi and Lord Ganesha worship during Nishitha / Pradosh Kaal on Kartika Amavasya night.",
        "significanceHi": "महापर्व दीपावली! प्रदोष व निशीथ काल में माँ महालक्ष्मी, भगवान गणेश व कुबेर देव का महापूजन व दीपदान।"
    },
    "2026-11-09": {
        "specialLabelEn": "Somvati Amavasya • Kartika Snan",
        "specialLabelHi": "सोमवती अमावस्या (कार्तिक स्नान)",
        "significanceEn": "Auspicious Monday Amavasya falling in the holy month of Kartika. Sacred dips in Ganga and circumambulation of Peepal tree.",
        "significanceHi": "कार्तिक माह में सोमवार का परम पावन संयोग। गंगा स्नान, दान, दीपदान एवं पीपल वृक्ष की परिक्रमा।"
    },
    "2026-12-08": {
        "specialLabelEn": "Bhaumvati Amavasya (Margashirsha)",
        "specialLabelHi": "भौमवती अमावस्या (मार्गशीर्ष)",
        "significanceEn": "Margashirsha Amavasya falling on Tuesday. Dedicated to Lord Krishna and Hanumanji for peace and spiritual upliftment.",
        "significanceHi": "मार्गशीर्ष मास में मंगलवार को पड़ने वाली अमावस्या। गीता जयन्ती मास में भगवान श्रीकृष्ण व हनुमान जी की आराधना।"
    }
}

final_entries = []

for i in range(len(en_list)):
    e = en_list[i]
    h = hi_list[i]
    
    # parse ISO date
    m_iso = re.search(r'([A-Za-z]+)\s+(\d+),\s+(\d{4})', e['date'])
    iso = ""
    day_name_en = ""
    if m_iso:
        mon_name = m_iso.group(1)
        mon_info = month_map.get(mon_name, ('01', 'Magha', 'माघ'))
        day_num = f"{int(m_iso.group(2)):02d}"
        yr = m_iso.group(3)
        iso = f"{yr}-{mon_info[0]}-{day_num}"
    
    # day name
    if "Sunday" in e['date']: day_name_en, day_name_hi = "Sunday", "रविवार"
    elif "Monday" in e['date']: day_name_en, day_name_hi = "Monday", "सोमवार"
    elif "Tuesday" in e['date']: day_name_en, day_name_hi = "Tuesday", "मंगलवार"
    elif "Wednesday" in e['date']: day_name_en, day_name_hi = "Wednesday", "बुधवार"
    elif "Thursday" in e['date']: day_name_en, day_name_hi = "Thursday", "बृहस्पतिवार"
    elif "Friday" in e['date']: day_name_en, day_name_hi = "Friday", "शुक्रवार"
    elif "Saturday" in e['date']: day_name_en, day_name_hi = "Saturday", "शनिवार"
    else: day_name_en, day_name_hi = "", ""
    
    spec = special_meta.get(iso, {
        "specialLabelEn": None,
        "specialLabelHi": None,
        "significanceEn": "Appropriate day for performing Shraddha rituals to appease ancestors, charity, and taking sacred dips.",
        "significanceHi": "पूर्वजों की आत्मा की तृप्ति के लिए श्राद्ध की रस्मों, दान-पुण्य एवं पवित्र नदी स्नान हेतु उपयुक्त दिन।"
    })
    
    entry = {
        "id": f"amav-{i+1:02d}",
        "gregorianDate": e['date'],
        "gregorianDateHi": h['date'],
        "dayName": day_name_en,
        "dayNameHi": day_name_hi,
        "isoDate": iso,
        "vrats": e['vrats'],
        "vratsHi": h['vrats'],
        "monthTithi": e['monthTithi'],
        "monthTithiHi": h['monthTithi'],
        "begins": e['begins'],
        "beginsHi": h['begins'],
        "ends": e['ends'],
        "endsHi": h['ends'],
        "isAdhika": e['isAdhika'],
        "isPassed": e['isPassed'],
        "specialLabelEn": spec.get("specialLabelEn"),
        "specialLabelHi": spec.get("specialLabelHi"),
        "significanceEn": spec.get("significanceEn"),
        "significanceHi": spec.get("significanceHi")
    }
    final_entries.append(entry)

ts_content = """/* ─────────────────────────────────────────────────────────────
   AMAVASYA DATES 2026 (2026 अमावस्या तिथियाँ)
   Source: drikpanchang.com/vrats/amavasyadates.html
   Location: New Delhi, India (IST)
   Vikrama Samvata 2082 - 2083
───────────────────────────────────────────────────────────── */

export interface AmavasyaEntry {
  id: string;
  gregorianDate: string;
  gregorianDateHi: string;
  dayName: string;
  dayNameHi: string;
  isoDate: string;
  vrats: string[];
  vratsHi: string[];
  monthTithi: string;
  monthTithiHi: string;
  begins: string;
  beginsHi: string;
  ends: string;
  endsHi: string;
  isAdhika: boolean;
  isPassed: boolean;
  specialLabelEn: string | null;
  specialLabelHi: string | null;
  significanceEn: string;
  significanceHi: string;
}

export const AMAVASYA_INTRO = {
  en: "Amavasya is the new moon day in the Hindu calendar. It is a highly significant day as many important religious rituals and pujas are performed exclusively on Amavasya Tithi. Amavasya falling on a Monday is celebrated as Somvati Amavasya, on a Saturday as Shani Amavasya, and on a Tuesday as Bhaumvati Amavasya. All Amavasya days are considered auspicious for performing Shraddha rituals, Tarpana, and charitable deeds to appease ancestors (Pitrus) and to seek relief from Kalasarpa Dosha.",
  hi: "हिन्दु कैलेण्डर में नये चन्द्रमा के दिन को अमावस्या कहते हैं। यह एक अत्यन्त महत्त्वपूर्ण दिन होता है क्योंकि कई धार्मिक कृत्य केवल अमावस्या तिथि के दिन ही किये जाते हैं। अमावस्या जब सोमवार के दिन पड़ती है तो उसे सोमवती अमावस्या, शनिवार को शनि अमावस्या, तथा मंगलवार को भौमवती अमावस्या कहते हैं। पूर्वजों की आत्मा की तृप्ति के लिए अमावस्या के सभी दिन श्राद्ध एवं तर्पण के लिए सर्वोत्तम माने गये हैं। कालसर्प दोष निवारण की पूजा करने के लिए भी अमावस्या का दिन उपयुक्त होता है।"
};

export const AMAVASYA_2026: AmavasyaEntry[] = """ + json.dumps(final_entries, ensure_ascii=False, indent=2) + ";\n"

out_ts = r'd:\FabricQ_OSHub\NewsHub\NewsGraphic02\bhakti-platform\apps\web\src\data\amavasyaDatesData.ts'
os.makedirs(os.path.dirname(out_ts), exist_ok=True)
with open(out_ts, 'w', encoding='utf-8') as f:
    f.write(ts_content)

print(f"Written {len(final_entries)} entries to {out_ts} successfully!")
