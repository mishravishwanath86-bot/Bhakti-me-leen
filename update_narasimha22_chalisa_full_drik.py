import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री नृसिंह चालीसा ॥

॥ दोहा ॥
मास वैशाख कृतिका युत, हरण मही को भार।
शुक्ल चतुर्दशी सोम दिन, लियो नरसिंह अवतार॥
धन्य तुम्हारो सिंह तनु, धन्य तुम्हारो नाम।
तुमरे सुमरन से प्रभु, पूरन हो सब काम॥

॥ चौपाई ॥
नरसिंह देव मैं सुमरों तोहि। धन बल विद्या दान दे मोहि॥१॥
जय जय नरसिंह कृपाला। करो सदा भक्तन प्रतिपाला॥२॥
विष्णु के अवतार दयाला। महाकाल कालन को काला॥३॥
नाम अनेक तुम्हारो बखानो। अल्प बुद्धि मैं ना कछु जानों॥४॥
हिरणाकुश नृप अति अभिमानी। तेहि के भार मही अकुलानी॥५॥
हिरणाकुश कयाधू के जाये। नाम भक्त प्रहलाद कहाये॥६॥
भक्त बना बिष्णु को दासा। पिता कियो मारन परसाया॥७॥
अस्त्र-शस्त्र मारे भुज दण्डा। अग्निदाह कियो प्रचण्डा॥८॥
भक्त हेतु तुम लियो अवतारा। दुष्ट-दलन हरण महिभारा॥९॥
तुम भक्तन के भक्त तुम्हारे। प्रह्लाद के प्राण पियारे॥१०॥
प्रगट भये फाड़कर तुम खम्भा। देख दुष्ट-दल भये अचम्भा॥११॥
खड्ग जिह्व तनु सुन्दर साजा। ऊर्ध्व केश महादष्ट्र विराजा॥१२॥
तप्त स्वर्ण सम बदन तुम्हारा। को वरने तुम्हरों विस्तारा॥१३॥
रूप चतुर्भुज बदन विशाला। नख जिह्वा है अति विकराला॥१४॥
स्वर्ण मुकुट बदन अति भारी। कानन कुण्डल की छवि न्यारी॥१५॥
भक्त प्रहलाद को तुमने उबारा। हिरणा कुश खल क्षण मह मारा॥१६॥
ब्रह्मा, बिष्णु तुम्हे नित ध्यावे। इन्द्र महेश सदा मन लावे॥१७॥
वेद पुराण तुम्हरो यश गावे। शेष शारदा पारन पावे॥१८॥
जो नर धरो तुम्हरो ध्याना। ताको होय सदा कल्याना॥१९॥
त्राहि-त्राहि प्रभु दुःख निवारो। भव बन्धन प्रभु आप ही टारो॥२०॥
नित्य जपे जो नाम तिहारा। दुःख व्याधि हो निस्तारा॥२१॥
सन्तान-हीन जो जाप कराये। मन इच्छित सो नर सुत पावे॥२२॥
बन्ध्या नारी सुसन्तान को पावे। नर दरिद्र धनी होई जावे॥२३॥
जो नरसिंह का जाप करावे। ताहि विपत्ति सपनें नही आवे॥२४॥
जो कामना करे मन माही। सब निश्चय सो सिद्ध हुयी जाही॥२५॥
जीवन मैं जो कछु सङ्कट होयी। निश्चय नरसिंह सुमरे सोयी॥२६॥
रोग ग्रसित जो ध्यावे कोई। ताकि काया कञ्चन होई॥२७॥
डाकिनी-शाकिनी प्रेत बेताला। ग्रह-व्याधि अरु यम विकराला॥२८॥
प्रेत पिशाच सबे भय खाये। यम के दूत निकट नहीं आवे॥२९॥
सुमर नाम व्याधि सब भागे। रोग-शोक कबहूँ नही लागे॥३०॥
जाको नजर दोष हो भाई। सो नरसिंह चालीसा गाई॥३१॥
हटे नजर होवे कल्याना। बचन सत्य साखी भगवाना॥३२॥
जो नर ध्यान तुम्हारो लावे। सो नर मन वाञ्छित फल पावे॥३३॥
बनवाये जो मन्दिर ज्ञानी। हो जावे वह नर जग मानी॥३४॥
नित-प्रति पाठ करे इक बारा। सो नर रहे तुम्हारा प्यारा॥३५॥
नरसिंह चालीसा जो जन गावे। दुःख दरिद्र ताके निकट न आवे॥३६॥
चालीसा जो नर पढ़े-पढ़ावे। सो नर जग में सब कुछ पावे॥३७॥
यह श्री नरसिंह चालीसा। पढ़े रङ्क होवे अवनीसा॥३८॥
जो ध्यावे सो नर सुख पावे। तोही विमुख बहु दुःख उठावे॥३९॥
शिव स्वरूप है शरण तुम्हारी। हरो नाथ सब विपत्ति हमारी॥४०॥

