import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Authentic Devanagari Lyrics from Drik Panchang
ramdev_chalisa_content = """॥ श्री रामदेव चालीसा ॥
(पीरों के पीर बाबा रामदेव जी / रामापीर • भाषा: राजस्थानी / ब्रज)

॥ दोहा ॥
श्री गुरु पद नमन करि, गिरा गनेश मनाय।
कथूं रामदेव विमल यश, सुने पाप विनशाय॥

द्वार केश से आय कर, लिया मनुज अवतार।
अजमल गेह बधावणा, जग में जय जयकार॥

॥ चौपाई ॥
जय जय रामदेव सुर राया। अजमल पुत्र अनोखी माया॥
विष्णु रूप सुर नर के स्वामी। परम प्रतापी अन्तर्यामी॥

ले अवतार अवनि पर आये। तंवर वंश अवतंश कहाये॥
संत जनों के कारज सारे। दानव दैत्य दुष्ट संहारे॥

परच्या प्रथम पिता को दीन्हा। दूध परीण्डा मांही कीन्हा॥
कुमकुम पद पोली दर्शाये। ज्योंही प्रभु पलने प्रगटाये॥

परचा दूजा जननी पाया। दूध उफणता चरा उठाया॥
परचा तीजा पुरजन पाया। चिथड़ों का घोड़ा ही साया॥

परच्या चौथा भैरव मारा। भक्त जनों का कष्ट निवारा॥
पंचम परच्या रतना पाया। पुंगल जा प्रभु फंद छुड़ाया॥

परच्या छठा विजयसिंह पाया। जला नगर शरणागत आया॥
परच्या सप्तम् सुगना पाया। मुवा पुत्र हंसता भग आया॥

परच्या अष्टम् बौहित पाया। जा परदेश द्रव्य बहु लाया॥
भंवर डूबती नाव उबारी। प्रगत टेर पहुँचे अवतारी॥

नवमां परच्या वीरम पाया। बनियां आ जब हाल सुनाया॥
दसवां परच्या पा बिनजारा। मिश्री बनी नमक सब खारा॥

परच्या ग्यारह किरपा थारी। नमक हुआ मिश्री फिर सारी॥
परच्या द्वादश ठोकर मारी। निकलंग नाड़ी सिरजी प्यारी॥

परच्या तेरहवां पीर परी पधारया। ल्याय कटोरा कारज सारा॥
चौदहवां परच्या जाभो पाया। निजसर जल खारा करवाया॥

परच्या पन्द्रह फिर बतलाया। राम सरोवर प्रभु खुदवाया॥
परच्या सोलह हरबू पाया। दर्श पाय अतिशय हरषाया॥

परच्या सत्रह हर जी पाया। दूध थणा बकरया के आया॥
सुखी नाडी पानी कीन्हों। आत्म ज्ञान हरजी ने दीन्हों॥

परच्या अठारहवां हाकिम पाया। सूते को धरती लुढ़काया॥
परच्या उन्नीसवां दल जी पाया। पुत्र पाय मन में हरषाया॥

परच्या बीसवां पाया सेठाणी। आये प्रभु सुन गदगद वाणी॥
तुरंत सेठ सरजीवण कीन्हा। उक्त उजागर अभय वर दीन्हा॥

परच्या इक्कीसवां चोर जो पाया। हो अन्धा करनी फल पाया॥
परच्या बाईसवां मिर्जो चीहां। सातो तवा बेध प्रभु दीन्हां॥

परच्या तेईसवां बादशाह पाया। फेर भक्त को नहीं सताया॥
परच्या चैबीसवां बख्शी पाया। मुवा पुत्र पल में उठ धाया॥

जब-जब जिसने सुमरण कीन्हां। तब-तब आ तुम दर्शन दीन्हां॥
भक्त टेर सुन आतुर धाते। चढ़ लीले पर जल्दी आते॥

जो जन प्रभु की लीला गावें। मनवांछित कारज फल पावें॥
यह चालीसा सुने सुनावे। ताके कष्ट सकल कट जावे॥

जय जय जय प्रभु लीला धारी। तेरी महिमा अपरम्पारी॥
मैं मूरख क्या गुण तब गाऊँ। कहाँ बुद्धि शारद सी लाऊँ॥

नहीं बुद्धि बल घट लव लेशा। मती अनुसार रची चालीसा॥
दास सभी शरण में तेरी। रखियों प्रभु लज्जा मेरी॥

॥ दोहा ॥
भक्त हेतु अवतार ले, कीन्हे काज अपार।
रामदेव प्रभु राखिये, भवसागर से पार॥"""

