import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Authentic Devanagari Lyrics from Drik Panchang
durga_chalisa_content = """॥ श्री दुर्गा चालीसा ॥
(जगज्जननी माँ आद्यशक्ति दुर्गा भवानी • भाषा: अवधी / ब्रज)

॥ चौपाई ॥
नमो नमो दुर्गे सुख करनी। नमो नमो अम्बे दुःख हरनी॥
निराकार है ज्योति तुम्हारी। तिहूँ लोक फैली उजियारी॥

शशि ललाट मुख महाविशाला। नेत्र लाल भृकुटि विकराला॥
रूप मातु को अधिक सुहावे। दरश करत जन अति सुख पावे॥

तुम संसार शक्ति लय कीना। पालन हेतु अन्न धन दीना॥
अन्नपूर्णा हुई जग पाला। तुम ही आदि सुन्दरी बाला॥

प्रलयकाल सब नाशन हारी। तुम गौरी शिवशंकर प्यारी॥
शिव योगी तुम्हरे गुण गावें। ब्रह्मा विष्णु तुम्हें नित ध्यावें॥

रूप सरस्वती को तुम धारा। दे सुबुद्धि ऋषि-मुनिन उबारा॥
धरा रूप नरसिंह को अम्बा। प्रगट भईं फाड़कर खम्बा॥

रक्षा कर प्रह्लाद बचायो। हिरण्याक्ष को स्वर्ग पठायो॥
लक्ष्मी रूप धरो जग माहीं। श्री नारायण अंग समाहीं॥

क्षीरसिन्धु में करत विलासा। दयासिन्धु दीजै मन आसा॥
हिंगलाज में तुम्हीं भवानी। महिमा अमित न जात बखानी॥

मातंगी अरु धूमावति माता। भुवनेश्वरी बगला सुख दाता॥
श्री भैरव तारा जग तारिणी। छिन्न भाल भव दुःख निवारिणी॥

केहरि वाहन सोह भवानी। लांगुर वीर चलत अगवानी॥
कर में खप्पर-खड्ग विराजै। जाको देख काल डर भाजे॥

सोहै अस्त्र और त्रिशूला। जाते उठत शत्रु हिय शूला॥
नगर कोटि में तुम्हीं विराजत। तिहुंलोक में डंका बाजत॥

शुम्भ निशुम्भ दानव तुम मारे। रक्तबीज शंखन संहारे॥
महिषासुर नृप अति अभिमानी। जेहि अघ भार मही अकुलानी॥

रूप कराल कालिका धारा। सेन सहित तुम तिहि संहारा॥
परी गाढ़ सन्तन पर जब-जब। भई सहाय मातु तुम तब तब॥

अमरपुरी अरु बासव लोका। तब महिमा सब रहें अशोका॥
ज्वाला में है ज्योति तुम्हारी। तुम्हें सदा पूजें नर-नारी॥

प्रेम भक्ति से जो यश गावै। दुःख दारिद्र निकट नहिं आवें॥
ध्यावे तुम्हें जो नर मन लाई। जन्म-मरण ताकौ छुटि जाई॥

जोगी सुर मुनि कहत पुकारी। योग न हो बिन शक्ति तुम्हारी॥
शंकर आचारज तप कीनो। काम अरु क्रोध जीति सब लीनो॥

निशिदिन ध्यान धरो शंकर को। काहु काल नहिं सुमिरो तुमको॥
शक्ति रूप को मरम न पायो। शक्ति गई तब मन पछितायो॥

शरणागत हुई कीर्ति बखानी। जय जय जय जगदम्ब भवानी॥
भई प्रसन्न आदि जगदम्बा। दई शक्ति नहिं कीन विलम्बा॥

मोको मातु कष्ट अति घेरो। तुम बिन कौन हरै दुःख मेरो॥
आशा तृष्णा निपट सतावे। मोह मदादिक सब विनशावै॥

शत्रु नाश कीजै महारानी। सुमिरौं इकचित तुम्हें भवानी॥
करो कृपा हे मातु दयाला। ऋद्धि-सिद्धि दे करहु निहाला॥

जब लगि जियउं दया फल पाऊं। तुम्हरो यश मैं सदा सुनाऊं॥
दुर्गा चालीसा जो नित गावै। सब सुख भोग परमपद पावै॥

देवीदास शरण निज जानी। करहु कृपा जगदम्ब भवानी॥

॥ दोहा ॥
शरणागत रक्षा करे, भक्तन पर कृपा अपार।
दुष्ट दलन दुःख हरन माँ, करहु भव से पार॥"""

