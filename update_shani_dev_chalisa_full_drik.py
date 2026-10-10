import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री शनि देव चालीसा ॥
(दशरथ कृत शनि स्तुति आधारित • भाषा: ब्रज / अवधी)

॥ दोहा ॥
श्री शनिश्चर देवजी, सुनहु श्रवण मम् टेर।
कोटि विघ्ननाशक प्रभो, करो न मम् हित बेर॥
तव स्तुति हे नाथ, जोरि जुगल कर करत हौं।
करिये मोहि सनाथ, विघ्नहरन हे रवि सुव्रन॥

॥ चौपाई ॥
शनिदेव मैं सुमिरौं तोही। विद्या बुद्धि ज्ञान दो मोही॥१॥
तुम्हरो नाम अनेक बखानौं। क्षुद्रबुद्धि मैं जो कुछ जानौं॥२॥
अन्तक, कोण, रौद्रय मनाऊँ। कृष्ण बभ्रु शनि सबहिं सुनाऊँ॥३॥
पिंगल मन्दसौरि सुख दाता। हित अनहित सब जग के ज्ञाता॥४॥
नित जपै जो नाम तुम्हारा। करहु व्याधि दुःख से निस्तारा॥५॥
राशि विषमवस असुरन सुरनर। पन्नग शेष सहित विद्याधर॥६॥
राजा रंक रहहिं जो नीको। पशु पक्षी वनचर सबही को॥७॥
कानन किला शिविर सेनाकर। नाश करत सब ग्राम्य नगर भर॥८॥
डालत विघ्न सबहि के सुख में। व्याकुल होहिं पड़े सब दुःख में॥९॥
नाथ विनय तुमसे यह मेरी। करिये मोपर दया घनेरी॥१०॥
मम हित विषम राशि महँवासा। करिय न नाथ यही मम आसा॥११॥
जो गुड़ उड़द दे बार शनीचर। तिल जव लोह अन्न धन बस्तर॥१२॥
दान दिये से होंय सुखारी। सोइ शनि सुन यह विनय हमारी॥१३॥
नाथ दया तुम मोपर कीजै। कोटिक विघ्न क्षणिक महँ छीजै॥१४॥
वंदत नाथ जुगल कर जोरी। सुनहु दया कर विनती मोरी॥१५॥
कबहुँक तीरथ राज प्रयागा। सरयू तोर सहित अनुरागा॥१६॥
कबहुँ सरस्वती शुद्ध नार महँ। या कहुँ गिरी खोह कंदर महँ॥१७॥
ध्यान धरत हैं जो जोगी जनि। ताहि ध्यान महँ सूक्ष्म होहि शनि॥१८॥
है अगम्य क्या करूँ बड़ाई। करत प्रणाम चरण शिर नाई॥१९॥
जो विदेश से बार शनीचर। मुड़कर आवेगा निज घर पर॥२०॥
रहैं सुखी शनि देव दुहाई। रक्षा रवि सुत रखैं बनाई॥२१॥
जो विदेश जावैं शनिवारा। गृह आवैं नहिं सहै दुखारा॥२२॥
संकट देय शनीचर ताही। जेते दुखी होई मन माही॥२३॥
सोई रवि नन्दन कर जोरी। वन्दन करत मूढ़ मति थोरी॥२४॥
ब्रह्मा जगत बनावन हारा। विष्णु सबहिं नित देत अहारा॥२५॥
हैं त्रिशूलधारी त्रिपुरारी। विभू देव मूरति एक वारी॥२६॥
इकहोइ धारण करत शनि नित। वंदत सोई शनि को दमनचित॥२७॥
जो नर पाठ करै मन चित से। सो नर छूटै व्यथा अमित से॥२८॥
हौं सुपुत्र धन सन्तति बाढ़े। कलि काल कर जोड़े ठाढ़े॥२९॥
पशु कुटुम्ब बांधन आदि से। भरो भवन रहिहैं नित सबसे॥३०॥
नाना भाँति भोग सुख सारा। अन्त समय तजकर संसारा॥३१॥
पावै मुक्ति अमर पद भाई। जो नित शनि सम ध्यान लगाई॥३२॥
पढ़ै प्रात जो नाम शनि दस। रहैं शनिश्चर नित उसके बस॥३३॥
पीड़ा शनि की कबहुँ न होई। नित उठ ध्यान धरै जो कोई॥३४॥
जो यह पाठ करैं चालीसा। होय सुख साखी जगदीशा॥३५॥
चालिस दिन नित पढ़ै सबेरे। पातक नाशै शनी घनेरे॥३६॥
रवि नन्दन की अस प्रभुताई। जगत मोहतम नाशै भाई॥३७॥
याको पाठ करै जो कोई। सुख सम्पति की कमी न होई॥३८॥
निशिदिन ध्यान धरै मनमाहीं। आधिव्याधि ढिंग आवै नाहीं॥३९॥

