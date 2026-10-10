import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री विष्णु चालीसा ॥

॥ दोहा ॥
विष्णु सुनिए विनय, सेवक की चितलाय।
कीरत कुछ वर्णन करूँ, दीजै ज्ञान बताय॥

॥ चौपाई ॥
नमो विष्णु भगवान खरारी। कष्ट नशावन अखिल बिहारी॥१॥
प्रबल जगत में शक्ति तुम्हारी। त्रिभुवन फैल रही उजियारी॥२॥
सुन्दर रूप मनोहर सूरत। सरल स्वभाव मोहनी मूरत॥३॥
तन पर पीताम्बर अति सोहत। बैजन्ती माला मन मोहत॥४॥
शंख चक्र कर गदा बिराजे। देखत दैत्य असुर दल भाजे॥५॥
सत्य धर्म मद लोभ न गाजे। काम क्रोध मद लोभ न छाजे॥६॥
सन्तभक्त सज्जन मनरंजन। दनुज असुर दुष्टन दल गंजन॥७॥
सुख उपजाय कष्ट सब भंजन। दोष मिटाय करत जन सज्जन॥८॥
पाप काट भव सिन्धु उतारण। कष्ट नाशकर भक्त उबारण॥९॥
करत अनेक रूप प्रभु धारण। केवल आप भक्ति के कारण॥१०॥
धरणि धेनु बन तुमहिं पुकारा। तब तुम रूप राम का धारा॥११॥
भार उतार असुर दल मारा। रावण आदिक को संहारा॥१२॥
आप वाराह रूप बनाया। हिरण्याक्ष को मार गिराया॥१३॥
धर मत्स्य तन सिन्धु बनाया। चौदह रतनन को निकलाया॥१४॥
अमिलख असुरन द्वन्द मचाया। रूप मोहनी आप दिखाया॥१५॥
देवन को अमृत पान कराया। असुरन को छबि से बहलाया॥१६॥
कूर्म रूप धर सिन्धु मझाया। मन्द्राचल गिरि तुरत उठाया॥१७॥
शंकर का तुम फन्द छुड़ाया। भस्मासुर को रूप दिखाया॥१८॥
वेदन को जब असुर डुबाया। कर प्रबन्ध उन्हें ढुँढवाया॥१९॥
मोहित बनकर खलहि नचाया। उसही कर से भस्म कराया॥२०॥
असुर जलंधर अति बलदाई। शंकर से उन कीन्ह लड़ाई॥२१॥
हार पार शिव सकल बनाई। कीन सती से छल खल जाई॥२२॥
सुमिरन कीन तुम्हें शिवरानी। बतलाई सब विपत कहानी॥२३॥
तब तुम बने मुनीश्वर ज्ञानी। वृन्दा की सब सुरति भुलानी॥२४॥
देखत तीन दनुज शैतानी। वृन्दा आय तुम्हें लपटानी॥२५॥
हो स्पर्श धर्म क्षति मानी। हना असुर उर शिव शैतानी॥२६॥
तुमने धुरू प्रहलाद उबारे। हिरणाकुश आदिक खल मारे॥२७॥
गणिका और अजामिल तारे। बहुत भक्त भव सिन्धु उतारे॥२८॥
हरहु सकल संताप हमारे। कृपा करहु हरि सिरजन हारे॥२९॥
देखहुँ मैं निज दरश तुम्हारे। दीन बन्धु भक्तन हितकारे॥३०॥
चहत आपका सेवक दर्शन। करहु दया अपनी मधुसूदन॥३१॥
जानूं नहीं योग्य जप पूजन। होय यज्ञ स्तुति अनुमोदन॥३२॥
शीलदया सन्तोष सुलक्षण। विदित नहीं व्रतबोध विलक्षण॥३३॥
करहुँ आपका किस विधि पूजन। कुमति विलोक होत दुख भीषण॥३४॥
करहुँ प्रणाम कौन विधिसुमिरण। कौन भाँति मैं करहुँ समर्पण॥३५॥
सुर मुनि करत सदा सिवकाई। हर्षित रहत परम गति पाई॥३६॥
दीन दुखिन पर सदा सहाई। निज जन जान लेव अपनाई॥३७॥
पाप दोष संताप नशाओ। भव बन्धन से मुक्त कराओ॥३८॥
सुत सम्पति दे सुख उपजाओ। निज चरनन का दास बनाओ॥३९॥
निगम सदा ये विनय सुनावै। पढ़ै सुनै सो जन सुख पावै॥४०॥

