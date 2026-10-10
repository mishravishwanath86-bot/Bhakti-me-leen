import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री तुलसी माता चालीसा ॥

॥ दोहा ॥
जय जय तुलसी भगवती, सत्यवती सुखदानी।
नमो नमो हरि प्रेयसी, श्री वृन्दा गुन खानी॥
श्री हरि शीश बिरजिनी, देहु अमर वर अम्ब।
जनहित हे वृन्दावनी, अब न करहु विलम्ब॥

॥ चौपाई ॥
धन्य धन्य श्री तुलसी माता। महिमा अगम सदा श्रुति गाता॥१॥
हरि के प्राणहु से तुम प्यारी। हरीहीँ हेतु कीन्हो तप भारी॥२॥
जब प्रसन्न है दर्शन दीन्ह्यो। तब कर जोरी विनय उस कीन्ह्यो॥३॥
हे भगवन्त कन्त मम होहू। दीन जानी जनि छाडाहू छोहु॥४॥
सुनी लक्ष्मी तुलसी की बानी। दीन्हो श्राप कध पर आनी॥५॥
उस अयोग्य वर मांगन हारी। होहू विटप तुम जड़ तनु धारी॥६॥
सुनी तुलसी हीँ श्रप्यो तेहिं ठामा। करहु वास तुहू नीचन धामा॥७॥
दियो वचन हरि तब तत्काला। सुनहु सुमुखी जनि होहू बिहाला॥८॥
समय पाई व्हौ रौ पाती तोरा। पुजिहौ आस वचन सत मोरा॥९॥
तब गोकुल मह गोप सुदामा। तासु भई तुलसी तू बामा॥१०॥
कृष्ण रास लीला के माही। राधे शक्यो प्रेम लखी नाही॥११॥
दियो श्राप तुलसिह तत्काला। नर लोकही तुम जन्महु बाला॥१२॥
यो गोप वह दानव राजा। शङ्ख चुड नामक शिर ताजा॥१३॥
तुलसी भई तासु की नारी। परम सती गुण रूप अगारी॥१४॥
अस द्वै कल्प बीत जब गयऊ। कल्प तृतीय जन्म तब भयऊ॥१५॥
वृन्दा नाम भयो तुलसी को। असुर जलन्धर नाम पति को॥१६॥
करि अति द्वन्द अतुल बलधामा। लीन्हा शंकर से संग्राम॥१७॥
जब निज सैन्य सहित शिव हारे। मरही न तब हर हरिही पुकारे॥१८॥
पतिव्रता वृन्दा थी नारी। कोऊ न सके पतिहि संहारी॥१९॥
तब जलन्धर ही भेष बनाई। वृन्दा ढिग हरि पहुच्यो जाई॥२०॥
शिव हित लही करि कपट प्रसंगा। कियो सतीत्व धर्म तोही भंगा॥२१॥
भयो जलन्धर कर संहारा। सुनी उर शोक उपारा॥२२॥
तिही क्षण दियो कपट हरि टारी। लखी वृन्दा दुःख गिरा उचारी॥२३॥
जलन्धर जस हत्यो अभीता। सोई रावन तस हरिही सीता॥२४॥
अस प्रस्तर सम हृदय तुम्हारा। धर्म खण्डी मम पतिहि संहारा॥२५॥
यही कारण लही श्राप हमारा। होवे तनु पाषाण तुम्हारा॥२६॥
सुनी हरि तुरतहि वचन उचारे। दियो श्राप बिना विचारे॥२७॥
लख्यो न निज करतूती पति को। छलन चह्यो जब पारवती को॥२८॥
जड़मति तुहु अस हो जड़रूपा। जग मह तुलसी विटप अनूपा॥२९॥
धग्व रूप हम शालिग्रामा। नदी गण्डकी बीच ललामा॥३०॥
जो तुलसी दल हमही चढ़ इहैं। सब सुख भोगी परम पद पईहै॥३१॥
बिनु तुलसी हरि जलत शरीरा। अतिशय उठत शीश उर पीरा॥३२॥
जो तुलसी दल हरि शिर धारत। सो सहस्र घट अमृत डारत॥३३॥
तुलसी हरि मन रञ्जनी हारी। रोग दोष दुःख भंजनी हारी॥३४॥
प्रेम सहित हरि भजन निरन्तर। तुलसी राधा में नाही अन्तर॥३५॥
व्यन्जन हो छप्पनहु प्रकारा। बिनु तुलसी दल न हरीहि प्यारा॥३६॥
सकल तीर्थ तुलसी तरु छाही। लहत मुक्ति जन संशय नाही॥३७॥
कवि सुन्दर इक हरि गुण गावत। तुलसिहि निकट सहसगुण पावत॥३८॥
बसत निकट दुर्बासा धामा। जो प्रयास ते पूर्व ललामा॥३९॥
पाठ करहि जो नित नर नारी। होही सुख भाषहि त्रिपुरारी॥४०॥

