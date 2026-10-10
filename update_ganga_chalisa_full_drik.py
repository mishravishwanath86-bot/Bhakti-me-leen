import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ गंगा माता चालीसा ॥

॥ दोहा ॥
जय जय जय जग पावनी, जयति देवसरि गंग।
जय शिव जटा निवासिनी, अनुपम तुंग तरंग॥

॥ चौपाई ॥
जय जय जननी हराना अघखानी। आनंद करनी गंगा महारानी॥१॥
जय भगीरथी सुरसरि माता। कलिमल मूल डालिनी विख्याता॥२॥
जय जय जहानु सुता अघ हनानी। भीष्म की माता जगा जननी॥३॥
धवल कमल दल मम तनु सजे। लखी शत शरद चन्द्र छवि लजाई॥४॥
वहां मकर विमल शुची सोहें। अमिया कलश कर लखी मन मोहें॥५॥
जदिता रत्ना कंचन आभूषण। हिय मणि हर, हरानितम दूषण॥६॥
जग पावनी त्रय ताप नासवनी। तरल तरंग तुंग मन भावनी॥७॥
जो गणपति अति पूज्य प्रधान। इहूं ते प्रथम गंगा अस्नाना॥८॥
ब्रह्मा कमंडल वासिनी देवी। श्री प्रभु पद पंकज सुख सेवि॥९॥
साथी सहस्र सागर सुत तरयो। गंगा सागर तीरथ धरयो॥१०॥
अगम तरंग उठ्यो मन भवन। लखी तीरथ हरिद्वार सुहावन॥११॥
तीरथ राज प्रयाग अक्षैवेता। धरयो मातु पुनि काशी करवत॥१२॥
धनी धनी सुरसरि स्वर्ग की सीधी। तरनी अमिता पितु पड़ पिरही॥१३॥
भागीरथी ताप कियो उपारा। दियो ब्रह्म तव सुरसरि धारा॥१४॥
जब जग जननी चल्यो हहराई। शम्भु जाता महं रह्यो समाई॥१५॥
वर्षा पर्यंत गंगा महारानी। रहीं शम्भू के जाता भुलानी॥१६॥
पुनि भागीरथी शम्भुहीं ध्यायो। तब इक बूंद जटा से पायो॥१७॥
ताते मातु भें त्रय धारा। मृत्यु लोक, नाभा, अरु पातारा॥१८॥
गईं पाताल प्रभावती नामा। मन्दाकिनी गई गगन ललामा॥१९॥
मृत्यु लोक जाह्नवी सुहावनी। कलिमल हरनी अगम जग पावनि॥२०॥
धनि मइया तब महिमा भारी। धर्मं धुरी कलि कलुष कुठारी॥२१॥
मातु प्रभवति धनि मंदाकिनी। धनि सुर सरित सकल भयनासिनी॥२२॥
पन करत निर्मल गंगा जल। पावत मन इच्छित अनंत फल॥२३॥
पुरव जन्म पुण्य जब जागत। तबहीं ध्यान गंगा महं लागत॥२४॥
जई पगु सुरसरी हेतु उठावही। तई जगि अश्वमेघ फल पावहि॥२५॥
महा पतित जिन कहू न तारे। तिन तारे इक नाम तिहारे॥२६॥
शत योजन हूं से जो ध्यावहिं। निशचाई विष्णु लोक पद पावहीं॥२७॥
नाम भजत अगणित अघ नाशै। विमल ज्ञान बल बुद्धि प्रकाशे॥२८॥
जिमी धन मूल धर्मं अरु दाना। धर्मं मूल गंगाजल पाना॥२९॥
तब गुन गुणन करत दुख भाजत। गृह गृह सम्पति सुमति विराजत॥३०॥
गंगहि नेम सहित नित ध्यावत। दुर्जनहूं सज्जन पद पावत॥३१॥
उद्दिहिन विद्या बल पावै। रोगी रोग मुक्त हवे जावै॥३२॥
गंगा गंगा जो नर कहहीं। भूखा नंगा कभुहुह न रहहि॥३३॥
निकसत ही मुख गंगा माई। श्रवण दाबी यम चलहिं पराई॥३४॥
महं अघिन अधमन कहं तारे। भए नरका के बंद किवारें॥३५॥
जो नर जपी गंग शत नामा। सकल सिद्धि पूरण ह्वै कामा॥३६॥
सब सुख भोग परम पद पावहीं। आवागमन रहित ह्वै जावहीं॥३७॥
धनि मइया सुरसरि सुख दैनि। धनि धनि तीरथ राज त्रिवेणी॥३८॥
ककरा ग्राम ऋषि दुर्वासा। सुन्दरदास गंगा कर दासा॥३९॥
जो यह पढ़े गंगा चालीसा। मिली भक्ति अविरल वागीसा॥४०॥

