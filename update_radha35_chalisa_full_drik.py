import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री राधा चालीसा ॥

॥ दोहा ॥
श्री राधे वृषभानुजा, भक्तनि प्राणाधार।
वृन्दाविपिन विहारिणि, प्रणवौं बारंबार॥
जैसौ तैसौ रावरौ, कृष्ण प्रिया सुखधाम।
चरण शरण निज दीजिये, सुन्दर सुखद ललाम॥

॥ चौपाई ॥
जय वृषभानु कुँवरि श्री श्यामा। कीरति नंदिनी शोभा धामा॥१॥
नित्य विहारिनि श्याम अधारा। अमित मोद मंगल दातारा॥२॥
रास विलासिनि रस विस्तारिनि। सहचरि सुभग यूथ मन भावनि॥३॥
नित्य किशोरी राधा गोरी। श्याम प्राणधन अति जिय भोरी॥४॥
करुणा सागर हिय उमंगिनी। ललितादिक सखियन की संगिनी॥५॥
दिन कर कन्या कूल विहारिनि। कृष्ण प्राण प्रिय हिय हुलसावनि॥६॥
नित्य श्याम तुमरौ गुण गावैं। राधा राधा कहि हरषावैं॥७॥
मुरली में नित नाम उचारें। तुव कारण लीला वपु धारें॥८॥
प्रेम स्वरूपिणि अति सुकुमारी। श्याम प्रिया वृषभानु दुलारी॥९॥
नवल किशोरी अति छवि धामा। द्युति लघु लगै कोटि रति कामा॥१०॥
गौरांगी शशि निंदक बदना। सुभग चपल अनियारे नयना॥११॥
जावक युत युग पंकज चरना। नूपुर धुनि प्रीतम मन हरना॥१२॥
संतत सहचरि सेवा करहीं। महा मोद मंगल मन भरहीं॥१३॥
रसिकन जीवन प्राण अधारा। राधा नाम सकल सुख सारा॥१४॥
अगम अगोचर नित्य स्वरूपा। ध्यान धरत निशिदिन ब्रज भूपा॥१५॥
उपजेउ जासु अंश गुण खानी। कोटिन उमा रमा ब्रह्मानी॥१६॥
नित्य धाम गोलोक विहारिनि। जन रक्षक दुख दोष नसावनि॥१७॥
शिव अज मुनि सनकादिक नारद। पार न पाँइ शेष अरु शारद॥१८॥
राधा शुभ गुण रूप उजारी। निरखि प्रसन्न होत बनबारी॥१९॥
ब्रज जीवन धन राधा रानी। महिमा अमित न जाय बखानी॥२०॥
प्रीतम संग देइ गलबाँही। बिहरत नित वृन्दावन माँही॥२१॥
राधा कृष्ण कृष्ण कहैं राधा। एक रूप दोउ प्रीति अगाधा॥२२॥
श्री राधा मोहन मन हरनी। जन सुख दायक प्रफुलित बदनी॥२३॥
कोटिक रूप धरें नंद नंदा। दर्श करन हित गोकुल चन्दा॥२४॥
रास केलि करि तुम्हें रिझावें। मान करौ जब अति दुःख पावें॥२५॥
प्रफुलित होत दर्श जब पावें। विविध भांति नित विनय सुनावें॥२६॥
वृन्दारण्य विहारिनि श्यामा। नाम लेत पूरण सब कामा॥२७॥
कोटिन यज्ञ तपस्या करहू। विविध नेम व्रत हिय में धरहू॥२८॥
तऊ न श्याम भक्तहिं अपनावें। जब लगि राधा नाम न गावें॥२९॥
वृन्दाविपिन स्वामिनी राधा। लीला वपु तब अमित अगाधा॥३०॥
स्वयं कृष्ण पावैं नहिं पारा। और तुम्हें को जानन हारा॥३१॥
श्री राधा रस प्रीति अभेदा। सादर गान करत नित वेदा॥३२॥
राधा त्यागि कृष्ण को भजिहैं। ते सपनेहु जग जलधि न तरि हैं॥३३॥
कीरति कुँवरि लाड़िली राधा। सुमिरत सकल मिटहिं भवबाधा॥३४॥
नाम अमंगल मूल नसावन। त्रिविध ताप हर हरि मनभावन॥३५॥
राधा नाम लेइ जो कोई। सहजहि दामोदर बस होई॥३६॥
राधा नाम परम सुखदाई। भजतहिं कृपा करहिं यदुराई॥३७॥
यशुमति नन्दन पीछे फिरिहैं। जो कोऊ राधा नाम सुमिरिहैं॥३८॥
रास विहारिनि श्यामा प्यारी। करहु कृपा बरसाने वारी॥३९॥
वृन्दावन है शरण तिहारी। जय जय जय वृषभानु दुलारी॥४०॥

