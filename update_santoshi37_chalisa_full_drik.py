import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री संतोषी माता चालीसा ॥

॥ दोहा ॥
श्री गणपति पद नाय सिर, धरि हिय शारदा ध्यान।
सन्तोषी मां की करुँ, कीरति सकल बखान॥

॥ चौपाई ॥
जय संतोषी मां जग जननी। खल मति दुष्ट दैत्य दल हननी॥१॥
गणपति देव तुम्हारे ताता। रिद्धि सिद्धि कहलावहं माता॥२॥
माता-पिता की रहौ दुलारी। कीरति केहि विधि कहुं तुम्हारी॥३॥
क्रीट मुकुट सिर अनुपम भारी। कानन कुण्डल को छवि न्यारी॥४॥
सोहत अंग छटा छवि प्यारी। सुन्दर चीर सुनहरी धारी॥५॥
आप चतुर्भुज सुघड़ विशाला। धारण करहु गले वन माला॥६॥
निकट है गौ अमित दुलारी। करहु मयूर आप असवारी॥७॥
जानत सबही आप प्रभुताई। सुर नर मुनि सब करहिं बड़ाई॥८॥
तुम्हरे दरश करत क्षण माई। दुख दरिद्र सब जाय नसाई॥९॥
वेद पुराण रहे यश गाई। करहु भक्त की आप सहाई॥१०॥
ब्रह्मा ढिंग सरस्वती कहाई। लक्ष्मी रूप विष्णु ढिंग आई॥११॥
शिव ढिंग गिरजा रूप बिराजी। महिमा तीनों लोक में गाजी॥१२॥
शक्ति रूप प्रगटी जन जानी। रुद्र रूप भई मात भवानी॥१३॥
दुष्टदलन हित प्रगटी काली। जगमग ज्योति प्रचंड निराली॥१४॥
चण्ड मुण्ड महिषासुर मारे। शुम्भ निशुम्भ असुर हनि डारे॥१५॥
महिमा वेद पुरनान बरनी। निज भक्तन के संकट हरनी॥१६॥
रूप शारदा हंस मोहिनी। निरंकार साकार दाहिनी॥१७॥
प्रगटाई चहुंदिश निज माया। कण कण में है तेज समाया॥१८॥
पृथ्वी सूर्य चन्द्र अरु तारे। तव इंगित क्रम बद्ध हैं सारे॥१९॥
पालन पोषण तुमहीं करता। क्षण भंगुर में प्राण हरता॥२०॥
ब्रह्मा विष्णु तुम्हें नित ध्यावैं। शेष महेश सदा मन लावे॥२१॥
मनोकમના पूरण करनी। पाप काटनी भव भय तरनी॥२२॥
चित्त लगाय तुम्हें जो ध्याता। सो नर सुख सम्पत्ति है पाता॥२३॥
बन्ध्या नारि तुमहिं जो ध्यावैं। पुत्र पुष्प लता सम वह पावैं॥२४॥
पति वियोगी अति व्याकुलनारी। तुम वियोग अति व्याकुलयारी॥२५॥
कन्या जो कोइ तुमको ध्यावै। अपना मन वांछित वर पावै॥२६॥
शीलवान गुणवान हो मैया। अपने जन की नाव खिवैया॥२७॥
विधि पूर्वक व्रत जो कोई करहीं। ताहि अमित सुख संपत्ति भरहीं॥२८॥
गुड़ और चना भोग तोहि भावै। सेवा करै सो आनंद पावै॥२९॥
श्रद्धा युक्त ध्यान जो धरहीं। सो नर निश्चय भव सों तरहीं॥३०॥
उद्यापन जो करहि तुम्हारा। ताको सहज करहु निस्तारा॥३१॥
नारि सुहागिन व्रत जो करती। सुख सम्पत्ति सों गोदी भरती॥३२॥
जो सुमिरत जैसी मन भावा। सो नर वैसो ही फल पावा॥३३॥
सात शुक्र जो व्रत मन धारे। ताके पूर्ण मनोरथ सारे॥३४॥
सेवा करहि भक्ति युत जोई। ताको दूर दरिद्र दुख होई॥३५॥
जो जन शरण माता तेरी आवै। ताके क्षण में काज बनावै॥३६॥
जय जय जय अम्बे कल्यानी। कृपा करौ मोरी महारानी॥३७॥
जो कोई पढ़ै मात चालीसा। तापे करहिं कृपा जगदीशा॥३८॥
नित प्रति पाठ करै इक बारा। सो नर रहै तुम्हारा प्यारा॥३९॥
नाम लेत ब्याधा सब भागे। रोग दोष कबहूँ नहीं लागे॥४०॥

