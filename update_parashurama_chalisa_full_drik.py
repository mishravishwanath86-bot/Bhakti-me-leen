import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Authentic Devanagari Lyrics from Drik Panchang
parashurama_chalisa_content = """॥ भगवान परशुराम चालीसा ॥
(भगवान विष्णु के षष्ठ अवतार • भाषा: अवधी / ब्रज)

॥ दोहा ॥
श्री गुरु चरण सरोज छवि, निज मन मन्दिर धारि।
सुमरि गजानन शारदा, गहि आशिष त्रिपुरारि॥

बुद्धिहीन जन जानिये, अवगुणों का भण्डार।
बरणों परशुराम सुयश, निज मति के अनुसार॥

॥ चौपाई ॥
जय प्रभु परशुराम सुख सागर। जय मुनीश गुण ज्ञान दिवाकर॥
भृगुकुल मुकुट विकट रणधीरा। क्षत्रिय तेज मुख संत शरीरा॥

जमदग्नी सुत रेणुका जाया। तेज प्रताप सकल जग छाया॥
मास बैसाख सित पच्छ उदारा। तृतीया पुनर्वसु मनुहारा॥

प्रहर प्रथम निशा शीत न घामा। तिथि प्रदोष व्यापि सुखधामा॥
तब ऋषि कुटीर रूदन शिशु कीन्हा। रेणुका कोखि जनम हरि लीन्हा॥

निज घर उच्च ग्रह छः ठाढ़े। मिथुन राशि राहु सुख गाढ़े॥
तेज-ज्ञान मिल नर तनु धारा। जमदग्नी घर ब्रह्म अवतारा॥

धरा राम शिशु पावन नामा। नाम जपत जग लह विश्रामा॥
भाल त्रिपुण्ड जटा सिर सुन्दर। कांधे मुंज जनेऊ मनहर॥

मंजु मेखला कटि मृगछाला। रूद्र माला बर वक्ष विशाला॥
पीत बसन सुन्दर तनु सोहें। कंध तुणीर धनुष मन मोहें॥

वेद-पुराण-श्रुति-स्मृति ज्ञाता। क्रोध रूप तुम जग विख्याता॥
दायें हाथ श्रीपरशु उठावा। वेद-संहिता बायें सुहावा॥

विद्यावान गुण ज्ञान अपारा। शास्त्र-शस्त्र दोउ पर अधिकारा॥
भुवन चारिदस अरु नवखंडा। चहुं दिशि सुयश प्रताप प्रचंडा॥

एक बार गणपति के संगा। जूझे भृगुकुल कमल पतंगा॥
दांत तोड़ रण कीन्ह विरामा। एक दंत गणपति भयो नामा॥

कार्तवीर्य अर्जुन भूपाला। सहस्रबाहु दुर्जन विकराला॥
सुरगऊ लखि जमदग्नी पांहीं। रखिहहुं निज घर ठानि मन मांहीं॥

मिली न मांगि तब कीन्ह लड़ाई। भयो पराजित जगत हंसाई॥
तन खल हृदय भई रिस गाढ़ी। रिपुता मुनि सौं अतिसय बाढ़ी॥

ऋषिवर रहे ध्यान लवलीना। तिन्ह पर शक्तिघात नृप कीन्हा॥
लगत शक्ति जमदग्नी निपाता। मनहुं क्षत्रिकुल बाम विधाता॥

पितु-बध मातु-रूदन सुनि भारा। भा अति क्रोध मन शोक अपारा॥
कर गहि तीक्षण परशु कराला। दुष्ट हनन कीन्हेउ तत्काला॥

क्षत्रिय रुधिर पितु तर्पण कीन्हा। पितु-बध प्रतिशोध सुत लीन्हा॥
इक्कीस बार भू क्षत्रिय बिहीनी। छीन धरा बिप्रन्ह कहँ दीनी॥

जुग त्रेता कर चरित सुहाई। शिव-धनु भंग कीन्ह रघुराई॥
गुरु धनु भंजक रिपु करि जाना। तब समूल नाश ताहि ठाना॥

कर जोरि तब राम रघुराई। बिनय कीन्ही पुनि शक्ति दिखाई॥
भीष्म द्रोण कर्ण बलवन्ता। भये शिष्या द्वापर महँ अनन्ता॥

शास्त्र विद्या देह सुयश कमावा। गुरु प्रताप दिगन्त फिरावा॥
चारों युग तव महिमा गाई। सुर मुनि मनुज दनुज समुदाई॥

दे कश्यप सों संपदा भाई। तप कीन्हा महेन्द्र गिरि जाई॥
अब लौं लीन समाधि नाथा। सकल लोक नावइ नित माथा॥

चारों वर्ण एक सम जाना। समदर्शी प्रभु तुम भगवाना॥
ललहिं चारि फल शरण तुम्हारी। देव दनुज नर भूप भिखारी॥

जो यह पढ़ै श्री परशु चालीसा। तिन्ह अनुकूल सदा गौरीसा॥
पृर्णेन्दु निसि बासर स्वामी। बसहु हृदय प्रभु अन्तरयामी॥

॥ दोहा ॥
परशुराम को चारू चरित, मेटत सकल अज्ञान।
शरण पड़े को देत प्रभु, सदा सुयश सम्मान॥

॥ श्लोक ॥
भृगुदेव कुलं भानुं, सहस्रबाहुर्मर्दनम्।
रेणुका नयना नंदं, परशुंवन्दे विप्रधनम्॥"""

