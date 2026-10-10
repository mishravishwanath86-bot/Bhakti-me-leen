import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Authentic Devanagari Lyrics from Drik Panchang
gopala_chalisa_content = """॥ श्री गोपाल चालीसा ॥
(आनन्दकन्द भगवान श्री कृष्ण / बाल गोपाल • भाषा: ब्रजभाषा / अवधी)

॥ दोहा ॥
श्री राधापद कमल रज, सिर धरि यमुना कूल।
वरणो चालीसा सरस, सकल सुमंगल मूल॥

॥ चौपाई ॥
जय जय पूरण ब्रह्म बिहारी। दुष्ट दलन लीला अवतारी॥
जो कोई तुम्हरी लीला गावै। बिन श्रम सकल पदारथ पावै॥

श्री वसुदेव देवकी माता। प्रकट भये संग हलधर भ्राता॥
मथुरा सों प्रभु गोकुल आये। नन्द भवन में बजत बधाये॥

जो विष देन पूतना आई। सो मुक्ति दै धाम पठाई॥
तृणावर्त राक्षस संहार्यौ। पग बढ़ाय सकटासुर मार्यौ॥

खेल खेल में माटी खाई। मुख में सब जग दियो दिखाई॥
गोपिन घर घर माखन खायो। जसुमति बाल केलि सुख पायो॥

ऊखल सों निज अंग बँधाई। यमलार्जुन जड़ योनि छुड़ाई॥
बका असुर की चोंच विदारी। विकट अघासुर दियो सँहारी॥

ब्रह्मा बालक वत्स चुराये। मोहन को मोहन हित आये॥
बाल वत्स सब बने मुरारी। ब्रह्मा विनय करी तब भारी॥

काली नाग नाथि भगवाना। दावानल को कीन्हों पाना॥
सखन संग खेलत सुख पायो। श्रीदामा निज कन्ध चढ़ायो॥

चीर हरन करि सीख सिखाई। नख पर गिरवर लियो उठाई॥
दरश यज्ञ पत्निन को दीन्हों। राधा प्रेम सुधा सुख लीन्हों॥

नन्दहिं वरुण लोक सों लाये। ग्वालन को निज लोक दिखाये॥
शरद चन्द्र लखि वेणु बजाई। अति सुख दीन्हों रास रचाई॥

अजगर सों पितु चरण छुड़ायो। शंखचूड़ को मूड़ गिरायो॥
हने अरिष्टा सुर अरु केशी। व्योमासुर मार्यो छल वेषी॥

व्याकुल ब्रज तजि मथुरा आये। मारि कंस यदुवंश बसाये॥
मात पिता की बन्दि छुड़ाई। सान्दीपनि गृह विद्या पाई॥

पुनि पठयौ ब्रज ऊधौ ज्ञानी। प्रेम देखि सुधि सकल भुलानी॥
कीन्हीं कुबरी सुन्दर नारी। हरि लाये रुक्मिणि सुकुमारी॥

भौमासुर हनि भक्त छुड़ाये। सुरन जीति सुरतरु महि लाये॥
दन्तवक्र शिशुपाल संहारे। खग मृग नृग अरु बधिक उधारे॥

दीन सुदामा धनपति कीन्हों। पारथ रथ सारथि यश लीन्हों॥
गीता ज्ञान सिखावन हारे। अर्जुन मोह मिटावन हारे॥

केला भक्त बिदुर घर पायो। युद्ध महाभारत रचवायो॥
द्रुपद सुता को चीर बढ़ायो। गर्भ परीक्षित जरत बचायो॥

कच्छ मच्छ वाराह अहीशा। बावन कल्की बुद्धि मुनीशा॥
ह्वै नृसिंह प्रह्लाद उबार्यो। राम रुप धरि रावण मार्यो॥

जय मधु कैटभ दैत्य हनैया। अम्बरीय प्रिय चक्र धरैया॥
ब्याध अजामिल दीन्हें तारी। शबरी अरु गणिका सी नारी॥

गरुड़ासन गज फन्द निकन्दन। देहु दरश ध्रुव नयनानन्दन॥
देहु शुद्ध सन्तन कर सङ्गा। बाढ़ै प्रेम भक्ति रस रङ्गा॥

देहु दिव्य वृन्दावन बासा। छूटै मृग तृष्णा जग आशा॥
तुम्हरो ध्यान धरत शिव नारद। शुक सनकादिक ब्रह्म विशारद॥

जय जय राधारमण कृपाला। हरण सकल संकट भ्रम जाला॥
बिनसैं बिघन रोग दुःख भारी। जो सुमरैं जगपति गिरधारी॥
जो सत बार पढ़ै चालीसा। देहि सकल बाँछित फल शीशा॥

॥ छन्द ॥
गोपाल चालीसा पढ़ै नित, नेम सों चित्त लावई।
सो दिव्य तन धरि अन्त महँ, गोलोक धाम सिधावई॥
संसार सुख सम्पत्ति सकल, जो भक्तजन सन महँ चहैं।
'जयरामदेव' सदैव सो, गुरुदेव दाया सों लहैं॥

॥ दोहा ॥
प्रणत पाल अशरण शरण, करुणा-सिन्धु ब्रजेश।
चालीसा के संग मोहि, अपनावहु प्राणेश॥"""