॥ दोहा ॥
सन्तोषी माँ के सदा, बन्दहुँ पग निश वास।
पूर्ण मनोरथ हों सकल, मात हरौ भव त्रास॥"""

meaning = """॥ श्री संतोषी माता चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहा】
• "श्री गणपति पद नाय सिर, धरि हिय शारदा ध्यान। सन्तोषी मां की करुँ, कीरति सकल बखान॥"
भावार्थ: प्रथम पूज्य भगवान श्री गणेश जी के पावन चरणों में शीश नवाकर और हृदय में विद्यादात्री माँ सरस्वती (शारदा) का ध्यान धरकर, मैं समस्त मनोरथ पूर्ण करने वाली करुणामयी माँ संतोषी के पावन सुयश और महिमा का श्रद्धापूर्वक बखान करता हूँ।

【चौपाइयां — पद्यवार भावार्थ】
१-१०. "जय संतोषी मां जग जननी... करहु भक्त की आप सहाई॥"
भावार्थ: हे संपूर्ण चराचर जगत की जननी माँ संतोषी! आपकी सदा-सर्वदा जय हो; आप दुष्टों और आसुरी शक्तियों के दलों का संहार करने वाली हैं। विघ्नहर्ता भगवान श्री गणेश जी आपके पूज्य पिता हैं और रिद्धि-सिद्धि आपकी माताएं हैं। आप अपने माता-पिता की अत्यंत लाड़ली और दुलारी पुत्री हैं; आपकी अगाध महिमा का वर्णन कोई किस प्रकार कर सकता है? आपके पावन मस्तक पर अत्यंत अनुपम, स्वर्ण-जड़ित भारी मुकुट शोभायमान है और आपके कानों में दिव्य कुण्डलों की छटा अत्यंत निराली है। आपके सुकोमल अंगों पर सुनहरी किनारी वाली सुंदर लाल साड़ी और अलौकिक कांति सुशोभित है। आप चार भुजाओं वाली (चतुर्भुजा) हैं, जिनका सुघड़ रूप अत्यंत विशाल व मनोहारी है और आपने अपने कंठ में सुगंधित वनमाला धारण की हुई है। आपके समीप आपकी परम दुलारी गौमाता स्थित है और आप मयूर (मोर) की दिव्य सवारी करती हैं। आपकी अतुलित प्रभुता व ईश्वरीय शक्ति को सभी जानते हैं; देवता, मनुष्य और मुनिगण निरंतर आपकी स्तुति करते हैं। हे मैया! आपके दिव्य दर्शन प्राप्त होते ही जीवन के समस्त दुख और दारिद्र्य क्षण भर में नष्ट हो जाते हैं। चारों वेद और पुराण आपके यश का गान करते हैं; हे माँ! आप अपने प्रत्येक अनन्य भक्त की सदा सहायिका बनती हैं।

