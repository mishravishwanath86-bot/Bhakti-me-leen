import re, os, json, sys

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🖼️ UPDATING BAL ROOP GALLERY & REMOVING '60' ACROSS ENTIRE APP")
print("======================================================================")

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Tab Pills in index.html
old_tabs = """      <!-- 4 Luxury Pill Tabs -->
      <div class="gal-tabs-bar">
        <button class="gal-tab-pill active" data-tab="bal" onclick="switchGalleryTab('bal')">
          👶 बाल रूप (60)
        </button>
        <button class="gal-tab-pill" data-tab="divya" onclick="switchGalleryTab('divya')">
          🕉️ दिव्य रूप (60)
        </button>
        <button class="gal-tab-pill" data-tab="india" onclick="switchGalleryTab('india')">
          🇮🇳 भारत के प्रमुख मंदिर (69)
        </button>
        <button class="gal-tab-pill" data-tab="world" onclick="switchGalleryTab('world')">
          🌍 विश्व के प्रमुख मंदिर (32)
        </button>
      </div>"""

new_tabs = """      <!-- 4 Luxury Pill Tabs -->
      <div class="gal-tabs-bar">
        <button class="gal-tab-pill active" data-tab="bal" onclick="switchGalleryTab('bal')">
          👶 बाल रूप
        </button>
        <button class="gal-tab-pill" data-tab="divya" onclick="switchGalleryTab('divya')">
          🕉️ दिव्य रूप
        </button>
        <button class="gal-tab-pill" data-tab="india" onclick="switchGalleryTab('india')">
          🇮🇳 भारत के प्रमुख मंदिर
        </button>
        <button class="gal-tab-pill" data-tab="world" onclick="switchGalleryTab('world')">
          🌍 विश्व के प्रमुख मंदिर
        </button>
      </div>"""

if old_tabs in html:
    html = html.replace(old_tabs, new_tabs, 1)
    print("✓ Updated Gallery Tab Pills in index.html (removed counts from tabs)")
else:
    # Regex replacement for tab pills
    html = re.sub(r'👶\s*बाल रूप\s*\(\d+\)', '👶 बाल रूप', html)
    html = re.sub(r'🕉️\s*दिव्य रूप\s*\(\d+\)', '🕉️ दिव्य रूप', html)
    html = re.sub(r'🇮🇳\s*भारत के प्रमुख मंदिर\s*\(\d+\)', '🇮🇳 भारत के प्रमुख मंदिर', html)
    html = re.sub(r'🌍\s*विश्व के प्रमुख मंदिर\s*\(\d+\)', '🌍 विश्व के प्रमुख मंदिर', html)
    print("✓ Replaced tab pill labels via regex")

