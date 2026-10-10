import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री श्याम चालीसा ॥
(खाटू श्याम जी चालीसा)

॥ दोहा ॥
श्री गुरु चरण ध्यान धर, सुमिरि सच्चिदानन्द।
श्याम चालीसा भणत हूँ, रच चैपाई छन्द॥

॥ चौपाई ॥
श्याम श्याम भजि बारम्बारा। सहज ही हो भवसागर पारा॥१॥
इन सम देव न दूजा कोई। दीन दयालु न दाता होई॥२॥
भीमसुपुत्र अहिलवती जाया। कहीं भीम का पौत्र कहाया॥३॥
यह सब कथा सही कल्पान्तर। तनिक न मानों इसमें अन्तर॥४॥
बर्बरीक विष्णु अवतारा। भक्तन हेतु मनुज तनु धारा॥५॥
वसुदेव देवकी प्यारे। यशुमति मैया नन्द दुलारे॥६॥
मधुसूदन गोपाल मुरारी। बृजकिशोर गोवर्धन धारी॥७॥
सियाराम श्री हरि गोविन्दा। दीनपाल श्री बाल मुकुन्दा॥८॥
दामोदर रणछोड़ बिहारी। नाथ द्वारिकाधीश खरारी॥९॥
नरहरि रुप प्रहलाद प्यारा। खम्भ फारि हिरनाकुश मारा॥१०॥
राधा वल्लभ रुक्मिणी कंता। गोपी वल्लभ कंस हनंता॥११॥
मनमोहन चित्तचोर कहाये। माखन चोरि चोरि कर खाये॥१२॥
मुरलीधर यदुपति घनश्याम। कृष्ण पतितपावन अभिरामा॥१३॥
मायापति लक्ष्मीपति ईसा। पुरुषोत्तम केशव जगदीशा॥१४॥
विश्वपति त्रिभुवन उजियारा। दीन बन्धु भक्तन रखवारा॥१५॥
प्रभु का भेद कोई न पाया। शेष महेश थके मुनिराया॥१६॥
नारद शारद ऋषि योगिन्दर। श्याम श्याम सब रटत निरन्तर॥१७॥
करि कोविद करि सके न गिनन्ता। नाम अपार अथाह अनन्ता॥१८॥
हर सृष्टि हर युग में भाई। ले अवतार भक्त सुखदाई॥१९॥
हृदय माँहि करि देखु विचारा। श्याम भजे तो हो निस्तारा॥२०॥
कीर पढ़ावत गणिका तारी। भीलनी की भक्ति बलिहारी॥२१॥
सती अहिल्या गौतम नारी। भई श्राप वश शिला दुखारी॥२२॥
श्याम चरण रच नित लाई। पहुँची पतिलोक में जाई॥२३॥
अजामिल अरू सदन कसाई। नाम प्रताप परम गति पाई॥२४॥
जाके श्याम नाम अधारा। सुख लहहि दुःख दूर हो सारा॥२५॥
श्याम सुलोचन है अति सुन्दर। मोर मुकुट सिर तन पीताम्बर॥२६॥
गल वैजयन्तिमाल सुहाई। छवि अनूप भक्तन मन भाई॥२७॥
श्याम श्याम सुमिरहु दिनराती। शाम दुपहरि अरू परभाती॥२८॥
श्याम सारथी जिसके रथ के। रोड़े दूर होय उस पथ के॥२९॥
श्याम भक्त न कहीं पर हारा। भीर परि तब श्याम पुकारा॥३०॥
रसना श्याम नाम रस पी ले। जी ले श्याम नाम के हाले॥३१॥
संसारी सुख भोग मिलेगा। अन्त श्याम सुख योग मिलेगा॥३२॥
श्याम प्रभु हैं तन के काले। मन के गोरे भोले भाले॥३३॥
श्याम संत भक्तन हितकारी। रोग दोष अघ नाशै भारी॥३४॥
प्रेम सहित जे नाम पुकारा। भक्त लगत श्याम को प्यारा॥३५॥
खाटू में है मथुरा वासी। पार ब्रह्म पूरण अविनासी॥३६॥
सुधा तान भरि मुरली बजाई। चहुं दिशि नाना जहाँ सुनि पाई॥३७॥
वृद्ध बाल जेते नारी नर। मुग्ध भये सुनि वंशी के स्वर॥३८॥
दौड़ दौड़ पहुँचे सब जाई। खाटू में जहाँ श्याम कन्हाई॥३९॥
जिसने श्याम स्वरूप निहारा। भव भय से पाया छुटकारा॥४०॥

