import json, os, re

content = """॥ श्री नवग्रह चालीसा ॥

॥ दोहा ॥
श्री गणपति गुरुपद कमल, प्रेम सहित सिरनाय।
नवग्रह चालीसा कहत, शारद होत सहाय॥
जय जय रवि शशि सोम बुध, जय गुरु भृगु शनि राज।
जयति राहु अरु केतु ग्रह, करहु अनुग्रह आज॥

॥ चौपाई ॥
॥ श्री सूर्य स्तुति ॥
प्रथमहि रवि कहँ नावौं माथा। करहुं कृपा जनि जानि अनाथा॥
हे आदित्य दिवाकर भानू। मैं मति मन्द महा अज्ञानू॥
अब निज जन कहँ हरहु कलेषा। दिनकर द्वादश रूप दिनेशा॥
नमो भास्कर सूर्य प्रभाकर। अर्क मित्र अघ मोघ क्षमाकर॥

॥ श्री चन्द्र स्तुति ॥
शशि मयंक रजनीपति स्वामी। चन्द्र कलानिधि नमो नमामि॥
राकापति हिमांशु राकेशा। प्रणवत जन तन हरहुं कलेशा॥
सोम इन्दु विधु शान्ति सुधाकर। शीत रश्मि औषधि निशाकर॥
तुम्हीं शोभित सुन्दर भाल महेशा। शरण शरण जन हरहुं कलेशा॥

॥ श्री मङ्गल स्तुति ॥
जय जय जय मंगल सुखदाता। लोहित भौमादिक विख्याता॥
अंगारक कुज रुज ऋणहारी। करहु दया यही विनय हमारी॥
हे महिसुत छितिसुत सुखराशी। लोहितांग जय जन अघनाशी॥
अगम अमंगल अब हर लीजै। सकल मनोरथ पूरण कीजै॥

॥ श्री बुध स्तुति ॥
जय शशि नन्दन बुध महाराजा। करहु सकल जन कहँ शुभ काजा॥
दीजैबुद्धि बल सुमति सुजाना। कठिन कष्ट हरि करि कल्याणा॥
हे तारासुत रोहिणी नन्दन। चन्द्रसुवन दुख द्वन्द्व निकन्दन॥
पूजहु आस दास कहु स्वामी। प्रणत पाल प्रभु नमो नमामी॥

॥ श्री बृहस्पति स्तुति ॥
जयति जयति जय श्री गुरुदेवा। करों सदा तुम्हरी प्रभु सेवा॥
देवाचार्य तुम देव गुरु ज्ञानी। इन्द्र पुरोहित विद्यादानी॥
वाचस्पति बागीश उदारा। जीव बृहस्पति नाम तुम्हारा॥
विद्या सिन्धु अंगिरा नामा। करहु सकल विधि पूरण कामा॥

॥ श्री शुक्र स्तुति ॥
शुक्र देव पद तल जल जाता। दास निरन्तन ध्यान लगाता॥
हे उशना भार्गव भृगु नन्दन। दैत्य पुरोहित दुष्ट निकन्दन॥
भृगुकुल भूषण दूषण हारी। हरहु नेष्ट ग्रह करहु सुखारी॥
तुहि द्विजबर जोशी सिरताजा। नर शरीर के तुमहीं राजा॥

॥ श्री शनि स्तुति ॥
जय श्री शनिदेव रवि नन्दन। जय कृष्णो सौरी जगवन्दन॥
पिंगल मन्द रौद्र यम नामा। वप्र आदि कोणस्थ ललामा॥
वक्र दृष्टि पिप्पल तन साजा। क्षण महँ करत रंक क्षण राजा॥
ललत स्वर्ण पद करत निहाला। हरहु विपत्ति छाया के लाला॥

॥ श्री राहु स्तुति ॥
जय जय राहु गगन प्रविसइया। तुमही चन्द्र आदित्य ग्रसइया॥
रवि शशि अरि स्वर्भानु धारा। शिखी आदि बहु नाम तुम्हारा॥
सैहिंकेय तुम निशाचर राजा। अर्धकाय जग राखहु लाजा॥
यदि ग्रह समय पाय कहिं आवहु। सदा शान्ति और सुख उपजावहु॥

॥ श्री केतु स्तुति ॥
जय श्री केतु कठिन दुखहारी। करहु सुजन हित मंगलकारी॥
ध्वजयुत रुण्ड रूप विकराला। घोर रौद्रतन अघमन काला॥
शिखी तारिका ग्रह बलवान। महा प्रताप न तेज ठिकाना॥
वाहन मीन महा शुभकारी। दीजै शान्ति दया उर धारी॥

॥ नवग्रह शान्ति फल ॥
तीरथराज प्रयाग सुपासा। बसै राम के सुन्दर दासा॥
ककरा ग्रामहिं पुरे-तिवारी। दुर्वासाश्रम जन दुख हारी॥
नव-ग्रह शान्ति लिख्यो सुख हेतु। जन तन कष्ट उतारण सेतू॥
जो नित पाठ करै चित लावै। सब सुख भोगि परम पद पावै॥

॥ दोहा ॥
धन्य नवग्रह देव प्रभु, महिमा अगम अपार।
चित नव मंगल मोद गृह, जगत जनन सुखद्वार॥
यह चालीसा नवोग्रह, विरचित सुन्दरदास।
पढ़त प्रेम सुत बढ़त सुख, सर्वानन्द हुलास॥"""