॥ दोहा ॥
नित नए सुख सम्पति लहैं, धरें गंगा का ध्यान।
अंत समाई सुर पुर बसल, सदर बैठी विमान॥
संवत भुत नभ्दिशी, राम जन्म दिन चैत्र।
पूरण चालीसा किया, हरी भक्तन हित नेत्र॥"""

meaning = """॥ गंगा माता चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहा】
• "जय जय जय जग पावनी, जयति देवसरि गंग। जय शिव जटा निवासिनी, अनुपम तुंग तरंग॥"
भावार्थ: समस्त संसार को परम पवित्र करने वाली देवसरिता माँ गंगा की जय हो, जय हो! देवाधिदेव भगवान शिव की जटाओं में निवास करने वाली और अत्यंत ऊंची व मनोहारी लहरों (तरंगों) से सुशोभित माँ गंगे, आपकी सदा जय हो!

【४० चौपाइयां — भावार्थ】
१-३. "जय जय जननी हराना अघखानी... भीष्म की माता जगा जननी॥"
भावार्थ: हे पापों की खान को समूल नष्ट करने वाली जगन्माता गंगा महारानी! आपकी जय हो, आप परमानंद की वर्षा करने वाली हैं। राजा भगीरथ द्वारा पृथ्वी पर अवतरित कराई गई सुरसरि माता, आप कलियुग के समस्त मलों व पापों को उखाड़ फेंकने वाली विख्यात देवी हैं। महर्षि जह्नु की कन्या होने से जाह्नवी, महाबली गंगापुत्र भीष्म की जननी और संपूर्ण जगत का पालन करने वाली माँ गंगे, आपको बारम्बार नमन है।

४-६. "धवल कमल दल मम तनु सजे... हिय मणि हर, हरानितम दूषण॥"
भावार्थ: आपका दिव्य स्वरूप श्वेत कमल के दलों के समान कोमल और उज्ज्वल है, जिसकी अलौकिक कांति को देखकर सैकड़ों शरद पूर्णिमा के चंद्रमा भी लज्जित हो जाते हैं। आपकी पवित्र सवारी मकर (मगरमच्छ) सुशोभित है और आपके करकमलों में अमृत से भरा कलश मन को मुग्ध कर लेता है। आप स्वर्णाभूषणों और रत्नों से अलंकृत हैं तथा आपके हृदय पर मणियों का हार सुशोभित है, जो अज्ञान रूपी अंधकार और दूषणों को हर लेता है।

७-१०. "जग पावनी त्रय ताप नासवनी... गंगा सागर तीरथ धरयो॥"
भावार्थ: आप तीनों तापों (दैहिक, दैविक, भौतिक) का नाश करने वाली और मन को मोहने वाली चंचल तरंगों वाली हैं। अग्रपूज्य प्रथम देवता श्री गणेश जी ने भी सर्वप्रथम गंगा स्नान कर सर्वोच्च पद पाया। आप सृष्टि के आदि में ब्रह्मा जी के कमंडल में वास करने वाली और भगवान श्री हरि विष्णु के वामन रूप में चरण-कमलों की सेवा करने वाली देवी हैं। आपने राजा सगर के साठ हजार शापग्रस्त पुत्रों का उद्धार किया, जहाँ आज प्रसिद्ध 'गंगासागर' तीर्थ स्थापित है।

११-१४. "अगम तरंग उठ्यो मन भवन... दियो ब्रह्म तव सुरसरि धारा॥"
भावार्थ: आपकी ऊंची-ऊंची लहरें देखकर मन हर्षित हो जाता है; आपके तट पर हरिद्वार जैसा मनोहारी तीर्थ शोभायमान है। तीर्थराज प्रयाग में अक्षयवट और त्रिवेणी संगम तथा मोक्षनगरी काशी में आपका पावन प्रवाह साक्षात् मुक्ति का द्वार है। हे सुरसरि! आप स्वर्ग की सीधी सीढ़ी हैं, जो पूर्वजों और पितरों की पीढ़ियों को तार देती हैं। जब राजर्षि भगीरथ ने कठोर तपस्या की, तब ब्रह्मा जी ने प्रसन्न होकर आपकी पावन धारा को मुक्त किया।

