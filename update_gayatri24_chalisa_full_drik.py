import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री गायत्री माता चालीसा ॥

॥ दोहा ॥
ह्रीं श्रीं क्लीं मेधा प्रभा, जीवन ज्योति प्रचण्ड।
शान्ति कान्ति जागृत प्रगति, रचना शक्ति अखण्ड॥
जगत जननी मङ्गल करनि, गायत्री सुखधाम।
प्रणवों सावित्री स्वधा, स्वाहा पूरन काम॥

॥ चौपाई ॥
भूर्भुवः स्वः ॐ युत जननी। गायत्री नित कलिमल दहनी॥१॥
अक्षर चौविस परम पुनीता। इनमें बसें शास्त्र श्रुति गीता॥२॥
शाश्वत सतोगुणी सत रूपा। सत्य सनातन सुधा अनूपा॥३॥
हंसारूढ सिताम्बर धारी। स्वर्ण कान्ति शुचि गगन-बिहारी॥४॥
पुस्तक पुष्प कमण्डलु माला। शुभ्र वर्ण तनु नयन विशाला॥५॥
ध्यान धरत पुलकित हित होई। सुख उपजत दुःख दुर्मति खोई॥६॥
कामधेनु तुम सुर तरु छाया। निराकार की अद्भुत माया॥७॥
तुम्हरी शरण गहै जो कोई। तरै सकल संकट सों सोई॥८॥
सरस्वती लक्ष्मी तुम काली। दिपै तुम्हारी ज्योति निराली॥९॥
तुम्हरी महिमा पार न पावैं। जो शारद शत मुख गुन गावैं॥१०॥
चार वेद की मात पुनीता। तुम ब्रह्माणी गौरी सीता॥११॥
महामन्त्र जितने जग माहीं। कोउ गायत्री सम नाहीं॥१२॥
सुमिरत हिय में ज्ञान प्रकासै। आलस पाप अविद्या नासै॥१३॥
सृष्टि बीज जग जननि भवानी। कालरात्रि वरदा कल्याणी॥१४॥
ब्रह्मा विष्णु रुद्र सुर जेते। तुम सों पावें सुरता तेते॥१५॥
तुम भक्तन की भक्त तुम्हारे। जननिहिं पुत्र प्राण ते प्यारे॥१६॥
महिमा अपरम्पार तुम्हारी। जय जय जय त्रिपदा भयहारी॥१७॥
पूरित सकल ज्ञान विज्ञाना। तुम सम अधिक न जगमे आना॥१८॥
तुमहिं जानि कछु रहै न शेषा। तुमहिं पाय कछु रहै न कलेशा॥१९॥
जानत तुमहिं तुमहिं व्है जाई। पारस परसि कुधातु सुहाई॥२०॥
तुम्हरी शक्ति दिपै सब ठाई। माता तुम सब ठौर समाई॥२१॥
ग्रह नक्षत्र ब्रह्माण्ड घनेरे। सब गतिवान तुम्हारे प्रेरे॥२२॥
सकल सृष्टि की प्राण विधाता। पालक पोषक नाशक त्राता॥२३॥
मातेश्वरी दया व्रत धारी। तुम सन तरे पातकी भारी॥२४॥
जापर कृपा तुम्हारी होई। तापर कृपा करें सब कोई॥२५॥
मन्द बुद्धि ते बुधि बल पावें। रोगी रोग रहित हो जावें॥२६॥
दरिद्र मिटै कटै सब पीरा। नाशै दुःख हरै भव भीरा॥२७॥
गृह क्लेश चित चिन्ता भारी। नासै गायत्री भय हारी॥२८॥
सन्तति हीन सुसन्तति पावें। सुख संपति युत मोद मनावें॥२९॥
भूत पिशाच सबै भय खावें। यम के दूत निकट नहिं आवें॥३०॥
जो सधवा सुमिरें चित लाई। अछत सुहाग सदा सुखदाई॥३१॥
घर वर सुख प्रद लहैं कुमारी। विधवा रहें सत्य व्रत धारी॥३२॥
जयति जयति जगदम्ब भवानी। तुम सम ओर दयालु न दानी॥३३॥
जो सतगुरु सो दीक्षा पावे। सो साधन को सफल बनावे॥३४॥
सुमिरन करे सुरूचि बडभागी। लहै मनोरथ गृही विरागी॥३५॥
अष्ट सिद्धि नवनिधि की दाता। सब समर्थ गायत्री माता॥३६॥
ऋषि मुनि यती तपस्वी योगी। आरत अर्थी चिन्तित भोगी॥३७॥
जो जो शरण तुम्हारी आवें। सो सो मन वांछित फल पावें॥३८॥
बल बुधि विद्या शील स्वभाउ। धन वैभव यश तेज उछाउ॥३९॥
सकल बढें उपजें सुख नाना। जे यह पाठ करै धरि ध्याना॥४०॥