# 2. Verse-by-verse Spiritual Meaning (पद्यवार सम्पूर्ण पावन भावार्थ)
parashurama_chalisa_meaning = """॥ भगवान परशुराम चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【आरम्भिक दोहे】
दोहा १:
श्री गुरु चरण सरोज छवि, निज मन मन्दिर धारि।
सुमरि गजानन शारदा, गहि आशिष त्रिपुरारि॥
भावार्थ: श्री सद्गुरुदेव के चरण-कमलों की दिव्य छवि को अपने हृदय-मन्दिर में धारण करके, प्रथम पूज्य श्री गणेश जी एवं माँ सरस्वती का स्मरण कर तथा देवाधिदेव महादेव शिव जी का पावन आशीर्वाद ग्रहण करके—

दोहा २:
बुद्धिहीन जन जानिये, अवगुणों का भण्डार।
बरणों परशुराम सुयश, निज मति के अनुसार॥
भावार्थ: मैं स्वयं को बुद्धिहीन और समस्त दुर्गुणों का भण्डार जानकर, परम प्रतापी भगवान परशुराम जी के अलौकिक यश का अपनी बुद्धि और मति के अनुसार भक्तिपूर्वक वर्णन करता हूँ।

【चौपाइयां — भावार्थ】
१. जय प्रभु परशुराम सुख सागर। जय मुनीश गुण ज्ञान दिवाकर॥
भृगुकुल मुकुट विकट रणधीरा। क्षत्रिय तेज मुख संत शरीरा॥
भावार्थ: सुखों के अपार सागर भगवान श्री परशुराम जी की जय हो! मुनियों में श्रेष्ठ, सद्गुणों व आत्म-ज्ञान के साक्षात् सूर्यदेव आपकी जय हो! आप भृगुवंश के मुकुटमणि और युद्धभूमि में अत्यंत पराक्रमी व धीर-वीर हैं। आपके मुख पर क्षत्रियोचित प्रचंड तेज और शरीर संतों के समान परम पावन है।

२. जमदग्नी सुत रेणुका जाया। तेज प्रताप सकल जग छाया॥
मास बैसाख सित पच्छ उदारा। तृतीया पुनर्वसु मनुहारा॥
भावार्थ: आप महर्षि जमदग्नि के सुपुत्र और माता रेणुका के गर्भ से उत्पन्न हुए। आपका अलौकिक तेज और प्रताप समस्त ब्रह्मांड में व्याप्त है। आपका प्राकट्य वैशाख मास के शुक्ल पक्ष की उदार एवं पावन तृतीया (अक्षय तृतीया) तिथि तथा पुनर्वसु नक्षत्र में हुआ।

३. प्रहर प्रथम निशा शीत न घामा। तिथि प्रदोष व्यापि सुखधामा॥
तब ऋषि कुटीर रूदन शिशु कीन्हा। रेणुका कोखि जनम हरि लीन्हा॥
भावार्थ: रात्रि के प्रथम प्रहर में, जब न अधिक शीत थी और न अधिक गर्मी, तथा सुखदायी प्रदोष काल व्याप्त था, तब महर्षि जमदग्नि की पावन कुटिया में दिव्य शिशु ने रुदन किया—साक्षात् श्री हरि विष्णु ने माता रेणुका की कोख से अवतार धारण किया।

४. निज घर उच्च ग्रह छः ठाढ़े। मिथुन राशि राहु सुख गाढ़े॥
तेज-ज्ञान मिल नर तनु धारा। जमदग्नी घर ब्रह्म अवतारा॥
भावार्थ: आपके जन्मोत्सव के समय कुंडली में छह उच्च ग्रह अपने-अपने घरों में स्थित थे और मिथुन राशि में राहु सुखद स्थिति में था। साक्षात् ब्रह्म-तेज और ज्ञान ने नर-शरीर धारण किया और महर्षि जमदग्नि के आश्रम में साक्षात् परब्रह्म अवतरित हुए।

५. धरा राम शिशु पावन नामा। नाम जपत जग लह विश्रामा॥
भाल त्रिपुण्ड जटा सिर सुन्दर। कांधे मुंज जनेऊ मनहर॥
भावार्थ: शिशु का पावन नाम 'राम' रखा गया, जिसके पावन नाम का जप करने से सम्पूर्ण संसार को परम शांति और विश्राम मिलता है। आपके मस्तक पर भस्म का सुंदर त्रिपुण्ड, सिर पर तपस्वियों जैसी जटाएं और कंधे पर मूंज की बनी पवित्र यज्ञोपवीत (जनेऊ) सुशोभित है।

६. मंजु मेखला कटि मृगछाला। रूद्र माला बर वक्ष विशाला॥
पीत बसन सुन्दर तनु सोहें। कंध तुणीर धनुष मन मोहें॥
भावार्थ: आपकी कमर में सुंदर मेखला और मृगचर्म बंधा है, विशाल वक्षस्थल पर रुद्राक्ष की माला शोभायमान है। आपके गौर-श्याम शरीर पर दिव्य पीताम्बर सुशोभित है, कंधे पर बाणों से भरा तरकश और विशाल धनुष मन को मोहित करता है।

७. वेद-पुराण-श्रुति-स्मृति ज्ञाता। क्रोध रूप तुम जग विख्याता॥
दायें हाथ श्रीपरशु उठावा। वेद-संहिता बायें सुहावा॥
भावार्थ: आप चारों वेदों, अठारह पुराणों, श्रुतियों और स्मृतियों के परम मर्मज्ञ ज्ञाता हैं। धर्म और न्याय की रक्षा हेतु अधर्मियों पर आपका रौद्र रूप संसार में विख्यात है। आपके दाहिने हाथ में तीक्ष्ण परशु (फरसा) और बायें हाथ में ज्ञानमयी वेद-संहिता सुशोभित है।

८. विद्यावान गुण ज्ञान अपारा। शास्त्र-शस्त्र दोउ पर अधिकारा॥
भुवन चारिदस अरु नवखंडा। चहुं दिशि सुयश प्रताप प्रचंडा॥
भावार्थ: आप अपार विद्या, ज्ञान और सद्गुणों के सागर हैं। आपका शास्त्र (आध्यात्मिक ज्ञान) और शस्त्र (युद्ध कौशल) दोनों पर समान पूर्ण अधिकार है। चौदह भुवनों और नौ खण्डों में आपका प्रचण्ड तेज और पावन सुयश चारों दिशाओं में गूंजता है।

९. एक बार गणपति के संगा। जूझे भृगुकुल कमल पतंगा॥
दांत तोड़ रण कीन्ह विरामा। एक दंत गणपति भयो नामा॥
भावार्थ: एक बार कैलाश द्वार पर प्रथम पूज्य श्री गणेश जी के साथ आपका युद्ध हुआ। युद्ध में आपने शिव जी द्वारा प्रदत्त अमोघ परशु का प्रहार किया, जिसे सम्मान देते हुए गणेश जी ने अपने एक दांत पर झेला और वह टूट गया। तब से श्री गणेश जी का नाम संसार में 'एकदंत' विख्यात हुआ।

१०. कार्तवीर्य अर्जुन भूपाला। सहस्रबाहु दुर्जन विकराला॥
सुरगऊ लखि जमदग्नी पांहीं। रखिहहुं निज घर ठानि मन मांहीं॥
भावार्थ: महिष्मती का राजा सहस्रबाहु (कार्तवीर्यार्जुन) अत्यंत अभिमानी, क्रूर और दुष्ट था। जब उसने महर्षि जमदग्नि के आश्रम में अलौकिक कामधेनु सुरभि गऊ को देखा, तो उसने बलपूर्वक उसे अपने घर ले जाने की कुत्सित ठान ली।

११. मिली न मांगि तब कीन्ह लड़ाई। भयो पराजित जगत हंसाई॥
तन खल हृदय भई रिस गाढ़ी। रिपुता मुनि सौं अतिसय बाढ़ी॥
भावार्थ: जब मुनि ने कामधेनु देने से मना कर दिया, तब सहस्रबाहु ने सेना सहित युद्ध छेड़ा, किंतु भगवान परशुराम के हाथों बुरी तरह पराजित हुआ और संसार में उसकी भारी जग-हंसाई हुई। इससे उस दुष्ट के हृदय में भीषण प्रतिशोध की आग भड़क उठी और मुनि से उसकी शत्रुता अत्यंत बढ़ गई।

१२. ऋषिवर रहे ध्यान लवलीना। तिन्ह पर शक्तिघात नृप कीन्हा॥
लगत शक्ति जमदग्नी निपाता। मनहुं क्षत्रिकुल बाम विधाता॥
भावार्थ: अवसर पाकर जब महर्षि जमदग्नि समाधि में लीन थे, तब उस कायर राजा के पुत्रों ने उन पर शक्ति-बाणों से कायरतापूर्ण प्रहार किया। शक्ति के प्रहार से महर्षि जमदग्नि ब्रह्मलीन हो गए, मानो क्षत्रिय कुल का विधाता ही उनके विरुद्ध हो गया हो।

१३. पितु-बध मातु-रूदन सुनि भारा। भा अति क्रोध मन शोक अपारा॥
कर गहि तीक्षण परशु कराला। दुष्ट हनन कीन्हेउ तत्काला॥
भावार्थ: पिता की हत्या और माता रेणुका का विलाप सुनकर भगवान परशुराम के हृदय में अपार शोक और भयानक क्रोध उत्पन्न हुआ। उन्होंने हाथ में तीक्ष्ण और विकराल परशु धारण किया और तत्काल उस अधर्मी सहस्रबाहु व उसके समस्त दुष्ट पुत्रों का संहार कर दिया।

१४. क्षत्रिय रुधिर पितु तर्पण कीन्हा। पितु-बध प्रतिशोध सुत लीन्हा॥
इक्कीस बार भू क्षत्रिय बिहीनी। छीन धरा बिप्रन्ह कहँ दीनी॥
भावार्थ: आपने समंतपंचक तीर्थ में पिता का तर्पण कर पितृ-ऋण और प्रतिशोध पूर्ण किया। धर्म की मर्यादा स्थापित करने हेतु आपने पृथ्वी को इक्कीस बार अत्याचारी और अहंकारी राजाओं से रहित किया और जीती हुई सम्पूर्ण पृथ्वी महर्षि कश्यप आदि पवित्र ब्राह्मणों को दान कर दी।

१५. जुग त्रेता कर चरित सुहाई। शिव-धनु भंग कीन्ह रघुराई॥
गुरु धनु भंजक रिपु करि जाना। तब समूल नाश ताहि ठाना॥
भावार्थ: त्रेता युग में जब भगवान श्री रामचन्द्र जी ने जनकपुर में भगवान शिव के 'पिनाक' धनुष को तोड़ा, तब अपने आराध्य गुरु शिव के धनुष का भंजन सुनकर आप क्रोधित होकर वहाँ पधारे और उसे अपना शत्रु समझकर उसका नाश करने का संकल्प किया।

१६. कर जोरि तब राम रघुराई। बिनय कीन्ही पुनि शक्ति दिखाई॥
भीष्म द्रोण कर्ण बलवन्ता। भये शिष्या द्वापर महँ अनन्ता॥
भावार्थ: तब भगवान श्री राम ने हाथ जोड़कर अत्यंत विनम्रता से विनय की और अपने वैकुण्ठपति विष्णु स्वरूप का दिव्य तेज प्रकट किया, जिसे देखकर आप शांत व प्रसन्न हुए। द्वापर युग में महाबली पितामह भीष्म, गुरु द्रोणाचार्य और दानवीर कर्ण जैसे महारथी आपके ही शिष्य बने।

१७. शास्त्र विद्या देह सुयश कमावा। गुरु प्रताप दिगन्त फिरावा॥
चारों युग तव महिमा गाई। सुर मुनि मनुज दनुज समुदाई॥
भावार्थ: आपने शिष्यों को अमोघ दिव्यास्त्रों और नीति की शिक्षा देकर अद्वितीय सुयश अर्जित किया और अपने गुरु-प्रताप को दिग-दिगंत में फैलाया। चारों युगों में देवता, मुनि, मनुष्य और दानव सभी आपकी अनंत महिमा का गान करते हैं।

१८. दे कश्यप सों संपदा भाई। तप कीन्हा महेन्द्र गिरि जाई॥
अब लौं लीन समाधि नाथा। सकल लोक नावइ नित माथा॥
भावार्थ: सम्पूर्ण पृथ्वी महर्षि कश्यप को समर्पित कर, आप तपस्या करने हेतु महेन्द्र पर्वत पर पधारे। हे नाथ! आप आज भी महेन्द्र पर्वत पर चिरंजीवी रूप में समाधिस्थ हैं और सम्पूर्ण त्रिलोकी आपके चरणों में नित्य शीश झुकाती है।

१९. चारों वर्ण एक सम जाना। समदर्शी प्रभु तुम भगवाना॥
ललहिं चारि फल शरण तुम्हारी। देव दनुज नर भूप भिखारी॥
भावार्थ: आपने चारों वर्णों को समभाव से देखा, आप निष्पक्ष और साक्षात् समदर्शी भगवान हैं। जो भी प्राणी—चाहे वह देव, दानव, राजा हो या रंक—आपकी शरण ग्रहण करता है, वह धर्म, अर्थ, काम और मोक्ष—चारों फलों को सहज ही प्राप्त कर लेता है।

२०. जो यह पढ़ै श्री परशु चालीसा। तिन्ह अनुकूल सदा गौरीसा॥
पृर्णेन्दु निसि बासर स्वामी। बसहु हृदय प्रभु अन्तरयामी॥
भावार्थ: जो भी मनुष्य इस श्री परशुराम चालीसा का श्रद्धा से पाठ करता है, उस पर देवाधिदेव महादेव शिव जी सदैव प्रसन्न व अनुकूल रहते हैं। हे पूर्ण चन्द्रमा के समान शीतल और सूर्य के समान प्रतापी अंतर्यामी प्रभु! आप रात-दिन हमारे हृदय में निवास कीजिए।

【समापन दोहा व श्लोक】
॥ दोहा ॥
परशुराम को चारू चरित, मेटत सकल अज्ञान।
शरण पड़े को देत प्रभु, सदा सुयश सम्मान॥
भावार्थ: भगवान श्री परशुराम जी का यह परम पावन एवं मनोहर चरित्र साधक के समस्त अज्ञान, अंधकार और भय को मिटा देता है। जो भी इनकी शरण में आता है, प्रभु उसे जीवन भर श्रेष्ठ सुयश और मान-सम्मान प्रदान करते हैं।

॥ श्लोक ॥
भृगुदेव कुलं भानुं, सहस्रबाहुर्मर्दनम्।
रेणुका नयना नंदं, परशुंवन्दे विप्रधनम्॥
भावार्थ: भृगुकुल के तेजस्वी सूर्य, सहस्रबाहु के मद का मर्दन करने वाले, माता रेणुका के नेत्रों को आनंद देने वाले तथा विप्रों व धर्म के परम रक्षक भगवान परशुराम जी के चरणों में मैं बारम्बार वन्दना करता हूँ।"""