# 2. Verse-by-verse Spiritual Meaning (पद्यवार सम्पूर्ण पावन भावार्थ)
ramdev_chalisa_meaning = """॥ श्री रामदेव चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【आरम्भिक दोहे】
दोहा १:
श्री गुरु पद नमन करि, गिरा गनेश मनाय।
कथूं रामदेव विमल यश, सुने पाप विनशाय॥
भावार्थ: श्री गुरुदेव के पावन चरणों में साष्टांग नमन करके, वाणी की देवी माँ सरस्वती और विघ्नहर्ता श्री गणेश जी को मनाकर, मैं बाबा रामदेव जी के निर्मल यश का गान करता हूँ, जिसके केवल श्रवण मात्र से समस्त पाप नष्ट हो जाते हैं।

दोहा २:
द्वार केश से आय कर, लिया मनुज अवतार।
अजमल गेह बधावणा, जग में जय जयकार॥
भावार्थ: साक्षात् द्वारकानाथ भगवान श्री कृष्ण ने भक्तों के कल्याण हेतु मनुष्य रूप में अवतार लिया। राजा अजमल जी के पावन घर में जन्मोत्सव की बधाइयां बजीं और सम्पूर्ण जगत में आपकी जय-जयकार गूंज उठी।

【चौपाइयां — भावार्थ】
१. जय जय रामदेव सुर राया। अजमल पुत्र अनोखी माया॥
विष्णु रूप सुर नर के स्वामी। परम प्रतापी अन्तर्यामी॥
भावार्थ: देवों के देव, राजाधिराज बाबा रामदेव जी की जय हो, जय हो! राजा अजमल जी के सुपुत्र के रूप में आपकी माया अत्यंत अलौकिक व अनोखी है। आप साक्षात् भगवान विष्णु के अवतारी, देवताओं व मनुष्यों के स्वामी, परम प्रतापी और सबके अंतर्यामी प्रभु हैं।

२. ले अवतार अवनि पर आये। तंवर वंश अवतंश कहाये॥
संत जनों के कारज सारे। दानव दैत्य दुष्ट संहारे॥
भावार्थ: आपने पृथ्वी पर अवतार धारण किया और तंवर (तोमर) राजपूत वंश के शिरोमणि व मुकुट कहलाए। आपने साधु-संतों और दीनों के बिगड़े काम संवारे और समाज को पीड़ित करने वाले दैत्यों, दानवों और दुष्टों का संहार किया।

३. परच्या प्रथम पिता को दीन्हा। दूध परीण्डा मांही कीन्हा॥
कुमकुम पद पोली दर्शाये। ज्योंही प्रभु पलने प्रगटाये॥
भावार्थ (पहला परचा): प्रभु ने प्रथम चमत्कार (परचा) अपने पिता अजमल जी को दिखाया। जैसे ही प्रभु पालने में प्रकट हुए, उन्होंने उफनते दूध को परीण्डे (जलपात्र) में भर दिया और द्वार पर कुमकुम के दिव्य चरण-चिह्न (पगलिए) प्रकट कर अपने ईश्वरत्व का प्रमाण दिया।

४. परचा दूजा जननी पाया। दूध उफणता चरा उठाया॥
परचा तीजा पुरजन पाया। चिथड़ों का घोड़ा ही साया॥
भावार्थ (दूसरा व तीसरा परचा): दूसरा परचा माता मैणादे ने पाया, जब चूल्हे पर खौलते दूध के बर्तन को बाल रामदेव ने अपने नन्हे हाथों से बिना जले नीचे उतार लिया। तीसरा परचा नगरवासियों (दर्जी) ने देखा, जब साधारण कपड़ों के चिथड़ों से सिला हुआ खिलौना घोड़ा साक्षात् सजीव होकर आकाश में उड़ने लगा।

५. परच्या चौथा भैरव मारा। भक्त जनों का कष्ट निवारा॥
पंचम परच्या रतना पाया। पुंगल जा प्रभु फंद छुड़ाया॥
भावार्थ (चौथा व पाँचवाँ परचा): चौथा परचा पोकरण की भूमि पर भैरव नामक क्रूर नरभक्षी राक्षस का वध कर दिया और जन-जन का भय दूर किया। पाँचवाँ परचा रत्ना रायका को दिया, जब पूँगल जाकर उसकी विपदा को दूर किया और कारागार के बंधनों से मुक्त कराया।

६. परच्या छठा विजयसिंह पाया। जला नगर शरणागत आया॥
परच्या सप्तम् सुगना पाया। मुवा पुत्र हंसता भग आया॥
भावार्थ (छठा व सातवाँ परचा): छठा परचा जलानगर के राजा विजयसिंह ने पाया, जब संकट में प्रभु की शरण में आने पर उसकी रक्षा हुई। सातवाँ परचा अपनी प्रिय बहिन सुगना को दिया, जब उसके मृत पुत्र को पुनः जीवित कर दिया और वह बालक हंसता-खेलता माँ की गोद में लौट आया।

७. परच्या अष्टम् बौहित पाया। जा परदेश द्रव्य बहु लाया॥
भंवर डूबती नाव उबारी। प्रगत टेर पहुँचे अवतारी॥
भावार्थ (आठवाँ परचा): आठवाँ परचा सेठ बौहित ने पाया, जब परदेश से अपार धन लेकर लौटते समय समुद्र के भंवर में उसकी जहाज डूबने लगा। सेठ की आर्त पुकार सुनते ही अवतारी प्रभु ने प्रकट होकर डूबती नाव को किनारे लगा दिया।

८. नवमां परच्या वीरम पाया। बनियां आ जब हाल सुनाया॥
दसवां परच्या पा बिनजारा। मिश्री बनी नमक सब खारा॥
भावार्थ (नौवाँ व दसवाँ परचा): नौवाँ परचा बड़े भाई वीरमदेव ने देखा जब बनिए ने आकर प्रभु की कृपा का वृत्तांत सुनाया। दसवाँ परचा लखी बंजारे ने पाया, जिसने प्रभु से झूठ बोलकर मिश्री को नमक बताया था, तो प्रभु की माया से उसकी सारी मिश्री खारा नमक बन गई।

९. परच्या ग्यारह किरपा थारी। नमक हुआ मिश्री फिर सारी॥
परच्या द्वादश ठोकर मारी। निकलंग नाड़ी सिरजी प्यारी॥
भावार्थ (ग्यारहवाँ व बारहवाँ परचा): ग्यारहवाँ परचा तब मिला जब लखी बंजारे ने रो-रोकर क्षमा मांगी, तो दयालु बाबा ने पुनः सारे नमक को मीठी मिश्री बना दिया। बारहवाँ परचा तब दिखाया जब मरुभूमि में जल संकट होने पर प्रभु ने धरती पर ठोकर मारी और वहाँ पवित्र व मीठे जल की 'निकलंग नाड़ी' (सरोवर) प्रकट कर दी।

१०. परच्या तेरहवां पीर परी पधारया। ल्याय कटोरा कारज सारा॥
चौदहवां परच्या जाभो पाया। निजसर जल खारा करवाया॥
भावार्थ (तेरहवाँ व चौदहवाँ परचा): तेरहवाँ परचा मक्का से आए पांच पीरों को दिया; जब उन्होंने अपने ही बर्तनों में खाने की शर्त रखी, तो प्रभु ने पलक झपकते मक्का से उनके कटोरे मंगाकर भोजन कराया, जिससे उन्होंने कहा—"हम तो पीर हैं, आप पीरों के पीर हो"। चौदहवाँ परचा जाभो को दिया और निजसर के खारे जल को मीठा करवाया।

११. परच्या पन्द्रह फिर बतलाया। राम सरोवर प्रभु खुदवाया॥
परच्या सोलह हरबू पाया। दर्श पाय अतिशय हरषाया॥
भावार्थ (पन्द्रहवाँ व सोलहवाँ परचा): पन्द्रहवाँ परचा देकर रूणिचा में अकाल व जल संकट दूर करने हेतु विशाल 'राम सरोवर' का निर्माण करवाया। सोलहवाँ परचा अपने मौसेरे भाई वीर हरबू जी सांखला को दिव्य स्वरूप में साक्षात् दर्शन देकर दिया।

१२. परच्या सत्रह हर जी पाया। दूध थणा बकरया के आया॥
सुखी नाडी पानी कीन्हों। आत्म ज्ञान हरजी ने दीन्हों॥
भावार्थ (सत्रहवाँ परचा): सत्रहवाँ परचा अनन्य भक्त हरजी भाटी को दिया; बकरों के थनों से दूध की धारा बहा दी, सूखी नाड़ी को लबालब जल से भर दिया और हरजी को दिव्य आत्मज्ञान प्रदान किया।

१३. परच्या अठारहवां हाकिम पाया। सूते को धरती लुढ़काया॥
परच्या उन्नीसवां दल जी पाया। पुत्र पाय मन में हरषाया॥
भावार्थ (अठारहवाँ व उन्नीसवाँ परचा): अठारहवाँ परचा अहंकारी हाकिम को दिया, जो साधु-संतों का अपमान करता था, उसे पलंग सहित जमीन पर पटक कर उसका मान भंग किया। उन्नीसवाँ परचा दल जी ने पाया, जिसे प्रभु कृपा से सुयोग्य पुत्र रत्न की प्राप्ति हुई।

१४. परच्या बीसवां पाया सेठाणी। आये प्रभु सुन गदगद वाणी॥
तुरंत सेठ सरजीवण कीन्हा। उक्त उजागर अभय वर दीन्हा॥
भावार्थ (बीसवाँ परचा): बीसवाँ परचा आर्त भाव से पुकारने वाली सेठाणी ने पाया। प्रभु ने उसकी गद्गद वाणी सुनकर तत्काल उसके मृत पति (सेठ) को पुनः जीवित (सरजीवन) कर दिया और अभय वरदान दिया।

१५. परच्या इक्कीसवां चोर जो पाया। हो अन्धा करनी फल पाया॥
परच्या बाईसवां मिर्जो चीहां। सातो तवा बेध प्रभु दीन्हां॥
भावार्थ (इक्कीसवाँ व बाईसवाँ परचा): इक्कीसवाँ परचा मंदिर में चोरी करने आए चोर को मिला, जो अपनी कुकरनी के फलस्वरूप तुरंत अंधा हो गया। बाईसवाँ परचा मिर्जो चीहां को दिया, जिसके अहंकार को चूर करने हेतु प्रभु ने अपने एक ही बाण से लोहे के सातों तवों को एक साथ भेद दिया।

१६. परच्या तेईसवां बादशाह पाया। फेर भक्त को नहीं सताया॥
परच्या चैबीसवां बख्शी पाया। मुवा पुत्र पल में उठ धाया॥
भावार्थ (तेईसवाँ व चौबीसवाँ परचा): तेईसवाँ परचा दिल्ली के बादशाह को दिया, जिसने प्रभु का चमत्कार देखकर कभी किसी हिंदू या भक्त को न सताने का वचन दिया। चौबीसवाँ परचा बख्शी ने पाया, जिसके मृत पुत्र को प्रभु ने पल भर में जीवित कर दिया और वह दौड़ पड़ा।

१७. जब-जब जिसने सुमरण कीन्हां। तब-तब आ तुम दर्शन दीन्हां॥
भक्त टेर सुन आतुर धाते। चढ़ लीले पर जल्दी आते॥
भावार्थ: जब-जब जिस किसी भी भक्त ने संकट में आपको सच्चे हृदय से याद किया, आपने तत्काल प्रकट होकर उसे दर्शन दिए। भक्त की आर्त पुकार (टेर) सुनते ही आप व्याकुल होकर अपने नीले घोड़े (लीला घोड़ा) पर सवार होकर पलक झपकते रक्षा करने पहुँचते हैं।

१८. जो जन प्रभु की लीला गावें। मनवांछित कारज फल पावें॥
यह चालीसा सुने सुनावे। ताके कष्ट सकल कट जावे॥
भावार्थ: जो मनुष्य बाबा रामदेव जी की इस दिव्य लीला और परचों का गान करता है, उसके समस्त मनवांछित कार्य सिद्ध होते हैं। जो भी इस पावन चालीसा को नित्य पढ़ता या सुनता है, उसके जीवन के सभी संकट, रोग और बाधाएं तत्काल कट जाती हैं।

१९. जय जय जय प्रभु लीला धारी। तेरी महिमा अपरम्पारी॥
मैं मूरख क्या गुण तब गाऊँ। कहाँ बुद्धि शारद सी लाऊँ॥
भावार्थ: हे लीलाधारी प्रभु! आपकी सदा जय हो, जय हो, जय हो! आपकी महिमा असीम और अपरम्पार है। मुझ जैसा अज्ञानी आपके अनन्त गुणों का वर्णन कैसे कर सकता है? मेरे पास माँ सरस्वती जैसी बुद्धि कहाँ?

२०. नहीं बुद्धि बल घट लव लेशा। मती अनुसार रची चालीसा॥
दास सभी शरण में तेरी। रखियों प्रभु लज्जा मेरी॥
भावार्थ: मेरे हृदय में लेशमात्र भी बुद्धि और बल नहीं है, मैंने अपनी अल्प मति के अनुसार ही इस चालीसा की रचना की है। हे रामापीर! हम सब दास आपकी ही शरण में हैं, आप कृपा करके हमारी लाज रखिए।

【समापन दोहा】
भक्त हेतु अवतार ले, कीन्हे काज अपार।
रामदेव प्रभु राखिये, भवसागर से पार॥
भावार्थ: अपने भक्तों के उद्धार हेतु मनुष्य रूप में अवतार लेकर आपने असंख्य अलौकिक कार्य किए। हे बाबा रामदेव जी! हम पर अपनी कृपा बनाए रखिए और हमें इस भवसागर से पार उतारिए।"""

