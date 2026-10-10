import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री बगलामुखी माता चालीसा ॥

॥ दोहा ॥
सिर नवाइ बगलामुखी, लिखूँ चालीसा आज।
कृपा करहु मोपर सदा, पूरन हो मम काज॥

॥ चौपाई ॥
जय जय जय श्री बगला माता। आदिशक्ति सब जग की त्राता॥१॥
बगला सम तब आनन माता। एहि ते भयउ नाम विख्याता॥२॥
शशि ललाट कुण्डल छवि न्यारी। अस्तुति करहिं देव नर-नारी॥३॥
पीतवसन तन पर तव राजै। हाथहिं मुद्गर गदा विराजै॥४॥
तीन नयन गल चम्पक माला। अमित तेज प्रकटत है भाला॥५॥
रत्न-जटित सिंहासन सोहै। शोभा निरखि सकल जन मोहै॥६॥
आसन पीतवर्ण महारानी। भक्तन की तुम हो वरदानी॥७॥
पीताभूषण पीतहिं चन्दन। सुर नर नाग करत सब वन्दन॥८॥
एहि विधि ध्यान हृदय में राखै। वेद पुराण सन्त अस भाखै॥९॥
अब पूजा विधि करौं प्रकाशा। जाके किये होत दुख-नाशा॥१०॥
प्रथमहिं पीत ध्वजा फहरावै। पीतवसन देवी पहिरावै॥११॥
कुंकुम अक्षत मोदक बेसन। अबिर गुलाल सुपारी चन्दन॥१२॥
माल्य हरिद्रा अरु फल पाना। सबहिं चढ़इ धरै उर ध्याना॥१३॥
धूप दीप कर्पूर की बाती। प्रेम-सहित तब करै आरती॥१४॥
अस्तुति करै हाथ दोउ जोरे। पुरवहु मातु मनोरथ मोरे॥१५॥
मातु भगति तब सब सुख खानी। करहु कृपा मोपर जनजानी॥१६॥
त्रिविध ताप सब दुःख नशावहु। तिमिर मिटाकर ज्ञान बढ़ावहु॥१७॥
बार-बार मैं बिनवउँ तोहीं। अविरल भगति ज्ञान दो मोहीं॥१८॥
पूजनान्त में हवन करावै। सो नर मनवांछित फल पावै॥१९॥
सर्षप होम करै जो कोई। ताके वश सचराचर होई॥२०॥
तिल तण्डुल संग क्षीर मिरावै। भक्ति प्रेम से हवन करावै॥२१॥
दुःख दरिद्र व्यापै नहिं सोई। निश्चय सुख-संपति सब होई॥२२॥
फूल अशोक हवन जो करई। ताके गृह सुख-सम्पत्ति भरई॥२३॥
फल सेमर का होम करीजै। निश्चय वाको रिपु सब छीजै॥२४॥
गुग्गुल घृत होमै जो कोई। तेहि के वश में राजा होई॥२५॥
गुग्गुल तिल सँग होम करावै। ताको सकल बन्ध कट जावै॥२६॥
बीजाक्षर का पाठ जो करहीं। बीजमन्त्र तुम्हरो उच्चरहीं॥२७॥
एक मास निशि जो कर जापा। तेहि कर मिटत सकल सन्तापा॥२८॥
घर की शुद्ध भूमि जहँ होई। साधक जाप करै तहँ सोई॥२९॥
सोइ इच्छित फल निश्चय पावै। जामे नहिं कछु संशय लावै॥३०॥
अथवा तीर नदी के जाई। साधक जाप करै मन लाई॥३१॥
दस सहस्र जप करै जो कोई। सकल काज तेहि कर सिधि होई॥३२॥
जाप करै जो लक्षहिं बारा। ताकर होय सुयश विस्तारा॥३३॥
जो तव नाम जपै मन लाई। अल्पकाल महँ रिपुहिं नसाई॥३४॥
सप्तरात्रि जो जापहिं नामा। वाको पूरन हो सब कामा॥३५॥
नव दिन जाप करे जो कोई। व्याधि रहित ताकर तन होई॥३६॥
ध्यान करै जो बन्ध्या नारी। पावै पुत्रादिक फल चारी॥३७॥
प्रातः सायं अरु मध्याना। धरे ध्यान होवै कल्याना॥३८॥
कहँ लगि महिमा कहौं तिहारी। नाम सदा शुभ मंगलकारी॥३९॥
पाठ करै जो नित्य चालीसा। तेहि पर कृपा करहिं गौरीशा॥४०॥