॥ दोहा ॥
श्रीराधा सर्वेश्वरी, रसिकेश्वर घनश्याम।
करहुँ निरंतर बास मैं, श्रीवृन्दावन धाम॥"""

meaning = """॥ श्री राधा चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "श्री राधे वृषभानुजा, भक्तनि प्राणाधार। वृन्दाविपिन विहारिणि, प्रणवौं बारंबार॥"
भावार्थ: हे राजा वृषभानु की दुलारी श्री किशोरी जी! आप अपने अनन्य भक्तों के प्राणों का एकमात्र आधार हैं। श्री वृन्दावन के पावन कुंजों में नित्य विहार करने वाली हे स्वामिनी! मैं आपके श्रीचरणों में बारंबार साष्टांग प्रणाम करता हूँ।
• "जैसौ तैसौ रावरौ, कृष्ण प्रिया सुखधाम। चरण शरण निज दीजिये, सुन्दर सुखद ललाम॥"
भावार्थ: हे भगवान श्रीकृष्ण की परम प्रियतमा, समस्त सुखों के पावन धाम श्रीराधा जी! मैं जैसा भी हूँ, भला-बुरा, आपका ही हूँ। मुझे अपने परम सुंदर, सुखप्रद और अलौकिक युगल चरणों की पावन शरण प्रदान कीजिए।

【४० चौपाइयां — पद्यवार भावार्थ】
१-४. "जय वृषभानु कुँवरि श्री श्यामा... श्याम प्राणधन अति जिय भोरी॥"
भावार्थ: हे वृषभानु की सुकुमारी श्री श्यामा जू! आपकी सदा जय हो; आप माता कीर्ति की आनंददायिनी कन्या और सौंदर्य का साक्षात् धाम हैं। आप श्री वृन्दावन में नित्य विहार करने वाली और श्यामसुंदर का एकमात्र जीवन-आधार हैं; आप भक्तों को अपार आनंद और सर्वमंगल प्रदान करने वाली हैं। आप महारास की विलासिनी और दिव्य भक्ति-रस का विस्तार करने वाली हैं; अपनी प्रिय सखियों और सहचरियों के समूह को मन से भाने वाली हैं। आप नित्य नवल किशोरी, गौर वर्ण रूपा और कन्हैया के प्राणों का धन हैं; आपका हृदय अत्यंत भोला और निर्मल है।

५-८. "करुणा सागर हिय उमंगिनी... तुव कारण लीला वपु धारें॥"
भावार्थ: आपके हृदय में अहैतुकी करुणा और दया का सागर नित्य उमड़ता रहता है; आप ललिता, विशाखा आदि अष्टसखियों की प्राण-सहेली हैं। आप सूर्यपुत्री यमुना के पावन कूल (तटों) पर नित्य क्रीड़ा करती हैं और प्राणप्रिय श्रीकृष्ण के हृदय को नित्य आनंदित (हुलसित) करती हैं। साक्षात् भगवान श्यामसुंदर नित्य आपकी ही महिमा का गान करते हैं और 'राधे-राधे' कहकर परमानंद में मग्न होते हैं। वे अपनी मोहन मुरली की तान में नित्य आपका ही नाम पुकारते हैं और केवल आपके प्रेम के वशीभूत होकर ही विविध लीलाएं करने हेतु अवतार धारण करते हैं।

९-१२. "प्रेम स्वरूपिणि अति सुकुमारी... नूपुर धुनि प्रीतम मन हरना॥"
भावार्थ: आप साक्षात् विशुद्ध दिव्य प्रेम का स्वरूप और अत्यंत सुकुमारी हैं; आप श्यामसुंदर की नित्य प्रिया और राजा वृषभानु की लाड़ली हैं। आप नित्य नवल किशोरी और अलौकिक छवि का धाम हैं; आपकी रूप-कांति के समक्ष करोड़ों रति और कामदेव की कांति भी अत्यंत तुच्छ लगती है। आपका अंग-अंग गौर वर्ण (स्वर्ण के समान) और मुख पूर्ण चन्द्रमा के सौंदर्य को भी लजाने वाला है; आपके दोनों नेत्र अत्यंत सुंदर, चंचल और प्रेम-बाणों से युक्त हैं। आपके दोनों चरण-कमलों पर लगा लाल महावर (जावक) अत्यंत शोभायमान है और चरणों में बजने वाले नूपुरों की मधुर ध्वनि प्रियतम कन्हैया के मन को हर लेती है।

