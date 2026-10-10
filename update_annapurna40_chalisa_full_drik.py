import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री अन्नपूर्णा माता चालीसा ॥

॥ दोहा ॥
विश्वेश्वर-पदपदम की, रज-निज शीश-लगाय।
अन्नपूर्णे! तव सुयश, बरनौं कवि-मतिलाय॥

॥ चौपाई ॥
नित्य आनन्द करिणी माता। वर-अरु अभय भाव प्रख्याता॥१॥
जय! सौंदर्य सिन्धु जग-जननी। अखिल पाप हर भव-भय हरनी॥२॥
श्वेत बदन पर श्वेत बसन पुनि। सन्तन तुव पद सेवत ऋषिमुनि॥३॥
काशी पुराधीश्वरी माता। माहेश्वरी सकल जग-त्राता॥४॥
बृषभारुढ़ नाम रुद्राणी। विश्व विहारिणि जय! कल्याणी॥५॥
पदिदेवता सुतीत शिरोमनि। पदवी प्राप्त कीह्न गिरि-नंदिनि॥६॥
पति विछोह दुख सहि नहि पावा। योग अग्नि तब बदन जरावा॥७॥
देह तजत शिव-चरण सनेहू। राखेहु जाते हिमगिरि-गेहू॥८॥
प्रकटी गिरिजा नाम धरायो। अति आनन्द भवन मँह छायो॥९॥
नारद ने तब तोहिं भरमायहु। ब्याह करन हित पाठ पढ़ायहु॥१०॥
ब्रह्मा-वरुण-कुबेर गनाये। देवराज आदिक कहि गाय॥११॥
सब देवन को सुजस बखानी। मतिपलटन की मन मँह ठानी॥१२॥
अचल रहीं तुम प्रण पर धन्या। कीह्नी सिद्ध हिमाचल कन्या॥१३॥
निज कौ तव नारद घबराये। तब प्रण-पूरण मंत्र पढ़ाये॥१४॥
करन हेतु तप तोहिं उपदेशेउ। सन्त-बचन तुम सत्य परेखेहु॥१५॥
गगनगिरा सुनि टरी न टारे। ब्रह्मा, तब तुव पास पधारे॥१६॥
कहेउ पुत्रि वर माँगु अनूपा। देहुँ आज तुव मति अनुरुपा॥१७॥
तुम तप कीन्ह अलौकिक भारी। कष्ट उठायेहु अति सुकुमारी॥१८॥
अब संदेह छाँड़ि कछु मोसों। है सौगंध नहीं छल तोसों॥१९॥
करत वेद विद ब्रह्मा जानहु। वचन मोर यह सांचो मानहु॥२०॥
तजि संकोच कहहु निज इच्छा। देहौं मैं मन मानी भिक्षा॥२१॥
सुनि ब्रह्मा की मधुरी बानी। मुखसों कछु मुसुकायि भवानी॥२२॥
बोली तुम का कहहु विधाता। तुम तो जगके स्रष्टाधाता॥२३॥
मम कामना गुप्त नहिं तोंसों। कहवावा चाहहु का मोसों॥२४॥
इज्ञ यज्ञ महँ मरती बारा। शंभुनाथ पुनि होहिं हमारा॥२५॥
सो अब मिलहिं मोहिं मनभाय। कहि तथास्तु विधि धाम सिधाये॥२६॥
तब गिरिजा शंकर तव भयऊ। फल कामना संशय गयऊ॥२७॥
चन्द्रकोटि रवि कोटि प्रकाशा। तब आनन महँ करत निवासा॥२८॥
माला पुस्तक अंकुश सोहै। करमँह अपर पाश मन मोहे॥२९॥
अन्नपूर्णे! सदपूर्णे। अज-अनवद्य अनन्त अपूर्णे॥३०॥
कृपा सगरी क्षेमंकरी माँ। भव-विभूति आनन्द भरी माँ॥३१॥
कमल बिलोचन विलसित बाले। देवि कालिके! चण्डि कराले॥३२॥
तुम कैलास मांहि ह्वै गिरिजा। विलसी आनन्दसाथ सिन्धुजा॥३३॥
स्वर्ग-महालक्ष्मी कहलायी। मर्त्य-लोक लक्ष्मी पदपायी॥३४॥
विलसी सब मँह सर्व सरुपा। सेवत तोहिं अमर पुर-भूपा॥३५॥
जो पढ़िहहिं यह तुव चालीसा। फल पइहहिं शुभ साखी ईसा॥३६॥
प्रात समय जो जन मन लायो। पढ़िहहिं भक्ति सुरुचि अघिकायो॥३७॥
स्त्री-कलत्र पति मित्र-पुत्र युत। परमैश्वर्य लाभ लहि अद्भुत॥३८॥
राज विमुखको राज दिवावै। जस तेरो जन-सुजस बढ़ावै॥३९॥
पाठ महा मुद मंगल दाता। भक्त मनो वांछित निधिपाता॥४०॥

