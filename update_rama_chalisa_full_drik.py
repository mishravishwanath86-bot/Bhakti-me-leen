import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Authentic Devanagari Lyrics from Drik Panchang
rama_chalisa_content = """॥ श्री राम चालीसा ॥
(मर्यादा पुरुषोत्तम भगवान श्री राम • भाषा: अवधी / ब्रज)

॥ चौपाई ॥
श्री रघुबीर भक्त हितकारी। सुनि लीजै प्रभु अरज हमारी॥
निशि दिन ध्यान धरै जो कोई। ता सम भक्त और नहीं होई॥

ध्यान धरें शिवजी मन मांही। ब्रह्मा, इन्द्र पार नहीं पाहीं॥
दूत तुम्हार वीर हनुमाना। जासु प्रभाव तिहुं पुर जाना॥

जय, जय, जय रघुनाथ कृपाला। सदा करो संतन प्रतिपाला॥
तुव भुजदण्ड प्रचण्ड कृपाला। रावण मारि सुरन प्रतिपाला॥

तुम अनाथ के नाथ गोसाईं। दीनन के हो सदा सहाई॥
ब्रह्मादिक तव पार न पावैं। सदा ईश तुम्हरो यश गावैं॥

चारिउ भेद भरत हैं साखी। तुम भक्तन की लज्जा राखी॥
गुण गावत शारद मन माहीं। सुरपति ताको पार न पाहिं॥

नाम तुम्हार लेत जो कोई। ता सम धन्य और नहीं होई॥
राम नाम है अपरम्पारा। चारिहु वेदन जाहि पुकारा॥

गणपति नाम तुम्हारो लीन्हो। तिनको प्रथम पूज्य तुम कीन्हो॥
शेष रटत नित नाम तुम्हारा। महि को भार शीश पर धारा॥

फूल समान रहत सो भारा। पावत कोऊ न तुम्हरो पारा॥
भरत नाम तुम्हरो उर धारो। तासों कबहूं न रण में हारो॥

नाम शत्रुहन हृदय प्रकाशा। सुमिरत होत शत्रु कर नाशा॥
लखन तुम्हारे आज्ञाकारी। सदा करत सन्तन रखवारी॥

ताते रण जीते नहिं कोई। युद्ध जुरे यमहूं किन होई॥
महालक्ष्मी धर अवतारा। सब विधि करत पाप को छारा॥

सीता राम पुनीता गायो। भुवनेश्वरी प्रभाव दिखायो॥
घट सों प्रकट भई सो आई। जाको देखत चन्द्र लजाई॥

जो तुम्हरे नित पांव पलोटत। नवो निद्धि चरणन में लोटत॥
सिद्धि अठारह मंगलकारी। सो तुम पर जावै बलिहारी॥

औरहु जो अनेक प्रभुताई। सो सीतापति तुमहिं बनाई॥
इच्छा ते कोटिन संसारा। रचत न लागत पल की बारा॥

जो तुम्हरे चरणन चित लावै। ताकी मुक्ति अवसि हो जावै॥
सुनहु राम तुम तात हमारे। तुमहिं भरत कुल पूज्य प्रचारे॥

तुमहिं देव कुल देव हमारे। तुम गुरु देव प्राण के प्यारे॥
जो कुछ हो सो तुमहिं राजा। जय जय जय प्रभु राखो लाजा॥

राम आत्मा पोषण हारे। जय जय जय दशरथ के प्यारे॥
जय जय जय प्रभु ज्योति स्वरुपा। नर्गुण ब्रहृ अखण्ड अनूपा॥

सत्य सत्य जय सत्यव्रत स्वामी। सत्य सनातन अन्तर्यामी॥
सत्य भजन तुम्हरो जो गावै। सो निश्चय चारों फल पावै॥

सत्य शपथ गौरीपति कीन्हीं। तुमने भक्तिहिं सब सिधि दीन्हीं॥
ज्ञान हृदय दो ज्ञान स्वरुपा। नमो नमो जय जगपति भूपा॥

धन्य धन्य तुम धन्य प्रतापा। नाम तुम्हार हरत संतापा॥
सत्य शुद्ध देवन मुख गाया। बजी दुन्दुभी शंख बजाया॥

सत्य सत्य तुम सत्य सनातन। तुम ही हो हमरे तन-मन धन॥
याको पाठ करे जो कोई। ज्ञान प्रकट ताके उर होई॥

आवागमन मिटै तिहि केरा। सत्य वचन माने शिव मेरा॥
और आस मन में जो होई। मनवांछित फल पावे सोई॥

तीनहुं काल ध्यान जो ल्यावै। तुलसी दल अरु फूल चढ़ावै॥
साग पत्र सो भोग लगावै। सो नर सकल सिद्धता पावै॥

अन्त समय रघुबर पुर जाई। जहां जन्म हरि भक्त कहाई॥
श्री हरिदास कहै अरु गावै। सो बैकुण्ठ धाम को पावै॥

॥ दोहा ॥
सात दिवस जो नेम कर, पाठ करे चित लाय।
हरिदास हरि कृपा से, अवसि भक्ति को पाय॥

राम चालीसा जो पढ़े, राम चरण चित लाय।
जो इच्छा मन में करै, सकल सिद्ध हो जाय॥"""