# 3. Authentic Worship Procedure & Rules (शास्त्रोक्त पाठ विधि व नियम)
ramdev_chalisa_vidhi = """॥ बाबा रामदेव चालीसा पाठ एवं पूजन विधि व नियम ॥

१. पावन काल व विशेष मुहूर्त:
• प्रतिदिन प्रातःकाल ब्रह्ममुहूर्त अथवा संध्याकाल में पाठ करना सर्वोत्तम है।
• विशेष रूप से भाद्रपद शुक्ल द्वितीया (बाबे री बीज / रामदेव जयंती), भाद्रपद शुक्ल एकादशी (समाधि दिवस), माघ शुक्ल द्वितीया, प्रत्येक माह के शुक्ल पक्ष की दूज (बीज) तथा प्रत्येक गुरुवार व रविवार को इसका पाठ अनंत गुना फलदायी है।

२. आवश्यक पूजन सामग्री:
• बाबा रामदेव जी का पावन चित्र, विग्रह अथवा उनके चरण-चिह्न (पगलिए)।
• लीले घोड़े का प्रतीक (कपड़े का छोटा घोड़ा)।
• पचरंगी ध्वजा (बाबा का नेजा), शुद्ध गाय के घी का दीपक, गुग्गल व कपूर की धूप।
• कच्चा गाय का दूध, पंचामृत, रोली, कुमकुम, अक्षत, पीला चंदन।
• नैवेद्य: चूरमा (विशेष प्रिय), मिश्री, माखन, पेड़ा, नारियल तथा ऋतुफल।

३. शास्त्रोक्त पूजन विधान:
• स्नानादि कर स्वच्छ पीले या श्वेत वस्त्र धारण करें।
• पूर्व अथवा उत्तर दिशा की ओर मुख करके पवित्र आसन पर बैठें।
• पाटे पर पीला वस्त्र बिछाकर बाबा रामदेव जी का चित्र व पगलिए स्थापित करें।
• शुद्ध घी का अखण्ड दीपक प्रज्वलित करें और गुग्गल की धूप दें।
• कच्चे दूध व गंगाजल से प्रतीकात्मक अभिषेक कर कुमकुम व अक्षत से पगलिए की पूजा करें।
• कपड़े का लीला घोड़ा व ध्वजा अर्पित करें।
• चूरमा और मिश्री का प्रेमपूर्वक भोग लगाएं।
• हाथ में जल लेकर संकल्प करें और एकाग्रचित्त होकर चालीसा का पाठ करें।
• पाठ के उपरांत 'जय बाबे री' तथा 'ॐ श्री रामदेवाय नमः' का जप करें और बाबा की आरती करें।

४. जमा जागरण (जम्मा) का नियम:
• विशेष संकट निवारण अथवा मन्नत पूर्ति हेतु दूज की रात्रि में 'जमा जागरण' (रात भर संकीर्तन व भजन) करना अत्यंत शुभ माना गया है।
• जागरण के दौरान ज्योत प्रज्वलित रखें, सात्विक भाव रखें और सभी में चूरमे का प्रसाद वितरित करें।"""

