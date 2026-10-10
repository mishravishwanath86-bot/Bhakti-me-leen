import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री नर्मदा देवी चालीसा ॥

॥ दोहा ॥
देवि पूजिता नर्मदा, महिमा बड़ी अपार।
चालीसा वर्णन करत, कवि अरु भक्त उदार॥
इनकी सेवा से सदा, मिटते पाप महान।
तट पर कर जप दान नर, पाते हैं नित ज्ञान॥

॥ चौपाई ॥
जय-जय-जय नर्मदा भवानी। तुम्हरी महिमा सब जग जानी॥१॥
अमरकण्ठ से निकलीं माता। सर्व सिद्धि नव निधि की दाता॥२॥
कन्या रूप सकल गुण खानी। जब प्रकटीं नर्मदा भवानी॥३॥
सप्तमी सूर्य मकर रविवारा। अश्वनि माघ मास अवतारा॥४॥
वाहन मकर आपको साजैं। कमल पुष्प पर आप विराजैं॥५॥
ब्रह्मा हरि हर तुमको ध्यावैं। तब ही मनवांछित फल पावैं॥६॥
दर्शन करत पाप कटि जाते। कोटि भक्त गण नित्य नहाते॥७॥
जो नर तुमको नित ही ध्यावै। वह नर रुद्र लोक को जावैं॥८॥
मगरमच्छ तुम में सुख पावैं। अन्तिम समय परमपद पावैं॥९॥
मस्तक मुकुट सदा ही साजैं। पांव पैंजनी नित ही राजैं॥१०॥
कल-कल ध्वनि करती हो माता। पाप ताप हरती हो माता॥११॥
पूरब से पश्चिम की ओरा। बहतीं माता नाचत मोरा॥१२॥
शौनक ऋषि तुम्हरौ गुण गावैं। सूत आदि तुम्हरौ यश गावैं॥१३॥
शिव गणेश भी तेरे गुण गावैं। सकल देव गण तुमको ध्यावैं॥१४॥
कोटि तीर्थ नर्मदा किनारे। ये सब कहलाते दुःख हारे॥१५॥
मनोकामना पूरण करती। सर्व दुःख माँ नित ही हरतीं॥१६॥
कनखल में गंगा की महिमा। कुरुक्षेत्र में सरस्वती महिमा॥१७॥
पर नर्मदा ग्राम जंगल में। नित रहती माता मंगल में॥१८॥
एक बार करके असनाना। तरत पीढ़ी है नर नारा॥१९॥
मेकल कन्या तुम ही रेवा। तुम्हरी भजन करें नित देवा॥२०॥
जटा शंकरी नाम तुम्हारा। तुमने कोटि जनों को तारा॥२१॥
समोद्भवा नर्मदा तुम हो। पाप मोचनी रेवा तुम हो॥२२॥
तुम महिमा कहि नहिं जाई। करत न बनती मातु बड़ाई॥२३॥
जल प्रताप तुममें अति माता। जो रमणीय तथा सुख दाता॥२४॥
चाल सर्पिणी सम है तुम्हारी। महिमा अति अपार है तुम्हारी॥२५॥
तुम में पड़ी अस्थि भी भारी। छुवत पाषाण होत वर वारी॥२६॥
यमुना में जो मनुज नहाता। सात दिनों में वह फल पाता॥२७॥
सरसुति तीन दिनों में देतीं। गंगा तुरत बाद ही देतीं॥२८॥
पर रेवा का दर्शन करके। मानव फल पाता मन भर के॥२९॥
तुम्हरी महिमा है अति भारी। जिसको गाते हैं नर-नारी॥३०॥
जो नर तुम में नित्य नहाता। रुद्र लोक मे पूजा जाता॥३१॥
जड़ी बूटियां तट पर राजें। मोहक दृश्य सदा ही साजें॥३२॥
वायु सुगन्धित चलती तीरा। जो हरती नर तन की पीरा॥३३॥
घाट-घाट की महिमा भारी। कवि भी गा नहिं सकते सारी॥३४॥
नहिं जानूँ मैं तुम्हरी पूजा। और सहारा नहीं मम दूजा॥३५॥
हो प्रसन्न ऊपर मम माता। तुम ही मातु मोक्ष की दाता॥३६॥
जो मानव यह नित है पढ़ता। उसका मान सदा ही बढ़ता॥३७॥
जो शत बार इसे है गाता। वह विद्या धन दौलत पाता॥३८॥
अगणित बार पढ़ै जो कोई। पूरण मनोकामना होई॥३९॥
सबके उर में बसत नर्मदा। यहां वहां सर्वत्र नर्मदा॥४०॥

