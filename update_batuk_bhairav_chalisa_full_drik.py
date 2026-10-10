import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री बटुक भैरव चालीसा ॥

॥ दोहा ॥
विश्वनाथ को सुमिर मन, धर गणेश का ध्यान।
भैरव चालीसा रचूं, कृपा करहु भगवान॥
बटुकनाथ भैरव भजू, श्री काली के लाल।
छीतरमल पर कर कृपा, काशी के कुतवाल॥

॥ चौपाई ॥
जय जय श्रीकाली के लाला। रहो दास पर सदा दयाला॥१॥
भैरव भीषण भीम कपाली। क्रोधवन्त लोचन में लाली॥२॥
कर त्रिशूल है कठिन कराला। गल में प्रभु मुण्डन की माला॥३॥
कृष्ण रूप तन वर्ण विशाला। पीकर मद रहता मतवाला॥४॥
रुद्र बटुक भक्तन के संगी। प्रेत नाथ भूतेश भुजंगी॥५॥
त्रैलतेश है नाम तुम्हारा। चक्र तुण्ड अमरेश पियारा॥६॥
शेखरचंद्र कपाल बिराजे। स्वान सवारी पै प्रभु गाजे॥७॥
शिव नकुलेश चण्ड हो स्वामी। बैजनाथ प्रभु नमो नमामी॥८॥
अश्वनाथ क्रोधेश बखाने। भैरों काल जगत ने जाने॥९॥
गायत्री कहैं निमिष दिगम्बर। जगन्नाथ उन्नत आडम्बर॥१०॥
क्षेत्रपाल दसपाण कहाये। मंजुल उमानन्द कहलाये॥११॥
चक्रनाथ भक्तन हितकारी। कहैं त्र्यम्बक सब नर नारी॥१२॥
संहारक सुनन्द तव नामा। करहु भक्त के पूरण कामा॥१३॥
नाथ पिशाचन के हो प्यारे। संकट मेटहु सकल हमारे॥१४॥
कृत्यायु सुन्दर आनन्दा। भक्त जनन के काटहु फन्दा॥१५॥
कारण लम्ब आप भय भंजन। नमोनाथ जय जनमन रंजन॥१६॥
हो तुम देव त्रिलोचन नाथा। भक्त चरण में नावत माथा॥१७॥
त्वं अशतांग रुद्र के लाला। महाकाल कालों के काला॥१८॥
ताप विमोचन अरि दल नासा। भाल चन्द्रमा करहि प्रकाशा॥१९॥
श्वेत काल अरु लाल शरीरा। मस्तक मुकुट शीश पर चीरा॥२०॥
काली के लाला बलधारी। कहाँ तक शोभा कहूँ तुम्हारी॥२१॥
शंकर के अवतार कृपाला। रहो चकाचक पी मद प्याला॥२२॥
शंकर के अवतार कृपाला। बटुक नाथ चेटक दिखलाओ॥२३॥
रवि के दिन जन भोग लगावें। धूप दीप नैवेद्य चढ़ावें॥२४॥
दरशन करके भक्त सिहावें। दारुड़ा की धार पिलावें॥२५॥
मठ में सुन्दर लटकत झावा। सिद्ध कार्य कर भैरों बाबा॥२६॥
नाथ आपका यश नहीं थोड़ा। करमें सुभग सुशोभित कोड़ा॥२७॥
कटि घूँघरा सुरीले बाजत। कंचनमय सिंहासन राजत॥२८॥
नर नारी सब तुमको ध्यावहिं। मनवांछित इच्छाफल पावहिं॥२९॥
भोपा हैं आपके पुजारी। करें आरती सेवा भारी॥३०॥
भैरव भात आपका गाऊँ। बार बार पद शीश नवाऊँ॥३१॥
आपहि वारे छीजन धाये। ऐलादी ने रूदन मचाये॥३२॥
बहन त्यागि भाई कहाँ जावे। तो बिन को मोहि भात पिन्हावे॥३३॥
रोये बटुक नाथ करुणा कर। गये हिवारे मैं तुम जाकर॥३४॥
दुखित भई ऐलादी बाला। तब हर का सिंहासन हाला॥३५॥
समय व्याह का जिस दिन आया। प्रभु ने तुमको तुरत पठाया॥३६॥
विष्णु कही मत विलम्ब लगाओ। तीन दिवस को भैरव जाओ॥३७॥
दल पठान संग लेकर धाया। ऐलादी को भात पिन्हाया॥३८॥
पूरन आस बहन की कीनी। सुर्ख चुन्दरी सिर धर दीनी॥३९॥
भात भेरा लौटे गुण ग्रामी। नमो नमामी अन्तर्यामी॥४०॥

