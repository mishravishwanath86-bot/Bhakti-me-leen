import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री ब्रह्मा चालीसा ॥

॥ दोहा ॥
जय ब्रह्मा जय स्वयम्भू, चतुरानन सुखमूल।
करहु कृपा निज दास पै, रहहु सदा अनुकूल॥
तुम सृजक ब्रह्माण्ड के, अज विधि घाता नाम।
विश्वविधाता कीजिये, जन पै कृपा ललाम॥

॥ चौपाई ॥
जय जय कमलासान जगमूला। रहहु सदा जनपै अनुकूला॥१॥
रुप चतुर्भुज परम सुहावन। तुम्हें अहैं चतुर्दिक आनन॥२॥
रक्तवर्ण तव सुभग शरीरा। मस्तक जटाजुट गंभीरा॥३॥
ताके ऊपर मुकुट बिराजै। दाढ़ी श्वेत महाछवि छाजै॥४॥
श्वेतवस्त्र धारे तुम सुन्दर। है यज्ञोपवीत अति मनहर॥५॥
कानन कुण्डल सुभग बिराजहिं। गल मोतिन की माला राजहिं॥६॥
चारिहु वेद तुम्हीं प्रगटाये। दिव्य ज्ञान त्रिभुवनहिं सिखाये॥७॥
ब्रह्मलोक शुभ धाम तुम्हारा। अखिल भुवन महँ यश बिस्तारा॥८॥
अर्द्धांगिनि तव है सावित्री। अपर नाम हिये गायत्री॥९॥
सरस्वती तब सुता मनोहर। वीणा वादिनि सब विधि मुन्दर॥१०॥
कमलासन पर रहे बिराजे। तुम हरिभक्ति साज सब साजे॥११॥
क्षीर सिन्धु सोवत सुरभूपा। नाभि कमल भो प्रगट अनूपा॥१२॥
तेहि पर तुम आसीन कृपाला। सदा करहु सन्तन प्रतिपाला॥१३॥
एक बार की कथा प्रचारी। तुम कहँ मोह भयेउ मन भारी॥१४॥
कमलासन लखि कीन्ह बिचारा। और न कोउ अहै संसारा॥१५॥
तब तुम कमलनाल गहि लीन्हा। अन्त बिलोकन कर प्रण कीन्हा॥१६॥
कोटिक वर्ष गये यहि भांती। भ्रमत भ्रमत बीते दिन राती॥१७॥
पै तुम ताकर अन्त न पाये। ह्वै निराश अतिशय दुःखियाये॥१८॥
पुनि बिचार मन महँ यह कीन्हा। महापद्म यह अति प्राचीन॥१९॥
याको जन्म भयो को कारन। तबहीं मोहि करयो यह धारन॥२०॥
अखिल भुवन महँ कहँ कोई नाहीं। सब कुछ अहै निहित मो माहीं॥२१॥
यह निश्चय करि गरब बढ़ायो। निज कहँ ब्रह्म मानि सुखपाये॥२२॥
गगन गिरा तब भई गंभीरा। ब्रह्मा वचन सुनहु धरि धीरा॥२३॥
सकल सृष्टि कर स्वामी जोई। ब्रह्म अनादि अलख है सोई॥२४॥
निज इच्छा इन सब निरमाये। ब्रह्मा विष्णु महेश बनाये॥२५॥
सृष्टि लागि प्रगटे त्रयदेवा। सब जग इनकी करिहै सेवा॥२६॥
महापद्म जो तुम्हरो आसन। ता पै अहै विष्णु को शासन॥२७॥
विष्णु नाभितें प्रगट्यो आई। तुम कहँ सत्य दीन्ह समुझाई॥२८॥
भेंटहु जाई विष्णु हितमानी। यह कहि बन्द भई नभवानी॥२९॥
ताहि श्रवण कहि अचरज माना। पुनि चतुरानन कीन्ह पयाना॥३०॥
कमल नाल धरि नीचे आवा। तहां विष्णु के दर्शन पावा॥३१॥
शयन करत देखे सुरभूपा। श्यामवर्ण तनु परम अनूपा॥३२॥
सोहत चतुर्भुजा अतिसुन्दर। क्रीटमुकट राजत मस्तक पर॥३३॥
गल बैजन्ती माल बिराजै। कोटि सूर्य की शोभा लाजै॥३४॥
शंख चक्र अरु गदा मनोहर। शेष नाग शय्या अति मनहर॥३५॥
दिव्यरुप लखि कीन्ह प्रणामू। हर्षित भे श्रीपति सुख धामू॥३६॥
बहु विधि विनय कीन्ह चतुरानन। तब लक्ष्मी पति कहेउ मुदित मन॥३७॥
ब्रह्मा दूरि करहु अभिमाना। ब्रह्मारुप हम दोउ समाना॥३८॥
तीजे श्री शिवशंकर आहीं। ब्रह्मरुप सब त्रिभुवन मांही॥३९॥
तुम सों होई सृष्टि विस्तारा। हम पालन करिहैं संसारा॥४०॥
शिव संहार करहिं सब केरा। हम तीनहुं कहँ काज धनेरा॥४१॥
अगुणरुप श्री ब्रह्म बखानहु। निराकार तिनकहँ तुम जानहु॥४२॥
हम साकार रुप त्रयदेवा। करिहैं सदा ब्रह्म की सेवा॥४३॥
यह सुनि ब्रह्मा परम सिहाये। परब्रह्म के यश अति गाये॥४४॥
सो सब विदित वेद के नामा। मुक्ति रुप सो परम ललामा॥४५॥
यहि विधि प्रभु भो जनम तुम्हारा। पुनि तुम प्रगट कीन्ह संसारा॥४६॥
नाम पितामह सुन्दर पायेउ। जड़ चेतन सब कहँ निरमायेउ॥४७॥
लीन्ह अनेक बार अवतारा। सुन्दर सुयश जगत विस्तारा॥४८॥
देवदनुज सब तुम कहँ ध्यावहिं। मनवांछित तुम सन सब पावहिं॥४९॥
जो कोउ ध्यान धरै नर नारी। ताकी आस पुजावहु सारी॥५०॥
पुष्कर तीर्थ परम सुखदाई। तहँ तुम बसहु सदा सुरराई॥५१॥
कुण्ड नहाइ करहि जो पूजन। ता कर दूर होई सब दूषण॥५२॥"""

meaning = """॥ श्री ब्रह्मा चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "जय ब्रह्मा जय स्वयम्भू, चतुरानन सुखमूल। करहु कृपा निज दास पै, रहहु सदा अनुकूल॥"
भावार्थ: हे स्वयंभू, चारों मुखों से चारों वेदों का उच्चारण करने वाले और समस्त सांसारिक व आत्मिक सुखों के मूल कारण भगवान ब्रह्मा जी! आपकी सदा जय हो। अपने इस अनन्य सेवक पर अपनी कृपा दृष्टि बनाए रखिए और सदा मेरे अनुकूल व सहायक रहिए।
• "तुम सृजक ब्रह्माण्ड के, अज विधि घाता नाम। विश्वविधाता कीजिये, जन पै कृपा ललाम॥"
भावार्थ: आप ही इस चराचर ब्रह्मांड के परम सृष्टिकर्ता (सृजक) हैं; अजन्मा, विधि, विधाता और धाता आपके ही पावन नाम हैं। हे विश्वविधाता! अपने इस शरणागत दास पर अपनी परम सुंदर व कल्याणकारी कृपा प्रदान कीजिए।

