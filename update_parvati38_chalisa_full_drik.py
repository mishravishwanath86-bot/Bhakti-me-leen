import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री पार्वती माता चालीसा ॥

॥ दोहा ॥
जय गिरी तनये दक्षजे, शम्भु प्रिये गुणखानि।
गणपति जननी पार्वती, अम्बे! शक्ति! भवानि॥

॥ चौपाई ॥
ब्रह्मा भेद न तुम्हरो पावे। पंच बदन नित तुमको ध्यावे॥१॥
षड्मुख कहि न सकत यश तेरो। सहसबदन श्रम करत घनेरो॥२॥
तेऊ पार न पावत माता। स्थित रक्षा लय हित सजाता॥३॥
अधर प्रवाल सदृश अरुणारे। अति कमनीय नयन कजरारे॥४॥
ललित ललाट विलेपित केशर। कुंकुम अक्षत शोभा मनहर॥५॥
कनक बसन कंचुकी सजाए। कटी मेखला दिव्य लहराए॥६॥
कण्ठ मदार हार की शोभा। जाहि देखि सहजहि मन लोभा॥७॥
बालारुण अनन्त छबि धारी। आभूषण की शोभा प्यारी॥८॥
नाना रत्न जटित सिंहासन। तापर राजति हरि चतुरानन॥९॥
इन्द्रादिक परिवार पूजित। जग मृग नाग यक्ष रव कूजित॥१०॥
गिर कैलास निवासिनी जय जय। कोटिक प्रभा विकासिन जय जय॥११॥
त्रिभुवन सकल कुटुम्ब तिहारी। अणु अणु महं तुम्हारी उजियारी॥१२॥
हैं महेश प्राणेश! तुम्हारे। त्रिभुवन के जो नित रखवारे॥१३॥
उनसो पति तुम प्राप्त कीन्ह जब। सुकृत पुरातन उदित भए तब॥१४॥
बूढ़ा बैल सवारी जिनकी। महिमा का गावे कोउ तिनकी॥१५॥
सदा श्मशान बिहारी शंकर। आभूषण हैं भुजंग भयंकर॥१६॥
कण्ठ हलाहल को छबि छायी। नीलकण्ठ की पदवी पायी॥१७॥
देव मगन के हित अस कीन्हों। विष लै आपु तिनहि अमि दीन्हों॥१८॥
ताकी तुम पत्नी छवि धारिणि। दूरित विदारिणी मंगल कारिणि॥१९॥
देखि परम सौन्दर्य तिहारो। त्रिभुवन चकित बनावन हारो॥२०॥
भय भीता सो माता गंगा। लज्जा मय है सलिल तरंगा॥२१॥
सौत समान शम्भु पहआयी। विष्णु पदाब्ज छोड़ि सो धायी॥२२॥
तेहिकों कमल बदन मुरझायो। लखि सत्वर शिव शीश चढ़ायो॥२३॥
नित्यानन्द करी बरदायिनी। अभय भक्त कर नित अनपायिनी॥२४॥
अखिल पाप त्रयताप निकन्दिनि। माहेश्वरी हिमालय नन्दिनि॥२५॥
काशी पुरी सदा मन भायी। सिद्ध पीठ तेहि आपु बनायी॥२६॥
भगवती प्रतिदिन भिक्षा दात्री। कृपा प्रमोद सनेह विधात्री॥२७॥
रिपुक्षय कारिणि जय जय अम्बे। वाचा सिद्ध करि अवलम्बे॥२८॥
गौरी उमा शंकरी काली। अन्नपूर्णा जग प्रतिपाली॥२९॥
सब जन की ईश्वरी भगवती। पतिप्राणा परमेश्वरी सती॥३०॥
तुमने कठिन तपस्या कीनी। नारद सों जब शिक्षा लीनी॥३१॥
अन्न न नीर न वायु अहारा। अस्थि मात्रतन भयउ तुम्हारा॥३२॥
पत्र घास को खाद्य न भायउ। उमा नाम तब तुमने पायउ॥३३॥
तप बिलोकि रिषि सात पधारे। लगे डिगावन डिगी न हारे॥३४॥
तब तव जय जय जय उच्चारेउ। सप्तरिषि निज गेह सिधारेउ॥३५॥
सुर विधि विष्णु पास तब आए। वर देने के वचन सुनाए॥३६॥
मांगे उमा वर पति तुम तिनसों। चाहत जग त्रिभुवन निधि जिनसों॥३७॥
एवमस्तु कहि ते दोऊ गए। सुफल मनोरथ तुमने लए॥३८॥
करि विवाह शिव सों हे भामा। पुनः कहाई हर की बामा॥३९॥
जो पढ़िहै जन यह चालीसा। धन जन सुख देइहै तेहि ईसा॥४०॥

