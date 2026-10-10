import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री ललिता चालीसा ॥

॥ चौपाई ॥
जयति जयति जय ललिते माता। तव गुण महिमा है विख्याता॥१॥
तू सुन्दरी, त्रिपुरेश्वरी देवी। सुर नर मुनि तेरे पद सेवी॥२॥
तू कल्याणी कष्ट निवारिणी। तू सुख दायिनी, विपदा हारिणी॥३॥
मोह विनाशिनी दैत्य नाशिनी। भक्त भाविनी ज्योति प्रकाशिनी॥४॥
आदि शक्ति श्री विद्या रूपा। चक्र स्वामिनी देह अनूपा॥५॥
हृदय निवासिनी-भक्त तारिणी। नाना कष्ट विपति दल हारिणी॥६॥
दश विद्या है रुप तुम्हारा। श्री चन्द्रेश्वरी नैमिष प्यारा॥७॥
धूमा, बगला, भैरवी, तारा। भुवनेश्वरी, कमला, विस्तारा॥८॥
षोडशी, छिन्न्मस्ता, मातंगी। ललितेशक्ति तुम्हारी संगी॥९॥
ललिते तुम हो ज्योतित भाला। भक्त जनों का काम संभाला॥१०॥
भारी संकट जब-जब आये। उनसे तुमने भक्त बचाए॥११॥
जिसने कृपा तुम्हारी पायी। उसकी सब विधि से बन आयी॥१२॥
संकट दूर करो माँ भारी। भक्त जनों को आस तुम्हारी॥१३॥
त्रिपुरेश्वरी, शैलजा, भवानी। जय जय जय शिव की महारानी॥१४॥
योग सिद्दि पावें सब योगी। भोगें भोग महा सुख भोगी॥१५॥
कृपा तुम्हारी पाके माता। जीवन सुखमय है बन जाता॥१६॥
दुखियों को तुमने अपनाया। महा मूढ़ जो शरण न आया॥१७॥
तुमने जिसकी ओर निहारा। मिली उसे सम्पत्ति, सुख सारा॥१८॥
आदि शक्ति जय त्रिपुर प्यारी। महाशक्ति जय जय, भय हारी॥१९॥
कुल योगिनी, कुण्डलिनी रूपा। लीला ललिते करें अनूपा॥२०॥
महा-महेश्वरी, महा शक्ति दे। त्रिपुर-सुन्दरी सदा भक्ति दे॥२१॥
महा महा-नन्दे कल्याणी। मूकों को देती हो वाणी॥२२॥
इच्छा-ज्ञान-क्रिया का भागी। होता तब सेवा अनुरागी॥२३॥
जो ललिते तेरा गुण गावे। उसे न कोई कष्ट सतावे॥२४॥
सर्व मंगले ज्वाला-मालिनी। तुम हो सर्व शक्ति संचालिनी॥२५॥
आया माँ जो शरण तुम्हारी। विपदा हरी उसी की सारी॥२६॥
नामा कर्षिणी, चिन्ता कर्षिणी। सर्व मोहिनी सब सुख-वर्षिणी॥२७॥
महिमा तव सब जग विख्याता। तुम हो दयामयी जग माता॥२८॥
सब सौभाग्य दायिनी ललिता। तुम हो सुखदा करुणा कलिता॥२९॥
आनन्द, सुख, सम्पत्ति देती हो। कष्ट भयानक हर लेती हो॥३०॥
मन से जो जन तुमको ध्यावे। वह तुरन्त मन वांछित पावे॥३१॥
लक्ष्मी, दुर्गा तुम हो काली। तुम्हीं शारदा चक्र-कपाली॥३२॥
मूलाधार, निवासिनी जय जय। सहस्रार गामिनी माँ जय जय॥३३॥
छः चक्रों को भेदने वाली। करती हो सबकी रखवाली॥३४॥
योगी, भोगी, क्रोधी, कामी। सब हैं सेवक सब अनुगामी॥३५॥
सबको पार लगाती हो माँ। सब पर दया दिखाती हो माँ॥३६॥
हेमावती, उमा, ब्रह्माणी। भण्डासुर कि हृदय विदारिणी॥३७॥
सर्व विपति हर, सर्वाधारे। तुमने कुटिल कुपंथी तारे॥३८॥
चन्द्र- धारिणी, नैमिश्वासिनी। कृपा करो ललिते अधनाशिनी॥३९॥
भक्त जनों को दरस दिखाओ। संशय भय सब शीघ्र मिटाओ॥४०॥
जो कोई पढ़े ललिता चालीसा। होवे सुख आनन्द अधीसा॥४१॥
जिस पर कोई संकट आवे। पाठ करे संकट मिट जावे॥४२॥
ध्यान लगा पढ़े इक्कीस बारा। पूर्ण मनोरथ होवे सारा॥४३॥
पुत्र-हीन संतति सुख पावे। निर्धन धनी बने गुण गावे॥४४॥
इस विधि पाठ करे जो कोई। दुःख बन्धन छूटे सुख होई॥४५॥
जितेन्द्र चन्द्र भारतीय बतावें। पढ़ें चालीसा तो सुख पावें॥४६॥
सबसे लघु उपाय यह जानो। सिद्ध होय मन में जो ठानो॥४७॥
ललिता करे हृदय में बासा। सिद्दि देत ललिता चालीसा॥४८॥