१३-१६. "संतत सहचरि सेवा करहीं... कोटिन उमा रमा ब्रह्मानी॥"
भावार्थ: ललितादिक सखियां निरंतर प्रेमपूर्वक आपकी चरण-सेवा करती हैं और अपने मनों को परम आनंद व मंगल से भरती हैं। आप समस्त रसिक संतों के जीवन और प्राणों का एकमात्र आधार हैं; श्री राधा नाम ही संसार के समस्त सुखों का सार-सर्वस्व है। आपका नित्य स्वरूप मन और वाणी की सीमा से परे अगम और अगोचर है; स्वयं ब्रजराज श्रीकृष्ण रात-दिन आपके ही रूप का ध्यान धरते हैं। आप समस्त सद्गुणों की ऐसी अक्षय खान हैं कि आपके एक अंशमात्र के प्रभाव से करोड़ों उमा (पार्वती), रमा (लक्ष्मी) और ब्रह्माणी प्रकट होती हैं।

१७-२०. "नित्य धाम गोलोक विहारिनि... महिमा अमित न जाय बखानी॥"
भावार्थ: आप अपने नित्य धाम श्री गोलोक और वृन्दावन में निरंतर विहार करती हैं; आप शरणागत भक्तों की रक्षा करने वाली और उनके समस्त दुखों व दोषों का नाश करने वाली हैं। देवाधिदेव शिव, ब्रह्मा, सनकादिक मुनि और नारद जी भी आपकी महिमा का पार नहीं पा सकते; शेषनाग और सरस्वती जी भी आपकी स्तुति करते-करते थक जाते हैं। आपके शुभ गुणों और अनुपम सौंदर्य को देखकर साक्षात् बनवारी श्रीकृष्ण तृप्त और प्रसन्न होते हैं। आप ब्रजवासियों के जीवन का एकमात्र धन हैं; आपकी असीम महिमा का शब्दों में वर्णन नहीं किया जा सकता।

२१-२४. "प्रीतम संग देइ गलबाँही... दर्श करन हित गोकुल चन्दा॥"
भावार्थ: आप प्रियतम श्रीकृष्ण के गले में अपनी कोमल बांहें डालकर श्री वृन्दावन के कुंज-निकुंजों में नित्य प्रेम-विहार करती हैं। राधा जी 'कृष्ण-कृष्ण' और कृष्ण जी 'राधा-राधा' पुकारते हैं; स्वरूप से दो होने पर भी दोनों का आत्म-स्वरूप एक है और दोनों का परस्पर प्रेम अथाह व अगाध है। श्री राधा जी मनमोहन श्रीकृष्ण के भी मन को हरने वाली हैं; आपका प्रफुल्लित मुखमंडल भक्तों को परमानंद प्रदान करता है। गोकुल के चन्द्रमा नंदनंदन श्रीकृष्ण केवल आपके दिव्य दर्शन पाने के लिए करोड़ों रूप धारण करते हैं।

२५-२८. "रास केलि करि तुम्हें रिझावें... विविध नेम व्रत हिय में धरहू॥"
भावार्थ: श्रीकृष्ण दिव्य रासलीला रचकर आपको रिझाते हैं; और जब आप मान (प्रेम-रूठना) करती हैं, तो वे अत्यंत व्याकुल और दुखी हो जाते हैं। जब वे आपका दर्शन पा लेते हैं, तो प्रफुल्लित होकर आपके सम्मुख विविध प्रकार से नित्य विनय-प्रार्थना करते हैं। हे श्री वृन्दावन की रानी श्यामा जू! आपका पावन नाम लेते ही भक्तों के समस्त मनोरथ पूर्ण हो जाते हैं। चाहे कोई मनुष्य करोड़ों यज्ञ और कठिन तपस्याएं क्यों न कर ले, और अपने हृदय में अनेक कठिन नियम व व्रत क्यों न धारण कर ले;