# 4. Spiritual Significance & Fruits (आध्यात्मिक महत्त्व व फलश्रुति)
ramdev_chalisa_significance = """॥ श्री रामदेव चालीसा का आध्यात्मिक महत्त्व व फलश्रुति ॥

१. पीरों के पीर रामापीर की अमोघ कृपा:
'परच्या तेरहवां पीर परी पधारया। ल्याय कटोरा कारज सारा॥'
मक्का के पीरों द्वारा 'पीरों के पीर' उपाधि प्राप्त बाबा रामदेव जी अपने भक्तों की पुकार कभी अनसुनी नहीं करते। चालीसा पाठ से साधक को सर्वत्र विजय और अभय मिलता है।

२. २४ परचों के स्मरण से संकट निवारण:
'यह चालीसा सुने सुनावे। ताके कष्ट सकल कट जावे॥'
बाबा के २४ चमत्कारों (परचों) का गुणगान करने से साधक के जीवन के बड़े से बड़े असाध्य कष्ट, ऋण, कोर्ट-कचहरी और व्यापारिक संकट तत्काल समाप्त हो जाते हैं।

३. असाध्य रोगों व कुष्ठ से मुक्ति:
राम सरोवर व परचा बावड़ी के पावन जल और बाबा के स्मरण से शारीरिक व्याधियां, असाध्य चर्मरोग और ऊपरी बाधाएं पूर्णतः शांत होती हैं।

४. सामाजिक समरसता व पारिवारिक शांति:
बाबा रामदेव जी ने समाज से ऊंच-नीच और जाति-पाति के भेद को समाप्त किया। इनके पूजन से घर-परिवार में प्रेम, एकता, सद्भाव और संतान सुख की वृद्धि होती है।

५. आर्त पुकार पर तत्काल सहायता:
'भक्त टेर सुन आतुर धाते। चढ़ लीले पर जल्दी आते॥'
सच्चे हृदय से स्मरण करने पर बाबा अपने लीले घोड़े पर सवार होकर भक्त की रक्षा हेतु स्वयं खिंचे चले आते हैं और अंत में भवसागर से पार लगाते हैं।"""