॥ दोहा ॥
ललिते माँ अब कृपा करो, सिद्ध करो सब काम।
श्रद्धा से सिर नाय करे, करते तुम्हें प्रणाम॥"""

meaning = """॥ श्री ललिता चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【४८ चौपाइयां — पद्यवार भावार्थ】
१-६. "जयति जयति जय ललिते माता... नाना कष्ट विपति दल हारिणी॥"
भावार्थ: हे माता ललिता जी! आपकी सदा-सदा जय हो, जय हो, जय हो! आपके दिव्य गुणों और अलौकिक महिमा का यश संपूर्ण त्रिलोकी में विख्यात है। आप परम सुंदरी, तीनों पुरों (स्वर्ग, मर्त्य, पाताल) की अधीश्वरी त्रिपुरसुन्दरी देवी हैं; देवता, मनुष्य और मुनिजन निरंतर आपके पावन चरणों की सेवा करते हैं। आप सबका कल्याण करने वाली और भक्तों के समस्त कष्टों का निवारण करने वाली हैं; आप सर्वसुखदायिनी और घोर विपत्तियों को हरने वाली हैं। आप सांसारिक अज्ञान व मोह का विनाश करने वाली, दैत्यों का संहार करने वाली, भक्तों का भावपूर्वक ध्यान रखने वाली और अंतःकरण में दिव्य ज्ञान की ज्योति प्रकाशित करने वाली हैं। आप साक्षात् परात्पर आदिशक्ति और श्रीविद्या (षोडशी) का साक्षात् विग्रह हैं; आप श्रीचक्र (श्री यंत्र) की स्वामिनी हैं और आपका स्वरूप अनुपम व अनिर्वचनीय है। आप भक्तों के हृदय-कमल में निवास करती हैं और उनका भव-बंधन से उद्धार करती हैं; आप उनके अनेक कष्टों और विपत्तियों के दलों का समूल नाश करती हैं।

७-१३. "दश विद्या है रुप तुम्हारा... भक्त जनों को आस तुम्हारी॥"
भावार्थ: दश महाविद्याएं (काली, तारा, षोडशी, भुवनेश्वरी, भैरवी, छिन्नमस्ता, धूमावती, बगलामुखी, मातंगी और कमला) आपका ही पावन स्वरूप हैं। नैमिषारण्य तीर्थ में आपका वास 'श्री चन्द्रेश्वरी' (ललिता देवी) के रूप में अत्यंत प्रिय है। धूमावती, बगलामुखी, त्रिपुरभैरवी, तारा, भुवनेश्वरी और कमला के रूप में आपका ही विस्तार है। षोडशी, छिन्नमस्ता और मातंगी—ये सभी दिव्य शक्तियां हे ललिते! आपकी ही सहचरी और संगिनी हैं। हे ललिता माँ! आपका भाल (मस्तक) दिव्य तेज और ज्योति से उद्भासित है; आपने सदा अपने शरणागत भक्तों के कठिन कार्यों को संभाला है। जब-जब भक्तों पर भारी संकट या आपदाएं आईं, तब-तब आपने स्वयं प्रकट होकर उनकी रक्षा की है। जिस पर भी आपकी दया-दृष्टि हुई, उसके बिगड़े हुए सारे काम सब प्रकार से बन गए। हे माता! हम भक्तों के भीषण संकटों को दूर कीजिए, हम सभी को केवल और केवल आपका ही सहारा है।