॥ दोहा ॥
यह चालीसा भक्ति युत, पाठ करै जो कोई।
तापर कृपा प्रसन्नता, गायत्री की होय॥"""

meaning = """॥ श्री गायत्री माता चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "ह्रीं श्रीं क्लीं मेधा प्रभा, जीवन ज्योति प्रचण्ड। शान्ति कान्ति जागृत प्रगति, रचना शक्ति अखण्ड॥"
भावार्थ: हे माँ गायत्री! आप ह्रीं (शक्ति), श्रीं (ऋद्धि-सिद्धि-लक्ष्मी) और क्लीं (आनंद-आकर्षण) महाबीज स्वरूप हैं; आप बुद्धि की मेधा, दिव्य प्रभा और चराचर में जाज्वल्यमान अखंड जीवन-ज्योति हैं। आप जीवन में शांति, दिव्य कांति, आत्म-जागृति, निरंतर प्रगति और ब्रह्मांड की अटूट सृजन शक्ति प्रदान करने वाली हैं।
• "जगत जननी मङ्गल करनि, गायत्री सुखधाम। प्रणवों सावित्री स्वधा, स्वाहा पूरन काम॥"
भावार्थ: हे संपूर्ण जगत को जन्म देने वाली जगज्जननी, सर्वमंगलकारिणी, सुखों का पावन धाम माँ गायत्री! आप ही ओंकार (प्रणव), साक्षात् सावित्री, पितरों की तृप्ति रूप 'स्वधा', देवताओं की आहुति रूप 'स्वाहा' और भक्तों के समस्त मनोरथ पूर्ण करने वाली हैं।

【४० चौपाइयां — पद्यवार भावार्थ】
१-४. "भूर्भुवः स्वः ॐ युत जननी... स्वर्ण कान्ति शुचि गगन-बिहारी॥"
भावार्थ: हे भूः (भूलोक), भुवः (अन्तरिक्ष), स्वः (स्वर्गलोक) और ओंकार युक्त महामन्त्र स्वरूपा माता! आप कलियुग के समस्त पापों और मलों को भस्म करने वाली हैं। आपके गायत्री महामन्त्र के चौबीस अक्षर अत्यंत पवित्र हैं; इन चौबीस अक्षरों में समस्त वेद, शास्त्र, उपनिषद, श्रुतियां और श्रीमद्भगवद्गीता समाहित हैं। आप नित्य शाश्वत, सतोगुण की अधिष्ठात्री और सत्य स्वरूप हैं; आप सनातन सत्य और अलौकिक अमृत के समान हैं। आप श्वेत हंस पर आरूढ़, निर्मल श्वेत वस्त्र धारण करने वाली, सुवर्ण के समान दिव्य कांति वाली और चिदाकाश (गगन) में विचरण करने वाली हैं।

५-८. "पुस्तक पुष्प कमण्डलु माला... तरै सकल संकट सों सोई॥"
भावार्थ: आपके कर-कमलों में ज्ञान की प्रतीक पुस्तक, सौंदर्य का प्रतीक श्वेत पुष्प, पवित्रता का कमण्डलु और जप की पावन माला सुशोभित है; आपका वर्ण श्वेत-शुभ्र और नेत्र विशाल व करुणामयी हैं। आपके स्वरूप का ध्यान धरते ही हृदय पुलकित हो उठता है; समस्त दुःखों और दुर्बुद्धि का नाश होकर अखंड सुख की उत्पत्ति होती है। आप देवलोक की कामधेनु गाय और कल्पवृक्ष की शीतल छाया के समान हैं; आप निराकार परब्रह्म की साक्षात् अद्भुत लीला-माया हैं। जो भी मनुष्य आपकी पावन शरण ग्रहण करता है, वह जीवन के समस्त संकटों और भयों से सहज ही पार उतर जाता है।