॥ दोहा ॥
कूट चन्द्रिका सुभग शिर, जयति जयति सुख खानि।
पार्वती निज भक्त हित, रहहु सदा वरदानि॥"""

meaning = """॥ श्री पार्वती माता चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहा】
• "जय गिरी तनये दक्षजे, शम्भु प्रिये गुणखानि। गणपति जननी पार्वती, अम्बे! शक्ति! भवानि॥"
भावार्थ: हे गिरिराज हिमालय की पुत्री (गिरितनये)! हे पूर्वजन्म में प्रजापति दक्ष की कन्या सती (दक्षजे)! हे देवाधिदेव भगवान शिव की परम प्रिया शम्भुप्रिये और समस्त सद्गुणों की अक्षय खान! हे प्रथम पूज्य भगवान श्री गणेश की माता पार्वती, हे जगदम्बा, हे पराशक्ति, हे भवानी! आपकी सदा सर्वदा जय हो।

【चौपाइयां — पद्यवार भावार्थ】
१-१०. "ब्रह्मा भेद न तुम्हरो पावे... जग मृग नाग यक्ष रव कूजित॥"
भावार्थ: स्वयं सृष्टि के रचयिता ब्रह्मदेव भी आपकी अगाध लीलाओं का भेद नहीं पा सकते; पंचमुखी भगवान शिव (पंचबदन) निरंतर आपके दिव्य स्वरूप का ध्यान धरते हैं। षडानन कार्तिकेय (छह मुख वाले) भी आपके संपूर्ण यश का गान करने में असमर्थ हैं; और सहस्र मुख वाले शेषनाग भी आपकी महिमा का वर्णन करते-करते थक जाते हैं। वे सभी भी आपकी पराशक्ति का पार नहीं पा सकते; आप ही इस संपूर्ण विश्व की स्थिति (पालन), रक्षा और प्रलय (लय) की परम अधिष्ठात्री हैं। आपके दोनों अधर मूंगे (प्रवाल) के समान अरुण (लाल) हैं और आपके कजरारे विशाल नयन अत्यंत कमनीय व मनोहारी हैं। आपके सुंदर ललाट पर केसर, कस्तूरी, कुंकुम और अक्षत का तिलक मन को मोह लेने वाला है। आपने स्वर्णिम आभा वाले सुंदर वस्त्र और चोली धारण की हुई है तथा आपकी कमर में बंधी दिव्य करधनी (मेखला) शोभा पा रही है। आपके कंठ में कल्पवृक्ष के मंदार पुष्पों की दिव्य माला सुशोभित है, जिसे देखकर सहज ही मन मुग्ध हो जाता है। आप प्रातःकालीन बाल-सूर्य के समान अनंत कांति से संपन्न हैं और आपके दिव्य आभूषणों की छटा अत्यंत मनमोहक है। आप अनेक प्रकार के दिव्य मणियों और रत्नों से जड़े स्वर्णिम सिंहासन पर विराजमान हैं, जहाँ भगवान श्रीहरि विष्णु और ब्रह्मा जी आपकी वंदना करते हैं। देवराज इन्द्र सहित समस्त देवगण, यक्ष, गंधर्व, मृग और नागगण मधुर ध्वनि में निरंतर आपकी स्तुति करते हैं।