॥ दोहा ॥
भक्ति भाव उर आनि के, जो करता है जाप।
माता जी की कृपा से, दूर होत सन्ताप॥"""

meaning = """॥ श्री नर्मदा देवी चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "देवि पूजिता नर्मदा, महिमा बड़ी अपार। चालीसा वर्णन करत, कवि अरु भक्त उदार॥"
भावार्थ: समस्त देवताओं द्वारा पूजित माँ नर्मदा की महिमा अत्यंत असीम और अपार है। उदार कवि और अनन्य भक्तजन श्रद्धापूर्वक इनकी चालीसा का गुणगान करते हैं।
• "इनकी सेवा से सदा, मिटते पाप महान। तट पर कर जप दान नर, पाते हैं नित ज्ञान॥"
भावार्थ: माँ नर्मदा की पवित्र सेवा-आराधना करने से जन्म-जन्मांतरों के घोर पाप भी नष्ट हो जाते हैं। इनके पावन तट पर जप, तप और दान करने से मनुष्य को नित्य दिव्य ज्ञान व आत्मशांति की प्राप्ति होती है।

【४० चौपाइयां — भावार्थ】
१-३. "जय-जय-जय नर्मदा भवानी... जब प्रकटीं नर्मदा भवानी॥"
भावार्थ: हे माँ नर्मदा भवानी! आपकी सदा-सदा जय हो; आपकी महिमा संपूर्ण जगत में विख्यात है। आप अमरकंटक (मैकल पर्वत) से अवतरित हुई हैं और भक्तों को समस्त सिद्धियां और नौ निधियां प्रदान करने वाली हैं। जब नर्मदा भवानी प्रकट हुईं, तो समस्त दिव्य गुणों की खान, परम सुंदरी कन्या रूप में आपका प्राकट्य हुआ।

४-६. "सप्तमी सूर्य मकर रविवारा... तब ही मनवांछित फल पावैं॥"
भावार्थ: माघ मास के शुक्ल पक्ष की सप्तमी तिथि (नर्मदा जयंती), रविवार के दिन, मकर राशि में सूर्य के प्रवेश काल में आपका पावन अवतरण हुआ। आपकी पावन सवारी मकर (मगरमच्छ) सुशोभित है और आप दिव्य कमल पुष्प पर विराजित हैं। सृष्टिकर्ता ब्रह्मा, पालनकर्ता श्री हरि विष्णु और संहारकर्ता देवाधिदेव महादेव शिव भी आपका ध्यान करते हैं, तभी वे मनवांछित कार्यों को सिद्ध करते हैं।

७-१०. "दर्शन करत पाप कटि जाते... पांव पैंजनी नित ही राजैं॥"
भावार्थ: आपके मात्र दर्शन करने से ही मनुष्य के संचित पाप कट जाते हैं; करोड़ों भक्तजन नित्य आपके पावन जल में स्नान करते हैं। जो साधक नित्य आपका ध्यान करता है, वह मृत्यु के उपरांत शिवलोक (रुद्रलोक) को प्राप्त होता है। आपके जल में विचरण करने वाले मगरमच्छ व जलचर भी सुख भोगकर अंत में परम पद पाते हैं। आपके मस्तक पर रत्नजड़ित मुकुट और चरणों में बजने वाली सुंदर पैंजनियां (नूपुर) सदा शोभायमान रहती हैं।