# 2. Verse-by-verse Spiritual Meaning (पद्यवार पावन भावार्थ)
gopala_chalisa_meaning = """॥ श्री गोपाल चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【आरम्भिक दोहा】
श्री राधापद कमल रज, सिर धरि यमुना कूल।
वरणो चालीसा सरस, सकल सुमंगल मूल॥
भावार्थ: यमुना जी के पावन तट पर श्री किशोरी जी (श्री राधा रानी) के चरण कमलों की पावन रज को अपने मस्तक पर धारण करके, मैं समस्त मंगलों की मूल कारण इस परम सरस 'गोपाल चालीसा' का भक्तिपूर्वक वर्णन करता हूँ।

【चौपाइयां — भावार्थ】
१. जय जय पूरण ब्रह्म बिहारी। दुष्ट दलन लीला अवतारी॥
जो कोई तुम्हरी लीला गावै। बिन श्रम सकल पदारथ पावै॥
भावार्थ: साक्षात् सच्चिदानंद पूर्णब्रह्म, वृंदावन बिहारी भगवान श्री कृष्ण की जय हो, जय हो! आप दुष्टों का दलन करने वाले और भक्तों के उद्धार हेतु दिव्य लीलाएं रचने वाले अवतारी हैं। जो भी प्राणी आपकी पावन लीलाओं का गान करता है, वह बिना किसी कठिन परिश्रम के चारों पदार्थों (धर्म, अर्थ, काम और मोक्ष) को सहज ही प्राप्त कर लेता है।

२. श्री वसुदेव देवकी माता। प्रकट भये संग हलधर भ्राता॥
मथुरा सों प्रभु गोकुल आये। नन्द भवन में बजत बधाये॥
भावार्थ: माता देवकी और पिता वासुदेव के घर आप अपने अग्रज श्री बलराम (हलधर) जी सहित कारागार में प्रकट हुए। फिर मथुरा से गोकुल पधारे, जहाँ नंदबाबा के पावन भवन में आनंदपूर्वक बधाइयां बजीं और उत्सव मनाया गया।

३. जो विष देन पूतना आई। सो मुक्ति दै धाम पठाई॥
तृणावर्त राक्षस संहार्यौ। पग बढ़ाय सकटासुर मार्यौ॥
भावार्थ: जो पूतना राक्षसी स्तन में कालकूट विष लगाकर मारने आई थी, दयानिधान गोपाल ने उसे भी माता की गति देकर अपने परम धाम भेज दिया। बवंडर बनकर आए तृणावर्त दैत्य का संहार किया और खेल-खेल में पैर की ठोकर मारकर भारी शकटासुर का वध किया।

४. खेल खेल में माटी खाई। मुख में सब जग दियो दिखाई॥
गोपिन घर घर माखन खायो। जसुमति बाल केलि सुख पायो॥
भावार्थ: खेल-खेल में जब कन्हैया ने मिट्टी खाई, तब माता यशोदा के मुख खुलवाने पर आपने अपने छोटे से मुख में संपूर्ण त्रिलोकी और चराचर ब्रह्मांड के साक्षात् दर्शन करा दिए। गोपियों के घर-घर जाकर प्रेम का माखन खाया और माता यशोदा को अनुपम बाल-लीलाओं का असीम सुख प्रदान किया।

५. ऊखल सों निज अंग बँधाई। यमलार्जुन जड़ योनि छुड़ाई॥
बका असुर की चोंच विदारी। विकट अघासुर दियो सँहारी॥
भावार्थ: माता यशोदा के हाथों ओखल से बंधकर भी आपने कुबेर-पुत्र नलकूबर और मणिग्रीव को यमलार्जुन वृक्ष की जड़ योनि से मुक्त कर उनका उद्धार किया। बगुले का रूप धरकर आए बकासुर की चोंच चीर दी और विकराल अघासुर के पेट में प्रवेश कर उसका वध किया।

६. ब्रह्मा बालक वत्स चुराये। मोहन को मोहन हित आये॥
बाल वत्स सब बने मुरारी। ब्रह्मा विनय करी तब भारी॥
भावार्थ: जब ब्रह्मा जी ने परीक्षा लेने हेतु सभी ग्वालबालों और बछड़ों को चुरा लिया, तब स्वयं मोहन ने ही समस्त बछड़े और ग्वालबाल बनकर एक वर्ष तक लीला रची। जब ब्रह्मा जी ने लौटकर देखा, तो वे चकित रह गए और हाथ जोड़कर भगवान की भारी स्तुति की।

७. काली नाग नाथि भगवाना। दावानल को कीन्हों पाना॥
सखन संग खेलत सुख पायो। श्रीदामा निज कन्ध चढ़ायो॥
भावार्थ: यमुना के विषैले दह में उतरकर कालिया नाग के फनों पर नृत्य करते हुए उसे नाथ लिया और यमुना जल को अमृत बना दिया। वन में लगी भयंकर दावाग्नि का पान कर ब्रजवासियों की रक्षा की। सखाओं के संग खेलकर आनंद पाया और खेल में हारने पर सखा श्रीदामा को अपने कंधे पर बैठाया।

८. चीर हरन करि सीख सिखाई। नख पर गिरवर लियो उठाई॥
दरश यज्ञ पत्निन को दीन्हों। राधा प्रेम सुधा सुख लीन्हों॥
भावार्थ: गोपियों का चीर हरण करके उन्हें अहंता और लोक-लज्जा त्यागकर अनन्य समर्पण का मर्म सिखाया। इंद्र के कोप से ब्रज को बचाने हेतु गोवर्धन पर्वत को अपनी कनिष्ठा अंगुली के नख पर उठा लिया। अभिमानी ब्राह्मणों की यज्ञपत्नियों को अपने साक्षात् दर्शन दिए और श्री राधा जी के पावन प्रेमामृत का दिव्य सुख आस्वादन किया।

९. नन्दहिं वरुण लोक सों लाये। ग्वालन को निज लोक दिखाये॥
शरद चन्द्र लखि वेणु बजाई। अति सुख दीन्हों रास रचाई॥
भावार्थ: वरुण देव के लोक से नंदबाबा को ससम्मान वापस लाए और समस्त ग्वालबालों को अपने दिव्य वैकुंठ धाम का दर्शन कराया। शरद पूर्णिमा की धवल चांदनी में वंशी बजाकर गोपियों संग महारास रचाया और उन्हें परमानंद प्रदान किया।

१०. अजगर सों पितु चरण छुड़ायो। शंखचूड़ को मूड़ गिरायो॥
हने अरिष्टा सुर अरु केशी। व्योमासुर मार्यो छल वेषी॥
भावार्थ: नंदीश्वर पर आक्रमण करने वाले अजगर से पिता नंद के चरण छुड़ाकर उस सुदर्शन विद्याधर को मुक्ति दी। शंखचूड़ का शीश काटकर मणि प्राप्त की। अरिष्टासुर (बैल), केशी (घोड़ा) और छली व्योमासुर का संहार किया।

११. व्याकुल ब्रज तजि मथुरा आये। मारि कंस यदुवंश बसाये॥
मात पिता की बन्दि छुड़ाई। सान्दीपनि गृह विद्या पाई॥
भावार्थ: समस्त ब्रजवासियों को विरह में छोड़कर मथुरा पधारे, अत्याचारी कंस को पछाड़कर मारा और यदुवंशियों को पुनः प्रतिष्ठित किया। माता देवकी और पिता वासुदेव को कारागार के बंधनों से मुक्त कराया तथा गुरु सांदीपनि के आश्रम में जाकर समस्त चौंसठ कलाओं और वेदों की विद्या प्राप्त की।

१२. पुनि पठयौ ब्रज ऊधौ ज्ञानी। प्रेम देखि सुधि सकल भुलानी॥
कीन्हीं कुबरी सुन्दर नारी। हरि लाये रुक्मिणि सुकुमारी॥
भावार्थ: ज्ञानी उद्धव को ब्रज भेजा, जहाँ गोपियों का अलौकिक प्रेम देखकर उद्धव अपना सारा निर्गुण ज्ञान भूल गए। कुब्जा के अंग को सीधा कर उसे परम सुंदरी नारी बनाया और शिशुपाल आदि को परास्त कर सुकुमारी रुक्मिणी जी का हरण कर विवाह किया।

१३. भौमासुर हनि भक्त छुड़ाये। सुरन जीति सुरतरु महि लाये॥
दन्तवक्र शिशुपाल संहारे। खग मृग नृग अरु बधिक उधारे॥
भावार्थ: भौमासुर (नरकासुर) का वध कर १६,१०० बंदी कन्याओं को मुक्त कराकर उन्हें सम्मान दिलाया। देवराज इंद्र को परास्त कर स्वर्ग से कल्पवृक्ष (पारिजात) लाकर पृथ्वी पर स्थापित किया। दंतवक्र और शिशुपाल का वध किया तथा राजा नृग, पशु-पक्षियों और बहेलिए तक का उद्धार किया।

१४. दीन सुदामा धनपति कीन्हों। पारथ रथ सारथि यश लीन्हों॥
गीता ज्ञान सिखावन हारे। अर्जुन मोह मिटावन हारे॥
भावार्थ: अपने दरिद्र बालसखा सुदामा के प्रेम से लाए तीन मुट्ठी कच्चे चावल आरोग कर उन्हें कुबेर के समान धनपति बना दिया। महाभारत में अर्जुन (पार्थ) के सारथी बनकर यश प्राप्त किया और कुरुक्षेत्र में श्रीमद्भगवद्गीता का अमर ज्ञान देकर अर्जुन का मोह व विषाद नष्ट किया।

१५. केला भक्त बिदुर घर पायो। युद्ध महाभारत रचवायो॥
द्रुपद सुता को चीर बढ़ायो। गर्भ परीक्षित जरत बचायो॥
भावार्थ: भक्त विदुर जी के घर प्रेम के वशीभूत होकर केले के छिलके खाए और धर्म की स्थापना हेतु महाभारत युद्ध की रचना की। भरी सभा में द्रौपदी की लाज बचाने हेतु चीर (वस्त्र) बढ़ाया और अश्वत्थामा के ब्रह्मास्त्र से माता उत्तरा के गर्भ में जलते हुए परीक्षित की रक्षा की।

१६. कच्छ मच्छ वाराह अहीशा। बावन कल्की बुद्धि मुनीशा॥
ह्वै नृसिंह प्रह्लाद उबार्यो। राम रुप धरि रावण मार्यो॥
भावार्थ: कच्छप, मत्स्य, वराह, वामन, कल्कि, बुद्ध आदि रूपों में आप ही अवतरित हुए। नृसिंह बनकर भक्त प्रह्लाद की रक्षा की और मर्यादा पुरुषोत्तम श्री राम का रूप धारण करके अहंकारी रावण का संहार किया।

१७. जय मधु कैटभ दैत्य हनैया। अम्बरीय प्रिय चक्र धरैया॥
ब्याध अजामिल दीन्हें तारी। शबरी अरु गणिका सी नारी॥
भावार्थ: मधु-कैटभ दैत्यों का संहार करने वाले, भक्त अंबरीष की रक्षा हेतु सुदर्शन चक्र धारण करने वाले प्रभु! आपने बहेलिए, पापी अजामिल, भीलनी शबरी और गणिका जैसी पतित आत्माओं का भी उद्धार कर दिया।

१८. गरुड़ासन गज फन्द निकन्दन। देहु दरश ध्रुव नयनानन्दन॥
देहु शुद्ध सन्तन कर सङ्गा। बाढ़ै प्रेम भक्ति रस रङ्गा॥
भावार्थ: गरुड़ पर सवार होकर ग्राह के चंगुल से गजराज को छुड़ाने वाले और बालक ध्रुव को दर्शन देकर कृतार्थ करने वाले हे नयनानंद! हमें शुद्ध संतों का सत्संग प्रदान कीजिए, जिससे हमारे हृदय में आपकी प्रेमाभक्ति का रंग बढ़ता रहे।

१९. देहु दिव्य वृन्दावन बासा। छूटै मृग तृष्णा जग आशा॥
तुम्हरो ध्यान धरत शिव नारद। शुक सनकादिक ब्रह्म विशारद॥
भावार्थ: हे गोपाल! हमें अपने दिव्य वृंदावन धाम में नित्य वास प्रदान कीजिए, जिससे संसार की झूठी मृगतृष्णाएं और आशाएं छूट जाएं। देवाधिदेव भगवान शिव, देवर्षि नारद, शुकदेव जी और सनकादिक ब्रह्मवेत्ता मुनिजन निरंतर आपके पावन स्वरूप का ध्यान धरते हैं।

२०. जय जय राधारमण कृपाला। हरण सकल संकट भ्रम जाला॥
बिनसैं बिघन रोग दुःख भारी। जो सुमरैं जगपति गिरधारी॥
जो सत बार पढ़ै चालीसा। देहि सकल बाँछित फल शीशा॥
भावार्थ: हे राधारमण कृपालु प्रभु! आपकी जय हो, जय हो। आप भक्तों के समस्त संकटों और सांसारिक भ्रम-जाल को हरने वाले हैं। जो भी मनुष्य जगत्पति गिरिधारी का स्मरण करता है, उसके भारी से भारी विघ्न, असाध्य रोग और दुःख स्वतः नष्ट हो जाते हैं। जो साधक इस चालीसा का सौ बार पाठ करता है, गोपाल जी उसके शीश पर हाथ रखकर समस्त मनोवांछित फल प्रदान करते हैं।

【छन्द】
गोपाल चालीसा पढ़ै नित, नेम सों चित्त लावई।
सो दिव्य तन धरि अन्त महँ, गोलोक धाम सिधावई॥
संसार सुख सम्पत्ति सकल, जो भक्तजन सन महँ चहैं।
'जयरामदेव' सदैव सो, गुरुदेव दाया सों लहैं॥
भावार्थ: जो साधक नित्य नियमपूर्वक एकाग्रचित्त होकर इस गोपाल चालीसा का पाठ करता है, वह अंत समय में दिव्य देह धारण करके साक्षात् परम धाम 'गोलोक धाम' को गमन करता है। भक्तजन संसार में जो भी सुख और संपत्ति की कामना करते हैं, वे गुरुदेव और भगवान गोपाल की कृपा से सब कुछ सहज ही प्राप्त कर लेते हैं।

【समापन दोहा】
प्रणत पाल अशरण शरण, करुणा-सिन्धु ब्रजेश।
चालीसा के संग मोहि, अपनावहु प्राणेश॥
भावार्थ: हे शरणागतवत्सल! हे निराश्रितों के एकमात्र आश्रय! हे करुणा के अगाध सागर ब्रजराज! इस चालीसा के पावन पाठ के साथ हे प्राणेश्वर! मुझे भी अपने श्रीचरणों में सदा के लिए अपना लीजिए।"""