# 2. Verse-by-verse Spiritual Meaning (पद्यवार सम्पूर्ण पावन भावार्थ)
durga_chalisa_meaning = """॥ श्री दुर्गा चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【चौपाइयां — भावार्थ】
१. नमो नमो दुर्गे सुख करनी। नमो नमो अम्बे दुःख हरनी॥
निराकार है ज्योति तुम्हारी। तिहूँ लोक फैली उजियारी॥
भावार्थ: समस्त सुखों को प्रदान करने वाली हे माँ दुर्गे! आपको बारम्बार नमन है। भक्तों के समस्त दुःखों और संतापों को हरने वाली हे जगदम्बे! आपको बारम्बार प्रणाम है। आपका मूल स्वरूप निराकार एवं दिव्य दिव्य-ज्योति स्वरूप है, जिसकी अलौकिक प्रभा तीनों लोकों (स्वर्ग, मर्त्य, पाताल) में प्रकाश फैला रही है।

२. शशि ललाट मुख महाविशाला। नेत्र लाल भृकुटि विकराला॥
रूप मातु को अधिक सुहावे। दरश करत जन अति सुख पावे॥
भावार्थ: आपके मस्तक पर द्वितीय का चंद्रमा शोभायमान है, आपका मुखमण्डल अत्यंत विशाल एवं दिव्य है। आपके नेत्र अरुण (लाल) हैं और दुष्टों के संहार हेतु भृकुटि विकराल है। माता का यह ममतामयी एवं तेजस्वी स्वरूप अत्यंत सुहावना लगता है, जिसके दर्शन मात्र से भक्तजन परम आनंद और शांति पाते हैं।

३. तुम संसार शक्ति लय कीना। पालन हेतु अन्न धन दीना॥
अन्नपूर्णा हुई जग पाला। तुम ही आदि सुन्दरी बाला॥
भावार्थ: आप ही सृष्टि की मूल शक्ति हैं और प्रलयकाल में सम्पूर्ण संसार को अपने भीतर विलीन (लय) कर लेती हैं। संसार के पालन-पोषण हेतु आप ही जीवों को अन्न और धन-धान्य प्रदान करती हैं। माँ अन्नपूर्णा बनकर आपने समस्त जगत का पालन किया और आप ही आद्यशक्ति त्रिपुर सुन्दरी (षोडशी) हैं।

४. प्रलयकाल सब नाशन हारी। तुम गौरी शिवशंकर प्यारी॥
शिव योगी तुम्हरे गुण गावें। ब्रह्मा विष्णु तुम्हें नित ध्यावें॥
भावार्थ: प्रलय के समय आप ही संहारिणी महाकाली बनकर समस्त बुराइयों का नाश करती हैं। आप ही भगवान शिवशंकर की परम प्रिय अर्धांगिनी माँ गौरी हैं। योगिराज भगवान शिव निरन्तर आपके पावन गुणों का गान करते हैं और सृष्टि के रचयिता ब्रह्मा तथा पालनकर्ता विष्णु नित्य आपका ही ध्यान धरते हैं।

५. रूप सरस्वती को तुम धारा। दे सुबुद्धि ऋषि-मुनिन उबारा॥
धरा रूप नरसिंह को अम्बा। प्रगट भईं फाड़कर खम्बा॥
भावार्थ: आपने ही विद्या की अधिष्ठात्री माँ सरस्वती का रूप धारण किया और ऋषि-मुनियों को दिव्य सुबुद्धि व ज्ञान प्रदान कर उनका उद्धार किया। हे अम्बे! भक्त प्रह्लाद की रक्षा हेतु आप ही भगवान नृसिंह की शक्ति बनकर पाषाण के खंभे को चीरकर प्रकट हुईं।

६. रक्षा कर प्रह्लाद बचायो। हिरण्याक्ष को स्वर्ग पठायो॥
लक्ष्मी रूप धरो जग माहीं। श्री नारायण अंग समाहीं॥
भावार्थ: आपने अपने अनन्य भक्त प्रह्लाद की रक्षा की और दुष्ट हिरण्यकशिपु (हिरण्याक्ष कुल) का वध कर दिया। इस जगत में आप ही धन-ऐश्वर्य की अधिष्ठात्री महालक्ष्मी का रूप धारण करती हैं और भगवान श्री नारायण के वक्षस्थल में नित्य निवास करती हैं।

७. क्षीरसिन्धु में करत विलासा। दयासिन्धु दीजै मन आसा॥
हिंगलाज में तुम्हीं भवानी। महिमा अमित न जात बखानी॥
भावार्थ: आप क्षीरसागर में भगवान विष्णु के संग आनंदपूर्वक विहार करती हैं। हे दया की सागर माँ! मेरे मन की सभी धर्मयुक्त अभिलाषाओं को पूर्ण कीजिए। परम पावन हिंगलाज शक्तिपीठ में आप ही माँ भवानी के रूप में विराजमान हैं, आपकी अनंत महिमा का वर्णन वाणी से संभव नहीं है।

८. मातंगी अरु धूमावति माता। भुवनेश्वरी बगला सुख दाता॥
श्री भैरव तारा जग तारिणी। छिन्न भाल भव दुःख निवारिणी॥
भावार्थ: आप ही दस महाविद्याओं के रूप में पूजित हैं—माँ मातंगी, धूमावती, समस्त सुखों को देने वाली भुवनेश्वरी और बगलामुखी आप ही हैं। संसार को भवसागर से तारने वाली माँ तारा, भैरवी तथा मस्तक पर खप्पर धारण कर संसार के दुःखों को मिटाने वाली छिन्नमस्ता भी आप ही हैं।

९. केहरि वाहन सोह भवानी। लांगुर वीर चलत अगवानी॥
कर में खप्पर-खड्ग विराजै। जाको देख काल डर भाजे॥
भावार्थ: हे माँ भवानी! आप सिंह (केहरि) पर सवार होकर अत्यंत शोभायमान होती हैं। महावीर हनुमान जी (लांगुर वीर) और भैरव जी आपकी अगवानी में आगे-आगे चलते हैं। आपके पावन हाथों में खप्पर और तीक्ष्ण खड्ग सुशोभित है, जिसके भयानक तेज को देखकर साक्षात् काल भी भयभीत होकर भाग जाता है।

१०. सोहै अस्त्र और त्रिशूला। जाते उठत शत्रु हिय शूला॥
नगर कोटि में तुम्हीं विराजत। तिहुंलोक में डंका बाजत॥
भावार्थ: आपके हाथों में दिव्य अस्त्र-शस्त्र और त्रिशूल सुशोभित हैं, जिन्हें देखकर शत्रुओं के हृदय में भय का शूल उठने लगता है। प्रसिद्ध नगरकोट (कांगड़ा धाम) में आप ही साक्षात् विराजमान हैं और तीनों लोकों में आपके नाम और प्रताप का डंका बजता है।

११. शुम्भ निशुम्भ दानव तुम मारे। रक्तबीज शंखन संहारे॥
महिषासुर नृप अति अभिमानी। जेहि अघ भार मही अकुलानी॥
भावार्थ: आपने देवताओं को संकटमुक्त करने हेतु शुम्भ और निशुम्भ जैसे भयंकर असुरों का वध किया और असंख्य रक्तबीज राक्षसों का संहार किया। जब घमंडी दैत्यराज महिषासुर के पापों के भार से समूची पृथ्वी व्याकुल होकर कराह उठी थी—

१२. रूप कराल कालिका धारा। सेन सहित तुम तिहि संहारा॥
परी गाढ़ सन्तन पर जब-जब। भई सहाय मातु तुम तब तब॥
भावार्थ: तब आपने भयानक एवं रौद्र रूपिणी महाकाली का स्वरूप धारण किया और महिषासुर को उसकी विशाल सेना सहित यमलोक भेज दिया। जब-जब भी साधु-संतों, भक्तों और धर्म पर संकट आया, तब-तब हे माँ! आपने प्रकट होकर उनकी सहायता और रक्षा की।

१३. अमरपुरी अरु बासव लोका। तब महिमा सब रहें अशोका॥
ज्वाला में है ज्योति तुम्हारी। तुम्हें सदा पूजें नर-नारी॥
भावार्थ: आपकी असीम कृपा से ही अमरावती और इन्द्रलोक (बासव लोक) दैत्यों के भय से मुक्त होकर सदा शोकरहित और आनंदित रहते हैं। श्री ज्वाला जी के पावन धाम में आपकी ही अखंड ज्योति प्रज्वलित रहती है, जहाँ संसार के समस्त नर-नारी श्रद्धापूर्वक आपका पूजन करते हैं।

१४. प्रेम भक्ति से जो यश गावै। दुःख दारिद्र निकट नहिं आवें॥
ध्यावे तुम्हें जो नर मन लाई। जन्म-मरण ताकौ छुटि जाई॥
भावार्थ: जो मनुष्य प्रेम और अनन्य भक्ति भाव से आपके पावन यश का गान करता है, उसके निकट कभी दुःख, दरिद्रता और संकट नहीं फटकते। जो एकाग्रचित्त होकर आपका ध्यान करता है, वह जन्म-मरण के कठिन आवागमन के चक्र से सदा के लिए मुक्त हो जाता है।

१५. जोगी सुर मुनि कहत पुकारी। योग न हो बिन शक्ति तुम्हारी॥
शंकर आचारज तप कीनो। काम अरु क्रोध जीति सब लीनो॥
भावार्थ: सभी योगी, देवता और ऋषि-मुनि पुकार-पुकार कर यही सत्य कहते हैं कि आपकी 'शक्ति' के बिना कोई भी योग या साधना सिद्ध नहीं हो सकती। जगद्गुरु आदि शंकराचार्य जी ने घोर तपस्या की और काम, क्रोध आदि समस्त विकारों पर पूर्ण विजय प्राप्त कर ली।

१६. निशिदिन ध्यान धरो शंकर को। काहु काल नहिं सुमिरो तुमको॥
शक्ति रूप को मरम न पायो। शक्ति गई तब मन पछितायो॥
भावार्थ: वे रात-दिन केवल भगवान शिव का ध्यान करते थे और आदि शक्ति (माँ भगवती) का स्मरण नहीं करते थे। जब वे आपकी शक्ति का मर्म न समझ सके और शरीर से शक्ति क्षीण हो गई, तब वे अत्यंत लज्जित होकर मन में पश्चाताप करने लगे।

१७. शरणागत हुई कीर्ति बखानी। जय जय जय जगदम्ब भवानी॥
भई प्रसन्न आदि जगदम्बा। दई शक्ति नहिं कीन विलम्बा॥
भावार्थ: तब शंकराचार्य जी ने आद्यशक्ति की शरणागति ली और 'सौंदर्य लहरी' रचकर जगदम्बा की जय-जयकार की। इस पर आदि जगदम्बा अत्यंत प्रसन्न हुईं और बिना किसी विलंब के उन्हें पुनः असीम चेतना व शक्ति प्रदान कर दी।

१८. मोको मातु कष्ट अति घेरो। तुम बिन कौन हरै दुःख मेरो॥
आशा तृष्णा निपट सतावे। मोह मदादिक सब विनशावै॥
भावार्थ: हे माँ! सांसारिक कष्टों और संतापों ने मुझे चारों ओर से घेर रखा है। आपके अतिरिक्त मेरे दुःखों को हरने वाला संसार में और कौन है? सांसारिक आशाएं और तृष्णाएं मुझे अत्यंत सताती हैं, कृपा करके मेरे मोह, मद, काम, क्रोध आदि विकारों का समूल नाश कीजिए।

१९. शत्रु नाश कीजै महारानी। सुमिरौं इकचित तुम्हें भवानी॥
करो कृपा हे मातु दयाला। ऋद्धि-सिद्धि दे करहु निहाला॥
भावार्थ: हे महारानी! मैं एकाग्रचित्त होकर केवल आपका ही स्मरण करता हूँ, मेरे समस्त आंतरिक और बाह्य शत्रुओं का नाश कीजिए। हे दयामयी माँ! मुझ पर अपनी कृपादृष्टि कीजिए और मुझे ऋद्धि-सिद्धि तथा आत्मिक सुख देकर कृतार्थ कर दीजिए।

२०. जब लगि जियउं दया फल पाऊं। तुम्हरो यश मैं सदा सुनाऊं॥
दुर्गा चालीसा जो नित गावै। सब सुख भोग परमपद पावै॥
देवीदास शरण निज जानी। करहु कृपा जगदम्ब भवानी॥
भावार्थ: जब तक मेरे शरीर में प्राण रहें, मैं आपकी दया और कृपा का फल प्राप्त करता रहूँ और सदैव आपके पावन यश का गान करता रहूँ। जो मनुष्य नित्य नियमपूर्वक इस दुर्गा चालीसा का पाठ करता है, वह संसार के समस्त सुखों को भोगकर अंत में परम पद (मोक्ष) को प्राप्त करता है। भक्त देवीदास को अपनी शरण में आया जानकर, हे जगदम्बा भवानी! सदा अपनी कृपा बनाए रखिए।

【समापन दोहा】
शरणागत रक्षा करे, भक्तन पर कृपा अपार।
दुष्ट दलन दुःख हरन माँ, करहु भव से पार॥
भावार्थ: अपने शरणागत की रक्षा करने वाली और भक्तों पर अपार कृपा बरसाने वाली हे माँ दुर्गे! आप दुष्टों का दलन करने वाली और समस्त दुःखों को हरने वाली हैं, कृपा करके हमें इस संसार-सागर से पार लगाइए।"""