॥ दोहा ॥
जय जय जय भैरव बटुक, स्वामी संकट टार।
कृपा दास पर कीजिए, शंकर के अवतार॥
जो यह चालीसा पढे, प्रेम सहित सत बार।
उस घर सर्वानन्द हों, वैभव बढ़ें अपार॥"""

meaning = """॥ श्री बटुक भैरव चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "विश्वनाथ को सुमिर मन, धर गणेश का ध्यान। भैरव चालीसा रचूं, कृपा करहु भगवान॥"
भावार्थ: मन में देवाधिदेव काशी विश्वनाथ का स्मरण कर तथा प्रथम पूज्य श्री गणेश जी का ध्यान धरकर, मैं श्री बटुक भैरव चालीसा की रचना कर रहा हूँ; हे दयालु भगवान भैरव! मुझ पर अपनी अहैतुकी कृपा कीजिए।
• "बटुकनाथ भैरव भजू, श्री काली के लाल। छीतरमल पर कर कृपा, काशी के कुतवाल॥"
भावार्थ: मैं माँ भगवती काली के प्रिय पुत्र, बालक रूप में पूजित श्री बटुकनाथ भैरव जी का भजन करता हूँ। हे काशी के कोतवाल भैरवनाथ! अपने अनन्य भक्त छीतरमल पर अपनी कृपा दृष्टि बनाए रखिए।

【४० चौपाइयां — पद्यवार भावार्थ】
१-४. "जय जय श्रीकाली के लाला... पीकर मद रहता मतवाला॥"
भावार्थ: हे माँ महाकाली के लाडले पुत्र! आपकी सदा-सदा जय हो; अपने इस दीन सेवक पर सदा दयालु रहिए। आपका भैरव रूप अत्यंत भीषण, विशाल और हाथ में कपाल धारण करने वाला है; आपके नेत्रों में दुष्टों के संहार के लिए लालिमा और क्रोध झलकता है। आपके कर-कमल में अत्यंत तीक्ष्ण और विकराल त्रिशूल सुशोभित है तथा गले में नरमुंडों की माला शोभित है। आपका श्याम वर्ण (काला स्वरूप) अत्यंत विशाल और प्रभावशाली है; आप दिव्य आनंद-रस (मद) का पान कर सदा मतवाले व परमानंद में मग्न रहते हैं।

५-८. "रुद्र बटुक भक्तन के संगी... बैजनाथ प्रभु नमो नमामी॥"
भावार्थ: आप भगवान रुद्र के बाल स्वरूप (बटुक) हैं और भक्तों के सदा संग रहने वाले सच्चे सखा हैं; आप समस्त प्रेतों, भूतों और सर्पों (भुजंग) के स्वामी हैं। आपका पावन नाम त्रैलतेश (तीनों लोकों के स्वामी) है; आप चक्रतुण्ड और देवताओं के अति प्रिय हैं। आपके शीश पर चंद्रमा और हाथ में कपाल सुशोभित है; आप अपनी पावन सवारी श्वान (कुत्ते) पर गरजते हुए सवार होते हैं। आप ही नकुलेश, चण्ड और बैजनाथ (वैद्यनाथ) स्वरूप शिव हैं; हे प्रभु! मैं आपको बारम्बार नमन करता हूँ।

९-१२. "अश्वनाथ क्रोधेश बखाने... कहैं त्र्यम्बक सब नर नारी॥"
भावार्थ: ज्ञानीजन आपको अश्वनाथ और क्रोधेश के नाम से पुकारते हैं; संपूर्ण संसार आपको साक्षात् काल (मृत्यु के भी काल) भैरव के रूप में जानता है। आप ही निमिष, दिगम्बर और गायत्री स्वरूप हैं; जगन्नाथ के रूप में आपका उन्नत और भव्य ऐश्वर्य प्रकट है। आप ही दस भुजाओं वाले क्षेत्रपाल हैं तथा माता उमा (पार्वती) को आनंदित करने वाले मंजुल उमानंद हैं। आप चक्रनाथ बनकर भक्तों का कल्याण करते हैं; समस्त नर-नारी आपको त्रिनेत्रधारी त्र्यम्बक स्वरूप कहते हैं।

