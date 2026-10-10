import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Authentic Devanagari Lyrics from Drik Panchang
ganesh_chalisa_content = """॥ श्री गणेश चालीसा ॥
(भगवान श्री गणेश • प्रथम पूज्य विघ्नहर्ता • भाषा: अवधी)

॥ दोहा ॥
जय गणपति सदगुण सदन, कविवर बदन कृपाल।
विघ्न हरण मंगल करण, जय जय गिरिजालाल॥

॥ चौपाई ॥
जय जय जय गणपति गणराजू। मंगल भरण करण शुभः काजू॥
जै गजबदन सदन सुखदाता। विश्व विनायका बुद्धि विधाता॥

वक्र तुण्ड शुची शुण्ड सुहावना। तिलक त्रिपुण्ड भाल मन भावन॥
राजत मणि मुक्तन उर माला। स्वर्ण मुकुट शिर नयन विशाला॥

पुस्तक पाणि कुठार त्रिशूलं। मोदक भोग सुगन्धित फूलं॥
सुन्दर पीताम्बर तन साजित। चरण पादुका मुनि मन राजित॥

धनि शिव सुवन षडानन भ्राता। गौरी लालन विश्व-विख्याता॥
ऋद्धि-सिद्धि तव चंवर सुधारे। मुषक वाहन सोहत द्वारे॥

कहौ जन्म शुभ कथा तुम्हारी। अति शुची पावन मंगलकारी॥
एक समय गिरिराज कुमारी। पुत्र हेतु तप कीन्हा भारी॥

भयो यज्ञ जब पूर्ण अनूपा। तब पहुंच्यो तुम धरी द्विज रूपा॥
अतिथि जानी के गौरी सुखारी। बहुविधि सेवा करी तुम्हारी॥

अति प्रसन्न हवै तुम वर दीन्हा। मातु पुत्र हित जो तप कीन्हा॥
मिलहि पुत्र तुहि, बुद्धि विशाला। बिना गर्भ धारण यहि काला॥

गणनायक गुण ज्ञान निधाना। पूजित प्रथम रूप भगवाना॥
अस कही अन्तर्धान रूप हवै। पालना पर बालक स्वरूप हवै॥

बनि शिशु रुदन जबहिं तुम ठाना। लखि मुख सुख नहिं गौरी समाना॥
सकल मगन, सुखमंगल गावहिं। नाभ ते सुरन, सुमन वर्षावहिं॥

शम्भु, उमा, बहुदान लुटावहिं। सुर मुनिजन, सुत देखन आवहिं॥
लखि अति आनन्द मंगल साजा। देखन भी आये शनि राजा॥

निज अवगुण गुनि शनि मन माहीं। बालक, देखन चाहत नाहीं॥
गिरिजा कछु मन भेद बढायो। उत्सव मोर, न शनि तुही भायो॥

कहत लगे शनि, मन सकुचाई। का करिहौ, शिशु मोहि दिखाई॥
नहिं विश्वास, उमा उर भयऊ। शनि सों बालक देखन कहयऊ॥

पदतहिं शनि दृग कोण प्रकाशा। बालक सिर उड़ि गयो अकाशा॥
गिरिजा गिरी विकल हवै धरणी। सो दुःख दशा गयो नहीं वरणी॥

हाहाकार मच्यौ कैलाशा। शनि कीन्हों लखि सुत को नाशा॥
तुरत गरुड़ चढ़ि विष्णु सिधायो। काटी चक्र सो गज सिर लाये॥

बालक के धड़ ऊपर धारयो। प्राण मन्त्र पढ़ि शंकर डारयो॥
नाम गणेश शम्भु तब कीन्हे। प्रथम पूज्य बुद्धि निधि, वर दीन्हे॥

बुद्धि परीक्षा जब शिव कीन्हा। पृथ्वी कर प्रदक्षिणा लीन्हा॥
चले षडानन, भरमि भुलाई। रचे बैठ तुम बुद्धि उपाई॥

चरण मातु-पितु के धर लीन्हें। तिनके सात प्रदक्षिण कीन्हें॥
धनि गणेश कही शिव हिये हरषे। नभ ते सुरन सुमन बहु बरसे॥

तुम्हरी महिमा बुद्धि बड़ाई। शेष सहसमुख सके न गाई॥
मैं मतिहीन मलीन दुखारी। करहूं कौन विधि विनय तुम्हारी॥

भजत रामसुन्दर प्रभुदासा। जग प्रयाग, ककरा, दुर्वासा॥
अब प्रभु दया दीना पर कीजै। अपनी शक्ति भक्ति कुछ दीजै॥

॥ दोहा ॥
श्री गणेश यह चालीसा, पाठ करै कर ध्यान।
नित नव मंगल गृह बसै, लहे जगत सन्मान॥

सम्बन्ध अपने सहस्र दश, ऋषि पंचमी दिनेश।
पूरण चालीसा भयो, मंगल मूर्ती गणेश॥"""