९-१२. "सरस्वती लक्ष्मी तुम काली... कोउ गायत्री सम नाहीं॥"
भावार्थ: आप ही विद्या की देवी सरस्वती, धन-ऐश्वर्य की अधिष्ठात्री महालक्ष्मी और दुष्ट-दलिनी महाकाली हैं; आपकी ज्योति त्रिलोकी में सबसे अनूठी व तेजोमयी है। यदि साक्षात् सरस्वती जी भी सौ मुखों से आपके गुणों का निरंतर गान करें, तो भी वे आपकी असीम महिमा का पार नहीं पा सकतीं। आप चारों वेदों (ऋग, यजुः, साम, अथर्व) को प्रकट करने वाली परम पुनीत वेदमाता हैं; आप ही ब्रह्माणी, शिवा (गौरी) और माता सीता हैं। इस चराचर जगत में जितने भी वैदिक व तांत्रिक महामन्त्र विद्यमान हैं, उनमें कोई भी मन्त्र गायत्री महामन्त्र के समान प्रभावशाली व श्रेष्ठ नहीं है।

१३-१६. "सुमिरत हिय में ज्ञान प्रकासै... जननिहिं पुत्र प्राण ते प्यारे॥"
भावार्थ: आपका स्मरण करते ही साधक के हृदय में आत्मज्ञान का दिव्य प्रकाश फैल जाता है और आलस्य, पाप, अज्ञान व अविद्या का समूल नाश हो जाता है। आप ही संपूर्ण सृष्टि का बीज और जगत को रचने वाली भवानी हैं; संहार काल में कालरात्रि और भक्तों के लिए सर्वकल्याणकारी वरदायिनी हैं। ब्रह्मा, विष्णु, महेश तथा समस्त देवता जो दिव्य देवत्व (सुरता) धारण करते हैं, वह सब आपकी ही कृपा से प्राप्त करते हैं। आप भक्तों की रक्षक हैं और भक्त आपके प्रिय हैं; जैसे माता को अपना पुत्र प्राणों से भी अधिक प्रिय होता है, वैसे ही आप अपने साधकों से स्नेह करती हैं।

१७-२०. "महिमा अपरम्पार तुम्हारी... पारस परसि कुधातु सुहाई॥"
भावार्थ: हे माँ! आपकी महिमा अत्यंत अपरंपार है; हे त्रिपदा (तीन चरणों वाली) गायत्री! आप जन्म-मृत्यु के भय को हरने वाली हैं, आपकी सदा जय हो। आप संपूर्ण ज्ञान और विज्ञान (ब्रह्मविद्या व भौतिक विज्ञान) से परिपूर्ण हैं; जगत में आपके समकक्ष या आपसे श्रेष्ठ कोई अन्य शक्ति नहीं है। आपको जान लेने के उपरांत संसार में कुछ भी जानना शेष नहीं रहता और आपको प्राप्त कर लेने पर जीव के समस्त क्लेश समाप्त हो जाते हैं। जो आपका साक्षात्कार कर लेता है, वह स्वयं ब्रह्ममय हो जाता है; जैसे पारस पत्थर के स्पर्श से निकृष्ट लोहा भी बहुमूल्य सुवर्ण बन जाता है।