meaning = """॥ श्री नवग्रह चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "श्री गणपति गुरुपद कमल, प्रेम सहित सिरनाय। नवग्रह चालीसा कहत, शारद होत सहाय॥"
भावार्थ: विघ्नहर्ता श्रीगणेश जी और पूज्य सदगुरुदेव के चरण कमलों में प्रेमपूर्वक शीश झुकाकर, तथा माँ सरस्वती की कृपा-सहायता प्राप्त कर नवग्रह चालीसा का गान करते हैं।
• "जय जय रवि शशि सोम बुध, जय गुरु भृगु शनि राज। जयति राहु अरु केतु ग्रह, करहु अनुग्रह आज॥"
भावार्थ: सूर्य (रवि), चन्द्र (शशि/सोम), बुध, देवगुरु बृहस्पति, भृगुपुत्र शुक्र, कर्मफलदाता शनिदेव तथा राहु और केतु—समस्त नवग्रह देवों की जय हो। हे नवग्रह देवगण! आज हम सभी शरणागत भक्तों पर अपनी कृपा व अनुग्रह कीजिए।

【१. श्री सूर्य स्तुति】
• "प्रथमहि रवि कहँ नावौं माथा। करहुं कृपा जनि जानि अनाथा॥ हे आदित्य दिवाकर भानू। मैं मति मन्द महा अज्ञानू॥"
भावार्थ: सर्वप्रथम भुवन-भास्कर भगवान सूर्य के चरणों में मस्तक झुकाता हूँ। हे आदित्य, दिवाकर, भानु! मुझे अज्ञानी जानकर मुझ पर दया कीजिए।
• "अब निज जन कहँ हरहु कलेषा। दिनकर द्वादश रूप दिनेशा॥ नमो भास्कर सूर्य प्रभाकर। अर्क मित्र अघ मोघ क्षमाकर॥"
भावार्थ: हे बारह स्वरूपों में प्रकाशित होने वाले दिनपति दिनकर! अपने जन के समस्त क्लेशों को हरिए। हे भास्कर, प्रभाकर, अर्क, मित्र! हमारे समस्त पापों को क्षमा कर जीवन में प्रकाश भरिए।

【२. श्री चन्द्र स्तुति】
• "शशी मयंक रजनीपति स्वामी। चन्द्र कलानिधि नमो नमामि॥ राकापति हिमांशु राकेशा। प्रणवत जन तन हरहुं कलेशा॥"
भावार्थ: हे रात्रि के स्वामी मयंक, शशांक! सोलह कलाओं के निधि चन्द्रदेव, आपको बारम्बार नमन है। हे पूर्णमासी के स्वामी राकेशा, हिमांशु! अपने शरणागत भक्त के मानसिक व शारीरिक ताप हरिए।
• "सोम इन्दु विधु शान्ति सुधाकर। शीत रश्मि औषधि निशाकर॥ तुम्हीं शोभित सुन्दर भाल महेशा। शरण शरण जन हरहुं कलेशा॥"
भावार्थ: आप सोम, इन्दु, विधु, शान्ति के सागर, अमृत की वर्षा करने वाले सुधाकर तथा समस्त औषधियों के स्वामी हैं। आप देवाधिदेव महादेव के ललाट पर सुशोभित हैं; हे चन्द्रमौली के भूषण! हमारे कष्टों का निवारण कीजिए।

【३. श्री मङ्गल स्तुति】
• "जय जय जय मंगल सुखदाता। लोहित भौमादिक विख्याता॥ अंगारक कुज रुज ऋणहारी। करहु दया यही विनय हमारी॥"
भावार्थ: हे सुखदाता मंगलदेव! आपकी जय हो। आप लोहित, भौम, अंगारक और कुज नामों से प्रसिद्ध हैं। आप समस्त रोगों और ऋण (कर्ज) का नाश करने वाले हैं; मुझ पर दया कीजिए।
• "हे महिसुत छितिसुत सुखराशी। लोहितांग जय जन अघनाशी॥ अगम अमंगल अब हर लीजै। सकल मनोरथ पूरण कीजै॥"
भावार्थ: हे पृथ्वीपुत्र (महिसुत)! आप सुखों की राशि और पापों के नाशक हैं। हमारे जीवन के समस्त अमंगलों को दूर कर सभी मनोरथ सिद्ध कीजिए।

【४. श्री बुध स्तुति】
• "जय शशि नन्दन बुध महाराजा। करहु सकल जन कहँ शुभ काजा॥ दीजैबुद्धि बल सुमति सुजाना। कठिन कष्ट हरि करि कल्याणा॥"
भावार्थ: हे चन्द्र-पुत्र बुध महाराज! आपकी जय हो। समस्त जनों के कार्यों को शुभ बनाइए। हमें सद्बुद्धि, विवेक, ज्ञान और वाक्-शक्ति का बल प्रदान कर कठिन कष्टों से उबारिए।
• "हे तारासुत रोहिणी नन्दन। चन्द्रसुवन दुख द्वन्द्व निकन्दन॥ पूजहु आस दास कहु स्वामी। प्रणत पाल प्रभु नमो नमामी॥"
भावार्थ: हे तारा-पुत्र, रोहिणी-नन्दन, चन्द्रसुवन! आप जीवन के समस्त द्वन्द्वों और संशयों का नाश करने वाले हैं। अपने इस दास की आशाओं को पूर्ण कीजिए।

【५. श्री बृहस्पति स्तुति】
• "जयति जयति जय श्री गुरुदेवा। करों सदा तुम्हरी प्रभु सेवा॥ देवाचार्य तुम देव गुरु ज्ञानी। इन्द्र पुरोहित विद्यादानी॥"
भावार्थ: हे देवगुरु बृहस्पति! आपकी जय हो। आप देवताओं के आचार्य, परम ज्ञानी, इन्द्र के पुरोहित और दिव्य विद्या के प्रदाता हैं।
• "वाचस्पति बागीश उदारा। जीव बृहस्पति नाम तुम्हारा॥ विद्या सिन्धु अंगिरा नामा। करहु सकल विधि पूरण कामा॥"
भावार्थ: आप वाचस्पति, वाणी के स्वामी बागीश, जीव और अंगिरा ऋषि के कुलभूषण हैं। आप ज्ञान के अगाध सिन्धु हैं; हमारे समस्त धर्म, अर्थ, काम और मोक्ष के कार्यों को सिद्ध कीजिए।

【६. श्री शुक्र स्तुति】
• "शुक्र देव पद तल जल जाता। दास निरन्तन ध्यान लगाता॥ हे उशना भार्गव भृगु नन्दन। दैत्य पुरोहित दुष्ट निकन्दन॥"
भावार्थ: हे शुक्रदेव! आपके चरण कमलों में यह दास निरन्तर ध्यान लगाता है। आप उशना, भार्गव, महर्षि भृगु के तेजस्वी पुत्र और दैत्यों के नीति-कुशल गुरु हैं।
• "भृगुकुल भूषण दूषण हारी। हरहु नेष्ट ग्रह करहु सुखारी॥ तुहि द्विजबर जोशी सिरताजा। नर शरीर के तुमहीं राजा॥"
भावार्थ: आप भृगुकुल के भूषण और समस्त दोषों के संहारक हैं। हमारी कुण्डली के समस्त अनिष्ट को दूर कर हमें सुखी कीजिए। आप मनुष्य शरीर के तेज, वीर्य, ओज और आकर्षण के अधिपति हैं।

【७. श्री शनि स्तुति】
• "जय श्री शनिदेव रवि नन्दन। जय कृष्णो सौरी जगवन्दन॥ पिंगल मन्द रौद्र यम नामा। वप्र आदि कोणस्थ ललामा॥"
भावार्थ: हे भगवान सूर्य के पुत्र, जगद्वन्दनीय शनिदेव! आपकी जय हो। आप कृष्ण, सौरी, पिंगल, मन्द, रौद्र और यम जैसे पावन नामों से विख्यात हैं।
• "वक्र दृष्टि पिप्पल तन साजा। क्षण महँ करत रंक क्षण राजा॥ ललत स्वर्ण पद करत निहाला। हरहु विपत्ति छाया के लाला॥"
भावार्थ: आपकी दृष्टि में प्रचण्ड शक्ति है; आप क्षण भर में राजा को रंक और रंक को चक्रवर्ती राजा बना सकते हैं। हे छाया-पुत्र शनिदेव! हमारे समस्त संकटों, साढ़ेसाती व ढैय्या की विपत्तियों को हरकर हमें निहाल कीजिए।

【८. श्री राहु स्तुति】
• "जय जय राहु गगन प्रविसइया। तुमही चन्द्र आदित्य ग्रसइया॥ रवि शशि अरि स्वर्भानु धारा। शिखी आदि बहु नाम तुम्हारा॥"
भावार्थ: हे आकाश में विचरण करने वाले राहुदेव! आपकी जय हो। आप सूर्य और चन्द्रमा को भी अपनी छाया से ग्रसने वाले महाबली स्वर्भानु हैं।
• "सैहिंकेय तुम निशाचर राजा। अर्धकाय जग राखहु लाजा॥ यदि ग्रह समय पाय कहिं आवहु। सदा शान्ति और सुख उपजावहु॥"
भावार्थ: हे सिंहिका-पुत्र सैंहिकेय! आप आधे शरीर वाले हैं, इस संसार में हमारी लाज रखिए। यदि आपकी महादशा या अन्तर्दशा का समय आए, तो हमारे जीवन में अशान्ति के स्थान पर सुख और शान्ति की वृद्धि कीजिए।

【९. श्री केतु स्तुति】
• "जय श्री केतु कठिन दुखहारी। करहु सुजन हित मंगलकारी॥ ध्वजयुत रुण्ड रूप विकराला। घोर रौद्रतन अघमन काला॥"
भावार्थ: हे कठिन दुःखों का हरण करने वाले केतुदेव! आपकी जय हो। आप सज्जनों का कल्याण करने वाले और मंगलकारी हैं। आप ध्वजा धारण किए हुए रुण्ड रूप वाले तेजस्वी ग्रह हैं।
• "शिखी तारिका ग्रह बलवान। महा प्रताप न तेज ठिकाना॥ वाहन मीन महा शुभकारी। दीजै शान्ति दया उर धारी॥"
भावार्थ: आप शिखी, नक्षत्र-मण्डल के बलवान ग्रह और महा प्रतापी हैं। मीन (मत्स्य) आपका पावन वाहन है; हे मोक्षदाता केतुदेव! अपने हृदय में दया धारण कर हमें परम शान्ति प्रदान कीजिए।

【१०. नवग्रह शान्ति फल एवं रचनाकार परिचय】
• "तीरथराज प्रयाग सुपासा। बसै राम के सुन्दर दासा॥ ककरा ग्रामहिं पुरे-तिवारी। दुर्वासाश्रम जन दुख हारी॥ नव-ग्रह शान्ति लिख्यो सुख हेतु। जन तन कष्ट उतारण सेतू॥ जो नित पाठ करै चित लावै। सब सुख भोगि परम पद पावै॥"
भावार्थ: तीर्थराज प्रयाग के समीप दुर्वासा ऋषि के आश्रम के निकट ककरा ग्राम के निवासी सन्त सुन्दरदास जी ने समस्त जीवों के कल्याणार्थ और दैहिक, दैविक व भौतिक कष्टों को पार करने हेतु इस नवग्रह शान्ति चालीसा रूपी सेतु की रचना की है। जो इसका नित्य पाठ करता है, वह इस लोक में समस्त सुख भोगकर अन्त में परम पद को प्राप्त करता है।

【अन्तिम दोहे】
• "धन्य नवग्रह देव प्रभु, महिमा अगम अपार। चित नव मंगल मोद गृह, जगत जनन सुखद्वार॥"
भावार्थ: नवग्रह देवगण परम धन्य हैं, जिनकी महिमा अगम्य और अपार है। वे साधक के चित्त और गृह में नव मंगल, आनन्द और समस्त सुखों के द्वार खोल देते हैं।
• "यह चालीसा नवोग्रह, विरचित सुन्दरदास। पढ़त प्रेम सुत बढ़त सुख, सर्वानन्द हुलास॥"
भावार्थ: सन्त सुन्दरदास जी द्वारा रचित इस नवग्रह चालीसा का जो भक्त प्रेमपूर्वक पाठ करते हैं, उनके घर में संतान सुख, धन-धान्य, आरोग्य और सर्वानन्द का उल्लास निरन्तर बढ़ता रहता है।"""