# 3. Authentic Worship Procedure & Rules (शास्त्रोक्त पाठ विधि व नियम)
parashurama_chalisa_vidhi = """॥ भगवान परशुराम चालीसा पाठ एवं पूजन विधि व नियम ॥

१. पावन काल व विशेष मुहूर्त:
• प्रतिदिन प्रातःकाल अथवा संध्याकाल में पाठ करना अत्यंत मंगलकारी है।
• विशेष रूप से वैशाख शुक्ल तृतीया (अक्षय तृतीया / परशुराम जयंती), प्रत्येक एकादशी, प्रदोष काल, तथा मंगलवार व रविवार के दिन इसका पाठ अनंत गुना फल प्रदान करता है।

२. आवश्यक पूजन सामग्री:
• भगवान परशुराम जी का पावन चित्र या विग्रह (हाथ में परशु व वेद-संहिता धारण किए हुए)।
• शुद्ध घी का दीपक, गुग्गल या चंदन की धूप, रोली, पीला चंदन, अक्षत (अखंड चावल)।
• पीले पुष्प, तुलसी दल, दूर्वा, गंगाजल, पंचामृत।
• नैवेद्य: जौ, सत्तू, बेसन के लड्डू, खीर, ताजे ऋतुफल एवं माखन-मिश्री।

३. शास्त्रोक्त पूजन विधान:
• प्रातः स्नानादि कर स्वच्छ पीले या श्वेत वस्त्र धारण करें।
• पूर्व अथवा उत्तर दिशा की ओर मुख करके कुशा या ऊन के पवित्र आसन पर बैठें।
• चौकी पर पीला वस्त्र बिछाकर भगवान परशुराम जी का चित्र स्थापित करें।
• दीपक प्रज्वलित कर सर्वप्रथम श्री गणेश जी एवं देवाधिदेव महादेव का स्मरण करें।
• 'ॐ ॐ ॐ जामदग्न्याय विद्महे महावीराय धीमहि तन्नो परशुरामः प्रचोदयात्' अथवा 'ॐ परशुरामाय नमः' मंत्र का उच्चारण करते हुए भगवान परशुराम जी को पीला चंदन लगाएं, पीले पुष्प और तुलसी दल अर्पित करें।
• हाथ में जल व अक्षत लेकर चालीसा पाठ का संकल्प लें और अत्यंत श्रद्धा, स्पष्ट वाणी व एकाग्रता से पाठ करें।
• पाठ पूर्ण होने पर परशुराम जी की आरती करें और सात्विक प्रसाद सभी में वितरित करें।

४. विशेष साधना नियम:
• भयमुक्ति, कोर्ट-कचहरी में विजय अथवा आत्मबल की वृद्धि हेतु लगातार २१ या ४० दिनों तक नित्य ३ बार इस चालीसा का पाठ करें।
• साधना काल में सात्विक आहार ग्रहण करें, असत्य भाषण से बचें तथा क्रोध व अहंकार का त्याग करें।"""