# 3. Authentic Worship Procedure & Rules (शास्त्रोक्त पाठ विधि व नियम)
durga_chalisa_vidhi = """॥ श्री दुर्गा चालीसा पाठ एवं पूजन विधि व नियम ॥

१. पावन काल व विशेष मुहूर्त:
• प्रतिदिन प्रातःकाल ब्रह्ममुहूर्त अथवा संध्याकाल में पाठ करना सर्वोत्तम है।
• विशेष रूप से शारदीय एवं चैत्र नवरात्रि (नौ दिन), मासिक दुर्गाष्टमी, प्रत्येक शुक्रवार, मंगलवार, विजयादशमी एवं महाअष्टमी के दिन इसका पाठ अनंत गुना फलदायी है।

२. आवश्यक पूजन सामग्री:
• माँ दुर्गा का पावन चित्र या विग्रह (सिंहवाहिनी अष्टभुजा स्वरूप)।
• शुद्ध गाय के घी अथवा तिल के तेल का दीपक, धूप, अगरबत्ती, कपूर।
• रोली, कुमकुम, लाल चंदन, अक्षत (अखंड चावल)।
• लाल पुष्प (विशेषकर गुड़हल अथवा लाल गुलाब), लाल पुष्पों की माला।
• लाल चुनरी, सिन्दूर, इत्र।
• नैवेद्य: हलवा-पूरी, चना, खीर, बताशा, लौंग का जोड़ा (कपूर पर रखकर आहुति हेतु) एवं ताजे ऋतुफल।

३. शास्त्रोक्त पूजन विधान:
• स्नानादि कर स्वच्छ लाल या पीले वस्त्र धारण करें।
• पूर्व अथवा उत्तर दिशा की ओर मुख करके लाल ऊनी आसन पर बैठें।
• सम्मुख पाटे पर लाल वस्त्र बिछाकर माँ दुर्गा की स्थापना करें।
• सर्वप्रथम दीपक प्रज्वलित करें और विघ्नहर्ता श्री गणेश जी तथा भैरव जी का स्मरण करें।
• माँ दुर्गा को कुमकुम का तिलक लगाएं, अक्षत, लाल पुष्प और लाल चुनरी अर्पित करें।
• लौंग का जोड़ा और बताशा तथा हलवा-चना का भोग लगाएं।
• हाथ में जल व पुष्प लेकर संकल्प करें और पूर्ण श्रद्धा, शुद्ध उच्चारण व शांत चित्त से चालीसा का पाठ करें।
• पाठ पूर्ण होने पर 'ॐ दुं दुर्गायै नमः' अथवा नवार्ण मंत्र 'ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे' का १०८ बार जप करें।
• अंत में माँ दुर्गा की कपूर से आरती करें और क्षमा प्रार्थना करें।

४. विशेष मनोकामना अनुष्ठान नियम:
• किसी विशेष संकट निवारण अथवा मनोकामना पूर्ति हेतु नवरात्रि में नित्य ३, ७ या ११ बार दुर्गा चालीसा का पाठ करें।
• अनुष्ठान के दौरान पूर्ण सात्विक आहार लें, ब्रह्मचर्य का पालन करें और घर में अखंड ज्योति या नित्य दीप प्रज्वलित रखें।"""