॥ दोहा ॥
पाठ शनिश्चर देव को, कीहौं 'विमल' तैयार।
करत पाठ चालीस दिन, हो भवसागर पार॥
जो स्तुति दशरथ जी कियो, सम्मुख शनि निहार।
सरस सुभाषा में वही, ललिता लिखें सुधार॥"""

meaning = """॥ श्री शनि देव चालीसा (शनिदेव मैं सुमिरौं तोहीं) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "श्री शनिश्चर देवजी, सुनहु श्रवण मम् टेर। कोटि विघ्ननाशक प्रभो, करो न मम् हित बेर॥"
भावार्थ: हे भगवान श्री शनिश्चर देव जी! कृपा कर अपने पावन कानों से मुझ दीन-हीन सेवक की पुकार (टेर) सुनिए। हे करोड़ों विघ्नों और संकटों का नाश करने वाले समर्थ प्रभु! मेरे कल्याण में अब तनिक भी विलंब (देरी) न कीजिए।
• "तव स्तुति हे नाथ, जोरि जुगल कर करत हौं। करिये मोहि सनाथ, विघ्नहरन हे रवि सुव्रन॥"
भावार्थ: हे नाथ! मैं अपने दोनों हाथ जोड़कर आपकी पवित्र स्तुति करता हूँ। हे समस्त विघ्नों को हरने वाले सूर्यपुत्र (रवि सुत)! मुझ अनाथ पर कृपा कर मुझे सनाथ (संरक्षित) कीजिए।

【३९ चौपाइयां — भावार्थ】
१. "शनिदेव मैं सुमिरौं तोही। विद्या बुद्धि ज्ञान दो मोही॥"
भावार्थ: हे शनिदेव! मैं अनन्य भाव से आपका ध्यान व स्मरण करता हूँ। आप मुझे निर्मल विद्या, सद्बुद्धि और आत्मज्ञान प्रदान कीजिए।

२. "तुम्हरो नाम अनेक बखानौं। क्षुद्रबुद्धि मैं जो कुछ जानौं॥"
भावार्थ: आपके अनंत दिव्य नाम और महिमा हैं। अपनी अल्प व क्षुद्र बुद्धि से जो कुछ भी मैं जानता हूँ, उसी के अनुसार आपके पावन नामों का गान करता हूँ।

३. "अन्तक, कोण, रौद्रय मनाऊँ। कृष्ण बभ्रु शनि सबहिं सुनाऊँ॥"
भावार्थ: मैं अंतक (काल स्वरूप), कोणस्थ (कोणीय दृष्टि वाले), रौद्र (तेजस्वी उग्र स्वरूप), कृष्ण (श्यामल वर्ण), बभ्रु (भूरे-धूसर वर्ण) और शनि नामों का कीर्तन कर सबको सुनाता हूँ और आपको मनाता हूँ।