१३-१६. "संहारक सुनन्द तव नामा... नमोनाथ जय जनमन रंजन॥"
भावार्थ: आपका नाम संहारक और सुनंद है; आप शरणागत भक्तों के सभी मनोरथ पूर्ण करते हैं। आप समस्त पिशाचों और यक्ष-राक्षसों के नायक हैं; हे प्रभु! आप हमारे जीवन के सभी ज्ञात-अज्ञात संकटों को हर लीजिए। आप कृत्यायु, सुंदर और परमानंद स्वरूप हैं; आप भक्तों के जन्म-मरण और अज्ञान के समस्त बंधनों (फंदों) को काट देते हैं। आप ही कारण, लम्ब और भयभंजन (भय का नाश करने वाले) हैं; हे भक्तों के मन को आनंदित करने वाले नाथ! आपकी सदा जय हो।

१७-२०. "हो तुम देव त्रिलोचन नाथा... मस्तक मुकुट शीश पर चीरा॥"
भावार्थ: हे त्रिलोचन (तीन नेत्रों वाले) देवाधिदेव! आपके चरणों में सभी भक्तजन श्रद्धापूर्वक मस्तक नवाते हैं। आप अष्टांग योग स्वरूप और भगवान रुद्र के प्रिय लाडले हैं; आप महाकाल और कालों के भी महाकाल हैं। आप तीनों तापों का शमन करने वाले और शत्रुओं के दल का संहार करने वाले हैं; आपके भाल पर बाल-चंद्रमा प्रकाशमान है। आपके तीन दिव्य स्वरूप हैं—सात्त्विक श्वेत, तामसिक काल (काला) और राजसिक लाल; आपके मस्तक पर रत्नजड़ित मुकुट और शीश पर दिव्य साफा (चीरा) शोभा पाता है।

२१-२४. "काली के लाला बलधारी... धूप दीप नैवेद्य चढ़ावें॥"
भावार्थ: हे माँ काली के परम बलशाली पुत्र! आपकी अलौकिक शोभा और पराक्रम का वर्णन करने में कोई समर्थ नहीं है। हे शंकर के कृपालु अवतार! आप दिव्य मद का प्याला पीकर सदा प्रसन्न और तृप्त रहते हैं। हे शंकर के अवतार कृपालु बटुकनाथ! भक्तों के संकट दूर करने के लिए अपने चमत्कारी पराक्रम दिखाइए। रविवार के पावन दिन भक्तजन आपके मंदिर में सुंदर भोग लगाते हैं और श्रद्धा से धूप, दीप व नैवेद्य अर्पित करते हैं।

२५-२८. "दरशन करके भक्त सिहावें... कंचनमय सिंहासन राजत॥"
भावार्थ: आपके मनोहारी दर्शन पाकर भक्तजन धन्य हो जाते हैं; वे आपके चरणों में दारुड़ा (द्रव्य/अर्घ्य) की धार अर्पित करते हैं। आपके पवित्र मठ व धाम में सुंदर चमरी/झावा लटकते हैं; हे भैरव बाबा! भक्तों के सभी रुके हुए कार्य सिद्ध कीजिए। हे नाथ! आपका यश संसार में अत्यंत महान है; आपके हाथ में दुष्टों को दंड देने वाला सुंदर कोड़ा (सोटा) सुशोभित है। आपकी कमर में सुरीले घुंघरू बजते हैं और आप स्वर्णजड़ित भव्य सिंहासन पर विराजमान हैं।

२९-३०. "नर नारी सब तुमको ध्यावहिं... करें आरती सेवा भारी॥"
भावार्थ: सभी नर और नारी आपका ध्यान करते हैं और मनवांछित फल प्राप्त करते हैं। आपके अनन्य पुजारी (भोपा) अत्यंत श्रद्धा से आपकी भव्य आरती और सेवा-पूजा संपन्न करते हैं।