# 2. Verse-by-verse Spiritual Meaning (पद्यवार सम्पूर्ण पावन भावार्थ)
rama_chalisa_meaning = """॥ श्री राम चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【चौपाइयां — भावार्थ】
१. श्री रघुबीर भक्त हितकारी। सुनि लीजै प्रभु अरज हमारी॥
निशि दिन ध्यान धरै जो कोई। ता सम भक्त और नहीं होई॥
भावार्थ: हे भक्तों का परम कल्याण करने वाले श्री रघुनाथ जी! आप कृपा करके हम दीनों की प्रार्थना सुन लीजिए। जो भी प्राणी रात-दिन आपका निष्काम ध्यान करता है, संसार में उसके समान धन्य और श्रेष्ठ भक्त दूसरा कोई नहीं होता।

२. ध्यान धरें शिवजी मन मांही। ब्रह्मा, इन्द्र पार नहीं पाहीं॥
दूत तुम्हार वीर हनुमाना। जासु प्रभाव तिहुं पुर जाना॥
भावार्थ: स्वयं देवाधिदेव महादेव शिव जी अपने हृदय में निरन्तर आपके ही पावन स्वरूप का ध्यान धरते हैं। ब्रह्मा और इन्द्र जैसे श्रेष्ठ देवता भी आपकी महिमा का पार नहीं पा सकते। महावीर हनुमान जी आपके अनन्य दूत हैं, जिनके अतुलित बल और पराक्रम का डंका तीनों लोकों में बजता है।

३. जय, जय, जय रघुनाथ कृपाला। सदा करो संतन प्रतिपाला॥
तुव भुजदण्ड प्रचण्ड कृपाला। रावण मारि सुरन प्रतिपाला॥
भावार्थ: हे कृपालु श्री रघुनाथ जी! आपकी सदा जय हो, जय हो, जय हो! आप सदैव साधु-संतों और सज्जनों का प्रतिपालन करते हैं। आपकी विशाल एवं प्रचण्ड भुजाओं ने दुष्ट रावण का वध कर समस्त देवताओं और धर्म की रक्षा की।

४. तुम अनाथ के नाथ गोसाईं। दीनन के हो सदा सहाई॥
ब्रह्मादिक तव पार न पावैं। सदा ईश तुम्हरो यश गावैं॥
भावार्थ: हे स्वामी! आप अनाथों के एकमात्र नाथ और दीन-दुखियों के सदा सहायक हैं। ब्रह्मा आदि देवता भी आपके दिव्य स्वरूप का अंत नहीं पा सकते, और भगवान शंकर (ईश) स्वयं सदा आपका ही यशोगान करते रहते हैं।

५. चारिउ भेद भरत हैं साखी। तुम भक्तन की लज्जा राखी॥
गुण गावत शारद मन माहीं। सुरपति ताको पार न पाहिं॥
भावार्थ: चारों वेद साक्षी हैं कि आपने संकट के समय सदैव अपने अनन्य भक्तों की लज्जा और मान की रक्षा की है। माता सरस्वती अपने मन में आपके अनन्त गुणों का गान करती हैं, फिर भी देवराज इन्द्र आपके गुणों की थाह नहीं पा सकते।

६. नाम तुम्हार लेत जो कोई। ता सम धन्य और नहीं होई॥
राम नाम है अपरम्पारा। चारिहु वेदन जाहि पुकारा॥
भावार्थ: जो मनुष्य प्रेमपूर्वक केवल आपके 'राम' नाम का उच्चारण करता है, उसके समान परम सौभाग्यशाली और धन्य कोई नहीं है। श्री राम नाम की महिमा अपरम्पार और असीम है, जिसका उद्घोष चारों वेदों ने मुक्तकंठ से किया है।

७. गणपति नाम तुम्हारो लीन्हो। तिनको प्रथम पूज्य तुम कीन्हो॥
शेष रटत नित नाम तुम्हारा। महि को भार शीश पर धारा॥
भावार्थ: प्रथम पूज्य श्री गणेश जी ने जब आपके पावन नाम का स्मरण किया, तो आपने उन्हें सभी देवताओं में 'प्रथम पूज्य' होने का सर्वोच्च वरदान दिया। शेषनाग जी निरन्तर आपके नाम की रट लगाए रहते हैं, इसी सामर्थ्य से वे सम्पूर्ण पृथ्वी का भार अपने शीश पर धारण किए हुए हैं।

८. फूल समान रहत सो भारा। पावत कोऊ न तुम्हरो पारा॥
भरत नाम तुम्हरो उर धारो। तासों कबहूं न रण में हारो॥
भावार्थ: आपके नाम के प्रभाव से शेषजी को पृथ्वी का वह विशाल भार भी एक फूल के समान अत्यंत हल्का प्रतीत होता है। आपके परम प्रिय भाई भरत जी ने आपके नाम को हृदय में धारण किया, जिसके कारण वे कभी किसी भी युद्ध में पराजित नहीं हुए।

९. नाम शत्रुहन हृदय प्रकाशा। सुमिरत होत शत्रु कर नाशा॥
लखन तुम्हारे आज्ञाकारी। सदा करत सन्तन रखवारी॥
भावार्थ: शत्रुघ्न जी के हृदय में भी आपका ही पावन नाम प्रकाशित रहता है, जिसका स्मरण करने मात्र से समस्त बाह्य और आंतरिक (काम-क्रोध आदि) शत्रुओं का तत्काल विनाश हो जाता है। वीर लक्ष्मण जी आपके आज्ञाकारी अनुज हैं, जो सदैव संतों और धर्म की रक्षा में तत्पर रहते हैं।

१०. ताते रण जीते नहिं कोई। युद्ध जुरे यमहूं किन होई॥
महालक्ष्मी धर अवतारा। सब विधि करत पाप को छारा॥
भावार्थ: लक्ष्मण जी को युद्ध में कोई भी नहीं हरा सकता, चाहे साक्षात् यमराज ही युद्ध करने क्यों न आ जाएं। साक्षात् महालक्ष्मी जी ने आपके साथ अवतरित होकर समस्त जगत के पापों और तापों को भस्म कर दिया।

११. सीता राम पुनीता गायो। भुवनेश्वरी प्रभाव दिखायो॥
घट सों प्रकट भई सो आई। जाको देखत चन्द्र लजाई॥
भावार्थ: संतों ने 'सीताराम' नाम की परम पावन महिमा गाई है, जिन्होंने भुवनेश्वरी जगदम्बा का दिव्य प्रभाव प्रकट किया। माता जानकी पृथ्वी के घट से प्रकट होकर आईं, जिनके अलौकिक सौंदर्य और तेज को देखकर चन्द्रमा भी लज्जित हो जाता है।

१२. जो तुम्हरे नित पांव पलोटत। नवो निद्धि चरणन में लोटत॥
सिद्धि अठारह मंगलकारी। सो तुम पर जावै बलिहारी॥
भावार्थ: माता जानकी जो निरन्तर आपके चरण-कमलों की सेवा करती हैं, उनके चरणों में नवों निधियां सदा लोटती रहती हैं। समस्त मंगल करने वाली अठारह सिद्धियां आप प्रभु के युगल चरणों पर न्योछावर हैं।

१३. औरहु जो अनेक प्रभुताई। सो सीतापति तुमहिं बनाई॥
इच्छा ते कोटिन संसारा। रचत न लागत पल की बारा॥
भावार्थ: संसार में जितनी भी प्रभुता और ऐश्वर्य हैं, वह सब हे जानकीनाथ! आपने ही निर्मित किए हैं। आपकी केवल एक इच्छा मात्र से करोड़ों ब्रह्माण्डों की रचना हो जाती है, जिसमें एक पल का भी विलंब नहीं लगता।

१४. जो तुम्हरे चरणन चित लावै। ताकी मुक्ति अवसि हो जावै॥
सुनहु राम तुम तात हमारे। तुमहिं भरत कुल पूज्य प्रचारे॥
भावार्थ: जो मनुष्य आपके युगल चरणों में अपना चित्त लगाता है, उसकी संसार-बंधन से मुक्ति निश्चित रूप से हो जाती है। हे श्री राम! आप ही हमारे पिता (तात) हैं, और सम्पूर्ण भारतवर्ष में आप ही परम पूज्य रूप में प्रतिष्ठित हैं।

१५. तुमहिं देव कुल देव हमारे। तुम गुरु देव प्राण के प्यारे॥
जो कुछ हो सो तुमहिं राजा। जय जय जय प्रभु राखो लाजा॥
भावार्थ: आप ही हमारे कुलदेवता हैं, आप ही हमारे गुरुदेव हैं और आप ही प्राणों से भी अधिक प्रिय हैं। हमारे जो कुछ भी हैं—स्वामी, राजा, रक्षक—सब आप ही हैं। हे प्रभु! आपकी सदा जय हो, आप हमारी लाज रखिए।

१६. राम आत्मा पोषण हारे। जय जय जय दशरथ के प्यारे॥
जय जय जय प्रभु ज्योति स्वरुपा। नर्गुण ब्रहृ अखण्ड अनूपा॥
भावार्थ: हे श्री राम! आप समस्त जीवों की आत्मा का पोषण करने वाले हैं। हे महाराज दशरथ के प्राणप्रिय राजकुमार! आपकी सदा जय हो। हे प्रभु! आप साक्षात् ज्योति-स्वरूप, निर्गुण, अखण्ड, अनुपम और परब्रह्म परमात्मा हैं।

१७. सत्य सत्य जय सत्यव्रत स्वामी। सत्य सनातन अन्तर्यामी॥
सत्य भजन तुम्हरो जो गावै। सो निश्चय चारों फल पावै॥
भावार्थ: आप सत्यव्रत के स्वामी, त्रिकाल सत्य, सनातन परमात्मा और सबके अंतर्यामी हैं। जो मनुष्य सत्य भाव से आपका भजन-कीर्तन करता है, वह निश्चित ही धर्म, अर्थ, काम और मोक्ष—इन चारों फलों को प्राप्त करता है।

१८. सत्य शपथ गौरीपति कीन्हीं। तुमने भक्तिहिं सब सिधि दीन्हीं॥
ज्ञान हृदय दो ज्ञान स्वरुपा। नमो नमो जय जगपति भूपा॥
भावार्थ: भगवान शिव (गौरीपति) ने सत्य शपथपूर्वक कहा है कि आपने अनन्य भक्तों को समस्त सिद्धियां सहज ही प्रदान कर दी हैं। हे ज्ञानस्वरूप प्रभु! हमारे हृदय में दिव्य ज्ञान प्रदान कीजिए। हे सम्पूर्ण जगत के स्वामी और राजाओं के राजा! आपको बारम्बार नमन है।

१९. धन्य धन्य तुम धन्य प्रतापा। नाम तुम्हार हरत संतापा॥
सत्य शुद्ध देवन मुख गाया। बजी दुन्दुभी शंख बजाया॥
भावार्थ: हे प्रभु! आपका प्रताप और ऐश्वर्य धन्य है। आपका पावन नाम स्मरण करते ही भक्तों के समस्त त्रिविध संताप मिट जाते हैं। समस्त देवताओं ने अपने मुख से आपके सत्य और पावन चरित्र का गान किया है और आकाश में दिव्य दुन्दुभियां व शंख बजाए हैं।

२०. सत्य सत्य तुम सत्य सनातन। तुम ही हो हमरे तन-मन धन॥
याको पाठ करे जो कोई। ज्ञान प्रकट ताके उर होई॥
भावार्थ: आप ही परम सत्य, अनादि और सनातन परमात्मा हैं। आप ही हमारे तन, मन और वास्तविक धन हैं। जो भी भक्त इस पावन चालीसा का पाठ करता है, उसके हृदय में साक्षात् आत्म-ज्ञान प्रकट हो जाता है।

२१. आवागमन मिटै तिहि केरा। सत्य वचन माने शिव मेरा॥
और आस मन में जो होई। मनवांछित फल पावे सोई॥
भावार्थ: उस साधक का जन्म-मरण का आवागमन मिट जाता है, यह भगवान शिव का वचन है जो पूर्णतः सत्य है। इसके अतिरिक्त साधक के मन में जो भी धर्मयुक्त कामना होती है, वह सम्पूर्ण मनोवांछित फल प्राप्त कर लेता है।

२२. तीनहुं काल ध्यान जो ल्यावै। तुलसी दल अरु फूल चढ़ावै॥
साग पत्र सो भोग लगावै। सो नर सकल सिद्धता पावै॥
भावार्थ: जो त्रिकाल (प्रातः, मध्याह्न, सायं) प्रभु का ध्यान करता है, श्रद्धा से तुलसी दल व पुष्प अर्पित करता है और प्रेमपूर्वक सात्विक शाक-पत्र या फल का भोग लगाता है, वह मनुष्य समस्त सिद्धियों को प्राप्त कर लेता है।

२३. अन्त समय रघुबर पुर जाई। जहां जन्म हरि भक्त कहाई॥
श्री हरिदास कहै अरु गावै। सो बैकुण्ठ धाम को पावै॥
भावार्थ: अंत समय में वह साधक श्री रघुनाथ जी के परम धाम (साकेत / वैकुंठ) को जाता है, जहाँ वह भगवान का नित्य पार्षद बनकर रहता है। भक्त हरिदास जी कहते हैं कि जो इस चरित्र का गान करता है, वह निश्चित ही वैकुंठ धाम को प्राप्त करता है।

【समापन दोहे — भावार्थ】
दोहा १:
सात दिवस जो नेम कर, पाठ करे चित लाय।
हरिदास हरि कृपा से, अवसि भक्ति को पाय॥
भावार्थ: जो भी मनुष्य सात दिनों तक नियमपूर्वक एकाग्रचित्त होकर इस पावन चालीसा का पाठ करता है, श्री हरिदास जी कहते हैं कि भगवान श्री राम की कृपा से उसे अनन्य भगवद्भक्ति अवश्य प्राप्त होती है।

दोहा २:
राम चालीसा जो पढ़े, राम चरण चित लाय।
जो इच्छा मन में करै, सकल सिद्ध हो जाय॥
भावार्थ: जो भी साधक श्री रामचन्द्र जी के चरण-कमलों में मन लगाकर इस श्री राम चालीसा का पाठ करता है, वह मन में जिस किसी भी शुभ कार्य की कामना करता है, उसके वे सभी कार्य सिद्ध हो जाते हैं।"""

