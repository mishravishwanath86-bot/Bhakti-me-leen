import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री वैष्णो देवी चालीसा ॥

॥ दोहा ॥
गरुड़ वाहिनी वैष्णवी, त्रिकुटा पर्वत धाम।
काली, लक्ष्मी, सरस्वती, शक्ति तुम्हें प्रणाम॥

॥ चौपाई ॥
नमोः नमोः वैष्णो वरदानी। कलि काल मे शुभ कल्याणी॥१॥
मणि पर्वत पर ज्योति तुम्हारी। पिंडी रूप में हो अवतारी॥२॥
देवी देवता अंश दियो है। रत्नाकर घर जन्म लियो है॥३॥
करी तपस्या राम को पाऊँ। त्रेता की शक्ति कहलाऊँ॥४॥
कहा राम मणि पर्वत जाओ। कलियुग की देवी कहलाओ॥५॥
विष्णु रूप से कल्की बनकर। लूंगा शक्ति रूप बदलकर॥६॥
तब तक त्रिकुटा घाटी जाओ। गुफा अंधेरी जाकर पाओ॥७॥
काली-लक्ष्मी-सरस्वती माँ। करेंगी शोषण-पार्वती माँ॥८॥
ब्रह्मा, विष्णु, शंकर द्वारे। हनुमत भैरों प्रहरी प्यारे॥९॥
रिद्धि, सिद्धि चंवर डुलावें। कलियुग-वासी पूजत आवें॥१०॥
पान सुपारी ध्वजा नारियल। चरणामृत चरणों का निर्मल॥११॥
दिया फलित वर माँ मुस्काई। करन तपस्या पर्वत आई॥१२॥
कलि कालकी भड़की ज्वाला। इक दिन अपना रूप निकाला॥१३॥
कन्या बन नगरोटा आई। योगी भैरों दिया दिखाई॥१४॥
रूप देख सुन्दर ललचाया। पीछे-पीछे भागा आया॥१५॥
कन्याओं के साथ मिली माँ। कौल-कंदौली तभी चली माँ॥१६॥
देवा माई दर्शन दीना। पवन रूप हो गई प्रवीणा॥१७॥
नवरात्रों में लीला रचाई। भक्त श्रीधर के घर आई॥१८॥
योगिन को भण्डारा दीना। सबने रूचिकर भोजन कीना॥१९॥
मांस, मदिरा भैरों मांगी। रूप पवन कर इच्छा त्यागी॥२०॥
बाण मारकर गंगा निकाली। पर्वत भागी हो मतवाली॥२१॥
चरण रखे आ एक शिला जब। चरण-पादुका नाम पड़ा तब॥२२॥
पीछे भैरों था बलकारी। छोटी गुफा में जाय पधारी॥२३॥
नौ माह तक किया निवासा। चली फोड़कर किया प्रकाशा॥२४॥
आद्या शक्ति-ब्रह्म कुमारी। कहलाई माँ आद कुंवारी॥२५॥
गुफा द्वार पहुँची मुस्काई। लांगुर वीर ने आज्ञा पाई॥२६॥
भागा-भागा भैरों आया। रक्षा हित निज शस्त्र चलाया॥२७॥
पड़ा शीश जा पर्वत ऊपर। किया क्षमा जा दिया उसे वर॥२८॥
अपने संग में पुजवाऊंगी। भैरों घाटी बनवाऊंगी॥२९॥
पहले मेरा दर्शन होगा। पीछे तेरा सुमरन होगा॥३०॥
बैठ गई माँ पिण्डी होकर। चरणों में बहता जल झर-झर॥३१॥
चौंसठ योगिनी-भैंरो बरवन। सप्तऋषि आ करते सुमरन॥३२॥
घंटा ध्वनि पर्वत पर बाजे। गुफा निराली सुन्दर लागे॥३३॥
भक्त श्रीधर पूजन कीना। भक्ति सेवा का वर लीना॥३४॥
सेवक ध्यानूं तुमको ध्याया। ध्वजा व चोला आन चढ़ाया॥३५॥
सिंह सदा दर पहरा देता। पंजा शेर का दुःख हर लेता॥३६॥
जम्बू द्वीप महाराज मनाया। सर सोने का छत्र चढ़ाया॥३७॥
हीरे की मूरत संग प्यारी। जगे अखंड इक जोत तुम्हारी॥३८॥
आश्विन चैत्र नवराते आऊँ। पिण्डी रानी दर्शन पाऊँ॥३९॥
सेवक 'शर्मा' शरण तिहारी। हरो वैष्णो विपत हमारी॥४०॥