॥ दोहा ॥
चारों युग गायें तेरी, महिमा अपरम्पार।
निज भक्तनु के प्राण हित, लियो जगत अवतार॥
नरसिंह चालीसा जो पढ़े, प्रेम मगन शत बार।
उस घर आनन्द रहे, वैभव बढ़े अपार॥"""

meaning = """॥ श्री नृसिंह चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "मास वैशाख कृतिका युत, हरण मही को भार। शुक्ल चतुर्दशी सोम दिन, लियो नरसिंह अवतार॥"
भावार्थ: वैशाख मास के शुक्ल पक्ष की पावन चतुर्दशी तिथि को, कृतिका नक्षत्र व सोमवार के शुभ योग में, पृथ्वी का असह्य भार हरने हेतु भगवान श्रीहरि ने नृसिंह अवतार धारण किया।
• "धन्य तुम्हारो सिंह तनु, धन्य तुम्हारो नाम। तुमरे सुमरन से प्रभु, पूरन हो सब काम॥"
भावार्थ: हे प्रभु! आपका वह अलौकिक नृसिंह विग्रह (आधा सिंह व आधा मनुष्य) धन्य है, और आपका पावन नाम भी धन्य है। हे दीनानाथ! आपके स्मरण मात्र से भक्तों के समस्त कार्य निर्विघ्न पूर्ण हो जाते हैं।

【४० चौपाइयां — पद्यवार भावार्थ】
१-४. "नरसिंह देव मैं सुमरों तोहि... अल्प बुद्धि मैं ना कछु जानों॥"
भावार्थ: हे देवाधिदेव भगवान नृसिंह! मैं नित्य श्रद्धापूर्वक आपका स्मरण करता हूँ; मुझे धर्म, बल, बुद्धि और विद्या का दान प्रदान कीजिए। हे कृपालु नृसिंह भगवान! आपकी सदा जय हो; आप सदा अपने शरणागत भक्तों का प्रतिपालन व रक्षा करते हैं। आप साक्षात् भगवान श्रीहरि विष्णु के परम दयालु अवतार हैं; आप महाकाल और काल के भी परम काल हैं। आपके सहस्रों दिव्य नाम हैं, मेरी बुद्धि अत्यंत अल्प है, मैं आपकी असीम महिमा का पूर्ण पार नहीं पा सकता।

५-८. "हिरणाकुश नृप अति अभिमानी... अग्निदाह कियो प्रचण्डा॥"
भावार्थ: हिरण्यकश्यप नामक महाअभिमानी और क्रूर दैत्यराज के अत्याचारों व पाप के भार से यह संपूर्ण पृथ्वी व्याकुल और भयभीत हो उठी थी। उसी हिरण्यकश्यप और महारानी कयाधू के गर्भ से परम भगवद्भक्त बालक प्रह्लाद का प्राकट्य हुआ। बालक प्रह्लाद बाल्यकाल से ही भगवान श्रीहरि विष्णु का अनन्य दास बन गया, जिससे कुपित होकर पापी पिता हिरण्यकश्यप ने अपने ही पुत्र को मारने के अनगिनत उपाय रचे। उसने अस्त्र-शस्त्रों से प्रहार किए, पर्वत से फिंकवाया, विष पिलाया और होलिका की प्रचण्ड अग्नि में जलाने का घोर प्रयास किया।