# 4. Spiritual Significance & Fruits (आध्यात्मिक महत्त्व व फलश्रुति)
parashurama_chalisa_significance = """॥ भगवान परशुराम चालीसा का आध्यात्मिक महत्त्व व फलश्रुति ॥

१. शास्त्र एवं शस्त्र विद्या का वरदान:
'शास्त्र-शस्त्र दोउ पर अधिकारा। चहुं दिशि सुयश प्रताप प्रचंडा॥'
भगवान परशुराम ज्ञान (वेद) और शक्ति (शौर्य) के अद्वितीय समन्वयक हैं। इनकी आराधना से विद्यार्थियों और साधकों को तीव्र बुद्धि, विद्या और अदम्य आत्मबल की प्राप्ति होती है।

२. अन्याय, भय व शत्रुओं का शमन:
'कर गहि तीक्षण परशु कराला। दुष्ट हनन कीन्हेउ तत्काला॥'
भगवान परशुराम की कृपा से साधक के जीवन के समस्त ज्ञात-अज्ञात शत्रु, ऊपरी बाधाएं, षड्यंत्र और भय तत्काल नष्ट हो जाते हैं। साधक निर्भय होकर धर्म के मार्ग पर अग्रसर होता है।

३. भगवान शिव की अखंड कृपा:
'जो यह पढ़ै श्री परशु चालीसा। तिन्ह अनुकूल सदा गौरीसा॥'
भगवान परशुराम देवाधिदेव शिव के अनन्य शिष्य हैं। इनका नित्य पाठ करने वाले साधक पर साक्षात् भगवान शंकर और माता पार्वती सदैव अनुकूल व प्रसन्न रहते हैं।

४. पितृ-ऋण व पूर्वकृत दोषों की शांति:
अक्षय तृतीया के पावन अवसर पर भगवान परशुराम चालीसा का पाठ करने से पितृ दोषों की शांति होती है और कुल में सुयोग्य संतानों का प्रादुर्भाव होता है।

५. चिरंजीवी स्वरूप से सुयश व सम्मान:
'शरण पड़े को देत प्रभु, सदा सुयश सम्मान॥'
सप्त-चिरंजीवियों में अग्रगण्य भगवान परशुराम जी आज भी महेन्द्र पर्वत पर तपस्यारत हैं। इनकी शरण में आने वाले भक्त को समाज में चिरस्थायी प्रतिष्ठा, पद-सम्मान और अंत में मोक्ष पद प्राप्त होता है।"""