१५-१८. "जब जग जननी चल्यो हहराई... मृत्यु लोक, नाभा, अरु पातारा॥"
भावार्थ: जब जगज्जननी गंगा प्रचंड वेग से गर्जना करती हुई स्वर्ग से चलीं, तब उनके अपार वेग को संभालने के लिए देवाधिदेव भगवान शिव ने उन्हें अपनी जटाओं में समेट लिया। पूरे एक वर्ष तक गंगा महारानी शिव जी की जटाओं के भीतर ही भ्रमण करती रहीं। तब भगीरथ ने पुनः भगवान आशुतोष शिव का ध्यान व तप किया, जिससे प्रसन्न होकर शिव जी ने अपनी जटा से मात्र एक पावन बूंद को पृथ्वी पर छोड़ा। उसी से माँ गंगा की तीन दिव्य धाराएं (त्रिपथगा) प्रकट हुईं—स्वर्ग लोक, मृत्यु लोक और पाताल लोक।

१९-२२. "गईं पाताल प्रभावती नामा... धनि सुर सरित सकल भयनासिनी॥"
भावार्थ: पाताल लोक में आपकी पावन धारा 'प्रभावती' (भोगवती) नाम से प्रवाहित हुई, आकाश (स्वर्ग) में अत्यंत सुंदर 'मंदाकिनी' नाम से देवों को पावन करने लगी, और मृत्यु लोक (पृथ्वी) में कलिकाल के समस्त पापों को हरने वाली 'जाह्नवी' बनकर प्रकट हुईं। हे धर्म की धुरी और कलि के पापों को काटने वाली कुल्हाड़ी स्वरूपा माँ! आपकी महिमा अपरंपार है; समस्त भयों का नाश करने वाली सुरसरि माँ गंगे, आप धन्य हैं।

२३-२७. "पन करत निर्मल गंगा जल... निशचाई विष्णु लोक पद पावहीं॥"
भावार्थ: जो प्राणी आपके निर्मल गंगाजल का आचमन करता है, वह मनवांछित अनंत फलों को प्राप्त करता है। जब पूर्व जन्मों के संचित पुण्य जाग्रत होते हैं, तभी जीव का मन गंगा जी के ध्यान और दर्शन में लगता है। गंगा स्नान हेतु मनुष्य जितने पग (कदम) उठाता है, उसे प्रत्येक कदम पर अश्वमेध यज्ञ का महान फल प्राप्त होता है। जिन महापापियों को किसी ने नहीं तारा, वे आपके केवल एक नाम के स्मरण से तर गए। यहाँ तक कि जो मनुष्य सौ योजन (चार सौ कोस) की दूरी से भी 'गंगा-गंगा' का स्मरण करता है, वह निश्चित ही परम वैकुंठ लोक को प्राप्त होता है।

२८-३२. "नाम भजत अगणित अघ नाशै... रोगी रोग मुक्त हवे जावै॥"
भावार्थ: गंगा नाम का भजन करने से अनगिनत पाप नष्ट हो जाते हैं और निर्मल ज्ञान, बुद्धि व आत्मबल का प्रकाश होता है। जैसे धन का मूल धर्म और दान है, वैसे ही समस्त धर्मों और तीर्थों का मूल गंगाजल का पान है। आपके गुणों का गान करने से जीवन के सारे दुःख भाग जाते हैं और घर-घर में सद्बुद्धि व संपत्ति का वास होता है। नियमपूर्वक गंगा का ध्यान करने से दुर्जन भी सज्जन बन जाते हैं, बुद्धिहीनों को विद्या-बल मिलता है और रोगी समस्त असाध्य व्याधियों से मुक्त हो जाते हैं।

३३-३७. "गंगा गंगा जो नर कहहीं... आवागमन रहित ह्वै जावहीं॥"
भावार्थ: जो मनुष्य नित्य 'गंगा-गंगा' का उच्चारण करता है, वह कभी भूखा या दरिद्र नहीं रहता। मुख से 'गंगा' शब्द निकलते ही यमराज के दूत कान बंद करके दूर भाग जाते हैं और नरक के द्वार सदा के लिए बंद हो जाते हैं। जो मनुष्य गंगा जी के सौ पावन नामों का जप करता है, उसके समस्त कार्य सिद्ध होते हैं; वह संसार के सभी सुखों को भोगकर अंत में आवागमन (जन्म-मरण चक्र) से मुक्त होकर मोक्ष पद प्राप्त करता है।

