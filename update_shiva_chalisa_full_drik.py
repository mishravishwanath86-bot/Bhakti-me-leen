import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Authentic Devanagari Lyrics from Drik Panchang
shiva_chalisa_content = """॥ भगवान शिव चालीसा ॥
(रचनाकार: अयोध्यादास जी • भाषा: अवधी)

॥ दोहा ॥
जय गणेश गिरिजा सुवन, मंगल मूल सुजान।
कहत अयोध्यादास तुम, देहु अभय वरदान॥

॥ चौपाई ॥
जय गिरिजा पति दीन दयाला। सदा करत सन्तन प्रतिपाला॥
भाल चन्द्रमा सोहत नीके। कानन कुण्डल नागफनी के॥

अंग गौर शिर गंग बहाये। मुण्डमाल तन क्षार लगाए॥
वस्त्र खाल बाघम्बर सोहे। छवि को देखि नाग मन मोहे॥

मैना मातु की हवे दुलारी। बाम अंग सोहत छवि न्यारी॥
कर त्रिशूल सोहत छवि भारी। करत सदा शत्रुन क्षयकारी॥

नन्दि गणेश सोहै तहँ कैसे। सागर मध्य कमल हैं जैसे॥
कार्तिक श्याम और गणराऊ। या छवि को कहि जात न काऊ॥

देवन जबहीं जाय पुकारा। तब ही दुख प्रभु आप निवारा॥
किया उपद्रव तारक भारी। देवन सब मिलि तुमहिं जुहारी॥

तुरत षडानन आप पठायउ। लवनिमेष महँ मारि गिरायउ॥
आप जलंधर असुर संहारा। सुयश तुम्हार विदित संसारा॥

त्रिपुरासुर सन युद्ध मचाई। सबहिं कृपा कर लीन बचाई॥
किया तपहिं भागीरथ भारी। पुरब प्रतिज्ञा तासु पुरारी॥

दानिन महँ तुम सम कोउ नाहीं। सेवक स्तुति करत सदाहीं॥
वेद माहि महिमा तुम गाई। अकथ अनादि भेद नहिं पाई॥

प्रकटी उदधि मंथन में ज्वाला। जरत सुरासुर भए विहाला॥
कीन्ही दया तहं करी सहाई। नीलकण्ठ तब नाम कहाई॥

पूजन रामचन्द्र जब कीन्हा। जीत के लंक विभीषण दीन्हा॥
सहस कमल में हो रहे धारी। कीन्ह परीक्षा तबहिं पुरारी॥

एक कमल प्रभु राखेउ जोई। कमल नयन पूजन चहं सोई॥
कठिन भक्ति देखी प्रभु शंकर। भए प्रसन्न दिए इच्छित वर॥

जय जय जय अनन्त अविनाशी। करत कृपा सब के घटवासी॥
दुष्ट सकल नित मोहि सतावै। भ्रमत रहौं मोहि चैन न आवै॥

त्राहि त्राहि मैं नाथ पुकारो। येहि अवसर मोहि आन उबारो॥
लै त्रिशूल शत्रुन को मारो। संकट ते मोहि आन उबारो॥

मात-पिता भ्राता सब होई। संकट में पूछत नहिं कोई॥
स्वामी एक है आस तुम्हारी। आय हरहु मम संकट भारी॥

धन निर्धन को देत सदा हीं। जो कोई जांचे सो फल पाहीं॥
अस्तुति केहि विधि करैं तुम्हारी। क्षमहु नाथ अब चूक हमारी॥

शंकर हो संकट के नाशन। मंगल कारण विघ्न विनाशन॥
योगी यति मुनि ध्यान लगावैं। शारद नारद शीश नवावैं॥

नमो नमो जय नमः शिवाय। सुर ब्रह्मादिक पार न पाय॥
जो यह पाठ करे मन लाई। ता पर होत है शम्भु सहाई॥

ॠनियां जो कोई हो अधिकारी। पाठ करे सो पावन हारी॥
पुत्र होन कर इच्छा जोई। निश्चय शिव प्रसाद तेहि होई॥

पण्डित त्रयोदशी को लावे। ध्यान पूर्वक होम करावे॥
त्रयोदशी व्रत करै हमेशा। ताके तन नहीं रहै कलेशा॥

धूप दीप नैवेद्य चढ़ावे। शंकर सम्मुख पाठ सुनावे॥
जन्म जन्म के पाप नसावे। अन्त धाम शिवपुर में पावे॥

कहैं अयोध्यादास आस तुम्हारी। जानि सकल दुःख हरहु हमारी॥

॥ दोहा ॥
नित्त नेम उठि प्रातः ही, पाठ करो चालीसा।
तुम मेरी मनोकामना, पूर्ण करो जगदीश॥

मगसिर छठि हेमन्त ॠतु, संवत चौसठ जान।
स्तुति चालीसा शिवहि, पूर्ण कीन कल्याण॥"""