॥ दोहा ॥
तुलसी चालीसा पढ़ही, तुलसी तरु ग्रह धारी।
दीपदान करि पुत्र फल, पावही बन्ध्यहु नारी॥
सकल दुःख दरिद्र हरि, हार ह्वै परम प्रसन्न।
आशिय धन जन लड़हि, ग्रह बसही पूर्णा अत्र॥
लाही अभिमत फल जगत, मह लाही पूर्ण सब काम।
जेई दल अर्पही तुलसी तंह, सहस बसही हरीराम॥
तुलसी महिमा नाम लख, तुलसी सूत सुखराम।
मानस चालीस रच्यो, जग महं तुलसीदास॥"""

meaning = """॥ श्री तुलसी माता चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "जय जय तुलसी भगवती, सत्यवती सुखदानी। नमो नमो हरि प्रेयसी, श्री वृन्दा गुन खानी॥"
भावार्थ: हे सुख प्रदान करने वाली, सत्यव्रती भगवती तुलसी! आपकी सदा-सदा जय हो। हे भगवान श्री हरि विष्णु की परम प्रिया और समस्त दिव्य सद्गुणों की खान माँ वृन्दा! आपको मेरा बारम्बार सादर नमन है।
• "श्री हरि शीश बिरजिनी, देहु अमर वर अम्ब। जनहित हे वृन्दावनी, अब न करहु विलम्ब॥"
भावार्थ: हे साक्षात् भगवान श्री हरि के मस्तक पर विराजने वाली जगन्माता! मुझे अमर भक्ति का वरदान दीजिए। हे समस्त जीवों का कल्याण करने वाली वृन्दावनी माता! अब कृपा करने में तनिक भी विलंब मत कीजिए।

【४० चौपाइयां — पद्यवार भावार्थ】
१-४. "धन्य धन्य श्री तुलसी माता... दीन जानी जनि छाडाहू छोहु॥"
भावार्थ: हे श्री तुलसी माता! आप धन्य हैं, धन्य हैं; वेद और श्रुतियां सदा आपकी अगम्य व अलौकिक महिमा का गान करती हैं। आप भगवान श्री हरि को अपने प्राणों से भी अधिक प्रिय हैं; आपने भगवान विष्णु को पति रूप में पाने हेतु जन्म-जन्मांतरों तक घोर तपस्या की। जब भगवान ने प्रसन्न होकर आपको दिव्य दर्शन दिए, तब आपने हाथ जोड़कर विनम्र प्रार्थना की कि "हे भगवन! आप मेरे स्वामी (पति) बनिए; मुझे दीन जानकर अपने प्रेम और कृपा से कभी वंचित मत कीजिएगा।"