॥ दोहा ॥
सन्तशरण को तनय हूँ, कुलपति मिश्र सुनाम।
हरिद्वार मण्डल बसूँ, धाम हरिपुर ग्राम॥
उन्नीस सौ पिचानबे सन् की, श्रावण शुक्ला मास।
चालीसा रचना कियौं, तव चरणन को दास॥"""

meaning = """॥ श्री बगलामुखी माता चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहा】
• "सिर नवाइ बगलामुखी, लिखूँ चालीसा आज। कृपा करहु मोपर सदा, पूरन हो मम काज॥"
भावार्थ: हे भगवती बगलामुखी! आपके श्रीचरणों में श्रद्धापूर्वक शीश नवाकर आज मैं आपकी इस पावन चालीसा की रचना कर रहा हूँ। हे माता! मुझ पर अपनी नित्य अहैतुकी कृपा बनाए रखिए, जिससे मेरे समस्त मनोरथ और कार्य निर्विघ्न पूर्ण हों।

【चौपाइयां — पद्यवार भावार्थ】
१-१०. "जय जय जय श्री बगला माता... वेद पुराण सन्त अस भाखै॥"
भावार्थ: हे माँ बगलामुखी! आपकी जय हो, जय हो, जय हो; आप संपूर्ण संसार की रक्षा करने वाली आद्यशक्ति हैं। आपका पावन मुख बगुले (बक) के समान तीक्ष्ण ध्यान और एकाग्रता युक्त है, इसी कारण आपका नाम 'बगलामुखी' सर्वत्र विख्यात हुआ। आपके मस्तक पर दूज का चन्द्रमा और कानों में दिव्य कुण्डलों की छटा अत्यंत निराली है; देवता, मनुष्य और नारियां निरंतर आपकी स्तुति करते हैं। आपके सुवर्ण-जैसे कांतियुक्त श्रीअंगों पर पीताम्बरी (पीले वस्त्र) सुशोभित हैं और आपके कर-कमलों में संहारक मुद्गर (गदा) विराजमान है। आपके तीन दिव्य त्रिनेत्र हैं, गले में चंपा के पीले पुष्पों की सुगंधित माला है और आपके भाल (ललाट) से अमित अलौकिक तेज प्रकट होता है। आप बहुमूल्य रत्नों से जड़े स्वर्णिम सिंहासन पर विराजमान हैं, जिसकी अनुपम शोभा देखकर समस्त संसार मुग्ध हो जाता है। हे महारानी! आपका आसन पीतवर्ण (पीला) है और आप अपने अनन्य भक्तों को समस्त मनोवांछित वरदान देने वाली हैं। आपके सभी आभूषण पीले स्वर्ण के हैं और आप पीला चंदन धारण करती हैं; देवता, मनुष्य और नागगण सभी आपके पावन चरणों में वंदन करते हैं। वेद, पुराण और संतजन यही कहते हैं कि साधक को इस प्रकार माता के दिव्य पीत-स्वरूप का ध्यान सदैव अपने हृदय में रखना चाहिए।