# 2. Verse-by-verse Spiritual Meaning (पद्यवार पावन भावार्थ)
ganesh_chalisa_meaning = """॥ श्री गणेश चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【आरम्भिक दोहा】
जय गणपति सदगुण सदन, कविवर बदन कृपाल।
विघ्न हरण मंगल करण, जय जय गिरिजालाल॥
भावार्थ: समस्त दिव्य सद्गुणों के धाम, कवियों और भक्तों पर कृपा करने वाले, जीवन के सभी विघ्नों को हरने वाले और सर्वत्र मंगल का संचार करने वाले माता पार्वती (गिरिजा) के लाडले पुत्र श्री गणेश जी की सदा जय हो, जय हो।

【चौपाइयां — भावार्थ】
१. जय जय जय गणपति गणराजू। मंगल भरण करण शुभः काजू॥
जै गजबदन सदन सुखदाता। विश्व विनायका बुद्धि विधाता॥
भावार्थ: हे गणों के अधिपति, देवों के नायक गणपति महाराज! आपकी सदा जय हो। आप जीवन में कल्याण और शुभता भरने वाले तथा सभी शुभ कार्यों को सिद्ध करने वाले हैं। हे गजमुख! आप समस्त सुखों के धाम हैं। आप विश्व के प्रथम पूज्य विनायक और विशुद्ध बुद्धि के साक्षात् विधाता हैं।

२. वक्र तुण्ड शुची शुण्ड सुहावना। तिलक त्रिपुण्ड भाल मन भावन॥
राजत मणि मुक्तन उर माला। स्वर्ण मुकुट शिर नयन विशाला॥
भावार्थ: आपकी घुमावदार और पवित्र सूंड अत्यंत मनोहारी है। आपके मस्तक (भाल) पर लगा त्रिपुण्ड तिलक मन को मोह लेता है। आपके वक्षःस्थल पर बहुमूल्य मणियों और मोतियों की माला शोभा पा रही है। मस्तक पर दिव्य स्वर्ण मुकुट सुशोभित है और आपके विशाल नयन कृपा की वर्षा कर रहे हैं।

३. पुस्तक पाणि कुठार त्रिशूलं। मोदक भोग सुगन्धित फूलं॥
सुन्दर पीताम्बर तन साजित। चरण पादुका मुनि मन राजित॥
भावार्थ: आपके हाथों में ज्ञान की पुस्तक, पाश, कुठार (फरसा) और त्रिशूल सुशोभित हैं। आपको स्वादिष्ट मोदक (लड्डू) और सुगंधित पुष्पों का भोग अर्पित किया जाता है। आपके शरीर पर दिव्य पीताम्बर वस्त्र शोभायमान हैं और आपके श्रीचरणों की पादुकाएं मुनियों और संतों के मन को आनंदित करती हैं।

४. धनि शिव सुवन षडानन भ्राता। गौरी लालन विश्व-विख्याता॥
ऋद्धि-सिद्धि तव चंवर सुधारे। मुषक वाहन सोहत द्वारे॥
भावार्थ: हे भगवान शिव के तेजस्वी पुत्र और छह मुख वाले कार्तिकेय (षडानन) के भ्राता! आप धन्य हैं। माता पार्वती के लाडले पुत्र के रूप में आपकी कीर्ति संपूर्ण विश्व में विख्यात है। साक्षात् ऋद्धि और सिद्धि आपकी सेवा में चंवर डुलाती हैं और आपके पावन द्वार पर मूषक (चूहा) वाहन शोभायमान रहता है।

५. कहौ जन्म शुभ कथा तुम्हारी। अति शुची पावन मंगलकारी॥
एक समय गिरिराज कुमारी। पुत्र हेतु तप कीन्हा भारी॥
भावार्थ: हे प्रभु! अब मैं आपकी परम पवित्र, पावन और मंगलकारी जन्म कथा का वर्णन करता हूँ। एक समय पर्वतराज हिमालय की पुत्री माता पार्वती ने एक गुणवान पुत्र की प्राप्ति हेतु घोर और कठिन तपस्या की।

६. भयो यज्ञ जब पूर्ण अनूपा। तब पहुंच्यो तुम धरी द्विज रूपा॥
अतिथि जानी के गौरी सुखारी। बहुविधि सेवा करी तुम्हारी॥
भावार्थ: जब माता पार्वती का वह अनुपम यज्ञ और तप पूर्ण हुआ, तब आप स्वयं एक तेजस्वी ब्राह्मण (द्विज) का रूप धारण करके वहाँ पहुँचे। माता पार्वती ने आपको दिव्य अतिथि जानकर अत्यंत प्रसन्नता से आपका बहुविधि आदर-सत्कार और सेवा की।

७. अति प्रसन्न हवै तुम वर दीन्हा। मातु पुत्र हित जो तप कीन्हा॥
मिलहि पुत्र तुहि, बुद्धि विशाला। बिना गर्भ धारण यहि काला॥
भावार्थ: माता की अनन्य सेवा और भक्ति से परम प्रसन्न होकर आपने वरदान दिया कि हे माते! आपने पुत्र प्राप्ति हेतु जो तप किया है, उसके फलस्वरुप आपको बिना गर्भ धारण किए ही अत्यंत बुद्धिमान, तेजस्वी, समस्त गुणों और ज्ञान के निधान तथा देवताओं में प्रथम पूज्य पुत्र की प्राप्ति होगी।

८. गणनायक गुण ज्ञान निधाना। पूजित प्रथम रूप भगवाना॥
अस कही अन्तर्धान रूप हवै। पालना पर बालक स्वरूप हवै॥
भावार्थ: जो पुत्र आपको मिलेगा वह गणों का नायक, समस्त ज्ञान व सद्गुणों का अक्षय भंडार तथा देवताओं में सर्वप्रथम पूजित भगवान का साक्षात् स्वरूप होगा। ऐसा कहकर वह ब्राह्मण रूप अंतर्ध्यान हो गया और पालने में साक्षात् एक नवजात दिव्य बालक के रूप में प्रकट हो गया।

९. बनि शिशु रुदन जबहिं तुम ठाना। लखि मुख सुख नहिं गौरी समाना॥
सकल मगन, सुखमंगल गावहिं। नाभ ते सुरन, सुमन वर्षावहिं॥
भावार्थ: जब उस नन्हें शिशु ने रुदन करना आरम्भ किया, तब बालक के तेजस्वी मुख को देखकर माता पार्वती का हृदय असीम आनंद से भर गया। संपूर्ण कैलाशवासी आनंदमग्न होकर मंगल गीत गाने लगे और आकाश से देवतागण पुष्पों की वर्षा करने लगे।

१०. शम्भु, उमा, बहुदान लुटावहिं। सुर मुनिजन, सुत देखन आवहिं॥
लखि अति आनन्द मंगल साजा। देखन भी आये शनि राजा॥
भावार्थ: भगवान शिव और माता पार्वती ने ब्राह्मणों और याचकों को प्रचुर दान दिया। समस्त देवता, ऋषि और मुनिजन उस अद्भुत बालक के दर्शन करने कैलाश पधारे। कैलाश पर इस महामंगल और उत्सव को देखकर सूर्यपुत्र राजा शनिदेव भी बालक के दर्शन करने आए।

११. निज अवगुण गुनि शनि मन माहीं। बालक, देखन चाहत नाहीं॥
गिरिजा कछु मन भेद बढायो। उत्सव मोर, न शनि तुही भायो॥
भावार्थ: शनिदेव अपने मन में यह विचार कर रहे थे कि मुझे अपनी पत्नी का शाप है कि मेरी दृष्टि जिस पर पड़ेगी उसका अनिष्ट हो जाएगा; अतः वे बालक को देखना नहीं चाहते थे। शनिदेव को बालक से विमुख देखकर माता पार्वती के मन में संकोच हुआ कि क्या शनिदेव को मेरा यह पुत्रोत्सव पसंद नहीं आया?

१२. कहत लगे शनि, मन सकुचाई। का करिहौ, शिशु मोहि दिखाई॥
नहिं विश्वास, उमा उर भयऊ। शनि सों बालक देखन कहयऊ॥
भावार्थ: तब शनिदेव संकोच करते हुए बोले कि हे माते! मेरी दृष्टि वक्र है, अतः मुझे यह शिशु न दिखाएं। किंतु माता पार्वती को विश्वास नहीं हुआ और उन्होंने आग्रहपूर्वक शनिदेव को बालक की ओर देखने को कहा।

१३. पदतहिं शनि दृग कोण प्रकाशा। बालक सिर उड़ि गयो अकाशा॥
गिरिजा गिरी विकल हवै धरणी। सो दुःख दशा गयो नहीं वरणी॥
भावार्थ: जैसे ही शनिदेव की दृष्टि का कोण बालक पर पड़ा, बालक का मस्तक धड़ से अलग होकर आकाश में उड़ गया। माता पार्वती अत्यंत व्याकुल होकर मूर्छित हो पृथ्वी पर गिर पड़ीं; उनके उस अगाध दुःख की दशा का वर्णन शब्दों में नहीं किया जा सकता।

१४. हाहाकार मच्यौ कैलाशा। शनि कीन्हों लखि सुत को नाशा॥
तुरत गरुड़ चढ़ि विष्णु सिधायो। काटी चक्र सो गज सिर लाये॥
भावार्थ: समस्त कैलाश पर्वत पर हाहाकार मच गया कि शनिदेव की दृष्टि से सुत का अनिष्ट हो गया। तब इस घोर संकट को देखकर भगवान श्री विष्णु तुरंत गरुड़ पर सवार होकर उत्तर दिशा की ओर गए और अपने सुदर्शन चक्र से एक गज (हाथी) का शीश काटकर ले आए।

१५. बालक के धड़ ऊपर धारयो। प्राण मन्त्र पढ़ि शंकर डारयो॥
नाम गणेश शम्भु तब कीन्हे। प्रथम पूज्य बुद्धि निधि, वर दीन्हे॥
भावार्थ: भगवान विष्णु ने उस गज-शीश को बालक के धड़ पर स्थापित किया और देवाधिदेव भगवान शिव ने वेद मंत्रों का उच्चारण करके उसमें प्राण-प्रतिष्ठा की। भगवान शंकर ने बालक का नाम 'श्री गणेश' रखा और उन्हें देवताओं में 'प्रथम पूज्य' तथा 'समस्त बुद्धियों की निधि' होने का सर्वोच्च वरदान प्रदान किया।

१६. बुद्धि परीक्षा जब शिव कीन्हा। पृथ्वी कर प्रदक्षिणा लीन्हा॥
चले षडानन, भरमि भुलाई। रचे बैठ तुम बुद्धि उपाई॥
भावार्थ: जब एक बार भगवान शिव ने कार्तिकेय और गणेश की बुद्धि परीक्षा लेने हेतु समूची पृथ्वी की परिक्रमा करने की प्रतिस्पर्धा रखी; तब कार्तिकेय जी अपने मयूर पर सवार होकर तुरंत पृथ्वी की परिक्रमा हेतु उड़ चले, परंतु आपने बैठकर अपनी अगाध बुद्धि से एक उपाय निकाला।

१७. चरण मातु-पितु के धर लीन्हें। तिनके सात प्रदक्षिण कीन्हें॥
धनि गणेश कही शिव हिये हरषे। नभ ते सुरन सुमन बहु बरसे॥
भावार्थ: आपने माता पार्वती और पिता भगवान शिव के चरण पकड़ लिए और श्रद्धापूर्वक उनके ही सात फेरे (प्रदक्षिणा) लगा लिए, क्योंकि शास्त्रों के अनुसार माता-पिता के चरणों में ही संपूर्ण ब्रह्मांड और तीर्थ समाहित हैं। गणेश जी की इस अलौकिक बुद्धि पर हर्षित होकर शिवजी ने उन्हें 'धन्य' कहा और आकाश से देवताओं ने पुष्पों की वर्षा की।

१८. तुम्हरी महिमा बुद्धि बड़ाई। शेष सहसमुख सके न गाई॥
मैं मतिहीन मलीन दुखारी। करहूं कौन विधि विनय तुम्हारी॥
भावार्थ: आपकी अगाध बुद्धि और महिमा का पार सहस्र मुख वाले शेषनाग जी भी नहीं पा सकते। मैं तो मतिहीन, अज्ञानी और सांसारिक दुःखों से त्रस्त हूँ, मैं आपकी स्तुति किस प्रकार करूँ!

१९. भजत रामसुन्दर प्रभुदासा। जग प्रयाग, ककरा, दुर्वासा॥
अब प्रभु दया दीना पर कीजै। अपनी शक्ति भक्ति कुछ दीजै॥
भावार्थ: रामसुन्दर दास जी निरंतर आपके नाम का भजन करते हैं। हे दयालु प्रभु! अब मुझ दीन-हीन पर दया कीजिए और मुझे अपनी अनन्य भक्ति और आंतरिक आत्मबल प्रदान कीजिए।

【समापन दोहा】
श्री गणेश यह चालीसा, पाठ करै कर ध्यान।
नित नव मंगल गृह बसै, लहे जगत सन्मान॥
सम्बन्ध अपने सहस्र दश, ऋषि पंचमी दिनेश।
पूरण चालीसा भयो, मंगल मूर्ती गणेश॥
भावार्थ: जो भी मनुष्य एकाग्रचित्त होकर ध्यानपूर्वक इस श्री गणेश चालीसा का नित्य पाठ करता है, उसके घर में नित्य नए-नए मंगल और खुशहाली का वास होता है और वह संसार में सर्वत्र मान-सम्मान प्राप्त करता है। संवत, ऋषि पंचमी के पावन दिन यह चालीसा पूर्ण हुई। मंगलमूर्ति श्री गणेश जी की सदा जय हो!"""