# 3. Authentic Vidhi & Rules (शास्त्रोक्त पाठ विधि व नियम)
gopala_chalisa_vidhi = """॥ श्री गोपाल चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का समय व दिशा:
- प्रातःकाल ब्रह्ममुहूर्त अथवा सांध्यकाल गोधूलि बेला में पूर्व अथवा उत्तर दिशा की ओर मुख करके बैठना सर्वश्रेष्ठ है।
- गुरुवार, शुक्रवार, प्रत्येक माह की एकादशी, पूर्णिमा तथा श्री कृष्ण जन्माष्टमी पर पाठ करने से अनंत गुना फल प्राप्त होता है।

२. लड्डू गोपाल सेवा व पंचामृत अभिषेक:
- यदि घर में लड्डू गोपाल जी का विग्रह हो, तो उन्हें शुद्ध जल, कच्चे दूध, गंगाजल व पंचामृत (दूध, दही, घी, शहद, शक्कर) से स्नान कराएं।
- सुंदर नवीन पीले वस्त्र, मुकुट, मोरपंख, मुरली और कमरबंद से श्रृंगार करें।

३. प्रिय नैवेद्य व तुलसी दल (अनिवार्य):
- ताजा मक्खन (माखन), मिश्री, पेड़ा, पंचमेवा अथवा मौसमी फलों का भोग लगाएं।
- तुलसी दल अनिवार्य रूप से भोग में रखें (बिना तुलसी दल के बाल गोपाल भोग स्वीकार नहीं करते)।
- गोपीचंदन अथवा अष्टगंध का तिलक लगाएं।

४. दीपक व सुगंधित धूप:
- शुद्ध देशी गाय के घी का दीपक प्रज्वलित करें।
- चंदन, कर्पूर अथवा गुग्गुल की सुगंधित धूप अर्पित करें।

५. पाठ की संख्या व संकल्प:
- सामान्य दैनिक साधना: नित्य १, ३ या ७ पाठ।
- संतान गोपाल कामना (संतान प्राप्ति), गृह क्लेश निवारण अथवा गोलोक धाम प्राप्ति हेतु: ४० दिनों तक प्रतिदिन ११ पाठ अथवा एक बैठक में २१/१०० पाठ करने का संकल्प लें।
- पाठ के आरम्भ और अंत में 'ॐ क्लीं कृष्णाय गोविंदाय गोपीजनवल्लभाय स्वाहा' अथवा 'ॐ श्री गोपालाय नमः' महामंत्र का एक माला (१०८ बार) जप अवश्य करें।"""