५-८. "सुनी लक्ष्मी तुलसी की बानी... सुनहु सुमुखी जनि होहू बिहाला॥"
भावार्थ: तुलसी की इस अभिलाषा को सुनकर माता लक्ष्मी ने कुपित होकर श्राप दिया कि "हे अयोग्य वर मांगने वाली! तू पृथ्वी पर जाकर जड़ वनस्पति (वृक्ष/पौधा) का रूप धारण कर।" तब तुलसी ने भी आवेश में आकर लक्ष्मी जी को श्राप दिया कि "तू भी पृथ्वी पर नीच स्थानों में वास कर।" यह देखकर भगवान श्री हरि ने तत्काल वचन दिया कि "हे सुमुखी तुलसी! तुम तनिक भी व्याकुल मत होओ, समय आने पर मैं स्वयं तुम्हारा पति बनकर तुम्हारी मनोकामना पूर्ण करूँगा; मेरा यह वचन त्रिकाल सत्य है।"

९-१४. "समय पाई व्हौ रौ पाती तोरा... परम सती गुण रूप अगारी॥"
भावार्थ: समय पाकर गोकुल में गोप सुदामा प्रकट हुए और तुलसी उनकी धर्मपत्नी बनीं। श्रीकृष्ण की महारास लीला में राधारानी ने तुलसी के अनन्य प्रेम की परीक्षा में क्रोधवश श्राप दिया कि तुम मृत्युलोक में मानवी कन्या रूप में जन्म लो। वही गोप सुदामा पृथ्वी पर दानवों के अधिपति शंखचूड़ बने और तुलसी उनकी परम सती, रूपवती और पतिव्रता पत्नी बनीं।

१५-१८. "अस द्वै कल्प बीत जब गयऊ... मरही न तब हर हरिही पुकारे॥"
भावार्थ: इस प्रकार जब दो कल्प बीत गए, तब तीसरे कल्प में तुलसी का जन्म 'वृन्दा' नाम से हुआ और उनका विवाह महाबली असुर जलंधर के साथ हुआ। जलंधर ने अतुलित बल पाकर देवाधिदेव महादेव शिव से भयंकर युद्ध छेड़ दिया। जब शिवजी की सेना के सामने भी जलंधर का वध नहीं हो पा रहा था, तब महादेव ने भगवान विष्णु को पुकारा कि यह असुर किसी भी प्रकार से परास्त नहीं हो रहा है।

१९-२२. "पतिव्रता वृन्दा थी नारी... सुनी उर शोक उपारा॥"
भावार्थ: वृन्दा का पतिव्रता धर्म इतना प्रचंड था कि जब तक उसका सतीत्व अखंड था, तब तक त्रिलोकी में कोई भी जलंधर का वध नहीं कर सकता था। तब भगवान शिव और देवताओं के हित के लिए श्री हरि विष्णु ने जलंधर का छद्म भेष बनाया और वृन्दा के समक्ष पहुंचे। पति समझकर वृन्दा का पातिव्रत्य नियम खंडित होते ही रणभूमि में शिवजी के त्रिशूल से जलंधर का संहार हो गया। पति की मृत्यु का समाचार सुनकर वृन्दा के हृदय में अपार शोक उमड़ पड़ा।

२३-२६. "तिही क्षण दियो कपट हरि टारी... होवे तनु पाषाण तुम्हारा॥"
भावार्थ: उसी क्षण भगवान विष्णु ने अपना कपट भेष त्यागकर चतुर्भुज रूप प्रकट किया। वृन्दा ने अत्यंत दुखी होकर कहा कि "हे प्रभु! जैसे आपने निर्भय होकर मेरे पति का छल से संहार कराया है, त्रेतायुग में उसी प्रकार आपकी भार्या सीता का भी रावण द्वारा हरण होगा। आपका हृदय पत्थर के समान कठोर है, जिसने मेरे धर्म को खंडित कर मेरे पति का वध कराया; इसी कारण मैं आपको श्राप देती हूँ कि आपका शरीर पाषाण (पत्थर) बन जाए!"