# 5. English Transliteration (रोमन लिप्यंतरण)
parashurama_chalisa_en = """॥ Shri Parashurama Chalisa ॥

॥ Doha ॥
Shri Guru Charana Saroja Chhavi, Nija Mana Mandira Dhari।
Sumari Gajanana Sharada, Gahi Ashisha Tripurari॥

Buddhihina Jana Janiye, Avagunon Ka Bhandara।
Baranon Parashurama Suyasha, Nija Mati Ke Anusara॥

॥ Chaupai ॥
Jai Prabhu Parashurama Sukha Sagara। Jai Munisha Guna Gyana Divakara॥
Bhrigukula Mukuta Vikata Ranadhira। Kshatriya Teja Mukha Santa Sharira॥

Jamadagni Suta Renuka Jaya। Teja Pratapa Sakala Jaga Chhaya॥
Masa Baisakha Sita Pachchha Udara। Tritiya Punarvasu Manuhara॥

Prahara Prathama Nisha Shita Na Ghama। Tithi Pradosha Vyapi Sukhadhama॥
Taba Rishi Kutira Rudana Shishu Kinha। Renuka Kokhi Janama Hari Linha॥

Nija Ghara Uchcha Graha Chhah Thadhe। Mithuna Rashi Rahu Sukha Gadhe॥
Teja-Gyana Mila Nara Tanu Dhara। Jamadagni Ghara Brahma Avatara॥

Dhara Rama Shishu Pavana Nama। Nama Japata Jaga Laha Vishrama॥
Bhala Tripunda Jata Sira Sundara। Kandhe Munja Janeu Manahara॥

Manju Mekhala Kati Mrigachhala। Rudra Mala Bara Vaksha Vishala॥
Pita Basana Sundara Tanu Sohen। Kandha Tunira Dhanusha Mana Mohen॥

Veda-Purana-Shruti-Smriti Gyata। Krodha Rupa Tuma Jaga Vikhyata॥
Dayen Hatha Shriparashu Uthava। Veda-Samhita Bayen Suhava॥

Vidyavana Guna Gyana Apara। Shastra-Shastra Dou Para Adhikara॥
Bhuvana Charidasa Aru Navakhanda। Chahun Dishi Suyasha Pratapa Prachanda॥

Eka Bara Ganapati Ke Sanga। Jujhe Bhrigukula Kamala Patanga॥
Danta Toda Rana Kinha Virama। Eka Danta Ganapati Bhayo Nama॥

Kartavirya Arjuna Bhupala। Sahasrabahu Durjana Vikarala॥
Suragau Lakhi Jamadagni Panhin। Rakhihahun Nija Ghara Thani Mana Manhin॥

Mili Na Mangi Taba Kinha Ladai। Bhayo Parajita Jagata Hansai॥
Tana Khala Hridaya Bhai Risa Gadhi। Riputa Muni Saun Atisaya Badhi॥

Rishivara Rahe Dhyana Lavilina। Tinha Para Shaktighata Nripa Kinha॥
Lagata Shakti Jamadagni Nipata। Manahun Kshatrikula Bama Vidhata॥

Pitu-Badha Matu-Rudana Suni Bhara। Bha Ati Krodha Mana Shoka Apara॥
Kara Gahi Tikshana Parashu Karala। Dushta Hanana Kinheu Tatkala॥

Kshatriya Rudhira Pitu Tarpana Kinha। Pitu-Badha Pratishodha Suta Linha॥
Ikkisa Bara Bhu Kshatriya Bihini। Chhina Dhara Bipranha Kahan Dini॥

Juga Treta Kara Charita Suhai। Shiva-Dhanu Bhanga Kinha Raghurai॥
Guru Dhanu Bhanjaka Ripu Kari Jana। Taba Samula Nasha Tahi Thana॥

Kara Jori Taba Rama Raghurai। Binaya Kinhi Puni Shakti Dikhai॥
Bhishma Drona Karna Balavanta। Bhaye Shishya Dvapara Mahan Ananta॥

Shastra Vidya Deha Suyasha Kamava। Guru Pratapa Diganta Phirava॥
Charon Juga Tava Mahima Gai। Sura Muni Manuja Danuja Samudai॥

De Kashyapa Son Sampada Bhai। Tapa Kinha Mahendra Giri Jai॥
Aba Laun Lina Samadhi Natha। Sakala Loka Navai Nita Matha॥

Charon Varna Eka Sama Jana। Samadarshi Prabhu Tuma Bhagavana॥
Lalahin Chari Phala Sharana Tumhari। Deva Danuja Nara Bhupa Bhikhari॥

Jo Yaha Padhai Shri Parashu Chalisa। Tinha Anukula Sada Gaurisa॥
Purnendu Nisi Basara Swami। Basahu Hridaya Prabhu Antarayami॥

॥ Doha ॥
Parashurama Ko Charu Charita, Metata Sakala Agyana।
Sharana Pade Ko Deta Prabhu, Sada Suyasha Sammana॥

॥ Shloka ॥
Bhrigudeva Kulam Bhanum, Sahasrabahurmardanam।
Renuka Nayana Nandam, Parashumvande Vipradhanam॥"""