# 4. Significance & Phalasruti (आध्यात्मिक माहात्म्य व फलश्रुति)
gopala_chalisa_significance = """॥ श्री गोपाल चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. 'अन्त महँ गोलोक धाम सिधावई' — परम मोक्ष व गोलोक धाम वास:
गोपाल चालीसा की सबसे महान फलश्रुति यह है कि जो भी साधक इसका नित्य पाठ करता है, वह सांसारिक बंधनों और चौरासी लाख योनियों से मुक्त होकर अंत समय में दिव्य देह धारण कर सीधे भगवान के नित्य धाम 'गोलोक धाम' को प्राप्त होता है।

२. संतान गोपाल वरदान (संतान सुख):
संतानहीन दंपत्तियों के लिए यह चालीसा कल्पवृक्ष के समान है। शुद्ध भाव से इसका पाठ करने से भगवान बाल गोपाल के रूप में तेजस्वी, दीर्घायु और आज्ञाकारी संतान का आशीर्वाद प्रदान करते हैं।

३. 'बिनसैं बिघन रोग दुःख भारी' — समस्त व्याधियों व विघ्नों का शमन:
साधक के जीवन में आने वाली गंभीर बाधाएं, असाध्य शारीरिक-मानसिक रोग, दरिद्रता और भय गोपाल जी के सुदर्शन चक्र के प्रभाव से भस्म हो जाते हैं।

४. प्रेम-भक्ति व अलौकिक शांति:
संसार की झूठी मृगतृष्णाओं से मुक्ति मिलकर साधक के हृदय में श्री राधा-माधव के चरणों में अनन्य प्रेमाभक्ति और असीम आनंद का संचार होता है।

५. द्रिक पञ्चाङ्ग प्रमाणिकता:
यह चालीसा द्रिक पञ्चाङ्ग (Drik Panchang Verified) के मूल प्रामाणिक छंदों पर पूर्णतः आधारित है।"""