२७-३०. "सुनी हरि तुरतहि वचन उचारे... नदी गण्डकी बीच ललामा॥"
भावार्थ: भगवान विष्णु ने शांत भाव से कहा कि "हे देवी! तुमने बिना विचारे श्राप दिया, क्योंकि तुमने अपने पति जलंधर की दुष्टता नहीं देखी जिसने साक्षात् माता पार्वती को छलने का प्रयास किया था। तथापि तुम्हारी पतिव्रता निष्ठा अमर रहे, इसलिए तुम संसार में पावन 'तुलसी' पौधे का अनुपम रूप धारण करोगी। और मैं तुम्हारे श्राप को शिरोधार्य कर नेपाल की पवित्र गण्डकी नदी के गर्भ में 'शालिग्राम शिला' के रूप में सदा निवास करूँगा।"

३१-३४. "जो तुलसी दल हमही चढ़ इहैं... रोग दोष दुःख भंजनी हारी॥"
भावार्थ: भगवान ने वरदान दिया कि जो भक्त मुझ शालिग्राम पर तुलसी दल अर्पित करेगा, वह समस्त सांसारिक सुख भोगकर अंत में परम पद (वैकुंठ) प्राप्त करेगा। तुलसी दल के बिना मेरा शरीर ताप से जलता रहता है और शीश व हृदय में भारी पीड़ा होती है। जो भक्त तुलसी दल मेरे मस्तक पर धारण कराता है, वह मानो मुझ पर सहस्र घड़ों का शीतल अमृत ढालता है। माँ तुलसी भगवान हरि के मन को आनंदित करने वाली और भक्तों के समस्त रोगों, दोषों व दुखों का भंजन करने वाली हैं।

३५-३८. "प्रेम सहित हरि भजन निरन्तर... तुलसिहि निकट सहसगुण पावत॥"
भावार्थ: जो प्रेमपूर्वक निरंतर हरि नाम का भजन करता है, उसके लिए तुलसी और राधारानी में कोई अंतर नहीं है। चाहे भगवान के सम्मुख छप्पन प्रकार के स्वादिष्ट व्यंजन क्यों न परोसे जाएं, जब तक उसमें तुलसी दल न हो, भगवान श्री हरि उसे कभी स्वीकार नहीं करते। समस्त तीर्थ माँ तुलसी के पौधे की शीतल छाया में नित्य निवास करते हैं; जो भी इनका आश्रय लेता है, वह निःसंदेह मोक्ष पाता है। कवि जन तुलसी जी के सान्निध्य में सहस्र गुना पुण्य फल प्राप्त करते हैं।

३९-४०. "बसत निकट दुर्बासा धामा... होही सुख भाषहि त्रिपुरारी॥"
भावार्थ: प्रयागराज के पूर्व तट पर महर्षि दुर्वासा के आश्रम के समीप भी तुलसी माता की असीम महिमा है। जो भी नर-नारी नित्य इस पावन तुलसी चालीसा का पाठ करते हैं, देवाधिदेव त्रिपुरारी शिव के वचनानुसार उनके जीवन में समस्त सुख, शांति और आनंद की वर्षा होती है।