११-१४. "कल-कल ध्वनि करती हो माता... सकल देव गण तुमको ध्यावैं॥"
भावार्थ: हे माता! आप मधुर कल-कल ध्वनि के साथ प्रवाहित होती हैं और अपने जल से जीवों के समस्त पापों और तापों को हर लेती हैं। आप भारत की एकमात्र ऐसी अनोखी नदी हैं जो पूर्व से पश्चिम की ओर मयूरों को नचाती हुई प्रवाहित होती हैं। शौनक ऋषि, सूत जी, देवाधिदेव महादेव शिव, प्रथम पूज्य श्री गणेश और समस्त देवतागण आपके यश और गुणों का निरंतर गान करते हैं।

१५-२०. "कोटि तीर्थ नर्मदा किनारे... तुम्हरी भजन करें नित देवा॥"
भावार्थ: माँ नर्मदा के दोनों तटों पर करोड़ों तीर्थ (जैसे अमरकंटक, भेड़ाघाट, ओंकारेश्वर, महेश्वर) विद्यमान हैं, जो सभी दुखों का नाश करने वाले हैं। आप भक्तों की सभी मनोकामनाएं पूर्ण करती हैं और उनके समस्त कष्ट हर लेती हैं। कनखल में केवल गंगा जी की और कुरुक्षेत्र में सरस्वती जी की विशेष महिमा है; किंतु माँ नर्मदा अपने संपूर्ण प्रवाह में हर ग्राम, वन और पर्वत पर समान रूप से मंगलमयी हैं। आपके जल में मात्र एक बार स्नान करने से मनुष्य की अनेक पीढ़ियां तर जाती हैं। मैकल पर्वत की कन्या होने से 'मेकलसुता' और वेगवती होने से 'रेवा' नाम से देवता आपकी पूजा करते हैं।

२१-२६. "जटा शंकरी नाम तुम्हारा... छुवत पाषाण होत वर वारी॥"
भावार्थ: भगवान शिव के शरीर/जटाओं से प्रकट होने के कारण आपका नाम 'जटाशंकरी' और 'शिवतनया' है; आपने करोड़ों जीवों का उद्धार किया है। आप समोद्भवा, पापमोचनी रेवा हैं; आपकी महिमा अवर्णनीय है। आपका जल अत्यंत रमणीय, सुखप्रद और रोगनाशक है। आपकी चाल सुंदर सर्पिणी के समान वक्राकार है। आपके जल का ऐसा अलौकिक चमत्कार है कि इसमें विसर्जित की गई अस्थियां भी कुछ ही समय में पाषाण (शिवलिंग रूपी पावन नर्मदेश्वर बाणलिंग) बन जाती हैं; 'नर्मदा के कंकड़ सब शंकर समाना'!

२७-३०. "यमुना में जो मनुज नहाता... जिसको गाते हैं नर-नारी॥"
भावार्थ: यमुना जी में सात दिनों तक स्नान करने पर जो पुण्य फल मिलता है, सरस्वती जी में तीन दिनों के स्नान से जो फल मिलता है, और गंगा जी में डुबकी लगाने से जो फल मिलता है; वही संपूर्ण फल माँ नर्मदा (रेवा) के मात्र दर्शन और स्मरण करने से ही मनुष्य को परिपूर्ण रूप से प्राप्त हो जाता है! आपकी ऐसी महान महिमा का गान सभी नर-नारी करते हैं।

३१-३४. "जो नर तुम में नित्य नहाता... कवि भी गा नहिं सकते सारी॥"
भावार्थ: जो मनुष्य नित्य आपके जल में स्नान करता है, वह रुद्रलोक (शिवलोक) में आदरपूर्वक पूजा जाता है। आपके दोनों पावन तटों पर दुर्लभ औषधीय जड़ी-बूटियां सुशोभित हैं, जो मनोहारी दृश्य बनाती हैं। आपके तटों पर बहने वाली सुगंधित पावन वायु मनुष्यों की समस्त शारीरिक व मानसिक पीड़ाओं को हर लेती है। आपके एक-एक पावन घाट की महिमा इतनी अपार है कि बड़े-बड़े कवि भी उसका पूर्ण वर्णन नहीं कर सकते।