# 5. English Transliteration (रोमन लिपि)
gopala_chalisa_en = """॥ Shri Gopala Chalisa ॥
(Dedicated to Lord Gopala • Awadhi/Brajbhasha)

॥ Doha ॥
Shri Raadhaapada Kamala Raja, Sira Dhari Yamunaa Koola।
Varano Chaaleesaa Sarasa, Sakala Sumangala Moola॥

॥ Chaupai ॥
Jaya Jaya Poorana Brahma Bihaaree। Dushta Dalana Leelaa Avataaree॥
Jo Ko-ee Tumharee Leelaa Gaavai। Bina Shrama Sakala Padaaratha Paavai॥

Shri Vasudeva Devakee Maataa। Prakata Bhaye Sanga Haladhara Bhraataa॥
Mathuraa Son Prabhu Gokula Aaye। Nanda Bhavana Men Bajata Badhaaye॥

Jo Visha Dena Pootanaa Aa-ee। So Mukti Dai Dhaama Pathaa-ee॥
Trinaavarta Raakshasa Samhaaryau। Paga Badhaaya Sakataasura Maaryau॥

Khela Khela Men Maatee Khaa-ee। Mukha Men Saba Jaga Diyo Dikhaa-ee॥
Gopin Ghara Ghara Maakhana Khaayo। Jasumati Baala Keli Sukha Paayo॥

Ookhala Son Nija Anga Bandhaa-ee। Yamalaarjuna Jada Yoni Chhudhaa-ee॥
Bakaa Asura Kee Choncha Vidaaree। Vikata Aghaasura Diyo Samhaaree॥

Brahmaa Baalaka Vatsa Churaaye। Mohana Ko Mohana Hita Aaye॥
Baala Vatsa Saba Bane Muraaree। Brahmaa Vinaya Karee Taba Bhaaree॥

Kaalee Naaga Naathi Bhagavaanaa। Daavaanala Ko Keenhon Paanaa॥
Sakhana Sanga Khelata Sukha Paayo। Shreedaamaa Nija Kandha Chadhaayo॥

Cheera Harana Kari Seekha Sikhaa-ee। Nakha Para Giravara Liyo Uthaa-ee॥
Darasha Yagya Patnina Ko Deenhon। Raadhaa Prema Sudhaa Sukha Leenhon॥

Nandahin Varuna Loka Son Laaye। Gwaalana Ko Nija Loka Dikhaaye॥
Sharada Chandra Lakhi Venu Bajaa-ee। Ati Sukha Deenhon Raasa Rachaa-ee॥

Ajagara Son Pitu Charana Chhudhaayo। Shankhachooda Ko Mooda Giraayo॥
Hane Arishtaa Sura Aru Keshee। Vyomaasura Maaryo Chhala Veshee॥

Vyaakula Braja Taji Mathuraa Aaye। Maari Kamsa Yaduwamsha Basaaye॥
Maata Pitaa Kee Bandi Chhudhaa-ee। Saandeepani Griha Vidyaa Paa-ee॥

Puni Pathayau Braja Oodhau Gyaanee। Prema Dekhi Sudhi Sakala Bhulaanee॥
Keenheen Kubaree Sundara Naaree। Hari Laaye Rukmini Sukumaaree॥

Bhaumaasura Hani Bhakta Chhudhaaye। Surana Jeeti Surataru Mahi Laaye॥
Dantavakra Shishupaala Samhaare। Khaga Mriga Nriga Aru Badhika Udhaare॥

Deena Sudaamaa Dhanapati Keenhon। Paaratha Ratha Saarathi Yasha Leenhon॥
Geetaa Gyaana Sikhaavana Haare। Arjuna Moha Mitaavana Haare॥

Kelaa Bhakta Bidura Ghara Paayo। Yuddha Mahaabhaarata Rachavaayo॥
Drupada Sutaa Ko Cheera Badhaayo। Garbha Pareekshita Jarata Bachaayo॥

Kachchha Machchha Vaaraaha Aheeshaa। Baavana Kalkee Buddhi Muneeshaa॥
Hvai Nrisimha Prahlaada Ubaaryo। Raama Roopa Dhari Raavana Maaryo॥

Jaya Madhu Kaitabha Daitya Hanaiyaa। Ambareeya Priya Chakra Dharaiyaa॥
Byaadha Ajaamila Deenhen Taaree। Shabaree Aru Ganikaa See Naaree॥

Garudaasana Gaja Fanda Nikandana। Dehu Darasha Dhruva Nayanaanandana॥
Dehu Shuddha Santana Kara Sangaa। Baadhai Prema Bhakti Rasa Rangaa॥

Dehu Divya Vrindaavana Baasaa। Chhoothai Mriga Trishnaa Jaga Aashaa॥
Tumharo Dhyaana Dharata Shiva Naarada। Shuka Sanakaadika Brahma Vishaarada॥

Jaya Jaya Raadhaaramana Kripaalaa। Harana Sakala Sankata Bhrama Jaalaa॥
Binasain Bighana Roga Dukha Bhaaree। Jo Sumarain Jagapati Giridhaaree॥
Jo Sata Baara Padhai Chaaleesaa। Dehi Sakala Baanchhita Phala Sheeshaa॥

॥ Chhand ॥
Gopaala Chaaleesaa Padhai Nita, Nema Son Chitta Laava-ee।
So Divya Tana Dhari Anta Mahan, Goloka Dhaama Sidhaava-ee॥
Samsaara Sukha Sampatti Sakala, Jo Bhaktajana Sana Mahan Chahain।
'Jayaraamadeva' Sadaiva So, Gurudeva Daayaa Son Lahain॥

॥ Doha ॥
Pranata Paala Asharana Sharana, Karunaa-Sindhu Brajesha।
Chaaleesaa Ke Sanga Mohi, Apanaavahu Praanesha॥"""