vidhi = """॥ श्री नवग्रह चालीसा — शास्त्रीय पूजन विधि एवं ग्रह शान्ति नियम ॥

१. विशेष पावन काल व तिथियाँ:
• प्रत्येक शनिवार व रविवार अथवा जिस ग्रह की महादशा/अन्तर्दशा चल रही हो, उस ग्रह का वार।
• अमावस्या, पूर्णिमा, ग्रहण काल के उपरांत, संक्रान्ति तथा नव संवत्सर।
• कुण्डली में कालसर्प दोष, शनि साढ़ेसाती, मंगल दोष अथवा ग्रह पीड़ा निवारण हेतु।

२. पूजा स्थल व नवग्रह मण्डल वेदी:
• पूर्व अथवा उत्तर-पूर्व (ईशान कोण) दिशा की ओर मुख करके बैठें।
• लकड़ी की चौकी पर नया लाल वस्त्र बिछाएं। नवग्रह यन्त्र अथवा नवग्रहों के प्रतीक रूप में अक्षत से नवग्रह मण्डल स्थापित करें:
  - मध्य में सूर्य (लाल)।
  - पूर्व-दक्षिण में चन्द्र (श्वेत)।
  - दक्षिण में मंगल (लाल)।
  - उत्तर-पूर्व में बुध (हरा)।
  - उत्तर में बृहस्पति (पीला)।
  - पूर्व में शुक्र (श्वेत)।
  - पश्चिम में शनि (काला/नीला)।
  - दक्षिण-पश्चिम में राहु (धूम्र/नीला)।
  - उत्तर-पश्चिम में केतु (धूम्र/चितकबरा)।

३. दीपक व धूप:
• शुद्ध गौ-घृत का दीपक मध्य में तथा एक तिल/सरसों के तेल का दीपक शनि-राहु-केतु के निमित्त प्रज्वलित करें।
• गुग्गल, लोबान अथवा चन्दन की सुगन्धित धूप जलाएं।

४. नवग्रह समिधा व अर्पण:
• पुष्प: लाल, पीले, श्वेत व नीले मिश्रित पुष्प अर्पित करें।
• नवधान्य अर्पण: गेहूं (सूर्य), चावल (चन्द्र), मसूर (मंगल), मूंग (बुध), चना (गुरु), सफेद तिल/जौ (शुक्र), काले उड़द (शनि), सरसों (राहु) और तिल (केतु)।
• नैवेद्य: गुड़, पंचमेवा, खीर, बेसन के लड्डू तथा मौसमी फल।

५. चालीसा पाठ एवं जप नियम:
• आचमन, प्राणायाम के बाद हाथ में जल लेकर नवग्रह शान्ति का संकल्प करें।
• नित्य १ पाठ समस्त ग्रहों की अनुकूलता हेतु सर्वोत्तम है।
• विशेष ग्रह दोष शान्ति हेतु उस ग्रह की स्तुति का विशेष ध्यान करते हुए ९ या २१ पाठ करने का विधान है।

६. आरती व दान:
• पाठ समाप्ति पर नवग्रहों की आरती करें तथा जरूरतमंदों को अपनी सामर्थ्यानुसार नवधान्य, वस्त्र अथवा भोजन का दान दें।"""