# 5. English Transliteration (रोमन लिप्यंतरण)
ramdev_chalisa_en = """॥ Shri Ramdev Chalisa ॥

॥ Doha ॥
Shri Guru Pada Namana Kari, Gira Ganesha Manaya।
Kathun Ramdeva Vimala Yasha, Sune Papa Vinashaya॥

Dvara Kesha Se Aaya Kara, Liya Manuja Avatara।
Ajamala Geha Badhavana, Jaga Mein Jai Jaikara॥

॥ Chaupai ॥
Jai Jai Ramdeva Sura Raya। Ajamala Putra Anokhi Maya॥
Vishnu Rupa Sura Nara Ke Swami। Parama Pratapi Antaryami॥

Le Avatara Avani Para Aaye। Tanvara Vansha Avatansha Kahaye॥
Santa Janon Ke Karaja Sare। Danava Daitya Dushta Samhare॥

Parachya Prathama Pita Ko Dinha। Dudha Parinda Manhi Kinha॥
Kumkuma Pada Poli Darshaye। Jyonhi Prabhu Palane Pragataye॥

Paracha Duja Janani Paya। Dudha Uphanata Chara Uthaya॥
Paracha Tija Purajana Paya। Chithadon Ka Ghoda Hi Saya॥

Parachya Chautha Bhairava Mara। Bhakta Janon Ka Kashta Nivara॥
Panchama Parachya Ratana Paya। Pungala Ja Prabhu Fanda Chhudaya॥

Parachya Chhatha Vijayasinha Paya। Jala Nagara Sharanagata Aaya॥
Parachya Saptam Sugana Paya। Muva Putra Hansata Bhaga Aaya॥

Parachya Ashtam Bauhita Paya। Ja Paradesha Dravya Bahu Laya॥
Bhanvara Dubati Nava Ubari। Pragata Tera Pahunche Avatari॥

Navaman Parachya Virama Paya। Baniyan Aa Jaba Hala Sunaya॥
Dasavan Parachya Pa Binjara। Mishri Bani Namaka Saba Khara॥

Parachya Gyaraha Kirapa Thari। Namaka Hua Mishri Phira Sari॥
Parachya Dvadasha Thokara Mari। Nikalanga Nadi Siraji Pyari॥

Parachya Terahavan Pira Pari Padharaya। Lyaya Katora Karaja Sara॥
Chaudahavan Parachya Jabho Paya। Nijasara Jala Khara Karavaya॥

Parachya Pandrah Phira Batalaya। Rama Sarovara Prabhu Khudvaya॥
Parachya Solaha Harabu Paya। Darsha Paya Atishaya Harashaya॥

Parachya Satraha Hara Ji Paya। Dudha Thana Bakaraya Ke Aaya॥
Sukhi Nadi Pani Kinho। Atma Gyana Haraji Ne Dinho॥

Parachya Atharahavan Hakima Paya। Sute Ko Dharati Ludhkaya॥
Parachya Unnisavan Dala Ji Paya। Putra Paya Mana Mein Harashaya॥

Parachya Bisavan Paya Sethani। Aaye Prabhu Suna Gadgada Vani॥
Turanta Setha Sarjivana Kinha। Ukta Ujagara Abhaya Vara Dinha॥

Parachya Ikkisavan Chora Jo Paya। Ho Andha Karani Phala Paya॥
Parachya Baisavan Mirjo Chihan। Sato Tava Bedha Prabhu Dinhan॥

Parachya Teisavan Badashaha Paya। Phera Bhakta Ko Nahin Sataya॥
Parachya Chaubisavan Bakhshi Paya। Muva Putra Pala Mein Utha Dhaya॥

Jaba-Jaba Jisane Sumarana Kinhan। Taba-Taba Aa Tuma Darshana Dinhan॥
Bhakta Tera Suna Aatura Dhate। Chadha Lile Para Jaldi Aate॥

Jo Jana Prabhu Ki Lila Gaven। Manavanchhita Karaja Phala Paven॥
Yaha Chalisa Sune Sunave। Take Kashta Sakala Kata Jave॥

Jai Jai Jai Prabhu Lila Dhari। Teri Mahima Aparamapari॥
Main Murakha Kya Guna Taba Gaun। Kahan Buddhi Sharada Si Laun॥

Nahin Buddhi Bala Ghata Lava Lesha। Mati Anusara Rachi Chalisa॥
Dasa Sabhi Sharana Mein Teri। Rakhiyon Prabhu Lajja Meri॥

॥ Doha ॥
Bhakta Hetu Avatara Le, Kinhe Kaja Apara।
Ramdeva Prabhu Rakhiye, Bhavasagara Se Para॥"""