# 6. Update drik_chalisa_collections.json
with open('drik_chalisa_collections.json', encoding='utf-8') as f:
    chalisa_data = json.load(f)

for it in chalisa_data['krishna']['items']:
    if it['id'] == 'drik_chalisa_8':
        it['title'] = 'भगवान गोपाल चालीसा'
        it['title_en'] = 'Shri Gopala Chalisa (Lord Gopala Chalisa)'
        it['hi_line'] = 'जय जय पूरण ब्रह्म बिहारी'
        it['en_line'] = 'Jai Jai Pooran Brahma Bihari'
        it['sub'] = 'आनन्दकन्द बाल गोपाल चालीसा • Drik Panchang Verified'
        it['thumb'] = 'assets/gallery/bal_krishna.jpg'
        it['video_id'] = 'gUIUKPRBjwk'
        it['audio_url'] = 'https://www.youtube.com/watch?v=gUIUKPRBjwk'
        it['drik_url'] = 'https://www.drikpanchang.com/lyrics/chalisa/lord-gopala/shri-gopala-chalisa.html?lang=hi&ck=1'
        it['source'] = 'Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)'
        it['content'] = gopala_chalisa_content
        it['meaning'] = gopala_chalisa_meaning
        it['vidhi'] = gopala_chalisa_vidhi
        it['significance'] = gopala_chalisa_significance
        it['english_lyrics'] = gopala_chalisa_en
        print("Updated drik_chalisa_8 in drik_chalisa_collections.json!")
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