३१-३६. "भैरव भात आपका गाऊँ... प्रभु ने तुमको तुरत पठाया॥"
भावार्थ: हे भैरवनाथ! मैं आपकी बहन ऐलादी के 'भात' (मायरा) भरने की पावन लीला का गान करता हूँ और आपके चरणों में बार-बार शीश नवाता हूँ। जब आप वैराग्य धारण कर घर त्यागने लगे, तब आपकी बहन ऐलादी बिलख-बिलख कर रोने लगी कि "हे भाई! मुझे छोड़कर कहाँ जा रहे हो? तुम्हारे बिना मेरे विवाह में भात कौन पहनाएगा?" बहन का क्रंदन सुनकर करुणानिधान बटुकनाथ भी रो पड़े और फिर गहन साधना में लीन हो गए। बहन ऐलादी जब अत्यंत दुखी हुई, तब उसके अश्रुओं से देवाधिदेव शिव का सिंहासन डोल उठा। जिस दिन बहन के विवाह का पावन समय आया, उस दिन महादेव ने तुरंत आपको भात भरने का आदेश देकर भेजा।

३७-४०. "विष्णु कही मत विलम्ब लगाओ... नमो नमामी अन्तर्यामी॥"
भावार्थ: भगवान श्री हरि विष्णु ने भी कहा कि हे भैरव! अब तनिक भी विलंब मत करो और तीन दिनों के भीतर जाकर अपनी बहन का मायरा भरो। तब बटुक भैरव अपने विशाल दल और पठान संगी-साथियों के साथ वेग से पहुंचे और बहन ऐलादी को सोने-चांदी से युक्त भव्य भात पहनाया। आपने बहन की समस्त आशाएं पूरी कीं और उसके शीश पर सौभाग्य की लाल चुनरी ओढ़ाई। संपूर्ण मर्यादा के साथ भात भरकर गुणनिधि भैरवनाथ लौटे; हे घट-घट के ज्ञाता अन्तर्यामी प्रभु! मैं आपको बारंबार नमन करता हूँ।

【समापन दोहे】
• "जय जय जय भैरव बटुक, स्वामी संकट टार। कृपा दास पर कीजिए, शंकर के अवतार॥"
भावार्थ: हे बटुक भैरव स्वामी! आपकी सदा जय-जयकार हो, आप अपने भक्तों के सभी संकटों को टालने वाले हैं। हे साक्षात् देवाधिदेव शंकर के अवतार! अपने इस सेवक पर अपनी दया और कृपा दृष्टि सदैव बनाए रखिए।
• "जो यह चालीसा पढे, प्रेम सहित सत बार। उस घर सर्वानन्द हों, वैभव बढ़ें अपार॥"
भावार्थ: जो भी श्रद्धालु भक्तजन इस बटुक भैरव चालीसा का प्रेम और निष्ठापूर्वक सौ (शत) बार पाठ करते हैं, उनके घर में समस्त आनंदों का वास होता है और उनका यश, वैभव व धन-धान्य अपार रूप से बढ़ता है।"""

vidhi = """॥ श्री बटुक भैरव चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन दिन:
- सर्वश्रेष्ठ दिन: प्रत्येक रविवार (रवि के दिन जन भोग लगावें), मंगलवार, तथा प्रत्येक मास के कृष्ण पक्ष की अष्टमी (कालाष्टमी)।
- वार्षिक महापर्व: श्री कालभैरव अष्टमी / भैरव जयंती (मार्गशीर्ष मास के कृष्ण पक्ष की अष्टमी तिथि)।
- समय: सायंकाल प्रदोष काल (सूर्यास्त के उपरांत) अथवा रात्रिकालीन निशीथ काल में पाठ करना सर्वाधिक फलदायी माना गया है।

२. दिशा, आसन व दीपक:
- दिशा: दक्षिण अथवा पूर्व दिशा की ओर मुख करके बैठें।
- आसन: काले, लाल अथवा ऊनी कंबल के आसन पर बैठना चाहिए।
- दीपक: मिट्टी या पीतल के दीपक में सरसों के तेल अथवा तिल के तेल का चौमुखी या एकमुखी दीपक प्रज्वलित करें।