११-२०. "ब्रह्मा ढिंग सरस्वती कहाई... क्षण भंगुर में प्राण हरता॥"
भावार्थ: आप ही ब्रह्मदेव के समीप ज्ञानस्वरूपा सरस्वती कहलाती हैं, आप ही भगवान श्रीहरि विष्णु के समीप महालक्ष्मी रूप में विराजती हैं। भगवान शिव के समीप आप ही गिरिराज किशोरी गिरिजा (पार्वती) के रूप में प्रतिष्ठित हैं; आपकी अगाध महिमा तीनों लोकों में गूंजती है। जब-जब भक्तों ने पुकारा, आप ही पराशक्ति रूप में प्रकट हुईं और संहार के समय भवानी रुद्ररूपा बन गईं। दुष्टों और असुरों का दलन करने हेतु प्रचंड व जगमगाती ज्योति के साथ आप ही महाकाली रूप में अवतरित हुईं। आपने ही चण्ड, मुण्ड और महिषासुर का वध किया तथा शुंभ और निशुंभ जैसे महादैत्यों को रणभूमि में मार गिराया। वेदों और पुराणों ने आपकी महिमा का वर्णन करते हुए आपको अपने भक्तों के संकट हरने वाली कहा है। आप ही हंस पर विराजमान मोहिनी शारदा हैं, और आप ही निराकार परमात्मा का साकार, मंगलकारी स्वरूप हैं। आपने दसों दिशाओं में अपनी माया का विस्तार किया है और इस सृष्टि के कण-कण में आपका ही दिव्य तेज समाया हुआ है। पृथ्वी, सूर्य, चन्द्रमा और आकाश के समस्त नक्षत्र-तारे आपके ही एक संकेत (इशारे) पर क्रमबद्ध होकर नियमपूर्वक गतिमान हैं। इस चराचर जगत का पालन-पोषण करने वाली भी आप ही हैं, और संहारकाल में एक क्षण के भीतर प्राणों का हरण करने वाली भी आप ही हैं।

२१-३३. "ब्रह्मा विष्णु तुम्हें नित ध्यावैं... सो नर वैसो ही फल पावा॥"
भावार्थ: ब्रह्मा और विष्णु निरंतर आपका ध्यान करते हैं तथा शेषनाग और देवाधिदेव महादेव शिव सदा अपने मन को आपके पावन चरणों में लगाते हैं। आप अपने भक्तों की समस्त मनोकामनाओं को पूर्ण करने वाली, पापों को काटने वाली और संसार-सागर के भय से पार उतारने वाली हैं। जो भी मनुष्य एकाग्रचित्त होकर आपका ध्यान करता है, वह जीवन में विपुल सुख, शांति और धन-संपत्ति प्राप्त करता है। यदि कोई निःसंतान (वन्ध्या) स्त्री श्रद्धापूर्वक आपका ध्यान व व्रत करे, तो उसे फूलों से लदी लता के समान सुंदर व सुयोग्य पुत्र रत्न की प्राप्ति होती है। पति के वियोग या विपत्ति से व्याकुल स्त्री का संताप दूर होकर उसे पुनः अखंड सौभाग्य प्राप्त होता है। जो कुंवारी कन्या आपका ध्यान करती है, उसे मनवांछित, सुयोग्य व सुशील वर की प्राप्ति होती है। हे मैया! आप अत्यंत शीलवान और गुणवान हैं और अपने आश्रित भक्तों की जीवन-रूपी नौका की स्वयं खिवैया (पार लगाने वाली) हैं। जो भी जातक विधिपूर्वक आपके पावन शुक्रवार व्रत का पालन करता है, आप उसके जीवन को अपार सुख और संपत्ति से भर देती हैं। आपको शुद्ध गुड़ और भुने हुए चने का सरल नैवेद्य (भोग) अत्यंत प्रिय है; जो निष्काम भाव से आपकी सेवा करता है, वह परम आनंद प्राप्त करता है। श्रद्धापूर्वक आपका ध्यान करने वाला मनुष्य निश्चित रूप से इस भवसागर से तर जाता है। जो आपके व्रत का विधिपूर्वक उद्यापन करता है, आप उसका सहज ही उद्धार कर देती हैं। जो सुहागिन नारी यह व्रत करती है, उसकी गोद सदा सुख, सौभाग्य और संतान से हरी-भरी रहती है। जो मनुष्य जिस भाव से आपका स्मरण करता है, उसे वैसा ही अभीष्ट फल प्राप्त होता है।

