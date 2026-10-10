import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

rich_quiz_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🎯 COMPLETE SACRED MCQ QUIZ ENGINE (120s Timer + TTS + Theme + WhatsApp)
// ══════════════════════════════════════════════════════════════════════════════

window.currentQuizCategory = 'india';
window.currentQuizIndex = 0;
window.quizScore = 0;
window.quizHighScore = parseInt(localStorage.getItem('sanatan_quiz_high_score') || '0', 10);
window.isQuizAnswered = false;
window.quizTimerInterval = null;
window.quizSecondsLeft = 120;
window.isQuizLightMode = localStorage.getItem('sanatan_quiz_theme') === 'light';

// 📚 EXPANDED RICH 10-QUESTION DECKS PER CATEGORY
window.QUIZ_DECK = {
  india: [
    {
      q: 'विश्व में 1200 से अधिक नक्काशीदार खंभों वाला सबसे लंबा गलियारा किस मंदिर में है?',
      opts: ['मीनाक्षी अम्मन मंदिर, मदुरै', 'बृहदीश्वर मंदिर, तंजावुर', 'रामनाथस्वामी मंदिर, रामेश्वरम', 'जगन्नाथ मंदिर, पुरी'],
      correct: 2,
      desc: 'रामेश्वरम का रामनाथस्वामी मंदिर 1,220 मीटर लंबे विश्व के सबसे भव्य खंभों वाले गलियारे के लिए प्रसिद्ध है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Ramanathaswamy+Temple+Rameswaram'
    },
    {
      q: 'विश्व प्रसिद्ध भस्म आरती भारत के किस पावन ज्योतिर्लिंग में नित्य प्रातः की जाती है?',
      opts: ['काशी विश्वनाथ', 'महाकालेश्वर (उज्जैन)', 'केदारनाथ', 'सोमनाथ'],
      correct: 1,
      desc: 'उज्जैन के महाकालेश्वर ज्योतिर्लिंग में नित्य ब्रह्म मुहूर्त में भगवान शिव की दिव्य भस्म आरती होती है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Mahakaleshwar+Temple+Ujjain'
    },
    {
      q: 'भारत का कौन सा पावन धाम है जहाँ भगवान जगन्नाथ, बलभद्र और सुभद्रा जी के काष्ठ विग्रह प्रतिष्ठित हैं?',
      opts: ['द्वारकाधीश मंदिर', 'श्री जगन्नाथ मंदिर, पुरी', 'बद्रीनाथ धाम', 'तिरुपति बालाजी'],
      correct: 1,
      desc: 'पुरी का श्री जगन्नाथ मंदिर चार धामों में से एक है, जहाँ नीम की पवित्र काष्ठ (दारु ब्रह्म) से विग्रह बनाए जाते हैं।',
      map: 'https://www.google.com/maps/search/?api=1&query=Jagannath+Temple+Puri'
    },
    {
      q: 'किस पावन मंदिर का प्रसाद रसोई विश्व की सबसे बड़ी रसोई मानी जाती है जिसे आनंद बाज़ार कहते हैं?',
      opts: ['स्वर्ण मंदिर', 'जगन्नाथ पुरी', 'तिरुपति वेंकटेश्वर', 'वैष्णो देवी'],
      correct: 1,
      desc: 'जगन्नाथ पुरी के आनंद बाज़ार में मिट्टी के सात बरतनों को एक के ऊपर एक रखकर केवल काष्ठ की अग्नि से महाप्रसाद पकता है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Jagannath+Puri+Kitchen'
    },
    {
      q: 'उत्तराखंड के चार धामों में सबसे ऊँचाई पर स्थित भगवान शिव का ज्योतिर्लिंग कौन सा है?',
      opts: ['तुंगनाथ', 'केदारनाथ', 'रुद्रनाथ', 'मध्यमहेश्वर'],
      correct: 1,
      desc: 'केदारनाथ धाम 3,583 मीटर की ऊँचाई पर मंदाकिनी नदी के तट पर स्थित द्वादश ज्योतिर्लिंगों में पंचम ज्योतिर्लिंग है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Kedarnath+Temple'
    },
    {
      q: 'द्रविड़ स्थापत्य कला का अनुपम उदाहरण "हवाई जहाज जैसा गोपुरम" किस मंदिर की पहचान है?',
      opts: ['मीनाक्षी सुंदरेश्वर मंदिर', 'बृहदीश्वर मंदिर', 'रंगनाथस्वामी मंदिर, श्रीरंगम', 'पद्मनाभस्वामी मंदिर'],
      correct: 2,
      desc: 'श्रीरंगम का रंगनाथस्वामी मंदिर 156 एकड़ में फैला भारत का सबसे विशाल क्रियाशील मंदिर परिसर है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Sri+Ranganathaswamy+Temple+Srirangam'
    },
    {
      q: 'माँ कामाख्या का प्रसिद्ध शक्तिपीठ जहाँ प्रतिवर्ष पावन अंबुवाची मेला लगता है, किस पर्वत पर स्थित है?',
      opts: ['नीलांचल पर्वत (गुवाहाटी)', 'त्रिकूट पर्वत', 'विंध्याचल पर्वत', 'गिरनार पर्वत'],
      correct: 0,
      desc: 'असम के गुवाहाटी में नीलांचल पर्वत पर स्थित माँ कामाख्या मंदिर 51 महाशक्तिपीठों का सर्वोच्च केंद्र है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Kamakhya+Temple+Guwahati'
    },
    {
      q: 'विश्व प्रसिद्ध सोमनाथ ज्योतिर्लिंग भारत के किस राज्य के सौराष्ट्र क्षेत्र में स्थित है?',
      opts: ['महाराष्ट्र', 'गुजरात', 'राजस्थान', 'मध्य प्रदेश'],
      correct: 1,
      desc: 'गुजरात के प्रभास पाटन में स्थित सोमनाथ मंदिर को प्रथम ज्योतिर्लिंग माना जाता है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Somnath+Temple+Gujarat'
    },
    {
      q: 'भगवान वेंकटेश्वर (तिरुपति बालाजी) का मंदिर किस पवित्र पर्वत श्रृंखला पर स्थित है?',
      opts: ['मलयगिरि', 'शेषाचलम पहाड़ियाँ (सप्तगिरि)', 'अन्नामलाई', 'नीलगिरि'],
      correct: 1,
      desc: 'आंध्र प्रदेश की शेषाचलम पर्वतमाला के सात शिखरों (सप्तगिरि) में वैंकटाद्रि पर बालाजी का दिव्य मंदिर है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Tirupati+Balaji+Temple'
    },
    {
      q: 'अयोध्या में नवनिर्मित भव्य राम जन्मभूमि मंदिर किस पारंपरिक स्थापत्य शैली में निर्मित है?',
      opts: ['द्रविड़ शैली', 'नागर शैली', 'वेसर शैली', 'कलिंग शैली'],
      correct: 1,
      desc: 'प्रभु श्री राम का भव्य मंदिर उत्तर भारतीय नागर स्थापत्य शैली के शास्त्रसम्मत नियमों के अनुसार बंसी पहाड़पुर के बलुआ पत्थरों से बना है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Ram+Mandir+Ayodhya'
    }
  ],
  world: [
    {
      q: 'कम्बोडिया में स्थित विश्व का सबसे बड़ा हिन्दू मंदिर परिसर कौन सा है?',
      opts: ['प्रम्बानन मंदिर', 'अंगकोर वाट', 'पशुपतिनाथ', 'बाटू गुफाएं'],
      correct: 1,
      desc: 'अंगकोर वाट 12वीं सदी में सूर्यवर्मन द्वितीय द्वारा भगवान विष्णु को समर्पित विश्व का सबसे विशाल मंदिर परिसर है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Angkor+Wat+Cambodia'
    },
    {
      q: 'नेपाल की राजधानी काठमांडू में बागमती नदी के तट पर स्थित भगवान शिव का पावन मंदिर कौन सा है?',
      opts: ['मुक्तिनाथ', 'पशुपतिनाथ मंदिर', 'जानकी मंदिर', 'गुह्येश्वरी'],
      correct: 1,
      desc: 'पशुपतिनाथ मंदिर नेपाल का सबसे पवित्र हिंदू तीर्थस्थल है जो यूनेस्को विश्व धरोहर में शामिल है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Pashupatinath+Temple+Kathmandu'
    },
    {
      q: 'इंडोनेशिया के जावा द्वीप पर स्थित 9वीं शताब्दी का सबसे भव्य त्रिमूर्ति शिव मंदिर कौन सा है?',
      opts: ['प्रम्बानन मंदिर', 'तनाह लोट', 'बेसाकिह मंदिर', 'उलुन दानु'],
      correct: 0,
      desc: 'प्रम्बानन मंदिर इंडोनेशिया का सबसे बड़ा हिंदू मंदिर परिसर है जो ब्रह्मा, विष्णु और महेश को समर्पित है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Prambanan+Temple+Indonesia'
    },
    {
      q: 'मलेशिया में 140 फीट ऊँची भगवान मुरुगन (कार्तिकेय) की स्वर्ण प्रतिमा किस पावन गुफा के बाहर स्थित है?',
      opts: ['बाटू गुफाएं (Batu Caves)', 'गुआ गोमंतोंग', 'मुरीद गुफा', 'कैनिंग गुफा'],
      correct: 0,
      desc: 'मलेशिया के कुआलालंपुर में बाटू गुफाएं भगवान मुरुगन का विश्व प्रसिद्ध तीर्थ स्थल हैं।',
      map: 'https://www.google.com/maps/search/?api=1&query=Batu+Caves+Malaysia'
    },
    {
      q: 'अमेरिका के न्यू जर्सी में नवनिर्मित विश्व का दूसरा सबसे विशाल हिंदू मंदिर कौन सा है?',
      opts: ['स्वामीनारायण अक्षरधाम मंदिर (रॉबिंसविले)', 'श्री शिव विष्णु मंदिर', 'मीनाक्षी मंदिर ह्यूस्टन', 'राधा कृष्ण मंदिर'],
      correct: 0,
      desc: 'न्यू जर्सी का अक्षरधाम महामंदिर 183 एकड़ में प्राचीन शिल्पशास्त्र और 10,000 मूर्तियों के साथ निर्मित है।',
      map: 'https://www.google.com/maps/search/?api=1&query=BAPS+Swaminarayan+Akshardham+New+Jersey'
    },
    {
      q: 'श्रीलंका में स्थित "मुन्नेश्वरम मंदिर" का संबंध रामायण काल की किस पावन घटना से है?',
      opts: ['लक्ष्मण मूर्छा', 'प्रभु श्री राम द्वारा शिव पूजा (ब्रह्महत्या निवारण)', 'हनुमान मिलन', 'सीता हरण'],
      correct: 1,
      desc: 'रावण वध के उपरांत प्रभु श्री राम ने मुन्नेश्वरम में भगवान शिव की आराधना कर आशीर्वाद प्राप्त किया था।',
      map: 'https://www.google.com/maps/search/?api=1&query=Munneswaram+Temple+Sri+Lanka'
    },
    {
      q: 'वियतनाम में चाम राजवंश द्वारा निर्मित 4थी से 14वीं शताब्दी के प्राचीन शिव मंदिर समूह को क्या कहते हैं?',
      opts: ['माई सन (My Son Sanctuary)', 'पो नगर', 'बा फनोम', 'वाट फू'],
      correct: 0,
      desc: 'वियतनाम का "माई सन" हिंदू मंदिर समूह भगवान भद्रेश्वर (शिव) को समर्पित यूनेस्को धरोहर है।',
      map: 'https://www.google.com/maps/search/?api=1&query=My+Son+Sanctuary+Vietnam'
    },
    {
      q: 'मॉरीशस में स्थित "गंगा तालाब" (Grand Bassin) के तट पर भगवान शिव की कितनी ऊँची प्रतिमा स्थित है?',
      opts: ['51 फीट', '108 फीट', '125 फीट', '151 फीट'],
      correct: 1,
      desc: 'मॉरीशस के गंगा तालाब पर 108 फीट ऊँचे मंगल महादेव की दिव्य प्रतिमा विश्व भर में विख्यात है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Grand+Bassin+Mauritius'
    },
    {
      q: 'बाली (इंडोनेशिया) में समुद्र की चट्टान पर स्थित कौन सा मंदिर सूर्यास्त दर्शन के लिए प्रसिद्ध है?',
      opts: ['तनाह लोट मंदिर (Tanah Lot)', 'उलुवातु मंदिर', 'तीर्थ एम्पुल', 'लेम्पूयांग'],
      correct: 0,
      desc: 'तनाह लोट मंदिर बाली के तट पर समुद्र के भीतर शिला पर स्थित सागर देव वरुण और शिव का मंदिर है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Tanah+Lot+Temple+Bali'
    },
    {
      q: 'पाकिस्तान के पंजाब प्रांत में स्थित वह प्राचीन ऐतिहासिक तीर्थ कौन सा है जहाँ भगवान शिव के अश्रु से सरोवर बना?',
      opts: ['हिंगलाज माता', 'कटास राज मंदिर', 'शारदा पीठ', 'पंचमुखी हनुमान'],
      correct: 1,
      desc: 'कटास राज मंदिर का अमृत कुंड माता सती के वियोग में भगवान शिव के अश्रुओं से निर्मित माना जाता है।',
      map: 'https://www.google.com/maps/search/?api=1&query=Katas+Raj+Temples'
    }
  ],
  chalisa: [
    {
      q: 'हनुमान चालीसा के अनुसार अष्ट सिद्धि और नौ निधियों के दाता होने का वरदान किसने दिया?',
      opts: ['माता सीता', 'प्रभु श्री राम', 'सूर्य देव', 'भगवान शिव'],
      correct: 0,
      desc: 'माता सीता ने अशोक वाटिका में प्रसन्न होकर हनुमान जी को "अष्ट सिद्धि नवनिधि के दाता। अस बर दीन जानकी माता॥" का वरदान दिया था।'
    },
    {
      q: 'हनुमान चालीसा में सूर्य और पृथ्वी के बीच की दूरी का वर्णन किस चौपाई में मिलता है?',
      opts: ['जय हनुमान ज्ञान गुन सागर', 'जुग सहस्र जोजन पर भानू। लील्यो ताहि मधुर फल जानू॥', 'भीम रूप धरि असुर संहारे', 'दुर्गम काज जगत के जेते'],
      correct: 1,
      desc: 'जुग (12000) × सहस्र (1000) × जोजन (8 मील) = 96,000,000 मील (लगभग 15.36 करोड़ किमी), जो सूर्य की सटीक दूरी है।'
    },
    {
      q: 'हनुमान चालीसा की रचना 16वीं शताब्दी में किस महान संत एवं कवि ने की थी?',
      opts: ['संत कबीरदास', 'गोस्वामी तुलसीदास जी', 'सूरदास जी', 'संत तुकाराम'],
      correct: 1,
      desc: 'गोस्वामी तुलसीदास जी ने काशी के संकटमोचन क्षेत्र में अवधि भाषा में दिव्य श्री हनुमान चालीसा की रचना की।'
    },
    {
      q: 'शिव चालीसा के अनुसार भगवान शिव के मस्तक पर कौन सी पावन नदी विराजती है?',
      opts: ['यमुना जी', 'गंगा जी', 'सरयू जी', 'नर्मदा जी'],
      correct: 1,
      desc: '"गले रुण्डमाला तन छार लगावै। कासी में विराजे गंगा बहावै॥" - भगवान शिव ने स्वर्ग से उतरती गंगा को अपनी जटाओं में धारण किया।'
    },
    {
      q: 'हनुमान जी ने लंका में प्रवेश करते समय किस राक्षसी को मुष्टिका प्रहार से पराजित किया था?',
      opts: ['ताड़का', 'त्रिजटा', 'लंकिनी', 'सूर्पणखा'],
      correct: 2,
      desc: 'हनुमान जी ने लंका द्वार पर लंकिनी को परास्त कर लंका में प्रवेश किया था।'
    },
    {
      q: 'दुर्गा चालीसा में माँ दुर्गा के वाहन के रूप में किसका वर्णन आता है?',
      opts: ['गरुड़', 'सिंह (शेर)', 'मयूर', 'हंस'],
      correct: 1,
      desc: '"सिंह वाहिनी मात भवानी। तेरी महिमा सब जग जानी॥" - माँ दुर्गा सिंह पर सवार होकर दुष्टों का संहार करती हैं।'
    },
    {
      q: 'हनुमान चालीसा में "कंचन बरन बिराज सुबेसा। कानन कुण्डल कुंचित..." अगली पंक्ति क्या है?',
      opts: ['हाथ बज्र औ ध्वजा बिराजै', 'केसा', 'लाली देह लाली लसे', 'जय कपीस तिहुँ लोक उजागर'],
      correct: 1,
      desc: '"कंचन बरन बिराज सुबेसा। कानन कुण्डल कुंचित केसा॥"'
    },
    {
      q: 'गायत्री चालीसा के अनुसार गायत्री महामंत्र किस प्राचीनतम वेद का सर्वोपरि मंत्र है?',
      opts: ['सामवेद', 'ऋग्वेद (तीसरा मंडल)', 'यजुर्वेद', 'अथर्ववेद'],
      correct: 1,
      desc: 'गायत्री मंत्र ऋग्वेद के तीसरे मंडल (सूक्त 62, मंत्र 10) में महर्षि विश्वामित्र द्वारा दृष्ट है।'
    },
    {
      q: 'हनुमान चालीसा का पाठ कितनी बार करने से सभी बंधनों से मुक्ति का फल बताया गया है?',
      opts: ['11 बार', '21 बार', '100 बार (शत बार)', '108 बार'],
      correct: 2,
      desc: '"जो सत बार पाठ कर कोई। छूटहि बंदि महा सुख होई॥"'
    },
    {
      q: 'श्री गणेश चालीसा में सर्वप्रथम किस पावन नाम का स्मरण कर विघ्न दूर करने की प्रार्थना की गई है?',
      opts: ['गजानन', 'एकदंत', 'लम्बोदर', 'जय गणपति सदगुण सदन'],
      correct: 3,
      desc: '"जय गणपति सदगुण सदन, कविवर बदन कृपाल। विघ्न हरण मंगल करण, जय जय गिरिजालाल॥"'
    }
  ],
  gita: [
    {
      q: 'गीता में "स्थितप्रज्ञ" किसे कहा गया है?',
      opts: ['जो केवल तपस्या करे', 'जो सुख-दुःख में समभाव रखे', 'जो युद्ध छोड़ दे', 'जो धन संचय करे'],
      correct: 1,
      desc: 'भगवान श्री कृष्ण के अनुसार जो सुख में अति-उत्साही और दुःख में विचलित नहीं होता, वही स्थितप्रज्ञ है।'
    },
    {
      q: 'श्रीमद्भगवद्गीता में कुल कितने अध्याय (Chapters) और श्लोक हैं?',
      opts: ['12 अध्याय, 500 श्लोक', '18 अध्याय, 700 श्लोक', '24 अध्याय, 1000 श्लोक', '16 अध्याय, 600 श्लोक'],
      correct: 1,
      desc: 'महाभारत के भीष्म पर्व के अंतर्गत गीता में कुल 18 अध्याय और 700 पवित्र श्लोक हैं।'
    },
    {
      q: 'भगवान श्री कृष्ण ने अर्जुन को गीता का दिव्य उपदेश कुरुक्षेत्र के किस पावन तीर्थ पर दिया था?',
      opts: ['ब्रह्म सरोवर', 'ज्योतिसर तीर्थ', 'बाणगंगा', 'थानेश्वर'],
      correct: 1,
      desc: 'कुरुक्षेत्र में ज्योतिसर नामक पावन स्थान पर वटवृक्ष की छत्रछाया में भगवान ने गीता का ज्ञान दिया था।'
    },
    {
      q: 'गीता के अनुसार आत्मा का स्वरूप क्या है?',
      opts: ['नश्वर', 'अजर-अमर (न जायते म्रियते वा कदाचित्)', 'केवल जल से नष्ट होने वाली', 'अग्नि से जलने वाली'],
      correct: 1,
      desc: '"नैनं छिन्दन्ति शस्त्राणि नैनं दहति पावकः।" - आत्मा को न शस्त्र काट सकते हैं, न अग्नि जला सकती है, यह अमर है।'
    },
    {
      q: 'गीता के 11वें अध्याय में भगवान श्री कृष्ण ने अर्जुन को अपने किस रूप के दर्शन कराए थे?',
      opts: ['बाल रूप', 'विश्वरूप (विराट रूप)', 'चतुर्भुज विष्णु रूप', 'नटराज रूप'],
      correct: 1,
      desc: '11वें अध्याय (विश्वरूपदर्शनयोग) में भगवान ने अपने अनंत मुखों, नेत्रों और संपूर्ण ब्रह्मांड समाहित विराट रूप के दर्शन कराए।'
    },
    {
      q: 'भगवान श्री कृष्ण ने अर्जुन के रथ के सारथी बनते समय कौन सा दिव्य शंख बजाया था?',
      opts: ['देवदत्त', 'पांचजन्य', 'पौण्ड्र', 'अनंतविजय'],
      correct: 1,
      desc: '"पाञ्चजन्यं हृषीकेशो देवदत्तं धनञ्जयः।" - भगवान श्री कृष्ण का शंख पांचजन्य था और अर्जुन का देवदत्त।'
    },
    {
      q: 'गीता में कर्म के कितने प्रकार बताए गए हैं?',
      opts: ['कर्म, अकर्म और विकर्म', 'केवल शुभ और अशुभ', 'सत्य और असत्य', 'धर्म और अधर्म'],
      correct: 0,
      desc: 'अध्याय 4 श्लोक 17 में भगवान ने कर्म (कर्तव्य), अकर्म (निष्काम कर्म) और विकर्म (निषिद्ध पाप कर्म) का भेद बताया है।'
    },
    {
      q: '"यदा यदा ही धर्मस्य ग्लानिर्भवति भारत..." यह प्रसिद्ध श्लोक गीता के किस अध्याय में आता है?',
      opts: ['अध्याय 2', 'अध्याय 4 (ज्ञानकर्मसंन्यासयोग)', 'अध्याय 9', 'अध्याय 18'],
      correct: 1,
      desc: 'अध्याय 4 के श्लोक 7-8 में भगवान ने धर्म की स्थापना और सज्जनों के उद्धार हेतु अपने अवतार लेने का रहस्य बताया है।'
    },
    {
      q: 'अर्जुन के प्रसिद्ध गांडीव धनुष और रथ की ध्वजा पर कौन सा पावन चिन्ह था?',
      opts: ['गरुड़', 'कपिध्वज (श्री हनुमान जी)', 'सूर्य', 'सिंह'],
      correct: 1,
      desc: 'अर्जुन के रथ की ध्वजा पर पवनपुत्र हनुमान जी साक्षात विराजमान थे, इसलिए अर्जुन को कपिध्वज कहा जाता है।'
    },
    {
      q: 'गीता का अंतिम और 18वां श्लोक संजय के मुख से क्या उद्घोष करता है?',
      opts: ['सर्वधर्मान्परित्यज्य', 'यत्र योगेश्वरः कृष्णो यत्र पार्थो धनुर्धरः। तत्र श्रीर्विजयो भूतिः...', 'मा शुचः', 'संजयो उवाच'],
      correct: 1,
      desc: 'जहाँ योगेश्वर श्री कृष्ण हैं और जहाँ गांडीवधारी अर्जुन हैं, वहाँ विजय, ऐश्वर्य और निश्चित नीति है।'
    }
  ]
};