# 3. Authentic Vidhi & Rules (शास्त्रोक्त पाठ विधि व नियम)
ganesh_chalisa_vidhi = """॥ श्री गणेश चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का समय व दिशा:
- प्रातःकाल ब्रह्ममुहूर्त अथवा सांध्यकाल गोधूलि बेला में पूर्व अथवा उत्तर दिशा की ओर मुख करके बैठना सर्वश्रेष्ठ है।
- बुधवार तथा प्रत्येक माह की विनायक चतुर्थी व संकष्टी चतुर्थी पर पाठ करने से अनंत गुना फल प्राप्त होता है।

२. आसन व वस्त्र:
- पीले अथवा लाल रंग के शुद्ध सूती वस्त्र धारण करें।
- कुशा अथवा लाल/पीले ऊनी आसन पर बैठकर पाठ करें।

३. प्रिय पूजन सामग्री व अर्पण (अनिवार्य):
- दूर्वा (दूब घास): श्री गणेश जी को २१ दूर्वा की गांठें अवश्य अर्पित करें। बिना दूर्वा के गणेश पूजन अपूर्ण माना जाता है।
- लाल सिंदूर: गणेश जी के मस्तक और चरणों में लाल सिंदूर का त्रिपुण्ड/तिलक लगाएं।
- मोदक व लड्डू: बेसन या बूंदी के मोदक, मोतीचूर के लड्डू अथवा केले का भोग लगाएं।
- लाल पुष्प: गुड़हल (जवाकुसुम) अथवा लाल गुलाब का पुष्प गणेश जी को अत्यंत प्रिय है।

४. दीपक व धूप:
- शुद्ध देशी गाय के घी अथवा तिल के तेल का दीपक प्रज्वलित करें।
- कर्पूर, गुग्गुल या चंदन की सुगंधित धूप अर्पित करें।

५. पाठ की संख्या व संकल्प:
- सामान्य दैनिक पाठ: नित्य १, ३ या ५ पाठ।
- नवीन कार्य आरम्भ, व्यापार वृद्धि अथवा विघ्न निवारण: २१ दिनों तक प्रतिदिन ११ पाठ का संकल्प लें।
- पाठ के आरम्भ में 'ॐ गं गणपतये नमः' अथवा 'ॐ वक्रतुण्डाय हुम्' का एक माला (१०८ बार) जप अवश्य करें।
- पाठ उपरांत 'जय गणेश जय गणेश देवा' की आरती करें।"""