# 6. Update drik_chalisa_collections.json
with open('drik_chalisa_collections.json', encoding='utf-8') as f:
    chalisa_data = json.load(f)

rama_items = chalisa_data['rama']['items']
target_item = None
for item in rama_items:
    if item['id'] == 'drik_chalisa_17':
        target_item = item
        break

if target_item:
    target_item['title'] = 'भगवान परशुराम चालीसा'
    target_item['title_en'] = 'Shri Parashurama Chalisa'
    target_item['en_line'] = 'Jai Prabhu Parashurama Sukha Sagara'
    target_item['hi_line'] = 'जय प्रभु परशुराम सुख सागर'
    target_item['sub'] = 'जय प्रभु परशुराम सुख सागर • Drik Panchang Verified'
    target_item['thumb'] = 'assets/dwadashi_parashurama.jpg'
    target_item['audio_url'] = 'https://www.youtube.com/watch?v=72P8PIkKF7Q'
    target_item['video_id'] = '72P8PIkKF7Q'
    target_item['drik_url'] = 'https://www.drikpanchang.com/lyrics/chalisa/shri-parashurama/shri-parashurama-chalisa.html?lang=hi&ck=1'
    target_item['source'] = 'Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)'
    target_item['content'] = parashurama_chalisa_content
    target_item['meaning'] = parashurama_chalisa_meaning
    target_item['vidhi'] = parashurama_chalisa_vidhi
    target_item['significance'] = parashurama_chalisa_significance
    target_item['english_lyrics'] = parashurama_chalisa_en
    print("Updated drik_chalisa_17 in drik_chalisa_collections.json!")
