import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Authentic Devanagari Lyrics from Drik Panchang
vindhyeshwari_chalisa_content = """॥ श्री विन्ध्येश्वरी चालीसा ॥
(परम पावन विन्ध्याचल निवासिनी माँ विन्ध्यवासिनी • भाषा: अवधी / ब्रज)

॥ दोहा ॥
नमो नमो विन्ध्येश्वरी, नमो नमो जगदम्ब।
सन्तजनों के काज में, माँ करती नहीं विलम्ब॥

॥ चौपाई ॥
जय जय जय विन्ध्याचल रानी। आदि शक्ति जग विदित भवानी॥
सिंहवाहिनी जै जग माता। जय जय जय त्रिभुवन सुखदाता॥

कष्ट निवारिनी जय जग देवी। जय जय जय जय असुरासुर सेवी॥
महिमा अमित अपार तुम्हारी। शेष सहस मुख वर्णत हारी॥

दीनन के दुःख हरत भवानी। नहिं देख्यो तुम सम कोई दानी॥
सब कर मनसा पुरवत माता। महिमा अमित जगत विख्याता॥

जो जन ध्यान तुम्हारो लावै। सो तुरतहि वांछित फल पावै॥
तू ही वैष्णवी तू ही रुद्राणी। तू ही शारदा अरु ब्रह्माणी॥

रमा राधिका शामा काली। तू ही मात सन्तन प्रतिपाली॥
उमा माधवी चण्डी ज्वाला। बेगि मोहि पर होहु दयाला॥

तू ही हिंगलाज महारानी। तू ही शीतला अरु विज्ञानी॥
दुर्गा दुर्ग विनाशिनी माता। तू ही लक्श्मी जग सुखदाता॥

तू ही जान्हवी अरु उत्रानी। हेमावती अम्बे निर्वानी॥
अष्टभुजी वाराहिनी देवी। करत विष्णु शिव जाकर सेवी॥

चोंसट्ठी देवी कल्यानी। गौरी मंगला सब गुण खानी॥
पाटन मुम्बा दन्त कुमारी। भद्रकाली सुन विनय हमारी॥

वज्रधारिणी शोक नाशिनी। आयु रक्शिणी विन्ध्यवासिनी॥
जया और विजया बैताली। मातु सुगन्धा अरु विकराली॥

नाम अनन्त तुम्हार भवानी। बरनैं किमि मानुष अज्ञानी॥
जा पर कृपा मातु तव होई। तो वह करै चहै मन जोई॥

कृपा करहु मो पर महारानी। सिद्धि करिय अम्बे मम बानी॥
जो नर धरै मातु कर ध्याना। ताकर सदा होय कल्याना॥

विपत्ति ताहि सपनेहु नहिं आवै। जो देवी कर जाप करावै॥
जो नर कहं ऋण होय अपारा। सो नर पाठ करै शत बारा॥

निश्चय ऋण मोचन होई जाई। जो नर पाठ करै मन लाई॥
अस्तुति जो नर पढ़े पढ़ावे। या जग में सो बहु सुख पावै॥

जाको व्याधि सतावै भाई। जाप करत सब दूरि पराई॥
जो नर अति बन्दी महं होई। बार हजार पाठ कर सोई॥

निश्चय बन्दी ते छुटि जाई। सत्य बचन मम मानहु भाई॥
जा पर जो कछु संकट होई। निश्चय देबिहि सुमिरै सोई॥

जो नर पुत्र होय नहिं भाई। सो नर या विधि करे उपाई॥
पांच वर्ष सो पाठ करावै। नौरातर में विप्र जिमावै॥

निश्चय होय प्रसन्न भवानी। पुत्र देहि ताकहं गुण खानी॥
ध्वजा नारियल आनि चढ़ावै। विधि समेत पूजन करवावै॥

नित प्रति पाठ करै मन लाई। प्रेम सहित नहिं आन उपाई॥
यह श्री विन्ध्याचल चालीसा। रंक पढ़त होवे अवनीसा॥

यह जनि अचरज मानहु भाई। कृपा दृष्टि तापर होई जाई॥
जय जय जय जगमातु भवानी। कृपा करहु मो पर जन जानी॥

॥ दोहा ॥
ऋद्धि सिद्धि सब सम्पदा, देहु मात वरदान।
विन्ध्यवासिनी शरण में, राखहु निज कल्यान॥"""