॥ दोहा ॥
छवि विलोकि श्रीपति सुख पावै। प्रेम सहित चालीसा गावै॥
विष्णु कृपा सब संकट टारे। भवसागर से पार उतारे॥"""

meaning = """॥ श्री विष्णु चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहा】
• "विष्णु सुनिए विनय, सेवक की चितलाय। कीरत कुछ वर्णन करूँ, दीजै ज्ञान बताय॥"
भावार्थ: हे चराचर जगत के पालनकर्ता भगवान श्रीहरि विष्णु! अपने इस अनन्य सेवक की विनीत प्रार्थना ध्यानपूर्वक चित्त लगाकर सुनिए। मैं आपकी पावन कीर्ति और दिव्य महिमा का अल्प वर्णन करने का प्रयास कर रहा हूँ, कृपा करके मुझे दिव्य ज्ञान, सद्बुद्धि और विवेक प्रदान कीजिए।

【४० चौपाइयां — पद्यवार भावार्थ】
१-४. "नमो विष्णु भगवान खरारी... बैजन्ती माला मन मोहत॥"
भावार्थ: खर नामक दुष्ट दैत्य का संहार करने वाले हे सर्वेश्वर भगवान विष्णु! आपको मेरा बारंबार साष्टांग प्रणाम है। आप संपूर्ण ब्रह्मांड में व्याप्त रहने वाले अखिल बिहारी और अपने शरणागत भक्तों के समस्त संकटों व दुखों का समूल नाश करने वाले हैं। इस चराचर जगत में आपकी शक्ति परम प्रबल और अतुलनीय है; आपके दिव्य तेज से तीनों लोकों में अलौकिक प्रकाश फैल रहा है। आपका रूप अत्यंत सुंदर और सूरत मन को मोहने वाली है; आपका स्वभाव परम सरल, कृपालु और सम्मोहक है। आपके श्यामवर्ण श्रीविग्रह पर पीताम्बर वस्त्र अत्यंत सुशोभित हो रहा है और गले में विराजित वैजयंती माला सभी भक्तों के मनों को मुग्ध कर रही है।

५-८. "शंख चक्र कर गदा बिराजे... दोष मिटाय करत जन सज्जन॥"
भावार्थ: आपके चारों दिव्य कर-कमलों में शंख, सुदर्शन चक्र, कौमोदकी गदा और पद्म कमल शोभायमान हैं; आपके इस भव्य चतुर्भुज स्वरूप और अस्त्र-शस्त्रों को देखते ही दैत्य व असुरों के दल भयभीत होकर भाग खड़े होते हैं। आपमें सत्य और धर्म का पूर्ण वास है; काम, क्रोध, मद और लोभ जैसे विकार आपके समक्ष कभी टिक नहीं सकते। आप साधु, संत, भक्त और सज्जनों के मनों को परमानंद प्रदान करने वाले हैं, तथा दुष्टों, असुरों और दनुजों के दलों का संहार करने वाले हैं। आप भक्तों के जीवन में सुख-शांति उत्पन्न करते हैं और उनके समस्त कष्टों का भंजन (विनाश) करते हैं; आप जीवों के समस्त दोषों और पापों को मिटाकर उन्हें निर्मल व सज्जन बना देते हैं।

९-१२. "पाप काट भव सिन्धु उतारण... रावण आदिक को संहारा॥"
भावार्थ: आप जीवों के संचित पापों को काटकर उन्हें इस दुर्गम भवसागर से पार उतारने वाले हैं और अपने अनन्य भक्तों के संतापों को हरकर उनका उद्धार करते हैं। हे प्रभु! केवल और केवल अपने भक्तों के प्रेम और भक्ति की रक्षा हेतु आप समय-समय पर अनेक दिव्य अवतार और रूप धारण करते हैं। जब-जब पृथ्वी पाप के असह्य भार से व्याकुल होकर गौ का रूप धरकर आपके सम्मुख करुण पुकार करती है, तब-तब आपने मर्यादा पुरुषोत्तम भगवान श्रीराम का पावन रूप धारण किया। आपने धरा का भारी भार उतारकर असुरों की विशाल सेना को नष्ट किया और दशानन रावण, कुंभकर्ण आदि महादुष्टों का संहार करके धर्म की पुनर्स्थापना की।