# 4. Spiritual Significance & Fruits (आध्यात्मिक महत्त्व व फलश्रुति)
durga_chalisa_significance = """॥ श्री दुर्गा चालीसा का आध्यात्मिक महत्त्व व फलश्रुति ॥

१. समस्त दुःखों व संतापों का नाश:
'नमो नमो दुर्गे सुख करनी। नमो नमो अम्बे दुःख हरनी॥'
माँ दुर्गा सुखों की दात्री और समस्त दैहिक, दैविक व भौतिक तापों की संहारिणी हैं। इस चालीसा के पाठ से घर से अशांति, क्लेश और दरिद्रता का समूल नाश होता है।

२. भय, शत्रु व नकारात्मक ऊर्जा से रक्षा:
'सोहै अस्त्र और त्रिशूला। जाते उठत शत्रु हिय शूला॥'
माँ भवानी अपने सिंहवाहिनी स्वरूप में भक्तों के समस्त ज्ञात-अज्ञात शत्रुओं, ऊपरी बाधाओं, तंत्र-मंत्र और नकारात्मक शक्तियों से ढाल बनकर रक्षा करती हैं।

३. अखंड सौभाग्य, ऋद्धि-सिद्धि व ऐश्वर्य:
माँ अन्नपूर्णा और महालक्ष्मी स्वरूप में जगदम्बा अपने साधकों को अखंड धन-धान्य, सुखी गृहस्थ जीवन, उत्तम स्वास्थ्य और ऋद्धि-सिद्धि प्रदान करती हैं।

४. आत्मबल व आंतरिक विकारों पर विजय:
'आशा तृष्णा निपट सतावे। मोह मदादिक सब विनशावै॥'
चालीसा पाठ से काम, क्रोध, मद, लोभ और अहंकार जैसे आंतरिक शत्रुओं का शमन होता है और साधक को अदम्य आत्मबल व विवेक की प्राप्ति होती है।

५. परम पद (मोक्ष) की प्राप्ति:
'दुर्गा चालीसा जो नित गावै। सब सुख भोग परमपद पावै॥'
जो भी भक्त निष्काम भाव से नित्य दुर्गा चालीसा का गायन करता है, वह इस लोक में समस्त सुख-ऐश्वर्य का उपभोग कर अंत में माँ के परम धाम (मणिद्वीप / मोक्ष) को प्राप्त करता है।"""