// 🎯 CONTROLLER METHODS

window.openQuizHubModal = function() {
  const modal = document.getElementById('quiz-hub-modal');
  if (modal) {
    modal.style.display = 'flex';
    window.currentQuizIndex = 0;
    window.quizScore = 0;
    window.isQuizAnswered = false;
    window.applyQuizTheme();
    window.startQuizTimer();
    window.renderCurrentQuiz();
    if (navigator.vibrate) navigator.vibrate(30);
  }
};

window.closeQuizHubModal = function() {
  const modal = document.getElementById('quiz-hub-modal');
  if (modal) modal.style.display = 'none';
  window.stopQuizTimer();
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
};

window.toggleQuizTheme = function() {
  window.isQuizLightMode = !window.isQuizLightMode;
  localStorage.setItem('sanatan_quiz_theme', window.isQuizLightMode ? 'light' : 'dark');
  window.applyQuizTheme();
};

window.applyQuizTheme = function() {
  const card = document.getElementById('quiz-hub-card');
  const themeBtn = document.getElementById('quiz-theme-btn');
  const title = document.getElementById('quiz-header-title');
  const qBox = document.getElementById('quiz-question-box');
  const qText = document.getElementById('quiz-question-text');

  if (!card) return;

  if (window.isQuizLightMode) {
    card.style.background = 'linear-gradient(160deg, #FFFDF8 0%, #FEF3C7 100%)';
    card.style.borderColor = '#D97706';
    card.style.color = '#1A0B2E';
    if (themeBtn) themeBtn.textContent = '🌙';
    if (title) title.style.color = '#78350F';
    if (qBox) {
      qBox.style.background = 'rgba(255,255,255,0.85)';
      qBox.style.borderColor = '#F59E0B';
    }
    if (qText) qText.style.color = '#1A0B2E';
  } else {
    card.style.background = 'linear-gradient(160deg, #2A0948 0%, #150426 60%, #0B0116 100%)';
    card.style.borderColor = 'rgba(248,200,59,0.5)';
    card.style.color = '#FFFDF8';
    if (themeBtn) themeBtn.textContent = '☀️';
    if (title) title.style.color = '#FFFDF8';
    if (qBox) {
      qBox.style.background = 'rgba(255,255,255,0.06)';
      qBox.style.borderColor = 'rgba(248,200,59,0.25)';
    }
    if (qText) qText.style.color = '#FFFDF8';
  }
};