३. पूजन सामग्री व प्रिय भोग:
- भगवान बटुक भैरव बाल स्वरूप हैं, अतः इनकी सौम्य सात्त्विक पूजा का विशेष विधान है।
- फूल व माला: लाल पुष्प (गुड़हल/गुलाब) या आक के फूल, और सुगंधित इत्र।
- सिंदूर व अक्षत: भैरव जी को सिंदूर, चमेली का तेल व भस्म अति प्रिय है।
- प्रिय नैवेद्य/भोग: उड़द की दाल के पकौड़े (बड़े), बेसन के लड्डू, इमरती, मीठा रोट (रोटड़ा), पान का बीड़ा, काले तिल, बताशे, अथवा नारियल।
- द्रव्य अर्घ्य: तामसिक व अघोर विधान में मदिरा/दारू की धार का उल्लेख है, किंतु गृहस्थ साधक शुद्ध जल में सुगंधित इत्र व कच्चा दूध मिलाकर अर्घ्य (धार) प्रदान करें।

४. श्वान (कुत्ते) की सेवा — भैरव कृपा की अनिवार्य कुंजी:
- भगवान बटुक भैरव का वाहन श्वान (कुत्ता) है।
- पाठ के दिन अथवा प्रत्येक रविवार को काले कुत्ते को सरसों के तेल से चुपड़ी मीठी रोटी, दूध या जलेबी अवश्य खिलाएं। इससे भैरव जी तत्काल प्रसन्न होते हैं।

५. प्रामाणिक पाठ क्रम:
- सर्वप्रथम पवित्रीकरण व आचमन करें।
- भगवान शिव, माता पार्वती व श्री गणेश जी का स्मरण करें।
- बटुक भैरव जी का ध्यान मंत्र बोलें:
  'ॐ ह्रीं बटुकाय आपदुद्धारणाय कुरु कुरु बटुकाय ह्रीं ॐ स्वाहा।'
  अथवा सरल नाम मंत्र 'ॐ बटुक भैरवाय नमः' का ११ या २१ बार जप करें।
- इसके उपरांत श्रद्धापूर्वक श्री बटुक भैरव चालीसा का १, ३, ७, ११ अथवा २१ बार पाठ करें (विशेष कार्य सिद्धि हेतु १०० बार का अनुष्ठान करें)।
- पाठ के उपरांत भैरव जी की आरती करें और सभी में प्रसाद वितरित करें।"""

significance = """॥ श्री बटुक भैरव चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. बाल स्वरूप की सौम्यता — गृहस्थों के लिए परम कल्याणकारी:
भगवान भैरव के उग्र स्वरूपों (कालभैरव, असितांग, भीषण) की साधना जहां कठोर नियमों वाली होती है, वहीं 'बटुक भैरव' उनका बाल रूप है। माता काली के लाडले और देवाधिदेव शिव के बाल स्वरूप होने के कारण बटुक भैरव जी अत्यंत शीघ्र प्रसन्न होते हैं और गृहस्थ साधकों पर वात्सल्यमयी कृपा बरसाते हैं।

२. भय, प्रेत बाधा व नकारात्मक शक्तियों का समूल नाश:
"कारण लम्ब आप भय भंजन। नमोनाथ जय जनमन रंजन॥"
चालीसा के नित्य पाठ से भूत, प्रेत, पिशाच, डाकनी-शाकनी, नजर दोष, तंत्र-मंत्र और अकाल मृत्यु का भय तत्काल नष्ट हो जाता है। साधक के चारों ओर अभेद्य सुरक्षा चक्र (भैरव कवच) स्थापित हो जाता है।

३. शत्रु पराजय, मुकदमे व कोर्ट-कचहरी में विजय:
"ताप विमोचन अरि दल नासा। भाल चन्द्रमा करहि प्रकाशा॥"
यदि कोई शत्रु अकारण पीड़ा पहुंचा रहा हो या न्यायालय में झूठे विवाद चल रहे हों, तो रविवार अथवा कालाष्टमी को बटुक भैरव चालीसा का पाठ करने से विरोधी परास्त होते हैं और साधक को विजय प्राप्त होती है।

४. राहु-केतु, शनि साढ़ेसाती व ग्रह दोष शांति:
ज्योतिष शास्त्र में भैरव जी को काल और दण्ड के नियंत्रक माना गया है। इनकी आराधना से कुंडली में राहु-केतु की क्रूर दशा, कालसर्प दोष और शनि की साढ़ेसाती या ढैय्या के अनिष्ट प्रभाव शांत हो जाते हैं।