२९-३२. "तऊ न श्याम भक्तहिं अपनावें... सादर गान करत नित वेदा॥"
भावार्थ: तब तक भगवान श्यामसुंदर उस साधक को कदापि नहीं अपनाते, जब तक कि वह प्रेमपूर्वक 'श्री राधा' नाम का संकीर्तन नहीं करता! आप वृन्दावन की स्वामिनी महारानी हैं; आपकी लीलाएं और स्वरूप असीम, अगाध और रहस्यमय हैं। जब स्वयं सर्वज्ञ श्रीकृष्ण भी आपकी महिमा का पार नहीं पा सकते, तब अन्य कौन आपको पूर्णतः जान सकता है? श्री राधा और कृष्ण का रस व प्रेम सर्वथा अभेद और एक रूप है; चारों वेद भी नित्य आदरपूर्वक इसी युगल प्रेम का गान करते हैं।

३३-३६. "राधा त्यागि कृष्ण को भजिहैं... सहजहि दामोदर बस होई॥"
भावार्थ: जो अज्ञानी जीव श्री राधा जी को छोड़कर केवल श्रीकृष्ण का भजन करना चाहते हैं, वे स्वप्न में भी इस भवसागर से पार नहीं उतर सकते! कीर्ति की राजदुलारी लाड़िली राधा का स्मरण करते ही संसार की समस्त भव-बाधाएं और संकट पल भर में मिट जाते हैं। श्री राधा नाम अमंगल की मूल जड़ को उखाड़ फेंकने वाला, तीनों तापों (दैहिक, दैविक, भौतिक) को हरने वाला और श्री हरि को परम प्रिय है। जो भी मनुष्य एक बार 'राधा' नाम का उच्चारण कर लेता है, साक्षात् दामोदर (श्रीकृष्ण) सहज ही उसके वशीभूत हो जाते हैं!

३७-४०. "राधा नाम परम सुखदाई... जय जय जय वृषभानु दुलारी॥"
भावार्थ: 'राधा' नाम परम सुख प्रदान करने वाला है; इसका जप करते ही यदुराई श्रीकृष्ण तत्काल अपनी कृपा बरसाते हैं। जो मनुष्य 'राधा-राधा' नाम का स्मरण करता है, यशोदानंदन कन्हैया उसके पीछे-पीछे दौड़ते हैं! हे रासविहारिणी श्यामा प्यारी! हे बरसाने वाली श्रीजी! मुझ दीन पर अपनी दया दृष्टि कीजिए। यह सम्पूर्ण वृन्दावन धाम और यह दास आपकी ही शरण में है; हे राजा वृषभानु की दुलारी, आपकी सदा-सदा जय हो, जय हो, जय हो!

【समापन दोहा】
• "श्रीराधा सर्वेश्वरी, रसिकेश्वर घनश्याम। करहुँ निरंतर बास मैं, श्रीवृन्दावन धाम॥"
भावार्थ: श्री राधारानी समस्त ब्रह्मांडों की सर्वेश्वरी स्वामिनी हैं और रसिकों के मुकुटमणि श्यामसुंदर रसिकेश्वर हैं। मेरी यही एकमात्र अभिलाषा है कि मुझे नित्य और निरंतर पावन श्री वृन्दावन धाम की रज (धूलि) में वास प्राप्त हो!"""

vidhi = """॥ श्री राधा चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल ब्रह्ममुहूर्त, सूर्योदय वेला, अथवा सांध्यकाल गोधूलि वेला।
- महापर्व: श्री राधाष्टमी (भाद्रपद मास के शुक्ल पक्ष की अष्टमी तिथि) — इस दिन चालीसा का १०० बार पाठ करने से साक्षात् राधा-कृपा सुलभ होती है।
- पावन अवसर: शरद पूर्णिमा (महारास रात्रि), कार्तिक मास (दामोदर मास), प्रत्येक मास की एकादशी व पूर्णिमा, तथा शुक्रवार।

२. दिशा, आसन व वस्त्र:
- दिशा: पूर्व अथवा उत्तर दिशा की ओर मुख करके बैठें।
- आसन: पीले अथवा गुलाबी रेशमी/ऊनी आसन पर बैठना चाहिए।
- वस्त्र: साधक को स्वच्छ पीले, गुलाबी, लाल अथवा श्वेत वस्त्र धारण करने चाहिए (नीले व काले वस्त्र वर्जित हैं)।