१४-२०. "त्रिपुरेश्वरी, शैलजा, भवानी... लीला ललिते करें अनूपा॥"
भावार्थ: आप त्रिपुरेश्वरी, गिरिराज हिमालय की कन्या शैलजा और समस्त जगत को उत्पन्न करने वाली भवानी हैं; देवाधिदेव महादेव शिव की पटरानी महारानी की सदा जय हो। आपकी कृपा से योगीजन अष्ट महासिद्धियों को प्राप्त करते हैं, और संसारी लोग समस्त उत्तम सुखों व ऐश्वर्यों को भोगते हैं। हे माता! आपकी अहैतुकी कृपा पाकर मनुष्य का संपूर्ण जीवन सुखमय और आनंदमय बन जाता है। जो अज्ञानी व मूढ़ आपकी शरण में नहीं आते वे भटकते हैं, परंतु जब भी कोई दीन-दुखी आपकी शरण में आता है तो आप उसे वात्सल्य से अपना लेती हैं। आपने जिस भी साधक पर अपनी कृपादृष्टि डाली, उसे संसार की समस्त संपत्ति, वैभव और सुख सुलभ हो गया। हे आदि-महाशक्ति! हे त्रिपुर प्यारी! आपकी जय हो; आप भक्तों के समस्त भयों का हरण करने वाली हैं। आप साधकों की सुषुम्ना नाड़ी में जाग्रत होने वाली कुल-योगिनी और कुण्डलिनी महाशक्ति का रूप हैं; हे माँ ललिते! आपकी लीलाएं सर्वथा अलौकिक हैं।

२१-२८. "महा-महेश्वरी, महा शक्ति दे... तुम हो दयामयी जग माता॥"
भावार्थ: हे महा-माहेश्वरी! मुझे महान आत्मशक्ति प्रदान कीजिए; हे त्रिपुर-सुन्दरी! मुझे अपनी अनन्य व निष्काम भक्ति का वरदान दीजिए। आप परम आनंदमयी और कल्याणकारिणी हैं; आप मूक (गूंगा) व्यक्ति को भी वाक-सिद्धि (दिव्य वाणी) प्रदान कर देती हैं। साधक आपकी कृपा से ही इच्छा शक्ति, ज्ञान शक्ति और क्रिया शक्ति का अधिपति बनता है और आपकी पावन सेवा का अनुरागी होता है। जो मनुष्य हे ललिते! आपकी महिमा और गुणों का गान करता है, उसे संसार का कोई भी कष्ट कभी सता नहीं सकता। आप सर्वमंगला और ज्वालामालिनी हैं; आप संपूर्ण ब्रह्मांड की समस्त शक्तियों का संचालन करने वाली मुख्य अधिष्ठात्री हैं। जो भी दीन भाव से आपकी शरण में आ गया, आपने उसकी समस्त विपत्तियों को हर लिया। आप 'नामाकर्षिणी' (नाम से आकर्षित करने वाली), 'चिन्ताकर्षिणी' (चिंताओं को खींचकर नष्ट करने वाली), सर्वमोहिनी और भक्तों पर समस्त सुखों की अमृत वर्षा करने वाली हैं। आपकी अगाध महिमा संपूर्ण जगत में विख्यात है; आप परम दयालु जगतजननी माँ हैं।

२९-३६. "सब सौभाग्य दायिनी ललिता... सब पर दया दिखाती हो माँ॥"
भावार्थ: हे माँ ललिता! आप स्त्रियों व पुरुषों को समस्त सौभाग्य, सुहाग व ऐश्वर्य प्रदान करने वाली हैं; आप सुखदायिनी और करुणा से परिपूर्ण हैं। आप भक्तों को आंतरिक आनंद, भौतिक सुख और अक्षय संपत्ति प्रदान करती हैं और उनके भयानक संकटों को हर लेती हैं। जो मनुष्य एकाग्र मन से आपका ध्यान करता है, वह तत्काल अपने मनवांछित फलों को प्राप्त करता है। आप ही महालक्ष्मी, महादुर्गा और महाकाली हैं; आप ही शारदा और चक्रधारिणी चंडिका हैं। मूलाधार चक्र में वास करने वाली हे माँ, आपकी जय हो! सहस्रार चक्र तक गमन करने वाली हे पराशक्ति, आपकी जय हो! आप साधक के मूलाधार से लेकर आज्ञा चक्र तक समस्त षट्चक्रों का भेदन करने वाली और सबकी रक्षा करने वाली हैं। चाहे कोई योगी हो, भोगी हो, कामी हो या क्रोधी—अंततः सभी आपकी ही माया के अधीन, आपके सेवक और अनुगामी हैं। आप सभी जीवों को भवसागर से पार लगाती हैं और सभी पर अपनी मातृवत् करुणा बरसाती हैं।

