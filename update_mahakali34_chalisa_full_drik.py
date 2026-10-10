import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री महाकाली चालीसा ॥

॥ दोहा ॥
जय जय सीताराम के, मध्यवासिनी अम्ब।
देहु दर्श जगदम्ब, अब करो न मातु विलम्ब॥
जय तारा जय कालिका, जय दश विद्या वृन्द।
काली चालीसा रचत, एक सिद्धि कवि हिन्द॥
प्रातः काल उठ जो पढ़े, दुपहरिया या शाम।
दुःख दरिद्रता दूर हों, सिद्धि होय सब काम॥

॥ चौपाई ॥
जय काली कंकाल मालिनी। जय मंगला महा कपालिनी॥१॥
रक्तबीज बधकारिणि माता। सदा भक्त जननकी सुखदाता॥२॥
शिरो मालिका भूषित अंगे। जय काली जय मद्य मतंगे॥३॥
हर हृदयारविन्द सुविलासिनि। जय जगदम्बा सकल दुःख नाशिनि॥४॥
ह्रीं काली श्री महाकाली। क्रीं कल्याणी दक्षिणाकाली॥५॥
जय कलावती जय विद्यावती। जय तारा सुन्दरी महामति॥६॥
देहु सुबुद्धि हरहु सब संकट। होहु भक्त के आगे परगट॥७॥
जय ॐ कारे जय हुंकारे। महा शक्ति जय अपरम्पारे॥८॥
कमला कलियुग दर्प विनाशिनी। सदा भक्त जन के भयनाशिनी॥९॥
अब जगदम्ब न देर लगावहु। दुख दरिद्रता मोर हटावहु॥१०॥
जयति कराल कालिका माता। कालानल समान द्युतिगाता॥११॥
जयशंकरी सुरेशि सनातनि। कोटि सिद्धि कवि मातु पुरातनि॥१२॥
कपर्दिनी कलि कल्प बिमोचनि। जय विकसित नव नलिनविलोचनि॥१३॥
आनन्द करणि आनन्द निधाना। देहुमातु मोहि निर्मल ज्ञाना॥१४॥
करुणामृत सागर कृपामयी। होहु दुष्ट जनपर अब निर्दयी॥१५॥
सकल जीव तोहि परम पियारा। सकल विश्व तोरे आधारा॥१६॥
प्रलय काल में नर्तन कारिणि। जय जननी सब जग की पालनि॥१७॥
महोदरी महेश्वरी माया। हिमगिरि सुता विश्व की छाया॥१८॥
स्वछन्द रद मारद धुनि माही। गर्जत तुम्ही और कोउ नाही॥१९॥
स्फुरति मणिगणाकार प्रताने। तारागण तू ब्योम विताने॥२०॥
श्री धारे सन्तन हितकारिणी। अग्नि पाणि अति दुष्ट विदारिणि॥२१॥
धूम्र विलोचनि प्राण विमोचनि। शुम्भ निशुम्भ मथनि वरलोचनि॥२२॥
सहस भुजी सरोरुह मालिनी। चामुण्डे मरघट की वासिनी॥२३॥
खप्पर मध्य सुशोणित साजी। मारेहु माँ महिषासुर पाजी॥२४॥
अम्ब अम्बिका चण्ड चण्डिका। सब एके तुम आदि कालिका॥२५॥
अजा एकरूपा बहुरूपा। अकथ चरित्र तव शक्ति अनूपा॥२६॥
कलकत्ता के दक्षिण द्वारे। मूरति तोर महेशि अपारे॥२७॥
कादम्बरी पानरत श्यामा। जय मातंगी काम के धामा॥२८॥
कमलासन वासिनी कमलायनि। जय श्यामा जय जय श्यामायनि॥२९॥
मातंगी जय जयति प्रकृति हे। जयति भक्ति उर कुमति सुमति है॥३०॥
कोटिब्रह्म शिव विष्णु कामदा। जयति अहिंसा धर्म जन्मदा॥३१॥
जल थल नभमण्डल में व्यापिनी। सौदामिनि मध्य अलापिनि॥३२॥
झननन तच्छु मरिरिन नादिनि। जय सरस्वती वीणा वादिनी॥३३॥
ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे। कलित कण्ठ शोभित नरमुण्डा॥३४॥
जय ब्रह्माण्ड सिद्धि कवि माता। कामाख्या और काली माता॥३५॥
हिंगलाज विन्ध्याचल वासिनी। अट्टहासिनी अरु अघन नाशिनी॥३६॥
कितनी स्तुति करूँ अखण्डे। तू ब्रह्माण्डे शक्तिजितचण्डे॥३७॥
करहु कृपा सबपे जगदम्बा। रहहिं निशंक तोर अवलम्बा॥३८॥
चतुर्भुजी काली तुम श्यामा। रूप तुम्हार महा अभिरामा॥३९॥
खड्ग और खप्पर कर सोहत। सुर नर मुनि सबको मन मोहत॥४०॥
तुम्हरि कृपा पावे जो कोई। रोग शोक नहिं ताकहँ होई॥४१॥
जो यह पाठ करे चालीसा। तापर कृपा करहि गौरीशा॥४२॥