else:
    print("ERROR: drik_chalisa_17 not found in rama items!")

with open('drik_chalisa_collections.json', 'w', encoding='utf-8') as f:
    json.dump(chalisa_data, f, ensure_ascii=False, indent=2)

# 7. Update app.js
with open('app.js', encoding='utf-8') as f:
    app_js = f.read()

# Replace window.CHALISA_COLLECTIONS in app.js
marker = 'window.CHALISA_COLLECTIONS = '
idx_start = app_js.find(marker)
if idx_start != -1:
    idx_end = app_js.find(';\n\n// 1. Render Chalisa Card HTML', idx_start)
    if idx_end != -1:
        new_json_str = json.dumps(chalisa_data, ensure_ascii=False, indent=2)
        app_js = app_js[:idx_start + len(marker)] + new_json_str + app_js[idx_end:]
        print("Updated window.CHALISA_COLLECTIONS in app.js!")
    else:
        print("ERROR: could not find end of CHALISA_COLLECTIONS in app.js")
else:
    print("ERROR: marker not found in app.js")

# Replace chalisa_parashurama in CONTENT in app.js
c_parashurama_record = f"""chalisa_parashurama: {{
    title: 'भगवान परशुराम चालीसा',
    deity: 'भगवान विष्णु के षष्ठ अवतार (श्री परशुराम जी)',
    mantra: '॥ ॐ जामदग्न्याय विद्महे महावीराय धीमहि तन्नो परशुरामः प्रचोदयात् ॥',
    text: `{parashurama_chalisa_content}`,
    meaning: `{parashurama_chalisa_meaning}`,
    vidhi: `{parashurama_chalisa_vidhi}`,
    significance: `{parashurama_chalisa_significance}`,
    english_lyrics: `{parashurama_chalisa_en}`,
    audio_url: 'https://www.youtube.com/watch?v=72P8PIkKF7Q',
    video_id: '72P8PIkKF7Q',
    thumb: 'assets/dwadashi_parashurama.jpg',
    drik_url: 'https://www.drikpanchang.com/lyrics/chalisa/shri-parashurama/shri-parashurama-chalisa.html?lang=hi&ck=1'
  }},
  """