३७-४०. "हेमावती, उमा, ब्रह्माणी... संशय भय सब शीघ्र मिटाओ॥"
भावार्थ: आप ही हेमावती (स्वर्णवर्णी), उमा और ब्रह्माणी हैं; आपने ही देवताओं की रक्षा हेतु महाअसुर भण्डासुर की छाती विदीर्ण कर उसका संहार किया था। आप समस्त विपत्तियों का हरण करने वाली और संपूर्ण सृष्टि का एकमात्र आधार हैं; आपने कुटिल और कुमार्ग पर चलने वाले पापियों का भी उद्धार किया है। मस्तक पर अर्धचन्द्र धारण करने वाली और नैमिषारण्य में वास करने वाली हे ललिते! हमारे समस्त पापों का नाश कर हम पर अपनी कृपा कीजिए। अपने अनन्य भक्तों को अपने दिव्य स्वरूप का दर्शन कराइए और हमारे समस्त संशयों व भयों को शीघ्रता से मिटा दीजिए।

४१-४८. "जो कोई पढ़े ललिता चालीसा... सिद्दि देत ललिता चालीसा॥"
भावार्थ: जो कोई भी श्रद्धालु इस पावन ललिता चालीसा का पाठ करता है, वह सुख, शांति और परमानंद का स्वामी बन जाता है। जिस किसी मनुष्य पर भी कोई भारी संकट या विपत्ति आए, वह इस चालीसा का पाठ करे तो उसका संकट तत्काल कट जाता है। जो साधक पूर्ण ध्यान लगाकर २१ बार इस चालीसा का पाठ करता है, उसके जीवन के समस्त मनोरथ निश्चित ही पूर्ण हो जाते हैं। संतानहीन व्यक्ति को सुयोग्य संतान का सुख मिलता है और निर्धन मनुष्य धनवान बनकर माता के गुणों का गान करता है। इस प्रकार जो कोई भी नियमपूर्वक पाठ करता है, उसके समस्त दुख-बंधन छूट जाते हैं और उसे परम सुख की प्राप्ति होती है। संत जितेन्द्र चन्द्र भारतीय बताते हैं कि जो इस चालीसा को पढ़ता है, वह अलौकिक सुख पाता है। अपने मनोरथों को सिद्ध करने का यह सबसे सरल और सुगम उपाय है कि जो भी मन में ठान लिया जाए, वह सिद्ध हो जाता है। जब माँ ललिता भक्त के हृदय में वास कर लेती हैं, तो यह ललिता चालीसा उसे समस्त आध्यात्मिक और भौतिक सिद्धियां प्रदान करती है।

【समापन दोहा】
• "ललिते माँ अब कृपा करो, सिद्ध करो सब काम। श्रद्धा से सिर नाय करे, करते तुम्हें प्रणाम॥"
भावार्थ: हे करुणामयी माँ ललिता! अब मुझ अकिंचन पर कृपा कीजिए और मेरे समस्त शुभ कार्यों को सिद्ध कीजिए। मैं परम श्रद्धा व विनयपूर्वक आपके श्रीचरणों में सिर झुकाकर आपको बारंबार साष्टांग प्रणाम करता हूँ।"""

vidhi = """॥ श्री ललिता चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल सूर्योदय वेला, ब्रह्ममुहूर्त, अथवा सांध्यकाल गोधूलि वेला।
- सर्वोत्तम वार: प्रत्येक शुक्रवार (भगवती ललिता का विशेष दिन), तथा अष्टमी व नवमी तिथि।
- महापर्व व पावन तिथियां: ललिता पंचमी (शारदीय नवरात्रि की पंचमी तिथि), माघ मास की पूर्णिमा (ललिता जयंती), चैत्र व शारदीय नवरात्रि, तथा प्रत्येक मास की पूर्णिमा।