# Update initial counter badge in index.html
html = html.replace('<div id="gallery-count-badge" class="gallery-counter-badge">\n          60 स्वरूप\n        </div>', '<div id="gallery-count-badge" class="gallery-counter-badge">\n          ✨ समस्त बाल रूप स्वरूप\n        </div>')
html = re.sub(r'<div id="gallery-count-badge" class="gallery-counter-badge">\s*60 स्वरूप\s*<\/div>', '<div id="gallery-count-badge" class="gallery-counter-badge">\n          ✨ समस्त बाल रूप स्वरूप\n        </div>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ index.html updated successfully!")


# 2. Build Authentic Bal Roop Dataset (All 30 Deities with 100% Real Image Assets)
bal_roop_dataset = [
  {
    "id": "bal-ganesha",
    "nameHi": "बाल गणेश",
    "nameEn": "Little Bal Ganesha",
    "category": "tridev",
    "mantra": "॥ ॐ गं गणपतये नमः ॥",
    "img": "assets/gallery/bal_ganesha_little.jpg",
    "fallbackImg": "assets/gallery/bal_ganesha.jpg",
    "desc": "मोदक प्रिय, रिद्धि-सिद्धि दाता नन्हे बाल गणेश का अत्यंत मनोहारी एवं मनमोहक स्वरूप।"
  },
  {
    "id": "bal-krishna",
    "nameHi": "बाल कृष्ण (माखनचोर)",
    "nameEn": "Little Bal Krishna",
    "category": "avatar",
    "mantra": "॥ ॐ नमो भगवते वासुदेवाय ॥",
    "img": "assets/gallery/bal_krishna.jpg",
    "fallbackImg": "assets/gallery/bal_radha_krishna.jpg",
    "desc": "मयूर मुकुट धारी, माखन की मटकी के साथ नटखट कान्हा का अलौकिक बाल स्वरूप।"
  },
  {
    "id": "bal-shiva",
    "nameHi": "बाल शिव (भोलेनाथ)",
    "nameEn": "Little Bal Shiva",
    "category": "tridev",
    "mantra": "॥ ॐ नमः शिवाय ॥",
    "img": "assets/gallery/bal_shiva.jpg",
    "fallbackImg": "assets/deity_shiv.jpg",
    "desc": "मस्तक पर बाल-चंद्र, हाथ में छोटा डमरू और त्रिशूल लिए ध्यानमग्न बाल शिव।"
  },
  {
    "id": "bal-hanuman",
    "nameHi": "बाल हनुमान (बजरंगबली)",
    "nameEn": "Little Bal Hanuman",
    "category": "avatar",
    "mantra": "॥ ॐ हं हनुमते नमः ॥",
    "img": "assets/gallery/bal_hanuman.jpg",
    "fallbackImg": "assets/deity_hanuman.jpg",
    "desc": "हाथ में स्वर्णिम गदा, सूर्यदेव की ओर कुलांचे भरते असीम बलशाली बाल पवनपुत्र।"
  },
  {
    "id": "bal-rama",
    "nameHi": "बाल राम (रघुनंदन)",
    "nameEn": "Little Bal Rama",
    "category": "avatar",
    "mantra": "॥ श्री राम जय राम जय जय राम ॥",
    "img": "assets/gallery/bal_rama_little.jpg",
    "fallbackImg": "assets/gallery/bal_rama.jpg",
    "desc": "अयोध्या के नन्हें राजकुमार, धनुष-बाण लिए सौम्य एवं तेजस्वी मर्यादा पुरुषोत्तम बाल राम।"
  },
  {
    "id": "bal-durga",
    "nameHi": "बाल दुर्गा",
    "nameEn": "Little Devi Durga",
    "category": "devi",
    "mantra": "॥ ॐ दुं दुर्गायै नमः ॥",
    "img": "assets/gallery/bal_durga_little.jpg",
    "fallbackImg": "assets/gallery/bal_durga.jpg",
    "desc": "सिंह शावक के संग, अष्टभुजाओं में दिव्य आयुध लिए माँ आद्यशक्ति का बाल स्वरूप।"
  },
  {
    "id": "bal-saraswati",
    "nameHi": "बाल सरस्वती",
    "nameEn": "Little Devi Saraswati",
    "category": "devi",
    "mantra": "॥ ॐ ऐं सरस्वत्यै नमः ॥",
    "img": "assets/gallery/bal_saraswati_little.jpg",
    "fallbackImg": "assets/gallery/bal_saraswati.jpg",
    "desc": "श्वेत कमल पर विराजित, नन्हीं वीणा वादन करती ज्ञान और विद्या की देवी बाल सरस्वती।"
  },
  {
    "id": "bal-lakshmi",
    "nameHi": "बाल लक्ष्मी",
    "nameEn": "Little Devi Lakshmi",
    "category": "devi",
    "mantra": "॥ ॐ श्रीं ह्रीं क्लीं महालक्ष्म्यै नमः ॥",
    "img": "assets/gallery/bal_lakshmi_little.jpg",
    "fallbackImg": "assets/gallery/bal_lakshmi.jpg",
    "desc": "हाथों से स्वर्ण वर्षा करती, सुख-समृद्धि प्रदायिनी माँ महालक्ष्मी का पावन बाल स्वरूप।"
  },
  {
    "id": "bal-kartikeya",
    "nameHi": "बाल कार्तिकेय (मुरुगन)",
    "nameEn": "Little Bal Kartikeya",
    "category": "tridev",
    "mantra": "॥ ॐ शरवणभवाय नमः ॥",
    "img": "assets/gallery/bal_murugan_little.jpg",
    "fallbackImg": "assets/gallery/bal_ganesha.jpg",
    "desc": "मयूर वाहन पर सवार, दिव्य शक्ति अस्त्र धारण किए देवसेनापति बाल मुरुगन।"
  },
  {
    "id": "bal-vishnu",
    "nameHi": "बाल विष्णु",
    "nameEn": "Little Bal Vishnu",
    "category": "tridev",
    "mantra": "॥ ॐ नमो नारायणाय ॥",
    "img": "assets/gallery/bal_vishnu_little.jpg",
    "fallbackImg": "assets/gallery/bal_vishnu.jpg",
    "desc": "शंख, चक्र, गदा और पद्म धारण किए क्षीरसागर में जगतपालक श्री हरि का बाल स्वरूप।"
  },
  {
    "id": "bal-indra",
    "nameHi": "बाल इंद्र",
    "nameEn": "Little Bal Indra",
    "category": "vedic",
    "mantra": "॥ ॐ इन्द्राय नमः ॥",
    "img": "assets/gallery/bal_indra_little.jpg",
    "fallbackImg": "assets/deity_surya.jpg",
    "desc": "ऐरावत हाथी के संग, हाथ में छोटा वज्र लिए देवराज इंद्र का तेजस्वी बाल स्वरूप।"
  },
  {
    "id": "bal-parvati",
    "nameHi": "बाल पार्वती (गौरी)",
    "nameEn": "Little Devi Parvati",
    "category": "devi",
    "mantra": "॥ ॐ गौर्ये नमः ॥",
    "img": "assets/gallery/bal_parvati_little.jpg",
    "fallbackImg": "assets/gallery/bal_durga.jpg",
    "desc": "हिमालय पुत्री, नन्हीं कन्या के रूप में तपस्या और वात्सल्य की अधिष्ठात्री बाल पार्वती।"
  },
  {
    "id": "bal-agni",
    "nameHi": "बाल अग्नि",
    "nameEn": "Little Bal Agni",
    "category": "vedic",
    "mantra": "॥ ॐ अग्नये नमः ॥",
    "img": "assets/gallery/bal_agni_little.jpg",
    "fallbackImg": "assets/deity_surya.jpg",
    "desc": "यज्ञ और पावन ज्वाला के देवता, मेष वाहन संग तेजस्वी बाल अग्निदेव।"
  },
  {
    "id": "bal-vayu",
    "nameHi": "बाल वायु",
    "nameEn": "Little Bal Vayu",
    "category": "vedic",
    "mantra": "॥ ॐ वायवे नमः ॥",
    "img": "assets/gallery/bal_vayu_little.jpg",
    "fallbackImg": "assets/deity_hanuman.jpg",
    "desc": "प्राणवायु और पवन के स्वामी, हिरण के संग चंचल एवं प्राणवान बाल वायुदेव।"
  },
  {
    "id": "bal-varuna",
    "nameHi": "बाल वरुण",
    "nameEn": "Little Bal Varuna",
    "category": "vedic",
    "mantra": "॥ ॐ वरुणाय नमः ॥",
    "img": "assets/gallery/bal_varuna_little.jpg",
    "fallbackImg": "assets/deity_ganga.jpg",
    "desc": "जल, समुद्र और वर्षा के अधिपति, मकर वाहन संग सौम्य बाल वरुणदेव।"
  },
  {
    "id": "bal-surya",
    "nameHi": "बाल सूर्य (भास्कर)",
    "nameEn": "Little Bal Surya",
    "category": "vedic",
    "mantra": "॥ ॐ सूर्याय नमः ॥",
    "img": "assets/gallery/bal_surya_little.jpg",
    "fallbackImg": "assets/deity_surya.jpg",
    "desc": "स्वर्णिम रथ और सात श्वेत अश्वों के संग संपूर्ण ब्रह्मांड को आलोकित करते बाल सूर्यदेव।"
  },
  {
    "id": "bal-chandra",
    "nameHi": "बाल चंद्र (सोम)",
    "nameEn": "Little Bal Chandra",
    "category": "vedic",
    "mantra": "॥ ॐ सोमाय नमः ॥",
    "img": "assets/gallery/bal_chandra_little.jpg",
    "fallbackImg": "assets/deity_shiv.jpg",
    "desc": "शीतल अमृत किरणें बिखेरते, नन्हे बाल-चंद्र का शांत और आह्लादकारी स्वरूप।"
  },
  {
    "id": "bal-kali",
    "nameHi": "बाल काली",
    "nameEn": "Little Devi Kali",
    "category": "devi",
    "mantra": "॥ ॐ क्रीं कालिकायै नमः ॥",
    "img": "assets/gallery/bal_kali_little.jpg",
    "fallbackImg": "assets/gallery/bal_durga.jpg",
    "desc": "दुष्टों का संहार करने वाली और भक्तों की रक्षा करने वाली माँ महाकाली का दिव्य बाल स्वरूप।"
  },
  {
    "id": "bal-brahma",
    "nameHi": "बाल ब्रह्मा",
    "nameEn": "Little Bal Brahma",
    "category": "tridev",
    "mantra": "॥ ॐ ब्रह्मणे नमः ॥",
    "img": "assets/gallery/bal_brahma_little.jpg",
    "fallbackImg": "assets/gallery/bal_saraswati.jpg",
    "desc": "चतुर्मुख, हाथ में वेद और कमंडल लिए सृष्टि के रचयिता भगवान ब्रह्मा का नन्हा बाल स्वरूप।"
  },
  {
    "id": "bal-narasimha",
    "nameHi": "बाल नरसिंह",
    "nameEn": "Little Bal Narasimha",
    "category": "avatar",
    "mantra": "॥ ॐ उग्रं वीरं महाविष्णुं ज्वलन्तं सर्वतोमुखम् ॥",
    "img": "assets/gallery/bal_narasimha_little.jpg",
    "fallbackImg": "assets/deity_narasimha.jpg",
    "desc": "भक्त प्रह्लाद के रक्षक, सौम्य शांत मुखमंडल युक्त भगवान श्री नृसिंह का बाल स्वरूप।"
  },
  {
    "id": "bal-radha",
    "nameHi": "बाल राधा (लाडली जी)",
    "nameEn": "Little Bal Radha",
    "category": "devi",
    "mantra": "॥ ॐ राधायै स्वाहा ॥",
    "img": "assets/gallery/bal_radha_little.jpg",
    "fallbackImg": "assets/gallery/bal_radha_krishna.jpg",
    "desc": "बरसाना की दुलारी, प्रेम और भक्ति की साक्षात मूर्ति नन्हीं किशोरी जी बाल राधा।"
  },
  {
    "id": "bal-balarama",
    "nameHi": "बाल बलराम (दाऊ)",
    "nameEn": "Little Bal Balarama",
    "category": "avatar",
    "mantra": "॥ ॐ बलभद्राय नमः ॥",
    "img": "assets/gallery/bal_balarama_little.jpg",
    "fallbackImg": "assets/gallery/bal_krishna.jpg",
    "desc": "हाथ में छोटा हल और मूसल धारण किए, कान्हा के बड़े भाई बलशाली दाऊ भैया।"
  },
  {
    "id": "bal-kubera",
    "nameHi": "बाल कुबेर",
    "nameEn": "Little Bal Kubera",
    "category": "vedic",
    "mantra": "॥ ॐ यक्षाय कुबेराय वैश्रवणाय धनधान्याधिपतये नमः ॥",
    "img": "assets/gallery/bal_kubera_little.jpg",
    "fallbackImg": "assets/gallery/bal_lakshmi.jpg",
    "desc": "धन-धान्य और समस्त निधियों के स्वामी, रत्नों की थैली लिए बाल कुबेर देव।"
  },
  {
    "id": "bal-annapurna",
    "nameHi": "बाल अन्नपूर्णा",
    "nameEn": "Little Devi Annapurna",
    "category": "devi",
    "mantra": "॥ ॐ अन्नपूर्णायै नमः ॥",
    "img": "assets/gallery/bal_annapurna_little.jpg",
    "fallbackImg": "assets/gallery/bal_durga.jpg",
    "desc": "स्वर्ण कलश और करछी लिए समस्त जीवों को पोषण और तृप्ति देने वाली माँ बाल अन्नपूर्णा।"
  },
  {
    "id": "bal-kamadhenu",
    "nameHi": "बाल कामधेनु",
    "nameEn": "Little Bal Kamadhenu",
    "category": "bhakt",
    "mantra": "॥ ॐ कामधेन्वै नमः ॥",
    "img": "assets/gallery/bal_kamadhenu_little.jpg",
    "fallbackImg": "assets/gallery/bal_krishna.jpg",
    "desc": "सभी मनोकामनाओं को पूर्ण करने वाली, अमृतमयी दिव्य सुरभि बाल कामधेनु।"
  },
  {
    "id": "bal-hayagriva",
    "nameHi": "बाल हयग्रीव",
    "nameEn": "Little Bal Hayagriva",
    "category": "avatar",
    "mantra": "॥ ॐ हयग्रीवाय नमः ॥",
    "img": "assets/gallery/bal_hayagriva_little.jpg",
    "fallbackImg": "assets/gallery/bal_vishnu.jpg",
    "desc": "ज्ञान, मेधा और विद्या के दाता, भगवान विष्णु के अश्वमुखी बाल हयग्रीव स्वरूप।"
  },
  {
    "id": "bal-gayatri",
    "nameHi": "बाल गायत्री",
    "nameEn": "Little Devi Gayatri",
    "category": "devi",
    "mantra": "॥ ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि ॥",
    "img": "assets/gallery/bal_gayatri_little.jpg",
    "fallbackImg": "assets/gallery/bal_saraswati.jpg",
    "desc": "वेदों की जननी, पंचमुखी ज्योतिर्मयी माँ गायत्री का पावन बाल स्वरूप।"
  },
  {
    "id": "bal-ganga",
    "nameHi": "बाल गंगा",
    "nameEn": "Little Devi Ganga",
    "category": "bhakt",
    "mantra": "॥ ॐ गंगायै नमः ॥",
    "img": "assets/gallery/bal_ganga_little.jpg",
    "fallbackImg": "assets/deity_ganga.jpg",
    "desc": "पतित पावनी, स्वर्ग से अवतरित होकर मोक्षदायिनी माँ बाल गंगा का निर्मल स्वरूप।"
  },
  {
    "id": "bal-yamuna",
    "nameHi": "बाल यमुना",
    "nameEn": "Little Devi Yamuna",
    "category": "bhakt",
    "mantra": "॥ ॐ यमुनाथायै नमः ॥",
    "img": "assets/gallery/bal_yamuna_little.jpg",
    "fallbackImg": "assets/gallery/bal_radha_little.jpg",
    "desc": "सूर्यपुत्री, कालिंदी तट पर कान्हा की प्रिय सखी माँ बाल यमुना का श्यामल स्वरूप।"
  },
  {
    "id": "bal-shakti",
    "nameHi": "बाल शक्ति",
    "nameEn": "Little Bal Shakti",
    "category": "devi",
    "mantra": "॥ ॐ सर्वशक्तिमयी नमः ॥",
    "img": "assets/gallery/bal_shakti_little.jpg",
    "fallbackImg": "assets/gallery/bal_durga.jpg",
    "desc": "समस्त ब्रह्मांडीय ऊर्जा और दिव्यता की मूल स्रोत माँ बाल शक्ति।"
  }
]

# 3. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace window.BAL_ROOP_GALLERY in app.js
new_bal_json = "window.BAL_ROOP_GALLERY = " + json.dumps(bal_roop_dataset, ensure_ascii=False, indent=2) + ";\n"

bal_pattern = r'window\.BAL_ROOP_GALLERY\s*=\s*\[[\s\S]*?\n\];'
if re.search(bal_pattern, js):
    js = re.sub(bal_pattern, lambda m: new_bal_json, js, count=1)
    print("✓ Replaced window.BAL_ROOP_GALLERY with authentic 30 Bal Rup dataset in app.js")

# Update renderDivineGallery counter logic to remove hardcoded '60'
old_count_code = "countEl.textContent = `${filtered.length} ${tabName}`;"
new_count_code = "countEl.textContent = `✨ ${filtered.length} ${tabName} स्वरूप`;"

if old_count_code in js:
    js = js.replace(old_count_code, new_count_code)
    print("✓ Updated count badge display format in renderDivineGallery")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ app.js updated successfully!")