११-१८. "अब पूजा विधि करौं प्रकाशा... अविरल भगति ज्ञान दो मोहीं॥"
भावार्थ: अब मैं माता की उस पावन पूजन विधि का वर्णन करता हूँ, जिसके अनुष्ठान से समस्त दुखों का समूल नाश हो जाता है। सर्वप्रथम पूजा स्थल पर पीली ध्वजा फहराएं और माता को पीले वस्त्र (पीताम्बरी) पहनाएं। इसके पश्चात कुंकुम, अक्षत, बेसन के पीले मोदक (लड्डू), अबीर, गुलाल, सुपारी और पीला चंदन अर्पित करें। हल्दी की गांठें, पीले पुष्पों की माला, फल और पान का बीड़ा चढ़ाकर हृदय में माता का एकाग्र ध्यान धरें। धूप, दीप और कर्पूर की ज्योति प्रज्वलित कर अत्यंत प्रेम व भक्तिभाव से माता की पावन आरती करें। दोनों हाथ जोड़कर माता से विनीत प्रार्थना करें कि हे माता! मेरे सभी धर्मानुकूल मनोरथों को पूर्ण कीजिए। हे माता! आपकी अनन्य भक्ति ही समस्त सुखों की अक्षय खान है; मुझे अपना दीन सेवक जानकर मुझ पर कृपा कीजिए। मेरे आधि, व्याधि और उपाधि रूपी तीनों तापों को नष्ट कर दीजिए तथा अज्ञान का अंधकार मिटाकर दिव्य आत्मज्ञान का प्रकाश बढ़ाइए। मैं बार-बार आपके चरणों में यही प्रार्थना करता हूँ कि मुझे अपनी अविरल भक्ति और विशुद्ध ज्ञान प्रदान कीजिए।

१९-२६. "पूजनान्त में हवन करावै... ताको सकल बन्ध कट जावै॥"
भावार्थ: पूजन की पूर्णता पर जो साधक विधिपूर्वक हवन (यज्ञ) करता है, वह अपने मनवांछित समस्त फलों को प्राप्त करता है। जो साधक पीली सरसों (सर्षप) से आहुति देकर हवन करता है, उसके प्रभाव से चराचर जगत उसके अनुकूल व वशीभूत हो जाता है। जो तिल, अक्षत (चावल) और दूध-खीर मिलाकर भक्ति-प्रेम से हवन करता है, उसके घर में कभी दुख और दरिद्रता नहीं फटकती तथा निश्चय ही समस्त सुख और समृद्धि की वृद्धि होती है। जो अशोक के ताजे पुष्पों से हवन करता है, उसका घर धन-धान्य और वैभव से परिपूर्ण हो जाता है। जो सेमर के फल से आहुति देता है, उसके समस्त प्रबल शत्रुओं का निश्चय ही समूल नाश हो जाता है। जो शुद्ध घृत (घी) और गुग्गुल से हवन करता है, बड़े-बड़े अधिकारी और राजा भी उसके वशीभूत हो जाते हैं। जो गुग्गुल और काले तिलों को मिलाकर हवन करता है, उसके जीवन के समस्त बंधन, कारागार-दोष और कानूनी संकट तत्काल कट जाते हैं।