३५-४०. "नहिं जानूँ मैं तुम्हरी पूजा... यहां वहां सर्वत्र नर्मदा॥"
भावार्थ: हे माँ! मैं आपकी विधिवत पूजा-अर्चना नहीं जानता, संसार में आपके अतिरिक्त मेरा कोई दूसरा सहारा नहीं है। हे माते! मुझ पर प्रसन्न होइए, आप ही साक्षात् मोक्षदायिनी हैं। जो मनुष्य नित्य इस चालीसा का पाठ करता है, समाज में उसका मान-सम्मान सदा बढ़ता है। जो सौ बार इसका गायन करता है, वह विद्या, धन और ऐश्वर्य प्राप्त करता है। अगणित बार श्रद्धा से पाठ करने पर सभी मनोकामनाएं सिद्ध होती हैं; सबके हृदय में और संपूर्ण चराचर में माँ नर्मदा ही रमण कर रही हैं।

【समापन दोहा】
• "भक्ति भाव उर आनि के, जो करता है जाप। माता जी की कृपा से, दूर होत सन्ताप॥"
भावार्थ: जो भी भक्त अपने हृदय में निश्चल भक्तिभाव धारण करके माँ नर्मदा के नाम का जप और चालीसा का पाठ करता है, माँ नर्मदा भवानी की अहैतुकी कृपा से उसके जीवन के तीनों ताप व समस्त संताप सदा के लिए दूर हो जाते हैं।"""

vidhi = """॥ श्री नर्मदा देवी चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- प्रातःकाल ब्रह्म मुहूर्त या सूर्योदय के समय पूर्व अथवा उत्तर दिशा की ओर मुख करके पाठ करना सर्वश्रेष्ठ है।
- पावन पर्व: नर्मदा जयंती (माघ शुक्ल सप्तमी), प्रत्येक मास की पूर्णिमा व अमावस्या, सावन मास के सोमवार, तथा मकर संक्रांति।

२. नर्मदा स्नान व आचमन नियम:
- यदि माँ नर्मदा के तट पर हों, तो ॐ नमः शिवाय या 'त्वदीय पाद पंकजं नमामि देवि नर्मदे' बोलकर पवित्र भाव से स्नान करें।
- यदि घर पर हों, तो साधारण जल में कुछ बूंदें नर्मदा जल मिलाकर स्नान करें।
- स्नान के उपरांत श्वेत, पीले अथवा लाल स्वच्छ वस्त्र धारण कर कुशा या ऊनी आसन पर बैठें।

३. पूजन सामग्री:
- गाय के शुद्ध देशी घी का दीपक।
- माँ नर्मदा शिवतनया हैं, अतः पूजन में श्वेत चंदन, अक्षत, श्वेत पुष्प और विशेष रूप से बिल्वपत्र (बेलपत्र) अवश्य अर्पित करें।
- भोग: कच्चा गाय का दूध, मिश्री, खीर, ऋतुफल (विशेषकर केला, अमरूद), अथवा बेसन के लड्डू।
- माँ नर्मदा को अर्पित करने हेतु चुनरी, सिंदूर, रोली और श्रीफल।

४. नर्मदा दीपदान व परिक्रमा विधान:
- सांध्यकाल सूर्यास्त के समय नर्मदा तट पर अथवा घर के पूजा स्थल में पत्तों के दोने में पुष्प रखकर घी का दीपक प्रज्वलित करें और दीपदान करें।
- विश्व भर में केवल माँ नर्मदा की ही संपूर्ण परिक्रमा (लगभग ३,४०० किमी) की जाती है, जो जन्म-जन्मांतरों के पापों का नाश कर मोक्ष प्रदान करती है। सामान्य भक्त घर में बैठकर माँ नर्मदा के चित्र की ७ या ११ परिक्रमा भी कर सकते हैं।