॥ दोहा ॥
श्याम सलोने साँवरे, बर्बरीक तनु धार।
इच्छा पूर्ण भक्त की, करो न लाओ बार॥"""

meaning = """॥ श्री श्याम चालीसा (खाटू श्याम जी) — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहा】
• "श्री गुरु चरण ध्यान धर, सुमिरि सच्चिदानन्द। श्याम चालीसा भणत हूँ, रच चैपाई छन्द॥"
भावार्थ: पूज्य सदगुरुदेव के पावन चरण कमलों का ध्यान करके और सत्य-चित्त-आनंद स्वरूप परमात्मा का स्मरण करते हुए, मैं चौपाई छंदों में श्री श्याम चालीसा का श्रद्धापूर्वक गान करता हूँ।

【४० चौपाइयां — भावार्थ】
१. "श्याम श्याम भजि बारम्बारा। सहज ही हो भवसागर पारा॥"
भावार्थ: जो भक्त बारम्बार 'श्याम-श्याम' नाम का संकीर्तन व जप करता है, वह अत्यंत सुगमता और सहजता से इस अपार भवसागर से पार उतर जाता है।

२. "इन सम देव न दूजा कोई। दीन दयालु न दाता होई॥"
भावार्थ: संसार में खाटू श्याम जी के समान कोई दूसरा कृपालु देव नहीं है। वे दीनों पर दया करने वाले और भक्तों को सब कुछ न्योछावर कर देने वाले सर्वश्रेष्ठ दाता हैं।

३. "भीमसुपुत्र अहिलवती जाया। कहीं भीम का पौत्र कहाया॥"
भावार्थ: आप महाबली भीम के सुपुत्र घटोत्कच और माता अहिलावती (कामकटंकटा) के पुत्र हैं; इस प्रकार आप पाण्डु-पुत्र भीमसेन के प्रतापी पौत्र कहलाते हैं।

४. "यह सब कथा सही कल्पान्तर। तनिक न मानों इसमें अन्तर॥"
भावार्थ: कल्प-भेद और युग-भेद से पुराणों में इनकी कथाएं भिन्न-भिन्न प्रतीत होती हैं, किंतु ये सभी कथाएं सत्य हैं; इनमें तनिक भी भेद या संशय नहीं मानना चाहिए।

५. "बर्बरीक विष्णु अवतारा। भक्तन हेतु मनुज तनु धारा॥"
भावार्थ: आप साक्षात् भगवान श्री हरि विष्णु के अंश 'वीर बर्बरीक' हैं, जिन्होंने कलियुगी जीवों और आर्त भक्तों का उद्धार करने हेतु मनुष्य रूप धारण किया।

६-९. "वसुदेव देवकी प्यारे... नाथ द्वारिकाधीश खरारी॥"
भावार्थ: आप ही वसुदेव-देवकी के नंदन, यशोदा मैया व नंदबाबा के दुलारे हैं। आप ही मधुसूदन, गोपाल, मुरारी, गोवर्धनधारी, सियाराम, गोविंद, बाल मुकुंद, दामोदर, रणछोड़राय और द्वारिकाधीश खरारी हैं।

१०. "नरहरि रुप प्रहलाद प्यारा। खम्भ फारि हिरनाकुश मारा॥"
भावार्थ: अपने अनन्य बाल-भक्त प्रह्लाद की रक्षा करने के लिए आपने ही पाषाण के खंभे को फाड़कर नृसिंह अवतार लिया और दुष्ट हिरण्यकशिपु का वध किया।

११-१५. "राधा वल्लभ रुक्मिणी कंता... दीन बन्धु भक्तन रखवारा॥"
भावार्थ: आप ही राधारमण, रुक्मिणीकांत, गोपियों के प्रियतम और कंस का संहार करने वाले हैं। आप माखनचोर, मुरलीधर, घनश्याम, लक्ष्मीपति, पुरुषोत्तम और त्रिभुवन को प्रकाशित करने वाले दीनानाथ व भक्तों के रक्षक हैं।