॥ दोहा ॥
जो यह चालीसा सुभग, पढ़ि नावहिंगे माथ।
तिनके कारज सिद्ध सब, साखी काशी नाथ॥"""

meaning = """॥ श्री अन्नपूर्णा माता चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहा】
• "विश्वेश्वर-पदपदम की, रज-निज शीश-लगाय। अन्नपूर्णे! तव सुयश, बरनौं कवि-मतिलाय॥"
भावार्थ: देवाधिदेव काशी विश्वनाथ भगवान शिव के पावन चरण-कमलों की पावन रज (धूल) को अपने शीश पर धारण कर, हे माँ अन्नपूर्णा! मैं अपनी मति और श्रद्धा के अनुसार आपके अलौकिक सुयश व महिमा का श्रद्धापूर्वक बखान करता हूँ।

【चौपाइयां — पद्यवार भावार्थ】
१-१०. "नित्य आनन्द करिणी माता... अति आनन्द भवन मँह छायो॥"
भावार्थ: हे माँ अन्नपूर्णा! आप सदा भक्तों को नित्यानंद (अखंड आनंद) प्रदान करने वाली और वरदान तथा अभय मुद्रा धारण करने के लिए विख्यात हैं। हे सौंदर्य के अगाध सिंधु! हे संपूर्ण जगत की जननी! आपकी जय हो; आप भक्तों के समस्त पापों और भवसागर के जन्म-मरण रूपी भय को हरने वाली हैं। आपके सुंदर गौर-श्वेत मुखमंडल पर श्वेत वसन (वस्त्र) सुशोभित हैं; साधु-संत और ऋषि-मुनि निरंतर आपके पावन चरणों की सेवा करते हैं। आप पवित्र काशी नगरी की अधिष्ठात्री महारानी (काशीपुराधीश्वरी) हैं; हे माहेश्वरी! आप संपूर्ण संसार की रक्षा करने वाली जगत-त्राता हैं। नंदी बैल पर आरूढ़ होने वाली रुद्राणी! हे चराचर जगत में विहार करने वाली कल्याणी माँ! आपकी सदा जय हो। पूर्वजन्म में प्रजापति दक्ष की पुत्री सती के रूप में आपने पतिव्रता शिरोमणि की पदवी प्राप्त की थी। जब आपने पिता के यज्ञ में पति भगवान शिव का अपमान देखा, तो पति-वियोग का दारुण दुख सहन न कर पाने के कारण आपने अपनी योगाग्नि में अपनी देह भस्म कर दी। देह त्यागते समय भी आपने भगवान शिव के चरणों का पावन स्नेह अपने हृदय में संजोए रखा, जिसके प्रभाव से आपने पुनः हिमवान (हिमालय) के घर में जन्म लिया। जब आप हिमालय के यहाँ 'गिरिजा' नाम से प्रकट हुईं, तो संपूर्ण पर्वतराज के भवन में अपार आनंद छा गया।