॥ दोहा ॥
कलियुग में महिमा तेरी, है माँ अपरम्पार।
धर्म की हानि हो रही, प्रगट हो अवतार॥"""

meaning = """॥ श्री वैष्णो देवी चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहा】
• "गरुड़ वाहिनी वैष्णवी, त्रिकुटा पर्वत धाम। काली, लक्ष्मी, सरस्वती, शक्ति तुम्हें प्रणाम॥"
भावार्थ: हे भगवान श्रीहरि विष्णु की पराशक्ति गरुड़वाहिनी वैष्णवी! जम्मू के पावन त्रिकूट पर्वत पर आपका परम दिव्य धाम है। आप महाकाली, महालक्ष्मी और महासरस्वती—इन तीनों महाशक्तियों का सम्मिलित त्रिशक्ति स्वरूप हैं; हे परम शक्ति माँ वैष्णो देवी! आपके पावन श्रीचरणों में हमारा कोटि-कोटि प्रणाम है।

【चौपाइयां — पद्यवार भावार्थ】
१-१०. "नमोः नमोः वैष्णो वरदानी... कलियुग-वासी पूजत आवें॥"
भावार्थ: हे मनोवांछित वरदान देने वाली माँ वैष्णो देवी! आपको बारंबार नमस्कार है। इस कलिकाल में आप ही संपूर्ण चराचर जगत का परम मंगल और कल्याण करने वाली हैं। पावन त्रिकूट पर्वत पर आपकी दिव्य ज्योति निरंतर जगमगाती है और आप महागुफा में तीन पवित्र पिण्डियों (महाकाली, महालक्ष्मी, महासरस्वती) के रूप में अवतरित हुई हैं। समस्त देवी-देवताओं ने अपने-अपने दिव्य तेज का अंश प्रदान किया, जिससे आपका प्राकट्य दक्षिण भारत के धर्मात्मा रत्नाकर जी के घर कन्या रूप में हुआ। आपने प्रभु श्रीराम को पति रूप में पाने हेतु बाल्यकाल से ही घोर तपस्या की और त्रेतायुग की परम तपस्विनी शक्ति कहलाईं। मर्यादा पुरुषोत्तम भगवान श्रीराम ने आपसे कहा कि हे देवी! आप उत्तर में पावन त्रिकूट पर्वत पर जाकर तपस्या कीजिए और कलियुग में संपूर्ण जगत की तारक अधिष्ठात्री देवी के रूप में पूजित होइए। जब मैं कलिकाल के अंत में भगवान विष्णु के दशम अवतार 'कल्कि' रूप में अवतरित होऊँगा, तब मैं आपको अपनी शक्ति के रूप में स्वीकार करूँगा। तब तक आप पावन त्रिकुटा घाटी की रहस्यमयी गुफा में निवास कीजिए। वहां महाकाली, महालक्ष्मी और महासरस्वती—तीनों देवियां तथा आदि शक्ति पार्वती माँ आपका पोषण और सान्निध्य करेंगी। आपके पवित्र गुफा-द्वार पर ब्रह्मा, विष्णु और महेश नित्य वंदन करते हैं तथा श्री हनुमान जी (लांगुर वीर) और कालभैरव आपके प्रिय रक्षक-प्रहरी बनकर उपस्थित रहते हैं। रिद्धि और सिद्धि आपके ऊपर चंवर डुलाती हैं और संपूर्ण कलियुग के नर-नारी आपके पावन दर्शन हेतु खिंचे चले आते हैं।