# 5. English Transliteration (रोमन लिप्यंतरण)
durga_chalisa_en = """॥ Shri Durga Chalisa ॥

॥ Chaupai ॥
Namo Namo Durge Sukha Karani। Namo Namo Ambe Dukha Harani॥
Nirakara Hai Jyoti Tumhari। Tihun Loka Phaili Ujiyari॥

Shashi Lalata Mukha Mahavishala। Netra Lala Bhrikuti Vikarala॥
Rupa Matu Ko Adhika Suhave। Darasha Karata Jana Ati Sukha Pave॥

Tuma Sansara Shakti Laya Kina। Palana Hetu Anna Dhana Dina॥
Annapurna Hui Jaga Pala। Tuma Hi Adi Sundari Bala॥

Pralayakala Saba Nashana Hari। Tuma Gauri Shivashankara Pyari॥
Shiva Yogi Tumhare Guna Gaven। Brahma Vishnu Tumhen Nita Dhyaven॥

Rupa Sarasvati Ko Tuma Dhara। De Subuddhi Rishi-Munina Ubara॥
Dhara Rupa Narsimha Ko Amba। Pragata Bhain Phadakara Khamba॥

Raksha Kara Prahlada Bachayo। Hiranyaksha Ko Svarga Pathayo॥
Lakshmi Rupa Dharo Jaga Mahin। Shri Narayana Anga Samahin॥

Kshirasindhu Mein Karata Vilasa। Dayasindhu Dijai Mana Aasa॥
Hingalaja Mein Tumhin Bhavani। Mahima Amita Na Jata Bakhani॥

Matangi Aru Dhumavati Mata। Bhuvaneshvari Bagala Sukha Data॥
Shri Bhairava Tara Jaga Tarini। Chhinna Bhala Bhava Dukha Nivarini॥

Kehari Vahana Soha Bhavani। Langura Vira Chalata Agavani॥
Kara Mein Khappara-Khadga Virajai। Jako Dekha Kala Dara Bhaje॥

Sohai Astra Aura Trishula। Jate Uthata Shatru Hiya Shula॥
Nagara Koti Mein Tumhin Virajata। Tihunloka Mein Danka Bajata॥

Shumbha Nishumbha Danava Tuma Mare। Raktabija Shankhana Samhare॥
Mahishasura Nripa Ati Abhimani। Jehi Agha Bhara Mahi Akulani॥

Rupa Karala Kalika Dhara। Sena Sahita Tuma Tihi Samhara॥
Pari Gadha Santana Para Jaba-Jaba। Bhai Sahaya Matu Tuma Taba Taba॥

Amarapuri Aru Basava Loka। Taba Mahima Saba Rahen Ashoka॥
Jvala Mein Hai Jyoti Tumhari। Tumhen Sada Pujen Nara-Nari॥

Prema Bhakti Se Jo Yasha Gavai। Dukha Daridra Nikata Nahin Aaven॥
Dhyave Tumhen Jo Nara Mana Lai। Janma-Marana Tako Chhuti Jai॥

Jogi Sura Muni Kahata Pukari। Yoga Na Ho Bina Shakti Tumhari॥
Shankara Acharaja Tapa Kino। Kama Aru Krodha Jiti Saba Lino॥

Nishidina Dhyana Dharo Shankara Ko। Kahu Kala Nahin Sumiro Tumako॥
Shakti Rupa Ko Marama Na Payo। Shakti Gai Taba Mana Pachhitayo॥

Sharanagata Hui Kirti Bakhani। Jai Jai Jai Jagadamba Bhavani॥
Bhai Prasanna Adi Jagadamba। Dai Shakti Nahin Kina Vilamba॥

Moko Matu Kashta Ati Ghero। Tuma Bina Kauna Harai Dukha Mero॥
Asha Trishna Nipata Satave। Moha Madadika Saba Vinashavai॥

Shatru Nasha Kijai Maharani। Sumiraun Ikachita Tumhen Bhavani॥
Karo Kripa He Matu Dayala। Riddhi-Siddhi De Karahu Nihala॥

Jaba Lagi Jiyaun Daya Phala Paun। Tumharo Yasha Main Sada Sunaun॥
Durga Chalisa Jo Nita Gavai। Saba Sukha Bhoga Paramapada Pavai॥

Devidasa Sharana Nija Jani। Karahu Kripa Jagadamba Bhavani॥

॥ Doha ॥
Sharanagata Raksha Kare, Bhaktana Para Kripa Apara।
Dushta Dalana Dukha Harana Maan, Karahu Bhava Se Para॥"""