२१-२४. "तुम्हरी शक्ति दिपै सब ठाई... तुम सन तरे पातकी भारी॥"
भावार्थ: आपकी पराशक्ति समस्त ब्रह्मांड में व्याप्त और प्रकाशित है; हे माता! आप कण-कण में समाई हुई हैं। आकाशगंगाओं में स्थित अनगिनत ग्रह, नक्षत्र और ब्रह्मांडीय पिण्ड केवल आपकी प्रेरणा और गति-शक्ति से नियमबद्ध भ्रमण कर रहे हैं। आप संपूर्ण सृष्टि की जीवनदायिनी प्राण-विधाता हैं; आप ही जीवों की पालक, पोषक, संहारक और मोक्षदाता रक्षिका हैं। हे दया का व्रत धारण करने वाली करुणामयी मातेश्वरी! आपकी शरण में आकर बड़े से बड़े पापी भी परम पावन होकर भवसागर तर गए।

२५-२८. "जापर कृपा तुम्हारी होई... नासै गायत्री भय हारी॥"
भावार्थ: हे माता! जिस पर आपकी एक बार कृपा हो जाती है, उस पर संसार के समस्त देवी-देवता और जन-समुदाय स्वतः कृपा करने लगते हैं। मंदबुद्धि और मतिहीन मनुष्य भी तीव्र बुद्धि, विवेक और आत्मबल प्राप्त कर लेते हैं तथा असाध्य रोगी भी पूर्णतः रोग-मुक्त व स्वस्थ हो जाते हैं। साधक की दरिद्रता दूर हो जाती है, समस्त शारीरिक-मानसिक पीड़ाएं मिट जाती हैं और सांसारिक दुःखों व भव-भय का नाश हो जाता है। घर के आपसी कलह, अशांति और चित्त की भारी चिंताएं भयहारिणी माँ गायत्री के स्मरण से तत्काल नष्ट हो जाती हैं।

२९-३२. "सन्तति हीन सुसन्तति पावें... विधवा रहें सत्य व्रत धारी॥"
भावार्थ: संतानहीन दंपत्ति संस्कारी व दीर्घायु संतान प्राप्त करते हैं और घर में सुख-समृद्धि व आनंद का उत्सव मनाते हैं। आपके नाम के प्रभाव से भूत, प्रेत, पिशाच आदि नकारात्मक शक्तियां भयभीत होकर भाग जाती हैं और यमराज के दूत भी साधक के निकट नहीं आते। जो सौभाग्यवती स्त्रियां एकाग्रचित्त होकर आपका ध्यान करती हैं, उन्हें अखंड सौभाग्य (अक्षत सुहाग) और सुख प्राप्त होता है। कुंवारी कन्याओं को मनोनुकूल श्रेष्ठ वर व उत्तम कुल की प्राप्ति होती है और विधवाएं सत्य व पवित्र व्रत का पालन करते हुए आत्म-शांति पाती हैं।

३३-३६. "जयति जयति जगदम्ब भवानी... सब समर्थ गायत्री माता॥"
भावार्थ: हे जगदम्बे भवानी! आपकी जय हो, जय हो! संसार में आपके समान कोई अन्य परम दयालु और मुक्ति-भुक्ति का दाता नहीं है। जो साधक सद्गुरु से गायत्री मन्त्र की दीक्षा प्राप्त करता है, वह अपनी समस्त आध्यात्मिक साधनाओं को सहज ही सिद्ध कर लेता है। जो सौभाग्यशाली मनुष्य सुरुचिपूर्ण भक्ति से आपका स्मरण करता है, चाहे वह गृहस्थ हो या विरक्त संन्यासी, वह अपने समस्त मनोवांछित लक्ष्यों को प्राप्त कर लेता है। हे सर्वसमर्थ गायत्री माता! आप अष्ट सिद्धियों और नौ निधियों की साक्षात् दात्री हैं।

३७-४०. "ऋषि मुनि यती तपस्वी योगी... जे यह पाठ करै धरि ध्याना॥"
भावार्थ: ऋषि, मुनि, यति, तपस्वी, योगी, अथवा दुःखी, आर्त, धनार्थी, चिंतातुर व संसारी मनुष्य—जो-जो भी आपकी पावन शरण में आते हैं, वे सब मनवांछित फल प्राप्त करते हैं। जो भी साधक एकाग्रचित्त होकर माँ गायत्री का ध्यान धरते हुए इस चालीसा का पाठ करता है, उसका आत्मबल, बुद्धि, विद्या, शील, सदाचार, धन, ऐश्वर्य, यश और तेज निरंतर बढ़ता है तथा उसके जीवन में नाना प्रकार के अलौकिक सुख प्रकट होते हैं।