【५२ चौपाइयां — पद्यवार भावार्थ】
१-६. "जय जय कमलासान जगमूला... गल मोतिन की माला राजहिं॥"
भावार्थ: कमल के दिव्य आसन पर विराजमान और संपूर्ण जगत के मूल कारण हे ब्रह्मा जी! आपकी जय हो, आप सदा भक्तों पर प्रसन्न रहें। आपका चतुर्भुज रूप अत्यंत मनोहारी है और चारों दिशाओं में आपके चार पावन मुख (चतुरानन) सुशोभित हैं। आपका शरीर सुंदर रक्त वर्ण (अरुण कांति) से दीप्तिमान है और आपके मस्तक पर गंभीर जटाजूट विराजमान है। उस जटाजूट के ऊपर भव्य स्वर्ण मुकुट सुशोभित है और आपकी श्वेत दाढ़ी अलौकिक शोभा प्रदान कर रही है। आप श्वेत वस्त्र और मनमोहक यज्ञोपवीत (जनेऊ) धारण किए हुए हैं। आपके कानों में सुंदर कुंडल और गले में मोतियों की भव्य माला शोभा पा रही है।

७-१३. "चारिहु वेद तुम्हीं प्रगटाये... सदा करहु सन्तन प्रतिपाला॥"
भावार्थ: चारों वेदों (ऋग्वेद, यजुर्वेद, सामवेद, अथर्ववेद) को आपने ही प्रकट किया और तीनों लोकों को दिव्य ब्रह्मज्ञान की शिक्षा दी। आपका परम पावन शुभ धाम 'ब्रह्मलोक' है और आपका यश संपूर्ण ब्रह्मांड में फैला हुआ है। माता सावित्री आपकी अर्द्धांगिनी हैं, जिन्हें गायत्री नाम से भी स्मरण किया जाता है। वीणावादिनी, विद्या की अधिष्ठात्री देवी माता सरस्वती आपकी मनोहारिणी सुता (पुत्री) हैं जो सब प्रकार से सौंदर्य व कला का धाम हैं। आप कमल के आसन पर विराजमान होकर निरंतर श्रीहरि की भक्ति के साधन सजाते हैं। जब क्षीरसागर में देवों के स्वामी श्रीहरि शयन कर रहे थे, तब उनकी नाभि से एक अनुपम दिव्य कमल प्रकट हुआ। हे कृपालु ब्रह्मा जी! आप उसी नाभि-कमल पर आसीन होकर प्रकट हुए और सदा साधु-संतों का प्रतिपालन करते हैं।