# 2. Verse-by-verse Spiritual Meaning (पद्यवार पावन भावार्थ)
shiva_chalisa_meaning = """॥ भगवान शिव चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【आरम्भिक दोहा】
जय गणेश गिरिजा सुवन, मंगल मूल सुजान।
कहत अयोध्यादास तुम, देहु अभय वरदान॥
भावार्थ: माता पार्वती (गिरिजा) के लाडले पुत्र और समस्त मंगलों के आदि मूल, परम ज्ञानी भगवान श्री गणेश जी की जय हो। कवि अयोध्यादास जी प्रार्थना करते हैं कि हे प्रभु! आप मुझे निर्भयता और कल्याण का वरदान प्रदान करें।

【चौपाइयां — भावार्थ】
१. जय गिरिजा पति दीन दयाला। सदा करत सन्तन प्रतिपाला॥
भाल चन्द्रमा सोहत नीके। कानन कुण्डल नागफनी के॥
भावार्थ: हे माता पार्वती के पति, दीनों पर अहैतुकी दया करने वाले और संतों के प्रतिपालक भगवान शिव! आपकी सदा जय हो। आपके सुंदर मस्तक (भाल) पर द्वितीया का चन्द्रमा शोभायमान है और आपके कानों में सर्पों (नागफनी) के कुंडल अत्यंत मनोहारी लग रहे हैं।

२. अंग गौर शिर गंग बहाये। मुण्डमाल तन क्षार लगाए॥
वस्त्र खाल बाघम्बर सोहे। छवि को देखि नाग मन मोहे॥
भावार्थ: आपका शारीरिक वर्ण कर्पूर के समान गौर है, आपकी दिव्य जटाओं से पावन गंगा जी प्रवाहित हो रही हैं। आपके गले में मुंडमाला और समस्त शरीर पर पवित्र भस्म (क्षार) रमी हुई है। आपने बाघ की खाल (बाघम्बर) का वस्त्र धारण किया हुआ है; आपकी इस अलौकिक छवि को देखकर नाग भी मोहित हो जाते हैं।

३. मैना मातु की हवे दुलारी। बाम अंग सोहत छवि न्यारी॥
कर त्रिशूल सोहत छवि भारी। करत सदा शत्रुन क्षयकारी॥
भावार्थ: माता मैनावती की दुलारी पुत्री जगन्माता पार्वती जी आपके वाम (बाएं) अंग में अनुपम छवि के साथ विराजित हैं। आपके हाथ में प्रचंड त्रिशूल सुशोभित है, जो भक्तों की रक्षा हेतु सदा अधर्मी शत्रुओं और आसुरी शक्तियों का नाश करता है।

४. नन्दि गणेश सोहै तहँ कैसे। सागर मध्य कमल हैं जैसे॥
कार्तिक श्याम और गणराऊ। या छवि को कहि जात न काऊ॥
भावार्थ: आपके समीप नंदीश्वर और बाल गणेश जी ऐसे शोभा पा रहे हैं, मानो क्षीरसागर के मध्य खिले हुए दिव्य कमल हों। कार्तिकेय जी, श्याम वर्ण सेवक और समस्त शिवगणों से घिरे आपके इस दिव्य परिवार की छवि का वर्णन कोई भी नहीं कर सकता।

५. देवन जबहीं जाय पुकारा। तब ही दुख प्रभु आप निवारा॥
किया उपद्रव तारक भारी। देवन सब मिलि तुमहिं जुहारी॥
भावार्थ: जब-जब देवताओं पर कोई संकट आया और उन्होंने आपकी शरण में आकर पुकार लगाई, तब-तब हे प्रभु! आपने उनके समस्त दुःखों का तत्काल निवारण किया। जब तारकासुर दैत्य ने तीनों लोकों में भारी उत्पात मचाया, तब समस्त देवताओं ने मिलकर आपकी ही वंदना की।

६. तुरत षडानन आप पठायउ। लवनिमेष महँ मारि गिरायउ॥
आप जलंधर असुर संहारा। सुयश तुम्हार विदित संसारा॥
भावार्थ: देवताओं की रक्षा हेतु आपने तुरंत अपने प्रतापी पुत्र षडानन (कार्तिकेय जी) को भेजा, जिन्होंने पलक झपकते ही (लवनिमेष में) उस महाबली तारकासुर का वध कर दिया। आपने ही उपद्रवी जलंधर असुर का संहार किया; आपका यह पावन सुयश समस्त संसार में प्रसिद्ध है।

७. त्रिपुरासुर सन युद्ध मचाई। सबहिं कृपा कर लीन बचाई॥
किया तपहिं भागीरथ भारी। पुरब प्रतिज्ञा तासु पुरारी॥
भावार्थ: जब त्रिपुरासुर ने देवताओं को त्रस्त किया, तब आपने उसके तीनों नगरों को एक ही बाण से भस्म कर देवताओं की रक्षा की। जब राजा भगीरथ ने गंगा अवतरण हेतु घोर तपस्या की, तब हे त्रिपुरारी! आपने गंगा जी को अपनी जटाओं में धारण कर उनकी प्रतिज्ञा पूर्ण की।

८. दानिन महँ तुम सम कोउ नाहीं। सेवक स्तुति करत सदाहीं॥
वेद माहि महिमा तुम गाई। अकथ अनादि भेद नहिं पाई॥
भावार्थ: संसार के समस्त दानियों में आपके समान कोई दूसरा दानी नहीं है, जो प्रसन्न होने पर अपना सर्वस्व (यहाँ तक कि स्वयं को भी) दे देता है। समस्त सेवक सदा आपकी स्तुति करते हैं। चारों वेदों ने भी आपकी महिमा का गान किया है, किंतु आपकी अनादि और अकथ लीला का भेद कोई नहीं पा सका।

९. प्रकटी उदधि मंथन में ज्वाला। जरत सुरासुर भए विहाला॥
कीन्ही दया तहं करी सहाई। नीलकण्ठ तब नाम कहाई॥
भावार्थ: जब समुद्र मंथन के समय अत्यंत भीषण हलाहल विष की ज्वाला प्रकटी और उससे देवता तथा दानव जलने लगे व व्याकुल हो गए; तब आपने दया करके उस महाविष का पान कर अपने कंठ में धारण कर लिया। तभी से संसार में आपका नाम 'नीलकंठ' प्रसिद्ध हुआ।

१०. पूजन रामचन्द्र जब कीन्हा। जीत के लंक विभीषण दीन्हा॥
सहस कमल में हो रहे धारी। कीन्ह परीक्षा तबहिं पुरारी॥
भावार्थ: जब मर्यादा पुरुषोत्तम भगवान श्री रामचंद्र जी ने लंका पर चढ़ाई से पूर्व रामेश्वरम में आपका विधिवत पूजन किया, तब आपने विजय का आशीर्वाद दिया जिसके फलस्वरूप श्री राम ने लंका जीतकर विभीषण को सौंपी। जब श्री राम एक सहस्र (हजार) नीलकमलों से आपकी पूजा कर रहे थे, तब आपने उनकी परीक्षा लेने हेतु एक कमल छिपा लिया।

११. एक कमल प्रभु राखेउ जोई। कमल नयन पूजन चहं सोई॥
कठिन भक्ति देखी प्रभु शंकर। भए प्रसन्न दिए इच्छित वर॥
भावार्थ: जब एक कमल कम पड़ा, तब भगवान श्री राम ने अपने 'कमलनयन' (नेत्र) को ही कमल के स्थान पर अर्पित करने के लिए बाण उठा लिया। अपने भक्त की ऐसी अनन्य और कठिन भक्ति देखकर देवाधिदेव महादेव अत्यंत प्रसन्न हुए और साक्षात् प्रकट होकर उन्हें अभीष्ट विजय का वरदान दिया।

१२. जय जय जय अनन्त अविनाशी। करत कृपा सब के घटवासी॥
दुष्ट सकल नित मोहि सतावै। भ्रमत रहौं मोहि चैन न आवै॥
भावार्थ: हे आदि-अंत रहित, अविनाशी और समस्त जीवों के हृदय (घट) में निवास करने वाले भगवान शिव! आपकी जय हो, जय हो, जय हो। काम, क्रोध, मद, मोह आदि आंतरिक विकार और बाहरी दुष्ट मुझे निरंतर सताते हैं; मैं संसार में भटक रहा हूँ और मुझे कहीं शांति नहीं मिलती।

१३. त्राहि त्राहि मैं नाथ पुकारो। येहि अवसर मोहि आन उबारो॥
लै त्रिशूल शत्रुन को मारो। संकट ते मोहि आन उबारो॥
भावार्थ: हे नाथ! मैं 'त्राहि-त्राहि' (रक्षा करो-रक्षा करो) कहकर आपकी शरण में पुकार रहा हूँ; इस कठिन समय में तुरंत आकर मेरा उद्धार कीजिए। अपना दिव्य त्रिशूल उठाकर मेरे आंतरिक व बाह्य शत्रुओं का संहार कीजिए और मुझे इस घोर संकट से उबार लीजिए।

१४. मात-पिता भ्राता सब होई। संकट में पूछत नहिं कोई॥
स्वामी एक है आस तुम्हारी। आय हरहु मम संकट भारी॥
भावार्थ: इस संसार में माता, पिता, भाई-बंधु सब कहलाते हैं, किंतु जब घोर विपत्ति आती है तो कोई साथ नहीं देता और न ही सुधि लेता है। हे मेरे स्वामी! मुझे केवल और केवल आपकी ही एक आशा है; आप पधारकर मेरे इस भारी संकट को हर लीजिए।

१५. धन निर्धन को देत सदा हीं। जो कोई जांचे सो फल पाहीं॥
अस्तुति केहि विधि करैं तुम्हारी। क्षमहु नाथ अब चूक हमारी॥
भावार्थ: आप औढरदानी हैं, आप निर्धन को अक्षय धन और ऐश्वर्य प्रदान करते हैं। जो भक्त जैसी याचना लेकर आपके सम्मुख आता है, वह वैसा ही मनोवांछित फल पाता है। मैं अज्ञानी आपकी स्तुति किस विधि करूँ! हे नाथ! मेरी समस्त भूलों और अपराधों को क्षमा कर दीजिए।

१६. शंकर हो संकट के नाशन। मंगल कारण विघ्न विनाशन॥
योगी यति मुनि ध्यान लगावैं। शारद नारद शीश नवावैं॥
भावार्थ: हे भगवान शंकर! आप भक्तों के सभी संकटों का नाश करने वाले, सर्व मंगल के कारण और विघ्नों के विनाशक हैं। श्रेष्ठ योगी, यति और मुनिजन निरंतर आपके ध्यान में मग्न रहते हैं तथा विद्या की देवी सरस्वती (शारदा) और देवर्षि नारद जी आपके चरणों में शीश झुकाते हैं।

१७. नमो नमो जय नमः शिवाय। सुर ब्रह्मादिक पार न पाय॥
जो यह पाठ करे मन लाई। ता पर होत है शम्भु सहाई॥
भावार्थ: 'ॐ नमः शिवाय' के परम पावन पंचाक्षर महामंत्र को बारंबार नमन है, जिसकी अगाध महिमा का पार ब्रह्मा आदि प्रमुख देवता भी नहीं पा सकते। जो भी साधक एकाग्रचित्त होकर पूर्ण श्रद्धा से इस शिव चालीसा का पाठ करता है, देवाधिदेव भगवान शिव साक्षात् उसके सहायक और रक्षक बन जाते हैं।

१८. ॠनियां जो कोई हो अधिकारी। पाठ करे सो पावन हारी॥
पुत्र होन कर इच्छा जोई। निश्चय शिव प्रसाद तेहि होई॥
भावार्थ: जो व्यक्ति भारी कर्ज (ऋण) अथवा दरिद्रता से पीड़ित हो, वह यदि इस पावन चालीसा का पाठ करे तो वह शीघ्र ही ऋणमुक्त होकर पवित्र व समृद्ध हो जाता है। जिस दंपत्ति को संतान प्राप्ति की अभिलाषा हो, उसे भगवान शिव के पावन प्रसाद से अवश्य ही सुयोग्य संतान की प्राप्ति होती है।

१९. पण्डित त्रयोदशी को लावे। ध्यान पूर्वक होम करावे॥
त्रयोदशी व्रत करै हमेशा। ताके तन नहीं रहै कलेशा॥
भावार्थ: त्रयोदशी (प्रदोष काल) के दिन योग्य ब्राह्मण को आमंत्रित कर जो विधिपूर्वक भगवान शिव के निमित्त आहुति और हवन कराता है; तथा जो नियमपूर्वक प्रदोष (त्रयोदशी) का व्रत रखता है, उसके तन और मन में कभी किसी प्रकार का रोग, संताप या क्लेश शेष नहीं रहता।

२०. धूप दीप नैवेद्य चढ़ावे। शंकर सम्मुख पाठ सुनावे॥
जन्म जन्म के पाप नसावे। अन्त धाम शिवपुर में पावे॥
कहैं अयोध्यादास आस तुम्हारी। जानि सकल दुःख हरहु हमारी॥
भावार्थ: जो भक्त शिवलिंग के सम्मुख शुद्ध धूप, दीप और नैवेद्य अर्पित करके श्रद्धापूर्वक इस चालीसा का पाठ करता है, उसके जन्म-जन्मांतर के संचित पाप कट जाते हैं और देहावसान के बाद वह परम पावन 'शिवपुर' (कैलाश धाम) को प्राप्त होता है। कवि अयोध्यादास जी कहते हैं कि हे भोलेनाथ! मुझे केवल आपकी ही आस है, आप मेरे समस्त दुःखों को हर लीजिए।

【समापन दोहे】
नित्त नेम उठि प्रातः ही, पाठ करो चालीसा।
तुम मेरी मनोकामना, पूर्ण करो जगदीश॥
मगसिर छठि हेमन्त ॠतु, संवत चौसठ जान।
स्तुति चालीसा शिवहि, पूर्ण कीन कल्याण॥
भावार्थ: जो मनुष्य नित्य प्रातःकाल उठकर नियमपूर्वक इस शिव चालीसा का पाठ करता है, हे जगदीश्वर शिव! आप उसकी समस्त मनोकामनाओं को पूर्ण करते हैं। मार्गशीर्ष मास की षष्ठी तिथि, हेमंत ऋतु और संवत १६६४ में यह कल्याणकारी शिव चालीसा पूर्ण हुई। देवाधिदेव महादेव की सदा जय हो!"""