३. पूजन सामग्री व प्रिय भोग:
- दीपक: गाय के शुद्ध देशी घी का दीपक प्रज्वलित करें।
- पुष्प: सुगंधित श्वेत, गुलाबी व लाल पुष्प (गुलाब, चंपा, चमेली, कमल) और सुगंधित अत्तर/इत्र (गुलाब या चंदन)।
- प्रिय नैवेद्य: माखन-मिश्री, खीर, रबड़ी, मालपुआ, खोये के पेड़े, ऋतुफल (विशेष रूप से अनार व केला), तथा मीठा पान।
- ध्यान रहे: श्रीराधा रानी की पूजा में तुलसी दल सीधे उनके चरणों में न चढ़ाकर, उनके हाथ में या युगल सरकार के भोग में अर्पित किया जाता है।

४. युगल उपासना नियम (राधा-कृष्ण संयुक्त ध्यान):
- श्री राधा रानी की साधना कभी भी एकांगी नहीं होती; भगवान श्रीकृष्ण और श्री राधा जी के युगल स्वरूप की तस्वीर या विग्रह के सम्मुख बैठकर पाठ करें।
- पाठ से पूर्व 'राधे-राधे' महामन्त्र का अथवा 'ॐ ह्रीं श्रीं राधिकायै नमः' का कम से कम १ माला (१०८ बार) जप अवश्य करें।

५. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन व पवित्रीकरण करें।
- श्री वृन्दावन धाम, यमुना जी, गिरिराज गोवर्धन और ललिता-विशाखा सखियों का स्मरण करें।
- श्री युगल सरकार का ध्यान कर 'श्री राधा चालीसा' का १, ३, ७, ११ अथवा २१ बार पाठ करें।
- पाठ के उपरांत श्री राधा जी की पावन आरती गाएं और श्री वृन्दावन धाम की चरण-रज मस्तक पर लगाएं।"""

significance = """॥ श्री राधा चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. श्रीकृष्ण की प्राप्ति का एकमात्र सुगम द्वार (ह्लादिनी शक्ति रहस्य):
"तऊ न श्याम भक्तहिं अपनावें। जब लगि राधा नाम न गावें॥"
सनातन वैष्णव गौड़ीय व निम्बार्क परंपरा के अनुसार श्री राधा रानी भगवान श्रीकृष्ण की अभिन्न 'ह्लादिनी महाशक्ति' हैं। बिना राधा रानी की कृपा के श्रीकृष्ण की प्राप्ति तीनों लोकों में किसी को भी नहीं हो सकती। जो राधा चालीसा का पाठ करता है, श्रीकृष्ण स्वयं उसके ऋणी होकर उस पर कृपा बरसाते हैं।

२. दामोदर का वशीकरण — कन्हैया का अनुगमन:
"राधा नाम लेइ जो कोई। सहजहि दामोदर बस होई॥ यशुमति नन्दन पीछे फिरिहैं। जो कोऊ राधा नाम सुमिरिहैं॥"
श्रीमद्भागवत और पद्म पुराण का उद्घोष है कि 'राधा' नाम सुनते ही श्रीकृष्ण मतवाले हो जाते हैं और जो भक्त राधा नाम का आश्रय लेता है, भगवान उसके पीछे-पीछे रक्षा कवच बनकर चलते हैं।

३. समस्त भव-बाधाओं और त्रिविध तापों का समूल नाश:
"कीरति कुँवरि लाड़िली राधा। सुमिरत सकल मिटहिं भवबाधा॥ नाम अमंगल मूल नसावन। त्रिविध ताप हर हरि मनभावन॥"
चालीसा के पाठ से जन्म-जन्मांतरों के पाप, अज्ञान, मानसिक तनाव, ग्रह दोष और तीनों ताप (दैहिक, दैविक, भौतिक) नष्ट हो जाते हैं और जीवन में परम शांति व आनंद का संचार होता है।

४. दांपत्य जीवन में अगाध प्रेम और कलह-मुक्ति:
श्री राधा-कृष्ण का प्रेम निस्वार्थ, अलौकिक और अखंड है। जो दंपत्ति नित्य राधा चालीसा का पाठ करते हैं, उनके दांपत्य में कटुता दूर होकर अटूट प्रेम, सम्मान और मधुरता स्थापित होती है।