# 4. Significance & Phalasruti (आध्यात्मिक माहात्म्य व फलश्रुति)
ganesh_chalisa_significance = """॥ श्री गणेश चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'विघ्न हरण मंगल करण' — सर्व विघ्न विनाश व कार्य सिद्धि:
श्री गणेश जी को प्रथम पूज्य और विघ्नहर्ता का वरदान प्राप्त है। किसी भी नए व्यापार, गृह-प्रवेश, विवाह, नवीन पदभार, अध्ययन अथवा यात्रा से पूर्व गणेश चालीसा का पाठ करने से सभी अमंगल और बाधाएं स्वतः समाप्त हो जाती हैं।

२. बुद्धि, ज्ञान व विवेक की प्राप्ति:
'विश्व विनायका बुद्धि विधाता' — विद्यार्थियों, शोधकर्ताओं और बौद्धिक कार्यों से जुड़े साधकों के लिए यह चालीसा विशेष फलदायी है। इसके नित्य पाठ से एकाग्रता, कुशाग्र बुद्धि और स्मरण शक्ति में अप्रत्याशित वृद्धि होती है।

३. रिद्धि-सिद्धि व वास्तु दोष निवारण:
ऋद्धि और सिद्धि गणेश जी की शक्तियां हैं। जहाँ गणेश जी की आराधना होती है, वहाँ दरिद्रता, गृह-क्लेश और नकारात्मक ऊर्जा का नाश होकर सुख, शांति और वैभव का वास होता है।

४. शनि दोष व ग्रह बाधा शांति:
चालीसा में वर्णित शनिदेव प्रसंग के अनुसार गणेश चालीसा का पाठ करने वाले साधक पर शनिदेव की वक्र दृष्टि का अशुभ प्रभाव नहीं पड़ता और नवग्रहों की अनुकूलता प्राप्त होती है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह चालीसा द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक अवधी छंदों पर पूर्णतः आधारित है।"""