# 3. Authentic Vidhi & Rules for Lord Shiva (शास्त्रोक्त पाठ विधि व नियम)
shiva_chalisa_vidhi = """॥ भगवान शिव चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का समय व दिशा:
- प्रातःकाल ब्रह्ममुहूर्त अथवा सांध्यकाल प्रदोष वेला (सूर्यास्त के समय) में पाठ करना सर्वश्रेष्ठ फलदायी है।
- पूर्व अथवा उत्तर दिशा (ईशान कोण) की ओर मुख करके बैठना चाहिए।
- सोमवार, मासिक शिवरात्रि, महाशिवरात्रि, सावन मास तथा प्रत्येक माह के दोनों पक्षों की त्रयोदशी (प्रदोष व्रत) के दिन इसका पाठ अनंत गुना फल देता है।

२. आसन व वस्त्र:
- श्वेत (सफेद) अथवा हल्के पीले रंग के शुद्ध, धुले हुए वस्त्र धारण करें।
- कुशा अथवा सफेद/ऊनी आसन पर बैठकर पाठ करें।

३. शिवलिंग अभिषेक व पूजन सामग्री (अनिवार्य):
- जल व पंचामृत: तांबे के लोटे में शुद्ध जल, गंगाजल, कच्चा दूध, दही, शहद, शक्कर मिलाकर शिवलिंग का अभिषेक करें।
- अखंड बेलपत्र: तीन दलों वाला बिना कटा-फटा अक्षत बेलपत्र, भांग, धतूरा और सफेद मदार के पुष्प अर्पित करें।
- भस्म व चंदन: शिवलिंग पर सफेद चंदन और भस्म (त्रिपुण्ड) लगाएं।
- भोग: मौसमी फल, बेर, पंचमेवा, सफेद मिष्ठान अथवा मखाने की खीर अर्पित करें।
- विशेष निषेध: शिवलिंग पर कभी भी तुलसी दल, केतकी का पुष्प, सिंदूर या हल्दी न चढ़ाएं।

४. दीपक व धूप:
- शुद्ध देशी गाय के घी का दीपक प्रज्वलित करें।
- गुग्गुल, लोबान अथवा कर्पूर की सुगंधित धूप अवश्य दें।

५. पाठ की संख्या व संकल्प:
- सामान्य दैनिक साधना: नित्य १, ३ या ५ पाठ।
- ऋण मुक्ति, रोग मुक्ति अथवा संतान प्राप्ति हेतु: ४० दिनों तक नित्य ११ पाठ अथवा प्रदोष व्रत रखकर हवन सहित पाठ का संकल्प लें।
- पाठ के आरम्भ और अंत में 'ॐ नमः शिवाय' महामंत्र का कम से कम एक माला (१०८ बार) जप अवश्य करें।
- पाठ उपरांत 'कर्पूरगौरं करुणावतारं' तथा शिव जी की आरती करें।"""