# 2. Verse-by-verse Spiritual Meaning (पद्यवार सम्पूर्ण पावन भावार्थ)
vindhyeshwari_chalisa_meaning = """॥ श्री विन्ध्येश्वरी चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【आरम्भिक दोहा】
नमो नमो विन्ध्येश्वरी, नमो नमो जगदम्ब।
सन्तजनों के काज में, माँ करती नहीं विलम्ब॥
भावार्थ: विन्ध्याचल पर्वत पर निवास करने वाली माँ विन्ध्येश्वरी को बारम्बार नमन है! सम्पूर्ण जगत की जननी माँ जगदम्बा को बारम्बार प्रणाम है! अपने शरणागत साधु-संतों और निष्कपट भक्तों के कार्यों को सिद्ध करने में माँ भगवती तनिक भी विलंब नहीं करतीं।

【चौपाइयां — भावार्थ】
१. जय जय जय विन्ध्याचल रानी। आदि शक्ति जग विदित भवानी॥
सिंहवाहिनी जै जग माता। जय जय जय त्रिभुवन सुखदाता॥
भावार्थ: हे विन्ध्याचल की महारानी माँ विन्ध्यवासिनी! आपकी सदा जय हो, जय हो, जय हो! आप ही सम्पूर्ण जगत में प्रसिद्ध आद्यशक्ति माँ भवानी हैं। सिंह की सवारी करने वाली हे जगन्माता! तीनों लोकों को समस्त सुख व आनंद प्रदान करने वाली माँ! आपकी जय हो।

२. कष्ट निवारिनी जय जग देवी। जय जय जय जय असुरासुर सेवी॥
महिमा अमित अपार तुम्हारी। शेष सहस मुख वर्णत हारी॥
भावार्थ: भक्तों के समस्त कष्टों व संतापों का निवारण करने वाली हे देवी! देवता और असुर सभी नतमस्तक होकर आपके पावन चरणों की सेवा करते हैं। आपकी महिमा असीम और अपार है, जिसका सम्पूर्ण वर्णन करने में सहस्र मुख वाले शेषनाग जी भी असमर्थ हो जाते हैं।

३. दीनन के दुःख हरत भवानी। नहिं देख्यो तुम सम कोई दानी॥
सब कर मनसा पुरवत माता। महिमा अमित जगत विख्याता॥
भावार्थ: हे माँ भवानी! आप दीन-दुखियों के समस्त कष्टों को पल भर में हर लेती हैं। सम्पूर्ण संसार में आपके समान कोई दूसरा उदार दानी नहीं है। आप सभी प्राणियों के मन की धर्मयुक्त इच्छाओं को पूर्ण करती हैं, आपकी अलौकिक महिमा तीनों लोकों में विख्यात है।

४. जो जन ध्यान तुम्हारो लावै। सो तुरतहि वांछित फल पावै॥
तू ही वैष्णवी तू ही रुद्राणी। तू ही शारदा अरु ब्रह्माणी॥
भावार्थ: जो मनुष्य एकाग्रचित्त होकर आपके श्रीचरणों का ध्यान करता है, वह तत्काल ही मनवांछित फल प्राप्त कर लेता है। आप ही भगवान विष्णु की शक्ति वैष्णवी, महादेव शिव की शक्ति रुद्राणी, विद्या की देवी शारदा और ब्रह्मा जी की शक्ति ब्रह्माणी हैं।

५. रमा राधिका शामा काली। तू ही मात सन्तन प्रतिपाली॥
उमा माधवी चण्डी ज्वाला। बेगि मोहि पर होहु दयाला॥
भावार्थ: आप ही महालक्ष्मी (रमा), श्री राधिका जी, श्यामा और महाकाली हैं। आप ही साधु-संतों का ममतापूर्वक प्रतिपालन करने वाली परम जननी हैं। आप ही उमा, माधवी, चण्डिका और ज्योतिर्मयी ज्वाला जी हैं। हे करुणामयी माँ! मुझ पर शीघ्र ही अपनी दया दृष्टि कीजिए।

६. तू ही हिंगलाज महारानी। तू ही शीतला अरु विज्ञानी॥
दुर्गा दुर्ग विनाशिनी माता। तू ही लक्श्मी जग सुखदाता॥
भावार्थ: हिंगलाज शक्तिपीठ में महारानी के रूप में आप ही विराजमान हैं। शीतलता प्रदान करने वाली माँ शीतला और साक्षात् आत्म-विद्या (विज्ञानी) आप ही हैं। दुर्गम संकटों का नाश करने वाली माँ दुर्गा और सम्पूर्ण जगत को सुख-समृद्धि देने वाली माँ महालक्ष्मी भी आप ही हैं।

७. तू ही जान्हवी अरु उत्रानी। हेमावती अम्बे निर्वानी॥
अष्टभुजी वाराहिनी देवी। करत विष्णु शिव जाकर सेवी॥
भावार्थ: आप ही पतित-पावनी गंगा (जाह्नवी), हिमालय-पुत्री पार्वती (हेमावती) और मोक्ष प्रदायिनी अम्बे हैं। विन्ध्याचल में विराजमान माँ अष्टभुजी और वाराही देवी आप ही हैं, जिनकी नित्य आराधना स्वयं भगवान श्री हरि विष्णु और देवाधिदेव महादेव शिव जी करते हैं।

८. चोंसट्ठी देवी कल्यानी। गौरी मंगला सब गुण खानी॥
पाटन मुम्बा दन्त कुमारी। भद्रकाली सुन विनय हमारी॥
भावार्थ: चौंसठ योगिनियों के रूप में आप ही कल्याण करने वाली हैं, सर्वमंगलदायिनी माँ गौरी और समस्त सद्गुणों की खान आप ही हैं। पाटन देवी, मुम्बा देवी, दन्त कुमारी और माँ भद्रकाली! हम पर कृपा कीजिए और हमारी दीन प्रार्थना सुनिए।

९. वज्रधारिणी शोक नाशिनी। आयु रक्शिणी विन्ध्यवासिनी॥
जया और विजया बैताली। मातु सुगन्धा अरु विकराली॥
भावार्थ: आप वज्र धारण करने वाली, समस्त शोकों का नाश करने वाली और भक्तों की अकाल मृत्यु से रक्षा कर दीर्घायु प्रदान करने वाली माँ विन्ध्यवासिनी हैं। आप ही जया, विजया, वैताली, सुगन्धा और दुष्टों के लिए विकराल कालिका हैं।

१०. नाम अनन्त तुम्हार भवानी। बरनैं किमि मानुष अज्ञानी॥
जा पर कृपा मातु तव होई। तो वह करै चहै मन जोई॥
भावार्थ: हे माँ भवानी! आपके अनन्त नाम और अनंत स्वरूप हैं, मुझ जैसा अल्पज्ञानी मनुष्य उनका पूर्ण वर्णन कैसे कर सकता है? जिस साधक पर आपकी कृपादृष्टि हो जाती है, वह संसार में जो भी शुभ कार्य करना चाहता है, वह सहज ही सिद्ध हो जाता है।

११. कृपा करहु मो पर महारानी। सिद्धि करिय अम्बे मम बानी॥
जो नर धरै मातु कर ध्याना। ताकर सदा होय कल्याना॥
भावार्थ: हे महारानी माँ विन्ध्येश्वरी! मुझ पर अपनी असीम कृपा कीजिए और मेरी वाणी को सिद्ध व निर्मल बना दीजिए। जो भी मनुष्य श्रद्धापूर्वक माँ के चरणों का ध्यान धरता है, उसका सर्वदा सर्वत्र कल्याण ही कल्याण होता है।

१२. विपत्ति ताहि सपनेहु नहिं आवै। जो देवी कर जाप करावै॥
जो नर कहं ऋण होय अपारा। सो नर पाठ करै शत बारा॥
भावार्थ: जो भक्त देवी के पावन मंत्रों का जाप करता है अथवा कराता है, उसके जीवन में स्वप्न में भी कभी कोई विपत्ति नहीं आती। जिस मनुष्य पर अत्यधिक कर्ज़ (अपार ऋण) का बोझ हो, वह यदि इस चालीसा का सौ (१००) बार पाठ करे—

१३. निश्चय ऋण मोचन होई जाई। जो नर पाठ करै मन लाई॥
अस्तुति जो नर पढ़े पढ़ावे। या जग में सो बहु सुख पावै॥
भावार्थ: तो वह निश्चय ही सम्पूर्ण ऋण (कर्ज) के बंधन से मुक्त हो जाता है, बशर्ते वह एकाग्र मन लगाकर पाठ करे। जो मनुष्य इस पावन स्तुति को स्वयं पढ़ता है और दूसरों को सुनाता है, वह इस संसार में समस्त ऐश्वर्य और सुखों को भोगता है।

१४. जाको व्याधि सतावै भाई। जाप करत सब दूरि पराई॥
जो नर अति बन्दी महं होई। बार हजार पाठ कर सोई॥
भावार्थ: जिस किसी को भी असाध्य शारीरिक व्याधियां और रोग सताते हों, वह माँ के नाम-जाप से तत्काल रोगमुक्त हो जाता है। जो मनुष्य किसी कारणवश कारागार (जेल या कानूनी बंधन) में बंदी हो, वह यदि श्रद्धापूर्वक एक हजार (१०००) बार इसका पाठ करे—

१५. निश्चय बन्दी ते छुटि जाई। सत्य बचन मम मानहु भाई॥
जा पर जो कछु संकट होई। निश्चय देबिहि सुमिरै सोई॥
भावार्थ: तो वह निश्चित रूप से कारागार और सभी बंधनों से छूट जाता है, यह सत्य वचन है। जिस किसी पर भी जीवन में कोई भी भारी संकट या ऊपरी बाधा आ पड़े, वह निष्कपट भाव से माँ विन्ध्येश्वरी का स्मरण करे।

१६. जो नर पुत्र होय नहिं भाई। सो नर या विधि करे उपाई॥
पांच वर्ष सो पाठ करावै। नौरातर में विप्र जिमावै॥
भावार्थ: जिस दंपत्ति के कोई संतान (पुत्र) न हो, वह इस शास्त्रोक्त विधि से उपाय करे—पाँच वर्षों तक लगातार नियमपूर्वक नवरात्रि में पाठ कराए अथवा करे और नवरात्रि की पूर्णाहुति पर ब्राह्मणों व कन्याओं को आदरपूर्वक भोजन कराए।

१७. निश्चय होय प्रसन्न भवानी। पुत्र देहि ताकहं गुण खानी॥
ध्वजा नारियल आनि चढ़ावै। विधि समेत पूजन करवावै॥
भावार्थ: ऐसा करने से माँ भवानी निश्चय ही प्रसन्न होती हैं और उस दंपत्ति को समस्त गुणों की खान, तेजस्वी व सुयोग्य पुत्र रत्न प्रदान करती हैं। भक्तजन विन्ध्याचल धाम में आकर लाल ध्वजा और नारियल भेंट करें तथा विधिवत पूजन संपन्न कराएं।

१८. नित प्रति पाठ करै मन लाई। प्रेम सहित नहिं आन उपाई॥
यह श्री विन्ध्याचल चालीसा। रंक पढ़त होवे अवनीसा॥
भावार्थ: प्रतिदिन जो मनुष्य अनन्य प्रेम और एकाग्रता से इस चालीसा का पाठ करता है, उसके लिए संसार में अन्य किसी कठिन उपाय की आवश्यकता नहीं रह जाती। इस परम सिद्ध विन्ध्याचल चालीसा के प्रभाव से अत्यंत निर्धन (रंक) व्यक्ति भी राजाओं (अवनीश) के समान ऐश्वर्यवान हो जाता है।

१९. यह जनि अचरज मानहु भाई। कृपा दृष्टि तापर होई जाई॥
जय जय जय जगमातु भवानी। कृपा करहु मो पर जन जानी॥
भावार्थ: हे भाइयो! इसमें तनिक भी आश्चर्य न करें, क्योंकि जिस पर जगदम्बा की कृपादृष्टि हो जाती है, उसके लिए कुछ भी असंभव नहीं रहता। हे सम्पूर्ण जगत की माता भवानी! आपकी सदा जय हो, जय हो, जय हो! मुझे अपना अनन्य सेवक जानकर मुझ पर सदा अपनी कृपा बनाए रखिए।

【समापन दोहा】
ऋद्धि सिद्धि सब सम्पदा, देहु मात वरदान।
विन्ध्यवासिनी शरण में, राखहु निज कल्यान॥
भावार्थ: हे माँ विन्ध्यवासिनी! हमें ऋद्धि-सिद्धि और समस्त शुभ संपदाओं का वरदान दीजिए। हम सर्वभाव से आपकी शरण में हैं, सदा हमारा परम कल्याण कीजिए।"""