३४-४०. "सात शुक्र जो व्रत मन धारे... रोग दोष कबहूँ नहीं लागे॥"
भावार्थ: जो मनुष्य मन में निष्ठा धारण कर लगातार सात शुक्रवार तक आपका व्रत रखता है, उसके समस्त मनोरथ निश्चित ही पूर्ण हो जाते हैं। जो भक्तिभाव से आपकी सेवा-आराधना करता है, उसके जीवन से दरिद्रता और दुख सदा के लिए दूर भाग जाते हैं। जो भी मनुष्य माँ संतोषी की शरण में आ जाता है, माँ उसके बिगड़े हुए कार्यों को क्षण भर में सिद्ध कर देती हैं। हे कल्याणकारिणी अम्बे महारानी! आपकी जय हो, जय हो, जय हो; मुझ पर अपनी अहैतुकी दया दृष्टि कीजिए। जो कोई भी माँ संतोषी की इस पावन चालीसा का श्रद्धा से पाठ करता है, उस पर साक्षात जगदीश्वर (भगवान) कृपा करते हैं। जो मनुष्य प्रतिदिन नियम से कम से कम एक बार इसका पाठ करता है, वह माँ संतोषी का अत्यंत प्रिय बन जाता है। माँ संतोषी का पावन नाम लेते ही जीवन की समस्त बाधाएं और संकट दूर भाग जाते हैं तथा कभी कोई रोग, दोष या कष्ट साधक को स्पर्श भी नहीं कर पाता।

【समापन दोहा】
• "सन्तोषी माँ के सदा, बन्दहुँ पग निश वास। पूर्ण मनोरथ हों सकल, मात हरौ भव त्रास॥"
भावार्थ: मैं दिन-रात (निशदिन) सदैव परम करुणामयी माँ संतोषी के पावन श्रीचरणों की वंदना करता हूँ। हे माता! आप हम सभी भक्तों के समस्त मनोरथ पूर्ण कीजिए और इस संसार के जन्म-मरण रूपी समस्त भयों व संतापों का समूल नाश कीजिए।"""

vidhi = """॥ श्री संतोषी माता चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल सूर्योदय वेला अथवा सांध्यकालीन आरती वेला।
- सर्वोत्तम वार: शुक्रवार (माँ संतोषी का परम पावन व्रत दिवस)।
- संकल्प व व्रत अवधि: निरंतर १६ शुक्रवार अथवा कम से कम ७ शुक्रवार तक व्रत का नियम धारण किया जाता है।
- महापर्व: चैत्र व शारदीय नवरात्रि, तथा प्रत्येक मास के शुक्ल पक्ष का शुक्रवार।

२. दिशा, आसन व वस्त्र:
- दिशा: पूर्व अथवा उत्तर-पूर्व (ईशान) दिशा की ओर मुख करके बैठें।
- आसन: लाल अथवा पीले रंग का स्वच्छ ऊनी आसन बिछाएं।
- वस्त्र: साधक को स्वच्छ लाल, पीले अथवा हल्के गुलाबी वस्त्र धारण करने चाहिए।

३. कलश, दीप व विशेष नैवेद्य:
- कलश: तांबे या पीतल के लोटे में शुद्ध जल भरकर उस पर एक कटोरी में गुड़ और भुने हुए चने रखें।
- दीपक: गाय के शुद्ध देशी घी का दीपक प्रज्वलित करें।
- प्रिय नैवेद्य: शुद्ध गुड़ और भुने हुए चने (सवा आने या सवा रुपए का गुड़-चना) माता का सर्वप्रिय भोग है। साथ ही केला, ऋतुफल और बताशे भी अर्पित किए जा सकते हैं।
- पुष्प: लाल गुलाब अथवा पीले गेंदे के ताजे पुष्प।