# 4. Significance & Phalasruti (आध्यात्मिक माहात्म्य व फलश्रुति)
shiva_chalisa_significance = """॥ भगवान शिव चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. अकाल मृत्यु भय व महामृत्युंजय रक्षा कवच:
भगवान शिव महाकाल और कालों के काल हैं। इस पावन चालीसा का नियमित पाठ करने वाले साधक को अकाल मृत्यु का भय नहीं रहता तथा गंभीर दुर्घटनाओं, विष-दोष और असाध्य रोगों से दिव्य रक्षा प्राप्त होती है।

२. 'ॠनियां जो कोई हो अधिकारी' — ऋण व दरिद्रता से मुक्ति:
आर्थिक संकट, भारी कर्ज और व्यापारिक मंदी से जूझ रहे भक्तों के लिए यह चालीसा वरदान स्वरूप है। शिव कृपा से दरिद्रता का नाश होकर धन-धान्य और अक्षय लक्ष्मी की वृद्धि होती है।

३. संतान सुख व परिवार कल्याण:
'पुत्र होन कर इच्छा जोई, निश्चय शिव प्रसाद तेहि होई' — जिन दंपत्तियों को संतान सुख में बाधा आ रही हो, वे यदि प्रदोष व्रत के साथ इस चालीसा का पाठ करें तो उन्हें सुयोग्य और दीर्घायु संतान की प्राप्ति होती है।

४. मानसिक शांति व ग्रह दोष निवारण:
शिवजी के मस्तक पर चंद्रमा विराजते हैं। इस चालीसा के पाठ से कुंडली का चंद्र दोष, राहु-केतु की पीड़ा और कालसर्प दोष शांत होता है तथा मानसिक अवसाद, अनिद्रा व तनाव दूर होकर आंतरिक शांति मिलती है।

५. अंत समय शिवपुर (कैलाश धाम) की प्राप्ति:
'जन्म जन्म के पाप नसावे, अन्त धाम शिवपुर में पावे' — निष्काम भाव से शिव आराधना करने वाले जीव के जन्म-जन्मांतर के पाप कट जाते हैं और मोक्ष की प्राप्ति होती है।

६. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह चालीसा द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल अवधी छंदों पर पूर्णतः आधारित है।"""