४. "पिंगल मन्दसौरि सुख दाता। हित अनहित सब जग के ज्ञाता॥"
भावार्थ: आप पिंगल (अग्नि सम कांति वाले), मंद (मन्द गति से चलने वाले), सौरी (सूर्यपुत्र) तथा समस्त सुखों के दाता हैं। संसार में किसका क्या हित है और क्या अहित—आप संपूर्ण कर्मों के परम ज्ञाता हैं।

५. "नित जपै जो नाम तुम्हारा। करहु व्याधि दुःख से निस्तारा॥"
भावार्थ: जो भी मनुष्य प्रतिदिन नियमपूर्वक आपके इन पावन नामों का जप करता है, आप उसके समस्त शारीरिक रोगों, व्याधियों और दुखों का तत्काल निस्तारण (निवारण) कर देते हैं।

६. "राशि विषमवस असुरन सुरनर। पन्नग शेष सहित विद्याधर॥"
भावार्थ: जब आपकी दृष्टि किसी विषम (प्रतिकूल) राशि पर पड़ती है, तो क्या असुर, क्या देवता और क्या मनुष्य—यहाँ तक कि पाताल के शेषनाग और गंधर्व-विद्याधर भी आपके प्रभाव से कांप उठते हैं।

७. "राजा रंक रहहिं जो नीको। पशु पक्षी वनचर सबही को॥"
भावार्थ: जो राजा महलों में सुखी रहते हैं वे रंक (कंगाल) हो जाते हैं, और वन के पशु-पक्षी तथा समस्त प्राणी आपके प्रभाव क्षेत्र में आ जाते हैं।

८. "कानन किला शिविर सेनाकर। नाश करत सब ग्राम्य नगर भर॥"
भावार्थ: आपकी वक्र दृष्टि और प्रतिकूल दशा से अभिमानी राजाओं के वन, सुदृढ़ किले, सैन्य छावनियां, संपूर्ण सेना, और यहाँ तक कि भरे-पूरे गांव व नगर नष्ट-भ्रष्ट हो जाते हैं।

९. "डालत विघ्न सबहि के सुख में। व्याकुल होहिं पड़े सब दुःख में॥"
भावार्थ: आप पापकर्मियों के सुखों में विघ्न डाल देते हैं, जिससे वे व्याकुल होकर कष्टों के चक्रव्यूह में पड़ जाते हैं और आत्ममंथन करने पर विवश होते हैं।

१०. "नाथ विनय तुमसे यह मेरी। करिये मोपर दया घनेरी॥"
भावार्थ: हे नाथ! आपसे मेरी यही करबद्ध प्रार्थना है कि मुझ अकिंचन भक्त पर अपनी असीम व घनी दया दृष्टि बनाए रखिए।

११. "मम हित विषम राशि महँवासा। करिय न नाथ यही मम आसा॥"
भावार्थ: हे कृपालु प्रभु! मेरी जन्मराशि में विषम (हानिकारक) गोचर व वास कभी न कीजिए; मुझ पर सदा अपनी सौम्य और कल्याणकारी दृष्टि रखिए—मेरी आपसे यही एकमात्र आशा है।

१२-१३. "जो गुड़ उड़द दे बार शनीचर। तिल जव लोह अन्न धन बस्तर॥ दान दिये से होंय सुखारी। सोइ शनि सुन यह विनय हमारी॥"
भावार्थ: जो साधक शनिवार के दिन गुड़, काली उड़द, काले तिल, जौ, लोहा, अन्न, धन और काले वस्त्रों का श्रद्धापूर्वक दान करता है, वह समस्त संकटों से छूटकर सुखी होता है। हे शनिदेव! मेरी यह विनम्र प्रार्थना सुनिए।