【समापन दोहे व फलश्रुति】
• "तुलसी चालीसा पढ़ही, तुलसी तरु ग्रह धारी... जग महं तुलसीदास॥"
भावार्थ: जो भी मनुष्य अपने घर में तुलसी का पौधा लगाकर नित्य इस चालीसा का पाठ करता है और सांध्यकाल में दीपदान करता है, बाँझ स्त्री भी गुणवान पुत्र रत्न प्राप्त करती है। श्री हरि उसके समस्त दुःख और दरिद्रता को हर लेते हैं और उसका घर धन-धान्य व अन्नपूर्णा की कृपा से भर जाता है। संसार में सभी मनोवांछित फल प्राप्त होते हैं और जहाँ तुलसी दल अर्पित होता है, वहाँ सहस्रों रूपों में साक्षात् भगवान श्री हरि राम निवास करते हैं।"""

vidhi = """॥ श्री तुलसी माता चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन दिन:
- नित्य प्रातःकाल: सूर्योदय के समय स्नान के उपरांत तुलसी जी को जल अर्पित करते हुए पाठ करना सर्वश्रेष्ठ है।
- सांध्यकाल (गोधूलि वेला): सूर्यास्त के समय तुलसी चौरे में घी का दीपक प्रज्वलित कर पाठ करने से घर में स्थिर लक्ष्मी का वास होता है।
- पावन तिथियां: देवउठनी एकादशी (तुलसी विवाह पर्व), कार्तिक मास के संपूर्ण ३० दिन, प्रत्येक मास की एकादशी व पूर्णिमा, तथा शुक्रवार।

२. तुलसी पत्र तोड़ने के अनिवार्य नियम (शास्त्रीय निषेध):
- रविवार (रविवासर), एकादशी, द्वादशी, सूर्य ग्रहण, चंद्र ग्रहण, संक्रांति और सूर्यास्त के बाद तुलसी के पत्ते कभी नहीं तोड़ने चाहिए।
- बिना स्नान किए अथवा अशुद्ध अवस्था में तुलसी का स्पर्श वर्जित है।
- तुलसी पत्र को कभी नाखून से नहीं तोड़ना चाहिए; हाथ जोड़कर 'ॐ सुभद्रायै नमः' अथवा आज्ञा मन्त्र बोलकर कोमलता से पत्र चुनना चाहिए।

३. पूजन सामग्री व दीपदान:
- जल अर्पण: तांबे के लोटे में शुद्ध जल, थोड़ा कच्चा दूध, अक्षत और रोली मिलाकर तुलसी की जड़ में अर्पित करें (रविवार को जल नहीं चढ़ाया जाता)।
- दीपक: गाय के शुद्ध देशी घी अथवा तिल के तेल का एकमुखी दीपक प्रज्वलित करें।
- श्रृंगार व भोग: तुलसी जी को लाल चुनरी, सिंदूर, हल्दी, कुमकुम और चंदन अर्पित करें। भोग में मिश्री, बताशे, मखाने अथवा मौसमी फल चढ़ाएं।

४. तुलसी प्रदक्षिणा (परिक्रमा):
- जल व धूप-दीप अर्पित करने के उपरांत तुलसी के पौधे की ३, ७ अथवा ११ बार परिक्रमा करें।
- परिक्रमा करते समय यह मन्त्र बोलें:
  'यानि कानि च पापानि ब्रह्महत्यादिकानि च।
   तानि तानि प्रणश्यन्ति प्रदक्षिण पदे पदे॥'

५. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन व पवित्रीकरण करें।
- भगवान शालिग्राम व तुलसी महारानी का ध्यान करें:
  'ॐ तुलस्यै नमः' अथवा 'ॐ नमो भगवते वासुदेवाय' का ११ बार जप करें।
- इसके उपरांत पूर्ण श्रद्धापूर्वक श्री तुलसी माता चालीसा का १, ३, ७ अथवा ११ बार पाठ करें।
- पाठ के उपरांत तुलसी जी की आरती गाएं और तुलसी जी की चरण-रज (मिट्टी) का मस्तक पर तिलक लगाएं।"""

significance = """॥ श्री तुलसी माता चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. साक्षात् वैकुंठ धाम की प्राप्ति — शालिग्राम व तुलसी का नित्य सान्निध्य:
"धग्व रूप हम शालिग्रामा। नदी गण्डकी बीच ललामा॥"
पद्म पुराण और स्कंद पुराण के अनुसार जिस घर में शालिग्राम और तुलसी का नित्य पूजन होता है, वह घर साक्षात् वैकुंठ के समान तीर्थ बन जाता है। वहाँ यमराज के दूत कभी प्रवेश नहीं कर सकते।