window.startQuizTimer = function() {
  window.stopQuizTimer();
  window.quizSecondsLeft = 120;
  window.updateTimerUI();

  window.quizTimerInterval = setInterval(() => {
    if (window.quizSecondsLeft > 0) {
      window.quizSecondsLeft--;
      window.updateTimerUI();
    } else {
      window.stopQuizTimer();
      window.handleQuizTimeout();
    }
  }, 1000);
};

window.stopQuizTimer = function() {
  if (window.quizTimerInterval) {
    clearInterval(window.quizTimerInterval);
    window.quizTimerInterval = null;
  }
};

window.updateTimerUI = function() {
  const timerText = document.getElementById('quiz-timer-text');
  const timerBadge = document.getElementById('quiz-timer-badge');
  if (timerText) timerText.textContent = `${window.quizSecondsLeft}s`;

  if (timerBadge) {
    if (window.quizSecondsLeft <= 15) {
      timerBadge.style.background = 'rgba(239, 68, 68, 0.25)';
      timerBadge.style.borderColor = '#EF4444';
      timerBadge.style.color = '#F87171';
    } else {
      timerBadge.style.background = 'rgba(248,200,59,0.18)';
      timerBadge.style.borderColor = '#F8C83B';
      timerBadge.style.color = '#FDE68A';
    }
  }
};