३८-४०. "धनि मइया सुरसरि सुख दैनि... मिली भक्ति अविरल वागीसा॥"
भावार्थ: हे समस्त सुखों को देने वाली सुरसरि माँ! आप धन्य हैं, और तीर्थराज प्रयाग की पावन त्रिवेणी धन्य है। ककरा ग्राम के महर्षि दुर्वासा आश्रम के निवासी सन्त सुन्दरदास जी कहते हैं कि वे माँ गंगा के अनन्य दास हैं। जो भी भक्त इस गंगा चालीसा का श्रद्धापूर्वक पाठ करता है, उसे माँ सरस्वती की कृपा और परमात्मा की अविरल व निश्चल भक्ति प्राप्त होती है।

【समापन दोहे】
• "नित नए सुख सम्पति लहैं, धरें गंगा का ध्यान। अंत समाई सुर पुर बसल, सदर बैठी विमान॥"
भावार्थ: जो भी मनुष्य नित्य माँ गंगा का ध्यान धरता है, वह जीवन में नित्य नए सुख और ऐश्वर्य प्राप्त करता है; और अंत समय में दिव्य विमान में आदरपूर्वक बैठकर देवताओं के परम धाम (सुरपुर/वैकुंठ) को प्राप्त होता है।
• "संवत भुत नभ्दिशी, राम जन्म दिन चैत्र। पूरण चालीसा किया, हरी भक्तन हित नेत्र॥"
भावार्थ: संवत के पावन काल में चैत्र मास की रामनवमी (प्रभु श्री राम के अवतरण दिवस) के परम शुभ अवसर पर, हरिभक्तों के कल्याण और दिव्य नेत्र (ज्ञान) प्रदान करने हेतु यह पवित्र चालीसा पूर्ण की गई।"""

vidhi = """॥ गंगा माता चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. सर्वोत्तम समय व पावन तिथियां:
- प्रातःकाल ब्रह्म मुहूर्त या सूर्योदय के समय पूर्व अथवा उत्तर दिशा की ओर मुख करके पाठ करना सर्वश्रेष्ठ है।
- विशेष पर्व: गंगा दशहरा (ज्येष्ठ शुक्ल दशमी), गंगा सप्तमी/जयंती (वैशाख शुक्ल सप्तमी), मकर संक्रांति, कार्तिक पूर्णिमा, तथा प्रत्येक मास की पूर्णिमा व अमावस्या।

२. स्नान व शुद्धि नियम:
- यदि गंगा तट पर हों, तो गंगा जी में तीन अथवा पाँच डुबकी लगाकर पवित्र मन से पाठ करें।
- यदि घर पर हों, तो सामान्य स्नान के जल में कुछ बूंदें गंगाजल की मिलाकर निम्न मंत्र बोलें:
  "गङ्गे च यमुने चैव गोदावरि सरस्वति। नर्मदे सिन्धु कावेरि जलेऽस्मिन् संनिधिं कुरु॥"
- स्नान के उपरांत स्वच्छ श्वेत अथवा पीले वस्त्र धारण कर कुशा या ऊनी आसन पर बैठें।

३. पूजन सामग्री:
- पूजा स्थल में तांबे अथवा पीतल के पात्र में शुद्ध गंगाजल रखें।
- गाय के शुद्ध देशी घी का दीपक अथवा कर्पूर प्रज्वलित करें।
- श्वेत चंदन, अक्षत, श्वेत पुष्प (मोगरा, चमेली या कमल), तथा दूर्वा।
- भोग: कच्चा गाय का दूध, बताशे, खीर, ऋतुफल (विशेषकर तरबूज, आम या केला)।
- माँ गंगा को अर्पित करने हेतु लाल चुनरी, रोली और श्रीफल।

४. दीपदान विधान (विशेष फलदायी):
- सांध्यकाल सूर्यास्त के समय गंगा तट पर (अथवा घर के मंदिर में) पत्तों के दोने में पुष्प रखकर घी का दीपक प्रज्वलित करें और गंगाजल में दीपदान करें। इससे जन्म-जन्मांतरों के पाप नष्ट होते हैं।