# 3. Authentic Worship Procedure & Rules (शास्त्रोक्त पाठ विधि व नियम)
vindhyeshwari_chalisa_vidhi = """॥ श्री विन्ध्येश्वरी चालीसा पाठ एवं पूजन विधि व नियम ॥

१. पावन काल व विशेष मुहूर्त:
• प्रतिदिन प्रातःकाल अथवा संध्याकाल में पाठ करना अत्यंत मंगलकारी है।
• विशेष रूप से चैत्र एवं शारदीय नवरात्रि (नौ दिन), मासिक दुर्गाष्टमी, ज्येष्ठ मास के मंगलवार, तथा प्रत्येक शुक्रवार को विन्ध्येश्वरी चालीसा का पाठ अनंत गुना फलदायी है।

२. आवश्यक पूजन सामग्री:
• माँ विन्ध्यवासिनी / माँ दुर्गा का पावन चित्र या विग्रह।
• शुद्ध गाय के घी का दीपक, धूप, अगरबत्ती, कपूर।
• लाल पुष्प (विशेषकर लाल गुड़हल अथवा गुलाब), रोली, कुमकुम, अक्षत, सिन्दूर।
• लाल चुनरी, नारियल (लाल कलावा बंधा हुआ), लाल ध्वजा।
• नैवेद्य: हलवा, पूड़ी, चना, बताशा, लौंग, ऋतुफल, पेड़ा अथवा खीर।

३. शास्त्रोक्त पूजन विधान:
• स्नानादि कर स्वच्छ लाल या पीले वस्त्र धारण करें।
• पूर्व अथवा उत्तर दिशा की ओर मुख करके कुशा या लाल ऊन के आसन पर बैठें।
• सम्मुख पाटे पर लाल वस्त्र बिछाकर माँ विन्ध्यवासिनी का चित्र स्थापित करें।
• शुद्ध घी का दीपक प्रज्वलित कर सर्वप्रथम श्री गणेश जी एवं भैरव जी का स्मरण करें।
• माँ विन्ध्येश्वरी को कुमकुम का तिलक लगाएं, अक्षत, लाल पुष्प, सिन्दूर और चुनरी अर्पित करें।
• नारियल, बताशा और हलवा-पूड़ी का प्रेमपूर्वक भोग लगाएं।
• हाथ में जल लेकर संकल्प करें और पूर्ण श्रद्धा व स्पष्ट वाणी से चालीसा का पाठ करें।
• पाठ पूर्ण होने पर 'ॐ विन्ध्यवासिन्यै नमः' अथवा 'जय विन्ध्याचल रानी' का १०८ बार जप करें और कपूर से आरती करें।

४. विशेष मनोकामना अनुष्ठान नियम:
• ऋण मुक्ति हेतु: लगातार शत (१००) बार पाठ करने का विशेष विधान है।
• बन्दी/कारागार मुक्ति हेतु: १००० बार श्रद्धापूर्वक पाठ करने से बंधन कटते हैं।
• संतान प्राप्ति हेतु: लगातार ५ वर्षों तक दोनों नवरात्रों में चालीसा पाठ एवं कन्या/विप्र भोज कराएं।"""