४. अत्यंत अनिवार्य खटाई निषेध नियम:
- संतोषी माता के व्रत और पूजा में घर के किसी भी सदस्य द्वारा खटाई (नींबू, इमली, दही, अमचूर, टमाटर, सिरका आदि) खाना अथवा किसी को देना पूर्णतया वर्जित होता है।

५. प्रामाणिक पाठ क्रम:
- आचमन, पवित्रीकरण एवं हाथ में अक्षत-पुष्प लेकर संकल्प करें।
- गणेश जी एवं माँ संतोषी का ध्यान करें: 'ॐ श्री संतोषी देव्यै नमः'।
- माँ संतोषी के मन्त्र: 'ॐ श्रीं संतोषी महादेव्यै नमः' का १०८ बार जप करें।
- इसके पश्चात शांत चित्त होकर 'श्री संतोषी माता चालीसा' का १, ३ अथवा ७ बार पाठ करें।
- पाठ उपरांत आरती करें, गुड़-चने का प्रसाद बांटें और स्वयं भी गुड़-चना व फलाहार/अन्न ग्रहण करें।
- उद्यापन के दिन आठ बालकों (लड़कों) को भोजन कराएं और उन्हें खटाई वाली कोई वस्तु कदापि न दें।"""

significance = """॥ श्री संतोषी माता चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. मन में परम शांति व संतोष की प्राप्ति:
"जय संतोषी मां जग जननी... सो नर सुख सम्पत्ति है पाता॥"
माँ संतोषी की आराधना से तृष्णा, मानसिक अशांति, ईर्ष्या और तनाव का शमन होता है तथा हृदय में सच्ची तृप्ति और परम संतोष की अनुभूति होती है।

२. दरिद्रता नाश व सुख-समृद्धि:
"सेवा करहि भक्ति युत जोई। ताको दूर दरिद्र दुख होई॥"
आर्थिक संकट, कर्ज और विपन्नता दूर होकर घर में धन-धान्य और लक्ष्मी का स्थाई वास होता है।

३. सुयोग्य वर एवं अखण्ड सौभाग्य प्राप्ति:
"कन्या जो कोइ तुमको ध्यावै। अपना मन वांछित वर पावै॥ नारि सुहागिन व्रत जो करती। सुख सम्पत्ति सों गोदी भरती॥"
कुंवारी कन्याओं को मनवांछित जीवनसाथी मिलता है और सुहागिन महिलाओं को अखंड सौभाग्य व पति-सुख की प्राप्ति होती है।

४. संतान सुख व वन्ध्या दोष निवारण:
"बन्ध्या नारि तुमहिं जो ध्यावैं। पुत्र पुष्प लता सम वह पावैं॥"
संतानहीन दंपतियों को सुयोग्य, संस्कारी और दीर्घायु संतान की प्राप्ति होती है।

५. सर्वकार्य सिद्धि एवं ग्रह-बाधा शांति:
"सात शुक्र जो व्रत मन धारे। ताके पूर्ण मनोरथ सारे॥"
शुक्रवार व्रत एवं चालीसा पाठ से शुक्र ग्रह के दोष शांत होते हैं और अटके हुए सभी कार्य सिद्ध होते हैं।"""

english_lyrics = """॥ Shri Santoshi Mata Chalisa ॥

॥ Doha ॥
Shree Ganapati Pada Naaya Sira, Dhari Hiya Shaaradaa Dhyaana।
Santawshee Maan Kee Karun, Keerati Sakala Bakhaana॥