# 3. Authentic Worship Procedure & Rules (शास्त्रोक्त पाठ विधि व नियम)
rama_chalisa_vidhi = """॥ श्री राम चालीसा पाठ एवं पूजन विधि व नियम ॥

१. पावन काल व शुभ मुहूर्त:
• प्रतिदिन प्रातःकाल ब्रह्ममुहूर्त अथवा संध्याकाल में श्री राम चालीसा का पाठ सर्वोत्तम है।
• विशेष रूप से चैत्र शुक्ल नवमी (श्री रामनवमी), मार्गशीर्ष शुक्ल पंचमी (श्री राम-विवाह पंचमी), आश्विन शुक्ल दशमी (विजयादशमी), प्रत्येक मंगलवार व रविवार, तथा हनुमान जयंती के दिन इसका पाठ अनंत गुना फलदायी माना गया है।

२. आवश्यक पूजन सामग्री:
• श्री राम दरबार का पावन चित्र या विग्रह (जिसमें श्री राम, सीता जी, लक्ष्मण जी, भरत-शत्रुघ्न जी और हनुमान जी हों)।
• शुद्ध गाय के घी का दीपक, धूपबत्ती, रोली, कुमकुम, अक्षत (अखंड चावल), पीला चंदन।
• तुलसी दल (अत्यंत अनिवार्य - भगवान श्री राम बिना तुलसी के भोग स्वीकार नहीं करते)।
• पीले पुष्प, गेंदे के फूलों की माला, इत्र।
• नैवेद्य: ताजे मौसमी फल, खीर, पंचामृत, पेड़ा अथवा सात्विक मिष्ठान।

३. पूजन विधान:
• स्नानादि से पवित्र होकर पीले या श्वेत स्वच्छ वस्त्र धारण करें।
• पूर्व अथवा उत्तर दिशा की ओर मुख करके कुशा या ऊन के आसन पर बैठें।
• सम्मुख पाटे पर पीला या लाल वस्त्र बिछाकर श्री राम दरबार की स्थापना करें।
• सर्वप्रथत घी का दीपक प्रज्वलित करें और श्री गणेश जी एवं हनुमान जी का स्मरण करें।
• प्रभु श्री राम को पंचामृत व गंगाजल से प्रतीकात्मक स्नान कराएं, पीला चंदन लगाएं और तुलसी दल सहित पुष्प अर्पित करें।
• आचमन कर हाथ में जल, अक्षत व पुष्प लेकर संकल्प लें और अत्यंत श्रद्धा व भक्ति से श्री राम चालीसा का पाठ करें।
• पाठ के उपरांत 'ॐ श्री रामाय नमः' अथवा 'श्री राम जय राम जय जय राम' महामंत्र का १०८ बार जप करें तथा श्री राम जी की आरती करें।

४. सात दिवसीय अनुष्ठान नियम:
'सात दिवस जो नेम कर, पाठ करे चित लाय।'
• किसी विशेष मनोकामना की पूर्ति हेतु लगातार ७ दिनों तक एक निश्चित समय पर नित्य ७, ११ या २१ बार चालीसा का पाठ करें।
• अनुष्ठान के दौरान सात्विक आहार लें, ब्रह्मचर्य का पालन करें तथा असत्य व कटु वचनों से दूर रहें।"""