window.handleQuizTimeout = function() {
  if (window.isQuizAnswered) return;
  window.isQuizAnswered = true;
  if (typeof playSoundEffect === 'function') playSoundEffect('wrong');
  
  const deck = window.QUIZ_DECK[window.currentQuizCategory] || window.QUIZ_DECK.india;
  const qData = deck[window.currentQuizIndex] || deck[0];

  const btns = document.querySelectorAll('.quiz-opt-btn');
  btns.forEach((btn, i) => {
    btn.disabled = true;
    if (i === qData.correct) {
      btn.style.background = 'rgba(16, 185, 129, 0.25)';
      btn.style.borderColor = '#10B981';
      btn.style.color = '#34D399';
    }
  });

  const fbBox = document.getElementById('quiz-feedback-box');
  const fbTitle = document.getElementById('quiz-feedback-title');
  const fbDesc = document.getElementById('quiz-feedback-desc');
  const mapLink = document.getElementById('quiz-map-link');

  if (fbBox) {
    fbBox.style.display = 'block';
    if (fbTitle) {
      fbTitle.textContent = '⏱️ समय समाप्त! सही उत्तर देखें:';
      fbTitle.style.color = '#F87171';
    }
    if (fbDesc) fbDesc.textContent = qData.desc;
    if (mapLink) {
      if (qData.map) {
        mapLink.href = qData.map;
        mapLink.style.display = 'inline';
      } else {
        mapLink.style.display = 'none';
      }
    }
  }
};