# 5. English Transliteration (रोमन लिपि)
ganesh_chalisa_en = """॥ Shri Ganesha Chalisa ॥
(By Ram Sundar Das • Awadhi)

॥ Doha ॥
Jaya Ganapati Sadaguna Sadana, Kavivara Badana Kripaala।
Vighna Harana Mangala Karana, Jaya Jaya Girijaalaala॥

॥ Chaupai ॥
Jaya Jaya Jaya Ganapati Ganaraajoo। Mangala Bharana Karana Shubha Kaajoo॥
Jai Gajabadana Sadana Sukhadaataa। Vishwa Vinaayakaa Buddhi Vidhaataa॥

Vakra Tunda Shuchee Shunda Suhaavanaa। Tilaka Tripunda Bhaala Mana Bhaavana॥
Raajata Mani Muktana Ura Maalaa। Swarna Mukuta Shira Nayana Vishaalaa॥

Pustaka Paani Kuthaara Trishoolam। Modaka Bhoga Sugandhita Phoolam॥
Sundara Peetaambara Tana Saajita। Charana Paadukaa Muni Mana Raajita॥

Dhani Shiva Suvana Shadaanana Bhraataa। Gauree Laalana Vishwa-Vikhyaataa॥
Riddhi-Siddhi Tava Chanvara Sudhaare। Mushaka Vaahana Sohata Dvaare॥

Kahau Janma Shubha Kathaa Tumhaaree। Ati Shuchee Paavana Mangalakaaree॥
Eka Samaya Giriraaja Kumaaree। Putra Hetu Tapa Keenhaa Bhaaree॥

Bhayo Yagya Jaba Poorna Anoopaa। Taba Pahunchyo Tuma Dharee Dvija Roopaa॥
Atithi Jaanee Ke Gauree Sukhaaree। Bahuvidhi Sevaa Karee Tumhaaree॥

Ati Prasanna Havai Tuma Vara Deenhaa। Maatu Putra Hita Jo Tapa Keenhaa॥
Milihi Putra Tuhi, Buddhi Vishaalaa। Binaa Garbha Dhaarana Yahi Kaalaa॥

Gananayaka Guna Gyaana Nidhaanaa। Poojita Prathama Roopa Bhagavaanaa॥
Asa Kahee Antardhaana Roopa Havai। Paalanaa Para Baalaka Svaroopa Havai॥

Bani Shishu Rudana Jabahin Tuma Thaanaa। Lakhi Mukha Sukha Nahin Gauree Samaanaa॥
Sakala Magana, Sukhamangala Gaavahin। Naabha Te Surana, Sumana Varshaavahin॥

Shambhu, Umaa, Bahudaana Lutaavahin। Sura Munijana, Suta Dekhana Aavahin॥
Lakhi Ati Aananda Mangala Saajaa। Dekhana Bhee Aaye Shani Raajaa॥

Nija Avaguna Guni Shani Mana Maaheen। Baalaka, Dekhana Chaahata Naaheen॥
Girijaa Kachhu Mana Bheda Badhaayo। Utsava Mora, Na Shani Tuhee Bhaayo॥

Kahata Lage Shani, Mana Sakuchaayee। Kaa Karihau, Shishu Mohi Dikhaa-ee॥
Nahin Vishwaasa, Umaa Ura Bhaya-oo। Shani Son Baalaka Dekhana Kahaya-oo॥

Padatahin Shani Driga Kona Prakaashaa। Baalaka Sira Udi Gayo Aakaashaa॥
Girijaa Giree Vikala Havai Dharanee। So Dukha Dashaa Gayo Naheen Varanee॥

Haahaakaara Machyau Kailaashaa। Shani Keenhon Lakhi Suta Ko Naashaa॥
Turata Garuda Chadhi Vishnu Sidhaayo। Kaatee Chakra So Gaja Sira Laaye॥

Baalaka Ke Dhada Oopara Dhaarayau। Praana Mantra Padhi Shankara Daarayau॥
Naama Ganesha Shambhu Taba Keenhe। Prathama Poojya Buddhi Nidhi, Vara Deenhe॥

Buddhi Pareekshaa Jaba Shiva Keenhaa। Prithvee Kara Pradakshinaa Leenhaa॥
Chale Shadaanana, Bharami Bhulaa-ee। Rache Baitha Tuma Buddhi Upaa-ee॥

Charana Maatu-Pitu Ke Dhara Leenhen। Tinake Saata Pradakshina Keenhen॥
Dhani Ganesha Kahee Shiva Hiye Harashe। Nabha Te Surana Sumana Bahu Barase॥

Tumharee Mahimaa Buddhi Badaa-ee। Shesha Sahasamukha Sake Na Gaa-ee॥
Main Matiheena Maleena Dukhaaree। Karahoon Kauna Vidhi Vinaya Tumhaaree॥

Bhajata Raamasundara Prabhudaasaa। Jaga Prayaaga, Kakaraa, Durvaasaa॥
Aba Prabhu Dayaa Deenaa Para Keejai। Apanee Shakti Bhakti Kuchha Deejai॥

॥ Doha ॥
Shri Ganesha Yaha Chaaleesaa, Paatha Karai Kara Dhyaana।
Nita Nava Mangala Griha Basai, Lahe Jagata Sanmaana॥

Sambandha Apane Sahasra Dasha, Rishi Panchamee Dinesha।
Poorana Chaaleesaa Bhayo, Mangala Moortee Ganesha॥"""