# 4. Spiritual Significance & Fruits (आध्यात्मिक महत्त्व व फलश्रुति)
rama_chalisa_significance = """॥ श्री राम चालीसा का आध्यात्मिक महत्त्व व फलश्रुति ॥

१. तारक महामंत्र का प्रभाव:
'राम नाम है अपरम्पारा। चारिहु वेदन जाहि पुकारा॥'
'राम' नाम समस्त वेदों का सार और साक्षात् तारक ब्रह्म है। इस चालीसा के नित्य पाठ से अंतःकरण के समस्त पाप, विकार और संताप जलकर भस्म हो जाते हैं।

२. समस्त शत्रुओं व भय का नाश:
'सुमिरत होत शत्रु कर नाशा। सदा करत सन्तन रखवारी॥'
श्री राम चालीसा का पाठ करने वाले साधक की रक्षा स्वयं महावीर हनुमान जी और लक्ष्मण जी करते हैं। साधक के बाह्य शत्रुओं का शमन होता है तथा काम, क्रोध, मद, लोभ रूपी आंतरिक शत्रुओं पर विजय प्राप्त होती है।

३. चारों पुरुषार्थों की सुलभ प्राप्ति:
'सत्य भजन तुम्हरो जो गावै। सो निश्चय चारों फल पावै॥'
भगवान श्री राम की कृपा से मनुष्य को जीवन में धर्म, अर्थ, काम और अंत में मोक्ष—इन चारों पुरुषार्थों की सहज प्राप्ति होती है।

४. अष्ट-सिद्धि व नव-निधि का आशीर्वाद:
'नवो निद्धि चरणन में लोटत। सिद्धि अठारह मंगलकारी॥'
माँ जानकी और प्रभु श्री राम की कृपा से घर-परिवार में दरिद्रता का नाश होता है, सुख-समृद्धि, उत्तम स्वास्थ्य और ऐश्वर्य का वास होता है।

५. जन्म-मरण के बंधन से मुक्ति:
'आवागमन मिटै तिहि केरा। सो बैकुण्ठ धाम को पावै॥'
देवाधिदेव महादेव शिव जी की साक्षी में यह सत्य प्रतिज्ञा है कि जो श्रद्धापूर्वक श्री राम चालीसा का अनुष्ठान करता है, उसका भवबंधन कट जाता है और अंत समय में उसे परम पद श्री वैकुंठ (साकेत) धाम की प्राप्ति होती है।"""