५. पाठ का क्रम:
- सर्वप्रथम आचमन व पवित्रीकरण करें।
- भगवान शिव व गणेश जी का ध्यान कर 'ॐ नर्मदायै नमः' अथवा 'त्वदीय पादपङ्कजं नमामि देवि नर्मदे' मंत्र का ११ या २१ बार जप करें।
- तदोपरांत एकाग्रचित्त होकर नर्मदा चालीसा का पाठ करें (१, ३, ७ या ११ बार)।
- पाठ के उपरांत नर्मदा जी की आरती गाएं और सभी में नर्मदा जल का चरणामृत व प्रसाद वितरित करें।"""

significance = """॥ श्री नर्मदा देवी चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'स्नानेन गंगा, पानेन यमुना, स्मरणाद् रेवा' — अद्वितीय प्रभाव:
सनातन शास्त्रों (स्कंद पुराण, पद्म पुराण, नर्मदा पुराण) में माँ नर्मदा की महिमा को अद्वितीय बताया गया है। गंगा में स्नान से, यमुना में आचमन से, किंतु माँ रेवा (नर्मदा) के केवल दर्शन व नाम-स्मरण मात्र से ही मनुष्य को संपूर्ण तीर्थों के स्नान का फल प्राप्त हो जाता है।

२. 'नर्मदा के कंकड़ सब शंकर समाना':
माँ नर्मदा भगवान शिव के पसीने और जटाओं से प्रकट हुई 'जटाशंकरी' और शिवतनया हैं। इसी कारण नर्मदा से प्राप्त होने वाला प्रत्येक पत्थर स्वतः प्रतिष्ठित 'नर्मदेश्वर शिवलिंग' होता है, जिसकी पूजा घर में करने से साक्षात् महादेव और माँ पार्वती का अखंड वास रहता है।

३. पूर्व से पश्चिम विपरीत प्रवाह — कुंडलिनी जागरण प्रतीक:
माँ नर्मदा भारत की एकमात्र ऐसी महापुण्यमयी नदी हैं जो पूर्व से पश्चिम की ओर उल्टी दिशा में बहती हैं। यौगिक दृष्टि से यह साधक के भीतर सुषुम्ना नाड़ी में कुंडलिनी शक्ति के ऊर्ध्वगामी प्रवाह का साक्षात् प्रतीक है, जो साधक को आत्मज्ञान और मोक्ष की ओर ले जाता है।

४. इक्कीस पीढ़ियों का उद्धार व पितृ तर्पण:
"एक बार करके असनाना। तरत पीढ़ी है नर नारा॥"
माँ नर्मदा के पावन जल में स्नान व तर्पण करने से साधक के पितर परम तृप्त होकर आशीर्वाद देते हैं और जातक की इक्कीस पीढ़ियों का उद्धार होता है।

५. कालसर्प, विष बाधा व ग्रह पीड़ा से मुक्ति:
नर्मदा जी की सर्पाकार चाल और शिवतनया स्वरूप के कारण, इनके चालीसा का नित्य पाठ करने से कुंडली में स्थित कालसर्प दोष, राहु-केतु की महादशा, अकाल मृत्यु का भय और समस्त शारीरिक व्याधियां शांत हो जाती हैं। अंत समय में साधक को शिवलोक (रुद्रलोक) की प्राप्ति होती है।"""

english_lyrics = """॥ Shri Narmada Devi Chalisa ॥

॥ Doha ॥
Devi Poojitaa Narmadaa, Mahimaa Badee Apaara।
Chaaleesaa Varnana Karata, Kavi Aru Bhakta Udaara॥
Inakee Sevaa Se Sadaa, Mitate Paapa Mahaana।
Tata Para Kara Japa Daana Nara, Paate Hain Nita Gyaana॥