१४-२२. "एक बार की कथा प्रचारी... निज कहँ ब्रह्म मानि सुखपाये॥"
भावार्थ: एक समय की प्राचीन कथा प्रसिद्ध है कि आपके मन में भारी मोह उत्पन्न हो गया। अपने आपको अकेले कमलासन पर देखकर आपने विचार किया कि इस विशाल संसार में मेरे अतिरिक्त कोई अन्य नहीं है। तब आपने उस कमलनाल को पकड़कर उसके अंत (मूल) का पता लगाने का दृढ़ प्रण किया। इस प्रकार खोजते-भटकते करोड़ों वर्ष और अनगिनत दिन-रात बीत गए। परंतु आप उस कमलनाल का अंत न पा सके और अत्यधिक निराश व दुखी हो गए। फिर आपने मन में विचार किया कि यह महाकमल अत्यंत प्राचीन है, इसके प्रकट होने का कोई न कोई गूढ़ कारण अवश्य है, जिसने मुझे भी धारण कर रखा है। फिर भी मोहवश आपने सोचा कि समस्त ब्रह्मांड में कोई नहीं है और सब कुछ मुझमें ही निहित है; ऐसा निश्चय करके आपने अहंकार बढ़ाया और स्वयं को ही परब्रह्म मानकर प्रसन्न होने लगे।