# 5. English Transliteration (रोमन लिपि)
shiva_chalisa_en = """॥ Shri Shiva Chalisa ॥
(By Ayodhya Das • Awadhi)

॥ Doha ॥
Jaya Ganesha Girijaa Suvana, Mangala Moola Sujaana।
Kahata Ayodhyaadaasa Tuma, Dehu Abhaya Varadaana॥

॥ Chaupai ॥
Jaya Girijaa Pati Deena Dayaalaa। Sadaa Karata Santana Pratipaalaa॥
Bhaala Chandramaa Sohata Neeke। Kaanana Kundala Naagaphanee Ke॥

Anga Gaura Shira Ganga Bahaaye। Mundamaala Tana Kshaara Lagaaye॥
Vastra Khaala Baaghambara Sohe। Chhavi Ko Dekhi Naaga Mana Mohe॥

Mainaa Maatu Kee Have Dulaaree। Baama Anga Sohata Chhavi Nyaaree॥
Kara Trishoola Sohata Chhavi Bhaaree। Karata Sadaa Shatruna Kshayakaaree॥

Nandi Ganesha Sohai Tahan Kaise। Saagara Madhya Kamala Hain Jaise॥
Kaartika Shyaama Aura Ganaraaoo। Yaa Chhavi Ko Kahi Jaata Na Kaaoo॥

Devana Jabheen Jaaya Pukaaraa। Taba Hee Dukha Prabhu Aapa Nivaaraa॥
Kiyaa Upadrava Taaraka Bhaaree। Devana Saba Mili Tumahin Juhaaree॥

Turata Shadaanana Aapa Pathaayau। Lavanimesha Mahan Maari Giraayau॥
Aapa Jalandhara Asura Samhaaraa। Suyasha Tumhaara Vidita Samsaaraa॥

Tripuraasura Sana Yuddha Machaa-ee। Sabahin Kripaa Kari Leena Bachaa-ee॥
Kiyaa Tapahin Bhaageeratha Bhaaree। Puraba Pratigyaa Taasu Puraaree॥

Daanina Mahan Tuma Sama Kou Naaheen। Sevaka Stuti Karata Sadaaheen॥
Veda Maahi Mahimaa Tuma Gaa-ee। Akatha Anaadi Bheda Nahin Paa-ee॥

Prakatee Udadhi Manthana Men Jwaalaa। Jarata Suraasura Bhae Vihaalaa॥
Keenhee Dayaa Tahan Karee Sahaa-ee। Neelakantha Taba Naama Kahaa-ee॥

Poojana Raamachandra Jaba Keenhaa। Jeeta Ke Lanka Vibheeshana Deenhaa॥
Sahasa Kamala Men Ho Rahe Dhaaree। Keenha Pareekshaa Tabahin Puraaree॥

Eka Kamala Prabhu Raakheu Jo-ee। Kamala Nayana Poojana Chahan So-ee॥
Kathina Bhakti Dekhee Prabhu Shankara। Bhae Prasanna Diye Ichhita Vara॥

Jaya Jaya Jaya Ananta Avinaashee। Karata Kripaa Saba Ke Ghatavaasee॥
Dushta Sakala Nita Mohi Sataavai। Bhramata Rahon Mohi Chaina Na Aavai॥

Traahi Traahi Main Naatha Pukaaro। Yehi Avasara Mohi Aana Ubaaro॥
Lai Trishoola Shatruna Ko Maaro। Sankata Te Mohi Aana Ubaaro॥

Maata-Pitaa Bhraataa Saba Ho-ee। Sankata Men Poochhata Nahin Ko-ee॥
Swaamee Eka Hai Aasa Tumhaaree। Aaya Harahu Mama Sankata Bhaaree॥

Dhana Nirdhana Ko Deta Sadaa Heen। Jo Ko-ee Jaanche So Phala Paaheen॥
Astuti Kehi Vidhi Karain Tumhaaree। Kshamahu Naatha Aba Chooka Hamaaree॥

Shankara Ho Sankata Ke Naashana। Mangala Kaarana Vighna Vinaashana॥
Yogee Yati Muni Dhyaana Lagaavain। Shaarada Naarada Sheesha Navaavain॥

Namo Namo Jaya Namah Shivaaya। Sura Brahmaadika Paara Na Paaya॥
Jo Yaha Paatha Kare Mana Laa-ee। Taa Para Hota Hai Shambhu Sahaa-ee॥

Riniyaan Jo Ko-ee Ho Adhikaaree। Paatha Kare So Paavana Haaree॥
Putra Hona Kara Ichhaa Jo-ee। Nishchaya Shiva Prasaada Tehi Ho-ee॥

Pandita Trayodashee Ko Laave। Dhyaana Poorvaka Homa Karaave॥
Trayodashee Vrata Karai Hameshaa। Taake Tana Naheen Rahai Kaleshaa॥

Dhoopa Deepa Naivedya Chadhaave। Shankara Sammukha Paatha Sunaave॥
Janma Janma Ke Paapa Nasaave। Anta Dhaama Shivapura Men Paave॥
Kahain Ayodhyaadaasa Aasa Tumhaaree। Jaani Sakala Dukha Harahu Hamaaree॥

॥ Doha ॥
Nitta Nema Uthi Praatah Hee, Paatha Karo Chaaleesaa।
Tuma Meree Manokaamanaa, Poorna Karo Jagadeesha॥

Magasira Chhathi Hemanta Ritu, Samvata Chausatha Jaana।
Stuti Chaaleesaa Shivahi, Poorna Keena Kalyaana॥"""