५. वृन्दावन वास एवं गोलोक धाम की प्राप्ति:
"श्रीराधा सर्वेश्वरी, रसिकेश्वर घनश्याम। करहुँ निरंतर बास मैं, श्रीवृन्दावन धाम॥"
नित्य पाठ करने वाले साधक को अंत समय में गोलोक धाम की नित्य निकुंज सेवा और श्री वृन्दावन धाम की पावन रज में शाश्वत विश्राम प्राप्त होता है।"""

english_lyrics = """॥ Shri Radha Chalisa ॥

॥ Doha ॥
Shree Raadhe Vrishabhaanujaa, Bhaktani Praanaadhaara।
Vrindaa-Vipina Vihaarini, Pranavaun Baarambaara॥
Jaisau Taisau Raavarau, Krishna Priyaa Sukhadhaama।
Charana Sharana Nija Deejiye, Sundara Sukhada Lalaama॥

॥ Chaupai ॥
Jaya Vrishabhaanu Kunvari Shree Shyaamaa। Keerati Nandinee Shobhaa Dhaamaa॥1॥
Nitya Vihaarini Shyaama Adhaaraa। Amita Moda Mangala Daataaraa॥2॥
Raasa Vilaasini Rasa Vistaarini। Sahachari Subhaga Yootha Mana Bhaavani॥3॥
Nitya Kishoree Raadhaa Goree। Shyaama Praanadhana Ati Jiya Bhoree॥4॥
Karunaa Saagara Hiya Umanginee। Lalitaadika Sakhiyan Kee Sanginee॥5॥
Dina Kara Kanyaa Koola Vihaarini। Krishna Praana Priya Hiya Hulasaavani॥6॥
Nitya Shyaama Tumaro Guna Gaavain। Raadhaa Raadhaa Kahi Harashaavain॥7॥
Muralee Men Nita Naama Uchaaren। Tuva Kaarana Leelaa Vapu Dhaaren॥8॥
Prema Svaroopini Ati Sukumaaree। Shyaama Priyaa Vrishabhaanu Dulaaree॥9॥
Navala Kishoree Ati Chhavi Dhaamaa। Dyuti Laghu Lagai Koti Rati Kaamaa॥10॥
Gouraangee Shashi Nindaka Badanaa। Subhaga Chapala Aniyaare Nayanaa॥11॥
Jaavaka Yuta Yuga Pankaja Charanaa। Noopura Dhuni Preetama Mana Haranaa॥12॥
Santata Sahachari Sevaa Karahin। Mahaa Moda Mangala Mana Bharahin॥13॥
Rasikana Jeevana Praana Adhaaraa। Raadhaa Naama Sakala Sukha Saaraa॥14॥
Agama Agochara Nitya Svaroopaa। Dhyaana Dharata Nishidina Braja Bhoopaa॥15॥
Upaje-u Jaasu Ansha Guna Khaanee। Kotina Umaa Ramaa BrahmaaNee॥16॥
Nitya Dhaama Goloka Vihaarini। Jana Rakshaka Dukha Dosha Nasaavani॥17॥
Shiva Aja Muni Sanakaadika Naarada। Paara Na Paain Shesha Aru Shaarada॥18॥
Raadhaa Shubha Guna Roopa Ujaaree। Nirakhi Prasanna Hota Banabaaree॥19॥
Braja Jeevana Dhana Raadhaa Raanee। Mahimaa Amita Na Jaaya Bakhaanee॥20॥
Preetama Sanga De-i Galabaanhee। Biharata Nita Vrindaavana Maanhee॥21॥
Raadhaa Krishna Krishna Kahain Raadhaa। Eka Roopa Dou Preeti Agaadhaa॥22॥
Shree Raadhaa Mohana Mana Haranee। Jana Sukha Daayaka Praphulita Badanee॥23॥
Kotika Roopa Dharen Nanda Nandaa। Darsha Karana Hita Gokula Chandaa॥24॥
Raasa Keli Kari Tumhen Rijaaven। Maana Karau Jaba Ati Dukha Paaven॥25॥
Praphulita Hota Darsha Jaba Paaven। Vividha Bhaanti Nita Vinaya Sunaaven॥26॥
Vrindaaranya Vihaarini Shyaamaa। Naama Leta Poorana Saba Kaamaa॥27॥
Kotina Yagya Tapasyaa Karahoo। Vividha Nema Vrata Hiya Men Dharahoo॥28॥
Tau Na Shyaama Bhaktahin Apanaaven। Jaba Lagi Raadhaa Naama Na Gaaven॥29॥
Vrindaavipina Svaaminee Raadhaa। Leelaa Vapu Taba Amita Agaadhaa॥30॥
Svayam Krishna Paavain Nahin Paaraa। Aura Tumhen Ko Jaanana Haaraa॥31॥
Shree Raadhaa Rasa Preeti Abhedaa। Saadara Gaana Karata Nita Vedaa॥32॥
Raadhaa Tyaagi Krishna Ko Bhajihain। Te Sapanehu Jaga Jaladhi Na Tari Hain॥33॥
Keerati Kunvari Laadilee Raadhaa। Sumirata Sakala Mitahin Bhavabaadhaa॥34॥
Naama Amangala Moola Nasaavana। Trividha Taapa Hara Hari Manabhaavana॥35॥
Raadhaa Naama Le-i Jo Ko-ee। Sahajahi Daamodara Basa Ho-ee॥36॥
Raadhaa Naama Parama Sukhadaa-ee। Bhajatahin Kripaa Karahin Yaduraa-ee॥37॥
Yashumati Nandana Peechhe Phirihain। Jo Kou Raadhaa Naama Sumirihain॥38॥
Raasa Vihaarini Shyaamaa Pyaaree। Karahu Kripaa Barasaane Vaaree॥39॥
Vrindaavana Hai Sharana Tihaaree। Jaya Jaya Jaya Vrishabhaanu Dulaaree॥40॥