११-२०. "पान सुपारी ध्वजा नारियल... रूप पवन कर इच्छा त्यागी॥"
भावार्थ: भक्तजन लाल चुनरी (ध्वजा), नारियल, पान, सुपारी और मेवे लेकर आपके पावन दरबार में आते हैं और आपके श्रीचरणों से प्रवाहित होने वाले निर्मल पवित्र चरणामृत का पान करते हैं। प्रभु श्रीराम द्वारा दिए गए वरदान को स्मरण कर माँ मंद-मंद मुस्काईं और तपस्या करने त्रिकूट पर्वत पर पधारीं। जब कलिकाल में पापों की ज्वाला भड़कने लगी, तब माँ ने लोक-कल्याण हेतु कन्या रूप में अपनी लीलाएं प्रकट कीं। माता एक सुंदर कन्या का रूप धरकर नगरोटा (जम्मू) आईं, जहाँ गोरखनाथ के शिष्य हठी योगी भैरवनाथ की दृष्टि उन पर पड़ी। कन्या का अलौकिक व दिव्य सौन्दर्य देखकर भैरवनाथ कामातुर व लोभी हो गया और उनका पीछा करने लगा। माता अन्य छोटी कन्याओं के संग खेलती हुईं कौल-कंदौली पहुंचीं और वहां से आगे बढ़ गईं। देवा माई में माता ने अपने भक्तों को दर्शन दिए और पवन (हवा) का सूक्ष्म वेगवान रूप धरकर द्रुत गति से आगे निकल गईं। शारदीय नवरात्र के पावन पर्व पर माता ने अद्भुत लीला रची और अपने अनन्य निष्काम भक्त पंडित श्रीधर के घर आईं। माता ने निर्धन श्रीधर के घर पर संपूर्ण गाँव और साधु-संतों हेतु विशाल दिव्य भण्डारा आयोजित करवाया, जहाँ सभी ने तृप्त होकर स्वादिष्ट भोजन किया। किन्तु हठी भैरवनाथ ने वहाँ मांस और मदिरा की अनुचित मांग की; तब माता ने उसे समझाया, किन्तु उसके न मानने पर माता ने पवन का रूप धरकर वहाँ से प्रस्थान किया।

२१-३०. "बाण मारकर गंगा निकाली... पीछे तेरा सुमरन होगा॥"
भावार्थ: प्यास से व्याकुल लांगुर वीर (वीर हनुमान जी) की प्यास बुझाने हेतु माता ने पर्वत पर बाण मारकर शीतल जल की पावन धारा निकाली, जो आज 'बाणगंगा' के नाम से विख्यात है। पर्वत की ओर आगे बढ़ते हुए माता ने जिस पावन शिला पर अपने पैर रखे, उस पर उनके दिव्य पद-चिह्न अंकित हो गए, जिसे आज 'चरण-पादुका' कहा जाता है। बलशाली भैरवनाथ जब हठपूर्वक पीछे-पीछे आता रहा, तब माता अर्द्धकुंवारी स्थित एक संकरी गुफा (गर्भजून) में पधारीं। वहां माता ने एक बालक की भांति माता के गर्भ के समान नौ माह तक एकांत में तपस्या की, और फिर गुफा को अपने त्रिशूल से भेदकर बाहर दिव्य प्रकाश फैलाते हुए निकलीं। आद्य शक्ति ब्रह्मकुमारी होने के कारण माता का यह पावन धाम 'माँ आदकुंवारी' के नाम से प्रसिद्ध हुआ। जब माता मुख्य भवन की पावन गुफा के द्वार पर पहुँचीं, तो उन्होंने लांगुर वीर (हनुमान जी) को रक्षा की आज्ञा दी। जब कामांध भैरवनाथ दौड़ता हुआ गुफा-द्वार पर आया, तो माता ने धर्म और मर्यादा की रक्षा हेतु अपने दिव्य खड्ग से प्रहार किया। भैरव का कटा हुआ सिर उड़कर कई किलोमीटर दूर ऊपर पर्वत की घाटी में जा गिरा। मरते समय जब उसने पश्चाताप कर क्षमा मांगी, तो कृपामयी माँ ने उसे क्षमा कर वरदान दिया। माता ने कहा कि मैं अपने दरबार के साथ-साथ तेरी भी पूजा करवाऊँगी और उस घाटी में 'भैरव घाटी' का निर्माण होगा। जो भी भक्त मेरे भवन का दर्शन करेगा, उसकी यात्रा तभी पूर्ण व फलदायी होगी जब वह तेरे मंदिर में जाकर तेरा दर्शन करेगा।