११-२०. "नारद ने तब तोहिं भरमायहु... वचन मोर यह सांचो मानहु॥"
भावार्थ: तब देवर्षि नारद जी ने आपकी परीक्षा लेने हेतु आपको अन्य देवों से विवाह करने का विचार सुझाया। उन्होंने ब्रह्मा, वरुण, कुबेर और देवराज इन्द्र आदि देवताओं के वैभव की गणना कराई। सभी देवताओं के सुयश का बखान कर उन्होंने आपके मन को शिव-तप से विचलित करने का प्रयास किया। किन्तु हे हिमाचल की पावन कन्या! आप धन्य हैं, आप अपने उस अखंड प्रण पर अडिग रहीं और अपने संकल्प को सिद्ध कर दिखाया। आपके अटूट संकल्प को देखकर नारद जी ने संतुष्ट होकर आपको शिव-प्राप्ति का सिद्ध पंचाक्षरी मन्त्र प्रदान किया। उन्होंने आपको कठोर तपस्या करने का उपदेश दिया और आपने संत-वचनों को सत्य मानकर स्वीकार किया। आकाशवाणी सुनकर भी जब आप अपने संकल्प से तनिक भी नहीं डिगीं, तब स्वयं सृष्टि के रचयिता ब्रह्मदेव आपके सम्मुख पधारे। ब्रह्मा जी ने कहा—हे पुत्री! आज अपने मन के अनुकूल मुझसे कोई अनुपम वरदान मांगो; मैं तुम्हारी इच्छानुसार तुम्हें वरदान दूँगा। हे सुकुमारी! तुमने यह जो अलौकिक और घोर तपस्या की है, इसमें तुमने अत्यंत भीषण कष्ट उठाए हैं। अब तुम मुझसे कोई संकोच मत करो; मैं सौगंध खाकर कहता हूँ कि मैं तुम्हारे साथ कोई छल नहीं कर रहा हूँ। मुझे वेदों के ज्ञाता ब्रह्मा जानो और मेरे इन वचनों को पूर्णतः सत्य मानो।

२१-३०. "तजि संकोच कहहु निज इच्छा... फल कामना संशय गयऊ॥"
भावार्थ: ब्रह्मा जी ने कहा—तुम संकोच छोड़कर अपनी मनचाही इच्छा बताओ, मैं तुम्हें तुम्हारी मनचाही भिक्षा (वरदान) प्रदान करूँगा। ब्रह्मा जी की यह मधुर वाणी सुनकर भगवती भवानी मंद-मंद मुस्कुराईं। वे बोलीं—हे विधाता! आप यह क्या कह रहे हैं? आप तो संपूर्ण जगत के रचयिता और अंतर्यामी हैं। मेरी आंतरिक कामना आपसे तनिक भी छिपी नहीं है; फिर आप मेरे मुख से क्या कहलवाना चाहते हैं? पूर्वजन्म में दक्ष-यज्ञ के समय जब मैंने शरीर त्यागा था, तब मैंने यही वर मांगा था कि देवाधिदेव शंभुनाथ ही पुनर्जन्म में मेरे पति हों। वही शिवजी आज मुझे पति रूप में प्राप्त हों। ब्रह्मा जी 'तथास्तु' कहकर अपने ब्रह्मलोक को सिधार गए। तब गिरिजा (पार्वती) का भगवान शंकर के साथ मंगल विवाह संपन्न हुआ और उनके सभी संशय व कामनाएं पूर्ण हुईं।