११-२०. "गिर कैलास निवासिनी जय जय... त्रिभुवन चकित बनावन हारो॥"
भावार्थ: पावन कैलास पर्वत पर निवास करने वाली हे माँ! आपकी जय हो, जय हो; करोड़ों सूर्यों के समान दिव्य प्रभा का विस्तार करने वाली देवी, आपकी जय हो। तीनों लोकों के समस्त प्राणी आपका ही विशाल कुटुंब हैं और ब्रह्मांड के कण-कण में आपका ही दिव्य प्रकाश व्याप्त है। तीनों लोकों के नित्य रक्षक देवाधिदेव महादेव शिव आपके प्राणेश्वर (पति) हैं। जब आपके पूर्व जन्मों के संचित महान पुण्यों का उदय हुआ, तब आपको भगवान शिव पति रूप में प्राप्त हुए। जिनकी सवारी बूढ़ा नंदी बैल (वृषभ) है, उन आशुतोष शिव की अनिर्वचनीय महिमा का पार कौन पा सकता है? भगवान शंकर सदा श्मशान में निवास करने वाले हैं और भयानक सर्प (भुजंग) ही जिनके आभूषण हैं। समुद्र मंथन से निकले हलाहल विष को अपने कंठ में धारण करने से उनके कंठ पर नीली कांति छा गई और वे 'नीलकंठ' कहलाए। देवताओं के कल्याण हेतु उन्होंने स्वयं विषपान किया और देवताओं को अमृत प्रदान किया। उन देवाधिदेव महादेव की आप ही परम शोभायमान अर्धांगिनी हैं; आप भक्तों के पापों और कष्टों का विदारण करने वाली और परम मंगल करने वाली हैं। आपके इस अप्रतिम और अलौकिक सौन्दर्य को देखकर तीनों लोक विस्मयचकित रह जाते हैं।

२१-३३. "भय भीता सो माता गंगा... अन्नपूर्णा जग प्रतिपाली॥"
भावार्थ: जब पावन गंगा जी भगवान विष्णु के चरण-कमलों को छोड़कर भगवान शिव की जटाओं में आईं, तो आपके दिव्य तेज को देखकर लज्जा और संकोच से उनके जल की तरंगें विचलित हो उठीं। जब वे शिवजी के समीप आईं, तो उनका मुख लज्जा से मुरझा गया; तब शिवजी ने उन्हें अपनी जटाओं में स्थान देकर सम्मानित किया। आप भक्तों को नित्यानंद प्रदान करने वाली, वरदायिनी, और अपने शरणागत को अभय देने वाली अविनाशिनी शक्ति हैं। आप समस्त पापों और आधि-व्याधि-उपाधि रूपी त्रितापों का नाश करने वाली, माहेश्वरी और हिमालय की नन्दिनी हैं। पावन मोक्षदायिनी काशी नगरी आपके मन को सदा भाती है, जिसे आपने साक्षात सिद्धपीठ बना दिया। वहाँ आप माँ अन्नपूर्णा के रूप में नित्य भगवान विश्वनाथ और समस्त चराचर जगत को भिक्षा (अन्न व कृपा) प्रदान करती हैं। हे अम्बे! आप शत्रुओं का नाश करने वाली हैं; अपनी कृपा के आश्रय से आप साधकों को वाक्-सिद्धि प्रदान करती हैं। आप ही गौरी, उमा, शंकरी, काली, और संपूर्ण विश्व का पालन-पोषण करने वाली जगद्धात्री अन्नपूर्णा हैं। आप समस्त जीवों की परम ईश्वरी, पतिव्रता सती और परमेश्वरी हैं।