५. बहन ऐलादी की भात लीला — कुल, परिवार व बहन-भाई की रक्षा:
चालीसा में वर्णित ऐतिहासिक लीला के अनुसार भगवान बटुक भैरव ने अपनी बहन ऐलादी के विवाह में भात भरकर उसकी मान-मर्यादा की रक्षा की थी। इस चालीसा का पाठ करने से परिवार में अटूट प्रेम बना रहता है, कन्याओं के विवाह में आ रही रुकावटें दूर होती हैं और घर में धन-धान्य व वैभव की कभी कमी नहीं होती।

६. काशी विश्वनाथ यात्रा की पूर्णता:
मान्यता है कि काशी के कोतवाल भैरवनाथ के दर्शन और स्तुति के बिना बाबा विश्वनाथ के दर्शन का फल पूर्ण नहीं होता। इनके चालीसा पाठ से साक्षात् काशी वास और अंत में शिवलोक का परम पद प्राप्त होता है।"""

english_lyrics = """॥ Shri Batuka Bhairava Chalisa ॥

॥ Doha ॥
Vishwanaatha Ko Sumira Mana, Dhara Ganesha Kaa Dhyaana।
Bhairava Chaaleesaa Rachoon, Kripaa Karahu Bhagavaana॥
Batukanaatha Bhairava Bhajoo, Shree Kaalee Ke Laala।
Chheetaramala Para Kara Kripaa, Kaashee Ke Kootavaala॥

॥ Chaupai ॥
Jaya Jaya Shree Kaalee Ke Laalaa। Raho Daasa Para Sadaa Dayaalaa॥1॥
Bhairava Bheeshana Bheema Kapaalee। Krodhavanta Lochana Men Laalee॥2॥
Kara Trishoola Hai Kathina Karaalaa। Gala Men Prabhu Mundana Kee Maalaa॥3॥
Krishna Roopa Tana Varna Vishaalaa। Peekara Mada Rahataa Matavaalaa॥4॥
Rudra Batuka Bhaktana Ke Sangee। Preta Naatha Bhootesha Bhujangee॥5॥
Trailatesha Hai Naama Tumhaaraa। Chakra Tunda Amaresha Piyaaraa॥6॥
Shekharachandra Kapaala Biraaje। Svaana Savaaree Pai Prabhu Gaaje॥7॥
Shiva Nakulesha Chanda Ho Svaamee। Baijanaatha Prabhu Namo Namaamee॥8॥
Ashwanaatha Krodhesha Bakhaane। Bhairon Kaala Jagata Ne Jaane॥9॥
Gaayatree Kahain Nimisha Digambara। Jagannaatha Unnata Aadambara॥10॥
Kshetrapaala Dasapaana Kahaaye। Manjula Umaananda Kahalaaye॥11॥
Chakranaatha Bhaktana Hitakaaree। Kahain Tryambaka Saba Nara Naaree॥12॥
Sanhaaraka Sunanda Tava Naamaa। Karahu Bhakta Ke Poorana Kaamaa॥13॥
Naatha Pishaachana Ke Ho Pyaare। Sankata Metahu Sakala Hamaare॥14॥
Krityaayu Sundara Aanandaa। Bhakta Janana Ke Kaatahu Fandaa॥15॥
Kaarana Lamba Aapa Bhaya Bhanjana। Namonaatha Jaya Janamana Ranjana॥16॥
Ho Tuma Deva Trilochana Naathaa। Bhakta Charana Men Naavata Maathaa॥17॥
Tvam Ashataanga Rudra Ke Laalaa। Mahaakaala Kaalon Ke Kaalaa॥18॥
Taapa Vimochana Ari Dala Naasaa। Bhaala Chandramaa Karahi Prakaashaa॥19॥
Shweta Kaala Aru Laala Shareeraa। Mastaka Mukuta Sheesha Para Cheeraa॥20॥
Kaalee Ke Laalaa Baladhaaree। Kahaan Taka Shobhaa Kahoon Tumhaaree॥21॥
Shankara Ke Avataara Kripaalaa। Raho Chakaachaka Pee Mada Pyaalaa॥22॥
Shankara Ke Avataara Kripaalaa। Batuka Naatha Chetaka Dikhalaao॥23॥
Ravi Ke Dina Jana Bhoga Lagaaven। Dhoopa Deepa Naivedya Chadhaaven॥24॥
Darashana Karake Bhakta Sihaaven। Daarudaa Kee Dhaara Pilaaven॥25॥
Matha Men Sundara Latakata Jhaavaa। Siddha Kaarya Kara Bhairon Baabaa॥26॥
Naatha Aapakaa Yasha Nahin Thodaa। Karamen Subhaga Sushobhita Kodaa॥27॥
Kati Ghoongharaa Sureele Baajata। Kanchanamaya Singhaasana Raajata॥28॥
Nara Naaree Saba Tumako Dhyaavahin। Manavaanchhita Ichchhaaphala Paavahin॥29॥
Bhopaa Hain Aapake Poojaaree। Karain Aaratee Sevaa Bhaaree॥30॥
Bhairava Bhaata Aapakaa Gaaoon। Baara Baara Pada Sheesha Navaaoon॥31॥
Aapahi Vaare Chheejana Dhaaye। Ailaadee Ne Roodana Machaaye॥32॥
Bahana Tyaagi Bhaa-ee Kahaan Jaave। To Bina Ko Mohi Bhaata Pinhaave॥33॥
Roye Batuka Naatha Karunaa Kara। Gaye Hivaare Main Tuma Jaakara॥34॥
Dukhita Bha-ee Ailaadee Baalaa। Taba Hara Kaa Singhaasana Haalaa॥35॥
Samaya Vyaaha Kaa Jisa Dina Aayaa। Prabhu Ne Tumako Turata Pathaayaa॥36॥
Vishnu Kahee Mata Vilamba Lagaao। Teena Divasa Ko Bhairava Jaao॥37॥
Dala Pathaana Sanga Lekara Dhaayaa। Ailaadee Ko Bhaata Pinhaayaa॥38॥
Poorana Aasa Bahana Kee Keenee। Surkha Chundaree Sira Dhara Deenee॥39॥
Bhaata Bheraa Laute Guna Graamee। Namo Namaamee Antaryaamee॥40॥