# 5. English Transliteration (रोमन लिप्यंतरण)
rama_chalisa_en = """॥ Shri Rama Chalisa ॥

॥ Chaupai ॥
Shri Raghubira Bhakta Hitakari। Suni Lijai Prabhu Araja Hamari॥
Nishi Dina Dhyana Dharai Jo Koi। Ta Sama Bhakta Aura Nahin Hoi॥

Dhyana Dharen Shivaji Mana Manhin। Brahma, Indra Para Nahin Pahin॥
Duta Tumhara Vira Hanumana। Jasu Prabhava Tihu Pura Jana॥

Jai, Jai, Jai Raghunatha Kripala। Sada Karo Santana Pratipala॥
Tuva Bhujadanda Prachanda Kripala। Ravana Mari Surana Pratipala॥

Tuma Anatha Ke Natha Gosain। Dinana Ke Ho Sada Sahai॥
Brahmadika Tava Para Na Pavain। Sada Isha Tumharo Yasha Gavain॥

Chariu Bheda Bharata Hain Sakhi। Tuma Bhaktana Ki Lajja Rakhi॥
Guna Gavata Sharada Mana Mahin। Surapati Tako Para Na Pahin॥

Nama Tumhara Leta Jo Koi। Ta Sama Dhanya Aura Nahin Hoi॥
Rama Nama Hai Aparampara। Charihu Vedana Jahi Pukara॥

Ganapati Nama Tumharo Linho। Tinako Prathama Pujya Tuma Kinho॥
Shesha Ratata Nita Nama Tumhara। Mahi Ko Bhara Shisha Para Dhara॥

Phula Samana Rahata So Bhara। Pavata Kou Na Tumharo Para॥
Bharata Nama Tumharo Ura Dharo। Tason Kabahun Na Rana Mein Haro॥

Nama Shatruhana Hridaya Prakasha। Sumirata Hota Shatru Kara Nasha॥
Lakhana Tumhare Agyakari। Sada Karata Santana Rakhavari॥

Tate Rana Jite Nahin Koi। Yuddha Jure Yamahun Kina Hoi॥
Mahalakshmi Dhara Avatara। Saba Vidhi Karata Papa Ko Chhara॥

Sita Rama Punita Gayo। Bhuvaneshvari Prabhava Dikhayo॥
Ghata Son Prakata Bhai So Aai। Jako Dekhata Chandra Lajai॥

Jo Tumhare Nita Panva Palotata। Navo Niddhi Charanana Mein Lotata॥
Siddhi Atharaha Mangalakari। So Tuma Para Javai Balihari॥

Aúrahu Jo Aneka Prabhutai। So Sitapati Tumhin Banai॥
Ichchha Te Kotina Sansara। Rachata Na Lagata Pala Ki Bara॥

Jo Tumhare Charanana Chita Lavai। Taki Mukti Avasi Ho Javai॥
Sunahu Rama Tuma Tata Hamare। Tumhin Bharata Kula Pujya Prachare॥

Tumhin Deva Kula Deva Hamare। Tuma Guru Deva Prana Ke Pyare॥
Jo Kuchha Ho So Tumhin Raja। Jai Jai Jai Prabhu Rakho Laja॥

Rama Atma Poshana Hare। Jai Jai Jai Dasharatha Ke Pyare॥
Jai Jai Jai Prabhu Jyoti Svarupa। Nirguna Brahma Akhanda Anupa॥

Satya Satya Jai Satyavrata Swami। Satya Sanatana Antaryami॥
Satya Bhajana Tumharo Jo Gavai। So Nishchaya Charo Phala Pavai॥

Satya Shapatha Gauripati Kinhi। Tumane Bhaktihi Saba Sidhi Dinhi॥
Gyana Hridaya Do Gyana Svarupa। Namo Namo Jai Jagapati Bhupa॥

Dhanya Dhanya Tuma Dhanya Pratapa। Nama Tumhara Harata Santapa॥
Satya Shuddha Devana Mukha Gaya। Baji Dundubhi Shankha Bajaya॥

Satya Satya Tuma Satya Sanatana। Tuma Hi Ho Hamare Tana-Mana Dhana॥
Yako Patha Kare Jo Koi। Gyana Prakata Take Ura Hoi॥

Avagamana Mitai Tihi Kera। Satya Vachana Mane Shiva Mera॥
Aura Asa Mana Mein Jo Hoi। Manavanchhita Phala Pave Soi॥

Tinahun Kala Dhyana Jo Lyavai। Tulasi Dala Aru Phula Chadhavai॥
Saga Patra So Bhoga Lagavai। So Nara Sakala Siddhata Pavai॥

Anta Samaya Raghubara Pura Jai। Jahan Janma Hari Bhakta Kahai॥
Shri Haridasa Kahai Aru Gavai। So Baikuntha Dhama Ko Pavai॥

॥ Doha ॥
Sata Divasa Jo Nema Kara, Patha Kare Chita Laya।
Haridasa Hari Kripa Se, Avasi Bhakti Ko Paya॥

Rama Chalisa Jo Padhe, Rama Charana Chita Laya।
Jo Ichchha Mana Mein Karai, Sakala Siddha Ho Jaya॥"""