【समापन दोहा】
• "यह चालीसा भक्ति युत, पाठ करै जो कोई। तापर कृपा प्रसन्नता, गायत्री की होय॥"
भावार्थ: जो भी श्रद्धालु भक्तजन पूर्ण भक्तिभाव और निष्ठा के साथ इस पावन गायत्री चालीसा का नित्य पाठ करता है, उस पर जगज्जननी वेदमाता गायत्री की अखंड कृपा, प्रसन्नता और वरदान सदैव बने रहते हैं।"""

vidhi = """॥ श्री गायत्री माता चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय (त्रिकाल संध्या):
- प्रातःकाल: ब्रह्ममुहूर्त अथवा सूर्योदय काल (प्रातः संध्या) — यह समय विद्या, बुद्धि, मेधा और आत्मबल की प्राप्ति हेतु सर्वश्रेष्ठ है।
- मध्याह्न काल: दोपहर १२ बजे (माध्यंदिन संध्या) — तेज और ऐश्वर्य प्राप्ति हेतु।
- सायं काल: सूर्यास्त के समय (सायं संध्या) — मानसिक शांति, पाप-मुक्ति और पारिवारिक क्लेश निवारण हेतु।
- विशेष पावन तिथियां: गायत्री जयंती (ज्येष्ठ शुक्ल एकादशी / गंगा दशहरा), प्रत्येक मास की पूर्णिमा, रविवार, नवरात्रि, तथा गुरु पूर्णिमा।

२. दिशा, आसन व वस्त्र:
- दिशा: पूर्व दिशा की ओर मुख करके बैठना सर्वोत्तम है (उदीयमान सूर्य की ओर)। सांध्यकाल में पश्चिम या उत्तर दिशा में मुख कर सकते हैं।
- आसन: कुश, श्वेत कम्बल अथवा पीले ऊनी आसन पर बैठें।
- वस्त्र: स्वच्छ श्वेत (सफेद) अथवा पीले वस्त्र धारण करें।

३. पूजन सामग्री व दीप प्रज्वलन:
- दीपक: गाय के शुद्ध देशी घी का एकमुखी दीपक प्रज्वलित करें।
- पुष्प: श्वेत पुष्प (श्वेत कमल, चमेली, मोगरा, चांदनी) अथवा पीले गेंदे के फूल।
- चंदन व तिलक: श्वेत चंदन अथवा पीला चंदन और अक्षत।
- प्रिय भोग/नैवेद्य: गाय का कच्चा दूध, मिश्री, खीर, श्वेत पेड़ा, फल (विशेषकर केला/सेब), अथवा पंचामृत।
- जल कलश: तांबे अथवा पीतल के पात्र में शुद्ध जल, गंगाजल और तुलसी पत्र रखकर वेदी पर स्थापित करें।

४. सूर्य अर्घ्य व गायत्री मन्त्र का पावन समन्वय:
- पाठ से पूर्व तांबे के लोटे में जल, अक्षत, रोली और लाल पुष्प डालकर भगवान सूर्यदेव को 'ॐ सूर्याय नमः' अथवा गायत्री मन्त्र बोलते हुए तीन बार अर्घ्य प्रदान करें।
- अर्घ्य के उपरांत तुलसी या रुद्राक्ष की माला से गायत्री महामन्त्र:
  'ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात्।'
  का कम से कम १ माला (१०८ बार) अथवा ११/२१ बार जप अवश्य करें।

