import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('full_drik_aarti_collections.json', 'r', encoding='utf-8') as f:
    colls = json.load(f)

# Build granular deity categories as requested by user
granular = {}

# 1. Ganesh
granular['ganesh'] = colls['ganesh']

# 2. Hanuman
granular['hanuman'] = colls['hanuman']

# 3. Krishna
granular['krishna'] = colls['krishna']

# 4. Rama
granular['rama'] = colls['rama']

# 5. Shiva
granular['shiva'] = colls['shiva']

# 6. Narayana
granular['narayana'] = colls['narayana']

# 7. Durga
goddesses_items = colls['goddesses']['items']
durga_items = [i for i in goddesses_items if any(k in i['title'].lower() or k in i['hi_line'] for k in ['ambe', 'durga', 'vaishno', 'parvati', 'vindhyeshwari', 'kali', 'lalita', 'bagalamukhi', 'shakambhari'])]
granular['durga'] = {
    "key": "durga",
    "title": "माँ दुर्गा व अम्बे आरती संग्रह",
    "title_en": "Durga Mata Aarti",
    "deity": "माँ दुर्गा भवानी",
    "img": "assets/gallery/bal_durga.jpg",
    "fallbackImg": "assets/deity_durga.jpg",
    "mantra": "॥ सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके ॥",
    "sub": "अम्बे गौरी • जगदम्बे काली • वैष्णो देवी",
    "items": durga_items[:5] if len(durga_items) >= 5 else durga_items
}

# 8. Lakshmi
lakshmi_items = [i for i in goddesses_items if any(k in i['title'].lower() or k in i['hi_line'] for k in ['lakshmi', 'लक्ष्मी', 'ahoi', 'अहोई', 'ekadashi', 'एकादशी', 'annapurna', 'अन्नपूर्णा'])]
granular['lakshmi'] = {
    "key": "lakshmi",
    "title": "माँ लक्ष्मी आरती संग्रह",
    "title_en": "Lakshmi Mata Aarti",
    "deity": "महालक्ष्मी माता",
    "img": "assets/deity_lakshmi.jpg",
    "fallbackImg": "assets/deity_lakshmi.jpg",
    "mantra": "॥ ॐ श्रीं ह्रीं क्लीं श्री सिद्ध लक्ष्म्यै नमः ॥",
    "sub": "महालक्ष्मी • वैभव लक्ष्मी • अहोई माता",
    "items": lakshmi_items
}

# 9. Saraswati
saraswati_items = [i for i in goddesses_items if any(k in i['title'].lower() or k in i['hi_line'] for k in ['saraswati', 'सरस्वती', 'sharda', 'शारदा'])]
granular['saraswati'] = {
    "key": "saraswati",
    "title": "माँ सरस्वती आरती संग्रह",
    "title_en": "Saraswati Mata Aarti",
    "deity": "विद्यादायिनी माँ सरस्वती",
    "img": "assets/deity_saraswati.jpg",
    "fallbackImg": "assets/deity_saraswati.jpg",
    "mantra": "॥ ॐ ऐं सरस्वत्यै नमः ॥",
    "sub": "सरस्वती माता • मैया शारदा मैहर",
    "items": saraswati_items
}

# 10. Surya
gods_items = colls['gods']['items']
surya_items = [i for i in gods_items if any(k in i['title'].lower() or k in i['hi_line'] for k in ['surya', 'सूर्य', 'kashyap', 'कश्यप', 'brahma', 'ब्रह्मा', 'parashu', 'परशु'])]
granular['surya'] = {
    "key": "surya",
    "title": "श्री सूर्य देव व नवग्रह आरती",
    "title_en": "Surya Dev Aarti",
    "deity": "भगवान सूर्य नारायण",
    "img": "assets/gallery/bal_surya_little.jpg",
    "fallbackImg": "assets/deity_surya.jpg",
    "mantra": "॥ ॐ सूर्याय नमः • ॐ आदित्याय नमः ॥",
    "sub": "कश्यप नन्दन • सूर्य भगवान • नवग्रह",
    "items": surya_items
}

# 11. Shanidev
shani_items = [i for i in gods_items if 'shani' in i['title'].lower() or 'शनि' in i['hi_line']]
granular['shanidev'] = {
    "key": "shanidev",
    "title": "भगवान शनिदेव आरती संग्रह",
    "title_en": "Shanidev Aarti",
    "deity": "न्यायदेव भगवान शनिदेव",
    "img": "assets/deity_shanidev.jpg",
    "fallbackImg": "assets/deity_shanidev.jpg",
    "mantra": "॥ ॐ शं शनैश्चराय नमः ॥",
    "sub": "जय जय शनिदेव • कर्मफल दाता",
    "items": shani_items
}

# 12. Khatu Shyam
sants_items = colls['sants']['items']
shyam_items = [i for i in sants_items if 'shyam' in i['title'].lower() or 'श्याम' in i['hi_line']]
granular['khatushyam'] = {
    "key": "khatushyam",
    "title": "खाटू श्याम जी आरती संग्रह",
    "title_en": "Khatu Shyam Aarti",
    "deity": "हारे का सहारा बाबा श्याम",
    "img": "assets/deity_khatushyam.jpg",
    "fallbackImg": "assets/deity_khatushyam.jpg",
    "mantra": "॥ ॐ श्री श्याम देवाय नमः ॥",
    "sub": "ॐ जय श्री श्याम हरे • लखदातार",
    "items": shyam_items
}