१४-१५. "नाथ दया तुम मोपर कीजै। कोटिक विघ्न क्षणिक महँ छीजै॥ वंदत नाथ जुगल कर जोरी। सुनहु दया कर विनती मोरी॥"
भावार्थ: हे नाथ! मुझ पर दया कीजिए जिससे मेरे जीवन के करोड़ों विघ्न-बाधाएं क्षण मात्र में नष्ट हो जाएं। मैं दोनों हाथ जोड़कर वंदना करता हूँ, मेरी विनती सुनिए।

१६-१९. "कबहुँक तीरथ राज प्रयागा... करत प्रणाम चरण शिर नाई॥"
भावार्थ: कभी तीर्थराज प्रयाग, कभी सरयू तट, कभी पवित्र सरस्वती नदी के किनारे तो कभी दुर्गम पर्वत-कंदराओं में जो तपस्वी योगी ध्यान लगाते हैं, उनके अंतर्मन में आप सूक्ष्म रूप से प्रकट होते हैं। हे प्रभु! आपकी महिमा अत्यंत अगम्य और अपार है; मैं आपके चरणों में शीश नवाकर बारम्बार प्रणाम करता हूँ।

२०-२१. "जो विदेश से बार शनीचर। मुड़कर आवेगा निज घर पर॥ रहैं सुखी शनि देव दुहाई। रक्षा रवि सुत रखैं बनाई॥"
भावार्थ: जो व्यक्ति शनिवार के दिन परदेश/विदेश से अपने घर लौटता है, वह सदा सुखी रहता है और सूर्यपुत्र शनिदेव उसकी सब प्रकार से रक्षा करते हैं।

२२-२३. "जो विदेश जावैं शनिवारा। गृह आवैं नहिं सहै दुखारा॥ संकट देय शनीचर ताही। जेते दुखी होई मन माही॥"
भावार्थ: परंतु जो व्यक्ति शनिवार के दिन परदेश यात्रा पर प्रस्थान करता है, वह यात्रा में भारी कष्ट और विघ्न झेलता है। शनिदेव उसे संकटों का अनुभव कराते हैं जिससे वह मन में दुखी होता है।

२४-२७. "सोई रवि नन्दन कर जोरी... वंदत सोई शनि को दमनचित॥"
भावार्थ: वही सूर्यपुत्र शनिदेव जगत के सृष्टा ब्रह्मा, पालनकर्ता भगवान विष्णु, और त्रिशूलधारी महादेव शिव—इन तीनों दिव्य स्वरूपों की शक्तियों को एकाकार रूप में धारण करते हैं। ऐसे परम प्रभु शनिदेव की मैं एकाग्रचित्त होकर वंदना करता हूँ।

२८-३२. "जो नर पाठ करै मन चित से... जो नित शनि सम ध्यान लगाई॥"
भावार्थ: जो मनुष्य एकाग्रचित्त होकर इस पावन चालीसा का पाठ करता है, वह अनगिनत व्यथाओं से मुक्त हो जाता है। उसके घर में सुपुत्र, धन, वंश-वृद्धि होती है और स्वयं कलिकाल भी हाथ जोड़कर दूर रहता है। पशु, कुटुम्ब और संपदा से उसका भवन भरा रहता है, वह सांसारिक सुख भोगकर अंत में मोक्ष पद प्राप्त करता है।

३३-३६. "पढ़ै प्रात जो नाम शनि दस... पातक नाशै शनी घनेरे॥"
भावार्थ: जो नित्य प्रातःकाल शनिदेव के दस पावन नामों का पाठ करता है, उस पर शनिदेव सदा प्रसन्न रहते हैं। उसे कभी शनि पीड़ा नहीं सताती। चालीस दिनों तक प्रातःकाल इसका पाठ करने से जीवन के घोर से घोर पाप भस्म हो जाते हैं।