५. प्रामाणिक पाठ क्रम:
- सर्वप्रथम पवित्रीकरण, आचमन और शिखा-बंधन करें।
- हाथ में जल व पुष्प लेकर पाठ का संकल्प लें।
- वेदमूर्ति तपोनिष्ठ गुरुदेव व भगवान गणेश जी का स्मरण कर ध्यान करें।
- एकाग्रचित्त होकर श्री गायत्री माता चालीसा का १, ३, ७, ११ अथवा २१ बार पाठ करें (विद्यार्थी नित्य ३ पाठ करें)।
- पाठ समाप्ति के उपरांत माँ गायत्री की पावन आरती गाएं और कलश के पवित्र जल का सम्पूर्ण घर में छिड़काव कर चरणामृत व प्रसाद ग्रहण करें।"""

significance = """॥ श्री गायत्री माता चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. चौबीस दिव्य शक्तियों का जागरण (२४ अक्षर रहस्य):
"अक्षर चौविस परम पुनीता। इनमें बसें शास्त्र श्रुति गीता॥"
गायत्री महामन्त्र के २४ अक्षरों में ब्रह्मांड की २४ दिव्य शक्तियां, २४ गुण और २४ ऋषि-तत्व समाहित हैं। चालीसा के पाठ से साधक के शरीर में स्थित २४ सूक्ष्म ऊर्जा-ग्रंथियां और षट्चक्र जाग्रत होते हैं, जिससे कुंडलिनी शक्ति का ऊर्ध्वगमन होता है।

२. मेधा, तीव्र बुद्धि व विद्या की अचूक सिद्धि:
"मन्द बुद्धि ते बुधि बल पावें... बल बुधि विद्या शील स्वभाउ॥"
माँ गायत्री ज्ञान, विवेक और सद्बुद्धि की मूल अधिष्ठात्री हैं। जो विद्यार्थी या बौद्धिक कार्य करने वाले साधक नित्य इस चालीसा का पाठ करते हैं, उनकी विस्मृति दूर होती है, ग्रहण-शक्ति व स्मरण-शक्ति आश्चर्यजनक रूप से बढ़ती है और वे शिक्षा व प्रतियोगिता में अद्वितीय सफलता प्राप्त करते हैं।

३. महामन्त्र का अमृत फल:
"महामन्त्र जितने जग माहीं। कोउ गायत्री सम नाहीं॥"
सनातन धर्म में गायत्री को वेदों की जननी (वेदमाता) और मन्त्रों का शिरोमणि माना गया है। चालीसा के पाठ से करोड़ों गायत्री मन्त्रों के जप का पुण्य-फल और तेज सहज ही सुलभ हो जाता है।

४. दरिद्रता, गृह-क्लेश व मानसिक अवसाद का निवारण:
"दरिद्र मिटै कटै सब पीरा... गृह क्लेश चित चिन्ता भारी॥"
गायत्री चालीसा का पाठ घर में सकारात्मक ऊर्जा (पॉजिटिव ऑरा) का संचार करता है। इससे पारिवारिक कलह, मानसिक तनाव, डिप्रेशन, आर्थिक तंगी और दुर्भाग्य का नाश होकर घर में सुख, शांति व लक्ष्मी का स्थायी वास होता है।

५. भूत-प्रेत, नजर दोष व अकाल मृत्यु से सुरक्षा:
"भूत पिशाच सबै भय खावें। यम के दूत निकट नहिं आवें॥"
माँ गायत्री का तेजोमय रक्षा-कवच साधक के चारों ओर निर्मित हो जाता है। इससे तामसिक शक्तियां, बुरी नजर, तांत्रिक मारण-उच्चाटन और अकाल मृत्यु का भय स्वतः दूर भाग जाते हैं।

६. अखण्ड सौभाग्य एवं उत्तम संतान की प्राप्ति:
"सन्तति हीन सुसन्तति पावें... अछत सुहाग सदा सुखदाई॥"
निसंतान दंपत्तियों को सद्गुणी, बुद्धिमान व दीर्घायु संतान की प्राप्ति होती है। सुहागिन स्त्रियों को अखण्ड सौभाग्य और कन्याओं को मनोनुकूल श्रेष्ठ वर व सुखी दांपत्य जीवन की प्राप्ति होती है।"""

english_lyrics = """॥ Shri Gayatri Mata Chalisa ॥

॥ Doha ॥
Hreem Shreem Kleem Medhaa Prabhaa, Jeevana Jyoti Prachanda।
Shaanti Kaanti Jaagrita Pragati, Rachanaa Shakti Akhanda॥
Jagata Jananee Mangala Karani, Gaayatree Sukhadhaama।
Pranavon Saavitree Swadhaa, Swaahaa Poorana Kaama॥