१३-१६. "आप वाराह रूप बनाया... असुरन को छबि से बहलाया॥"
भावार्थ: जब महादैत्य हिरण्याक्ष पृथ्वी को चुराकर रसातल में ले गया, तब आपने दिव्य वराह रूप धारण करके उसका वध किया और पृथ्वी को जल से बाहर निकालकर उद्धार किया। प्रलयकाल में आपने मत्स्य (मछली) का रूप धारण करके वेदों और बीजों की रक्षा की तथा समुद्र मंथन करवाकर चौदह अमूल्य रत्नों को बाहर प्रकट करवाया। जब अमृत के अधिकार हेतु असुरों ने उत्पात और द्वन्द्व मचाया, तब आपने परम सुंदरी मोहिनी का अलौकिक रूप प्रकट किया। अपनी उस सम्मोहक रूप-छवि से असुरों को मुग्ध व भ्रमित करके, आपने समस्त देवताओं को अमरता प्रदान करने वाला अमृत पान कराया।

१७-२०. "कूर्म रूप धर सिन्धु मझाया... उसही कर से भस्म कराया॥"
भावार्थ: समुद्र मंथन के समय जब मंदराचल पर्वत पाताल में डूबने लगा, तब आपने विशाल कच्छप (कूर्म) रूप धारण कर उस विशाल पर्वत को अपनी पीठ पर धारण कर लिया। जब भस्मासुर ने भगवान शिव को ही भस्म करने की ठानी, तब आपने मोहिनी रूप धारण कर भगवान भोलेनाथ को उस भीषण संकट के फंदे से छुड़ाया। जब हयग्रीव असुर ने वेदों को चुराकर समुद्र की गहराइयों में छिपा दिया, तब आपने मत्स्य रूप से उस असुर का अंत कर वेदों को पुनः ढूंढकर ब्रह्मा जी को सौंपा। मोहिनी रूप में आपने उस दुष्ट भस्मासुर को नृत्य में ऐसा मुग्ध किया कि उसने अपना ही हाथ अपने सिर पर रख लिया और क्षण भर में भस्म हो गया।

२१-२६. "असुर जलंधर अति बलदाई... हना असुर उर शिव शैतानी॥"
भावार्थ: महाबलशाली जलंधर असुर ने जब देवाधिदेव महादेव शिव से युद्ध ठाना, और अपनी पतिव्रता पत्नी वृंदा के सतीत्व के बल पर अजेय होकर शिव जी से छल करने पहुँचा; तब माता पार्वती (शिवरानी) ने आपका स्मरण कर अपनी पूरी विपत्ति सुनाई। तब आपने ज्ञानी मुनीश्वर का रूप धारण कर वृंदा के समक्ष अपनी माया फैलाई, जिससे वृंदा का सतीत्व नियम खंडित हुआ और भगवान शिव उस दुष्ट जलंधर के वक्षस्थल को त्रिशूल से भेदकर उसका संहार कर सके।

२७-३०. "तुमने धुरू प्रहलाद उबारे... दीन बन्धु भक्तन हितकारे॥"
भावार्थ: आपने बालक ध्रुव को अटल पद प्रदान किया और परम भक्त प्रह्लाद की रक्षा हेतु नृसिंह रूप धरकर हिरण्यकश्यप जैसे नराधम का वध किया। आपने गणिका और अजामिल जैसे महापापियों को भी केवल 'नारायण' नाम के प्रभाव से भवसागर से तार दिया और न जाने कितने अगणित भक्तों का उद्धार किया। हे समस्त सृष्टि के रचयिता और पालनकर्ता श्रीहरि! हमारे जीवन के समस्त संतापों, कष्टों और व्याधियों को हर लीजिए और हम पर अपनी अहैतुकी कृपा बरसाइए। हे दीनों के परम सखा और भक्तों का सर्वदा कल्याण करने वाले प्रभु! मेरी यही अभिलाषा है कि मुझे आपके दिव्य दर्शन प्राप्त हों।