window.switchQuizCategory = function(cat, btnEl) {
  window.currentQuizCategory = cat;
  window.currentQuizIndex = 0;
  window.quizScore = 0;
  window.isQuizAnswered = false;

  document.querySelectorAll('.quiz-cat-btn').forEach(b => {
    b.style.background = 'rgba(255,255,255,0.08)';
    b.style.color = '#CBD5E1';
    b.style.border = '1px solid rgba(255,255,255,0.15)';
  });
  if (btnEl) {
    btnEl.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btnEl.style.color = '#1A0B2E';
    btnEl.style.border = 'none';
  }

  // Hide Result View & Show Main View
  const mainView = document.getElementById('quiz-main-view');
  const resultView = document.getElementById('quiz-result-view');
  if (mainView) mainView.style.display = 'block';
  if (resultView) resultView.style.display = 'none';

  window.startQuizTimer();
  window.renderCurrentQuiz();
};

window.renderCurrentQuiz = function() {
  window.isQuizAnswered = false;
  const deck = window.QUIZ_DECK[window.currentQuizCategory] || window.QUIZ_DECK.india;
  const qData = deck[window.currentQuizIndex] || deck[0];
  
  const qText = document.getElementById('quiz-question-text');
  if (qText) qText.textContent = qData.q;

  const pBadge = document.getElementById('quiz-progress-badge');
  if (pBadge) pBadge.textContent = `Q ${window.currentQuizIndex + 1} / ${deck.length}`;

  const fbBox = document.getElementById('quiz-feedback-box');
  if (fbBox) fbBox.style.display = 'none';

  const list = document.getElementById('quiz-options-list');
  if (list) {
    const letters = ['A', 'B', 'C', 'D'];
    list.innerHTML = qData.opts.map((opt, i) => `
      <button onclick="selectQuizOption(${i})" class="quiz-opt-btn" style="width:100%; text-align:left; background:rgba(255,255,255,0.08); border:1.5px solid rgba(255,255,255,0.15); color:${window.isQuizLightMode ? '#1A0B2E' : '#FFF'}; padding:11px 14px; border-radius:14px; font-size:0.88rem; font-weight:700; cursor:pointer; display:flex; align-items:center; gap:10px; transition:transform 0.15s ease;">
        <span style="background:rgba(248,200,59,0.25); color:#FDE68A; width:26px; height:26px; border-radius:8px; display:inline-flex; align-items:center; justify-content:center; font-size:0.8rem; font-weight:900; flex-shrink:0;">${letters[i]}</span>
        <span style="flex:1;">${opt}</span>
      </button>
    `).join('');
  }
};