२३-२९. "गगन गिरा तब भई गंभीरा... यह कहि बन्द भई नभवानी॥"
भावार्थ: तभी आकाश से एक गंभीर आकाशवाणी गूंजी—हे ब्रह्मा! धैर्य धारण करके मेरे वचन सुनो। इस संपूर्ण सृष्टि का जो परम स्वामी है, वह अनादि, अजन्मा और अलख परब्रह्म है। उसी परब्रह्म ने अपनी इच्छा से इन सबकी रचना की और ब्रह्मा, विष्णु तथा महेश (त्रिमूर्ति) को प्रकट किया। सृष्टि के सृजन, पालन और संहार हेतु ये तीनों देव प्रकट हुए हैं और संपूर्ण जगत इनकी सेवा करेगा। जिस महापद्म (कमल) पर आपका आसन है, उस पर साक्षात् भगवान विष्णु का आधिपत्य है। आप भगवान विष्णु की नाभि से ही प्रकट हुए हैं, यह परम सत्य जान लीजिए। अब आप जाकर भगवान विष्णु से भेंट कीजिए; इतना कहकर वह आकाशवाणी मौन हो गई।

३०-३६. "ताहि श्रवण कहि अचरज माना... हर्षित भे श्रीपति सुख धामू॥"
भावार्थ: उस आकाशवाणी को सुनकर चतुरानन ब्रह्मा जी को बड़ा आश्चर्य हुआ और उन्होंने पुनः नीचे की ओर प्रस्थान किया। कमलनाल के सहारे नीचे उतरने पर उन्हें साक्षात् भगवान श्रीहरि विष्णु के दिव्य दर्शन प्राप्त हुए। उन्होंने देखा कि देवों के स्वामी, अत्यंत अनुपम श्यामवर्ण शरीर वाले श्रीहरि शेषनाग की शय्या पर योगनिद्रा में शयन कर रहे हैं। उनके चारों भुजाएं अत्यंत सुंदर हैं और मस्तक पर किरीट मुकुट सुशोभित है। गले में वैजयंती माला विराजमान है, जिसकी आभा करोड़ों सूर्यों की शोभा को भी लजा देती है। हाथों में शंख, चक्र, गदा और पद्म कमल शोभायमान हैं और शेषनाग की शय्या मन को हरने वाली है। इस अलौकिक दिव्य रूप का दर्शन करके ब्रह्मा जी ने साष्टांग प्रणाम किया, जिससे सुखधाम लक्ष्मीपति श्रीहरि अत्यंत हर्षित हुए।

३७-४५. "बहु विधि विनय कीन्ह चतुरानन... मुक्ति रुप सो परम ललामा॥"
भावार्थ: जब चतुरानन ब्रह्मा जी ने अनेक प्रकार से भगवान विष्णु की विनीत स्तुति की, तब लक्ष्मीपति ने प्रसन्न मन से कहा—हे ब्रह्मा! अपने मन का अहंकार त्याग दीजिए; तात्विक दृष्टि से परब्रह्म रूप में हम दोनों एक समान हैं। और तीसरे स्वयं देवाधिदेव शिवशंकर हैं; संपूर्ण त्रिलोकी में हम तीनों एक ही ब्रह्म के स्वरूप हैं। आपके द्वारा इस सृष्टि का विस्तार (सृजन) होगा, हम इस संसार का पालन करेंगे, और भगवान शिव समय आने पर सबका संहार करेंगे; हम तीनों के पास बहुत बड़ा कार्यभार है। जिस परब्रह्म की वेद स्तुति करते हैं, वे मूलतः निर्गुण और निराकार हैं। और हम तीनों देव उसी परब्रह्म के सगुण साकार रूप होकर सदा उनकी सेवा करते हैं। यह सुनकर ब्रह्मा जी अत्यंत प्रसन्न हुए और उन्होंने परब्रह्म के पावन यश का गान किया, जो वेदों में मुक्तिदाता के रूप में प्रसिद्ध है।