॥ Chaupai ॥
Bhoorbhuvah Svah Om Yuta Jananee। Gaayatree Nita Kalimala Dahanee॥1॥
Akshara Chaoubisa Parama Puneetaa। Inamen Basen Shaastra Shruti Geetaa॥2॥
Shaashwata Satoguni Sata Roopaa। Satya Sanaatana Sudhaa Anoopaa॥3॥
Hansaaroodha Sitaambara Dhaaree। Swarna Kaanti Shuchi Gagana-Bihaaree॥4॥
Pustaka Pushpa Kamandalu Maalaa। Shubhra Varna Tanu Nayana Vishaalaa॥5॥
Dhyaana Dharata Pulakita Hita Ho-ee। Sukha Upajata Dukha Durmati Kho-ee॥6॥
Kaamadhenu Tuma Sura Taru Chhaayaa। Niraakaara Kee Adbhuta Maayaa॥7॥
Tumharee Sharana Gahai Jo Ko-ee। Tarai Sakala Sankata Son So-ee॥8॥
Saraswatee Lakshmi Tuma Kaalee। Dipai Tumhaaree Jyoti Niraalee॥9॥
Tumhaaree Mahimaa Paara Na Paavain। Jo Shaarada Shata Mukha Guna Gaavain॥10॥
Chaara Veda Kee Maata Puneetaa। Tuma Brahmaanee Gauree Seetaa॥11॥
Mahaamantra Jitane Jaga Maaheen। Kou Gaayatree Sama Naaheen॥12॥
Sumirata Hiya Men Gyaana Prakaasai। Aalasa Paapa Avidyaa Naasai॥13॥
Srishti Beeja Jaga Janani Bhavaanee। Kaalaraatri Varadaa Kalyaanee॥14॥
Brahmaa Vishnu Rudra Sura Jete। Tuma Son Paaven Surataa Tete॥15॥
Tuma Bhaktana Kee Bhakta Tumhaare। Jananihin Putra Praana Te Pyaare॥16॥
Mahimaa Aparampaara Tumhaaree। Jaya Jaya Jaya Tripadaa Bhayahaaree॥17॥
Poorita Sakala Gyaana Vigyaanaa। Tuma Sama Adhika Na Jagame Aanaa॥18॥
Tumahin Jaani Kuchhu Rahai Na Sheshaa। Tumahin Paaya Kuchhu Rahai Na Kaleshaa॥19॥
Jaanata Tumahin Tumahin Vhai Jaa-ee। Paarasa Parasi Kudhaatu Suhaa-ee॥20॥
Tumhaaree Shakti Dipai Saba Thaa-ee। Maataa Tuma Saba Thoura Samaa-ee॥21॥
Graha Nakshatra Brahmaanda Ghanere। Saba Gativaana Tumhaare Prere॥22॥
Sakala Srishti Kee Praana Vidhaataa। Paalaka Poshaka Naashaka Traataa॥23॥
Maateshwaree Dayaa Vrata Dhaaree। Tuma Sana Tare Paatakee Bhaaree॥24॥
Jaapara Kripaa Tumhaaree Ho-ee। Taapara Kripaa Karain Saba Ko-ee॥25॥
Manda Buddhi Te Budhi Bala Paaven। Rogee Roga Rahita Ho Jaaven॥26॥
Daridra Mitai Katai Saba Peeraa। Naashai Dukha Harai Bhava Bheeraa॥27॥
Griha Klesha Chita Chintaa Bhaaree। Naasai Gaayatree Bhaya Haaree॥28॥
Santati Heena Susantati Paaven। Sukha Sampati Yuta Moda Manaaven॥29॥
Bhoota Pishaacha Sabai Bhaya Khaaven। Yama Ke Doota Nikata Nahin Aaven॥30॥
Jo Sadhavaa Sumirain Chita Laa-ee। Achhata Suhaaga Sadaa Sukhadaa-ee॥31॥
Ghara Vara Sukha Prada Lahain Kumaaree। Vidhavaa Rahain Satya Vrata Dhaaree॥32॥
Jayati Jayati Jagadamba Bhavaanee। Tuma Sama Ora Dayaalu Na Daanee॥33॥
Jo Sataguru So Deekshaa Paave। So Saadhana Ko Saphala Banaave॥34॥
Sumirana Kare Suroochi Badabhaagee। Lahai Manoratha Grihee Viraagee॥35॥
Ashta Siddhi Navanidhi Kee Daataa। Saba Samartha Gaayatree Maataa॥36॥
Rishi Muni Yatee Tapasvee Yogee। Aarata Arthee Chintita Bhogee॥37॥
Jo Jo Sharana Tumhaaree Aaven। So So Mana Vaanchhita Phala Paaven॥38॥
Bala Budhi Vidyaa Sheela Swabhaau। Dhana Vaibhava Yasha Teja Uchhaau॥39॥
Sakala Badhain Upajen Sukha Naanaa। Je Yaha Paatha Karai Dhari Dhyaanaa॥40॥