# 6. Update drik_chalisa_collections.json
with open('drik_chalisa_collections.json', encoding='utf-8') as f:
    chalisa_data = json.load(f)

durga_items = chalisa_data['durga']['items']
target_item = None
for item in durga_items:
    if item['id'] == 'drik_chalisa_23':
        target_item = item
        break

if target_item:
    target_item['title'] = 'दुर्गा माता चालीसा'
    target_item['title_en'] = 'Durga Mata Chalisa'
    target_item['en_line'] = 'Namo Namo Durge Sukh Karni'
    target_item['hi_line'] = 'नमो नमो दुर्गे सुख करनी'
    target_item['sub'] = 'नमो नमो दुर्गे सुख करनी • Drik Panchang Verified'
    target_item['thumb'] = 'assets/deity_durga_hd.jpg'
    target_item['audio_url'] = 'https://www.youtube.com/watch?v=bwPdADAHWtE'
    target_item['video_id'] = 'bwPdADAHWtE'
    target_item['drik_url'] = 'https://www.drikpanchang.com/lyrics/chalisa/durga-mata/durga-mata-chalisa.html?lang=hi&ck=1'
    target_item['source'] = 'Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)'
    target_item['content'] = durga_chalisa_content
    target_item['meaning'] = durga_chalisa_meaning
    target_item['vidhi'] = durga_chalisa_vidhi
    target_item['significance'] = durga_chalisa_significance
    target_item['english_lyrics'] = durga_chalisa_en
    print("Updated drik_chalisa_23 in drik_chalisa_collections.json!")