३१-४०. "बैठ गई माँ पिण्डी होकर... हरो वैष्णो विपत हमारी॥"
भावार्थ: इसके पश्चात भगवती महाकाली, महालक्ष्मी और महासरस्वती—तीनों पिण्डियों के दिव्य रूप में महागुफा में विराजमान हो गईं, जिनके पवित्र श्रीचरणों से अविरल शीतल जल झर-झर प्रवाहित होता है। चौंसठ योगिनियां, भैरव गण और सप्तर्षि नित्य आकर माता का स्मरण और ध्यान करते हैं। त्रिकूट पर्वत पर नित्य घंटों-घड़ियालों की मधुर मंगल ध्वनि गूंजती है और यह पावन गुफा अत्यंत अलौकिक व मनोरम लगती है। परम भक्त श्रीधर ने विधिपूर्वक माता का प्रथम पूजन किया और अनन्य भक्ति व सेवा का वरदान प्राप्त किया। अनन्य सेवक ध्यानू भगत ने माता का निष्काम ध्यान किया और सोने का छत्र व लाल चोला माता को समर्पित किया। माता के पावन सिंहद्वार पर साक्षात सिंह (शेर) नित्य पहरा देता है, और शेर का पंजा भक्तों के समस्त कष्टों को हर लेता है। जम्मू-कश्मीर के महाराजा ने माता की स्तुति कर दरबार में स्वर्ण का छत्र चढ़ाया। माता की दिव्य ज्योति के सम्मुख एक अखंड पावन ज्योति निरंतर जलती रहती है। साधक प्रार्थना करता है कि हे मैया! मैं आश्विन और चैत्र के नवरात्रों में नित्य आपके पावन दरबार में आऊँ और आपकी पवित्र पिण्डी रानी का दर्शन प्राप्त करूँ। आपका यह सेवक पूर्ण रूप से आपकी शरण में है; हे माँ वैष्णो देवी! हमारे जीवन की समस्त विपत्तियों, संकटों और रोगों का समूल नाश कीजिए।

【समापन दोहा】
• "कलियुग में महिमा तेरी, है माँ अपरम्पार। धर्म की हानि हो रही, प्रगट हो अवतार॥"
भावार्थ: हे माँ वैष्णो देवी! इस कलिकाल में आपकी महिमा अत्यंत असीम व अपरंपार है। हे जगदम्बा! संसार में जब-जब अधर्म बढ़ता है और धर्म की हानि होती है, तब-तब आप धर्म की रक्षा और भक्तों के उद्धार हेतु दिव्य अवतार धारण करती हैं।"""

vidhi = """॥ श्री वैष्णो देवी चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल ब्रह्ममुहूर्त अथवा सांध्यकालीन आरती वेला।
- सर्वोत्तम वार: मंगलवार एवं शुक्रवार (भगवती जगदम्बा की विशेष कृपा के दिन)।
- महापर्व व पावन तिथियां: चैत्र एवं शारदीय नवरात्रि (विशेषकर महाअष्टमी व महानवमी), नववर्ष, दीपावली, तथा प्रत्येक मास के शुक्ल पक्ष की अष्टमी तिथि।

२. दिशा, आसन व वस्त्र:
- दिशा: पूर्व अथवा उत्तर दिशा की ओर मुख करके बैठें।
- आसन: लाल अथवा पीले रंग का स्वच्छ ऊनी आसन या कुशासन बिछाएं।
- वस्त्र: साधक को शुद्ध, धुले हुए लाल, पीले अथवा श्वेत वस्त्र धारण करने चाहिए।