॥ Chaupai ॥
Jaya Santoshee Maan Jaga Jananee। Khala Mati Dushta Daitya Dala Hananee॥1॥
Ganapati Deva Tumhaare Taataa। Riddhi Siddhi Kahalaavahan Maataa॥2॥
Maataa-Pitaa Kee Rahau Dulaaree। Keerati Kehi Vidhi Kahun Tumhaaree॥3॥
Kreeta Mukuta Sira Anupama Bhaaree। Kaanana Kundala Ko Chhavi Nyaaree॥4॥
Sohata Anga Chhataa Chhavi Pyaaree। Sundara Cheera Sunaharee Dhaaree॥5॥
Aapa Chaturbhuja Sughada Vishaalaa। Dhaarana Karahu Gale Vana Maalaa॥6॥
Nikata Hai Gau Amita Dulaaree। Karahu Mayoora Aapa Asavaaree॥7॥
Jaanata Sabahee Aapa Prabhutaa-ee। Sura Nara Muni Saba Karahin Badaa-ee॥8॥
Tumhare Darasha Karata Kshana Maa-ee। Dukha Daridra Saba Jaaya Nasaa-ee॥9॥
Veda Puraana Rahe Yasha Gaa-ee। Karahu Bhakta Kee Aapa Sahaa-ee॥10॥
Brahmaa Dhinga Saraswatee Kahaa-ee। Lakshmee Roopa Vishnu Dhinga Aa-ee॥11॥
Shiva Dhinga Girajaa Roopa Biraajee। Mahimaa Teenon Loka Men Gaajee॥12॥
Shakti Roopa Pragatee Jana Jaanee। Rudra Roopa Bha-ee Maata Bhavaanee॥13॥
Dushtadalana Hita Pragatee Kaalee। Jagamaga Jyoti Prachanda Niraalee॥14॥
Chanda Munda Mahishaasura Maare। Shumbha Nishumbha Asura Hani Daare॥15॥
Mahimaa Veda Puraanana Baranee। Nija Bhaktana Ke Sankata Haranee॥16॥
Roopa Shaaradaa Hansa Mohinee। Nirankaara Saakaara Daahinee॥17॥
Pragataa-ee Chahundisha Nija Maayaa। Kana Kana Men Hai Teja Samaayaa॥18॥
Prithvee Soorya Chandra Aru Taare। Tava Ingita Krama Baddha Hain Saare॥19॥
Paalana Poshana Tumaheen Karataa। Kshana Bhangura Men Praana Harataa॥20॥
Brahmaa Vishnu Tumhen Nita Dhyaavain। Shesha Mahesha Sadaa Mana Laave॥21॥
Manokaamanaa Poorana Karanee। Paapa Kaatanee Bhava Bhaya Taranee॥22॥
Chitta Lagaaya Tumhen Jo Dhyaataa। So Nara Sukha Sampatti Hai Paataa॥23॥
Bandhyaa Naari Tumahin Jo Dhyaavain। Putra Pushpa Lataa Sama Vaha Paavain॥24॥
Pati Viyogee Ati Vyaakulanaaree। Tuma Viyoga Ati Vyaakulayaaree॥25॥
Kanyaa Jo Ko-ee Tumako Dhyaavai। Apanaa Mana VaanChhita Vara Paavai॥26॥
Sheelavaana Gunavaana Ho Maiyaa। Apane Jana Kee Naava Khivaiyaa॥27॥
Vidhi Poorvaka Vrata Jo Ko-ee Karahin। Taahi Amita Sukha Sampatti Bharahin॥28॥
Guda Aura Chanaa Bhoga Tohi Bhaavai। Sevaa Karai So Aananda Paavai॥29॥
Shraddhaa Yukta Dhyaana Jo Dharahin। So Nara Nishchaya Bhava Son Tarahin॥30॥
Udyaapana Jo Karahi Tumhaaraa। Taako Sahaja Karahu Nistaaraa॥31॥
Naari Suhaagina Vrata Jo Karatee। Sukha Sampatti Son Godee Bharatee॥32॥
Jo Sumirata Jaisee Mana Bhaavaa। So Nara Vaiso Hee Phala Paavaa॥33॥
Saata Shukra Jo Vrata Mana Dhaare। Taake Poorna Manoratha Saare॥34॥
Sevaa Karahi Bhakti Yuta Jo-ee। Taako Doora Daridra Dukha Ho-ee॥35॥
Jo Jana Sharana Maataa Teree Aavai। Taake Kshana Men Kaaja Banaavai॥36॥
Jaya Jaya Jaya Ambe Kalyaanee। Kripaa Karau Moree Mahaaraanee॥37॥
Jo Ko-ee Padhai Maata Chaaleesaa। Taape Karahin Kripaa Jagadeeshaa॥38॥
Nita Prati Paatha Karai Ika Baaraa। So Nara Rahai Tumhaaraa Pyaaraa॥39॥
Naama Leta Byaadhaa Saba Bhaage। Roga Dosha Kabahoon Naheen Laage॥40॥