# 4. Spiritual Significance & Fruits (आध्यात्मिक महत्त्व व फलश्रुति)
vindhyeshwari_chalisa_significance = """॥ श्री विन्ध्येश्वरी चालीसा का आध्यात्मिक महत्त्व व फलश्रुति ॥

१. जाग्रत शक्तिपीठ माँ विन्ध्यवासिनी का साक्षात् आशीर्वाद:
विन्ध्याचल धाम भारत का एकमात्र ऐसा सिद्ध पीठ है जहाँ देवी के तीनों स्वरूप—माँ विन्ध्यवासिनी (महालक्ष्मी), माँ महाकाली (कालीखोह) और माँ अष्टभुजा (महासरस्वती)—एक ही त्रिकोण में साक्षात् विराजमान हैं। चालीसा पाठ से तीनों महाशक्तियों का संयुक्त आशीर्वाद प्राप्त होता है।

२. अपार ऋण (कर्ज) से तत्काल मुक्ति:
'जो नर कहं ऋण होय अपारा। सो नर पाठ करै शत बारा॥ निश्चय ऋण मोचन होई जाई॥'
आर्थिक संकट और भारी कर्ज से दबे मनुष्यों के लिए विन्ध्येश्वरी चालीसा अचूक संजीवनी समान है। १०० बार पाठ करने से आय के नए मार्ग खुलते हैं और ऋण समाप्त होता है।

३. कारागार व मुकदमों के बंधनों से मुक्ति:
'जो नर अति बन्दी महं होई। बार हजार पाठ कर सोई॥ निश्चय बन्दी ते छुटि जाई॥'
झूठे मुकदमों, कारावास अथवा विकट बंधनों में फंसे भक्तों को यह चालीसा अभय और शीघ्र रिहाई दिलाती है।

४. असाध्य रोगों व अकाल मृत्यु से रक्षा:
'जाको व्याधि सतावै भाई। जाप करत सब दूरि पराई॥ आयु रक्शिणी विन्ध्यवासिनी॥'
माँ विन्ध्यवासिनी आयु की रक्षिणी हैं। इनकी कृपा से गंभीर बीमारियां, ऊपरी दोष और भय दूर होकर उत्तम स्वास्थ्य प्राप्त होता है।

५. संतान प्राप्ति एवं दरिद्रता का नाश:
'यह श्री विन्ध्याचल चालीसा। रंक पढ़त होवे अवनीसा॥'
संतानहीन दंपत्तियों को गुणवान पुत्र रत्न की प्राप्ति होती है और निर्धन मनुष्य भी राजा (अवनीश) के समान ऐश्वर्य और प्रतिष्ठा प्राप्त करता है।"""