॥ Chaupai ॥
Jaya-Jaya-Jaya Narmadaa Bhavaanee। Tumharee Mahimaa Saba Jaga Jaanee॥1॥
Amarakanthha Se Nikaleen Maataa। Sarva Siddhi Nava Nidhi Kee Daataa॥2॥
Kanyaa Roopa Sakala Guna Khaanee। Jaba Prakateen Narmadaa Bhavaanee॥3॥
Saptamee Soorya Makara Ravivaaraa। Ashvani Maagha Maasa Avataaraa॥4॥
Vaahana Makara Aapako Saajain। Kamala Pushpa Para Aapa Viraajain॥5॥
Brahmaa Hari Hara Tumako Dhyaavain। Taba Hee Manavaanchhita Phala Paavain॥6॥
Darshana Karata Paapa Kati Jaate। Koti Bhakta Gana Nitya Nahaate॥7॥
Jo Nara Tumako Nita Hee Dhyaavai। Vaha Nara Rudra Loka Ko Jaavain॥8॥
Magaramachchha Tuma Men Sukha Paavain। Antima Samaya Paramapada Paavain॥9॥
Mastaka Mukuta Sadaa Hee Saajain। Paanva Painjanee Nita Hee Raajain॥10॥
Kala-Kala Dhvani Karatee Ho Maataa। Paapa Taapa Haratee Ho Maataa॥11॥
Pooraba Se Pashchima Kee Oraa। Bahateen Maataa Naachata Moraa॥12॥
Shaunaka Rishi Tumharau Guna Gaavain। Soota Aadi Tumharau Yasha Gaavain॥13॥
Shiva Ganesha Bhee Tere Guna Gaavain। Sakala Deva Gana Tumako Dhyaavain॥14॥
Koti Teertha Narmadaa Kinaare। Ye Saba Kahalaate Dukha Haare॥15॥
Manokaamanaa Poorana Karatee। Sarva Dukha Maan Nita Hee Harateen॥16॥
Kanakhala Men Gangaa Kee Mahimaa। Kurukshetra Men Saraswatee Mahimaa॥17॥
Para Narmadaa Graama Jangala Men। Nita Rahatee Maataa Mangala Men॥18॥
Eka Baara Karake Asanaanaa। Tarata Peedhee Hai Nara Naaraa॥19॥
Mekala Kanyaa Tuma Hee Revaa। Tumharee Bhajana Karain Nita Devaa॥20॥
Jataa Shankaree Naama Tumhaaraa। Tumane Koti Janon Ko Taaraa॥21॥
Samodbhavaa Narmadaa Tuma Ho। Paapa Mochanee Revaa Tuma Ho॥22॥
Tuma Mahimaa Kahi Nahin Jaa-ee। Karata Na Banatee Maatu Badaa-ee॥23॥
Jala Prataapa Tumamen Ati Maataa। Jo Ramaneeya Tathaa Sukha Daataa॥24॥
Chaala Sarpinee Sama Hai Tumhaaree। Mahimaa Ati Apaara Hai Tumhaaree॥25॥
Tuma Men Padee Asthi Bhee Bhaaree। Chhuvata Paashaana Hota Vara Vaaree॥26॥
Yamunaa Men Jo Manuja Nahaataa। Saata Dinon Men Vaha Phala Paataa॥27॥
Sarasuti Teena Dinon Men Deteen। Gangaa Turata Baada Hee Deteen॥28॥
Para Revaa Kaa Darshana Karake। Maanava Phala Paataa Mana Bhara Ke॥29॥
Tumharee Mahimaa Hai Ati Bhaaree। Jisako Gaate Hain Nara-Naaree॥30॥
Jo Nara Tuma Men Nitya Nahaataa। Rudra Loka Me Poojaa Jaataa॥31॥
Jadee Bootiyaan Tata Para Raajen। Mohaka Drishya Sadaa Hee Saajen॥32॥
Vaayu Sugandhita Chalatee Teeraa। Jo Haratee Nara Tana Kee Peeraa॥33॥
Ghaata-Ghaata Kee Mahimaa Bhaaree। Kavi Bhee Gaa Nahin Sakate Saaree॥34॥
Nahin Jaanoon Main Tumharee Poojaa। Aura Sahaaraa Nahin Mama Doojaa॥35॥
Ho Prasanna Oopara Mama Maataa। Tuma Hee Maatu Moksha Kee Daataa॥36॥
Jo Maanava Yaha Nita Hai Padhataa। Usakaa Maana Sadaa Hee Badhataa॥37॥
Jo Shata Baara Ise Hai Gaataa। Vaha Vidyaa Dhana Daulata Paataa॥38॥
Aganita Baara Padhai Jo Ko-ee। Poorana Manokaamanaa Ho-ee॥39॥
Sabake Ura Men Basata Narmadaa। Yahaan Vahaan Sarvatra Narmadaa॥40॥