३७-३९. "रवि नन्दन की अस प्रभुताई... आधिव्याधि ढिंग आवै नाहीं॥"
भावार्थ: सूर्यपुत्र शनिदेव की ऐसी अद्भुत महिमा है कि यह पाठ संसार के अज्ञान और मोहरूपी अंधकार को नष्ट कर देता है। इसके पाठ से सुख-संपत्ति की कभी कमी नहीं होती और किसी प्रकार की आधि-व्याधि (शारीरिक व मानसिक रोग) पास नहीं फटकती।

【समापन दोहे】
• "पाठ शनिश्चर देव को, कीहौं 'विमल' तैयार। करत पाठ चालीस दिन, हो भवसागर पार॥"
भावार्थ: भगवान शनिश्चर देव का यह निर्मल चालीसा पाठ तैयार किया गया है। जो साधक चालीस दिनों तक इसका नित्य पाठ करता है, वह इस भवसागर से सहज ही पार उतर जाता है।
• "जो स्तुति दशरथ जी कियो, सम्मुख शनि निहार। सरस सुभाषा में वही, ललिता लिखें सुधार॥"
भावार्थ: जिस पावन स्तुति को चक्रवर्ती राजा दशरथ जी ने साक्षात् शनिदेव के सम्मुख खड़े होकर किया था (जिससे प्रसन्न होकर शनिदेव ने अकाल निवारण का वरदान दिया था), उसी ऐतिहासिक स्तुति को कवि ललिता प्रसाद जी ने परिष्कृत कर जन-कल्याण हेतु सरल व सरस लोकभाषा में रचा है।"""

vidhi = """॥ श्री शनि देव चालीसा (दशरथ स्तुति आधारित) — शास्त्रोक्त पाठ विधि व नियम ॥

१. पाठ का पावन समय:
- शनिवार का दिन, विशेषकर प्रातःकाल सूर्योदय के समय अथवा सांध्यकाल सूर्यास्त के उपरांत प्रदोष वेला।
- शनि प्रदोष, शनि अमावस्या, अथवा शनिवार से आरंभ करके लगातार ४० दिनों का नियमबद्ध पाठ सर्वश्रेष्ठ फल प्रदान करता है।

२. पूजा स्थल व दिशा:
- पूजा स्थल में पश्चिम दिशा की ओर मुख करके बैठें, क्योंकि पश्चिम दिशा के अधिपति स्वयं भगवान शनिदेव हैं।
- काले या गहरे नीले रंग के ऊनी अथवा कुशा के आसन पर बैठें।

३. विशिष्ट दशरथ-पद्धति पूजन सामग्री:
- लोहे या मिट्टी के दीपक में शुद्ध सरसों का तेल अथवा काले तिल का तेल।
- काले तिल, साबुत उड़द, लोहे की कील, नीला अपराजिता पुष्प या नीलकमल।
- भोग हेतु गुड़, तिलकुट, या काली उड़द की खिचड़ी।
- तांबे या कांसे के पात्र में जल, कच्चा दूध और काले तिल।

४. छाया-दान विधि (विशेष फलदायी):
- एक कटोरी में सरसों का तेल लेकर उसमें अपना मुख (चेहरा) देखें।
- तदोपरांत उस तेल को किसी शनि मंदिर में दान कर दें अथवा पीपल की जड़ में अर्पित करें। इससे कुंडली के समस्त अरिष्ट शांत होते हैं।

५. यात्रा संबंधी विशेष निर्देश (चालीसा अनुसार):
- चालीसा के निर्देशानुसार शनिवार के दिन परदेश से अपने घर लौटना अत्यंत शुभ होता है।
- शनिवार के दिन नए परदेश गमन या लंबी यात्रा आरंभ करने से बचें।