२. दिशा, आसन व वस्त्र:
- दिशा: उत्तर अथवा पूर्व दिशा की ओर मुख करके बैठना सर्वोत्तम है (श्रीविद्या साधना में उत्तर-पूर्व ईशान कोण श्रेयस्कर है)।
- आसन: लाल रंग का रेशमी अथवा ऊनी आसन बिछाएं।
- वस्त्र: साधक को स्वच्छ लाल, गुलाबी अथवा पीले वस्त्र धारण करने चाहिए।

३. दीपक, तिलक व श्रीचक्र पूजन:
- दीपक: गाय के शुद्ध देशी घी का अथवा तिल के तेल का दीपक प्रज्वलित करें।
- पुष्प व तिलक: लाल पुष्प (लाल गुलाब, गुड़हल, लाल कमल) तथा रक्त चंदन अथवा कुंकुम/केसर का तिलक लगाएं।
- श्रीचक्र (श्री यंत्र): यदि सम्मुख श्रीयंत्र स्थापित हो तो पाठ का फल अनंत गुना हो जाता है।
- प्रिय नैवेद्य: पंचामृत, मखाने की खीर, बताशे, अनार, सेब, मिश्री, तथा मीठा पान।

४. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन व पवित्रीकरण करें।
- भगवती ललिता त्रिपुरसुन्दरी एवं कामेश्वर शिव का ध्यान करें।
- ललिता बीज मन्त्र: 'ॐ श्रीं ललितायै नमः' अथवा 'ॐ ऐं ह्रीं श्रीं त्रिपुरसुन्दर्यै नमः' का कम से कम १ माला (१०८ बार) जप करें।
- इसके पश्चात एकाग्रचित्त होकर 'श्री ललिता चालीसा' का १, ३, ७, ११ अथवा २१ बार पाठ करें।
- पाठ समाप्ति पर माता ललिता जी की पावन आरती गाएं और क्षमा-प्रार्थना करें।"""

significance = """॥ श्री ललिता चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. श्रीविद्या एवं षट्चक्र भेदन (कुण्डलिनी जागरण):
"मूलाधार, निवासिनी जय जय। सहस्रार गामिनी माँ जय जय॥ छः चक्रों को भेदने वाली। करती हो सबकी रखवाली॥"
माता ललिता साक्षात् श्रीविद्या और कुण्डलिनी स्वरूपा हैं। चालीसा का नित्य पाठ करने से मूलाधार से सहस्रार तक षट्चक्रों में सकारात्मक ऊर्जा का संचार होता है और आत्म-साक्षात्कार का मार्ग प्रशस्त होता है।

२. अखंड सौभाग्य, दांपत्य सुख व संतान प्राप्ति:
"पुत्र-हीन संतति सुख पावे। निर्धन धनी बने गुण गावे॥"
स्त्रियों को अखंड सौभाग्य, रूप, तेज और निःसंतान दंपत्तियों को गुणवान संतान की प्राप्ति होती है। दांपत्य जीवन में परस्पर प्रेम व सौहार्द बना रहता है।

३. भय, शत्रु व तंत्र-मंत्र बाधा से मुक्ति:
"हेमावती, उमा, ब्रह्माणी। भण्डासुर कि हृदय विदारिणी॥"
भण्डासुर का मर्दन करने वाली पराशक्ति ललिता के स्मरण से समस्त गुप्त व प्रकट शत्रु, तांत्रिक मारण-मोहन-उच्चाटन आदि विकार और भय तत्काल समाप्त हो जाते हैं।

४. अकूत धन-वैभव व दारिद्र्य नाश:
"तुमने जिसकी ओर निहारा। मिली उसे सम्पत्ति, सुख सारा॥"
राजराजेश्वरी त्रिपुरसुन्दरी की कृपा से दरिद्रता का समूल नाश होता है और घर में सुख, शांति, समृद्धि व लक्ष्मी का स्थायी वास होता है।

५. २१ पाठ से सर्व मनोरथ सिद्धि:
"ध्यान लगा पढ़े इक्कीस बारा। पूर्ण मनोरथ होवे सारा॥"
चालीसा में स्पष्ट उद्घोष है कि पूर्ण श्रद्धा से २१ बार पाठ करने वाले साधक का कोई भी शुभ मनोरथ अधूरा नहीं रहता।"""

english_lyrics = """॥ Shri Lalita Chalisa ॥