९-१२. "भक्त हेतु तुम लियो अवतारा... ऊर्ध्व केश महादष्ट्र विराजा॥"
भावार्थ: अपने अनन्य भक्त प्रह्लाद की रक्षा करने, दुष्टों का दलन करने और पृथ्वी का भार हरने हेतु हे प्रभु! आपने यह अद्वितीय अवतार धारण किया। आप भक्तों के वशीभूत हैं और भक्त आपके प्राण हैं; आप प्रह्लाद के प्राणों से भी अधिक प्रिय हैं। हिरण्यकश्यप की सभा के पाषाण खंभे को चीरकर आप महागर्जना के साथ प्रकट हुए, जिसे देखकर समस्त असुर दल स्तब्ध और भयभीत हो गया। आपकी खड्ग के समान लपलपाती जिह्वा, दिव्य सुंदर व तेजोमय शरीर, ऊपर उठे हुए अग्निशिखा समान केश और विशाल दाढ़ें अत्यंत भयानक व भव्य प्रतीत हो रही थीं।

१३-१६. "तप्त स्वर्ण सम बदन तुम्हारा... हिरणा कुश खल क्षण मह मारा॥"
भावार्थ: तपे हुए शुद्ध स्वर्ण के समान आपके श्रीविग्रह की कांति चमक रही थी; आपके इस विराट स्वरूप के विस्तार का वर्णन करने में कौन समर्थ हो सकता है? आपका चतुर्भुज रूप और मुखमंडल अत्यंत विशाल था; आपके नख और जिह्वा असुरों के लिए अत्यंत विकराल व संहारक थे। मस्तक पर दिव्य स्वर्ण मुकुट सुशोभित था और दोनों कानों में झिलमिलाते कुंडल अलौकिक शोभा बिखेर रहे थे। आपने भक्त प्रह्लाद को तत्काल संकट से उबार लिया और पापी हिरण्यकश्यप को अपनी जंघाओं पर रखकर अपने तीक्ष्ण वज्र-नखों से क्षण भर में चीरकर उसका अंत कर दिया।

१७-२०. "ब्रह्मा, बिष्णु तुम्हे नित ध्यावे... भव बन्धन प्रभु आप ही टारो॥"
भावार्थ: ब्रह्मा और विष्णु नित्य आपका ध्यान धरते हैं; देवराज इंद्र और देवाधिदेव महादेव शिव भी सदा प्रेमपूर्वक आपका स्मरण करते हैं। चारों वेद और अठारह पुराण निरंतर आपके यश और पराक्रम का गान करते हैं; सहस्रमुख शेषनाग और माता सरस्वती भी आपकी महिमा का पार नहीं पा सकते। जो भी मनुष्य श्रद्धापूर्वक आपका ध्यान धरता है, उसका सदा सर्वथा कल्याण ही कल्याण होता है। हे प्रभु! 'त्राहि-त्राहि' कर मैं आपकी शरण में हूँ, मेरे दुखों का निवारण कीजिए और इस जन्म-मरण के सांसारिक बंधनों से मुझे सदा के लिए मुक्त कर दीजिए।

२१-२६. "नित्य जपे जो नाम तिहारा... निश्चय नरसिंह सुमरे सोयी॥"
भावार्थ: जो मनुष्य नित्य आपके पावन नाम का जप करता है, उसके समस्त दुख, दारिद्र्य और भयानक व्याधियां नष्ट हो जाती हैं। संतानहीन व्यक्ति यदि नृसिंह भगवान का अनुष्ठान व जाप करवाए, तो उसे मनवांछित सुयोग्य संतान की प्राप्ति होती है। बंध्या (निःसंतान) स्त्री को श्रेष्ठ संतान रत्न मिलता है और दरिद्र मनुष्य समस्त ऐश्वर्य पाकर धनवान बन जाता है। जो नृसिंह चालीसा का पाठ व जप करता है, उसे स्वप्न में भी कभी कोई विपत्ति या संकट नहीं सताता। साधक अपने मन में जो भी शुभ कामना करता है, वह निश्चय ही सिद्ध हो जाती है। जीवन में जब भी कोई विषम संकट या आपदा आए, तो निश्चयपूर्वक भगवान नृसिंह का स्मरण करना चाहिए।