# 6. Update drik_chalisa_collections.json
with open('drik_chalisa_collections.json', encoding='utf-8') as f:
    chalisa_data = json.load(f)

for it in chalisa_data['shiva']['items']:
    if it['id'] == 'drik_chalisa_4':
        it['title'] = 'भगवान शिव चालीसा'
        it['title_en'] = 'Lord Shiva Chalisa (Shiva Chalisa)'
        it['hi_line'] = 'जय गिरिजा पति दीन दयाला'
        it['en_line'] = 'Jai Girija Pati Deen Dayala'
        it['sub'] = 'कवि अयोध्यादास कृत पावन चालीसा • Drik Panchang Verified'
        it['thumb'] = 'assets/gallery/bal_shiva.jpg'
        it['video_id'] = '-mUoM-sSzkc'
        it['audio_url'] = 'https://www.youtube.com/watch?v=-mUoM-sSzkc'
        it['drik_url'] = 'https://www.drikpanchang.com/lyrics/chalisa/lord-shiva/shiva-chalisa.html?lang=hi&ck=1'
        it['source'] = 'Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)'
        it['content'] = shiva_chalisa_content
        it['meaning'] = shiva_chalisa_meaning
        it['vidhi'] = shiva_chalisa_vidhi
        it['significance'] = shiva_chalisa_significance
        it['english_lyrics'] = shiva_chalisa_en
        print("Updated drik_chalisa_4 in drik_chalisa_collections.json!")
        break

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