# 6. Update drik_chalisa_collections.json
with open('drik_chalisa_collections.json', encoding='utf-8') as f:
    chalisa_data = json.load(f)

for it in chalisa_data['ganesh']['items']:
    if it['id'] == 'drik_chalisa_3':
        it['title'] = 'श्री गणेश चालीसा'
        it['title_en'] = 'Shree Ganesha Chalisa (Shri Ganesh Chalisa)'
        it['hi_line'] = 'जय जय जय गणपति गणराजू'
        it['en_line'] = 'Jai Jai Jai Ganapati Ganraju'
        it['sub'] = 'प्रथम पूज्य विघ्नहर्ता पावन चालीसा • Drik Panchang Verified'
        it['thumb'] = 'assets/gallery/bal_ganesha_little.jpg'
        it['video_id'] = 'WyHFSjN0miU'
        it['audio_url'] = 'https://www.youtube.com/watch?v=WyHFSjN0miU'
        it['drik_url'] = 'https://www.drikpanchang.com/lyrics/chalisa/lord-ganesha/shree-ganesha-chalisa.html?lang=hi&ck=1'
        it['source'] = 'Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)'
        it['content'] = ganesh_chalisa_content
        it['meaning'] = ganesh_chalisa_meaning
        it['vidhi'] = ganesh_chalisa_vidhi
        it['significance'] = ganesh_chalisa_significance
        it['english_lyrics'] = ganesh_chalisa_en
        print("Updated drik_chalisa_3 in drik_chalisa_collections.json!")
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