२७-३०. "रोग ग्रसित जो ध्यावे कोई... रोग-शोक कबहूँ नही लागे॥"
भावार्थ: जो कोई असाध्य रोगों से ग्रसित होकर भगवान नृसिंह का ध्यान धरता है, उसका शरीर स्वर्ण की भांति पूर्णतः निरोगी और कांतिमय बन जाता है। डाकिनी, शाकिनी, प्रेत, बेताल, अनिष्टकारी ग्रह-दोष और यमराज का विकराल भय भी नृसिंह नाम के प्रभाव से तत्काल नष्ट हो जाता है। भूत, प्रेत और पिशाच भयभीत होकर भाग खड़े होते हैं और यमदूत कभी उस साधक के समीप नहीं फटकते। नृसिंह नाम का स्मरण करते ही समस्त आधि-व्याधियां भाग जाती हैं और उस मनुष्य को कभी कोई रोग व शोक स्पर्श नहीं कर पाता।

३१-३५. "जाको नजर दोष हो भाई... सो नर रहे तुम्हारा प्यारा॥"
भावार्थ: जिस किसी को भी बुरी नजर, तांत्रिक नजर-दोष या नकारात्मक ऊर्जा लगी हो, उसे नृसिंह चालीसा का पाठ करना चाहिए। बुरी नजर तत्काल हट जाती है और उसका कल्याण होता है; स्वयं भगवान इस सत्य वचन के साक्षी हैं। जो मनुष्य एकाग्रचित्त होकर आपका ध्यान लगाता है, वह अपने मनवांछित समस्त फलों को प्राप्त करता है। जो ज्ञानी भक्त भगवान नृसिंह का मंदिर बनवाता है अथवा उनकी सेवा करता है, वह संपूर्ण संसार में पूज्य और प्रतिष्ठित हो जाता है। जो नित्य-प्रतिदिन कम से कम एक बार इस चालीसा का पाठ करता है, वह भगवान नृसिंह का परम प्रिय भक्त बन जाता है।

३६-४०. "नरसिंह चालीसा जो जन गावे... हरो नाथ सब विपत्ति हमारी॥"
भावार्थ: जो मनुष्य नृसिंह चालीसा का सप्रेम गान करता है, दुख और दरिद्रता कभी उसके निकट नहीं आते। जो मनुष्य स्वयं इस चालीसा को पढ़ता है और दूसरों को पढ़ाता/सुनाता है, वह संसार के समस्त सुख, भोग और वैभव प्राप्त करता है। इस श्री नृसिंह चालीसा का नियमित पाठ करने से निर्धन रंक भी राजाओं का स्वामी (सम्राट/धनी) बन जाता है। जो भगवान नृसिंह का ध्यान करता है, वह परम सुख पाता है; और जो उनसे विमुख रहता है, वह सांसारिक कष्ट भोगता है। हे शिव स्वरूप, कल्याणकारी नृसिंह देव! मैं आपकी ही शरण में हूँ, कृपा करके हमारी समस्त विपत्तियों और कष्टों को हर लीजिए।

【समापन दोहे】
• "चारों युग गायें तेरी, महिमा अपरम्पार। निज भक्तनु के प्राण हित, लियो जगत अवतार॥"
भावार्थ: चारों युगों (सत्य, त्रेता, द्वापर, कलि) में आपकी पावन महिमा अपरंपार गाई जाती है। केवल अपने अनन्य भक्तों के प्राणों की रक्षा करने हेतु आपने इस चराचर जगत में पावन अवतार धारण किया।
• "नरसिंह चालीसा जो पढ़े, प्रेम मगन शत बार। उस घर आनन्द रहे, वैभव बढ़े अपार॥"
भावार्थ: जो भी साधक प्रेम में मग्न होकर श्रद्धापूर्वक इस नृसिंह चालीसा का सौ (१००) बार पाठ करता है, उसके घर में सदा परमानंद का वास रहता है और उसका वैभव व ऐश्वर्य दिन-दूना रात-चौगुना बढ़ता है।"""

vidhi = """॥ श्री नृसिंह चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: सांध्यकाल गोधूलि वेला (प्रदोष काल), क्योंकि भगवान नृसिंह का प्राकट्य सूर्यास्त के समय दिन और रात के संधिकाल में हुआ था।
- सर्वोत्तम वार: प्रत्येक मंगलवार (शत्रु, भय व संकट नाश हेतु), गुरुवार (विष्णु स्वरूप उपासना), तथा शनिवार (शनि, राहु-केतु ग्रह दोष शांति हेतु)।
- महापर्व व पावन तिथियां: श्री नृसिंह जयंती (वैशाख मास के शुक्ल पक्ष की चतुर्दशी), प्रत्येक मास की शुक्ल चतुर्दशी, प्रदोष व्रत, तथा स्वाति नक्षत्र युक्त दिन।