३. दीपक, पुष्प व नैवेद्य पूजन सामग्री:
- दीपक: गाय के शुद्ध देशी घी का अथवा तिल के तेल का दीपक प्रज्वलित करें।
- प्रिय पुष्प: लाल गुलाब, गुड़हल (जबा-कुसुम), अथवा पीले गेंदे के ताजे पुष्प।
- तिलक: रोली, कुंकुम, केसर, लाल चंदन और अक्षत का तिलक करें।
- प्रिय नैवेद्य: सूजी का हलवा, काले भुने/उबले चने, पूरी, पंचमेवा, बताशे, नारियल (श्रीफल), लाल चुनरी और मिश्री का भोग लगाएं।

४. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन, पवित्रीकरण एवं संकल्प करें।
- माँ वैष्णो देवी का ध्यान करें:
  'ॐ त्रिशक्ति-स्वरूपायै विद्महे महाशक्त्यै च धीमहि। तन्नो वैष्णवी प्रचोदयात्॥
   वन्दे वन्दारुमन्दारमिन्दिरामानन्दकन्दलम्। अमन्दवैभवामोदं वैष्णवीं विष्णुरूपिणीम्॥'
- माँ वैष्णवी के नर्वाण मन्त्र 'ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे' अथवा 'ॐ श्रीं ह्रीं क्लीं वैष्णवी देव्यै नमः' का १०८ बार जप करें।
- इसके पश्चात पूर्ण एकाग्रता एवं भक्तिभाव से 'श्री वैष्णो देवी चालीसा' का १, ३, ७ अथवा ११ बार पाठ करें।
- पाठ के उपरांत कर्पूर से आरती करें, छोटी कन्याओं (कंजक) का पूजन कर उन्हें हलवा-चना-पूरी का प्रसाद वितरित करें।"""

significance = """॥ श्री वैष्णो देवी चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. मनोवांछित फल व सर्वकामना सिद्धि (वरदानी शक्ति):
"नमोः नमोः वैष्णो वरदानी। कलि काल मे शुभ कल्याणी॥"
माँ वैष्णो देवी कलियुग की साक्षात जाग्रत अधिष्ठात्री देवी हैं। चालीसा का श्रद्धापूर्वक नित्य पाठ करने से साधक की धर्म, अर्थ, काम और मोक्ष से जुड़ी समस्त मनोकामनाएं पूर्ण होती हैं।

२. त्रिशक्ति (लक्ष्मी, काली, सरस्वती) का सम्मिलित अनुग्रह:
"काली, लक्ष्मी, सरस्वती, शक्ति तुम्हें प्रणाम॥"
एक ही आराधना से साधक को माँ महालक्ष्मी से विपुल धन-वैभव, माँ महासरस्वती से सद्बुद्धि व ज्ञान, तथा माँ महाकाली से असीम बल, ओज और रोग-शत्रु मुक्ति की प्राप्ति होती है।

३. आकस्मिक संकट, भय व विपत्ति निवारण:
"सेवक 'शर्मा' शरण तिहारी। हरो वैष्णो विपत हमारी॥"
माता के पावन दरबार में लांगुर वीर (श्री हनुमान जी) और कालभैरव रक्षक के रूप में उपस्थित रहते हैं, जिससे साधक को किसी भी प्रकार की बुरी नजर, ऊपरी बाधा, अकाल भय या संकट स्पर्श नहीं कर पाता।

४. पारिवारिक सुख-शांति व संतान रक्षा:
घर में क्लेश, अशांति और नकारात्मक ऊर्जा का शमन होकर सुख, समृद्धि और आरोग्य का वास होता है तथा अबोध बालकों व संतान की रक्षा होती है।

५. तीर्थ-यात्रा का अक्षय पुण्य फल:
जो भक्त किसी कारणवश कटरा स्थित त्रिकूट पर्वत के भवन नहीं जा पाते, उन्हें घर बैठे इस चालीसा के पाठ से माँ वैष्णो देवी के पावन दर्शन और संपूर्ण यात्रा का फल प्राप्त होता है।"""

english_lyrics = """॥ Shri Vaishno Devi Chalisa ॥

॥ Doha ॥
Garuda Vaahinee Vaishnavee, Trikutaa Parvata Dhaama।
Kaalee, Lakshmee, Saraswatee, Shakti Tumhen Pranaama॥