॥ दोहा ॥
जय कपालिनी जय शिवा, जय जय जय जगदम्ब।
सदा भक्तजन केरि दुःख हरहु, मातु अवलम्ब॥"""

meaning = """॥ श्री महाकाली चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "जय जय सीताराम के, मध्यवासिनी अम्ब। देहु दर्श जगदम्ब, अब करो न मातु विलम्ब॥"
भावार्थ: हे माँ जगदम्बा! आप श्री सीताराम जी के हृदय मध्य में विराजने वाली साक्षात पराशक्ति अम्बिका हैं। हे जननी! अब और विलम्ब न कीजिए और अपने इस दीन सेवक को शीघ्र दिव्य दर्शन दीजिए।

• "जय तारा जय कालिका, जय दश विद्या वृन्द। काली चालीसा रचत, एक सिद्धि कवि हिन्द॥"
भावार्थ: हे भगवती तारा, हे महाकालिका, हे समस्त दश महाविद्याओं के दिव्य वृन्द! आपकी सदा-सदा जय हो। हिन्द देश का यह साधक-कवि भगवती की कृपा-सिद्धि प्राप्त कर इस पावन चालीसा की रचना कर रहा है।

• "प्रातः काल उठ जो पढ़े, दुपहरिया या शाम। दुःख दरिद्रता दूर हों, सिद्धि होय सब काम॥"
भावार्थ: जो भी श्रद्धालु प्रातःकाल, दोपहर अथवा सांध्यकाल में इस चालीसा का नियमपूर्वक पाठ करता है, उसके जीवन से दुख और दरिद्रता सदा के लिए दूर हो जाती है और उसके सभी मनोरथ सिद्ध होते हैं।

【चौपाइयां — पद्यवार भावार्थ】
१-१०. "जय काली कंकाल मालिनी... दुख दरिद्रता मोर हटावहु॥"
भावार्थ: हे माँ काली! आप कंकालों व मुंडों की माला धारण करने वाली कंकाल-मालिनी हैं; हे मंगलमयी महाकपालिनी! आपकी सदा जय हो। आप रक्तबीज जैसे अजेय असुर का संहार करने वाली माता हैं और अपने भक्तजनों को सर्वदा सुख प्रदान करती हैं। आपके श्रीअंगों पर मुंडों की माला सुशोभित है; हे रणोन्मत्त काली, आपकी जय हो। आप देवाधिदेव महादेव शिव (हर) के हृदय-कमल पर विहार करने वाली हैं; हे जगदम्बा! आप अपने सेवकों के सभी दुखों का समूल नाश करने वाली हैं। बीज मन्त्र 'ह्रीं' स्वरूपा काली, 'श्रीं' स्वरूपा महाकाली, 'क्रीं' स्वरूपा कल्याणी और दक्षिण दिशा की स्वामिनी दक्षिणाकाली के रूप में आपको कोटिशः प्रणाम है। हे कलावती, विद्यावती, तारा, त्रिपुर सुन्दरी और महाबुद्धिशाली महामति! आपकी जय हो। हे माता! मुझे श्रेष्ठ सद्बुद्धि दीजिए, मेरे समस्त संकटों का हरण कीजिए और अपने भक्त के सम्मुख प्रत्यक्ष प्रकट हो जाइए। हे ओंकार स्वरूपा! हे हुंकार करने वाली पराशक्ति! हे असीम व अपरंपार महाशक्ति! आपकी सदा जय हो। आप कमल-वासिनी हैं, कलियुग के दंभ व पापों का नाश करने वाली हैं और अपने भक्तों के समस्त भयों का निवारण करने वाली हैं। हे जगदम्बा! अब अधिक विलम्ब न कीजिए और मेरी दरिद्रता व दुखों को तत्काल दूर कर दीजिए।