४६-५२. "यहि विधि प्रभु भो जनम तुम्हारा... ता कर दूर होई सब दूषण॥"
भावार्थ: हे प्रभु! इस प्रकार आपका प्राकट्य हुआ और फिर आपने इस संपूर्ण संसार की रचना की। आपने समस्त सृष्टि के 'पितामह' (परम पिता) की सुंदर उपाधि पाई और चर-अचर, जड़-चेतन संपूर्ण प्राणियों की रचना की। आपने धर्म की रक्षा हेतु अनेक अवतार लिए और जगत में अपना सुंदर सुयश फैलाया। देवता और दानव सभी आपका ध्यान करते हैं और आपसे मनवांछित फल प्राप्त करते हैं। जो भी स्त्री-पुरुष आपका ध्यान धरते हैं, आप उनकी समस्त मनोकामनाएं पूर्ण करते हैं। राजस्थान का परम पावन पुष्कर तीर्थ अत्यंत सुखदायी है, जहाँ हे देवराज ब्रह्मा! आप सदा निवास करते हैं। जो भी भक्त पुष्कर के पवित्र सरोवर/कुंड में स्नान कर आपका विधिपूर्वक पूजन करता है, उसके समस्त पाप, दोष और ताप सदा के लिए दूर हो जाते हैं।"""

vidhi = """॥ श्री ब्रह्मा चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल सूर्योदय वेला, ब्रह्ममुहूर्त (प्रातः ४:०० से ६:०० बजे तक), जो साक्षात् ब्रह्मा जी का काल माना जाता है।
- सर्वोत्तम वार: रविवार (सृष्टि के आदि दिवस के रूप में) तथा बुधवार (बुद्धि व विद्या हेतु)।
- महापर्व व पावन तिथियां: कार्तिक मास की पूर्णिमा (पुष्कर मेला महास्नान), वैशाख पूर्णिमा, ब्रह्म द्वादशी, तथा प्रत्येक मास की पूर्णिमा तिथि।

२. दिशा, आसन व वस्त्र:
- दिशा: पूर्व अथवा उत्तर-पूर्व (ईशान कोण) की ओर मुख करके बैठें।
- आसन: श्वेत अथवा पीले रंग का स्वच्छ ऊनी अथवा कुशा का आसन बिछाएं।
- वस्त्र: साधक को स्वच्छ श्वेत (सफेद) अथवा हल्के पीले रंग के वस्त्र धारण करने चाहिए।

३. पूजन सामग्री व प्रिय नैवेद्य:
- दीपक: गाय के शुद्ध देशी घी का दीपक प्रज्वलित करें।
- पुष्प व तिलक: श्वेत पुष्प (सफेद कमल, मोगरा, चमेली, कुंद) अथवा पीले गेंदे के फूल अर्पित करें। श्वेत चंदन अथवा केसर-चंदन का तिलक लगाएं।
- प्रिय नैवेद्य: पंचामृत, मखाने की खीर, बताशे, सफेद मिठाई, मिश्री, पीले फल (केला), तथा ऋतुफल।

४. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन व पवित्रीकरण करें।
- भगवान श्रीहरि विष्णु, माता सरस्वती एवं माता गायत्री-सावित्री का ध्यान करें।
- 'ॐ ब्रह्माणे नमः' अथवा 'ॐ ऐं ह्रीं श्रीं क्लीं सौः जगत्सृष्टिकर्त्रे नमः' मन्त्र का कम से कम १ माला (१०८ बार) जप करें।
- इसके पश्चात शांत व एकाग्र चित्त से 'श्री ब्रह्मा चालीसा' का १, ३, अथवा ५ बार श्रद्धापूर्वक पाठ करें।
- पाठ के उपरांत पुष्कर तीर्थ और पितामह ब्रह्मा जी का ध्यान करते हुए आरती गाएं और प्रसाद ग्रहण करें।"""

significance = """॥ श्री ब्रह्मा चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. सृजन शक्ति, तीक्ष्ण बुद्धि व विद्या सिद्धि:
"चारिहु वेद तुम्हीं प्रगटाये। दिव्य ज्ञान त्रिभुवनहिं सिखाये॥"
भगवान ब्रह्मा जी समस्त वेदों, शास्त्रों और ज्ञान के आदि प्रवर्तक हैं। चालीसा के नियमित पाठ से साधक में अद्वितीय बौद्धिक क्षमता, रचनात्मकता (Creativity), स्मरण शक्ति और विद्या में अभूतपूर्व सफलता प्राप्त होती है।