॥ Chaupai ॥
Namo Namo Vaishno Varadaanee। Kali Kaala Me Shubha Kalyaanee॥1॥
Mani Parvata Para Jyoti Tumhaaree। Pindee Roopa Men Ho Avataaree॥2॥
Devee Devataa Ansha Diyo Hai। Ratnaakara Ghara Janma Liyo Hai॥3॥
Karee Tapasyaa Raama Ko Paaoon। Tretaa Kee Shakti Kahalaaoon॥4॥
Kahaa Raama Mani Parvata Jaao। Kaliyuga Kee Devee Kahalaao॥5॥
Vishnu Roopa Se Kalkee Banakara। Loongaa Shakti Roopa Badalakar॥6॥
Taba Taka Trikutaa Ghaatee Jaao। Guphaa Andheree Jaakara Paao॥7॥
Kaalee-Lakshmee-Saraswatee Maan। Karengee Shoshana-Paarvatee Maan॥8॥
Brahmaa, Vishnu, Shankara Dvaare। Hanumata Bhairon Praharee Pyaare॥9॥
Riddhi, Siddhi Chanvara Dulaaven। Kaliyuga-Vaasee Poojata Aaven॥10॥
Paana Supaaree Dhvajaa Naariyala। Charanaamrita Charanon Kaa Nirmala॥11॥
Diyaa Phalita Vara Maan Muskaa-ee। Karana Tapasyaa Parvata Aa-ee॥12॥
Kali Kaalakee Bhadakee Jvaalaa। Ika Dina Apanaa Roopa Nikaalaa॥13॥
Kanyaa Bana Nagarotaa Aa-ee। Yogee Bhairon Diyaa Dikhaa-ee॥14॥
Roopa Dekha Sundara Lalachaayaa। Peechhe-Peechhe Bhaagaa Aayaa॥15॥
Kanyaaon Ke Saatha Milee Maan। Kaula-Kandaulee Tabhee Chalee Maan॥16॥
Devaa Maa-ee Darshana Deenaa। Pavana Roopa Ho Ga-ee Praveenaa॥17॥
Navaraatron Men Leelaa Rachaa-ee। Bhakta Shreedhara Ke Ghara Aa-ee॥18॥
Yogina Ko Bhandaaraa Deenaa। Sabane Roochikara Bhojana Keenaa॥19॥
Maansa, Madiraa Bhairon Maangee। Roopa Pavana Kara Ichchhaa Tyaagee॥20॥
Baana Maarakara Gangaa Nikaalee। Parvata Bhaagee Ho Matavaalee॥21॥
Charana Rakhe Aa Eka Shilaa Jaba। Charana-Paadukaa Naama Padaa Taba॥22॥
Peechhe Bhairon Thaa Balakaaree। Chhotee Guphaa Men Jaaya Padhaaree॥23॥
Nau Maaha Taka Kiyaa Nivaasaa। Chalee Phodakara Kiyaa Prakaashaa॥24॥
Aadyaa Shakti-Brahma Kumaaree। Kahalaa-ee Maan Aada Kunvaaree॥25॥
Guphaa Dvaara Pahunchee Muskaa-ee। Laangura Veera Ne Aagyaa Paa-ee॥26॥
Bhaagaa-Bhaagaa Bhairon Aayaa। Rakshaa Hita Nija Shastra Chalaa-ee॥27॥
Padaa Sheesha Jaa Parvata Oopara। Kiyaa Kshamaa Jaa Diyaa Use Vara॥28॥
Apane Sanga Men Poajavaaungee। Bhairon Ghaatee Banavaaungee॥29॥
Pahale Meraa Darshana Hogaa। Peechhe Teraa Sumarana Hogaa॥30॥
Baitha Ga-ee Maan Pindee Hokara। Charanon Men Bahataa Jala Jhara-Jhara॥31॥
Chaunsatha Yoginee-Bhairon Baravana। Saptarishi Aa Karate Sumarana॥32॥
Ghantaa Dhvani Parvata Para Baaje। Guphaa Niraalee Sundara Laage॥33॥
Bhakta Shreedhara Poojana Keenaa। Bhakti Sevaa Kaa Vara Leenaa॥34॥
Sevaka Dhyaanoon Tumako Dhyaayaa। Dhvajaa Va Cholaa Aana Chadhaayaa॥35॥
Sinha Sadaa Dara Paharaa Detaa। Panjaa Shera Kaa Duhkha Hara Letaa॥36॥
Jamboo Dweepa Mahaaraaja Manaayaa। Sara Sone Kaa Chhatra Chadhaayaa॥37॥
Heere Kee Moorata Sanga Pyaaree। Jage Akhanda Ika Jota Tumhaaree॥38॥
Aashvina Chaitra Navaraate Aaoon। Pindee Raanee Darshana Paaoon॥39॥
Sevaka 'Sharmaa' Sharana Tihaaree। Haro Vaishno Vipata Hamaaree॥40॥