३१-३५. "चहत आपका सेवक दर्शन... कौन भाँति मैं करहुँ समर्पण॥"
भावार्थ: हे मधुसूदन! आपका यह दास केवल आपके दर्शनों का प्यासा है, कृपा करके मुझ अकिंचन पर अपनी करुणा दृष्टि कीजिए। मैं न तो किसी गूढ़ जप-तप को जानता हूँ, न विधिपूर्वक पूजन करना जानता हूँ, और न ही मेरे पास यज्ञ-अनुष्ठान व वैदिक स्तुतियों का कोई ज्ञान है। मुझमें न तो शील है, न दया, न संतोष और न कोई उत्तम लक्षण हैं; न ही मुझे किसी विलक्षण व्रत और नियमों का बोध है। मैं भला आपकी पूजा किस विधि से करूँ? अपनी दुर्बुद्धि और अज्ञान को देखकर मेरे हृदय में भीषण दुख उत्पन्न होता है। हे प्रभु! मैं किस विधि से आपका स्मरण व साष्टांग प्रणाम करूँ और किस भाँति स्वयं को आपके पावन चरणों में पूर्ण समर्पित करूँ?

३६-४०. "सुर मुनि करत सदा सिवकाई... पढ़ै सुनै सो जन सुख पावै॥"
भावार्थ: समस्त देवता, ऋषि और मुनिजन निरंतर आपकी पावन सेवा करते हैं और आपके ध्यान से हर्षित होकर परम गति (मोक्ष) को प्राप्त होते हैं। आप दीन-दुखियों के सदा सबसे बड़े सहायक और रक्षक हैं; मुझे अपना ही जन समझकर अपने श्रीचरणों में अपना लीजिए। हे प्रभु! मेरे समस्त पापों, दोषों और संतापों को नष्ट कर दीजिए और मुझे इस जन्म-मरण के सांसारिक बंधनों से सदा के लिए मुक्त कर दीजिए। मुझे सुपुत्र, सद्बुद्धि, सुमति, आत्मिक सुख व समृद्धि प्रदान कीजिए और मुझे अपने युगल पावन चरणों का अनन्य दास बना लीजिए। वेद-शास्त्र और निगम सदा यही प्रार्थना सुनाते हैं कि जो भी मनुष्य प्रेमपूर्वक इस श्री विष्णु चालीसा का पाठ करता है या इसे सुनता है, वह संसार के समस्त सुखों को प्राप्त करता हुआ अंत में परम पद को प्राप्त करता है।

【समापन दोहा】
• "छवि विलोकि श्रीपति सुख पावै। प्रेम सहित चालीसा गावै॥ विष्णु कृपा सब संकट टारे। भवसागर से पार उतारे॥"
भावार्थ: लक्ष्मीपति भगवान विष्णु के इस दिव्य रूप का दर्शन कर भक्त परम सुख और परमानंद की प्राप्ति करता है। जो भी प्राणी प्रेम व श्रद्धा सहित इस विष्णु चालीसा का गान करता है, श्रीहरि विष्णु की कृपा से उसके समस्त संकट टल जाते हैं और वह सहज ही इस भवसागर से पार उतर जाता है।"""

vidhi = """॥ श्री विष्णु चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल सूर्योदय वेला, ब्रह्ममुहूर्त, अथवा सांध्यकाल गोधूलि वेला।
- सर्वोत्तम वार: प्रत्येक गुरुवार (बृहस्पतिवार), जो भगवान श्रीहरि विष्णु व देवगुरु बृहस्पति को समर्पित है।
- महापर्व व पावन तिथियां: प्रत्येक मास के दोनों पक्षों की एकादशी (निर्जला, देवशयनी, देवप्रबोधिनी, कामदा, मोक्षदा आदि), कार्तिक मास, वैशाख मास, अनंत चतुर्दशी, अक्षय तृतीया, गुरु पूर्णिमा एवं सत्यनारायण व्रत के दिन।