॥ Doha ॥
Shree Raadhaa Sarveshwaree, Rasikeshwara Ghanashyaama।
Karahun Nirantara Baasa Main, Shree Vrindaavana Dhaama॥"""

# 1. Update drik_chalisa_35 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["radha"]["items"]:
    if item["id"] == "drik_chalisa_35":
        item["title"] = "श्री राधा चालीसा"
        item["title_en"] = "Shri Radha Chalisa"
        item["en_line"] = "Jai Vrishabhana Kunvari Shri Shyama"
        item["hi_line"] = "जय वृषभान कुँवरि श्री श्यामा"
        item["sub"] = "जय वृषभान कुँवरि श्री श्यामा • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_radha_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=nLydYdxcQag"
        item["video_id"] = "nLydYdxcQag"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/shri-radha/shri-radha-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "ह्लादिनी महाशक्ति श्री राधा रानी"
        item["section"] = "श्री राधा रानी चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_35 in drik_chalisa_collections.json successfully!")

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

# 3. Add chalisa_radha in CONTENT in app.js
content_obj = {
    "title": "श्री राधा चालीसा",
    "title_en": "Shri Radha Chalisa",
    "en_line": "Jai Vrishabhana Kunvari Shri Shyama",
    "hi_line": "जय वृषभान कुँवरि श्री श्यामा",
    "sub": "जय वृषभान कुँवरि श्री श्यामा • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_radha_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=nLydYdxcQag",
    "video_id": "nLydYdxcQag",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/shri-radha/shri-radha-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "ह्लादिनी महाशक्ति श्री राधा रानी",
    "section": "श्री राधा रानी चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

radha_content_js = "  chalisa_radha: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_radha: {" in app_text:
    m_start = app_text.find("  chalisa_radha: {")
    m_end = app_text.find("\n  chalisa_", m_start + 1)
    if m_end == -1:
        m_end = app_text.find("\n  sundarkand:", m_start + 1)
    if m_end != -1:
        app_text = app_text[:m_start] + radha_content_js + app_text[m_end+1:]
        print("Replaced existing chalisa_radha in CONTENT!")
else:
    # Insert right after chalisa_tulsi
    t_pos = app_text.find("  chalisa_tulsi: {")
    if t_pos != -1:
        t_end = app_text.find("\n  chalisa_", t_pos + 1)
        if t_end == -1:
            t_end = app_text.find("\n  sundarkand:", t_pos + 1)
        if t_end != -1:
            app_text = app_text[:t_end+1] + radha_content_js + app_text[t_end+1:]
            print("Inserted chalisa_radha after chalisa_tulsi in CONTENT!")
    else:
        v_pos = app_text.find("  chalisa_vishwakarma: {")
        if v_pos != -1:
            app_text = app_text[:v_pos] + radha_content_js + app_text[v_pos:]
            print("Inserted chalisa_radha before chalisa_vishwakarma in CONTENT!")

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