५. पाठ का क्रम:
- सर्वप्रथम आचमन व पवित्रीकरण करें।
- श्री गणेश जी और भगवान शिव का ध्यान कर 'ॐ नमो भगवत्यै कालिन्द्यै गंगायै नारायण्यै नमो नमः' अथवा 'ॐ गं गंगायै नमः' मंत्र का ११ बार जप करें।
- तदोपरांत भक्तिभाव से एकाग्रचित्त होकर गंगा चालीसा का पाठ करें (१, ३, ७ या ११ बार)।
- अंत में 'ॐ जय गंगे माता' आरती गाएं और सभी परिजनों को गंगाजल का चरणामृत दें।"""

significance = """॥ गंगा माता चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. त्रिपथगा व त्रय ताप हरणी शक्ति:
माँ गंगा ब्रह्मांड की एकमात्र ऐसी दिव्य नदी हैं जो तीनों लोकों में प्रवाहित होती हैं—स्वर्ग में मंदाकिनी, मृत्युलोक में जाह्नवी/भागीरथी, और पाताल में प्रभावती/भोगवती। इसलिए इन्हें 'त्रिपथगा' कहा जाता है। गंगा चालीसा का पाठ करने से मनुष्य के तीनों ताप—दैहिक (रोग), दैविक (ग्रह बाधा), और भौतिक (शत्रु व दरिद्रता)—तत्काल शांत हो जाते हैं।

२. पितृ तर्पण व मुक्ति प्रदाता:
महाराजा सगर के ६०,००० भस्म हुए पुत्रों को मोक्ष प्रदान करने के लिए ही भगीरथ गंगा जी को पृथ्वी पर लाए थे। गंगा चालीसा का पाठ करने से कुल के समस्त पितर तृप्त होते हैं और पितृदोष का समूल नाश होकर वंश की वृद्धि होती है।

३. नरक निवारण व यमभय मुक्ति:
"निकसत ही मुख गंगा माई। श्रवण दाबी यम चलहिं पराई॥"
शास्त्रों में स्पष्ट उल्लेख है कि जो भी व्यक्ति गंगा नाम का संकीर्तन करता है, यमराज के दूत उसके पास नहीं फटकते और उसके लिए नरक के द्वार सदा के लिए बंद हो जाते हैं।

४. अश्वमेध यज्ञ तुल्य फल:
"जई पगु सुरसरी हेतु उठावही। तई जगि अश्वमेघ फल पावहि॥"
गंगा दर्शन, स्नान व स्मरण हेतु उठाया गया प्रत्येक कदम अश्वमेध यज्ञ का अक्षय पुण्य फल प्रदान करता है।

५. दरिद्रता व अकाल मृत्यु का नाश:
नित्य गंगा चालीसा का पाठ करने वाले साधक के घर में अन्न-धन के भंडार सदा भरे रहते हैं, व्यापार में प्रगति होती है और अकाल मृत्यु का भय मिट जाता है। अंत समय में जीव को वैकुंठ धाम की प्राप्ति होती है।"""

english_lyrics = """॥ Ganga Mata Chalisa ॥

॥ Doha ॥
Jaya Jaya Jaya Jaga Paavanee, Jayati Devasari Ganga।
Jaya Shiva Jataa Nivaasinee, Anupama Tunga Taranga॥