# 5. English Transliteration (रोमन लिप्यंतरण)
vindhyeshwari_chalisa_en = """॥ Shri Vindhyeshwari Chalisa ॥

॥ Doha ॥
Namo Namo Vindhyeshvari, Namo Namo Jagadamba।
Santajanona Ke Kaja Mein, Maan Karati Nahin Vilamba॥

॥ Chaupai ॥
Jai Jai Jai Vindhyachala Rani। Aadi Shakti Jaga Vidita Bhavani॥
Sinhavahini Jai Jaga Mata। Jai Jai Jai Tribhuvana Sukhadatha॥

Kashta Nivarini Jai Jaga Devi। Jai Jai Jai Jai Asurasura Sevi॥
Mahima Amita Apara Tumhari। Shesha Sahasa Mukha Varnata Hari॥

Dinana Ke Dukha Harata Bhavani। Nahin Dekhyo Tuma Sama Koi Dani॥
Saba Kara Manasa Puravata Mata। Mahima Amita Jagata Vikhyata॥

Jo Jana Dhyana Tumharo Lavai। So Turatahi Vanchhita Phala Pavai॥
Tu Hi Vaishnavi Tu Hi Rudrani। Tu Hi Sharada Aru Brahmani॥

Rama Radhika Shama Kali। Tu Hi Mata Santana Pratipali॥
Uma Madhavi Chandi Jvala। Begi Mohi Para Hohu Dayala॥

Tu Hi Hingalaja Maharani। Tu Hi Shitala Aru Vigyani॥
Durga Durgavinashini Mata। Tu Hi Lakshmi Jaga Sukhadatha॥

Tu Hi Jahnavi Aru Utrani। Hemavati Ambe Nirvani॥
Ashtabhuji Varahini Devi। Karata Vishnu Shiva Jakara Sevi॥

Chaunsatthi Devi Kalyani। Gauri Mangala Saba Guna Khani॥
Patana Mumba Danta Kumari। Bhadrakali Suna Vinaya Hamari॥

Vajradharini Shoka Nashini। Aayu Rakshini Vindhyavasini॥
Jaya Aura Vijaya Baitali। Matu Sugandha Aru Vikarali॥

Nama Ananta Tumhara Bhavani। Barnain Kimi Manusha Agyani॥
Ja Para Kripa Matu Tava Hoi। To Vaha Karai Chahai Mana Joi॥

Kripa Karahu Mo Para Maharani। Siddhi Kariya Ambe Mama Bani॥
Jo Nara Dharai Matu Kara Dhyana। Takara Sada Hoya Kalyana॥

Vipatti Tahi Sapanehu Nahin Aavai। Jo Devi Kara Japa Karavai॥
Jo Nara Kahan Rina Hoya Apara। So Nara Patha Karai Shata Bara॥

Nishchaya Rina Mochana Hoi Jai। Jo Nara Patha Karai Mana Lai॥
Astuti Jo Nara Padhe Padhave। Ya Jaga Mein So Bahu Sukha Pavai॥

Jako Vyadhi Satave Bhai। Japa Karata Saba Duri Parai॥
Jo Nara Ati Bandi Mahan Hoi। Bara Hajara Patha Kara Soi॥

Nishchaya Bandi Te Chhuti Jai। Satya Vachana Mama Manahu Bhai॥
Ja Para Jo Kuchha Sankata Hoi। Nishchaya Debihi Sumirai Soi॥

Jo Nara Putra Hoya Nahin Bhai। So Nara Ya Vidhi Kare Upai॥
Pancha Varsha So Patha Karavai। Nauratara Mein Vipra Jimavai॥

Nishchaya Hoya Prasanna Bhavani। Putra Dehi Takahan Guna Khani॥
Dhvaja Nariyala Aani Chadhave। Vidhi Sameta Pujana Karavave॥

Nita Prati Patha Karai Mana Lai। Prema Sahita Nahin Aana Upai॥
Yaha Shri Vindhyachala Chalisa। Ranka Padhata Hove Avanisa॥

Yaha Jani Acharaja Manahu Bhai। Kripa Drishti Tapara Hoi Jai॥
Jai Jai Jai Jagamatu Bhavani। Kripa Karahu Mo Para Jana Jani॥

॥ Doha ॥
Riddhi Siddhi Saba Sampada, Dehu Mata Varadana।
Vindhyavasini Sharana Mein, Rakhahu Nija Kalyana॥"""