# 6. Update drik_chalisa_collections.json
with open('drik_chalisa_collections.json', encoding='utf-8') as f:
    chalisa_data = json.load(f)

rama_items = chalisa_data['rama']['items']
target_item = None
for item in rama_items:
    if item['id'] == 'drik_chalisa_20':
        target_item = item
        break

if target_item:
    target_item['title'] = 'श्री रामदेव चालीसा'
    target_item['title_en'] = 'Shri Ramdev Chalisa'
    target_item['en_line'] = 'Jai Jai Ramdeva Sura Raya'
    target_item['hi_line'] = 'जय जय रामदेव सुर राया'
    target_item['sub'] = 'जय जय रामदेव सुर राया • Drik Panchang Verified'
    target_item['thumb'] = 'assets/gallery/bal_rama_little.jpg'
    target_item['audio_url'] = 'https://www.youtube.com/watch?v=UbEopserUb0'
    target_item['video_id'] = 'UbEopserUb0'
    target_item['drik_url'] = 'https://www.drikpanchang.com/lyrics/chalisa/shri-ramdev/shri-ramdev-chalisa.html?lang=hi&ck=1'
    target_item['source'] = 'Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)'
    target_item['content'] = ramdev_chalisa_content
    target_item['meaning'] = ramdev_chalisa_meaning
    target_item['vidhi'] = ramdev_chalisa_vidhi
    target_item['significance'] = ramdev_chalisa_significance
    target_item['english_lyrics'] = ramdev_chalisa_en
    print("Updated drik_chalisa_20 in drik_chalisa_collections.json!")