window.selectQuizOption = function(idx) {
  if (window.isQuizAnswered) return;
  window.isQuizAnswered = true;
  window.stopQuizTimer();

  const deck = window.QUIZ_DECK[window.currentQuizCategory] || window.QUIZ_DECK.india;
  const qData = deck[window.currentQuizIndex] || deck[0];
  const isRight = (idx === qData.correct);

  if (isRight) {
    window.quizScore++;
  }

  const btns = document.querySelectorAll('.quiz-opt-btn');
  btns.forEach((btn, i) => {
    btn.disabled = true;
    if (i === qData.correct) {
      btn.style.background = 'rgba(16, 185, 129, 0.25)';
      btn.style.borderColor = '#10B981';
      btn.style.color = '#34D399';
    } else if (i === idx && !isRight) {
      btn.style.background = 'rgba(239, 68, 68, 0.25)';
      btn.style.borderColor = '#EF4444';
      btn.style.color = '#F87171';
    }
  });

  const fbBox = document.getElementById('quiz-feedback-box');
  const fbTitle = document.getElementById('quiz-feedback-title');
  const fbDesc = document.getElementById('quiz-feedback-desc');
  const mapLink = document.getElementById('quiz-map-link');

  if (fbBox) {
    fbBox.style.display = 'block';
    if (isRight) {
      if (fbTitle) {
        fbTitle.textContent = '🎉 शाबाश! सही जवाब! (+10 साधना अंक)';
        fbTitle.style.color = '#34D399';
      }
      if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
      if (typeof playSoundEffect === 'function') playSoundEffect('correct');
    } else {
      if (fbTitle) {
        fbTitle.textContent = '❌ गलत जवाब! सही उत्तर देखें:';
        fbTitle.style.color = '#F87171';
      }
      if (typeof playSoundEffect === 'function') playSoundEffect('wrong');
    }
    if (fbDesc) fbDesc.textContent = qData.desc;
    if (mapLink) {
      if (qData.map) {
        mapLink.href = qData.map;
        mapLink.style.display = 'inline';
      } else {
        mapLink.style.display = 'none';
      }
    }
  }
};