२७-४०. "बीजाक्षर का पाठ जो करहीं... तेहि पर कृपा करहिं गौरीशा॥"
भावार्थ: जो साधक माता के एकाक्षरी बीजमन्त्र ('ह्ल्रीं' / 'ह्रीं') का नित्य पाठ और उच्चारण करते हैं; और एक मास तक रात्रि काल में इस दिव्य बीजमन्त्र का जप करते हैं, उनके समस्त संताप और कष्ट मिट जाते हैं। अपने घर की अत्यंत शुद्ध, पवित्र भूमि पर बैठकर जो साधक एकाग्रचित्त होकर जप करता है, उसे अपने समस्त इच्छित फलों की प्राप्ति होती है, इसमें तनिक भी संशय नहीं है। अथवा किसी पवित्र नदी के तट पर जाकर साधक मन लगाकर जप करे। जो साधक दस सहस्र (१०,०००) जप पूर्ण करता है, उसके रुके हुए सभी कार्य सिद्ध हो जाते हैं। जो एक लाख (१,००,०००) जप संपन्न करता है, उसके सुयश और कीर्ति का चारों दिशाओं में विस्तार होता है। जो मन लगाकर माता के नाम का जप करता है, अल्पकाल में ही उसके शत्रुओं का शमन हो जाता है। जो लगातार सात रात्रियों तक माता के नाम का अनुष्ठान करता है, उसके समस्त कार्य पूर्ण होते हैं। जो नौ दिनों (नवरात्रि) तक जप करता है, उसका शरीर समस्त असाध्य व्याधियों और रोगों से मुक्त होकर कांतिवान हो जाता है। जो निःसंतान स्त्री श्रद्धा से माता का ध्यान करती है, वह पुत्र-पौत्र और धर्म, अर्थ, काम, मोक्ष चारों फलों को प्राप्त करती है। प्रातः, दोपहर अथवा सांध्यकाल—तीनों कालों में माता का ध्यान करने से सर्वतोभावेन कल्याण होता है। माता की असीम महिमा का कहाँ तक बखान किया जाए; आपका पावन नाम सदा अत्यंत शुभ और मंगलकारी है। जो भी नित्य इस पावन चालीसा का पाठ करता है, उस पर देवाधिदेव भगवान शिव (गौरीश) और माता पीताम्बरा की अक्षय कृपा सदा बनी रहती है।

【समापन दोहे】
• "सन्तशरण को तनय हूँ, कुलपति मिश्र सुनाम। हरिद्वार मण्डल बसूँ, धाम हरिपुर ग्राम॥ उन्नीस सौ पिचानबे सन् की, श्रावण शुक्ला मास। चालीसा रचना कियौं, तव चरणन को दास॥"
भावार्थ: हरिद्वार मंडल के पावन हरिपुर ग्राम के निवासी, संतशरण जी के सुपुत्र कवि कुलपति मिश्र ने सन् १९९५ के श्रावण मास के शुक्ल पक्ष में माता बगलामुखी के चरणों के अनन्य दास बनकर इस पावन चालीसा की रचना की है।"""

vidhi = """॥ श्री बगलामुखी माता चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- सर्वोत्तम समय: रात्रि काल (निशीथ काल / सांध्यकाल — बगलामुखी साधना में रात्रि साधना विशेष प्रभावशाली मानी गई है) अथवा प्रातःकाल ब्रह्ममुहूर्त।
- सर्वोत्तम वार: गुरुवार एवं मंगलवार (माँ पीताम्बरा की विशेष आराधना के दिन)।
- महापर्व व पावन तिथियां: बगलामुखी जयंती (वैशाख शुक्ल अष्टमी), गुप्त व प्रकट नवरात्रि (विशेषकर अष्टमी तिथि), तथा चतुर्दशी।

२. पीताम्बरा साधना के अनिवार्य नियम (सर्वत्र पीत रंग):
- वस्त्र: साधक को पीले रंग के शुद्ध, धुले हुए सूती अथवा रेशमी वस्त्र धारण करने चाहिए।
- आसन: पीले रंग का ऊनी आसन अथवा कुशासन।
- दिशा: पूर्व अथवा उत्तर दिशा की ओर मुख करके बैठें।
- जप माला: हल्दी की गांठों से बनी माला (हरिद्रा माला) सर्वोत्तम है।

३. पूजन सामग्री, दीप व नैवेद्य:
- दीपक: गाय के शुद्ध देशी घी अथवा तिल के तेल का दीपक, जिसमें हल्दी मिलाकर बत्ती को पीला किया गया हो।
- प्रिय पुष्प: पीले कनेर, पीले गेंदे अथवा चंपा के ताजे पुष्प।
- प्रिय नैवेद्य: बेसन के लड्डू, चने की दाल, पके हुए पीले केले, आम, केसरिया खीर, और पीले बताशे।
- तिलक: हल्दी, केसर और पीले चंदन का तिलक करें।

४. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन, पवित्रीकरण एवं हाथ में जल व पीली सरसों लेकर संकल्प करें।
- माँ बगलामुखी का ध्यान करें:
  'ॐ मध्ये सुधाब्धिमणिमण्डपरत्नवेद्यां सिंहासनोपरिगतां परिपीतवर्णाम्।
   पीताम्बराभरणमाल्यविभूषिताङ्गीं देवीं स्मरामि धृतमुद्गरवैरिजिव्हाम्॥'
- माँ बगलामुखी का सिद्ध बीजमन्त्र: 'ॐ ह्ल्रीं बगलामुख्यै नमः' अथवा 'ॐ ह्ल्रीं बगलामुखि सर्वदुष्टानां वाचं मुखं पदं स्तम्भय जिह्वां कीलय बुद्धिं विनाशय ह्ल्रीं ॐ स्वाहा' का यथासंभव १ माला (१०८ बार) जप करें।
- इसके पश्चात शांत चित्त होकर 'श्री बगलामुखी माता चालीसा' का १, ३, अथवा ७ बार पाठ करें।
- पाठ उपरांत आरती करें, पीली सरसों व गुग्गुल से दशांश हवन करें और क्षमा-प्रार्थना करें।"""

significance = """॥ श्री बगलामुखी माता चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. शत्रु-स्तम्भन व वाक-सिद्धि:
"जो तव नाम जपै मन लाई। अल्पकाल महँ रिपुहिं नसाई॥"
माँ बगलामुखी दश महाविद्याओं में स्तम्भन शक्ति की अधिष्ठात्री हैं। चालीसा के पाठ से विरोधियों, ईर्ष्यालुओं और शत्रुओं की बुद्धि व वाणी स्तम्भित हो जाती है और साधक को वाक-सिद्धि प्राप्त होती है।

२. कोर्ट-कचहरी, मुकदमे व विवादों में विजय:
"गुग्गुल तिल सँग होम करावै। ताको सकल बन्ध कट जावै॥"
अकारण लगे झूठे आरोपों, कानूनी मुकदमों, और बंधनों से मुक्ति मिलकर साधक को विजयश्री प्राप्त होती है।

३. तंत्र-मंत्र, नजर दोष व मारण-उच्चाटन से रक्षा:
माता पीताम्बरा का प्रभाव साधक के चारों ओर प्रचंड स्वर्ण-कवच निर्मित करता है, जिससे किसी भी प्रकार की तांत्रिक क्रिया, बुरी नजर या मारण-दोष निष्फल हो जाता है।

४. असाध्य रोगों व अकाल संकटों का शमन:
"नव दिन जाप करे जो कोई। व्याधि रहित ताकर तन होई॥"
गंभीर व असाध्य शारीरिक-मानसिक रोगों का शमन होकर शरीर निरोगी और ओजस्वी बनता है।

५. वंश वृद्धि, पुत्र प्राप्ति व राज्य-सम्मान:
"ध्यान करै जो बन्ध्या नारी। पावै पुत्रादिक फल चारी॥ गुग्गुल घृत होमै जो कोई। तेहि के वश में राजा होई॥"
निःसंतान को संतान सुख मिलता है तथा समाज और कार्यक्षेत्र में उच्च पद, मान-प्रतिष्ठा और प्रभाव में वृद्धि होती है।"""

english_lyrics = """॥ Shri Bagalamukhi Mata Chalisa ॥

॥ Doha ॥
Sira Navaa-i Bagalaamukhee, Likhoon Chaaleesaa Aaja।
Kripaa Karahu Mopara Sadaa, Poorana Ho Mama Kaaja॥