else:
    print("ERROR: drik_chalisa_20 not found in rama items!")

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

# Replace chalisa_ramdev in CONTENT in app.js
c_ramdev_record = f"""chalisa_ramdev: {{
    title: 'श्री रामदेव चालीसा',
    deity: 'पीरों के पीर बाबा रामदेव जी (रामापीर)',
    mantra: '॥ जय बाबे री • ॐ श्री रामदेवाय नमः ॥',
    text: `{ramdev_chalisa_content}`,
    meaning: `{ramdev_chalisa_meaning}`,
    vidhi: `{ramdev_chalisa_vidhi}`,
    significance: `{ramdev_chalisa_significance}`,
    english_lyrics: `{ramdev_chalisa_en}`,
    audio_url: 'https://www.youtube.com/watch?v=UbEopserUb0',
    video_id: 'UbEopserUb0',
    thumb: 'assets/gallery/bal_rama_little.jpg',
    drik_url: 'https://www.drikpanchang.com/lyrics/chalisa/shri-ramdev/shri-ramdev-chalisa.html?lang=hi&ck=1'
  }},
  """

pos_r = app_js.find('chalisa_ramdev:')
if pos_r != -1:
    pos_next = app_js.find('chalisa_kubera:', pos_r)
    if pos_next != -1:
        app_js = app_js[:pos_r] + c_ramdev_record + app_js[pos_next:]
        print("Replaced chalisa_ramdev in CONTENT successfully!")
    else:
        print("ERROR: Could not find chalisa_kubera after chalisa_ramdev")
else:
    print("ERROR: chalisa_ramdev not found in app.js")

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