window.nextQuizQuestion = function() {
  const deck = window.QUIZ_DECK[window.currentQuizCategory] || window.QUIZ_DECK.india;
  if (window.currentQuizIndex < deck.length - 1) {
    window.currentQuizIndex++;
    window.startQuizTimer();
    window.renderCurrentQuiz();
  } else {
    window.showQuizCompletionView();
  }
};

window.showQuizCompletionView = function() {
  window.stopQuizTimer();
  const deck = window.QUIZ_DECK[window.currentQuizCategory] || window.QUIZ_DECK.india;

  if (window.quizScore > window.quizHighScore) {
    window.quizHighScore = window.quizScore;
    localStorage.setItem('sanatan_quiz_high_score', window.quizHighScore.toString());
  }

  const mainView = document.getElementById('quiz-main-view');
  const resultView = document.getElementById('quiz-result-view');
  const finalScoreEl = document.getElementById('quiz-final-score');
  const highScoreNumEl = document.getElementById('quiz-high-score-num');

  if (mainView) mainView.style.display = 'none';
  if (resultView) resultView.style.display = 'block';

  if (finalScoreEl) finalScoreEl.textContent = `${window.quizScore} / ${deck.length}`;
  if (highScoreNumEl) highScoreNumEl.textContent = `${window.quizHighScore}`;

  if (typeof triggerFlowerShower === 'function') {
    triggerFlowerShower();
    setTimeout(triggerFlowerShower, 500);
  }
};