३४-४०. "तुमने कठिन तपस्या कीनी... धन जन सुख देइहै तेहि ईसा॥"
भावार्थ: जब देवर्षि नारद जी से आपने शिव-प्राप्ति का उपदेश प्राप्त किया, तब आपने अत्यंत कठोर तपस्या की। आपने अन्न, जल और वायु तक का त्याग कर दिया, जिससे आपका सुकोमल शरीर मात्र अस्थि-पंजर रह गया। जब आपने सूखे पत्ते और घास तक खाना छोड़ दिया (अपर्णा बन गईं), तब माता मैना ने 'उ+मा' (तप मत करो) कहकर पुकारा और आपका नाम 'उमा' पड़ा। आपकी इस अलौकिक तपस्या को देखकर सप्तर्षि आपकी परीक्षा लेने पधारे और उन्होंने आपको शिव-तप से डिगाने का बहुत प्रयास किया, किन्तु आपके दृढ़ संकल्प के आगे वे हार गए। तब सप्तर्षियों ने आपकी मुक्तकंठ से जय-जयकार की और संतुष्ट होकर अपने लोक को सिधारे। तत्पश्चात ब्रह्मा और विष्णु जी आपके सम्मुख पधारे और वरदान मांगने को कहा। आपने वरदान में केवल और केवल देवाधिदेव शिव को पति रूप में मांगा, जिनसे तीनों लोक समस्त निधियों की याचना करते हैं। 'एवमस्तु' कहकर वे दोनों देवता अंतर्ध्यान हो गए और आपका परम मनोरथ सिद्ध हुआ। देवाधिदेव शिव से विवाह कर आप पुनः भगवान शिव की वामांगिनी (वामा/अर्धांगिनी) कहलाईं। जो भी श्रद्धालु इस पावन पार्वती चालीसा का नित्य श्रद्धापूर्वक पाठ करता है, देवाधिदेव भगवान शिव और माँ पार्वती उसे विपुल धन, सुयोग्य परिवार, संतान और समस्त सुख प्रदान करते हैं।

【समापन दोहा】
• "कूट चन्द्रिका सुभग शिर, जयति जयति सुख खानि। पार्वती निज भक्त हित, रहहु सदा वरदानि॥"
भावार्थ: जिनके पावन मस्तक पर सुंदर बाल-चन्द्रमा की अमृतमयी चन्द्रिका सुशोभित है, उन समस्त सुखों की खान माँ पार्वती की सदा-सदा जय हो। हे माँ पार्वती! आप अपने अनन्य भक्तों के कल्याण हेतु सदा वरदायिनी बनकर उन पर अपनी कृपा बनाए रखिए।"""

vidhi = """॥ श्री पार्वती माता चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल सूर्योदय अथवा सांध्यकालीन प्रदोष काल।
- सर्वोत्तम वार: सोमवार (शिव-शक्ति आराधना का विशेष दिन) एवं शुक्रवार।
- महापर्व व पावन तिथियां: हरितालिका तीज, हरियाली तीज, कजरी तीज, करवा चौथ, मंगला गौरी व्रत (सावन के सभी मंगलवार), महाशिवरात्रि, तथा चैत्र व शारदीय नवरात्रि।

२. दिशा, आसन व वस्त्र:
- दिशा: उत्तर अथवा पूर्व दिशा की ओर मुख करके बैठें (उत्तर दिशा शिव-पार्वती का कैलास धाम मानी गई है)।
- आसन: लाल अथवा पीले रंग का स्वच्छ ऊनी आसन बिछाएं।
- वस्त्र: साधक को शुद्ध, धुले हुए लाल, पीले अथवा नारंगी वस्त्र धारण करने चाहिए (श्वेत या काले वस्त्र सुहाग पूजा में वर्जित हैं)।