१६-२०. "प्रभु का भेद कोई न पाया... श्याम भजे तो हो निस्तारा॥"
भावार्थ: प्रभु की रहस्यमयी लीला का पार शेषनाग, देवाधिदेव महादेव और बड़े-बड़े मुनिराज भी नहीं पा सके। नारद, सरस्वती और बड़े-बड़े ऋषि-योगीजन निरंतर 'श्याम-श्याम' रटते हैं। प्रत्येक युग में भक्तों को सुख देने के लिए प्रभु अवतार लेते हैं; हृदय में विचार कर देखिए, केवल श्याम नाम भजने से ही जीवन का बेड़ा पार होता है।

२१-२५. "कीर पढ़ावत गणिका तारी... सुख लहहि दुःख दूर हो सारा॥"
भावार्थ: तोते को राम नाम रटाते हुए गणिका तर गई, शबरी भीलनी की निष्काम भक्ति पर प्रभु बलिहारी गए, गौतम ऋषि की पत्नी सती अहिल्या आपके चरणरज से पाषाण से मुक्त होकर पतिलोक पहुँची, और अजामिल व सदन कसाई ने नाम-महिमा से परम गति पाई। जिसके जीवन का आधार श्याम नाम है, उसके सारे दुःख मिट जाते हैं और अखंड सुख प्राप्त होता है।

२६-२७. "श्याम सुलोचन है अति सुन्दर। मोर मुकुट सिर तन पीताम्बर॥ गल वैजयन्तिमाल सुहाई। छवि अनूप भक्तन मन भाई॥"
भावार्थ: आपके सुंदर कमलवत नयन अत्यंत मनोहारी हैं। शीश पर मोर मुकुट और शरीर पर दिव्य पीतांबर सुशोभित है। गले में वैजयंती माला विराजमान है; आपकी यह अनुपम छवि भक्तों के मन को मुग्ध कर देती है।

२८-३०. "श्याम श्याम सुमिरहु दिनराती... भीर परि तब श्याम पुकारा॥"
भावार्थ: दिन-रात, प्रातः, दोपहर और संध्या समय निरंतर श्याम नाम का स्मरण करो। जिस भक्त के जीवन-रथ के सारथी स्वयं श्याम प्रभु बन जाते हैं, उसके मार्ग के सारे विघ्न-कंटक दूर हो जाते हैं। 'हारे का सहारा'—श्याम का भक्त कभी हारता नहीं, संकट पड़ते ही जब उसने पुकारा, प्रभु तुरंत रक्षा करते हैं।

३१-३५. "रसना श्याम नाम रस पी ले... भक्त लगत श्याम को प्यारा॥"
भावार्थ: हे जिह्वा! तू श्याम नाम रूपी अमृत रस का पान कर ले और आनंद से जीवन जी। इससे सांसारिक सुख भी मिलेगा और अंत में मोक्ष भी। प्रभु तन से भले श्यामल हैं, किंतु मन से अत्यंत कोमल, भोले-भाले और कृपालु हैं। वे भक्तों के समस्त रोगों, दोषों और पापों का नाश कर देते हैं; जो प्रेम से पुकारता है, वह भक्त प्रभु को प्राणों से प्यारा लगता है।

३६-४०. "खाटू में है मथुरा वासी... भव भय से पाया छुटकारा॥"
भावार्थ: वे ही मथुरावासी सच्चिदानंद परमात्मा आज राजस्थान के पावन 'खाटू धाम' में साक्षात् विराजित हैं। जहाँ से अमृतमयी मुरली की तान गूंजती है, जिसे सुनकर आबाल-वृद्ध, नर-नारी मुग्ध होकर दौड़-दौड़कर खाटू धाम पहुँचते हैं। जिसने भी खाटू श्याम जी के इस दिव्य शीश-स्वरूप का दर्शन कर लिया, वह जन्म-मरण के भव-भय से सदा के लिए मुक्त हो गया।

【समापन दोहा】
• "श्याम सलोने साँवरे, बर्बरीक तनु धार। इच्छा पूर्ण भक्त की, करो न लाओ बार॥"
भावार्थ: हे सलोने साँवरिया सेठ! हे वीर बर्बरीक स्वरूप खाटू नरेश! अपने शरणागत भक्तों की समस्त शुभ मनोकामनाएं शीघ्र पूर्ण कीजिए, अब कृपा करने में तनिक भी विलंब न कीजिए।"""

vidhi = """॥ श्री श्याम चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व दिन:
- शुक्ल पक्ष की एकादशी (ग्यारस) और द्वादशी (बारस) खाटू श्याम जी को परम प्रिय हैं।
- विशेष रूप से फाल्गुन शुक्ल एकादशी (फाल्गुन लक्खी मेला) और कार्तिक शुक्ल एकादशी (देवउठनी ग्यारस) पर पाठ का अनंत गुना फल मिलता है।
- साप्ताहिक रूप से प्रत्येक शनिवार और बुधवार को सांध्यकाल पाठ करना अत्यंत मंगलकारी है।