॥ Doha ॥
Santawshee Maan Ke Sadaa, Bandahun Paga Nisha Vaasa।
Poorna Manoratha Hon Sakala, Maata Harau Bhava Traasa॥"""

# 1. Update drik_chalisa_37 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

found = False
for item in cols["devi"]["items"]:
    if item["id"] == "drik_chalisa_37":
        item["title"] = "श्री संतोषी माता चालीसा"
        item["title_en"] = "Shri Santoshi Mata Chalisa"
        item["en_line"] = "Jai Santoshi Maa Jaga Janani"
        item["hi_line"] = "जय संतोषी मां जग जननी"
        item["sub"] = "जय संतोषी मां जग जननी • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_santoshi_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=VQXgD9VUjJc"
        item["video_id"] = "VQXgD9VUjJc"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/santoshi-mata/santoshi-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "सकल मनोरथ पूर्णकारिणी भगवती संतोषी माता"
        item["section"] = "दिव्य देवी माता चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        found = True
        break

if not found:
    print("ERROR: drik_chalisa_37 not found in devi category!")
    sys.exit(1)

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_37 in drik_chalisa_collections.json successfully!")

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

# 3. Add or update chalisa_santoshi in CONTENT in app.js
content_obj = {
    "title": "श्री संतोषी माता चालीसा",
    "title_en": "Shri Santoshi Mata Chalisa",
    "en_line": "Jai Santoshi Maa Jaga Janani",
    "hi_line": "जय संतोषी मां जग जननी",
    "sub": "जय संतोषी मां जग जननी • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_santoshi_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=VQXgD9VUjJc",
    "video_id": "VQXgD9VUjJc",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/santoshi-mata/santoshi-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "सकल मनोरथ पूर्णकारिणी भगवती संतोषी माता",
    "section": "दिव्य देवी माता चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

santoshi_content_js = "  chalisa_santoshi: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_santoshi: {" in app_text:
    pos_s = app_text.find("  chalisa_santoshi: {")
    pos_next = app_text.find("\n  chalisa_", pos_s + 1)
    if pos_next == -1:
        pos_next = app_text.find("\n  sundarkand:", pos_s + 1)
    app_text = app_text[:pos_s] + santoshi_content_js + app_text[pos_next+1:]
    print("Replaced existing chalisa_santoshi in CONTENT!")
else:
    # Insert right before chalisa_saraswati (after chalisa_vaishno)
    pos_saras = app_text.find("  chalisa_saraswati: {")
    if pos_saras != -1:
        app_text = app_text[:pos_saras] + santoshi_content_js + app_text[pos_saras:]
        print("Inserted chalisa_santoshi before chalisa_saraswati in CONTENT!")
    else:
        # fallback: insert before sundarkand
        pos_sun = app_text.find("  sundarkand: {")
        if pos_sun != -1:
            app_text = app_text[:pos_sun] + santoshi_content_js + app_text[pos_sun:]
            print("Inserted chalisa_santoshi before sundarkand in CONTENT!")
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

print("ALL SANTOSHI UPDATES COMPLETED!")