३. पूजन सामग्री, दीप व नैवेद्य:
- दीपक: गाय के शुद्ध देशी घी का दीपक प्रज्वलित करें।
- प्रिय पुष्प: लाल गुलाब, श्वेत मंदार/आक, कनेर, अथवा कमल के पुष्प।
- सुहाग पिटारी: माँ पार्वती को सोलह श्रृंगार की सामग्री (लाल चुनरी, चूड़ियां, बिंदी, सिन्दूर, मेहंदी, काजल, महावर, दर्पण आदि) अर्पित करें।
- प्रिय नैवेद्य: खीर, मालपुआ, पंचामृत, मौसमी फल, बताशे, और सूखे मेवे।

४. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन, पवित्रीकरण एवं हाथ में जल-अक्षत लेकर संकल्प करें।
- शिव-पार्वती का ध्यान करें:
  'ॐ नमः शिवायै च नमः शिवाय। उमामहेश्वराभ्यां नमः॥
   सर्वमंगलमांगल्ये शिवे सर्वार्थसाधिके। शरण्ये त्र्यम्बके गौरि नारायणि नमोऽस्तु ते॥'
- माँ पार्वती का एकाक्षरी अथवा सौभाग्य मन्त्र: 'ॐ उमामहेश्वराभ्यां नमः' अथवा 'ॐ ह्रीं उमायै नमः' का १०८ बार जप करें।
- इसके पश्चात पूर्ण श्रद्धा एवं एकाग्रता से 'श्री पार्वती चालीसा' का १, ३ अथवा ५ बार पाठ करें।
- पाठ के उपरांत कपूर से आरती करें, माता के चरणों का सिन्दूर अपनी मांग में लगाएं तथा सुहागिनों को सुहाग सामग्री वितरित करें।"""

significance = """॥ श्री पार्वती माता चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. अखण्ड सौभाग्य व पति रक्षा:
"करि विवाह शिव सों हे भामा... धन जन सुख देइहै तेहि ईसा॥"
विवाहित महिलाओं को अखंड सौभाग्य, पति की दीर्घायु और सुखद दांपत्य जीवन की प्राप्ति होती है।

२. सुयोग्य, मनवांछित वर की प्राप्ति (शीघ्र विवाह):
"मांगे उमा वर पति तुम तिनसों... सुफल मनोरथ तुमने लए॥"
विवाह योग्य कन्याओं को माँ पार्वती की कृपा से शीघ्र मनवांछित, सुशील और सुयोग्य वर की प्राप्ति होती है और विवाह के समस्त अवरोध दूर होते हैं।

३. संतान सुख एवं पारिवारिक शांति:
"गणपति जननी पार्वती, अम्बे! शक्ति! भवानि॥"
भगवान श्री गणेश और कार्तिकेय की माता पार्वती की कृपा से निःसंतान दंपतियों को संस्कारी संतान प्राप्त होती है और घर में सुख-शांति रहती है।

४. अन्नपूर्णा कृपा व दारिद्र्य निवारण:
"भगवती प्रतिदिन भिक्षा दात्री... अन्नपूर्णा जग प्रतिपाली॥"
घर में कभी अन्न, धन और वस्त्र का अभाव नहीं होता; माँ अन्नपूर्णा के रूप में वे घर का भण्डार सदा भरा रखती हैं।

५. त्रिताप शमन व आत्मिक सिद्धि:
"अखिल पाप त्रयताप निकन्दिनि... वाचा सिद्ध करि अवलम्बे॥"
शारीरिक, मानसिक और दैविक तीनों तापों का नाश होकर साधक को वाक्-सिद्धि, आत्मबल और अंत में मोक्ष की प्राप्ति होती है।"""

english_lyrics = """॥ Shri Parvati Mata Chalisa ॥

॥ Doha ॥
Jaya Giree Tanaye Dakshaje, Shambhu Priye Gunakhaani।
Ganapati Jananee Paarvatee, Ambe! Shakti! Bhavaani॥