# 6. Update drik_chalisa_collections.json
with open('drik_chalisa_collections.json', encoding='utf-8') as f:
    chalisa_data = json.load(f)

durga_items = chalisa_data['durga']['items']
target_item = None
for item in durga_items:
    if item['id'] == 'drik_chalisa_32':
        target_item = item
        break

if target_item:
    target_item['title'] = 'विन्धेश्वरी माता चालीसा'
    target_item['title_en'] = 'Vindhyeshwari Mata Chalisa'
    target_item['en_line'] = 'Jai Jai Jai Vindhyachala Rani'
    target_item['hi_line'] = 'जय जय जय विन्ध्याचल रानी'
    target_item['sub'] = 'जय जय जय विन्ध्याचल रानी • Drik Panchang Verified'
    target_item['thumb'] = 'assets/deity_durga_hd.jpg'
    target_item['audio_url'] = 'https://www.youtube.com/watch?v=5uWstz8m3Rw'
    target_item['video_id'] = '5uWstz8m3Rw'
    target_item['drik_url'] = 'https://www.drikpanchang.com/lyrics/chalisa/vindhyeshwari-mata/vindhyeshwari-mata-chalisa.html?lang=hi&ck=1'
    target_item['source'] = 'Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)'
    target_item['content'] = vindhyeshwari_chalisa_content
    target_item['meaning'] = vindhyeshwari_chalisa_meaning
    target_item['vidhi'] = vindhyeshwari_chalisa_vidhi
    target_item['significance'] = vindhyeshwari_chalisa_significance
    target_item['english_lyrics'] = vindhyeshwari_chalisa_en
    print("Updated drik_chalisa_32 in drik_chalisa_collections.json!")