significance = """॥ श्री नवग्रह चालीसा — आध्यात्मिक महत्त्व एवं अलौकिक फलश्रुति ॥

१. समस्त नवग्रह दोषों की एक साथ शान्ति:
वैदिक ज्योतिष के अनुसार जातक का प्रारब्ध और सुख-दुःख नवग्रहों की रश्मियों द्वारा संचालित होता है। इस चालीसा के पाठ से कुण्डली के समस्त जटिल दोष—कालसर्प दोष, पितृदोष, शनि की साढ़ेसाती व ढैय्या, मांगलिक दोष, गुरु चाण्डाल दोष, केमद्रुम दोष और ग्रहण दोष शांत होकर शुभ फल देने लगते हैं।

२. अंग-प्रत्यंग व त्रिदोष सन्तुलन:
नवग्रह मानव शरीर की धातुओं और वात, पित्त, कफ त्रिदोषों के नियंत्रक हैं। नवग्रह चालीसा के नियमित पाठ से रक्त विकार (मंगल), मानसिक अवसाद (चन्द्र), स्नायु दुर्बलता (बुध), अस्थि पीड़ा (सूर्य) और वात-जोड़ों का दर्द (शनि) शांत होकर शरीर पूर्णतः स्वस्थ रहता है।

३. ऋण मुक्ति एवं आर्थिक समृद्धि:
"अंगारक कुज रुज ऋणहारी... क्षण महँ करत रंक क्षण राजा..." — मंगल और शनिदेव की कृपा से कर्जों के जाल से मुक्ति मिलती है और व्यापार, आजीविका तथा संपत्ति में अभूतपूर्व वृद्धि होती है।

४. बुद्धि, विवेक एवं राज-सम्मान:
सूर्य, बुध और गुरु की संयुक्त कृपा से साधक को कुशाग्र बुद्धि, वाक्-चातुर्य, विद्या में सफलता और समाज तथा प्रशासन में मान-सम्मान प्राप्त होता है।

५. राहु-केतु जनित भ्रम व आकस्मिक संकटों से मुक्ति:
राहु और केतु की पीड़ा शांत होने से भूत-प्रेत, तंत्र-बाधा, न्यायालयी मुकदमे, शत्रु-षड्यंत्र और अज्ञात भय स्वतः समाप्त होकर घर में सुख-शान्ति और संतान सुख का विस्तार होता है।"""