# 6. Update drik_chalisa_collections.json
with open('drik_chalisa_collections.json', encoding='utf-8') as f:
    chalisa_data = json.load(f)

rama_items = chalisa_data['rama']['items']
target_item = None
for item in rama_items:
    if item['id'] == 'drik_chalisa_9':
        target_item = item
        break

if target_item:
    target_item['title'] = 'श्री राम चालीसा'
    target_item['title_en'] = 'Shri Rama Chalisa'
    target_item['en_line'] = 'Shri Raghubira Bhakta Hitakari'
    target_item['hi_line'] = 'श्री रघुवीर भक्त हितकारी'
    target_item['sub'] = 'श्री रघुवीर भक्त हितकारी • Drik Panchang Verified'
    target_item['thumb'] = 'assets/gallery/bal_rama_little.jpg'
    target_item['audio_url'] = 'https://www.youtube.com/watch?v=dnpi8ZcakL8'
    target_item['video_id'] = 'dnpi8ZcakL8'
    target_item['drik_url'] = 'https://www.drikpanchang.com/lyrics/chalisa/lord-rama/shree-rama-chalisa.html?lang=hi&ck=1'
    target_item['source'] = 'Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)'
    target_item['content'] = rama_chalisa_content
    target_item['meaning'] = rama_chalisa_meaning
    target_item['vidhi'] = rama_chalisa_vidhi
    target_item['significance'] = rama_chalisa_significance
    target_item['english_lyrics'] = rama_chalisa_en
    print("Updated drik_chalisa_9 in drik_chalisa_collections.json!")