२. छप्पन भोग की स्वीकृति का एकमात्र आधार:
"व्यन्जन हो छप्पनहु प्रकारा। बिनु तुलसी दल न हरीहि प्यारा॥"
भगवान विष्णु, बालकृष्ण और श्रीराम बिना तुलसी दल के कोई भी भोग, नैवेद्य या जल स्वीकार नहीं करते। तुलसी चालीसा के पाठ से साधक द्वारा की गई पूजा को भगवान कोटि गुना स्वीकार करते हैं।

३. वास्तु दोष व नकारात्मक ऊर्जा का समूल नाश:
घर के ईशान कोण (उत्तर-पूर्व) या पूर्व दिशा में तुलसी का पौधा स्थापित कर चालीसा पाठ करने से घर का भारी से भारी वास्तु दोष, नजर दोष, और नकारात्मक शक्तियां स्वतः नष्ट हो जाती हैं।

४. पुत्र-संतान प्राप्ति एवं अखण्ड सौभाग्य:
"दीपदान करि पुत्र फल, पावही बन्ध्यहु नारी॥"
कार्तिक मास में तुलसी जी के सम्मुख दीपदान करने और नित्य चालीसा पाठ करने से संतानहीन दंपत्तियों को दीर्घायु व संस्कारी संतान प्राप्त होती है तथा सुहागिनों का सुहाग अखण्ड रहता है।

५. आयुर्वेद व प्राण-ऊर्जा की संजीवनी:
तुलसी का पौधा चौबीसों घंटे ऑक्सीजन और सकारात्मक प्राण-ऊर्जा उत्सर्जित करता है। इसके दर्शन, स्पर्श, जल सेवन और परिक्रमा से श्वास रोग, हृदय रोग, रक्त विकार और मानसिक तनाव दूर होते हैं।

६. दरिद्रता का नाश एवं अन्न-धन की अखंडता:
"सकल दुःख दरिद्र हरि, हार ह्वै परम प्रसन्न। आशिय धन जन लड़हि, ग्रह बसही पूर्णा अत्र॥"
चालीसा के पाठ से माँ अन्नपूर्णा और महालक्ष्मी की कृपा से घर में कभी धन, वस्त्र और अन्न की कमी नहीं होती।"""

english_lyrics = """॥ Shri Tulasi Mata Chalisa ॥

॥ Doha ॥
Jaya Jaya Tulasee Bhagavatee, Satyavatee Sukhadaanee।
Namo Namo Hari Preyasee, Shree Vrindaa Guna Khaanee॥
Shree Hari Sheesha Birajinee, Dehu Amara Vara Amba।
Janahita He Vrindaavanee, Aba Na Karahu Vilamba॥