॥ Chaupai ॥
Jaya Jaya Jaya Shree Bagalaa Maataa। Aadishakti Saba Jaga Kee Traataa॥1॥
Bagalaa Sama Taba Aanana Maataa। Ehi Te Bhaya-u Naama Vikhyaataa॥2॥
Shashi Lalaata Kundala Chhavi Nyaaree। Astuti Karahin Deva Nara-Naaree॥3॥
Peetavasana Tana Para Tava Raajai। Haathahin Mudgara Gadaa Viraajai॥4॥
Teena Nayana Gala Champaka Maalaa। Amita Teja Prakatata Hai Bhaalaa॥5॥
Ratna-Jatita Sinhaasana Sohai। Shobhaa Nirakhi Sakala Jana Mohai॥6॥
Aasana Peetavarna Mahaaraanee। Bhaktana Kee Tuma Ho Varadaanee॥7॥
Peetaabhooshana Peetahin Chandana। Sura Nara Naaga Karata Saba Vandana॥8॥
Ehi Vidhi Dhyaana Hridaya Men Raakhai। Veda Puraana Santa Asa Bhaakhai॥9॥
Aba Poojaa Vidhi Karaun Prakaashaa। Jaake Kiye Hota Dukha-Naashaa॥10॥
Prathamahin Peeta Dhvajaa Phaharaavai। Peetavasana Devee Pahiraavai॥11॥
Kunkuma Akshata Modaka Besana। Abira Gulaala Supaaree Chandana॥12॥
Maalya Haridraa Aru Phala Paanaa। Sabahin Chadha-i Dharai Ura Dhyaanaa॥13॥
Dhoopa Deepa Karpoora Kee Baatee। Prema-Sahita Taba Karai Aaratee॥14॥
Astuti Karai Haatha Dou Jore। Puravahu Maatu Manoratha More॥15॥
Maatu Bhagati Taba Saba Sukha Khaanee। Karahu Kripaa Mopara Janajaanee॥16॥
Trividha Taapa Saba Duhkha Nashaavahu। Timira Mitaakara Gyaana Badhaavahu॥17॥
Baara-Baara Main Binava-un Toheen। Avirala Bhagati Gyaana Do Moheen॥18॥
Poojanaanta Men Havana Karaavai। So Nara ManavaanChhita Phala Paavai॥19॥
Sarshapa Homa Karai Jo Ko-ee। Taake Vasha Sacharaachara Ho-ee॥20॥
Tila Tandula Sanga Ksheera Miraavai। Bhakti Prema Se Havana Karaavai॥21॥
Duhkha Daridra Vyaapai Nahin So-ee। Nishchaya Sukha-Sampati Saba Ho-ee॥22॥
Phoola Ashoka Havana Jo Kara-ee। Taake Griha Sukha-Sampatti Bhara-ee॥23॥
Phala Semara Kaa Homa Kareeje। Nishchaya Vaako Ripu Saba Chheeje॥24॥
Guggula Ghrita Homai Jo Ko-ee। Tehi Ke Vasha Men Raajaa Ho-ee॥25॥
Guggula Tila Sanga Homa Karaavai। Taako Sakala Bandha Kata Jaavai॥26॥
Beejaakshara Kaa Paatha Jo Karahin। Beejamantra Tumharo Uchcharahin॥27॥
Eka Maasa Nishi Jo Kara Jaapaa। Tehi Kara Mitata Sakala Santaapaa॥28॥
Ghara Kee Shuddha Bhoomi Jahan Ho-ee। Saadhaka Jaapa Karai Tahan So-ee॥29॥
So-i Ichhita Phala Nishchaya Paavai। Jaame Nahin Kachhu Sanshaya Laavai॥30॥
Athavaa Teera Nadee Ke Jaa-ee। Saadhaka Jaapa Karai Mana Laa-ee॥31॥
Dasa Sahasra Japa Karai Jo Ko-ee। Sakala Kaaja Tehi Kara Sidhi Ho-ee॥32॥
Jaapa Karai Jo Lakshahin Baaraa। Taakara Hoya Suyasha Vistaaraa॥33॥
Jo Tava Naama Japai Mana Laa-ee। Alapakaala Mahan Ripuhin Nasaa-ee॥34॥
Saptaraatri Jo Jaapahin Naamaa। Vaako Poorana Ho Saba Kaamaa॥35॥
Nava Dina Jaapa Kare Jo Ko-ee। Vyaadhi Rahita Taakara Tana Ho-ee॥36॥
Dhyaana Karai Jo Bandhyaa Naaree। Paavai Putraadika Phala Chaaree॥37॥
Praatah Saayana Aru Madhyaanaa। Dhare Dhyaana Hovai Kalyaanaa॥38॥
Kahan Lagi Mahimaa Kahaun Tihaaree। Naama Sadaa Shubha Mangalakaaree॥39॥
Paatha Karai Jo Nitya Chaaleesaa। Tehi Para Kripaa Karahin Gaureeshaa॥40॥