२. दिशा, आसन व वस्त्र:
- दिशा: उत्तर अथवा पूर्व दिशा की ओर मुख करके बैठें।
- आसन: लाल अथवा पीले रंग का स्वच्छ ऊनी आसन बिछाएं।
- वस्त्र: साधक को लाल अथवा पीले रंग के स्वच्छ वस्त्र धारण करने चाहिए।

३. पूजन सामग्री व प्रिय नैवेद्य:
- दीपक: गाय के शुद्ध देशी घी का अथवा तिल के तेल का दीपक प्रज्वलित करें।
- पुष्प व तिलक: लाल पुष्प (लाल गुलाब, गुड़हल, कनेर), तुलसी पत्र, तथा रक्त चंदन या अष्टगंध-केसर का तिलक लगाएं।
- प्रिय नैवेद्य: गुड़-चना, पंचामृत, मखाने की खीर, नारियल, ऋतुफल, तथा शीतल जल।

४. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन व पवित्रीकरण करें।
- भगवान श्री नृसिंह एवं परम भक्त बालक प्रह्लाद का ध्यान करें।
- नृसिंह बीज मन्त्र: 'ॐ क्ष्रौं नृसिंहाय नमः' अथवा महामन्त्र: 'ॐ उग्रं वीरं महाविष्णुं ज्वलन्तं सर्वतोमुखम्। नृसिंहं भीषणं भद्रं मृत्योर्मृत्युं नमाम्यहम्॥' का कम से कम १ माला (१०८ बार) जप अवश्य करें।
- इसके पश्चात शांत व एकाग्र चित्त से 'श्री नृसिंह चालीसा' का १, ३, ७ अथवा ११ बार श्रद्धापूर्वक पाठ करें।
- पाठ समाप्ति पर भगवान नृसिंह की पावन आरती गाएं और सभी में प्रसाद वितरण करें।"""

significance = """॥ श्री नृसिंह चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. समस्त भय, शत्रु बाधा व भीषण संकटों का तत्काल नाश:
"भक्त हेतु तुम लियो अवतारा। दुष्ट-दलन हरण महिभारा॥"
भगवान नृसिंह का स्वरूप दुष्टों, असुरों और शत्रुओं के लिए साक्षात् काल है। चालीसा के पाठ से अज्ञात भय, शत्रु भय, कोर्ट-कचहरी के विवाद और आकस्मिक संकट तत्काल दूर हो जाते हैं।

२. तंत्र-मंत्र, भूत-प्रेत व नजर दोष से अभेद्य सुरक्षा कवच:
"डाकिनी-शाकिनी प्रेत बेताला। ग्रह-व्याधि अरु यम विकराला॥ प्रेत पिशाच सबे भय खाये। यम के दूत निकट नहीं आवे॥"
किसी भी प्रकार की तांत्रिक क्रिया, बुरी नजर, प्रेत बाधा या नकारात्मक ऊर्जा भगवान नृसिंह के प्रचंड तेज से क्षण भर में भस्म हो जाती है।

३. असाध्य रोगों से मुक्ति (काया कंचन):
"रोग ग्रसित जो ध्यावे कोई। ताकि काया कञ्चन होई॥ सुमर नाम व्याधि सब भागे। रोग-शोक कबहूँ नही लागे॥"
शारीरिक व्याधियां, असाध्य रोग, रक्त विकार और मानसिक अवसाद नष्ट होकर साधक का शरीर निरोगी व कांतिमय बन जाता है।

४. संतान प्राप्ति व दारिद्र्य का समूल नाश:
"सन्तान-हीन जो जाप कराये। मन इच्छित सो नर सुत पावे॥ बन्ध्या नारी सुसन्तान को पावे। नर दरिद्र धनी होई जावे॥"
निःसंतान दंपत्तियों को सुयोग्य संतान की प्राप्ति होती है और गंभीर आर्थिक संकटों से जूझ रहे साधक को विपुल धन-धान्य और ऐश्वर्य सुलभ होता है।