६. पाठ का क्रम:
- सर्वप्रथम आचमन व शुद्धि करके भगवान गणेश जी और सूर्यपुत्र शनिदेव का ध्यान करें।
- 'ॐ शं शनैश्चराय नमः' अथवा 'ॐ प्रां प्रीं प्रौं सः शनैश्चराय नमः' मंत्र का ११ बार जप करें।
- श्रद्धापूर्वक एकाग्रचित्त होकर चालीसा का पाठ करें (१, ३, ७ या ११ पाठ)।
- पाठ समाप्ति के पश्चात शनिदेव की आरती करें और किसी असहाय, निर्धन, दिव्यांग अथवा सफाईकर्मी को भोजन व वस्त्र दान करें।"""

significance = """॥ श्री शनि देव चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. राजा दशरथ कृत शनि स्तुति का पावन फल:
पद्म पुराण व स्कंद पुराण में वर्णित है कि जब शनिदेव रोहिणी नक्षत्र का भेदन करने वाले थे, जिससे पृथ्वी पर १२ वर्षों का भयंकर अकाल पड़ने वाला था, तब अयोध्यापति राजा दशरथ ने साक्षात् शनिदेव के सम्मुख जाकर इस अद्भुत स्तुति द्वारा उन्हें प्रसन्न किया था। शनिदेव ने प्रसन्न होकर राजा दशरथ को वरदान दिया था कि जो भी इस स्तुति का पाठ करेगा, उसे कभी अकाल, दरिद्रता या शनि पीड़ा नहीं सताएगी।

२. शनि की विषम राशि (साढ़ेसाती व ढैय्या) से रक्षा:
"मम हित विषम राशि महँवासा। करिय न नाथ यही मम आसा॥"
जब शनिदेव जातक की कुंडली में प्रतिकूल राशियों (१२वीं, पहली, दूसरी या चौथी, आठवीं) में गोचर करते हैं, तब यह चालीसा एक अभेद्य सुरक्षा कवच बनकर जातक के मान-सम्मान, धन और स्वास्थ्य की रक्षा करती है।

३. त्रिदेवों की समन्वित ऊर्जा:
इस चालीसा में उद्घाटित है कि शनिदेव केवल एक ग्रह नहीं हैं, अपितु वे सृष्टिकर्ता ब्रह्मा, पालनकर्ता श्री हरि विष्णु और संहारकर्ता देवाधिदेव महादेव—इन तीनों की न्यायकारी शक्ति को एक रूप में धारण करते हैं।

४. दस पावन नामों का अचूक प्रभाव:
चालीसा में वर्णित शनिदेव के दस नाम—अन्तक, कोणस्थ, रौद्र, कृष्ण, बभ्रु, शनि, पिंगल, मन्द, सौरी, और दुःखभंजन—का नित्य प्रातः स्मरण करने से भयानक से भयानक संकट और व्याधियां नष्ट हो जाती हैं।