॥ Doha ॥
Yaha Chaaleesaa Bhakti Yuta, Paatha Karai Jo Ko-ee।
Taapara Kripaa Prasannataa, Gaayatree Kee Hoya॥"""

# 1. Update drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["gayatri"]["items"]:
    if item["id"] == "drik_chalisa_24":
        item["title"] = "गायत्री माता चालीसा"
        item["title_en"] = "Shri Gayatri Mata Chalisa"
        item["en_line"] = "Hrim Shrim Klim Medha Prabha Jeevan Jyoti"
        item["hi_line"] = "ह्रीं श्रीं क्लीं मेधा प्रभा जीवन ज्योति"
        item["sub"] = "ह्रीं श्रीं क्लीं मेधा प्रभा जीवन ज्योति • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_gayatri_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=RMRAIZdZzwM"
        item["video_id"] = "RMRAIZdZzwM"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/gayatri-mata/gayatri-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "वेदमाता गायत्री व माँ तुलसी भगवती"
        item["section"] = "माँ गायत्री व तुलसी चालीसा"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_24 in drik_chalisa_collections.json successfully!")

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

# 3. Add chalisa_gayatri in CONTENT in app.js
content_obj = {
    "title": "गायत्री माता चालीसा",
    "title_en": "Shri Gayatri Mata Chalisa",
    "en_line": "Hrim Shrim Klim Medha Prabha Jeevan Jyoti",
    "hi_line": "ह्रीं श्रीं क्लीं मेधा प्रभा जीवन ज्योति",
    "sub": "ह्रीं श्रीं क्लीं मेधा प्रभा जीवन ज्योति • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_gayatri_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=RMRAIZdZzwM",
    "video_id": "RMRAIZdZzwM",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/gayatri-mata/gayatri-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "वेदमाता गायत्री व माँ तुलसी भगवती",
    "section": "माँ गायत्री व तुलसी चालीसा",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

gayatri_content_js = "  chalisa_gayatri: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_gayatri: {" in app_text:
    m_start = app_text.find("  chalisa_gayatri: {")
    m_end = app_text.find("\n  chalisa_", m_start + 1)
    if m_end == -1:
        m_end = app_text.find("\n  sundarkand:", m_start + 1)
    if m_end != -1:
        app_text = app_text[:m_start] + gayatri_content_js + app_text[m_end+1:]
        print("Replaced existing chalisa_gayatri in CONTENT!")
else:
    # Insert right after chalisa_narmada
    n_pos = app_text.find("  chalisa_narmada: {")
    if n_pos != -1:
        n_end = app_text.find("\n  chalisa_", n_pos + 1)
        if n_end == -1:
            n_end = app_text.find("\n  sundarkand:", n_pos + 1)
        if n_end != -1:
            app_text = app_text[:n_end+1] + gayatri_content_js + app_text[n_end+1:]
            print("Inserted chalisa_gayatri after chalisa_narmada in CONTENT!")
    else:
        v_pos = app_text.find("  chalisa_vishwakarma: {")
        if v_pos != -1:
            app_text = app_text[:v_pos] + gayatri_content_js + app_text[v_pos:]
            print("Inserted chalisa_gayatri before chalisa_vishwakarma in CONTENT!")

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