२. पूजा स्थल व दिशा:
- पूजा स्थल को गंगाजल छिड़ककर पवित्र करें। साधक का मुख पूर्व अथवा उत्तर दिशा की ओर होना चाहिए।
- स्वच्छ पीले अथवा श्वेत आसन पर बैठें।

३. आवश्यक पूजन सामग्री:
- शुद्ध देशी गाय के घी का अथवा चमेली/गुलाब के सुगंधित इत्र युक्त दीपक।
- ताजे गुलाब, मोगरा, पीले या नीले पुष्प, और विशेष रूप से गुलाब का इत्र।
- भोग: खाटू श्याम जी का प्रिय भोग — चूरमा, खीर, मावे के पेड़े, मिश्री-माखन अथवा कच्चा दूध।
- बाबा श्याम का प्रतीक 'निशान' (पंचरंगी या केसरिया ध्वजा) अथवा श्याम जी का शीश स्वरूप चित्र।

४. पाठ का क्रम:
- सर्वप्रथम आचमन व पवित्रीकरण के उपरांत भगवान गणेश जी का ध्यान करें।
- 'ॐ श्री श्यामाय नमः' अथवा 'ॐ श्री खाटूश्याम देवाय नमः' मंत्र की एक माला (१०८ बार) जपें।
- तदोपरांत पूर्ण श्रद्धा व प्रेमभाव से श्री श्याम चालीसा का पाठ करें (१, ३, ७ या ११ बार)।
- अंत में 'ॐ जय श्री श्याम हरे' आरती गाएं और मोरछड़ी का स्पर्श कराकर चरणामृत व प्रसाद ग्रहण करें।

५. मनोकामना पूर्ति संकल्प:
- जो भक्त किसी विशेष संकट, रोग, आर्थिक तंगी अथवा मनोकामना हेतु साधना करना चाहते हैं, वे ११, २१ अथवा ४० दिनों तक प्रतिदिन ३ या ११ पाठ का संकल्प लें।
- "हारे का सहारा — खाटू श्याम हमारा" इस महाभाव के साथ निष्काम सेवा करें और एकादशी के दिन अन्न-जल का त्याग कर फलाहार रखें।"""

significance = """॥ श्री श्याम चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'हारे का सहारा' — कलियुग के साक्षात् कल्पवृक्ष:
महाभारत युद्ध के समय जब भगवान श्री कृष्ण ने वीर बर्बरीक से उनकी दानवीरता की परीक्षा लेने हेतु शीश दान माँगा, तब बर्बरीक ने सहर्ष अपना शीश काटकर प्रभु के चरणों में समर्पित कर दिया। भगवान श्री कृष्ण ने परम प्रसन्न होकर उन्हें अपना स्वयं का नाम 'श्याम' प्रदान किया और वरदान दिया कि कलियुग में तुम मेरे स्वरूप में पूजित होओगे और जो कोई भी संसार से हारकर तुम्हारे द्वार आएगा, तुम उसके सहारे बनोगे।

२. 'श्याम सारथी जिसके रथ के, रोड़े दूर होय उस पथ के':
जिस प्रकार महाभारत में भगवान श्री कृष्ण ने अर्जुन के रथ का सारथ्य कर विजय दिलाई थी, उसी प्रकार जो भक्त नित्य श्याम चालीसा का पाठ करता है, स्वयं खाटू नरेश उसके जीवन-रथ के सारथी बनकर मार्ग की समस्त बाधाएं, रोड़े और संकट दूर कर देते हैं।

३. असाध्य व्याधियों व मानसिक संतापों का नाश:
"श्याम संत भक्तन हितकारी। रोग दोष अघ नाशै भारी॥"
चालीसा के नियमित पाठ से दीर्घकालीन असाध्य रोग, मानसिक तनाव (Depression), भय, नकारात्मक शक्तियां और ग्रहों के अनिष्ट प्रभाव तत्काल शांत होते हैं।

४. आर्थिक संपन्नता व मनोवांछित फल:
व्यापार में घाटा, कर्ज का बोझ, आजीविका का अभाव अथवा संतान बाधा—बाबा श्याम के पावन चालीसा के प्रभाव से साधक को यश, कीर्ति, धन-धान्य और पारिवारिक सुख-शांति की प्राप्ति होती है।