५. ४० दिनों का अखंड सिद्धि अनुष्ठान:
"करत पाठ चालीस दिन, हो भवसागर पार"
चालीस दिनों तक नियम, ब्रह्मचर्य और सात्विकता के साथ इस चालीसा का पाठ करने से मुकदमों में विजय, कर्जमुक्ति, व्यापार में स्थिरता और जीवन के अंतिम काल में सद्गति की प्राप्ति होती है।"""

english_lyrics = """॥ Shri Shani Deva Chalisa ॥
(Based on King Dasharatha's Stuti)

॥ Doha ॥
Shri Shanishchara Devaji, Sunahu Shravana Mam Tera।
Koti Vighnanaashaka Prabho, Karo Na Mam Hita Bera॥
Tava Stuti He Naatha, Jori Jugala Kara Karata Haun।
Kariye Mohi Sanaatha, Vighnaharana He Ravi Suvrana॥

॥ Chaupai ॥
Shanideva Main Sumirau Tohee। Vidyaa Buddhi Gyaana Do Mohee॥1॥
Tumharo Naama Aneka Bakhaanau। Kshudrabuddhi Main Jo Kuchha Jaanau॥2॥
Antaka, Kona, Raudraya Manaa-oon। Krishna Babhru Shani Sabahin Sunaa-oon॥3॥
Pingala Mandasauri Sukha Daataa। Hita Anahita Saba Jaga Ke Gyaataa॥4॥
Nita Japai Jo Naama Tumhaaraa। Karahu Vyaadhi Dukha Se Nistaaraa॥5॥
Raashi Vishamavasa Asurana Suranara। Pannaga Shesha Sahita Vidyaadhara॥6॥
Raajaa Ranka Rahahin Jo Neeko। Pashu Pakshee Vanachara Sabahee Ko॥7॥
Kaanana Kilaa Shivira Senaakara। Naasha Karata Saba Graamya Nagara Bhara॥8॥
Daalata Vighna Sabahi Ke Sukha Men। Vyaakula Hohin Pade Saba Dukha Men॥9॥
Naatha Vinaya Tumase Yaha Meree। Kariye Mopara Dayaa Ghaneree॥10॥
Mama Hita Vishama Raashi Mahanvaasaa। Kariya Na Naatha Yahee Mama Aasaa॥11॥
Jo Guda Udada De Baara Shaneechara। Tila Java Loha Anna Dhana Bastara॥12॥
Daana Diye Se Hoyan Sukhaaree। So-i Shani Suna Yaha Vinaya Hamaaree॥13॥
Naatha Dayaa Tuma Mopara Keejai। Kotika Vighna Kshanika Mahan Chheejai॥14॥
Vandata Naatha Jugala Kara Joree। Sunahu Dayaa Kara Vinatee Moree॥15॥
Kabahunk Teeratha Raaja Prayaagaa। Sarayoo Tora Sahita Anuraagaa॥16॥
Kabahun Saraswatee Shuddha Naara Mahan। Yaa Kahun Giree Khoha Kandara Mahan॥17॥
Dhyaana Dharata Hain Jo Jogee Jani। Taahi Dhyaana Mahan Sookshma Hohin Shani॥18॥
Hai Agamya Kyaa Karoon Badaa-ee। Karata Pranaama Charana Shira Naa-ee॥19॥
Jo Videsha Se Baara Shaneechara। Mudakara Aavegaa Nija Ghara Para॥20॥
Rahain Sukhee Shani Deva Duhaa-ee। Rakshaa Ravi Suta Rakhain Banaa-ee॥21॥
Jo Videsha Jaavain Shanivaaraa। Griha Aavain Nahin Sahai Dukhaaraa॥22॥
Sankata Deya Shaneechara Taahee। Jete Dukhee Ho-ee Mana Maahee॥23॥
So-ee Ravi Nandana Kara Joree। Vandana Karata Moodha Mati Thoree॥24॥
Brahmaa Jagata Banaavana Haaraa। Vishnu Sabahin Nita Deta Ahaaraa॥25॥
Hain Trishooladhaaree Tripuraaree। Vibhoo Deva Moorati Eka Vaaree॥26॥
Ikaho-i Dhaarana Karata Shani Nita। Vandata So-ee Shani Ko Damanachita॥27॥
Jo Nara Paatha Karai Mana Chita Se। So Nara Chhootai Vyathaa Amita Se॥28॥
Haun Suputra Dhana Santati Baadhe। Kali Kaala Kara Jode Thaadhe॥29॥
Pashu Kutumba Baandhana Aadi Se। Bharo Bhavana Rahihai Nita Sabase॥30॥
Naanaa Bhaanti Bhoga Sukha Saaraa। Anta Samaya Tajakara Samsaaraa॥31॥
Paavai Mukti Amara Pada Bhaa-ee। Jo Nita Shani Sama Dhyaana Lagaa-ee॥32॥
Padhai Praata Jo Naama Shani Dasa। Rahain Shanishchara Nita Usake Basa॥33॥
Peedaa Shani Kee Kabahun Na Ho-ee। Nita Uthha Dhyaana Dharai Jo Ko-ee॥34॥
Jo Yaha Paatha Karain Chaaleesaa। Hoya Sukha Saakhee Jagadeeshaa॥35॥
Chaalisa Dina Nita Padhai Sabere। Paataka Naashai Shanee Ghanere॥36॥
Ravi Nandana Kee Asa Prabhutaa-ee। Jagata Mohatama Naashai Bhaa-ee॥37॥
Yaako Paatha Karai Jo Ko-ee। Sukha Sampati Kee Kamee Na Ho-ee॥38॥
Nishidina Dhyaana Dharai Manamaaheen। Aadhivyaadhi Dhinga Aavai Naaheen॥39॥

॥ Doha ॥
Paatha Shanishchara Deva Ko, Keehaun 'Vimala' Taiyaara।
Karata Paatha Chaaleesa Dina, Ho Bhavasaagara Paara॥
Jo Stuti Dasharatha Jee Kiyo, Sammukha Shani Nihaara।
Sarasa Subhaashaa Men Vahee, Lalitaa Likhain Sudhaara॥"""

# 1. Update drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["shani"]["items"]:
    if item["id"] == "drik_chalisa_6":
        item["title"] = "श्री शनि देव चालीसा"
        item["title_en"] = "Shri Shani Deva Chalisa (Dasharatha Krut)"
        item["en_line"] = "Shanideva Main Sumirau Tohee"
        item["hi_line"] = "शनिदेव मैं सुमिरौं तोहीं"
        item["sub"] = "शनिदेव मैं सुमिरौं तोहीं • Drik Panchang Verified"
        item["thumb"] = "assets/deity_shanidev.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=RrPjukz4S1c"
        item["video_id"] = "RrPjukz4S1c"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/lord-shani/other/shani-dev-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "कर्मफलदाता भगवान श्री शनिदेव"
        item["section"] = "भगवान शनिदेव चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_6 in drik_chalisa_collections.json successfully!")

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

# 3. Add chalisa_shani_dev in CONTENT in app.js
content_obj = {
    "title": "श्री शनि देव चालीसा",
    "title_en": "Shri Shani Deva Chalisa (Dasharatha Krut)",
    "en_line": "Shanideva Main Sumirau Tohee",
    "hi_line": "शनिदेव मैं सुमिरौं तोहीं",
    "sub": "शनिदेव मैं सुमिरौं तोहीं • Drik Panchang Verified",
    "thumb": "assets/deity_shanidev.jpg",
    "audio_url": "https://www.youtube.com/watch?v=RrPjukz4S1c",
    "video_id": "RrPjukz4S1c",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/lord-shani/other/shani-dev-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "कर्मफलदाता भगवान श्री शनिदेव",
    "section": "भगवान शनिदेव चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

shani_dev_content_js = "  chalisa_shani_dev: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_shani_dev: {" in app_text:
    m_start = app_text.find("  chalisa_shani_dev: {")
    m_end = app_text.find("\n  chalisa_", m_start + 1)
    if m_end != -1:
        app_text = app_text[:m_start] + shani_dev_content_js + app_text[m_end+1:]
        print("Replaced existing chalisa_shani_dev in CONTENT!")
else:
    # Insert right after chalisa_shani
    s_pos = app_text.find("  chalisa_shani: {")
    if s_pos != -1:
        s_end = app_text.find("\n  chalisa_", s_pos + 1)
        if s_end != -1:
            app_text = app_text[:s_end+1] + shani_dev_content_js + app_text[s_end+1:]
            print("Inserted chalisa_shani_dev after chalisa_shani in CONTENT!")
    else:
        # Fallback before chalisa_vishwakarma
        v_pos = app_text.find("  chalisa_vishwakarma: {")
        if v_pos != -1:
            app_text = app_text[:v_pos] + shani_dev_content_js + app_text[v_pos:]
            print("Inserted chalisa_shani_dev before chalisa_vishwakarma in CONTENT!")

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