॥ Chaupai ॥
Dhanya Dhanya Shree Tulasee Maataa। Mahimaa Agama Sadaa Shruti Gaataa॥1॥
Hari Ke Praanahu Se Tuma Pyaaree। Hareeheen Hetu Keenho Tapa Bhaaree॥2॥
Jaba Prasanna Hvaidarshana Deenhyo। Taba Kara Joree Vinaya Usa Keenhyo॥3॥
He Bhagavanta Kanta Mama Hohoo। Deena Jaanee Jani Chhaadaahoo Chhohoo॥4॥
Sunee Lakshmi Tulasee Kee Baanee। Deenho Shraapa Krodha Para Aanee॥5॥
Usa Ayogya Vara Maangana Haaree। Hohoo Vitapa Tuma Jada Tanu Dhaaree॥6॥
Sunee Tulasee Heen Shrapyo Tehin Thaamaa। Karahu Vaasa Tuhoo Neechana Dhaamaa॥7॥
Diyo Vachana Hari Taba Tatkaalaa। Sunahu Sumukhee Jani Hohoo Bihaalaa॥8॥
Samaya Paa-ee Vhau Rau Paatee Toraa। Pujihoi Aasa Vachana Sata Moraa॥9॥
Taba Gokula Maha Gopa Sudaamaa। Taasu Bha-ee Tulasee Too Baamaa॥10॥
Krishna Raasa Leelaa Ke Maahee। Raadhe Shakyo Prema Lakhee Naahee॥11॥
Diyo Shraapa Tulasiha Tatkaalaa। Nara Lokahi Tuma Janmahu Baalaa॥12॥
Yo Gopa Vaha Daanava Raajaa। Shankha Chuda Naamaka Shira Taajaa॥13॥
Tulasee Bha-ee Taasu Kee Naaree। Parama Satee Guna Roopa Agaaree॥14॥
Asa Dvai Kalpa Beeta Jaba Gaya-oo। Kalpa Triteeya Janma Taba Bhaya-oo॥15॥
Vrindaa Naama Bhayo Tulasee Ko। Asura Jalandhara Naama Pati Ko॥16॥
Kari Ati Dvanda Atula Baladhaamaa। Leenhaa Shankara Se Sangraama॥17॥
Jaba Nija Sainya Sahita Shiva Haare। Marahee Na Taba Hara Harihee Pukaare॥18॥
Pativrataa Vrindaa Thee Naaree। Ko-oo Na Sake Patihi Sanhaaree॥19॥
Taba Jalandhara Hee Bhesha Banaa-ee। Vrindaa Dhiga Hari Pahuchyo Jaa-ee॥20॥
Shiva Hita Lahee Kari Kapata Prasangaa। Kiyo Sateetva Dharma Tohi Bhangaa॥21॥
Bhayo Jalandhara Kara Sanhaaraa। Sunee Ura Shoka Upaaraa॥22॥
Tihee Kshana Diyo Kapata Hari Taaree। Lakhee Vrindaa Dukha Giraa Uchaaree॥23॥
Jalandhara Jasa Hatyo Abheetaa। So-ee Raavana Tasa Harihee Seetaa॥24॥
Asa Prastara Sama Hridaya Tumhaaraa। Dharma Khandee Mama Patihi Sanhaaraa॥25॥
Yahee Kaarana Lahee Shraapa Hamaaraa। Hove Tanu Paashaana Tumhaaraa॥26॥
Sunee Hari Turatahi Vachana Uchaare। Diyo Shraapa Binaa Vichaare॥27॥
Lakhyo Na Nija Karatootee Pati Ko। Chhalana Chahyo Jaba Paaravatee Ko॥28॥
Jadamati Tuhu Asa Ho Jdaroopaa। Jaga Maha Tulasee Vitapa Anoopaa॥29॥
Dhagva Roopa Hama Shaaligraamaa। Nadee Gandakee Beecha Lalaamaa॥30॥
Jo Tulasee Dala Hamahee Chadha Ihain। Saba Sukha Bhogee Parama Pada Pa-eehai॥31॥
Binu Tulasee Hari Jalata Shareeraa। Atishaya Uthata Sheesha Ura Peeraa॥32॥
Jo Tulasee Dala Hari Shira Dhaarata। So Sahasra Ghata Amrita Daarata॥33॥
Tulasee Hari Mana Ranjanee Haaree। Roga Dosha Dukha Bhanjanee Haaree॥34॥
Prema Sahita Hari Bhajana Nirantara। Tulasee Raadhaa Men Naahee Antara॥35॥
Vyanjana Ho Chhappanahu Prakaaraa। Binu Tulasee Dala Na Hareehi Pyaaraa॥36॥
Sakala Teertha Tulasee Taru Chhaahee। Lahata Mukti Jana Sanshaya Naahee॥37॥
Kavi Sundara Ika Hari Guna Gaavata। Tulasihi Nikata Sahasaguna Paavata॥38॥
Basata Nikata Durbaasaa Dhaamaa। Jo Prayaasa Te Poorva Lalaamaa॥39॥
Paatha Karahi Jo Nita Nara Naaree। Hohee Sukha Bhaashahi Tripuraaree॥40॥