११-२०. "जयति कराल कालिका माता... तारागण तू ब्योम विताने॥"
भावार्थ: हे प्रलयंकारी कराल कालिका माता! आपकी जय हो; आपका दिव्य स्वरूप प्रलयकाल की अग्नि (कालानल) के समान परम तेजस्वी और देदीप्यमान है। हे शंकरप्रिया, देवराज इन्द्र की ईश्वरी सुरेशी और सनातनी शक्ति! आपकी जय हो; आप करोड़ों सिद्धियों के कवियों की परम पुरातन आराध्या हैं। जटाजूट धारण करने वाली कपर्दिनी और कलिकाल के समस्त संतापों से मुक्त करने वाली हे माँ! नवीन खिले हुए नीलकमल के समान सुंदर नयनों वाली देवी, आपकी जय हो। आप परमानंद की अधिष्ठात्री और आनंद का अक्षय भंडार हैं; हे माता! मुझे निष्पाप, निर्मल आत्मज्ञान प्रदान कीजिए। आप दया और करुणा के अमृत का अथाह सागर हैं; किन्तु धर्म और भक्तों पर अत्याचार करने वाले दुष्टों पर आप अत्यंत कठोर व निर्दयी हो जाती हैं। संसार के समस्त प्राणी आपके अत्यंत प्रिय बालक हैं और यह संपूर्ण ब्रह्मांड आपके ही आधार पर टिका हुआ है। आप महाप्रलय के समय संहारक तांडव नृत्य करती हैं; हे जननी! आप ही इस समस्त चराचर जगत का पालन-पोषण करने वाली हैं। आप ही महोदरी, महेश्वरी और त्रिगुणात्मक महामाया हैं; आप ही हिमालय की पुत्री पार्वती होकर समस्त विश्व पर अपनी ममतामयी छाया रखती हैं। सिंहनाद के समान जब आपकी प्रचंड गर्जना गूंजती है, तो संपूर्ण ब्रह्मांड में केवल आपकी ही ध्वनि व्याप्त होती है, आपके अतिरिक्त कोई अन्य नहीं ठहर सकता। आकाश रूपी विशाल वितान (तम्बू) में जो तारे टिमटिमाते हैं, वे आपके द्वारा धारण किए गए चमचमाते मणियों के समूह के समान प्रकाशित होते हैं।

२१-३३. "श्री धारे सन्तन हितकारिणी... जय सरस्वती वीणा वादिनी॥"
भावार्थ: आप संतों और साधकों का कल्याण करने वाली, हाथों में संहारक अग्नि धारण कर दुष्टों का विदारण करने वाली हैं। आपने धूम्रलोचन के प्राणों का अंत किया और शुंभ-निशुंभ का संहार करने वाली आप श्रेष्ठ नेत्रों वाली देवी हैं। सहस्र भुजाओं वाली, कमल की माला धारण करने वाली हे चामुण्डा! आप श्मशान में निवास करने वाली हैं। आपने अपने खप्पर में असुरों के रक्त को भरकर पापी महिषासुर का वध किया। हे माँ! आप ही अम्बा, अम्बिका, चण्ड और चण्डिका हैं; वास्तव में यह समस्त रूप आपकी ही आदि कालिका शक्ति के विविध प्रकटीकरण हैं। आप अजन्मा हैं, आप ही एकरूपा और बहुरूपा हैं; आपकी लीलाएं अकथनीय और आपकी शक्ति अनुपम है। कोलकाता के दक्षिण द्वार पर (कालीघाट एवं दक्षिणेश्वर तीर्थ में) हे महेश्वरी! आपकी अत्यंत दिव्य और अपार महिमा वाली पावन मूर्ति विराजती है। आप कादम्बरी के आनंद में मग्न रहने वाली श्यामा हैं; काम की अधिष्ठात्री मातंगी देवी के रूप में आपकी जय हो। आप कमल के आसन पर विराजमान होने वाली कमलायनी हैं; हे श्यामा, हे जगन्माता! आपकी जय हो, जय हो। हे मातंगी! आप ही मूल पराप्रकृति हैं; भक्तों के हृदय से कुबुद्धि को हटाकर सद्बुद्धि प्रदान करने वाली आप ही हैं। आप करोड़ों ब्रह्मा, शिव और विष्णु की अभीष्ट इच्छाओं को पूर्ण करने वाली कामदा हैं और अहिंसा रूपी परम धर्म को जन्म देने वाली हैं। आप जल, थल, आकाश और संपूर्ण नभमंडल में व्याप्त हैं तथा आकाश में कौंधने वाली बिजली (सौदामिनी) के मध्य गंभीर आलाप करती हैं। नूपुरों की झननन-झंकार और दिव्य संगीत की ध्वनि करने वाली आप ही ज्ञान की अधिष्ठात्री सरस्वती और वीणावादिनी हैं।