५. खाटू धाम दर्शन का पुण्य फल:
चालीसा में वर्णित है कि जिसने खाटू धाम में विराजित श्री श्याम स्वरूप का भावपूर्ण दर्शन व स्मरण कर लिया, वह जन्म-मरण के चक्रव्यूह से मुक्त होकर अंत समय में परम पद को प्राप्त करता है।"""

english_lyrics = """॥ Shri Shyama Chalisa ॥
(Khatu Shyam Ji Chalisa)

॥ Doha ॥
Shri Guru Charana Dhyaana Dhara, Sumiri Sachchidaananda।
Shyama Chaaleesaa Bhanata Hoon, Racha Chaupaa-ee Chhanda॥

॥ Chaupai ॥
Shyama Shyama Bhaji Baarambaaraa। Sahaja Hee Ho Bhavasaagara Paaraa॥1॥
Ina Sama Deva Na Doojaa Ko-ee। Deena Dayaalu Na Daataa Ho-ee॥2॥
Bheemasuputra Ahilavatee Jaayaa। Kaheen Bheema Kaa Pautra Kahaayaa॥3॥
Yaha Saba Kathaa Sahee Kalpaantara। Tanika Na Maanon Isamen Antara॥4॥
Barbareeka Vishnu Avataaraa। Bhaktana Hetu Manuja Tanu Dhaaraa॥5॥
Vasudeva Devakee Pyaare। Yashumati Maiyaa Nanda Dulaare॥6॥
Madhusoodana Gopaala Muraaree। Brijakishora Govardhana Dhaaree॥7॥
Siyaaraama Shree Hari Govindaa। Deenapaala Shree Baala Mukundaa॥8॥
Daamodara Ranachhoda Bihaaree। Naatha Dwaarikaadheesha Kharaaree॥9॥
Narahari Roopa Prahlaada Pyaaraa। Khambha Phaari Hiranaakusha Maaraa॥10॥
Raadhaa Vallabha Rukminee Kantaa। Gopee Vallabha Kansa Hanantaa॥11॥
Manamohana Chittachora Kahaaye। Maakhana Chori Chori Kara Khaaye॥12॥
Muraleedhara Yadupati Ghanashyama। Krishna Patitapaavana Abhiraamaa॥13॥
Maayaapati Lakshmeepati Eesaa। Purushottama Keshava Jagadeeshaa॥14॥
Vishwapati Tribhuvana Ujiyaaraa। Deena Bandhu Bhaktana Rakhavaaraa॥15॥
Prabhu Kaa Bheda Ko-ee Na Paayaa। Shesha Mahesha Thake Muniraayaa॥16॥
Naarada Saarada Rishi Yogindara। Shyama Shyama Saba Ratata Nirantara॥17॥
Kari Kovida Kari Sake Na Ginantaa। Naama Apaara Athaaha Anantaa॥18॥
Hara Srishti Hara Yuga Men Bhaa-ee। Le Avataara Bhakta Sukhadaa-ee॥19॥
Hridaya Maanhi Kari Dekhu Vichaaraa। Shyama Bhaje To Ho Nistaaraa॥20॥
Keera Padhaavata Ganikaa Taaree। Bheelanee Kee Bhakti Balihaaree॥21॥
Satee Ahilyaa Gautama Naaree। Bha-ee Shraapa Vasha Shilaa Dukhaaree॥22॥
Shyama Charana Racha Nita Laa-ee। Pahunchee Patiloka Men Jaa-ee॥23॥
Ajaamila Aroo Sadana Kasaa-ee। Naama Prataapa Parama Gati Paa-ee॥24॥
Jaake Shyama Naama Adhaaraa। Sukha Lahahi Dukha Doora Ho Saaraa॥25॥
Shyama Surochana Hai Ati Sundara। Mora Mukuta Sira Tana Peetaambara॥26॥
Gala Vaijayantimaala Suhaa-ee। Chhavi Anoopa Bhaktana Mana Bhaa-ee॥27॥
Shyama Shyama Sumirahu Dinaraatee। Shaama Dupahari Aroo Parabhaatee॥28॥
Shyama Saarathi Jisake Ratha Ke। Rode Doora Hoya Usa Patha Ke॥29॥
Shyama Bhakta Na Kaheen Para Haaraa। Bheera Pari Taba Shyama Pukaaraa॥30॥
Rasanaa Shyama Naama Rasa Pee Le। Jee Le Shyama Naama Ke Haale॥31॥
Sansaaree Sukha Bhoga Milegaa। Anta Shyama Sukha Yoga Milegaa॥32॥
Shyama Prabhu Hain Tana Ke Kaale। Mana Ke Gore Bhole Bhaale॥33॥
Shyama Santa Bhaktana Hitakaaree। Roga Dosha Agha Naashai Bhaaree॥34॥
Prema Sahita Je Naama Pukaaraa। Bhakta Lagata Shyama Ko Pyaaraa॥35॥
Khaatoo Men Hai Mathuraa Vaasee। Paara Brahma Poorana Avinaasee॥36॥
Sudhaa Taana Bhari Muralee Bajaa-ee। Chahun Dishi Naanaa Jahaan Suni Paa-ee॥37॥
Vriddha Baala Jete Naaree Nara। Mugdha Bhaye Suni Vanshee Ke Swara॥38॥
Dauda Dauda Pahunche Saba Jaa-ee। Khaatoo Men Jahaan Shyama Kanhaa-ee॥39॥
Jisane Shyama Svaroopa Nihaaraa। Bhava Bhaya Se Paayaa Chhutakaaraa॥40॥