५. चारों युगों में अमर कीर्ति व वैभव वृद्धि:
"नरसिंह चालीसा जो पढ़े, प्रेम मगन शत बार। उस घर आनन्द रहे, वैभव बढ़े अपार॥"
सच्चे हृदय से नित्य पाठ करने वाले के घर में सुख-शांति, रिद्धि-सिद्धि और अखंड वैभव का वास रहता है।"""

english_lyrics = """॥ Shri Narasimha Chalisa ॥

॥ Doha ॥
Maasa Vaishaakha Kritikaa Yuta, Harana Mahee Ko Bhaara।
Shukla Chaturdashee Soma Dina, Liyo Narasinha Avataara॥
Dhanya Tumhaaro Sinha Tanu, Dhanya Tumhaaro Naama।
Tumare Sumarana Se Prabhu, Poorana Ho Saba Kaama॥

॥ Chaupai ॥
Narasinha Deva Main Sumaron Tohi। Dhana Bala Vidyaa Daana De Mohi॥1॥
Jaya Jaya Narasinha Kripaalaa। Karo Sadaa Bhaktana Pratipaalaa॥2॥
Vishnu Ke Avataara Dayaalaa। Mahaakaala Kaalana Ko Kaalaa॥3॥
Naama Aneka Tumhaaro Bakhaano। Alpa Buddhi Main Naa Kachhu Jaanon॥4॥
Hiranaakusha Nripa Ati Abhimaanee। Tehi Ke Bhaara Mahee Akulaanee॥5॥
Hiranaakusha Kayaadhoo Ke Jaaye। Naama Bhakta Prahlaada Kahaaye॥6॥
Bhakta Banaa Bishnu Ko Daasaa। Pitaa Kiyo Maarana Parasaayaa॥7॥
Astra-Shastra Maare Bhuja Dandaa। Agnidaaha Kiyo Prachandaa॥8॥
Bhakta Hetu Tuma Liyo Avataaraa। Dushta-Dalana Harana Mahibhaaraa॥9॥
Tuma Bhaktana Ke Bhakta Tumhaare। Prahlaada Ke Praana Piyaare॥10॥
Pragata Bhaye Phaarakara Tuma Khambhaa। Dekha Dushta-Dala Bhaye Achambhaa॥11॥
Khadga Jihva Tanu Sundara Saajaa। Oordhva Kesha Mahaadashtra Viraajaa॥12॥
Tapta Svarna Sama Badana Tumhaaraa। Ko Varane Tumharon Vistaaraa॥13॥
Roopa Chaturbhuja Badana Vishaalaa। Nakha Jihvaa Hai Ati Vikaraalaa॥14॥
Svarna Mukuta Badana Ati Bhaaree। Kaanana Kundala Kee Chhavi Nyaaree॥15॥
Bhakta Prahlaada Ko Tumane Ubaaraa। Hiranaa Kusha Khala Kshana Maha Maaraa॥16॥
Brahmaa, Bishnu Tumhe Nita Dhyaave। Indra Mahesha Sadaa Mana Laave॥17॥
Veda Puraana Tumharo Yasha Gaave। Shesha Shaaradaa Paarana Paave॥18॥
Jo Nara Dharo Tumharo Dhyaanaa। Taako Hoya Sadaa Kalyaanaa॥19॥
Traahi-Traahi Prabhu Duhkha Nivaaro। Bhava Bandhana Prabhu Aapa Hee Taaro॥20॥
Nitya Jape Jo Naama Tihaaraa। Duhkha Vyaadhi Ho Nistaaraa॥21॥
Santaana-Heena Jo Jaapa Karaaye। Mana Ichhita So Nara Suta Paave॥22॥
Bandhyaa Naaree Susantaana Ko Paave। Nara Daridra Dhanee Ho-ee Jaave॥23॥
Jo Narasinha Kaa Jaapa Karaave। Taahi Vipatti Sapanen Nahee Aave॥24॥
Jo Kaamanaa Kare Mana Maahee। Saba Nishchaya So Siddha Huyee Jaahee॥25॥
Jeevana Main Jo Kachhu Sankata Ho-ee। Nishchaya Narasinha Sumare So-ee॥26॥
Roga Grasita Jo Dhyaave Ko-ee। Taaki Kaayaa Kanchana Ho-ee॥27॥
Daakinee-Shaakinee Preta Betaalaa। Graha-Vyaadhi Aru Yama Vikaraalaa॥28॥
Preta Pishaacha Sabe Bhaya Khaaye। Yama Ke Doota Nikata Naheen Aave॥29॥
Sumara Naama Vyaadhi Saba Bhaage। Roga-Shoka Kabahoon Nahee Laage॥30॥
Jaako Najara Dosha Ho Bhaa-ee। So Narasinha Chaaleesaa Gaa-ee॥31॥
Hate Najara Hove Kalyaanaa। Bachana Satya Saakhee Bhagavaanaa॥32॥
Jo Nara Dhyaana Tumhaaro Laave। So Nara Mana VaanChhita Phala Paave॥33॥
Banavaaye Jo Mandira Gyaanee। Ho Jaave Vaha Nara Jaga Maanee॥34॥
Nita-Prati Paatha Kare Ika Baaraa। So Nara Rahe Tumhaaraa Pyaaraa॥35॥
Narasinha Chaaleesaa Jo Jana Gaave। Duhkha Daridra Taake Nikata Na Aave॥36॥
Chaaleesaa Jo Nara Padhe-Padhaave। So Nara Jaga Men Saba Kuchha Paave॥37॥
Yaha Shree Narasinha Chaaleesaa। Padhe Ranka Hove Avaneesaa॥38॥
Jo Dhyaave So Nara Sukha Paave। Tohee Vimukha Bahu Duhkha Uthaave॥39॥
Shiva Svaroopa Hai Sharana Tumhaaree। Haro Naatha Saba Vipatti Hamaaree॥40॥