॥ Doha ॥
Kaliyuga Men Mahimaa Teree, Hai Maan Aparamppaara।
Dharma Kee Haani Ho Rahee, Pragata Ho Avataara॥"""

# 1. Update drik_chalisa_36 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

found = False
for item in cols["devi"]["items"]:
    if item["id"] == "drik_chalisa_36":
        item["title"] = "श्री वैष्णो देवी चालीसा"
        item["title_en"] = "Shri Vaishno Devi Chalisa"
        item["en_line"] = "Namo Namo Vaishno Varadani"
        item["hi_line"] = "नमोः नमोः वैष्णो वरदानी"
        item["sub"] = "नमोः नमोः वैष्णो वरदानी • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_vaishno_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=H9bCt3M67os"
        item["video_id"] = "H9bCt3M67os"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/vaishno-mata/vaishno-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "त्रिकूटपर्वतवासिनी त्रिशक्ति स्वरूपा भगवती वैष्णो देवी माता"
        item["section"] = "दिव्य देवी माता चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        found = True
        break

if not found:
    print("ERROR: drik_chalisa_36 not found in devi category!")
    sys.exit(1)

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_36 in drik_chalisa_collections.json successfully!")

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

# 3. Add or update chalisa_vaishno in CONTENT in app.js
content_obj = {
    "title": "श्री वैष्णो देवी चालीसा",
    "title_en": "Shri Vaishno Devi Chalisa",
    "en_line": "Namo Namo Vaishno Varadani",
    "hi_line": "नमोः नमोः वैष्णो वरदानी",
    "sub": "नमोः नमोः वैष्णो वरदानी • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_vaishno_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=H9bCt3M67os",
    "video_id": "H9bCt3M67os",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/vaishno-mata/vaishno-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "त्रिकूटपर्वतवासिनी त्रिशक्ति स्वरूपा भगवती वैष्णो देवी माता",
    "section": "दिव्य देवी माता चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

vaishno_content_js = "  chalisa_vaishno: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_vaishno: {" in app_text:
    pos_s = app_text.find("  chalisa_vaishno: {")
    pos_next = app_text.find("\n  chalisa_", pos_s + 1)
    if pos_next == -1:
        pos_next = app_text.find("\n  sundarkand:", pos_s + 1)
    app_text = app_text[:pos_s] + vaishno_content_js + app_text[pos_next+1:]
    print("Replaced existing chalisa_vaishno in CONTENT!")
else:
    # Insert right before chalisa_saraswati (after chalisa_mahakali)
    pos_saras = app_text.find("  chalisa_saraswati: {")
    if pos_saras != -1:
        app_text = app_text[:pos_saras] + vaishno_content_js + app_text[pos_saras:]
        print("Inserted chalisa_vaishno before chalisa_saraswati in CONTENT!")
    else:
        # fallback: insert before sundarkand
        pos_sun = app_text.find("  sundarkand: {")
        if pos_sun != -1:
            app_text = app_text[:pos_sun] + vaishno_content_js + app_text[pos_sun:]
            print("Inserted chalisa_vaishno before sundarkand in CONTENT!")
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

print("ALL VAISHNO UPDATES COMPLETED!")
