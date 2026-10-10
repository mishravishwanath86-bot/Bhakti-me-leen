import os, json, sys

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🌐 BUILDING MULTI-LANGUAGE (i18n) DICTIONARIES & ENGINE")
print("======================================================================")

os.makedirs('locales', exist_ok=True)
os.makedirs('src/locales', exist_ok=True)

locales = {
  "hi": {
    "appName": "भक्ति में लीन",
    "tagline": "सनातन धर्म, ध्यान एवं आत्मिक शांति का पावन द्वार",
    "shubhaMantra": "✨ ॐ श्री गणेशाय नमः ✨",
    "nav": {
      "panchang": "पंचांग",
      "jar": "अमृत कलश",
      "home": "होम",
      "katha": "ऑडियो",
      "profile": "प्रोफ़ाइल",
      "settings": "सेटिंग्स",
      "aarti": "आरती दर्शन",
      "japMala": "जाप माला"
    },
    "home": {
      "welcome": "स्वागत है",
      "guestLogin": "अतिथि प्रवेश",
      "dailyTracker": "दैनिक साधना संज्ञान",
      "visitsToday": "आज का पावन प्रवेश",
      "times": "बार",
      "streak": "दिन स्ट्रीक",
      "streakShield": "सक्रिय कवच",
      "punyaPoints": "संचित पुण्य",
      "openSadhanaCenter": "साधना नियंत्रण कक्ष खोलें",
      "liveRadio": "24×7 लाइव भक्ति रेडियो",
      "parikrama": "दिव्य 3D मंदिर परिक्रमा",
      "amritKalash": "भक्ति अमृत कलश",
      "radioNowPlaying": "अब बज रहा है",
      "categories": "दिव्य श्रेणियां",
      "dailyPanchang": "दैनिक पंचांग",
      "shubhMuhurat": "शुभ मुहूर्त"
    },
    "categories": {
      "aarti": "आरती",
      "chalisa": "चालीसा",
      "mantra": "मंत्र",
      "stotra": "स्तोत्र",
      "vrat": "व्रत",
      "festival": "त्यौहार",
      "ramayana": "रामायण",
      "katha": "कथा",
      "desh": "देशभक्ति",
      "panchang": "पंचांग"
    },
    "settings": {
      "title": "साधना नियंत्रण व सेटिंग्स",
      "haptics": "दिव्य अनुभूति एवं हैप्टिक्स",
      "brahmaMuhurta": "अलार्म एवं ब्रह्म मुहूर्त अलर्ट",
      "bioAura": "क्वांटम बायो-एनर्जी व ऑरा",
      "vault": "साधना वॉल्ट व क्लाउड सिंक",
      "language": "भाषा चयन (Language)",
      "selectLanguage": "अपनी पसंदीदा भाषा चुनें",
      "applyLanguage": "भाषा लागू करें",
      "logout": "लॉग आउट"
    },
    "audio": {
      "title": "भक्ति ऑडियो लाइब्रेरी",
      "pureAudio": "केवल ऑडियो सुनें",
      "watchVideo": "वीडियो देखें",
      "nowPlaying": "अब बज रहा है",
      "lyrics": "पाठ एवं भावार्थ देखें"
    }
  },

  "en": {
    "appName": "Bhakti Me Leen",
    "tagline": "The Path to Divine Sadhana and Inner Peace",
    "shubhaMantra": "✨ Om Shri Ganeshaya Namah ✨",
    "nav": {
      "panchang": "Panchang",
      "jar": "Amrit Kalash",
      "home": "Home",
      "katha": "Audio",
      "profile": "Profile",
      "settings": "Settings",
      "aarti": "Aarti Darshan",
      "japMala": "Jap Mala"
    },
    "home": {
      "welcome": "Welcome to",
      "guestLogin": "Guest Entry",
      "dailyTracker": "Daily Sadhana Tracker",
      "visitsToday": "Holy visits today",
      "times": "times",
      "streak": "Day Streak",
      "streakShield": "Active Shield",
      "punyaPoints": "Punya Points",
      "openSadhanaCenter": "Open Sadhana Center",
      "liveRadio": "24×7 Live Bhakti Radio",
      "parikrama": "Divine 3D Temple Parikrama",
      "amritKalash": "Bhakti Amrit Kalash",
      "radioNowPlaying": "Now Playing",
      "categories": "Divine Categories",
      "dailyPanchang": "Daily Panchang",
      "shubhMuhurat": "Auspicious Muhurat"
    },
    "categories": {
      "aarti": "Aarti",
      "chalisa": "Chalisa",
      "mantra": "Mantra",
      "stotra": "Stotra",
      "vrat": "Vrat",
      "festival": "Festivals",
      "ramayana": "Ramayana",
      "katha": "Stories",
      "desh": "Patriotic",
      "panchang": "Panchang"
    },
    "settings": {
      "title": "Settings & Sadhana Control",
      "haptics": "Spiritual Haptics & Sound",
      "brahmaMuhurta": "Brahma Muhurta Alarm",
      "bioAura": "Pranic Aura Visualizer",
      "vault": "Sadhana Cloud Vault",
      "language": "App Language",
      "selectLanguage": "Choose Preferred Language",
      "applyLanguage": "Apply Language",
      "logout": "Log Out"
    },
    "audio": {
      "title": "Bhakti Audio Library",
      "pureAudio": "Audio Only",
      "watchVideo": "Watch Video",
      "nowPlaying": "Now Playing",
      "lyrics": "View Lyrics & Meaning"
    }
  },

  "sa": {
    "appName": "भक्ति में लीन",
    "tagline": "सनातनधर्मस्य ध्यानस्य आत्मशान्तेश्च पावनद्वारम्",
    "shubhaMantra": "✨ ॐ श्रीगणेशाय नमः ✨",
    "nav": {
      "panchang": "पञ्चाङ्गम्",
      "jar": "अमृतकलशः",
      "home": "गृहम्",
      "katha": "श्रव्यम्",
      "profile": "विवरणम्",
      "settings": "नियन्त्रणम्",
      "aarti": "आरतीदर्शनम्",
      "japMala": "जपमाला"
    },
    "home": {
      "welcome": "स्वागतम्",
      "guestLogin": "अतिथिप्रवेशः",
      "dailyTracker": "नित्यसाधनासंज्ञानम्",
      "visitsToday": "अद्यतनपावनप्रवेशः",
      "times": "वारम्",
      "streak": "दिनक्रमः",
      "streakShield": "सक्रियकवचम्",
      "punyaPoints": "पुण्याङ्काः",
      "openSadhanaCenter": "साधनानियन्त्रणकक्षमुद्घाटयतु",
      "liveRadio": "२४×७ भक्तिरेडियो",
      "parikrama": "दिव्य ३D मन्दिरपरिक्रमा",
      "amritKalash": "भक्ति-अमृतकलशः",
      "radioNowPlaying": "अधुना प्रचलति",
      "categories": "दिव्यविभागाः",
      "dailyPanchang": "दैनिकपञ्चाङ्गम्",
      "shubhMuhurat": "शुभमुहूर्तः"
    },
    "categories": {
      "aarti": "आरती",
      "chalisa": "चालीसा",
      "mantra": "मन्त्राः",
      "stotra": "स्तोत्राणि",
      "vrat": "व्रतम्",
      "festival": "उत्सवाः",
      "ramayana": "रामायणम्",
      "katha": "कथाः",
      "desh": "देशभक्तिः",
      "panchang": "पञ्चाङ्गम्"
    },
    "settings": {
      "title": "साधनानियन्त्रणं तथा विन्यासाः",
      "haptics": "दिव्यानुभूतिः हैप्टिक्स च",
      "brahmaMuhurta": "ब्राह्ममुहूर्तजागरणम्",
      "bioAura": "प्राणिक-ऊर्जा-ऑरा",
      "vault": "साधनाकोशः मेघसञ्चयः",
      "language": "भाषाचयनम् (Language)",
      "selectLanguage": "स्वाभिमतां भाषां चिनोतु",
      "applyLanguage": "भाषां प्रयोजयतु",
      "logout": "निर्गमः"
    },
    "audio": {
      "title": "भक्ति-श्रव्य-पुस्तकालयः",
      "pureAudio": "केवलं श्रव्यम्",
      "watchVideo": "दृश्यं पश्यतु",
      "nowPlaying": "अधुना प्रचलति",
      "lyrics": "पाठं भावार्थं च पश्यतु"
    }
  },

  "gu": {
    "appName": "ભક્તિ મેં લીન",
    "tagline": "સનાતન ધર્મ, ધ્યાન અને આત્મિક શાંતિનું પાવન દ્વાર",
    "shubhaMantra": "✨ ૐ શ્રી ગણેશાય નમઃ ✨",
    "nav": {
      "panchang": "પંચાંગ",
      "jar": "અમૃત કળશ",
      "home": "હોમ",
      "katha": "ઓડિયો",
      "profile": "પ્રોફાઇલ",
      "settings": "સેટિંગ્સ",
      "aarti": "આરતી દર્શન",
      "japMala": "જાપ માળા"
    },
    "home": {
      "welcome": "સ્વાગત છે",
      "guestLogin": "અતિથિ પ્રવેશ",
      "dailyTracker": "દૈનિક સાધના સંજ્ઞાન",
      "visitsToday": "આજનો પાવન પ્રવેશ",
      "times": "વખત",
      "streak": "દિવસ સ્ટ્રીક",
      "streakShield": "સક્રિય કવચ",
      "punyaPoints": "સંચિત પુણ્ય",
      "openSadhanaCenter": "સાધના નિયંત્રણ કક્ષ ખોલો",
      "liveRadio": "24×7 લાઈવ ભક્તિ રેડિયો",
      "parikrama": "દિવ્ય 3D મંદિર પરિક્રમા",
      "amritKalash": "ભક્તિ અમૃત કળશ",
      "radioNowPlaying": "હમણાં વાગી રહ્યું છે",
      "categories": "દિવ્ય શ્રેણીઓ",
      "dailyPanchang": "દૈનિક પંચાંગ",
      "shubhMuhurat": "શુભ મુહૂર્ત"
    },
    "categories": {
      "aarti": "આરતી",
      "chalisa": "ચાલીસા",
      "mantra": "મંત્ર",
      "stotra": "સ્તોત્ર",
      "vrat": "વ્રત",
      "festival": "તહેવાર",
      "ramayana": "રામાયણ",
      "katha": "કથા",
      "desh": "દેશભક્તિ",
      "panchang": "પંચાંગ"
    },
    "settings": {
      "title": "સાધના નિયંત્રણ અને સેટિંગ્સ",
      "haptics": "દિવ્ય અનુભૂતિ અને હેપ્ટિક્સ",
      "brahmaMuhurta": "બ્રહ્મ મુહૂર્ત એલાર્મ",
      "bioAura": "પ્રાણિક ઊર્જા અને ઓરા",
      "vault": "સાધના વોલ્ટ અને ક્લાઉડ સિંક",
      "language": "ભાષા પસંદગી (Language)",
      "selectLanguage": "તમારી મનપસંદ ભાષા પસંદ કરો",
      "applyLanguage": "ભાષા લાગુ કરો",
      "logout": "લોગ આઉટ"
    },
    "audio": {
      "title": "ભક્તિ ઓડિયો લાઇબ્રેરી",
      "pureAudio": "માત્ર ઓડિયો સાંભળો",
      "watchVideo": "વીડિયો જુઓ",
      "nowPlaying": "હમણાં વાગી રહ્યું છે",
      "lyrics": "પાઠ અને ભાવાર્થ જુઓ"
    }
  },

  "mr": {
    "appName": "भक्ती मध्ये लीन",
    "tagline": "सनातन धर्म, ध्यान आणि आत्मिक शांततेचे पावन द्वार",
    "shubhaMantra": "✨ ॐ श्री गणेशाय नमः ✨",
    "nav": {
      "panchang": "पंचांग",
      "jar": "अमृत कलश",
      "home": "होम",
      "katha": "ऑडिओ",
      "profile": "प्रोफाइल",
      "settings": "सेटिंग्ज",
      "aarti": "आरती दर्शन",
      "japMala": "जप माळ"
    },
    "home": {
      "welcome": "स्वागत आहे",
      "guestLogin": "अतिथी प्रवेश",
      "dailyTracker": "दैनिक साधना संज्ञान",
      "visitsToday": "आजचा पावन प्रवेश",
      "times": "वेळा",
      "streak": "दिवस सलगता",
      "streakShield": "सक्रिय कवच",
      "punyaPoints": "संचित पुण्य",
      "openSadhanaCenter": "साधना नियंत्रण कक्ष उघडा",
      "liveRadio": "24×7 लाइव्ह भक्ती रेडिओ",
      "parikrama": "दिव्य 3D मंदिर परिक्रमा",
      "amritKalash": "भक्ती अमृत कलश",
      "radioNowPlaying": "आता वाजत आहे",
      "categories": "दिव्य विभाग",
      "dailyPanchang": "दैनिक पंचांग",
      "shubhMuhurat": "शुभ मुहूर्त"
    },
    "categories": {
      "aarti": "आरती",
      "chalisa": "चालीसा",
      "mantra": "मंत्र",
      "stotra": "स्तोत्र",
      "vrat": "व्रत",
      "festival": "सण व उत्सव",
      "ramayana": "रामायण",
      "katha": "कथा",
      "desh": "देशभक्ती",
      "panchang": "पंचांग"
    },
    "settings": {
      "title": "साधना नियंत्रण आणि सेटिंग्ज",
      "haptics": "दिव्य अनुभूती व हॅप्टिक्स",
      "brahmaMuhurta": "ब्राह्म मुहूर्त अलार्म",
      "bioAura": "प्राणिक ऊर्जा व ऑरा",
      "vault": "साधना क्लाउड व्हॉल्ट",
      "language": "भाषा निवड (Language)",
      "selectLanguage": "तुमची पसंतीची भाषा निवडा",
      "applyLanguage": "भाषा लागू करा",
      "logout": "लॉग आउट"
    },
    "audio": {
      "title": "भक्ती ऑडिओ लायब्ररी",
      "pureAudio": "फक्त ऑडिओ ऐका",
      "watchVideo": "व्हिडिओ पहा",
      "nowPlaying": "आता वाजत आहे",
      "lyrics": "पाठ आणि भावार्थ पहा"
    }
  },

  "bn": {
    "appName": "Bhakti Me Leen",
    "tagline": "সনাতন ধর্ম, ধ্যান এবং আত্মিক শান্তির পবিত্র দ্বার",
    "shubhaMantra": "✨ ওঁ শ্রী গণেশায় নমঃ ✨",
    "nav": {
      "panchang": "পঞ্জিকা",
      "jar": "অমৃত কলশ",
      "home": "হোম",
      "katha": "অডিও",
      "profile": "প্রোফাইল",
      "settings": "সেটিংস",
      "aarti": "আরতি দর্শন",
      "japMala": "জপ মালা"
    },
    "home": {
      "welcome": "স্বাগতম",
      "guestLogin": "অতিথি প্রবেশ",
      "dailyTracker": "দৈনিক সাধনা ট্র্যাকার",
      "visitsToday": "আজকের পবিত্র প্রবেশ",
      "times": "বার",
      "streak": "দিন স্ট্রিক",
      "streakShield": "সক্রিয় কবচ",
      "punyaPoints": "অর্জিত পুণ্য",
      "openSadhanaCenter": "সাধনা কেন্দ্র খুলুন",
      "liveRadio": "২৪×৭ লাইভ ভক্তি রেডিও",
      "parikrama": "দিব্য ৩ডি মন্দির পরিক্রমা",
      "amritKalash": "ভক্তি অমৃত কলশ",
      "radioNowPlaying": "এখন বাজছে",
      "categories": "দিব্য বিভাগ",
      "dailyPanchang": "দৈনিক পঞ্জিকা",
      "shubhMuhurat": "শুভ মুহূর্ত"
    },
    "categories": {
      "aarti": "আরতি",
      "chalisa": "চল্লিশা",
      "mantra": "মন্ত্র",
      "stotra": "স্তোত্র",
      "vrat": "ব্রত",
      "festival": "উৎসব",
      "ramayana": "রামায়ণ",
      "katha": "কথা",
      "desh": "দেশভক্তি",
      "panchang": "পঞ্জিকা"
    },
    "settings": {
      "title": "সাধনা নিয়ন্ত্রণ ও সেটিংস",
      "haptics": "আধ্যাত্মিক হ্যাপটিক্স ও ধ্বনি",
      "brahmaMuhurta": "ব্রহ্ম মুহূর্ত অ্যালার্ম",
      "bioAura": "প্রাণিক অরা স্ক্যানার",
      "vault": "সাধনা ক্লাউড ভল্ট",
      "language": "ভাষা নির্বাচন (Language)",
      "selectLanguage": "আপনার পছন্দের ভাষা নির্বাচন করুন",
      "applyLanguage": "ভাষা প্রয়োগ করুন",
      "logout": "লগ আউট"
    },
    "audio": {
      "title": "ভক্তি অডিও লাইব্রেরি",
      "pureAudio": "শুধু অডিও শুনুন",
      "watchVideo": "ভিডিও দেখুন",
      "nowPlaying": "এখন বাজছে",
      "lyrics": "পাঠ ও ভাবার্থ দেখুন"
    }
  },

  "ta": {
    "appName": "Bhakti Me Leen",
    "tagline": "சனாதன தர்மம், தியானம் மற்றும் ஆன்மீக அமைதிக்கான புனித வாசல்",
    "shubhaMantra": "✨ ஓம் ஸ்ரீ கணேசாய நமஹ ✨",
    "nav": {
      "panchang": "பஞ்சாங்கம்",
      "jar": "அமிர்த கலசம்",
      "home": "முகப்பு",
      "katha": "ஆடியோ",
      "profile": "சுயவிவரம்",
      "settings": "அமைப்புகள்",
      "aarti": "ஆரத்தி தரிசனம்",
      "japMala": "ஜெப மாலை"
    },
    "home": {
      "welcome": "வரவேற்கிறோம்",
      "guestLogin": "விருந்தினர் நுழைவு",
      "dailyTracker": "தினசரி சாதனா டிராக்கர்",
      "visitsToday": "இன்றைய புனித வருகை",
      "times": "முறை",
      "streak": "நாள் தொடர்ச்சி",
      "streakShield": "பாதுகாப்பு கவசம்",
      "punyaPoints": "புண்ணிய புள்ளிகள்",
      "openSadhanaCenter": "சாதனா மையத்தைத் திறக்கவும்",
      "liveRadio": "24×7 நேரலை பக்தி வானொலி",
      "parikrama": "புனித 3D கோவில் பிரகார வலம்",
      "amritKalash": "பக்தி அமிர்த கலசம்",
      "radioNowPlaying": "இப்போது ஒலிக்கிறது",
      "categories": "புனித பிரிவுகள்",
      "dailyPanchang": "தினசரி பஞ்சாங்கம்",
      "shubhMuhurat": "சுப முகூர்த்தம்"
    },
    "categories": {
      "aarti": "ஆரத்தி",
      "chalisa": "சாலிசா",
      "mantra": "மந்திரம்",
      "stotra": "ஸ்தோத்திரம்",
      "vrat": "விரதம்",
      "festival": "பண்டிகைகள்",
      "ramayana": "ராமாயணம்",
      "katha": "புராணக் கதைகள்",
      "desh": "தேசபக்தி",
      "panchang": "பஞ்சாங்கம்"
    },
    "settings": {
      "title": "சாதனா அமைப்புகள் & கட்டுப்பாடு",
      "haptics": "ஆன்மீக தொடு உணர்வு & ஒலி",
      "brahmaMuhurta": "பிரம்ம முகூர்த்த எச்சரிக்கை",
      "bioAura": "பிராண ஒளிவட்டம்",
      "vault": "சாதனா கிளவுட் பெட்டகம்",
      "language": "மொழி தேர்வு (Language)",
      "selectLanguage": "உங்கள் விருப்ப மொழியைத் தேர்வுசெய்க",
      "applyLanguage": "மொழியைப் பயன்படுத்துங்கள்",
      "logout": "வெளியேறு"
    },
    "audio": {
      "title": "பக்தி ஆடியோ நூலகம்",
      "pureAudio": "ஆடியோ மட்டும்",
      "watchVideo": "வீடியோ பாருங்கள்",
      "nowPlaying": "இப்போது ஒலிக்கிறது",
      "lyrics": "பாடல் வரிகள் & பொருள்"
    }
  },

  "te": {
    "appName": "Bhakti Me Leen",
    "tagline": "సనాతన ధర్మం, ధ్యానం మరియు ఆత్మిక శాంతికి పవిత్ర ద్వారం",
    "shubhaMantra": "✨ ఓం శ్రీ గణేశాయ నమః ✨",
    "nav": {
      "panchang": "పంచాంగం",
      "jar": "అమృత కలశం",
      "home": "హోమ్",
      "katha": "ఆడియో",
      "profile": "ప్రొఫైల్",
      "settings": "సెట్టింగ్‌లు",
      "aarti": "హారతి దర్శనం",
      "japMala": "జప మాల"
    },
    "home": {
      "welcome": "స్వాగతం",
      "guestLogin": "అతిథి ప్రవేశం",
      "dailyTracker": "రోజువారీ సాధన ట్రాకర్",
      "visitsToday": "ఈ రోజు పవిత్ర ప్రవేశం",
      "times": "సార్లు",
      "streak": "రోజుల స్ట్రీక్",
      "streakShield": "రక్షణ కవచం",
      "punyaPoints": "పుణ్య పాయింట్లు",
      "openSadhanaCenter": "సాధన కేంద్రాన్ని తెరవండి",
      "liveRadio": "24×7 లైవ్ భక్తి రేడియో",
      "parikrama": "దివ్య 3D ఆలయ ప్రదక్షిణ",
      "amritKalash": "భక్తి అమృత కలశం",
      "radioNowPlaying": "ఇప్పుడు ప్లే అవుతోంది",
      "categories": "దివ్య వర్గాలు",
      "dailyPanchang": "దైనందిన పంచాంగం",
      "shubhMuhurat": "శుభ ముహూర్తం"
    },
    "categories": {
      "aarti": "హారతి",
      "chalisa": "చాలీసా",
      "mantra": "మంత్రం",
      "stotra": "స్తోత్రం",
      "vrat": "వ్రతం",
      "festival": "పండుగలు",
      "ramayana": "రామాయణం",
      "katha": "కథలు",
      "desh": "దేశభక్తి",
      "panchang": "పంచాంగం"
    },
    "settings": {
      "title": "సాధన సెట్టింగ్‌లు & నియంత్రణ",
      "haptics": "ఆధ్యాత్మిక స్పర్శ & శబ్దం",
      "brahmaMuhurta": "బ్రహ్మ ముహూర్తం అలారం",
      "bioAura": "ప్రాణ శక్తి ఆరా",
      "vault": "సాధన క్లౌడ్ వాల్ట్",
      "language": "భాష ఎంపిక (Language)",
      "selectLanguage": "మీకు నచ్చిన భాషను ఎంచుకోండి",
      "applyLanguage": "భాషను వర్తింపజేయండి",
      "logout": "లాగ్ అవుట్"
    },
    "audio": {
      "title": "భక్తి ఆడియో లైబ్రరీ",
      "pureAudio": "ఆడియో మాత్రమే",
      "watchVideo": "వీడియో చూడండి",
      "nowPlaying": "ఇప్పుడు ప్లే అవుతోంది",
      "lyrics": "పాట సాహిత్యం & అర్థం"
    }
  },

  "kn": {
    "appName": "Bhakti Me Leen",
    "tagline": "ಸನಾತನ ಧರ್ಮ, ಧ್ಯಾನ ಮತ್ತು ಆತ್ಮಿಕ ಶಾಂತಿಯ ಪವಿತ್ರ ದ್ವಾರ",
    "shubhaMantra": "✨ ಓಂ ಶ್ರೀ ಗಣೇಶಾಯ ನಮಃ ✨",
    "nav": {
      "panchang": "ಪಂಚಾಂಗ",
      "jar": "ಅಮೃತ ಕಳಶ",
      "home": "ಮುಖಪುಟ",
      "katha": "ಆಡಿಯೋ",
      "profile": "ಪ್ರೊಫೈಲ್",
      "settings": "ಸೆಟ್ಟಿಂಗ್ಸ್",
      "aarti": "ಆರತಿ ದರ್ಶನ",
      "japMala": "ಜಪ ಮಾಲೆ"
    },
    "home": {
      "welcome": "ಸ್ವಾಗತ",
      "guestLogin": "ಅತಿಥಿ ಪ್ರವೇಶ",
      "dailyTracker": "ದೈನಂದಿನ ಸಾಧನಾ ಟ್ರ್ಯಾಕರ್",
      "visitsToday": "ಇಂದಿನ ಪವಿತ್ರ ಭೇಟಿ",
      "times": "ಬಾರಿ",
      "streak": "ದಿನಗಳ ಸರಣಿ",
      "streakShield": "ರಕ್ಷಣಾ ಕವಚ",
      "punyaPoints": "ಪುಣ್ಯ ಅಂಕಗಳು",
      "openSadhanaCenter": "ಸಾಧನಾ ನಿಯಂತ್ರಣ ತೆರೆಯಿರಿ",
      "liveRadio": "24×7 ಲೈವ್ ಭಕ್ತಿ ರೇಡಿಯೋ",
      "parikrama": "ದಿವ್ಯ 3D ದೇವಾಲಯ ಪರಿಕ್ರಮ",
      "amritKalash": "ಭಕ್ತಿ ಅಮೃತ ಕಳಶ",
      "radioNowPlaying": "ಈಗ ಪ್ಲೇ ಆಗುತ್ತಿದೆ",
      "categories": "ದಿವ್ಯ ವರ್ಗಗಳು",
      "dailyPanchang": "ದೈನಂದಿನ ಪಂಚಾಂಗ",
      "shubhMuhurat": "ಶುಭ ಮುಹೂರ್ತ"
    },
    "categories": {
      "aarti": "ಆರತಿ",
      "chalisa": "ಚಾಲೀಸಾ",
      "mantra": "ಮಂತ್ರ",
      "stotra": "ಸ್ತೋತ್ರ",
      "vrat": "ವ್ರತ",
      "festival": "ಹಬ್ಬಗಳು",
      "ramayana": "ರಾಮಾಯಣ",
      "katha": "ಕಥೆಗಳು",
      "desh": "ದೇಶಭಕ್ತಿ",
      "panchang": "ಪಂಚಾಂಗ"
    },
    "settings": {
      "title": "ಸಾಧನಾ ನಿಯಂತ್ರಣ ಮತ್ತು ಸೆಟ್ಟಿಂಗ್ಸ್",
      "haptics": "ಆಧ್ಯಾತ್ಮಿಕ ಸ್ಪರ್ಶ ಮತ್ತು ಧ್ವನಿ",
      "brahmaMuhurta": "ಬ್ರಾಹ್ಮೀ ಮುಹೂರ್ತ ಅಲಾರಾಂ",
      "bioAura": "ಪ್ರಾಣ ಶಕ್ತಿ ಔರಾ",
      "vault": "ಸಾಧನಾ ಕ್ಲೌಡ್ ವಾಲ್ಟ್",
      "language": "ಭಾಷೆ ಆಯ್ಕೆ (Language)",
      "selectLanguage": "ನಿಮ್ಮ ಮೆಚ್ಚಿನ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
      "applyLanguage": "ಭಾಷೆ ಅನ್ವಯಿಸಿ",
      "logout": "ಲಾಗ್ ಔಟ್"
    },
    "audio": {
      "title": "ಭಕ್ತಿ ಆಡಿಯೋ ಲೈಬ್ರರಿ",
      "pureAudio": "ಆಡಿಯೋ ಮಾತ್ರ",
      "watchVideo": "ವೀಡಿಯೊ ವೀಕ್ಷಿಸಿ",
      "nowPlaying": "ಈಗ ಪ್ಲೇ ಆಗುತ್ತಿದೆ",
      "lyrics": "ಸಾಹಿತ್ಯ ಮತ್ತು ಭಾವಾರ್ಥ"
    }
  }
}

# Write to both locales/ and src/locales/
for lang_code, data in locales.items():
    p1 = f'locales/{lang_code}.json'
    p2 = f'src/locales/{lang_code}.json'
    
    with open(p1, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(p2, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Created {p1} and {p2}")

print("✓ All 9 locale dictionaries created successfully!")