# Add or update chalisa_gopal in CONTENT in app.js
c_gopal_record = f"""chalisa_gopal: {{
    title: 'भगवान गोपाल चालीसा',
    deity: 'आनन्दकन्द भगवान श्री कृष्ण / बाल गोपाल',
    mantra: '॥ ॐ क्लीं कृष्णाय गोविंदाय गोपीजनवल्लभाय स्वाहा ॥',
    text: `{gopala_chalisa_content}`,
    meaning: `{gopala_chalisa_meaning}`,
    vidhi: `{gopala_chalisa_vidhi}`,
    significance: `{gopala_chalisa_significance}`,
    english_lyrics: `{gopala_chalisa_en}`,
    audio_url: 'https://www.youtube.com/watch?v=gUIUKPRBjwk',
    video_id: 'gUIUKPRBjwk',
    thumb: 'assets/gallery/bal_krishna.jpg',
    drik_url: 'https://www.drikpanchang.com/lyrics/chalisa/lord-gopala/shri-gopala-chalisa.html?lang=hi&ck=1'
  }},
  """

if 'chalisa_gopal:' in app_js:
    pos_g = app_js.find('chalisa_gopal:')
    pos_g_end = app_js.find('chalisa_', pos_g + 20)
    app_js = app_js[:pos_g] + c_gopal_record + app_js[pos_g_end:]
    print("Replaced existing chalisa_gopal in CONTENT!")
else:
    # Insert right before chalisa_krishna:
    pos_k = app_js.find('chalisa_krishna:')
    if pos_k != -1:
        app_js = app_js[:pos_k] + c_gopal_record + app_js[pos_k:]
        print("Inserted chalisa_gopal before chalisa_krishna in CONTENT!")
    else:
        print("Warning: chalisa_krishna not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Saved app.js successfully!")