# Add or update chalisa_ganesh in CONTENT in app.js
c_ganesh_record = f"""chalisa_ganesh: {{
    title: 'श्री गणेश चालीसा',
    deity: 'विघ्नहर्ता श्री गणेश जी महाराज',
    mantra: '॥ ॐ गं गणपतये नमः • ॐ वक्रतुण्डाय हुम् ॥',
    text: `{ganesh_chalisa_content}`,
    meaning: `{ganesh_chalisa_meaning}`,
    vidhi: `{ganesh_chalisa_vidhi}`,
    significance: `{ganesh_chalisa_significance}`,
    english_lyrics: `{ganesh_chalisa_en}`,
    audio_url: 'https://www.youtube.com/watch?v=WyHFSjN0miU',
    video_id: 'WyHFSjN0miU',
    thumb: 'assets/gallery/bal_ganesha_little.jpg',
    drik_url: 'https://www.drikpanchang.com/lyrics/chalisa/lord-ganesha/shree-ganesha-chalisa.html?lang=hi&ck=1'
  }},
  """

if 'chalisa_ganesh:' in app_js:
    pos_g = app_js.find('chalisa_ganesh:')
    pos_g_end = app_js.find('chalisa_', pos_g + 20)
    app_js = app_js[:pos_g] + c_ganesh_record + app_js[pos_g_end:]
    print("Replaced existing chalisa_ganesh in CONTENT!")
else:
    # Insert right before chalisa_bajrang_baan:
    pos_baj = app_js.find('chalisa_bajrang_baan:')
    if pos_baj != -1:
        app_js = app_js[:pos_baj] + c_ganesh_record + app_js[pos_baj:]
        print("Inserted chalisa_ganesh before chalisa_bajrang_baan in CONTENT!")
    else:
        print("Warning: chalisa_bajrang_baan not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Saved app.js successfully!")