window.restartQuizCurrentCategory = function() {
  const mainView = document.getElementById('quiz-main-view');
  const resultView = document.getElementById('quiz-result-view');
  if (mainView) mainView.style.display = 'block';
  if (resultView) resultView.style.display = 'none';

  window.currentQuizIndex = 0;
  window.quizScore = 0;
  window.startQuizTimer();
  window.renderCurrentQuiz();
};

window.shareQuizScoreWhatsApp = function() {
  const deck = window.QUIZ_DECK[window.currentQuizCategory] || window.QUIZ_DECK.india;
  const catName = window.currentQuizCategory === 'india' ? 'भारत मंदिर' : (window.currentQuizCategory === 'world' ? 'विश्व मंदिर' : (window.currentQuizCategory === 'chalisa' ? 'चालीसा' : 'गीता'));
  const text = `🚩 *दिव्य प्रश्नोत्तरी (सनातन ज्ञान) में मेरी उपलब्धि!* 🚩\nमैंने *${catName}* क्विज़ में *${window.quizScore} / ${deck.length}* अंक प्राप्त किए! 🏆\nमेरा उच्च स्कोर: *${window.quizHighScore}* 🌟\n\nक्या आप मेरा रिकॉर्ड तोड़ सकते हैं? डाउनलोड करें 'भक्ति में लीन' ऐप और अपना ज्ञान परखें! 🕉️\nhttp://localhost:8000`;
  
  if (navigator.share) {
    navigator.share({ title: 'सनातन ज्ञान क्विज़ उपलब्धि', text: text }).catch(() => {});
  } else {
    window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, '_blank');
  }
};

window.speakCurrentQuizQuestion = function() {
  if (!('speechSynthesis' in window)) {
    if (typeof showToast === 'function') showToast('ℹ️ आपका ब्राउज़र वॉइस सपोर्ट नहीं करता');
    return;
  }

  window.speechSynthesis.cancel();
  const deck = window.QUIZ_DECK[window.currentQuizCategory] || window.QUIZ_DECK.india;
  const qData = deck[window.currentQuizIndex] || deck[0];

  const speechText = `प्रश्न: ${qData.q}। विकल्प हैं: A: ${qData.opts[0]}। B: ${qData.opts[1]}। C: ${qData.opts[2]}। D: ${qData.opts[3]}।`;
  const utter = new SpeechSynthesisUtterance(speechText);
  utter.lang = 'hi-IN';
  utter.rate = 0.9;
  window.speechSynthesis.speak(utter);
};
"""

# Replace quiz section in app.js
start_pos = js.find('// 4. MCQ Quiz Hub Logic')
if start_pos != -1:
    end_pos = js.find('// 5. Kalyan Kund Seva Daan Logic', start_pos)
    js = js[:start_pos] + rich_quiz_js + "\n\n" + js[end_pos:]
    print("✓ Replaced MCQ Quiz Hub Logic in app.js")
else:
    print("start_pos not found, appending rich_quiz_js")
    js += "\n\n" + rich_quiz_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Saved app.js")