२. दिशा, आसन व वस्त्र:
- दिशा: पूर्व अथवा उत्तर दिशा की ओर मुख करके बैठना सर्वोत्तम माना गया है।
- आसन: पीले रंग का रेशमी अथवा ऊनी आसन बिछाएं।
- वस्त्र: साधक को पीले रंग के स्वच्छ व पवित्र वस्त्र (पीताम्बर) धारण करने चाहिए, क्योंकि पीला रंग भगवान विष्णु को अतिशय प्रिय है।

३. पूजन सामग्री व प्रिय नैवेद्य:
- दीपक: गाय के शुद्ध देशी घी का दीपक प्रज्वलित करें।
- पुष्प व तिलक: पीले पुष्प (गेंदा, पीला गुलाब, कनेर, कमल), पीला चंदन अथवा केसर-चंदन का तिलक लगाएं।
- तुलसी दल (अति अनिवार्य): भगवान विष्णु के पूजन और भोग में 'तुलसी दल' अनिवार्य रूप से अर्पित करें; बिना तुलसी पत्र के भगवान विष्णु भोग स्वीकार नहीं करते।
- प्रिय नैवेद्य: भुने हुए चने की दाल व गुड़, बेसन के लड्डू, पंजीरी, पंचामृत, पीले ऋतुफल (केला), तथा केसरिया खीर।

४. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन व पवित्रीकरण करें: 'ॐ अपवित्रः पवित्रो वा सर्वावस्थां गतोऽपि वा। यः स्मरेत्पुण्डरीकाक्षं स बाह्याभ्यन्तरः शुचिः॥'
- भगवान विष्णु और माता महालक्ष्मी के युगल स्वरूप का ध्यान करें।
- 'ॐ नमो भगवते वासुदेवाय' अथवा 'ॐ नमो नारायणाय' मन्त्र का कम से कम १ माला (१०८ बार) जप अवश्य करें।
- इसके पश्चात शांत व एकाग्र चित्त से 'श्री विष्णु चालीसा' का १, ३, ५ अथवा ११ बार पाठ करें।
- पाठ के उपरांत भगवान श्रीहरि विष्णु की पावन आरती ('ॐ जय जगदीश हरे') गाएं और चरणामृत व प्रसाद वितरण करें।"""

significance = """॥ श्री विष्णु चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. जगत के पालनकर्ता का प्रत्यक्ष रक्षा कवच:
"शंख चक्र कर गदा बिराजे। देखत दैत्य असुर दल भाजे॥"
भगवान विष्णु संपूर्ण ब्रह्मांड के पालनकर्ता और नियामक हैं। चालीसा का नित्य पाठ करने वाले साधक के जीवन में सुदर्शन चक्र की भांति एक अभेद्य सुरक्षा कवच बन जाता है, जिससे नकारात्मक शक्तियां, भूत-प्रेत और शत्रु परास्त होते हैं।

२. गुरु ग्रह (बृहस्पति दोष) की शांति व वैवाहिक सुख:
कुंडली में गुरु ग्रह की अशुभता, विवाह में देरी, अथवा शिक्षा-संतान संबंधी समस्याओं से जूझ रहे जातकों के लिए गुरुवार को विष्णु चालीसा का पाठ रामबाण उपाय है। इससे गुरु दोष समाप्त होकर शीघ्र विवाह व सुखद दांपत्य की प्राप्ति होती है।

३. महापापों का समूल नाश एवं मोक्ष प्रदायिनी:
"पाप काट भव सिन्धु उतारण। कष्ट नाशकर भक्त उबारण॥ गणिका और अजामिल तारे। बहुत भक्त भव सिन्धु उतारे॥"
जैसे अजामिल और गणिका केवल भगवान के नाम-स्मरण मात्र से परम गति को प्राप्त हुए, वैसे ही इस चालीसा का पाठ जन्म-जन्मांतरों के संचित पापों का क्षय कर अंत समय में वैकुण्ठ धाम की प्राप्ति कराता है।