# 13. Ganga & Rivers
ganga_items = [i for i in goddesses_items if any(k in i['title'].lower() or k in i['hi_line'] for k in ['ganga', 'गंगा', 'bhagirath', 'yamuna', 'यमुना', 'narmada', 'नर्मदा'])]
granular['ganga'] = {
    "key": "ganga",
    "title": "माँ गंगा व पवित्र नदियां आरती",
    "title_en": "Ganga & Sacred Rivers Aarti",
    "deity": "मोक्षदायिनी माँ गंगा",
    "img": "assets/deity_ganga.jpg",
    "fallbackImg": "assets/deity_ganga.jpg",
    "mantra": "॥ ॐ नमो भगवत्यै गङ्गायै नमः ॥",
    "sub": "जय गंगे माता • भगीरथी • यमुना जी",
    "items": ganga_items
}

# 14. Bhairav
bhairav_items = [i for i in gods_items if 'bhairav' in i['title'].lower() or 'भैरव' in i['hi_line']]
granular['bhairav'] = {
    "key": "bhairav",
    "title": "श्री कालभैरव व बटुक भैरव आरती",
    "title_en": "Bhairav Baba Aarti",
    "deity": "काशी के कोतवाल भैरव बाबा",
    "img": "assets/deity_bhairav.jpg",
    "fallbackImg": "assets/deity_bhairav.jpg",
    "mantra": "॥ ॐ भ्रं भैरवाय नमः ॥",
    "sub": "भैरव लाड़िले • बटुक भैरव देवा",
    "items": bhairav_items
}

# 15. Gayatri & Tulasi
gayatri_items = [i for i in goddesses_items if any(k in i['title'].lower() or k in i['hi_line'] for k in ['gayatri', 'गायत्री', 'tulasi', 'तुलसी', 'gau', 'गैया', 'shitala', 'शीतला'])]
granular['gayatri'] = {
    "key": "gayatri",
    "title": "माँ गायत्री व तुलसी आरती",
    "title_en": "Gayatri & Tulasi Aarti",
    "deity": "वेदमाता गायत्री व तुलसी महारानी",
    "img": "assets/deity_gayatri.jpg",
    "fallbackImg": "assets/deity_gayatri.jpg",
    "mantra": "॥ ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यम् ॥",
    "sub": "गायत्री जी • तुलसी माता • गौ माता",
    "items": gayatri_items
}

# 16. Radha Rani
radha_items = [i for i in goddesses_items if any(k in i['title'].lower() or k in i['hi_line'] for k in ['radha', 'राधा', 'vrishbhanu', 'वृषभानु'])]
granular['radha'] = {
    "key": "radha",
    "title": "श्री राधा रानी आरती संग्रह",
    "title_en": "Radha Rani Aarti",
    "deity": "श्री राधा वृषभानु नंदिनी",
    "img": "assets/deity_radharani.jpg",
    "fallbackImg": "assets/gallery/bal_krishna_little.jpg",
    "mantra": "॥ ॐ ह्रीं श्रीं राधिकायै नमः ॥",
    "sub": "वृषभानुसुता • वृषभानुलली आरती",
    "items": radha_items
}

# 17. Sants & Gurus
other_sants = [i for i in sants_items if 'shyam' not in i['title'].lower() and 'श्याम' not in i['hi_line']]
granular['sants'] = {
    "key": "sants",
    "title": "सन्त व लोकदेवता आरती संग्रह",
    "title_en": "Sants & Lokdevta Aarti",
    "deity": "शिर्डी साईं • बाबा रामदेव • संतजन",
    "img": "assets/deity_saibaba.jpg",
    "fallbackImg": "assets/deity_saibaba.jpg",
    "mantra": "॥ ॐ श्री साईं नाथाय नमः ॥",
    "sub": "साईं गुरुवर • रामदेव स्वामी • रविदास",
    "items": other_sants
}

# 18. Ramayan & Gita & Devas
gita_items = colls['other']['items'] + [i for i in gods_items if any(k in i['title'].lower() or k in i['hi_line'] for k in ['ramayan', 'रामायण', 'kubera', 'कुबेर', 'dhanvantari', 'धन्वन्तरि', 'vishwakarma', 'विश्वकर्मा', 'chitragupta', 'चित्रगुप्त', 'narsingh', 'नरसिंह'])]
granular['gita'] = {
    "key": "gita",
    "title": "श्री रामायण, गीता व देव स्तुति",
    "title_en": "Ramayana & Gita Aarti",
    "deity": "श्री रामायण जी व श्रीमद्भगवद्गीता",
    "img": "assets/gallery/bal_rama.jpg",
    "fallbackImg": "assets/deity_ram.jpg",
    "mantra": "॥ नमो भगवते वासुदेवाय • जय श्री राम ॥",
    "sub": "रामायण जी • भगवद् गीता • कुबेर • धन्वन्तरि",
    "items": gita_items
}

# Also keep full collections for Gods & Goddesses
granular['gods'] = colls['gods']
granular['goddesses'] = colls['goddesses']

print(f"Built {len(granular)} total categories!")
for k, v in granular.items():
    print(f"  • {k} ({v['title']}): {len(v['items'])} items")

with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(granular, f, ensure_ascii=False, indent=2)

print("\n✓ Saved to final_granular_aarti_collections.json")