॥ Chaupai ॥
Jaya Jaya Jananee Haraanaa Aghakhaanee। Aananda Karanee Gangaa Mahaaraanee॥1॥
Jaya Bhaageerathee Surasari Maataa। Kalimala Moola Daalinee Vikhyaataa॥2॥
Jaya Jaya Jahaanu Sutaa Agha Hanaanee। Bheeshma Kee Maataa Jagaa Jananee॥3॥
Dhavala Kamala Dala Mama Tanu Saje। Lakhee Shata Sharada Chandra Chhavi Lajaayee॥4॥
Vahaan Makara Vimala Shuchee Sohen। Amiyaa Kalasha Kara Lakhee Mana Mohen॥5॥
Jaditaa Ratnaa Kanchana Aabhooshana। Hiya Mani Hara, Haraani-Tama Dooshana॥6॥
Jaga Paavanee Traya Taapa Naasavanee। Tarala Taranga Tunga Mana Bhaavanee॥7॥
Jo Ganapati Ati Poojya Pradhaana। Ihoon Te Prathama Gangaa Asnaanaa॥8॥
Brahmaa Kamandala Vaasinee Devee। Shree Prabhu Pada Pankaja Sukha Sevee॥9॥
Saathee Sahasra Saagara Suta Tarayo। Gangaa Saagara Teeratha Dharayo॥10॥
Agama Taranga Uthyo Mana Bhavana। Lakhee Teeratha Haridwaara Suhaavana॥11॥
Teeratha Raaja Prayaaga Akshaivetaa। Dharayo Maatu Puni Kaashee Karavata॥12॥
Dhanee Dhanee Surasari Swarga Kee Seedhee। Taranee Amitaa Pitu Pada Pirahee॥13॥
Bhaageerathee Taapa Kiyo Upaaraa। Diyo Brahma Tava Surasari Dhaaraa॥14॥
Jaba Jaga Jananee Chalyo Haharaa-ee। Shambhu Jaataa Mahan Rahyo Samaa-ee॥15॥
Varshaa Paryanta Gangaa Mahaaraanee। Raheen Shambhoo Ke Jaataa Bhulaanee॥16॥
Puni Bhaageerathee Shambhuheen Dhyaayo। Taba Ika Boonda Jataa Se Paayo॥17॥
Taate Maatu Bhen Traya Dhaaraa। Mrityu Loka, Naabhaa, Aru Paataaraa॥18॥
Ga-een Paataala Prabhaavatee Naamaa। Mandaakinee Ga-ee Gagana Lalaamaa॥19॥
Mrityu Loka Jaahnavee Suhaavanee। Kalimala Haranee Agama Jaga Paavani॥20॥
Dhani Ma-iyaa Tava Mahimaa Bhaaree। Dharma Dhuree Kali Kalusha Kuthhaaree॥21॥
Maatu Prabhaavati Dhani Mandaakinee। Dhani Sura Sarita Sakala Bhayanaasinee॥22॥
Pana Karata Nirmala Gangaa Jala। Paavata Mana Ichchhita Ananta Phala॥23॥
Poorava Janma Punya Jaba Jaagata। Tabaheen Dhyaana Gangaa Mahan Laagata॥24॥
Ja-ee Pagu Surasaree Hetu Uthhaavahee। Ta-ee Jagi Ashwamedha Phala Paavahi॥25॥
Mahaa Patita Jina Kahoo Na Taare। Tina Taare Ika Naama Tihaare॥26॥
Shata Yojana Hoon Se Jo Dhyaavahin। Nishachaa-ee Vishnu Loka Pada Paavaneen॥27॥
Naama Bhajata Aganita Agha Naashai। Vimala Gyaana Bala Buddhi Prakaashe॥28॥
Jimee Dhana Moola Dharma Aru Daanaa। Dharma Moola Gangaajala Paanaa॥29॥
Taba Guna Gunana Karata Dukha Bhaajata। Griha Griha Sampati Sumati Viraajata॥30॥
Gangahi Nema Sahita Nita Dhyaavata। Durjanahoon Sajjana Pada Paavata॥31॥
Uddihina Vidyaa Bala Paavai। Rogee Roga Mukta Have Jaavai॥32॥
Gangaa Gangaa Jo Nara Kahaheen। Bhookhaa Nangaa Kabhuhuh Na Rahahi॥33॥
Nikasata Hee Mukha Gangaa Maa-ee। Shravana Daabee Yama Chalahin Paraa-ee॥34॥
Mahan Aghina Adhamana Kahan Taare। Bha-e Narakaa Ke Banda Kivaaren॥35॥
Jo Nara Japee Ganga Shata Naamaa। Sakala Siddhi Poorana Hwai Kaamaa॥36॥
Saba Sukha Bhoga Parama Pada Paavaneen। Aavaagamana Rahita Hwai Jaavaneen॥37॥
Dhani Ma-iyaa Surasari Sukha Dainee। Dhani Dhani Teeratha Raaja Triveanee॥38॥
Kakaraa Graama Rishi Durvaasaa। Sundaradaasa Gangaa Kara Daasaa॥39॥
Jo Yaha Padhe Gangaa Chaaleesaa। Milee Bhakti Avirala Vaageesaa॥40॥