३१-४०. "चन्द्रकोटि रवि कोटि प्रकाशा... भक्त मनो वांछित निधिपाता॥"
भावार्थ: आपके पावन मुखमंडल में करोड़ों चन्द्रमाओं और करोड़ों सूर्यों का दिव्य प्रकाश एक साथ निवास करता है। आपके कर-कमलों में जपमाला, ज्ञानमयी पुस्तक, अंकुश और मन को मोह लेने वाला पाश (तथा स्वर्ण की कलछी व अन्न-पात्र) सुशोभित है। हे माँ अन्नपूर्णा! आप सदा परिपूर्ण, अजन्मा, निर्दोष, अनंत और अक्षुण्ण हैं। हे समस्त कृपा की खान, कल्याणकारिणी क्षेमंकरी माँ! आप समस्त सांसारिक ऐश्वर्य और परमानंद से परिपूर्ण हैं। कमल जैसे सुंदर नयनों वाली हे बाले! आप ही संहार के समय कालिका और कराली चण्डी हैं। आप कैलास में गिरिजा हैं और क्षीरसागर में समुद्र-तनया लक्ष्मी होकर आनंदपूर्वक विहार करती हैं। स्वर्गलोक में आप स्वर्ग-महालक्ष्मी और मृत्युलोक में धन-धान्य की देवी लक्ष्मी कहलाती हैं। आप इस चराचर जगत में सर्वरूपा होकर व्याप्त हैं; देवराज इन्द्र सहित समस्त देवगण आपकी सेवा करते हैं। जो भी मनुष्य आपकी इस पावन चालीसा का पाठ करता है, देवाधिदेव भगवान शिव (काशी विश्वनाथ) साक्षी हैं कि उसे समस्त शुभ फल प्राप्त होते हैं। जो प्रातःकाल एकाग्रचित्त होकर अत्यंत भक्ति और सुरुचि से इसका पाठ करता है, वह सुंदर जीवनसाथी, सुयोग्य पुत्र, मित्रों और अद्भुत परमैश्वर्य को प्राप्त करता है। यह चालीसा राज्य-विहीन व्यक्ति को भी राज्य (उच्च पद व प्रतिष्ठा) दिलाती है और यश में वृद्धि करती है। इसका पाठ परम आनंद, मंगल और मनवांछित समस्त निधियां प्रदान करने वाला है।

【समापन दोहा】
• "जो यह चालीसा सुभग, पढ़ि नावहिंगे माथ। तिनके कारज सिद्ध सब, साखी काशी नाथ॥"
भावार्थ: जो भी श्रद्धालु इस पावन और सुंदर चालीसा का पाठ करके माँ अन्नपूर्णा के श्रीचरणों में अपना शीश नवाते हैं, स्वयं देवाधिदेव काशी विश्वनाथ साक्षी हैं कि उनके जीवन के समस्त कार्य निर्विघ्न सिद्ध हो जाते हैं।"""

vidhi = """॥ श्री अन्नपूर्णा माता चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल सूर्योदय वेला (भोजन पकाने/रसोई कार्य से पूर्व) अथवा सांध्य आरती वेला।
- सर्वोत्तम वार: शुक्रवार (धन-धान्य प्रदायिनी देवी का दिन) एवं सोमवार (काशी विश्वनाथ सान्निध्य)।
- महापर्व व पावन तिथियां: मार्गशीर्ष (अगहन) मास की पूर्णिमा (अन्नपूर्णा जयंती), धनतेरस, नवरात्रि, तथा मकर संक्रांति।

२. दिशा, आसन व वस्त्र:
- दिशा: उत्तर अथवा पूर्व दिशा की ओर मुख करके बैठें।
- आसन: श्वेत, पीत अथवा लाल रंग का स्वच्छ ऊनी आसन बिछाएं।
- वस्त्र: साधक को शुद्ध, धुले हुए श्वेत, पीले अथवा लाल वस्त्र धारण करने चाहिए।

३. अन्न-पात्र, दीपक व प्रिय नैवेद्य:
- दीपक: शुद्ध गाय के देशी घी का दीपक प्रज्वलित करें।
- अन्न पात्र: एक तांबे या पीतल की थाली में चावल (अक्षत) अथवा गेहूं भरकर उस पर माँ अन्नपूर्णा का विग्रह अथवा चित्र स्थापित करें।
- प्रिय नैवेद्य: शुद्ध घी से बनी खीर, हलवा, पके हुए मीठे चावल, ताजे फल, दूध और मिश्री।
- रसोई पूजन नियम: भोजन पकाने के बाद सर्वप्रथम पहली रोटी/अन्न माँ अन्नपूर्णा और गौमाता के निमित्त समर्पित करें।

४. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन, पवित्रीकरण एवं हाथ में अक्षत-जल लेकर संकल्प करें।
- माँ अन्नपूर्णा का ध्यान करें:
  'ॐ अन्नपूर्णे सदापूर्णे शङ्करप्राणवल्लभे। ज्ञानवैराग्यसिद्ध्यर्थं भिक्षां देहि च पार्वति॥
   माता च पार्वती देवी पिता देवो महेश्वरः। बान्धवाः शिवभक्ताश्च स्वदेशो भुवनत्रयम्॥'
- माँ अन्नपूर्णा का सिद्ध मन्त्र: 'ॐ ह्रीं श्रीं क्लीं भगवति अन्नपूर्णे ममाभिलषितम् अन्नं देहि देहि स्वाहा' अथवा 'ॐ अन्नपूर्णायै नमः' का १०८ बार जप करें।
- इसके पश्चात शांत चित्त होकर 'श्री अन्नपूर्णा माता चालीसा' का १, ३, अथवा ५ बार पाठ करें।
- पाठ उपरांत आरती करें और रसोई में बने भोजन का भोग लगाकर सभी में प्रसाद वितरित करें।"""

significance = """॥ श्री अन्नपूर्णा माता चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. अन्न-धन का अक्षय भण्डार (अकाल मुक्ति):
"अन्नपूर्णे! सदपूर्णे... भक्त मनो वांछित निधिपाता॥"
माँ अन्नपूर्णा की कृपा से घर, रसोई और व्यापार में अन्न और धन का कभी अभाव नहीं होता; घर का भण्डार सदा भरा रहता है।

२. भूख, दरिद्रता व आर्थिक तंगी का समूल नाश:
"दुःख दरिद्र व्यापै नहिं सोई... परमैश्वर्य लाभ लहि अद्भुत॥"
साधक के परिवार से दरिद्रता, कर्ज और आर्थिक विपन्नता दूर होकर स्थायी ऐश्वर्य और समृद्धि की प्राप्ति होती है।

३. दांपत्य सुख, वंश वृद्धि व सुयोग्य संतान:
"स्त्री-कलत्र पति मित्र-पुत्र युत... साखी काशी नाथ॥"
परिवार में परस्पर प्रेम, दांपत्य सामंजस्य, और सुयोग्य पुत्र व मित्रों का सहयोग प्राप्त होता है।

४. उच्च पद, राज्य-प्रतिष्ठा व सम्मान:
"राज विमुखको राज दिवावै। जस तेरो जन-सुजस बढ़ावै॥"
पदच्युत अथवा अधिकारों से वंचित जातक को पुनः मान-सम्मान, पद-प्रतिष्ठा और सामाजिक अधिकार प्राप्त होते हैं।

५. काशी विश्वनाथ की अक्षय कृपा:
साधक को भगवान शिव (काशी विश्वनाथ) और माँ अन्नपूर्णा दोनों का अनुग्रह प्राप्त होकर अंत में मोक्ष की प्राप्ति होती है।"""

english_lyrics = """॥ Shri Annapurna Mata Chalisa ॥

॥ Doha ॥
Vishweshwara-Padapadama Kee, Raja-Nija Sheesha-Lagaaya।
Annapoorne! Tava Suyasha, Baranoun Kavi-Matilaaya॥