३४-४२. "ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे... तापर कृपा करहि गौरीशा॥"
भावार्थ: महाशक्ति का परम सिद्ध नर्वाण मन्त्र 'ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे' आपका ही स्वरूप है; आपके सुंदर कंठ में नरमुंडों की माला सुशोभित है। संपूर्ण ब्रह्मांड को सिद्धियां प्रदान करने वाली, कवियों की माता, असम में कामाख्या और सर्वत्र महाकाली के रूप में आपकी जय हो। आप हिंगलाज और विंध्याचल पर्वत पर निवास करने वाली, प्रचंड अट्टहास करने वाली और समस्त पापों का नाश करने वाली हैं। हे अखंड स्वरूपिणी माँ! मैं आपकी कितनी स्तुति करूँ; आप संपूर्ण ब्रह्मांड में चण्ड-मुण्ड को जीतने वाली महाशक्ति हैं। हे जगदम्बा! आप समस्त जीवों पर अपनी कृपा कीजिए, ताकि आपका यह अनन्य सेवक आपके पावन आश्रय में सदा निर्भय होकर रहे। हे श्यामा! आप चार भुजाओं वाली (चतुर्भुजा) हैं और आपका यह स्वरूप अत्यंत मनोहारी और आनंददायक है। आपके कर-कमलों में तीक्ष्ण खड्ग (तलवार) और नर-कपाल (खप्पर) शोभायमान है, जो देवता, मनुष्य और मुनियों—सभी के मन को मुग्ध कर लेता है। जिस पर भी आपकी कृपा दृष्टि हो जाती है, उसे जीवन में कभी कोई रोग या शोक नहीं सताता। जो भी श्रद्धालु इस पावन चालीसा का श्रद्धापूर्वक पाठ करता है, उस पर देवाधिदेव भगवान गौरीश (शिवजी) की भी अक्षय कृपा प्राप्त होती है।

【समापन दोहा】
• "जय कपालिनी जय शिवा, जय जय जय जगदम्ब। सदा भक्तजन केरि दुःख हरहु, मातु अवलम्ब॥"
भावार्थ: हे कपालिनी! हे कल्याणकारिणी शिवा! हे जगदम्बा! आपकी सदा-सदा जय हो। हम भक्तजनों का एकमात्र सहारा (अवलंब) आप ही हैं; हे माता! हमारे समस्त दुखों और क्लेशों का सदा के लिए हरण कर लीजिए।"""

vidhi = """॥ श्री महाकाली चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल ब्रह्ममुहूर्त, सांध्यकाल (प्रदोष) अथवा मध्यरात्रि (निशीथ काल — तंत्र-साधना एवं महाकाली पूजन में मध्यरात्रि का विशेष महत्व है)।
- सर्वोत्तम वार: मंगलवार एवं शनिवार (भगवती महाकाली व कालभैरव के परम पावन दिन)।
- महापर्व व पावन तिथियां: नरक चतुर्दशी/दीपावली (कालरात्रि महानिशा), प्रत्येक मास की दर्श/कृष्ण पक्ष की अमावस्या, गुप्त एवं शारदीय नवरात्रि (विशेषकर महाअष्टमी व महानवमी), तथा तारा रात्रि/काली पूजा।

२. दिशा, आसन व वस्त्र:
- दिशा: पूर्व अथवा दक्षिण दिशा की ओर मुख करके बैठें (दक्षिण काली साधना में दक्षिणमुखी होना शास्त्रसम्मत है)।
- आसन: लाल अथवा काले रंग का स्वच्छ ऊनी आसन या कुशासन बिछाएं।
- वस्त्र: साधक को लाल अथवा गहरे रंग के शुद्ध, धुले हुए सूती/ऊनी वस्त्र धारण करने चाहिए।