॥ Doha ॥
Nita Na-e Sukha Sampati Lahain, Dharen Gangaa Kaa Dhyaana।
Anta Samaa-ee Sura Pura Basala, Sadara Baithee Vimaana॥
Samvata Bhuta Nabhdishee, Raama Janma Dina Chaitra।
Poorana Chaaleesaa Kiyaa, Haree Bhaktana Hita Netra॥"""

# 1. Update drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["ganga"]["items"]:
    if item["id"] == "drik_chalisa_27":
        item["title"] = "गंगा माता चालीसा"
        item["title_en"] = "Ganga Mata Chalisa"
        item["en_line"] = "Jaya Jaya Jaya Jaga Paavanee"
        item["hi_line"] = "जय जय जय जग पावनी, जयति"
        item["sub"] = "जय जय जय जग पावनी, जयति • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_ganga_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=zePrQdOZdus"
        item["video_id"] = "zePrQdOZdus"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/ganga-mata/ganga-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "माँ गंगा व पवित्र नदियां"
        item["section"] = "माँ गंगा व पवित्र नदियां चालीसा"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_27 in drik_chalisa_collections.json successfully!")

# 2. Update window.CHALISA_COLLECTIONS in app.js
with open("app.js", "r", encoding="utf-8") as f:
    app_text = f.read()

prefix = "window.CHALISA_COLLECTIONS = "
idx1 = app_text.find(prefix)
if idx1 != -1:
    idx2 = app_text.find(";\n", idx1)
    if idx2 != -1:
        new_cols_js = prefix + json.dumps(cols, ensure_ascii=False, indent=2)
        app_text = app_text[:idx1] + new_cols_js + app_text[idx2:]
        print("Updated window.CHALISA_COLLECTIONS in app.js!")

# 3. Add chalisa_ganga in CONTENT in app.js
content_obj = {
    "title": "गंगा माता चालीसा",
    "title_en": "Ganga Mata Chalisa",
    "en_line": "Jaya Jaya Jaya Jaga Paavanee",
    "hi_line": "जय जय जय जग पावनी, जयति",
    "sub": "जय जय जय जग पावनी, जयति • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_ganga_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=zePrQdOZdus",
    "video_id": "zePrQdOZdus",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/ganga-mata/ganga-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "माँ गंगा व पवित्र नदियां",
    "section": "माँ गंगा व पवित्र नदियां चालीसा",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

ganga_content_js = "  chalisa_ganga: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_ganga: {" in app_text:
    m_start = app_text.find("  chalisa_ganga: {")
    m_end = app_text.find("\n  chalisa_", m_start + 1)
    if m_end != -1:
        app_text = app_text[:m_start] + ganga_content_js + app_text[m_end+1:]
        print("Replaced existing chalisa_ganga in CONTENT!")
else:
    # Insert right after chalisa_khatushyam or chalisa_narasimha
    k_pos = app_text.find("  chalisa_khatushyam: {")
    if k_pos != -1:
        k_end = app_text.find("\n  chalisa_", k_pos + 1)
        if k_end == -1:
            k_end = app_text.find("\n  sundarkand:", k_pos + 1)
        if k_end != -1:
            app_text = app_text[:k_end+1] + ganga_content_js + app_text[k_end+1:]
            print("Inserted chalisa_ganga after chalisa_khatushyam in CONTENT!")
    else:
        v_pos = app_text.find("  chalisa_vishwakarma: {")
        if v_pos != -1:
            app_text = app_text[:v_pos] + ganga_content_js + app_text[v_pos:]
            print("Inserted chalisa_ganga before chalisa_vishwakarma in CONTENT!")

with open("app.js", "w", encoding="utf-8") as f:
    f.write(app_text)
print("Saved app.js successfully!")

# 4. Sync chalisa_engine.js with drik_chalisa_collections.json
if os.path.exists("chalisa_engine.js"):
    with open("chalisa_engine.js", "r", encoding="utf-8") as f:
        ce_text = f.read()
    ce_prefix = "window.CHALISA_COLLECTIONS = "
    c_idx1 = ce_text.find(ce_prefix)
    if c_idx1 != -1:
        c_idx2 = ce_text.find(";\n", c_idx1)
        if c_idx2 != -1:
            ce_text = ce_text[:c_idx1] + ce_prefix + json.dumps(cols, ensure_ascii=False, indent=2) + ce_text[c_idx2:]
            with open("chalisa_engine.js", "w", encoding="utf-8") as f:
                f.write(ce_text)
            print("Synced chalisa_engine.js successfully!")