॥ Doha ॥
Shyama Salone Saanvare, Barbareeka Tanu Dhaara।
Ichchhaa Poorna Bhakta Kee, Karo Na Laao Baara॥"""

# 1. Update drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["khatushyam"]["items"]:
    if item["id"] == "drik_chalisa_50":
        item["title"] = "श्री श्याम चालीसा"
        item["title_en"] = "Shri Shyam Chalisa (Khatu Shyam Chalisa)"
        item["en_line"] = "Shyama Shyama Bhaji Barambara"
        item["hi_line"] = "श्याम श्याम भजि बारम्बारा"
        item["sub"] = "श्याम श्याम भजि बारम्बारा • Drik Panchang Verified"
        item["thumb"] = "assets/deity_khatushyam.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=9GLVkIigVbw"
        item["video_id"] = "9GLVkIigVbw"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/shri-shyam/shri-shyam-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "हारे का सहारा श्री खाटू श्याम जी"
        item["section"] = "खाटू श्याम चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_50 in drik_chalisa_collections.json successfully!")

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

# 3. Add chalisa_khatushyam in CONTENT in app.js
content_obj = {
    "title": "श्री श्याम चालीसा",
    "title_en": "Shri Shyam Chalisa (Khatu Shyam Chalisa)",
    "en_line": "Shyama Shyama Bhaji Barambara",
    "hi_line": "श्याम श्याम भजि बारम्बारा",
    "sub": "श्याम श्याम भजि बारम्बारा • Drik Panchang Verified",
    "thumb": "assets/deity_khatushyam.jpg",
    "audio_url": "https://www.youtube.com/watch?v=9GLVkIigVbw",
    "video_id": "9GLVkIigVbw",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/shri-shyam/shri-shyam-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "हारे का सहारा श्री खाटू श्याम जी",
    "section": "खाटू श्याम चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

khatu_content_js = "  chalisa_khatushyam: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_khatushyam: {" in app_text:
    m_start = app_text.find("  chalisa_khatushyam: {")
    m_end = app_text.find("\n  chalisa_", m_start + 1)
    if m_end != -1:
        app_text = app_text[:m_start] + khatu_content_js + app_text[m_end+1:]
        print("Replaced existing chalisa_khatushyam in CONTENT!")
else:
    # Insert right after chalisa_narasimha or before chalisa_vishwakarma
    n_pos = app_text.find("  chalisa_narasimha: {")
    if n_pos != -1:
        n_end = app_text.find("\n  chalisa_", n_pos + 1)
        if n_end == -1:
            n_end = app_text.find("\n  sundarkand:", n_pos + 1)
        if n_end != -1:
            app_text = app_text[:n_end+1] + khatu_content_js + app_text[n_end+1:]
            print("Inserted chalisa_khatushyam after chalisa_narasimha in CONTENT!")
    else:
        v_pos = app_text.find("  chalisa_vishwakarma: {")
        if v_pos != -1:
            app_text = app_text[:v_pos] + khatu_content_js + app_text[v_pos:]
            print("Inserted chalisa_khatushyam before chalisa_vishwakarma in CONTENT!")

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