else:
    print("ERROR: drik_chalisa_32 not found in durga items!")

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

# Add or replace chalisa_vindhyeshwari in CONTENT in app.js
c_vindhyeshwari_record = f"""chalisa_vindhyeshwari: {{
    title: 'विन्धेश्वरी माता चालीसा',
    deity: 'माँ विन्ध्यवासिनी (विन्ध्याचल रानी)',
    mantra: '॥ ॐ विन्ध्यवासिन्यै नमः • जय विन्ध्याचल रानी ॥',
    text: `{vindhyeshwari_chalisa_content}`,
    meaning: `{vindhyeshwari_chalisa_meaning}`,
    vidhi: `{vindhyeshwari_chalisa_vidhi}`,
    significance: `{vindhyeshwari_chalisa_significance}`,
    english_lyrics: `{vindhyeshwari_chalisa_en}`,
    audio_url: 'https://www.youtube.com/watch?v=5uWstz8m3Rw',
    video_id: '5uWstz8m3Rw',
    thumb: 'assets/deity_durga_hd.jpg',
    drik_url: 'https://www.drikpanchang.com/lyrics/chalisa/vindhyeshwari-mata/vindhyeshwari-mata-chalisa.html?lang=hi&ck=1'
  }},
  """

if 'chalisa_vindhyeshwari:' in app_js:
    pos_v = app_js.find('chalisa_vindhyeshwari:')
    pos_next = app_js.find('chalisa_ram:', pos_v)
    if pos_next != -1:
        app_js = app_js[:pos_v] + c_vindhyeshwari_record + app_js[pos_next:]
        print("Replaced existing chalisa_vindhyeshwari in CONTENT!")
    else:
        print("Notice: could not find next item after chalisa_vindhyeshwari")
else:
    pos_target = app_js.find('chalisa_ram:')
    if pos_target != -1:
        app_js = app_js[:pos_target] + c_vindhyeshwari_record + app_js[pos_target:]
        print("Inserted chalisa_vindhyeshwari before chalisa_ram in CONTENT!")
    else:
        print("ERROR: chalisa_ram not found in CONTENT!")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("Saved app.js successfully!")

# 8. Update chalisa_engine.js
try:
    with open('chalisa_engine.js', encoding='utf-8') as f:
        c_engine = f.read()
    idx_start_e = c_engine.find(marker)
    if idx_start_e != -1:
        idx_end_e = c_engine.find(';\n\n// 1. Render Chalisa Card HTML', idx_start_e)
        if idx_end_e != -1:
            c_engine = c_engine[:idx_start_e + len(marker)] + json.dumps(chalisa_data, ensure_ascii=False, indent=2) + c_engine[idx_end_e:]
            with open('chalisa_engine.js', 'w', encoding='utf-8') as f:
                f.write(c_engine)
            print("Synced chalisa_engine.js successfully!")
except Exception as e:
    print("Notice on chalisa_engine.js:", e)