॥ Doha ॥
Santasharana Ko Tanaya Hoon, Kulapati Mishra Sunaama।
Haridvaara Mandala Basoon, Dhaama Haripura Graama॥
Unneesa Sau Pichaanabe Sanna Kee, Shraavana Shuklaa Maasa।
Chaaleesaa Rachanaa Kiyaun, Tava Charanana Ko Daasa॥"""

# 1. Update drik_chalisa_39 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

found = False
for item in cols["devi"]["items"]:
    if item["id"] == "drik_chalisa_39":
        item["title"] = "श्री बगलामुखी माता चालीसा"
        item["title_en"] = "Shri Bagalamukhi Mata Chalisa"
        item["en_line"] = "Jai Jai Jai Shri Bagala Mata"
        item["hi_line"] = "जय जय जय श्री बगला माता"
        item["sub"] = "जय जय जय श्री बगला माता • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_bagalamukhi_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=nAT4LNGnUsc"
        item["video_id"] = "nAT4LNGnUsc"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/bagalamukhi-mata/bagalamukhi-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "शत्रुस्तम्भिनी वाकसिद्धिप्रदायिनी पीताम्बरा भगवती बगलामुखी माता"
        item["section"] = "दिव्य देवी माता चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        found = True
        break

if not found:
    print("ERROR: drik_chalisa_39 not found in devi category!")
    sys.exit(1)

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_39 in drik_chalisa_collections.json successfully!")

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

# 3. Add or update chalisa_bagalamukhi in CONTENT in app.js
content_obj = {
    "title": "श्री बगलामुखी माता चालीसा",
    "title_en": "Shri Bagalamukhi Mata Chalisa",
    "en_line": "Jai Jai Jai Shri Bagala Mata",
    "hi_line": "जय जय जय श्री बगला माता",
    "sub": "जय जय जय श्री बगला माता • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_bagalamukhi_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=nAT4LNGnUsc",
    "video_id": "nAT4LNGnUsc",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/bagalamukhi-mata/bagalamukhi-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "शत्रुस्तम्भिनी वाकसिद्धिप्रदायिनी पीताम्बरा भगवती बगलामुखी माता",
    "section": "दिव्य देवी माता चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

bagala_content_js = "  chalisa_bagalamukhi: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_bagalamukhi: {" in app_text:
    pos_s = app_text.find("  chalisa_bagalamukhi: {")
    pos_next = app_text.find("\n  chalisa_", pos_s + 1)
    if pos_next == -1:
        pos_next = app_text.find("\n  sundarkand:", pos_s + 1)
    app_text = app_text[:pos_s] + bagala_content_js + app_text[pos_next+1:]
    print("Replaced existing chalisa_bagalamukhi in CONTENT!")
else:
    # Insert right before chalisa_saraswati (after chalisa_parvati)
    pos_saras = app_text.find("  chalisa_saraswati: {")
    if pos_saras != -1:
        app_text = app_text[:pos_saras] + bagala_content_js + app_text[pos_saras:]
        print("Inserted chalisa_bagalamukhi before chalisa_saraswati in CONTENT!")
    else:
        # fallback: insert before sundarkand
        pos_sun = app_text.find("  sundarkand: {")
        if pos_sun != -1:
            app_text = app_text[:pos_sun] + bagala_content_js + app_text[pos_sun:]
            print("Inserted chalisa_bagalamukhi before sundarkand in CONTENT!")
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

print("ALL BAGALAMUKHI UPDATES COMPLETED!")