else:
    print("ERROR: drik_chalisa_23 not found in durga items!")

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

# Add or replace chalisa_durga in CONTENT in app.js
c_durga_record = f"""chalisa_durga: {{
    title: 'दुर्गा माता चालीसा',
    deity: 'जगज्जननी माँ दुर्गा भवानी',
    mantra: '॥ ॐ दुं दुर्गायै नमः • ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे ॥',
    text: `{durga_chalisa_content}`,
    meaning: `{durga_chalisa_meaning}`,
    vidhi: `{durga_chalisa_vidhi}`,
    significance: `{durga_chalisa_significance}`,
    english_lyrics: `{durga_chalisa_en}`,
    audio_url: 'https://www.youtube.com/watch?v=bwPdADAHWtE',
    video_id: 'bwPdADAHWtE',
    thumb: 'assets/deity_durga_hd.jpg',
    drik_url: 'https://www.drikpanchang.com/lyrics/chalisa/durga-mata/durga-mata-chalisa.html?lang=hi&ck=1'
  }},
  """

if 'chalisa_durga:' in app_js:
    pos_d = app_js.find('chalisa_durga:')
    pos_next = app_js.find('chalisa_ram:', pos_d)
    if pos_next != -1:
        app_js = app_js[:pos_d] + c_durga_record + app_js[pos_next:]
        print("Replaced existing chalisa_durga in CONTENT!")
    else:
        print("Notice: could not find next item after chalisa_durga")
else:
    pos_target = app_js.find('chalisa_ram:')
    if pos_target != -1:
        app_js = app_js[:pos_target] + c_durga_record + app_js[pos_target:]
        print("Inserted chalisa_durga before chalisa_ram in CONTENT!")
    else:
        print("ERROR: chalisa_ram not found in CONTENT!")

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