२. भाग्य-सुधार व प्रारब्ध दोष निवारण:
भगवान ब्रह्मा जी को 'विधाता' कहा जाता है जो समस्त जीवों के भाग्य का निर्धारण करते हैं। श्रद्धापूर्वक ब्रह्मा चालीसा का पाठ करने से दुर्भाग्य, प्रतिकूल प्रारब्ध और जीवन के अवरोध दूर होकर सौभाग्य का उदय होता है।

३. अहंकार का नाश व आत्मिक शांति:
चालीसा में ब्रह्मा जी के अहंकार भंजन और भगवान विष्णु की शरण में जाने का आध्यात्मिक प्रसंग वर्णित है। इसका पाठ मनुष्य के भीतर के अहंकार को मिटाकर उसे विनम्र, विवेकशील और आत्मज्ञानी बनाता है।

४. पुष्कर तीर्थ स्नान तुल्य पुण्य फल:
"पुष्कर तीर्थ परम सुखदाई। तहँ तुम बसहु सदा सुरराई॥ कुण्ड नहाइ करहि जो पूजन। ता कर दूर होई सब दूषण॥"
जो साधक पुष्कर तीर्थ जाने में असमर्थ हैं, वे घर पर ही शुद्ध भाव से इस चालीसा का पाठ कर पुष्कर सरोवर के पावन स्नान और पितामह ब्रह्मा के प्रत्यक्ष दर्शन का फल प्राप्त करते हैं।

५. समस्त मनोकामनाओं की सिद्धि व पाप दोष मुक्ति:
"जो कोउ ध्यान धरै नर नारी। ताकी आस पुजावहु सारी॥"
सच्चे हृदय से पाठ करने वाले भक्तों की समस्त लौकिक व आध्यात्मिक मनोकामनाएं पूर्ण होती हैं और जीवन के समस्त दूषण (पाप-ताप) नष्ट हो जाते हैं।"""

english_lyrics = """॥ Shri Brahma Chalisa ॥

॥ Doha ॥
Jaya Brahmaa Jaya Svayambhoo, Chaturaanana Sukhamoola।
Karahu Kripaa Nija Daasa Pai, Rahahu Sadaa Anukoola॥
Tuma Srijaka Brahmaanda Ke, Aja Vidhi Ghaataa Naama।
Vishvavidhaataa Keejiye, Jana Pai Kripaa Lalaama॥