॥ Chaupai ॥
Jayati Jayati Jaya Lalite Maataa। Tava Guna Mahimaa Hai Vikhyaataa॥1॥
Too Sundaree, Tripureshwaree Devee। Sura Nara Muni Tere Pada Sevee॥2॥
Too Kalyaanee Kashta Nivaarinee। Too Sukha Daayinee, Vipadaa Haarinee॥3॥
Moha Vinaashinee Daitya Naashinee। Bhakta Bhaavinee Jyoti Prakaashinee॥4॥
Aadi Shakti Shree Vidyaa Roopaa। Chakra Svaaminee Deha Anoopaa॥5॥
Hridaya Nivaasinee-Bhakta Taarinee। Naanaa Kashta Vipati Dala Haarinee॥6॥
Dasha Vidyaa Hai Roopa Tumhaaraa। Shree Chandreshwaree Naimisha Pyaaraa॥7॥
Dhoomaa, Bagalaa, Bhairavee, Taaraa। Bhuvaneeshwaree, Kamalaa, Vistaaraa॥8॥
Shodhashee, Chhinnamastaa, Maatangee। Laliteshakti Tumhaaree Sangee॥9॥
Lalite Tuma Ho Jyotita Bhaalaa। Bhakta Janon Kaa Kaama Sambhaalaa॥10॥
Bhaaree Sankata Jaba-Jaba Aaye। Unase Tumane Bhakta Bachaaye॥11॥
Jisane Kripaa Tumhaaree Paayee। Usakee Saba Vidhi Se Bana Aayee॥12॥
Sankata Doora Karo Maan Bhaaree। Bhakta Janon Ko Aasa Tumhaaree॥13॥
Tripureshwaree, Shailajaa, Bhavaanee। Jaya Jaya Jaya Shiva Kee Mahaaraanee॥14॥
Yoga Siddi Paaven Saba Yogee। Bhogen Bhoga Mahaa Sukha Bhogee॥15॥
Kripaa Tumhaaree Paake Maataa। Jeevana Sukhamaya Hai Bana Jaataa॥16॥
Dukhiyon Ko Tumane Apanaayaa। Mahaa Moodha Jo Sharana Na Aayaa॥17॥
Tumane Jisakee Ora Nihaaraa। Milee Use Sampatti, Sukha Saaraa॥18॥
Aadi Shakti Jaya Tripura Pyaaree। Mahaashakti Jaya Jaya, Bhaya Haaree॥19॥
Kula Yoginee, Kundalinee Roopaa। Leelaa Lalite Karen Anoopaa॥20॥
Mahaa-Maheshwaree, Mahaa Shakti De। Tripura-Sundaree Sadaa Bhakti De॥21॥
Mahaa Mahaa-Nande Kalyaanee। Mookon Ko Detee Ho Vaanee॥22॥
Ichhaa-Gyaana-Kriyaa Kaa Bhaagee। Hotaa Taba Sevaa Anuraagee॥23॥
Jo Lalite Teraa Guna Gaave। Use Na Ko-ee Kashta Sataave॥24॥
Sarva Mangale Jvaalaa-Maalinee। Tuma Ho Sarva Shakti Sanchaalinee॥25॥
Aayaa Maan Jo Sharana Tumhaaree। Vipadaa Haree Usee Kee Saaree॥26॥
Naamaa Karshinee, Chintaa Karshinee। Sarva Mohinee Saba Sukha-Varshinee॥27॥
Mahimaa Tava Saba Jaga Vikhyaataa। Tuma Ho Dayaamayee Jaga Maataa॥28॥
Saba Saubhaagya Daayinee Lalitaa। Tuma Ho Sukhadaa Karunaa Kalitaa॥29॥
Aananda, Sukha, Sampatti Detee Ho। Kashta Bhayaanaka Hara Letee Ho॥30॥
Mana Se Jo Jana Tumako Dhyaave। Vaha Turanta Mana Vaanchhita Paave॥31॥
Lakshmee, Durgaa Tuma Ho Kaalee। Tumheen Shaaradaa Chakra-Kapaalee॥32॥
Moolaadhaara, Nivaasinee Jaya Jaya। Sahasraara Gaaminee Maan Jaya Jaya॥33॥
Chhah Chakron Ko Bhedane Vaalee। Karatee Ho Sabakee Rakhavaalee॥34॥
Yogee, Bhogee, Krodhee, Kaamee। Saba Hain Sevaka Saba Anugaamee॥35॥
Sabako Paara Lagaatee Ho Maan। Saba Para Dayaa Dikhatee Ho Maan॥36॥
Hemavatree, Umaa, BrahmaaNee। Bhandaasura Ki Hridaya Vidaarinee॥37॥
Sarva Vipati Hara, Sarvaadhaare। Tumane Kutila Kupanthee Taare॥38॥
Chandra- Dhaarinee, Naimishvaasinee। Kripaa Karo Lalite Adhanaashinee॥39॥
Bhakta Janon Ko Darasa Dikhaao। Sanshaya Bhaya Saba Sheeghra Mitaao॥40॥
Jo Ko-ee Padhe Lalitaa Chaaleesaa। Hove Sukha Aananda Adheesaa॥41॥
Jisa Para Ko-ee Sankata Aave। Paatha Kare Sankata Mita Jaave॥42॥
Dhyaana Lagaa Padhe Ikkeesa Baaraa। Poorna Manoratha Hove Saaraa॥43॥
Putra-Heena Santati Sukha Paave। Nirdhana Dhanee Bane Guna Gaave॥44॥
Isa Vidhi Paatha Kare Jo Ko-ee। Duhkha Bandhana Chhoote Sukha Ho-ee॥45॥
Jitendra Chandra Bhaarateeya Bataaven। Padhen Chaaleesaa To Sukha Paaven॥46॥
Sabase Laghu Upaaya Yaha Jaano। Siddha Hoya Mana Men Jo Thaano॥47॥
Lalitaa Kare Hridaya Men Baasaa। Siddi Deta Lalitaa Chaaleesaa॥48॥