३. दीपक, पुष्प व नैवेद्य पूजन सामग्री:
- दीपक: सरसों के तेल का अथवा शुद्ध देशी घी का चौमुखा दीपक प्रज्वलित करें।
- प्रिय पुष्प: माँ महाकाली को ताजे लाल गुड़हल (जबा-कुसुम) के पुष्प अथवा १०८ फूलों की माला अर्पित करें।
- तिलक: रक्त चंदन, रोली, कुंकुम और सिन्दूर का तिलक करें।
- प्रिय नैवेद्य: हलवा-पूरी, खीर, अनार, काले अंगूर, बताशे, लौंग का जोड़ा, पान का बीड़ा और नारियल का भोग लगाएं।

४. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन, पवित्रीकरण एवं संकल्प करें।
- माँ महाकाली का ध्यान करें:
  'ॐ शवारूढां महाभीमां घोरदंष्ट्रां हसन्मुखीम्। चतुर्भुजां खड्गमुण्डवराभयधरां पराम्॥
   नीलोत्पलदलश्यामां सुदंष्ट्रां कोटिरविप्रभाम्। त्रिनेत्रां रक्तनयनां मुक्तकेशीं दिगम्बराम्॥'
- महाकाली के नर्वाण मन्त्र 'ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे' अथवा 'ॐ क्रीं कालिकायै नमः' का १०८ बार जप करें।
- इसके पश्चात शांत चित्त होकर 'श्री महाकाली चालीसा' का १, ३, ७ अथवा ११ बार श्रद्धापूर्वक पाठ करें।
- पाठ के उपरांत कर्पूर से आरती करें और अनजाने में हुई भूलों के लिए क्षमा-प्रार्थना करें।"""

significance = """॥ श्री महाकाली चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. अजेय शत्रु-बाधा निवारण व विजय प्राप्ति:
"रक्तबीज बधकारिणि माता... अग्नि पाणि अति दुष्ट विदारिणि॥"
महाकाली चालीसा का पाठ साधक के जीवन से घोर से घोर शत्रुओं, विरोधियों और षड्यंत्रों का समूल नाश कर उसे प्रत्येक क्षेत्र में निर्भय व विजयी बनाता है।

२. तंत्र-मंत्र, नजर दोष व नकारात्मक शक्तियों से पूर्ण मुक्ति:
"चामुण्डे मरघट की वासिनी... अट्टहासिनी अरु अघन नाशिनी॥"
माता महाकाली श्मशान-वासिनी और पराशक्ति हैं; इनके प्रभाव से किसी भी प्रकार का नजर-दोष, ऊपरी बाधा, तांत्रिक अभिचार या नकारात्मक ऊर्जा तत्काल भस्म हो जाती है।

३. अकाल मृत्यु भय व घोर संकट निवारण:
"देहु सुबुद्धि हरहु सब संकट... तुम्हरि कृपा पावे जो कोई। रोग शोक नहिं ताकहँ होई॥"
मृत्यु-भय, असाध्य रोग, और आकस्मिक दुर्घटनाओं से महाकाल की शक्ति माँ कालरात्रि साधक के प्राणों की रक्षा करती हैं।

४. दुःख-दरिद्रता नाश व सर्वकार्य सिद्धि:
"प्रातः काल उठ जो पढ़े, दुपहरिया या शाम। दुःख दरिद्रता दूर हों, सिद्धि होय सब काम॥"
नियमित पाठ से आर्थिक तंगी, कर्ज और दरिद्रता का नाश होता है तथा साधक के अटके हुए समस्त कार्य द्रुत गति से सिद्ध होते हैं।

५. आत्मबल, कुण्डलिनी जागरण व शिव-कृपा प्राप्ति:
"जो यह पाठ करे चालीसा। तापर कृपा करहि गौरीशा॥"
साधक को असीम आत्मबल, ओज, तेज, मानसिक दृढ़ता प्राप्त होती है और भगवान शिव (गौरीश) का परम अनुग्रह प्राप्त होता है।"""

english_lyrics = """॥ Shri Mahakali Chalisa ॥

