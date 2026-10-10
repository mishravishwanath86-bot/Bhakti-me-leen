import os, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

# Deity point configurations with authentic gallery thumbnails and mantras
DEITY_CONFIG = {
    'hanuman': {
        'title': 'श्री हनुमान चालीसा संग्रह',
        'title_en': 'Shri Hanuman Chalisa',
        'deity': 'संकटमोचन श्री हनुमान जी महाराज',
        'img': 'assets/gallery/bal_hanuman.jpg',
        'fallbackImg': 'assets/deity_hanuman.jpg',
        'mantra': '॥ ॐ हं हनुमते रुद्रात्मकाय हुं फट् ॥',
        'sub': 'संकट मोचन • बल-बुद्धि-विद्या • अष्टसिद्धि नौ निधि के दाता',
        'slugs': ['shree-hanuman-chalisa', 'shri-bajarang-baan', 'shri-balaji-chalisa']
    },
    'ganesh': {
        'title': 'श्री गणेश चालीसा संग्रह',
        'title_en': 'Shri Ganesha Chalisa',
        'deity': 'विघ्नहर्ता श्री गणेश जी महाराज',
        'img': 'assets/gallery/bal_ganesha_little.jpg',
        'fallbackImg': 'assets/deity_ganesh.jpg',
        'mantra': '॥ वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ ॥',
        'sub': 'विघ्न विनाशक • प्रथम पूज्य • रिद्धि-सिद्धि के दाता',
        'slugs': ['shree-ganesha-chalisa']
    },
    'shiva': {
        'title': 'भगवान शिव चालीसा संग्रह',
        'title_en': 'Lord Shiva Chalisa',
        'deity': 'देवाधिदेव महादेव भगवान शिव',
        'img': 'assets/gallery/bal_shiva.jpg',
        'fallbackImg': 'assets/deity_shiv.jpg',
        'mantra': '॥ ॐ नमः शिवाय • ॐ त्र्यम्बकं यजामहे ॥',
        'sub': 'महामृत्युंजय • पशुपतिनाथ • आशुतोष कृपालु',
        'slugs': ['shiva-chalisa']
    },
    'krishna': {
        'title': 'श्री कृष्ण चालीसा संग्रह',
        'title_en': 'Shri Krishna Chalisa',
        'deity': 'आनन्दकन्द भगवान श्री कृष्ण',
        'img': 'assets/gallery/bal_krishna.jpg',
        'fallbackImg': 'assets/deity_krishna.jpg',
        'mantra': '॥ ॐ नमो भगवते वासुदेवाय • हरे कृष्ण ॥',
        'sub': 'गोपाल • गिरिराजधारी • भक्त वत्सल श्याम सुंदर',
        'slugs': ['shree-krishna-chalisa', 'shri-gopala-chalisa', 'shri-giriraj-chalisa']
    },
    'rama': {
        'title': 'श्री राम चालीसा संग्रह',
        'title_en': 'Shri Rama Chalisa',
        'deity': 'मर्यादा पुरुषोत्तम भगवान श्री राम',
        'img': 'assets/gallery/bal_rama_little.jpg',
        'fallbackImg': 'assets/deity_ram.jpg',
        'mantra': '॥ ॐ श्री रामाय नमः • श्री राम जय राम जय जय राम ॥',
        'sub': 'रघुकुल तिलक • धनुर्धारी • भक्त हितकारी',
        'slugs': ['shree-rama-chalisa', 'shri-parashurama-chalisa', 'shri-ramdev-chalisa']
    },
    'durga': {
        'title': 'माँ दुर्गा चालीसा संग्रह',
        'title_en': 'Maa Durga Chalisa',
        'deity': 'जगज्जननी माँ दुर्गा भवानी',
        'img': 'assets/gallery/bal_durga_little.jpg',
        'fallbackImg': 'assets/deity_durga.jpg',
        'mantra': '॥ ॐ दुं दुर्गायै नमः • सर्वमंगल मांगल्ये ॥',
        'sub': 'सिंहवाहिनी • अष्टभुजा • शक्ति स्वरूपा',
        'slugs': ['durga-mata-chalisa', 'vindhyeshwari-mata-chalisa', 'shakambhari-mata-chalisa']
    },
    'lakshmi': {
        'title': 'माँ लक्ष्मी चालीसा संग्रह',
        'title_en': 'Maa Lakshmi Chalisa',
        'deity': 'धन-धान्य प्रदायिनी माँ महालक्ष्मी',
        'img': 'assets/gallery/bal_lakshmi_little.jpg',
        'fallbackImg': 'assets/deity_lakshmi.jpg',
        'mantra': '॥ ॐ श्रीं ह्रीं श्रीं कमले कमलालये प्रसीद ॥',
        'sub': 'अष्टलक्ष्मी • कमलासना • वैभव व समृद्धि दायिनी',
        'slugs': ['lakshmi-mata-chalisa', 'mahalakshmi-mata-chalisa']
    },
    'saraswati': {
        'title': 'माँ सरस्वती चालीसा संग्रह',
        'title_en': 'Maa Saraswati Chalisa',
        'deity': 'विद्या-बुद्धि दायिनी माँ सरस्वती',
        'img': 'assets/gallery/bal_saraswati_little.jpg',
        'fallbackImg': 'assets/deity_saraswati.jpg',
        'mantra': '॥ ॐ ऐं सरस्वत्यै नमः • या कुन्देन्दुतुषारहारधवला ॥',
        'sub': 'वीणावादिनी • हंसवाहिनी • ज्ञान व वाणी प्रदात्री',
        'slugs': ['saraswati-mata-chalisa', 'sharda-mata-chalisa']
    },
    'surya': {
        'title': 'श्री सूर्य देव व नवग्रह चालीसा',
        'title_en': 'Surya Deva & Navagraha Chalisa',
        'deity': 'प्रत्यक्ष देवता भुवन-भास्कर सूर्य देव',
        'img': 'assets/gallery/bal_surya_little.jpg',
        'fallbackImg': 'assets/gallery/bal_surya_little.jpg',
        'mantra': '॥ ॐ सूर्याय नमः • ॐ घृणि सूर्याय नमः ॥',
        'sub': 'तेजोमय • नवग्रह अधिपति • आरोग्यता व ओज प्रदाता',
        'slugs': ['surya-deva-chalisa', 'navagraha-chalisa']
    },
    'shani': {
        'title': 'भगवान शनिदेव चालीसा संग्रह',
        'title_en': 'Lord Shanidev Chalisa',
        'deity': 'कर्मफलदाता भगवान श्री शनिदेव',
        'img': 'assets/deity_shanidev.jpg',
        'fallbackImg': 'assets/deity_shanidev.jpg',
        'mantra': '॥ ॐ शं शनैश्चराय नमः • नीलांजन समाभासं ॥',
        'sub': 'न्यायाधीश • सूर्यपुत्र • संकट हर्ता कृपा सिंधु',
        'slugs': ['shani-dev-chalisa', 'shani-dev-chalisa-other']
    },
    'khatushyam': {
        'title': 'खाटू श्याम चालीसा संग्रह',
        'title_en': 'Khatu Shyam Chalisa',
        'deity': 'हारे का सहारा लखदातारी श्याम बाबा',
        'img': 'assets/deity_khatushyam.jpg',
        'fallbackImg': 'assets/deity_khatushyam.jpg',
        'mantra': '॥ ॐ श्री श्याम देवाय नमः • ॐ मोर्वी नन्दनाय नमः ॥',
        'sub': 'शीश के दानी • कलियुग अवतारी • तीन बाण धारी',
        'slugs': ['shri-shyam-chalisa']
    },
    'ganga': {
        'title': 'माँ गंगा व पवित्र नदियां चालीसा',
        'title_en': 'Maa Ganga & Holy Rivers Chalisa',
        'deity': 'पतित-पावनी मोक्षदायिनी माँ गंगा',
        'img': 'assets/gallery/bal_ganga_little.jpg',
        'fallbackImg': 'assets/deity_ganga.jpg',
        'mantra': '॥ ॐ नमो गंगायै विश्वरूपिण्यै शिवानन्दायै नमः ॥',
        'sub': 'त्रिपथगा • भगीरथनन्दिनी • अमरत्व व पापनाशिनी',
        'slugs': ['ganga-mata-chalisa', 'narmada-mata-chalisa']
    },
    'bhairav': {
        'title': 'श्री कालभैरव व बटुक भैरव चालीसा',
        'title_en': 'Lord Bhairava Chalisa',
        'deity': 'रुद्रावतार श्री कालभैरव व बटुक भैरव',
        'img': 'assets/gallery/bal_bhairav_little.jpg',
        'fallbackImg': 'assets/gallery/bal_bhairav_little.jpg',
        'mantra': '॥ ॐ भ्रं भैरवाय नमः • ॐ बटुक भैरवाय नमः ॥',
        'sub': 'काशी के कोतवाल • भयभंजन • रक्षा कवच प्रदाता',
        'slugs': ['shri-batuka-bhairava-chalisa', 'shri-bhairava-chalisa']
    },
    'gayatri': {
        'title': 'माँ गायत्री व तुलसी चालीसा',
        'title_en': 'Maa Gayatri & Tulasi Chalisa',
        'deity': 'वेदमाता गायत्री व माँ तुलसी भगवती',
        'img': 'assets/gallery/bal_gayatri_little.jpg',
        'fallbackImg': 'assets/gallery/bal_tulsi_little.jpg',
        'mantra': '॥ ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि ॥',
        'sub': 'वेदमाता • सद्बुद्धि प्रदायिनी • हरिप्रिया तुलसी',
        'slugs': ['gayatri-mata-chalisa', 'tulasi-mata-chalisa']
    },
    'radha': {
        'title': 'श्री राधा रानी चालीसा संग्रह',
        'title_en': 'Shri Radha Rani Chalisa',
        'deity': 'ह्लादिनी महाशक्ति श्री राधा रानी',
        'img': 'assets/gallery/bal_radha_little.jpg',
        'fallbackImg': 'assets/gallery/bal_radha_little.jpg',
        'mantra': '॥ ॐ श्री राधायै नमः • राधे राधे जय श्री राधे ॥',
        'sub': 'वृषभानुनन्दिनी • निकुंजेश्वरी • प्रेमरूपा किशोरी जी',
        'slugs': ['shri-radha-chalisa']
    },
    'vishnu': {
        'title': 'श्री विष्णु, ब्रह्मा व नृसिंह चालीसा',
        'title_en': 'Lord Vishnu, Brahma & Narasimha Chalisa',
        'deity': 'जगतपालक श्री हरि विष्णु भगवान',
        'img': 'assets/gallery/bal_vishnu_little.jpg',
        'fallbackImg': 'assets/deity_vishnu.jpg',
        'mantra': '॥ ॐ नमो नारायणाय • ॐ विष्णवे नमः ॥',
        'sub': 'वैकुण्ठनाथ • चतुर्भुज • भक्त रक्षक नृसिंह भगवान',
        'slugs': ['shri-vishnu-chalisa', 'shri-brahma-chalisa']
    },
    'devi': {
        'title': 'दिव्य देवी माता चालीसा संग्रह',
        'title_en': 'Divine Goddesses Chalisa',
        'deity': 'समस्त दिव्य मातृशक्तियां',
        'img': 'assets/gallery/bal_parvati_little.jpg',
        'fallbackImg': 'assets/gallery/bal_shakti_little.jpg',
        'mantra': '॥ या देवी सर्वभूतेषु मातृ-रूपेण संस्थिता ॥',
        'sub': 'पार्वती • काली • वैष्णो • संतोषी • बगलामुखी • अन्नपूर्णा',
        'slugs': ['parvati-mata-chalisa', 'kali-mata-chalisa', 'mahakali-mata-chalisa', 'lalita-mata-chalisa', 'shitala-mata-chalisa', 'vaishno-mata-chalisa', 'bagalamukhi-mata-chalisa', 'annapurna-mata-chalisa']
    },
    'sants': {
        'title': 'सन्त, लोकदेवता व गीता चालीसा',
        'title_en': 'Saints, Folk Deities & Gita Chalisa',
        'deity': 'सिद्ध सन्त, लोकदेवता एवं श्रीमद्भगवद्गीता',
        'img': 'assets/deity_saibaba.jpg',
        'fallbackImg': 'assets/gallery/bal_kubera_little.jpg',
        'mantra': '॥ ॐ श्री सद्गुरुवे नमः • ॐ गीतायै नमः ॥',
        'sub': 'कुबेर • विश्वकर्मा • साईं बाबा • रविदास • गोरखनाथ • गीता',
        'slugs': ['shri-kubera-chalisa', 'shri-vishwakarma-chalisa', 'sai-baba-chalisa', 'shri-ravidas-chalisa', 'shri-gorakha-chalisa', 'shri-jaharveer-chalisa', 'shri-mahavir-chalisa', 'shri-pretraj-chalisa', 'shri-baba-gangaram-chalisa', 'shri-rani-sati-chalisa', 'shri-pitar-chalisa', 'gita-chalisa']
    }
}

print("Deity config defined with", len(DEITY_CONFIG), "points!")