॥ Chaupai ॥
Brahmaa Bheda Na Tumharo Paave। Pancha Badana Nita Tumako Dhyaave॥1॥
Shadmukha Kahi Na Sakata Yasha Tero। Sahasabadana Shrama Karata Ghanero॥2॥
Te-oo Paara Na Paavata Maataa। Sthita Rakshaa Laya Hita Sajaataa॥3॥
Adhara Pravaala Sadrisa Arunaare। Ati Kamaneeya Nayana Kajaraare॥4॥
Lalita Lalaata Vilepita Keshara। Kunkuma Akshata Shobhaa Manahara॥5॥
Kanaka Basana Kanchukee Sajaaye। Katee Mekhalaa Divya Laharaaye॥6॥
Kantha Madaara Haara Kee Shobhaa। Jaahi Dekhi Sahajahi Mana Lobhaa॥7॥
Baalaaruna Ananta Chhabi Dhaaree। Aabhooshana Kee Shobhaa Pyaaree॥8॥
Naanaa Ratna Jatita Sinhaasana। Taapara Raajati Hari Chaturaanana॥9॥
Indraadika Parivaara Poojita। Jaga Mriga Naaga Yaksha Rava Koojita॥10॥
Gira Kailaasa Nivaasinee Jaya Jaya। Kotika Prabhaa Vikaasina Jaya Jaya॥11॥
Tribhuvana Sakala Kutumba Tihaaree। Anu Anu Mahan Tumhaaree Ujiyaaree॥12॥
Hain Mahesha Praanesha! Tumhaare। Tribhuvana Ke Jo Nita Rakhavaare॥13॥
Unaso Pati Tuma Praapta Keenha Jaba। Sukrita Puraatana Udita Bhae Taba॥14॥
Boodhaa Baila Savaaree Jinakee। Mahimaa Kaa Gaave Kou Tinakee॥15॥
Sadaa Shmashaana Bihaaree Shankara। Aabhooshana Hain Bhujanga Bhayankara॥16॥
Kantha Halaahala Ko Chhabi Chhaayee। Neelakantha Kee Padavee Paayee॥17॥
Deva Magana Ke Hita Asa Keenhon। Visha Lai Aapu Tinahi Ami Deenhon॥18॥
Taakee Tuma Patnee Chhavi Dhaarinli। Doorita Vidaarinee Mangala Kaarini॥19॥
Dekhi Parama Saundarya Tihaaro। Tribhuvana Chakita Banaavana Haaro॥20॥
Bhaya Bheetaa So Maataa Gangaa। Lajjaa Maya Hai Salila Tarangaa॥21॥
Sauta Samaana Shambhu Pahaa-ee। Vishnu Padaabja Chhodi So Dhaayee॥22॥
Tehikon Kamala Badana Murajhaayo। Lakhi Satvara Shiva Sheesha Chadhaayo॥23॥
Nityaananda Karee Baradaayinee। Abhaya Bhakta Kara Nita Anapaayinee॥24॥
Akhila Paapa Trayataapa Nikandini। Maaheshwaree Himaalaya Nandini॥25॥
Kaashee Puree Sadaa Mana Bhaayee। Siddha Peetha Tehi Aapu Banaayee॥26॥
Bhagavatee Pratidina Bhikshaa Daatree। Kripaa Pramoda Saneha Vidhaatree॥27॥
Ripukshaya Kaarini Jaya Jaya Ambe। Vaachaa Siddha Kari Avalambe॥28॥
Gauree Umaa Shankaree Kaalee। Annapoornaa Jaga Pratipaalee॥29॥
Saba Jana Kee Eeshwaree Bhagavatee। Patipraanaa Parameshwaree Satee॥30॥
Tumane Kathina Tapasyaa Keenee। Naarada Son Jaba Shikshaa Leenee॥31॥
Anna Na Neera Na Vaayu Ahaaraa। Asthi Maatratana Bhaya-u Tumhaaraa॥32॥
Patra Ghaasa Ko Khaadya Na Bhaaya-u। Umaa Naama Taba Tumane Paaya-u॥33॥
Tapa Biloki Rishi Saata Padhaare। Lage Digaavana Digee Na Haare॥34॥
Taba Tava Jaya Jaya Jaya Uchchaare-u। Saptarishi Nija Geha Sidhaare-u॥35॥
Sura Vidhi Vishnu Paasa Taba Aaye। Vara Dene Ke Vachana Sunaaye॥36॥
Maange Umaa Vara Pati Tuma Tinason। Chaahata Jaga Tribhuvana Nidhi Jinason॥37॥
Evamastu Kahi Te Do-oo Gaye। Suphala Manoratha Tumane Laye॥38॥
Kari Vivaaha Shiva Son He Bhaamaa। Punah Kahaa-ee Hara Kee Baamaa॥39॥
Jo Padhihai Jana Yaha Chaaleesaa। Dhana Jana Sukha Dei-hai Tehi Eesaa॥40॥