॥ Doha ॥
Chaaron Yuga Gaayen Teree, Mahimaa Aparampara।
Nija Bhaktanu Ke Praana Hita, Liyo Jagata Avataara॥
Narasinha Chaaleesaa Jo Padhe, Prema Magana Shata Baara।
Usa Ghara Aananda Rahe, Vaibhava Badhe Apaara॥"""

# 1. Update drik_chalisa_22 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["vishnu"]["items"]:
    if item["id"] == "drik_chalisa_22":
        item["title"] = "श्री नृसिंह चालीसा"
        item["title_en"] = "Shri Narasimha Chalisa"
        item["en_line"] = "Narasimha Deva Main Sumarom Tohi"
        item["hi_line"] = "नरसिंह देव मैं सुमरों तोहि"
        item["sub"] = "नरसिंह देव मैं सुमरों तोहि • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_narasimha_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=S0T0-mX4yHw"
        item["video_id"] = "S0T0-mX4yHw"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/lord-narasimha/narasimha-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "भक्तवत्सल उग्रवीर भगवान श्री नृसिंह"
        item["section"] = "श्री विष्णु, ब्रह्मा व नृसिंह चालीसा"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_22 in drik_chalisa_collections.json successfully!")

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

# 3. Update chalisa_narasimha in CONTENT in app.js
content_obj = {
    "title": "श्री नृसिंह चालीसा",
    "title_en": "Shri Narasimha Chalisa",
    "en_line": "Narasimha Deva Main Sumarom Tohi",
    "hi_line": "नरसिंह देव मैं सुमरों तोहि",
    "sub": "नरसिंह देव मैं सुमरों तोहि • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_narasimha_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=S0T0-mX4yHw",
    "video_id": "S0T0-mX4yHw",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/lord-narasimha/narasimha-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "भक्तवत्सल उग्रवीर भगवान श्री नृसिंह",
    "section": "श्री विष्णु, ब्रह्मा व नृसिंह चालीसा",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

narasimha_content_js = "  chalisa_narasimha: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

pos_n = app_text.find("  chalisa_narasimha: {")
if pos_n != -1:
    pos_next = app_text.find("  chalisa_khatushyam: {", pos_n)
    if pos_next != -1:
        app_text = app_text[:pos_n] + narasimha_content_js + app_text[pos_next:]
        print("Replaced chalisa_narasimha in CONTENT!")
    else:
        print("ERROR: Could not find chalisa_khatushyam after chalisa_narasimha!")
else:
    print("ERROR: Could not find chalisa_narasimha in app.js!")

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