॥ Doha ॥
Tulasee Chaaleesaa Padhahi, Tulasee Taru Graha Dhaaree।
Deepadaana Kari Putra Phala, Paavahi Bandhyahu Naaree॥
Sakala Dukha Daridra Hari, Haara Hvai Parama Prasanna।
Aashiya Dhana Jana Ladahi, Graha Basahi Poornaa Atra॥
Laahee Abhimata Phala Jagata, Maha Laahee Poorna Saba Kaama।
Je-ee Dala Arpahi Tulasee Tanh, Sahasa Basahi Hareeraama॥
Tulasee Mahimaa Naama Lakha, Tulasee Soota Sukharaama।
Maanasa Chaaleesa Rachyo, Jaga Mahan Tulaseedaasa॥"""

# 1. Update drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["gayatri"]["items"]:
    if item["id"] == "drik_chalisa_30":
        item["title"] = "तुलसी माता चालीसा"
        item["title_en"] = "Shri Tulasi Mata Chalisa"
        item["en_line"] = "Jai Jai Tulasi Bhagavati Satyavati"
        item["hi_line"] = "जय जय तुलसी भगवती सत्यवती"
        item["sub"] = "जय जय तुलसी भगवती सत्यवती • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_tulsi_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=fmtYx-Ff6YQ"
        item["video_id"] = "fmtYx-Ff6YQ"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/tulasi-mata/tulasi-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "वेदमाता गायत्री व माँ तुलसी भगवती"
        item["section"] = "माँ गायत्री व तुलसी चालीसा"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_30 in drik_chalisa_collections.json successfully!")

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

# 3. Add chalisa_tulsi in CONTENT in app.js
content_obj = {
    "title": "तुलसी माता चालीसा",
    "title_en": "Shri Tulasi Mata Chalisa",
    "en_line": "Jai Jai Tulasi Bhagavati Satyavati",
    "hi_line": "जय जय तुलसी भगवती सत्यवती",
    "sub": "जय जय तुलसी भगवती सत्यवती • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_tulsi_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=fmtYx-Ff6YQ",
    "video_id": "fmtYx-Ff6YQ",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/tulasi-mata/tulasi-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "वेदमाता गायत्री व माँ तुलसी भगवती",
    "section": "माँ गायत्री व तुलसी चालीसा",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

tulsi_content_js = "  chalisa_tulsi: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_tulsi: {" in app_text:
    m_start = app_text.find("  chalisa_tulsi: {")
    m_end = app_text.find("\n  chalisa_", m_start + 1)
    if m_end == -1:
        m_end = app_text.find("\n  sundarkand:", m_start + 1)
    if m_end != -1:
        app_text = app_text[:m_start] + tulsi_content_js + app_text[m_end+1:]
        print("Replaced existing chalisa_tulsi in CONTENT!")
else:
    # Insert right after chalisa_gayatri
    g_pos = app_text.find("  chalisa_gayatri: {")
    if g_pos != -1:
        g_end = app_text.find("\n  chalisa_", g_pos + 1)
        if g_end == -1:
            g_end = app_text.find("\n  sundarkand:", g_pos + 1)
        if g_end != -1:
            app_text = app_text[:g_end+1] + tulsi_content_js + app_text[g_end+1:]
            print("Inserted chalisa_tulsi after chalisa_gayatri in CONTENT!")
    else:
        v_pos = app_text.find("  chalisa_vishwakarma: {")
        if v_pos != -1:
            app_text = app_text[:v_pos] + tulsi_content_js + app_text[v_pos:]
            print("Inserted chalisa_tulsi before chalisa_vishwakarma in CONTENT!")

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