॥ Chaupai ॥
Nitya Aananda Karinee Maataa। Vara-Aru Abhaya Bhaava Prakhyaataa॥1॥
Jaya! Saundarya Sindhu Jaga-Jananee। Akhila Paapa Hara Bhava-Bhaya Haranee॥2॥
Shweta Badana Para Shweta Basana Puni। Santana Tuva Pada Sevata Rishimuni॥3॥
Kaashee Puraadheeshwaree Maataa। Maaheshwaree Sakala Jaga-Traataa॥4॥
Brishabhaarudha Naama Rudraanee। Vishwa Vihaarini Jaya! Kalyaanee॥5॥
Padidevataa Suteeta Shiromani। Padavee Praapta Keenh Giri-Nandini॥6॥
Pati Vichhoha Dukha Sahi Nahi Paavaa। Yoga Agni Taba Badana Jaraavaa॥7॥
Deha Tajata Shiva-Charana Sanehoo। Raakhehu Jaate Himagiri-Gehoo॥8॥
Prakatee Girijaa Naama Dharaayo। Ati Aananda Bhavana Manha Chhaayo॥9॥
Naarada Ne Taba Tohin Bharamaayahu। Byaaha Karana Hita Paatha Padhaayahu॥10॥
Brahmaa-Varuna-Kubera Ganaaye। Devaraaja Aadika Kahi Gaaya॥11॥
Saba Devana Ko Sujasa Bakhaanee। Matipalatana Kee Mana Manha Thaanee॥12॥
Achala Raheen Tuma Prana Para Dhanyaa। Keehnee Siddha Himaachala Kanyaa॥13॥
Nija Kau Tava Naarada Ghabaraaye। Taba Prana-Poorana Mantra Padhaaye॥14॥
Karana Hetu Tapa Tohin Upadeshe-u। Santa-Bachana Tuma Satya Parekhehu॥15॥
Gaganagiraa Suni Taree Na Taare। Brahmaa, Taba Tuva Paasa Padhaare॥16॥
Kahe-u Putri Vara Maangu Anoopaa। Dehun Aaja Tuva Mati Anuroopaa॥17॥
Tuma Tapa Keenha Alaukika Bhaaree। Kashta Uthaayehu Ati Sukumaaree॥18॥
Aba Sandeha Chhaandi Kachhu Moson। Hai Saugandha Naheen Chhala Toson॥19॥
Karata Veda Vida Brahmaa Jaanahu। Vachana Mora Yaha Saancho Maanahu॥20॥
Taji Sankocha Kahahu Nija Ichchhaa। Dehaun Main Mana Maanee Bhikshaa॥21॥
Suni Brahmaa Kee Madhuree Baanee। Mukhason Kachhu Musukaayi Bhavaanee॥22॥
Bolee Tuma Kaa Kahahu Vidhaataa। Tuma To Jagake Srashtaadhaataa॥23॥
Mama Kaamanaa Gupta Nahin Tonson। Kahavaavaa Chaahahu Kaa Moson॥24॥
Igya Yagya Mahan Maratee Baaraa। Shambhunaatha Puni Hohin Hamaaraa॥25॥
So Aba Milahin Mohin Manabhaaya। Kahi Tathaastu Vidhi Dhaama Sidhaaye॥26॥
Taba Girijaa Shankara Tava Bhaya-oo। Phala Kaamanaa Sanshaya Gaya-oo॥27॥
Chandrakoti Ravi Koti Prakaashaa। Taba Aanana Mahan Karata Nivaasaa॥28॥
Maalaa Pustaka Ankusha Sohai। Karamänha Apara Paasha Mana Mohe॥29॥
Annapoorne! Sadapoorne। Aja-Anavadya Ananta Apoorne॥30॥
Kripaa Sagaree Kshemankaree Maan। Bhava-Vibhooti Aananda Bharee Maan॥31॥
Kamala Bilochana Vilasita Baale। Devi Kaalike! Chandi Karaale॥32॥
Tuma Kailaasa Maanhi Hvai Girijaa। Vilasee Aanandasaatha Sindhujaa॥33॥
Swarga-Mahaalakshmee Kahalaayee। Martya-Loka Lakshmee Padapaayee॥34॥
Vilasee Saba Manha Sarva Saroopaa। Sevata Tohin Amara Pura-Bhoopaa॥35॥
Jo Padhihahin Yaha Tuva Chaaleesaa। Phala Pa-ihahin Shubha Saakhee Eesaa॥36॥
Praata Samaya Jo Jana Mana Laayo। Padhihahin Bhakti Suruchi Aghikaayo॥37॥
Stree-Kalatra Pati Mitra-Putra Yuta। Paramaiswarya Laabha Lahi Adbhuta॥38॥
Raaja Vimukhako Raaja Divaavai। Jasa Tero Jana-Sujasa Badhaavai॥39॥
Paatha Mahaa Muda Mangala Daataa। Bhakta Mano VaanChhita Nidhipaataa॥40॥