pos_p = app_js.find('chalisa_parashurama:')
if pos_p != -1:
    pos_next = app_js.find('chalisa_balaji:', pos_p)
    if pos_next != -1:
        app_js = app_js[:pos_p] + c_parashurama_record + app_js[pos_next:]
        print("Replaced chalisa_parashurama in CONTENT successfully!")
    else:
        print("ERROR: Could not find chalisa_balaji after chalisa_parashurama")
else:
    print("ERROR: chalisa_parashurama not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("Saved app.js successfully!")

# 8. Update chalisa_engine.js
try:
    with open('chalisa_engine.js', encoding='utf-8') as f:
        c_engine = f.read()
    idx_start_e = c_engine.find(marker)
    if idx_start_e != -1:
        idx_end_e = c_engine.find(';\n\n// 1. Render Chalisa Card HTML', idx_start_e)
        if idx_end_e != -1:
            c_engine = c_engine[:idx_start_e + len(marker)] + json.dumps(chalisa_data, ensure_ascii=False, indent=2) + c_engine[idx_end_e:]
            with open('chalisa_engine.js', 'w', encoding='utf-8') as f:
                f.write(c_engine)
            print("Synced chalisa_engine.js successfully!")
except Exception as e:
    print("Notice on chalisa_engine.js:", e)