॥ Doha ॥
Jaya Jaya Jaya Bhairava Batuka, Svaamee Sankata Taara।
Kripaa Daasa Para Keejiye, Shankara Ke Avataara॥
Jo Yaha Chaaleesaa Padhe, Prema Sahita Sata Baara।
Usa Ghara Sarvaananda Hon, Vaibhava Badhain Apaara॥"""

# 1. Update drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["bhairav"]["items"]:
    if item["id"] == "drik_chalisa_13":
        item["title"] = "भगवान बटुक भैरव चालीसा"
        item["title_en"] = "Lord Batuka Bhairava Chalisa"
        item["en_line"] = "Jai Jai Shree Kali Ke Lala"
        item["hi_line"] = "जय जय श्रीकाली के लाला"
        item["sub"] = "जय जय श्रीकाली के लाला • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_bhairav_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=d4fIcvnKM4s"
        item["video_id"] = "d4fIcvnKM4s"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/batuka-bhairava/shri-batuka-bhairava-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "रुद्रावतार श्री कालभैरव व बटुक भैरव"
        item["section"] = "श्री कालभैरव व बटुक भैरव चालीसा"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_13 in drik_chalisa_collections.json successfully!")

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

# 3. Update chalisa_bhairav in CONTENT in app.js
content_obj = {
    "title": "भगवान बटुक भैरव चालीसा",
    "title_en": "Lord Batuka Bhairava Chalisa",
    "en_line": "Jai Jai Shree Kali Ke Lala",
    "hi_line": "जय जय श्रीकाली के लाला",
    "sub": "जय जय श्रीकाली के लाला • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_bhairav_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=d4fIcvnKM4s",
    "video_id": "d4fIcvnKM4s",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/batuka-bhairava/shri-batuka-bhairava-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "रुद्रावतार श्री कालभैरव व बटुक भैरव",
    "section": "श्री कालभैरव व बटुक भैरव चालीसा",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

bhairav_content_js = "  chalisa_bhairav: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

m_start = app_text.find("  chalisa_bhairav: {")
if m_start != -1:
    # find next chalisa_
    m_end = app_text.find("\n  chalisa_", m_start + 1)
    if m_end != -1:
        app_text = app_text[:m_start] + bhairav_content_js + app_text[m_end+1:]
        print("Replaced existing chalisa_bhairav in CONTENT!")
else:
    print("WARNING: chalisa_bhairav: { not found in app.js")

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