॥ Doha ॥
Jaya Jaya Seetaaraama Ke, Madhyavaasinee Amba।
Dehu Darsha Jagadamba, Aba Karo Na Maatu Vilamba॥
Jaya Taaraa Jaya Kaalikaa, Jaya Dasha Vidyaa Vrinda।
Kaalee Chaaleesaa Rachata, Eka Siddhi Kavi Hinda॥
Praatah Kaala Utha Jo Padhe, Dupahariyaa Yaa Shaama।
Duhkha Daridrataa Doora Hon, Siddhi Hoya Saba Kaama॥

॥ Chaupai ॥
Jaya Kaalee Kankaala Maalinee। Jaya Mangalaa Mahaa Kapaalinee॥1॥
Raktabeeja Badhakaarini Maataa। Sadaa Bhakta Jananakee Sukhadaataa॥2॥
Shiro Maalikaa Bhooshita Ange। Jaya Kaalee Jaya Madya Matange॥3॥
Hara Hridayaaravinda Suvilaasini। Jaya Jagadambaa Sakala Duhkha Naashini॥4॥
Hreem Kaalee Shree Mahaakaalee। Kreem Kalyaanee Dakshinaakaalee॥5॥
Jaya Kalaavatee Jaya Vidyaavatee। Jaya Taaraa Sundaree Mahaamati॥6॥
Dehu Subuddhi Harahu Saba Sankata। Hohu Bhakta Ke Aage Paragata॥7॥
Jaya Om Kaare Jaya Hunkaare। Mahaa Shakti Jaya Aparamppaare॥8॥
Kamalaa Kaliyuga Darpa Vinaashinee। Sadaa Bhakta Jana Ke Bhayanaashinee॥9॥
Aba Jagadamba Na Dera Lagaavahu। Dukha Daridrataa Mora Hataavahu॥10॥
Jayati Karaala Kaalikaa Maataa। Kaalaanala Samaana Dyutigaataa॥11॥
Jayashankaree Sureshi Sanaatani। Koti Siddhi Kavi Maatu Puraatani॥12॥
Kapardinee Kali Kalpa Bimochani। Jaya Vikasita Nava Nalinavilochani॥13॥
Aananda Karani Aananda Nidhaanaa। Dehumaatu Mohi Nirmala Gyaanaa॥14॥
Karunaamrita Saagara Kripaamayeel। Hohu Dushta Janapara Aba Nirdayee॥15॥
Sakala Jeeva Tohi Parama Piyaaraa। Sakala Vishwa Tore Aadhaaraa॥16॥
Pralaya Kaala Men Nartana Kaarini। Jaya Jananee Saba Jaga Kee Paalani॥17॥
Mahodaree Maheshwaree Maayaa। Himagiri Sutaa Vishwa Kee Chhaayaa॥18॥
Swachhanda Rada Maarada Dhuni Maahee। Garjata Tumhee Aura Kou Naahee॥19॥
Sphurati Maniganaakaara Prataane। Taaraagana Too Byoma Vitaane॥20॥
Shree Dhaare Santana Hitakaarinlee। Agni Paani Ati Dushta Vidaarini॥21॥
Dhoomra Vilochani Praana Vimochani। Shumbha Nishumbha Mathani Varalochani॥22॥
Sahasa Bhujee Saroruha Maalinee। Chaamunde Maraghata Kee Vaasinee॥23॥
Khappara Madhya Sushonita Saajee। Maarehu Maan Mahishaasura Paajee॥24॥
Amba Ambikaa Chanda Chandikaa। Saba Eke Tuma Aadi Kaalikaa॥25॥
Ajaa Ekaroopaa Bahuroopaa। Akatha Charitra Tava Shakti Anoopaa॥26॥
Kalkattaa Ke Dakshina Dvaare। Moorati Tora Maheshi Apaare॥27॥
Kaadambaree Paanarata Shyaamaa। Jaya Maatangee Kaama Ke Dhaamaa॥28॥
Kamalaasana Vaasinee Kamalaayani। Jaya Shyaamaa Jaya Jaya Shyaamaayani॥29॥
Maatangee Jaya Jayati Prakriti He। Jayati Bhakti Ura Kumati Sumati Hai॥30॥
Kotibrahma Shiva Vishnu Kaamadaa। Jayati Ahinsaa Dharma Janmadaa॥31॥
Jala Thala Nabhamandala Men Vyaapinee। Saudaamini Madhya Alaapini॥32॥
Jhananana Tachchhu Maririna Naadini। Jaya Saraswatee Veenaa Vaadinee॥33॥
Om Aim Hreem Kleem Chaamundaayai Vichche। Kalita Kantha Shobhita Naramundaa॥34॥
Jaya Brahmaanda Siddhi Kavi Maataa। Kaamaakhyaa Aura Kaalee Maataa॥35॥
Hingalaaja Vindhyaachala Vaasinee। Attahaasinee Aru Aghana Naashinee॥36॥
Kitanee Stuti Karoon Akhande। Too Brahmaande Shaktijitachande॥37॥
Karahu Kripaa Sabape Jagadambaa। Rahahin Nishanka Tora Avalambaa॥38॥
Chaturbhujee Kaalee Tuma Shyaamaa। Roopa Tumhaara Mahaa Abhiraamaa॥39॥
Khadga Aura Khappara Kara Sohata। Sura Nara Muni Sabako Mana Mohata॥40॥
Tumhari Kripaa Paave Jo Ko-ee। Roga Shoka Nahin Taakahan Ho-ee॥41॥
Jo Yaha Paatha Kare Chaaleesaa। Taapara Kripaa Karahi Gaureeshaa॥42॥