॥ Doha ॥
Bhakti Bhaava Ura Aani Ke, Jo Karataa Hai Jaapa।
Maataa Jee Kee Kripaa Se, Doora Hota Santaapa॥"""

# 1. Update drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["ganga"]["items"]:
    if item["id"] == "drik_chalisa_41":
        item["title"] = "श्री नर्मदा देवी चालीसा"
        item["title_en"] = "Shri Narmada Devi Chalisa"
        item["en_line"] = "Jai Jai Jai Narmada Bhavani"
        item["hi_line"] = "जय-जय-जय नर्मदा भवानी"
        item["sub"] = "जय-जय-जय नर्मदा भवानी • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_ganga_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=Tf23pQjPdxU"
        item["video_id"] = "Tf23pQjPdxU"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/narmada-mata/narmada-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "माँ नर्मदा भवानी (रेवा)"
        item["section"] = "माँ गंगा व पवित्र नदियां चालीसा"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_41 in drik_chalisa_collections.json successfully!")

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

# 3. Add chalisa_narmada in CONTENT in app.js
content_obj = {
    "title": "श्री नर्मदा देवी चालीसा",
    "title_en": "Shri Narmada Devi Chalisa",
    "en_line": "Jai Jai Jai Narmada Bhavani",
    "hi_line": "जय-जय-जय नर्मदा भवानी",
    "sub": "जय-जय-जय नर्मदा भवानी • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_ganga_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=Tf23pQjPdxU",
    "video_id": "Tf23pQjPdxU",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/narmada-mata/narmada-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "माँ नर्मदा भवानी (रेवा)",
    "section": "माँ गंगा व पवित्र नदियां चालीसा",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

narmada_content_js = "  chalisa_narmada: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_narmada: {" in app_text:
    m_start = app_text.find("  chalisa_narmada: {")
    m_end = app_text.find("\n  chalisa_", m_start + 1)
    if m_end != -1:
        app_text = app_text[:m_start] + narmada_content_js + app_text[m_end+1:]
        print("Replaced existing chalisa_narmada in CONTENT!")
else:
    # Insert right after chalisa_ganga
    g_pos = app_text.find("  chalisa_ganga: {")
    if g_pos != -1:
        g_end = app_text.find("\n  chalisa_", g_pos + 1)
        if g_end == -1:
            g_end = app_text.find("\n  sundarkand:", g_pos + 1)
        if g_end != -1:
            app_text = app_text[:g_end+1] + narmada_content_js + app_text[g_end+1:]
            print("Inserted chalisa_narmada after chalisa_ganga in CONTENT!")
    else:
        v_pos = app_text.find("  chalisa_vishwakarma: {")
        if v_pos != -1:
            app_text = app_text[:v_pos] + narmada_content_js + app_text[v_pos:]
            print("Inserted chalisa_narmada before chalisa_vishwakarma in CONTENT!")

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