४. माता महालक्ष्मी की अखंड कृपा व दरिद्रता नाश:
भगवान विष्णु 'श्रीपति' और 'लक्ष्मीनारायण' हैं। जहाँ श्रीहरि का वास और उनकी स्तुति होती है, वहाँ माता महालक्ष्मी स्थाई रूप से निवास करती हैं। नियमित पाठ से दरिद्रता, ऋण और आर्थिक तंगी दूर होकर यश, मान-प्रतिष्ठा व ऐश्वर्य की वृद्धि होती है।

५. सुख-शांति, सुसंतति व मनोवांछित फल सिद्धि:
"सुत सम्पति दे सुख उपजाओ। निज चरनन का दास बनाओ॥ निगम सदा ये विनय सुनावै। पढ़ै सुनै सो जन सुख पावै॥"
चालीसा के श्रवण व पठन से घर में क्लेश व अशांति समाप्त होती है, सुयोग्य संतान और धन-धान्य की समृद्धि होती है तथा समस्त सांसारिक कष्टों से मुक्ति मिलती है।"""

english_lyrics = """॥ Shri Vishnu Chalisa ॥

॥ Doha ॥
Vishnu Suniye Vinaya, Sevaka Kee Chitalaaya।
Keerata Kuchha Varnana Karoon, Deejai Gyaana Bataaya॥

॥ Chaupai ॥
Namo Vishnu Bhagavaana Kharaaree। Kashta Nashaavana Akhila Bihaaree॥1॥
Prabala Jagata Men Shakti Tumhaaree। Tribhuvana Phaila Rahee Ujiyaaree॥2॥
Sundara Roopa Manohara Soorata। Sarala Svabhaava Mohanee Moorata॥3॥
Tana Para Peetaambara Ati Sohata। Baijantee Maalaa Mana Mohata॥4॥
Shankha Chakra Kara Gadaa Biraaje। Dekhata Daitya Asura Dala Bhaaje॥5॥
Satya Dharma Mada Lobha Na Gaaje। Kaama Krodha Mada Lobha Na Chaaje॥6॥
Santa-Bhakta Sajjana Mana-Ranjana। Danuja Asura Dushtana Dala Ganjana॥7॥
Sukha Upajaaya Kashta Saba Bhanjana। Dosha Mitaaya Karata Jana Sajjana॥8॥
Paapa Kaata Bhava Sindhu Utaarana। Kashta Naashakara Bhakta Ubaarana॥9॥
Karata Aneka Roopa Prabhu Dhaarana। Kevala Aapa Bhakti Ke Kaarana॥10॥
Dharani Dhenu Bana Tumahin Pukaaraa। Taba Tuma Roopa Raama Kaa Dhaaraa॥11॥
Bhaara Utaara Asura Dala Maaraa। Raavana Aadika Ko Sanhaaraa॥12॥
Aapa Vaaraaha Roopa Banaayaa। Hiranyaaksha Ko Maara Giraayaa॥13॥
Dhara Matsya Tana Sindhu Banaayaa। Chaudaha Ratanana Ko Nikalaayaa॥14॥
Amilakha Asurana Dvanda Machaayaa। Roopa Mohanee Aapa Dikhayaa॥15॥
Devana Ko Amrita Paana Karaayaa। Asurana Ko Chhabi Se Bahalaayaa॥16॥
Koorma Roopa Dhara Sindhu Majhaayaa। Mandaachala Giri Turata Uthaayaa॥17॥
Shankara Kaa Tuma Phanda Chhudaayaa। Bhasmaasura Ko Roopa Dikhaayaa॥18॥
Vedana Ko Jaba Asura Dubaayaa। Kara Prabandha Unhen Dhundhavaayaa॥19॥
Mohita Banakara Khalahi Nachaayaa। Usihee Kara Se Bhasma Karaayaa॥20॥
Asura Jalandhara Ati Baladaa-ee। Shankara Se Una Keenha Ladaa-ee॥21॥
Haara Paara Shiva Sakala Banaa-ee। Keena Satee Se Chhala Khala Jaa-ee॥22॥
Sumirana Keena Tumhen Shivaranee। Batalaa-ee Saba Vipata Kahaanee॥23॥
Taba Tuma Bane Muneeshwara Gyaanee। Vrindaa Kee Saba Surati Bhulaanee॥24॥
Dekhata Teena Danuja Shaitaanee। Vrindaa Aaya Tumhen Lapataanee॥25॥
Ho Sparsha Dharma Kshati Maanee। Hanaa Asura Ura Shiva Shaitaanee॥26॥
Tumane Dhuroo Prahlaada Ubaare। Hiranaakusha Aadika Khala Maare॥27॥
Ganikaa Aura Ajaamila Taare। Bahuta Bhakta Bhava Sindhu Utaare॥28॥
Harahu Sakala Santaapa Hamaare। Kripaa Karahu Hari Sirajana Haare॥29॥
Dekhahun Main Nija Darasha Tumhaare। Deena Bandhu Bhaktana Hitakaare॥30॥
Chahata Aapakaa Sevaka Darshana। Karahu Dayaa Apanee Madhusoodana॥31॥
Jaanoon Naheen Yogya Japa Poojana। Hoya Yagya Stuti Anumodana॥32॥
Sheeladayaa Santosha Sulakshana। Vidita Naheen Vratabodha Vilakshana॥33॥
Karahun Aapakaa Kisa Vidhi Poojana। Kumati Viloka Hota Dukha Bheeshana॥34॥
Karahun Pranaama Kauna Vidhisumirana। Kauna Bhaanti Main Karahun Samarpana॥35॥
Sura Muni Karata Sadaa Sivakaa-ee। Harshita Rahata Parama Gati Paa-ee॥36॥
Deena Dukhina Para Sadaa Sahaa-ee। Nija Jana Jaana Leva Apanaa-ee॥37॥
Paapa Dosha Santaapa Nashaao। Bhava Bandhana Se Mukta Karaao॥38॥
Suta Sampati De Sukha Upajaao। Nija Charanana Kaa Daasa Banaao॥39॥
Nigama Sadaa Ye Vinaya Sunaavai। Padhai Sunai So Jana Sukha Paavai॥40॥