॥ Doha ॥
Jaya Kapaalinee Jaya Shivaa, Jaya Jaya Jaya Jagadamba।
Sadaa Bhaktajana Keri Duhkha Harahu, Maatu Avalamba॥"""

# 1. Update drik_chalisa_34 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

found = False
for item in cols["devi"]["items"]:
    if item["id"] == "drik_chalisa_34":
        item["title"] = "महाकाली माता चालीसा"
        item["title_en"] = "Mahakali Mata Chalisa"
        item["en_line"] = "Jai Kali Kankal Malini"
        item["hi_line"] = "जय काली कंकाल मालिनी"
        item["sub"] = "जय काली कंकाल मालिनी • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_kali_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=xcVv68gwc5Y"
        item["video_id"] = "xcVv68gwc5Y"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/kali-mata/mahakali-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "शत्रुमर्दिनी अकालमृत्युहारिणी भगवती महाकाली माता"
        item["section"] = "दिव्य देवी माता चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        found = True
        break

if not found:
    print("ERROR: drik_chalisa_34 not found in devi category!")
    sys.exit(1)

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_34 in drik_chalisa_collections.json successfully!")

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

# 3. Add or update chalisa_mahakali in CONTENT in app.js
content_obj = {
    "title": "श्री महाकाली माता चालीसा",
    "title_en": "Shri Mahakali Mata Chalisa",
    "en_line": "Jai Kali Kankal Malini",
    "hi_line": "जय काली कंकाल मालिनी",
    "sub": "जय काली कंकाल मालिनी • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_kali_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=xcVv68gwc5Y",
    "video_id": "xcVv68gwc5Y",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/kali-mata/mahakali-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "शत्रुमर्दिनी अकालमृत्युहारिणी भगवती महाकाली माता",
    "section": "दिव्य देवी माता चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

mahakali_content_js = "  chalisa_mahakali: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_mahakali: {" in app_text:
    pos_s = app_text.find("  chalisa_mahakali: {")
    pos_next = app_text.find("\n  chalisa_", pos_s + 1)
    if pos_next == -1:
        pos_next = app_text.find("\n  sundarkand:", pos_s + 1)
    app_text = app_text[:pos_s] + mahakali_content_js + app_text[pos_next+1:]
    print("Replaced existing chalisa_mahakali in CONTENT!")
else:
    # Insert right before chalisa_saraswati (after chalisa_kali)
    pos_saras = app_text.find("  chalisa_saraswati: {")
    if pos_saras != -1:
        app_text = app_text[:pos_saras] + mahakali_content_js + app_text[pos_saras:]
        print("Inserted chalisa_mahakali before chalisa_saraswati in CONTENT!")
    else:
        # fallback: insert before sundarkand
        pos_sun = app_text.find("  sundarkand: {")
        if pos_sun != -1:
            app_text = app_text[:pos_sun] + mahakali_content_js + app_text[pos_sun:]
            print("Inserted chalisa_mahakali before sundarkand in CONTENT!")
        else:
            print("ERROR: Could not find insert location in CONTENT!")

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

print("ALL MAHAKALI UPDATES COMPLETED!")