else:
    print("ERROR: drik_chalisa_9 not found in rama items!")

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

# Add or update chalisa_ram in CONTENT in app.js
c_ram_record = f"""chalisa_ram: {{
    title: 'श्री राम चालीसा',
    deity: 'मर्यादा पुरुषोत्तम भगवान श्री राम',
    mantra: '॥ ॐ श्री रामाय नमः • श्री राम जय राम जय जय राम ॥',
    text: `{rama_chalisa_content}`,
    meaning: `{rama_chalisa_meaning}`,
    vidhi: `{rama_chalisa_vidhi}`,
    significance: `{rama_chalisa_significance}`,
    english_lyrics: `{rama_chalisa_en}`,
    audio_url: 'https://www.youtube.com/watch?v=dnpi8ZcakL8',
    video_id: 'dnpi8ZcakL8',
    thumb: 'assets/gallery/bal_rama_little.jpg',
    drik_url: 'https://www.drikpanchang.com/lyrics/chalisa/lord-rama/shree-rama-chalisa.html?lang=hi&ck=1'
  }},
  """

if 'chalisa_ram:' in app_js:
    pos_r = app_js.find('chalisa_ram:')
    pos_next = app_js.find('chalisa_parashurama:', pos_r)
    if pos_next != -1:
        app_js = app_js[:pos_r] + c_ram_record + app_js[pos_next:]
        print("Replaced existing chalisa_ram in CONTENT!")
    else:
        print("Notice: chalisa_parashurama not found after chalisa_ram")
else:
    pos_target = app_js.find('chalisa_parashurama:')
    if pos_target != -1:
        app_js = app_js[:pos_target] + c_ram_record + app_js[pos_target:]
        print("Inserted chalisa_ram before chalisa_parashurama in CONTENT!")
    else:
        print("ERROR: chalisa_parashurama not found in CONTENT!")

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