# Add or update chalisa_shiv and chalisa_shiva in CONTENT in app.js
c_shiv_record = f"""chalisa_shiv: {{
    title: 'भगवान शिव चालीसा',
    deity: 'देवाधिदेव महादेव भगवान शिव',
    mantra: '॥ ॐ नमः शिवाय • ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम् ॥',
    text: `{shiva_chalisa_content}`,
    meaning: `{shiva_chalisa_meaning}`,
    vidhi: `{shiva_chalisa_vidhi}`,
    significance: `{shiva_chalisa_significance}`,
    english_lyrics: `{shiva_chalisa_en}`,
    audio_url: 'https://www.youtube.com/watch?v=-mUoM-sSzkc',
    video_id: '-mUoM-sSzkc',
    thumb: 'assets/gallery/bal_shiva.jpg',
    drik_url: 'https://www.drikpanchang.com/lyrics/chalisa/lord-shiva/shiva-chalisa.html?lang=hi&ck=1'
  }},
  chalisa_shiva: {{
    title: 'भगवान शिव चालीसा',
    deity: 'देवाधिदेव महादेव भगवान शिव',
    mantra: '॥ ॐ नमः शिवाय • ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम् ॥',
    text: `{shiva_chalisa_content}`,
    meaning: `{shiva_chalisa_meaning}`,
    vidhi: `{shiva_chalisa_vidhi}`,
    significance: `{shiva_chalisa_significance}`,
    english_lyrics: `{shiva_chalisa_en}`,
    audio_url: 'https://www.youtube.com/watch?v=-mUoM-sSzkc',
    video_id: '-mUoM-sSzkc',
    thumb: 'assets/gallery/bal_shiva.jpg',
    drik_url: 'https://www.drikpanchang.com/lyrics/chalisa/lord-shiva/shiva-chalisa.html?lang=hi&ck=1'
  }},
  """

if 'chalisa_shiv:' in app_js:
    pos_s = app_js.find('chalisa_shiv:')
    pos_s_end = app_js.find('chalisa_', pos_s + 20)
    app_js = app_js[:pos_s] + c_shiv_record + app_js[pos_s_end:]
    print("Replaced existing chalisa_shiv in CONTENT!")
else:
    # Insert right before chalisa_ganesh:
    pos_gan = app_js.find('chalisa_ganesh:')
    if pos_gan != -1:
        app_js = app_js[:pos_gan] + c_shiv_record + app_js[pos_gan:]
        print("Inserted chalisa_shiv before chalisa_ganesh in CONTENT!")
    else:
        print("Warning: chalisa_ganesh not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Saved app.js successfully!")