॥ Chaupai ॥
Jaya Jaya Kamalaasaana Jagamoolaa। Rahahu Sadaa Janapai Anukoolaa॥1॥
Roopa Chaturbhuja Parama Suhaavana। Tumhen Ahain Chaturdika Aanana॥2॥
Raktavarna Tava Subhaga Shareeraa। Mastaka Jataajuta Gambheeraa॥3॥
Taake Oopara Mukuta Biraajai। Daadhee Shweta Mahaachhavi Chhaajai॥4॥
Shweta-Vastra Dhaare Tuma Sundara। Hai Yagyopaveeta Ati Manahara॥5॥
Kaanana Kundala Subhaga Biraajahin। Gala Motina Kee Maalaa Raajahin॥6॥
Chaarihu Veda Tumheen Pragataaye। Divya Gyaana Tribhuvanahin Sikhaaye॥7॥
Brahmaloka Shubha Dhaama Tumhaaraa। Akhila Bhuvana Mahan Yasha Bistaaraa॥8॥
Arddhaangini Tava Hai Saavitree। Apara Naama Hiye Gaayatree॥9॥
Saraswatee Taba Sutaa Manohara। Veenaa Vaadini Saba Vidhi Mundara॥10॥
Kamalaasana Para Rahe Biraaje। Tuma Haribhakti Saaja Saba Saaje॥11॥
Ksheera Sindhu Sovata Surabhoopaa। Naabhi Kamala Bho Pragata Anoopaa॥12॥
Tehi Para Tuma Aaseena Kripaalaa। Sadaa Karahu Santana Pratipaalaa॥13॥
Eka Baara Kee Kathaa Prachaaree। Tuma Kahan Moha Bhaye-u Mana Bhaaree॥14॥
Kamalaasana Lakhi Keenha Bichaaraa। Aura Na Kou Ahai Sansaaraa॥15॥
Taba Tuma Kamalanaala Gahi Leenhaa। Anta Bilokana Kara Prana Keenhaa॥16॥
Kotika Varsha Gaye Yahi Bhaantee। Bhramata Bhramata Beete Dina Raatee॥17॥
Pai Tuma Taakara Anta Na Paaye। Hvai Niraasha Atishaya Dukhiyaaye॥18॥
Puni Bichaara Mana Mahan Yaha Keenhaa। Mahaapadma Yaha Ati Praacheena॥19॥
Yaako Janma Bhayo Ko Kaarana। Tabaheen Mohi Karayo Yaha Dhaarana॥20॥
Akhila Bhuvana Mahan Kahan Ko-ee Naaheen। Saba Kuchha Ahai Nihita Mo Maaheen॥21॥
Yaha Nishchaya Kari Garaba Badhaayo। Nija Kahan Brahma Maani Sukhapaaye॥22॥
Gagana Giraa Taba Bha-ee Gambheeraa। Brahmaa Vachana Sunahu Dhari Dheeraa॥23॥
Sakala Srishti Kara Svaamee Jo-ee। Brahma Anaadi Alakha Hai So-ee॥24॥
Nija Ichhaa Ina Saba Nirmaaye। Brahmaa Vishnu Mahesha Banaaye॥25॥
Srishti Laagi Pragate Trayadeva। Saba Jaga Inakee Karihai Sevaa॥26॥
Mahaapadma Jo Tumharo Aasana। Taa Pai Ahai Vishnu Ko Shaasana॥27॥
Vishnu Naabhiten Pragatyau Aa-ee। Tuma Kahan Satya Deenha Samujhaa-ee॥28॥
Bhentahu Jaa-ee Vishnu Hitamaanee। Yaha Kahi Banda Bha-ee Nabha-Vaanee॥29॥
Taahi Shravana Kahi Acharaja Maanaa। Puni Chaturaanana Keenha Payaanaa॥30॥
Kamala Naala Dhari Neeche Aavaa। Tahaan Vishnu Ke Darshana Paavaa॥31॥
Shayana Karata Dekhe Surabhoopaa। Shyaamavarna Tanu Parama Anoopaa॥32॥
Sohata Chaturbhujaa Atisundara। Kreetamukata Raajata Mastaka Para॥33॥
Gala Baijantee Maala Biraajai। Koti Soorya Kee Shobhaa Laajai॥34॥
Shankha Chakra Aru Gadaa Manohara। Shesha Naaga Shayyaa Ati Manahara॥35॥
Divyaroopa Lakhi Keenha Pranaamoo। Harshita Bhe Shreepati Sukha Dhaamoo॥36॥
Bahu Vidhi Vinaya Keenha Chaturaanana। Taba Lakshmee Pati Kaheu Mudita Mana॥37॥
Brahmaa Doori Karahu Abhimaanaa। Brahmaroopa Hama Dou Samaanaa॥38॥
Teeje Shree Shivashankara Aaheen। Brahmaroopa Saba Tribhuvana Maaheen॥39॥
Tuma Son Ho-ee Srishti Vistaaraa। Hama Paalana Karihain Sansaaraa॥40॥
Shiva Sanhaara Karahin Saba Keraa। Hama Teenahun Kahan Kaaja Dhaneraa॥41॥
Agunaroopa Shree Brahma Bakhaanahu। Niraakaara Tinakahan Tuma Jaanahu॥42॥
Hama Saakaara Roopa Trayadeva। Karihain Sadaa Brahma Kee Sevaa॥43॥
Yaha Suni Brahmaa Parama Sihaaye। Parabrahma Ke Yasha Ati Gaaye॥44॥
So Saba Vidita Veda Ke Naamaa। Mukti Roopa So Parama Lalaamaa॥45॥
Yahi Vidhi Prabhu Bho Janama Tumhaaraa। Puni Tuma Pragata Keenha Sansaaraa॥46॥
Naama Pitaamaha Sundara Paaye-u। Jada Chetana Saba Kahan Nirmaaye-u॥47॥
Leenha Aneka Baara Avataaraa। Sundara Suyasha Jagata Vistaaraa॥48॥
Devadanuja Saba Tuma Kahan Dhyaavahin। Manavaanchhita Tuma Sana Saba Paavahin॥49॥
Jo Kou Dhyaana Dharai Nara Naaree। Taakee Aasa Pujaavahu Saaree॥50॥
Pushkara Teertha Parama Sukhadaa-ee। Tahan Tuma Basahu Sadaa Suraraa-ee॥51॥
Kunda Nahaa-i Karahi Jo Poojana। Taa Kara Doora Ho-ee Saba Dooshana॥52॥"""

# 1. Update drik_chalisa_12 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["vishnu"]["items"]:
    if item["id"] == "drik_chalisa_12":
        item["title"] = "भगवान ब्रह्मा चालीसा"
        item["title_en"] = "Lord Brahma Chalisa"
        item["en_line"] = "Jai Jai Kamalasana Jagamula"
        item["hi_line"] = "जय जय कमलासान जगमूला"
        item["sub"] = "जय जय कमलासान जगमूला • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_brahma_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=4a5uYc9s_bE"
        item["video_id"] = "4a5uYc9s_bE"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/lord-brahma/shri-brahma-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "सृष्टिकर्ता पितामह भगवान ब्रह्मा"
        item["section"] = "श्री विष्णु, ब्रह्मा व नृसिंह चालीसा"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_12 in drik_chalisa_collections.json successfully!")

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

# 3. Update chalisa_brahma in CONTENT in app.js
content_obj = {
    "title": "श्री ब्रह्मा चालीसा",
    "title_en": "Lord Brahma Chalisa",
    "en_line": "Jai Jai Kamalasana Jagamula",
    "hi_line": "जय जय कमलासान जगमूला",
    "sub": "जय जय कमलासान जगमूला • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_brahma_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=4a5uYc9s_bE",
    "video_id": "4a5uYc9s_bE",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/lord-brahma/shri-brahma-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "सृष्टिकर्ता पितामह भगवान ब्रह्मा",
    "section": "श्री विष्णु, ब्रह्मा व नृसिंह चालीसा",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

brahma_content_js = "  chalisa_brahma: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

pos_b = app_text.find("  chalisa_brahma: {")
if pos_b != -1:
    pos_next = app_text.find("  chalisa_bhairav: {", pos_b)
    if pos_next != -1:
        app_text = app_text[:pos_b] + brahma_content_js + app_text[pos_next:]
        print("Replaced chalisa_brahma in CONTENT!")
    else:
        print("ERROR: Could not find chalisa_bhairav after chalisa_brahma!")
else:
    print("ERROR: Could not find chalisa_brahma in app.js!")

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