english_lyrics = """|| Shri Navagraha Chalisa ||

|| Doha ||
Shri Ganapati Guru-pad Kamal, Prem Sahit Sir Naay।
Navagraha Chalisa Kahat, Shaarad Hot Sahaay॥
Jai Jai Ravi Shashi Som Budh, Jai Guru Bhrigu Shani Raaj।
Jayati Rahu Aru Ketu Grah, Karahu Anugrah Aaj॥

|| Chaupai ||
|| Shri Surya Stuti ||
Prathamahin Ravi Kahan Naavaun Maatha। Karahun Kripa Jani Jaani Anaatha॥
He Aaditya Divaakar Bhaanoo। Main Mati Mand Maha Agyaanoo॥
Ab Nij Jan Kahan Harahu Kalesha। Dinkar Dwaadash Roop Dinesha॥
Namo Bhaaskar Soorya Prabhaakar। Ark Mitra Agh Mogh Kshamaakar॥

|| Shri Chandra Stuti ||
Shashi Mayank Rajanipati Swami। Chandra Kalaanidhi Namo Namaami॥
Raakaapati Himanshu Raakesha। Pranavat Jan Tan Harahun Kalesha॥
Som Indu Vidhu Shaanti Sudhaakar। Sheet Rashmi Aushadhi Nishaakar॥
Tumheen Shobhit Sundar Bhaal Mahesha। Sharan Sharan Jan Harahun Kalesha॥

|| Shri Mangala Stuti ||
Jai Jai Jai Mangal Sukhdaata। Lohit Bhaumaadik Vikhyaata॥
Angaarak Kuj Ruj Rinhaari। Karahu Daya Yahi Vinay Hamari॥
He Mahisut Chhitisut Sukhraashi। Lohitaang Jai Jan Aghnaashi॥
Agam Amangal Ab Har Leejai। Sakal Manorath Pooran Keejai॥

|| Shri Budha Stuti ||
Jai Shashi Nandan Budh Mahaaraaja। Karahu Sakal Jan Kahan Shubh Kaaja॥
Deejai Buddhi Bal Sumati Sujaana। Kathin Kasht Hari Kari Kalyaana॥
He Taarasut Rohini Nandan। Chandrasuvan Dukh Dwandva Nikandan॥
Poojahu Aas Daas Kahu Swami। Pranat Paal Prabhu Namo Namaami॥

|| Shri Brihaspati Stuti ||
Jayati Jayati Jai Shri Gurudeva। Karon Sada Tumhri Prabhu Seva॥
Devaachaarya Tum Dev Guru Gyaani। Indra Purohit Vidyaadaani॥
Vaachaspati Baageesh Udaara। Jeev Brihaspati Naam Tumhaara॥
Vidya Sindhu Angira Naama। Karahu Sakal Vidhi Pooran Kaama॥

|| Shri Shukra Stuti ||
Shukra Dev Pad Tal Jal Jaata। Daas Nirantan Dhyaan Lagaata॥
He Ushana Bhaargav Bhrigu Nandan। Daitya Purohit Dusht Nikandan॥
Bhrigukul Bhooshan Dooshan Haari। Harahu Nesht Grah Karahu Sukhaari॥
Tuhi Dwijbar Joshi Sirtaaja। Nar Shareer Ke Tumheen Raaja॥

|| Shri Shani Stuti ||
Jai Shri Shanidev Ravi Nandan। Jai Krishno Sauri Jagvandan॥
Pingal Mand Raudra Yam Naama। Vapra Aadi Konasth Lalaama॥
Vakra Drishti Pippal Tan Saaja। Kshan Mahan Karat Rank Kshan Raaja॥
Lalat Swarn Pad Karat Nihaala। Harahu Vipatti Chhaaya Ke Laala॥

|| Shri Rahu Stuti ||
Jai Jai Rahu Gagan Pravisaiya। Tumhi Chandra Aaditya Grasaiya॥
Ravi Shashi Ari Swarbhaanu Dhaara। Shikhee Aadi Bahu Naam Tumhaara॥
Saihinkey Tum Nishaachar Raaja। Ardhkaay Jag Raakhahu Laaja॥
Yadi Grah Samay Paay Kahin Aavahu। Sada Shaanti Aur Sukh Upjaavahu॥

|| Shri Ketu Stuti ||
Jai Shri Ketu Kathin Dukh-haari। Karahu Sujan Hit Mangalkaari॥
Dhwaj-yut Rund Roop Vikraala। Ghor Raudratan Aghman Kaala॥
Shikhee Taarika Grah Balwaan। Maha Prataap Na Tej Thikaana॥
Vaahan Meen Maha Shubhkaari। Deejai Shaanti Daya Ur Dhaari॥

|| Navagraha Shanti Phal ||
Teerathraaj Prayaag Supaasa। Basai Ram Ke Sundar Daasa॥
Kakra Graamhin Pure-Tiwaari। Durvaasaashram Jan Dukh Haari॥
Nav-grah Shaanti Likhyo Sukh Hetu। Jan Tan Kasht Utaaran Setu॥
Jo Nit Paath Karai Chit Laavai। Sab Sukh Bhogi Param Pad Paavai॥

|| Doha ||
Dhanya Navagraha Dev Prabhu, Mahima Agam Apaar।
Chit Nav Mangal Mod Grih, Jagat Janan Sukh-dwaar॥
Yeh Chalisa Navograh, Virchit Sundardaas।
Padhat Prem Sut Badhat Sukh, Sarvaanand Hulaas॥"""