॥ Doha ॥
Chhavi Viloki Shreepati Sukha Paavai। Prema Sahita Chaaleesaa Gaavai॥
Vishnu Kripaa Saba Sankata Taare। Bhavasaagara Se Paara Utaare॥"""

# 1. Update drik_chalisa_11 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["vishnu"]["items"]:
    if item["id"] == "drik_chalisa_11":
        item["title"] = "विष्णु चालीसा"
        item["title_en"] = "Shri Vishnu Chalisa"
        item["en_line"] = "Namo Vishnu Bhagawana Kharari"
        item["hi_line"] = "नमो विष्णु भगवान खरारी"
        item["sub"] = "नमो विष्णु भगवान खरारी • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_vishnu_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=ty_BRH3b9lY"
        item["video_id"] = "ty_BRH3b9lY"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/lord-vishnu/shri-vishnu-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "जगतपालक चतुर्भुज भगवान श्री हरि विष्णु"
        item["section"] = "श्री विष्णु, ब्रह्मा व नृसिंह चालीसा"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_11 in drik_chalisa_collections.json successfully!")

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

# 3. Update chalisa_vishnu in CONTENT in app.js
content_obj = {
    "title": "श्री विष्णु चालीसा",
    "title_en": "Shri Vishnu Chalisa",
    "en_line": "Namo Vishnu Bhagawana Kharari",
    "hi_line": "नमो विष्णु भगवान खरारी",
    "sub": "नमो विष्णु भगवान खरारी • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_vishnu_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=ty_BRH3b9lY",
    "video_id": "ty_BRH3b9lY",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/lord-vishnu/shri-vishnu-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "जगतपालक चतुर्भुज भगवान श्री हरि विष्णु",
    "section": "श्री विष्णु, ब्रह्मा व नृसिंह चालीसा",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

vishnu_content_js = "  chalisa_vishnu: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

pos_v = app_text.find("  chalisa_vishnu: {")
if pos_v != -1:
    pos_next = app_text.find("  chalisa_brahma: {", pos_v)
    if pos_next != -1:
        app_text = app_text[:pos_v] + vishnu_content_js + app_text[pos_next:]
        print("Replaced chalisa_vishnu in CONTENT!")
    else:
        print("ERROR: Could not find chalisa_brahma after chalisa_vishnu!")
else:
    print("ERROR: Could not find chalisa_vishnu in app.js!")

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