॥ Doha ॥
Koota Chandrikaa Subhaga Shira, Jayati Jayati Sukha Khaani।
Paarvatee Nija Bhakta Hita, Rahahu Sadaa Varadaani॥"""

# 1. Update drik_chalisa_38 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

found = False
for item in cols["devi"]["items"]:
    if item["id"] == "drik_chalisa_38":
        item["title"] = "श्री पार्वती माता चालीसा"
        item["title_en"] = "Shri Parvati Mata Chalisa"
        item["en_line"] = "Brahma Bheda Na Tumharo Pave"
        item["hi_line"] = "ब्रह्मा भेद न तुम्हरो पावे"
        item["sub"] = "ब्रह्मा भेद न तुम्हरो पावे • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_parvati_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=kYv06V4-u5o"
        item["video_id"] = "kYv06V4-u5o"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/parvati-mata/parvati-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "अखण्ड सौभाग्य प्रदायिनी भगवती जगज्जननी पार्वती माता"
        item["section"] = "दिव्य देवी माता चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        found = True
        break

if not found:
    print("ERROR: drik_chalisa_38 not found in devi category!")
    sys.exit(1)

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_38 in drik_chalisa_collections.json successfully!")

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

# 3. Add or update chalisa_parvati in CONTENT in app.js
content_obj = {
    "title": "श्री पार्वती माता चालीसा",
    "title_en": "Shri Parvati Mata Chalisa",
    "en_line": "Brahma Bheda Na Tumharo Pave",
    "hi_line": "ब्रह्मा भेद न तुम्हरो पावे",
    "sub": "ब्रह्मा भेद न तुम्हरो पावे • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_parvati_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=kYv06V4-u5o",
    "video_id": "kYv06V4-u5o",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/parvati-mata/parvati-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "अखण्ड सौभाग्य प्रदायिनी भगवती जगज्जननी पार्वती माता",
    "section": "दिव्य देवी माता चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

parvati_content_js = "  chalisa_parvati: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_parvati: {" in app_text:
    pos_s = app_text.find("  chalisa_parvati: {")
    pos_next = app_text.find("\n  chalisa_", pos_s + 1)
    if pos_next == -1:
        pos_next = app_text.find("\n  sundarkand:", pos_s + 1)
    app_text = app_text[:pos_s] + parvati_content_js + app_text[pos_next+1:]
    print("Replaced existing chalisa_parvati in CONTENT!")
else:
    # Insert right before chalisa_saraswati (after chalisa_santoshi)
    pos_saras = app_text.find("  chalisa_saraswati: {")
    if pos_saras != -1:
        app_text = app_text[:pos_saras] + parvati_content_js + app_text[pos_saras:]
        print("Inserted chalisa_parvati before chalisa_saraswati in CONTENT!")
    else:
        # fallback: insert before sundarkand
        pos_sun = app_text.find("  sundarkand: {")
        if pos_sun != -1:
            app_text = app_text[:pos_sun] + parvati_content_js + app_text[pos_sun:]
            print("Inserted chalisa_parvati before sundarkand in CONTENT!")
        else:
            print("ERROR: Could not find insert location in CONTENT!")

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

print("ALL PARVATI UPDATES COMPLETED!")