# 1. Update drik_chalisa_15 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["surya"]["items"]:
    if item["id"] == "drik_chalisa_15":
        item["title"] = "श्री नवग्रह चालीसा"
        item["title_en"] = "Shri Navagraha Chalisa"
        item["en_line"] = "Prathmahi Ravi Kahan Navaun Matha"
        item["hi_line"] = "प्रथमहि रवि कहँ नावौं माथा"
        item["sub"] = "प्रथमहि रवि कहँ नावौं माथा • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_surya_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=UkFxddhsyQk"
        item["video_id"] = "UkFxddhsyQk"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/navagraha/navagraha-chalisa.html?lang=hi"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "समस्त नवग्रह देवगण"
        item["section"] = "श्री सूर्य देव व नवग्रह चालीसा"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_15 in drik_chalisa_collections.json!")

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

# 3. Update chalisa_navagraha in CONTENT in app.js
content_obj = {
    "title": "श्री नवग्रह चालीसा",
    "title_en": "Shri Navagraha Chalisa",
    "en_line": "Prathmahi Ravi Kahan Navaun Matha",
    "hi_line": "प्रथमहि रवि कहँ नावौं माथा",
    "sub": "प्रथमहि रवि कहँ नावौं माथा • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_surya_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=UkFxddhsyQk",
    "video_id": "UkFxddhsyQk",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/navagraha/navagraha-chalisa.html?lang=hi",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "समस्त नवग्रह देवगण",
    "section": "श्री सूर्य देव व नवग्रह चालीसा",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

navagraha_content_js = "  chalisa_navagraha: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

# Replace old chalisa_navagraha in CONTENT using exact string slice
m_start = app_text.find("  chalisa_navagraha: {")
if m_start != -1:
    m_end = app_text.find("  chalisa_vishwakarma: {", m_start)
    if m_end != -1:
        app_text = app_text[:m_start] + navagraha_content_js + app_text[m_end:]
        print("Replaced existing chalisa_navagraha in CONTENT using string slice!")
    else:
        print("Could not find chalisa_vishwakarma in app.js!")
else:
    print("Could not find chalisa_navagraha in app.js!")

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