॥ Doha ॥
Jo Yaha Chaaleesaa Subhaga, Padhi Naavahinge Maatha।
Tinake Kaaraja Siddha Saba, Saakhee Kaashee Naatha॥"""

# 1. Update drik_chalisa_40 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

found = False
for item in cols["devi"]["items"]:
    if item["id"] == "drik_chalisa_40":
        item["title"] = "श्री अन्नपूर्णा माता चालीसा"
        item["title_en"] = "Shri Annapurna Mata Chalisa"
        item["en_line"] = "Nitya Ananda Karini Mata"
        item["hi_line"] = "नित्य आनंद करिणी माता"
        item["sub"] = "नित्य आनंद करिणी माता • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_annapurna_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=u8AEQrYuHbc"
        item["video_id"] = "u8AEQrYuHbc"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/annapurna-mata/annapurna-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "अन्न-धन-ऐश्वर्य प्रदायिनी काशीपुराधीश्वरी भगवती अन्नपूर्णा माता"
        item["section"] = "दिव्य देवी माता चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        found = True
        break

if not found:
    print("ERROR: drik_chalisa_40 not found in devi category!")
    sys.exit(1)

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_40 in drik_chalisa_collections.json successfully!")

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

# 3. Add or update chalisa_annapurna in CONTENT in app.js
content_obj = {
    "title": "श्री अन्नपूर्णा माता चालीसा",
    "title_en": "Shri Annapurna Mata Chalisa",
    "en_line": "Nitya Ananda Karini Mata",
    "hi_line": "नित्य आनंद करिणी माता",
    "sub": "नित्य आनंद करिणी माता • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_annapurna_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=u8AEQrYuHbc",
    "video_id": "u8AEQrYuHbc",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/annapurna-mata/annapurna-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "अन्न-धन-ऐश्वर्य प्रदायिनी काशीपुराधीश्वरी भगवती अन्नपूर्णा माता",
    "section": "दिव्य देवी माता चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

annapurna_content_js = "  chalisa_annapurna: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_annapurna: {" in app_text:
    pos_s = app_text.find("  chalisa_annapurna: {")
    pos_next = app_text.find("\n  chalisa_", pos_s + 1)
    if pos_next == -1:
        pos_next = app_text.find("\n  sundarkand:", pos_s + 1)
    app_text = app_text[:pos_s] + annapurna_content_js + app_text[pos_next+1:]
    print("Replaced existing chalisa_annapurna in CONTENT!")
else:
    # Insert right before chalisa_saraswati (after chalisa_bagalamukhi)
    pos_saras = app_text.find("  chalisa_saraswati: {")
    if pos_saras != -1:
        app_text = app_text[:pos_saras] + annapurna_content_js + app_text[pos_saras:]
        print("Inserted chalisa_annapurna before chalisa_saraswati in CONTENT!")
    else:
        # fallback: insert before sundarkand
        pos_sun = app_text.find("  sundarkand: {")
        if pos_sun != -1:
            app_text = app_text[:pos_sun] + annapurna_content_js + app_text[pos_sun:]
            print("Inserted chalisa_annapurna before sundarkand in CONTENT!")
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

print("ALL ANNAPURNA UPDATES COMPLETED!")