॥ Doha ॥
Lalite Maan Aba Kripaa Karo, Siddha Karo Saba Kaama।
Shraddhaa Se Sira Naaya Kare, Karate Tumhen Pranaama॥"""

# 1. Update drik_chalisa_29 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["devi"]["items"]:
    if item["id"] == "drik_chalisa_29":
        item["title"] = "ललिता माता चालीसा"
        item["title_en"] = "Lalita Mata Chalisa"
        item["en_line"] = "Jayati Jayati Jai Lalite Mata"
        item["hi_line"] = "जयति जयति जय ललिते माता"
        item["sub"] = "जयति जयति जय ललिते माता • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_lalita_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=JKpk-MH-1CE"
        item["video_id"] = "JKpk-MH-1CE"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/lalita-mata/lalita-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "आदिशक्ति राजराजेश्वरी ललिता त्रिपुरसुन्दरी"
        item["section"] = "दिव्य देवी माता चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_29 in drik_chalisa_collections.json successfully!")

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

# 3. Add or update chalisa_lalita in CONTENT in app.js
content_obj = {
    "title": "श्री ललिता माता चालीसा",
    "title_en": "Shri Lalita Mata Chalisa",
    "en_line": "Jayati Jayati Jai Lalite Mata",
    "hi_line": "जयति जयति जय ललिते माता",
    "sub": "जयति जयति जय ललिते माता • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_lalita_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=JKpk-MH-1CE",
    "video_id": "JKpk-MH-1CE",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/lalita-mata/lalita-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "आदिशक्ति राजराजेश्वरी ललिता त्रिपुरसुन्दरी",
    "section": "दिव्य देवी माता चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

lalita_content_js = "  chalisa_lalita: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_lalita: {" in app_text:
    pos_l = app_text.find("  chalisa_lalita: {")
    pos_next = app_text.find("\n  chalisa_", pos_l + 1)
    if pos_next == -1:
        pos_next = app_text.find("\n  sundarkand:", pos_l + 1)
    app_text = app_text[:pos_l] + lalita_content_js + app_text[pos_next+1:]
    print("Replaced existing chalisa_lalita in CONTENT!")
else:
    # Insert right after chalisa_shakambhari
    pos_sh = app_text.find("  chalisa_shakambhari: {")
    if pos_sh != -1:
        pos_saras = app_text.find("  chalisa_saraswati: {", pos_sh)
        if pos_saras != -1:
            app_text = app_text[:pos_saras] + lalita_content_js + app_text[pos_saras:]
            print("Inserted chalisa_lalita before chalisa_saraswati in CONTENT!")
        else:
            print("ERROR: Could not find chalisa_saraswati!")
    else:
        print("ERROR: Could not find chalisa_shakambhari!")

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
