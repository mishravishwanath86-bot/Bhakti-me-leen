import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री शीतला चालीसा ॥

॥ दोहा ॥
जय-जय माता शीतला, तुमहिं धरै जो ध्यान।
होय विमल शीतल हृदय, विकसै बुद्धि बलज्ञान॥

॥ चौपाई ॥
जय-जय-जय शीतला भवानी। जय जग जननि सकल गुणखानी॥१॥
गृह-गृह शक्ति तुम्हारी राजित। पूरण शरदचन्द्र समसाजित॥२॥
विस्फोटक से जलत शरीरा। शीतल करत हरत सब पीरा॥३॥
मातु शीतला तव शुभनामा। सबके गाढ़े आवहिं कामा॥४॥
शोकहरी शंकरी भवानी। बाल-प्राणरक्षी सुख दानी॥५॥
शुचि मार्जनी कलश करराजै। मस्तक तेज सूर्य समराजै॥६॥
चौसठ योगिन संग में गावैं। वीणा ताल मृदंग बजावै॥७॥
नृत्य नाथ भैरो दिखरावैं। सहज शेष शिव पार ना पावैं॥८॥
धन्य-धन्य धात्री महारानी। सुरनर मुनि तब सुयश बखानी॥९॥
ज्वाला रूप महा बलकारी। दैत्य एक विस्फोटक भारी॥१०॥
घर-घर प्रविशत कोई न रक्षत। रोग रूप धरि बालक भक्षत॥११॥
हाहाकार मच्यो जगभारी। सक्यो न जब संकट टारी॥१२॥
तब मैया धरि अद्भुत रूपा। करमें लिये मार्जनी सूपा॥१३॥
विस्फोटकहिं पकड़ि कर लीन्ह्यो। मुसल प्रहार बहुविधि कीन्ह्यो॥१४॥
बहुत प्रकार वह विनती कीन्हा। मैया नहीं भल मैं कछु चीन्हा॥१५॥
अबनहिं मातु, काहुगृह जइहौं। जहँ अपवित्र सकल दुःख हरिहौं॥१६॥
भभकत तन, शीतल ह्वै जइहैं। विस्फोटक भयघोर नसइहैं॥१७॥
श्री शीतलहिं भजे कल्याना। वचन सत्य भाषे भगवाना॥१८॥
विस्फोटक भय जिहि गृह भाई। भजै देवि कहँ यही उपाई॥१९॥
कलश शीतला का सजवावै। द्विज से विधिवत पाठ करावै॥२०॥
तुम्हीं शीतला, जग की माता। तुम्हीं पिता जग की सुखदाता॥२१॥
तुम्हीं जगद्धात्री सुखसेवी। नमो नमामि शीतले देवी॥२२॥
नमो सुक्खकरणी दुःखहरणी। नमो-नमो जगतारणि तरणी॥२३॥
नमो-नमो त्रैलोक्य वन्दिनी। दुखदारिद्रादिक कन्दिनी॥२४॥
श्री शीतला, शेढ़ला, महला। रुणलीह्युणनी मातु मंदला॥२५॥
हो तुम दिगम्बर तनुधारी। शोभित पंचनाम असवारी॥२६॥
रासभ, खर बैशाख सुनन्दन। गर्दभ दुर्वाकंद निकन्दन॥२७॥
सुमिरत संग शीतला माई। जाहि सकल दुख दूर पराई॥२८॥
गलका, गलगन्डादि जुहोई। ताकर मंत्र न औषधि कोई॥२९॥
एक मातु जी का आराधन। और नहिं कोई है साधन॥३०॥
निश्चय मातु शरण जो आवै। निर्भय मन इच्छित फल पावै॥३१॥
कोढ़ी, निर्मल काया धारै। अन्धा, दृग-निज दृष्टि निहारै॥३२॥
वन्ध्या नारि पुत्र को पावै। जन्म दरिद्र धनी होई जावै॥३३॥
मातु शीतला के गुण गावत। लखा मूक को छन्द बनावत॥३४॥
यामे कोई करै जनि शंका। जग मे मैया का ही डंका॥३५॥
भनत रामसुन्दर प्रभुदासा। तट प्रयाग से पूरब पासा॥३६॥
पुरी तिवारी मोर निवासा। ककरा गंगा तट दुर्वासा॥३७॥
अब विलम्ब मैं तोहि पुकारत। मातु कृपा कौ बाट निहारत॥३८॥
पड़ा क्षर तव आस लगाई। रक्षा करहु शीतला माई॥३९॥

॥ दोहा ॥
घट-घट वासी शीतला, शीतल प्रभा तुम्हार।
शीतल छइयां में झुलई, मइया पलना डार॥"""

meaning = """॥ श्री शीतला चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहा】
• "जय-जय माता शीतला, तुमहिं धरै जो ध्यान। होय विमल शीतल हृदय, विकसै बुद्धि बलज्ञान॥"
भावार्थ: हे माता शीतला! आपकी सदा-सदा जय हो। जो भी मनुष्य श्रद्धापूर्वक आपका ध्यान धरता है, उसका हृदय निर्मल, शांत और शीतल हो जाता है तथा उसके भीतर सद्बुद्धि, आत्मबल और दिव्य ज्ञान का विकास होता है।

【चौपाइयां — पद्यवार भावार्थ】
१-५. "जय-जय-जय शीतला भवानी... बाल-प्राणरक्षी सुख दानी॥"
भावार्थ: हे भगवती शीतला भवानी! आपकी जय हो, जय हो, जय हो; आप संपूर्ण जगत की जननी और समस्त सद्गुणों की अक्षय खान हैं। घर-घर में आपकी पावन शक्ति विराजित है; आपका रूप पूर्ण शरद पूर्णिमा के चन्द्रमा के समान शीतल, सुंदर व सुसज्जित है। विस्फोटक (चेचक, खसरा, बड़ी माता, छोटी माता, तीव्र ज्वर आदि) की ज्वाला से जब मनुष्य का शरीर भभकता और जलता है, तब आपकी दया-दृष्टि उसे शीतल कर समस्त पीड़ाओं को क्षण भर में हर लेती है। हे माता! आपका पावन नाम 'शीतला' अत्यंत शुभकारी है; आप संकट और गाढ़ी विपत्ति के समय सबकी सहायक बनती हैं। आप भक्तों के शोकों को हरने वाली, भगवान शंकर की शक्ति भवानी, अबोध बालकों के प्राणों की रक्षा करने वाली और समस्त सुखों को प्रदान करने वाली हैं।

६-१०. "शुचि मार्जनी कलश करराजै... दैत्य एक विस्फोटक भारी॥"
भावार्थ: आपके पवित्र कर-कमलों में नीम की झाड़ू (मार्जनी) और अमृतमय शीतल जल का कलश सुशोभित है; आपके मस्तक पर करोड़ों सूर्यों के समान दिव्य तेज जगमगा रहा है। चौंसठ योगिनियां आपके संग में वीणा, ताल और मृदंग बजाकर आपकी महिमा का मधुर गान करती हैं। भगवान भैरव आपके सम्मुख आनंद-नृत्य प्रस्तुत करते हैं; स्वयं शेषनाग और देवाधिदेव शिव भी आपकी अगाध लीला का पार नहीं पा सकते। हे संपूर्ण जगत का धात्री (पोषण करने वाली) महारानी! आप धन्य हैं, धन्य हैं; देवता, मनुष्य और ऋषि-मुनि निरंतर आपके सुयश का बखान करते हैं। एक समय की बात है कि 'विस्फोटक' नाम का एक भयानक, बलशाली दैत्य प्रचंड अग्नि-ज्वाला का रूप धरकर संसार में प्रकट हुआ।

११-१५. "घर-घर प्रविशत कोई न रक्षत... मैया नहीं भल मैं कछु चीन्हा॥"
भावार्थ: वह दुष्ट दैत्य घर-घर में घुसने लगा और कोई भी उससे रक्षा करने में समर्थ न हो सका; वह चेचक व तीव्र ज्वर रूपी भयानक रोग बनकर बालकों के प्राणों को भक्षण करने लगा। जब कोई भी इस भीषण संकट को टाल न सका, तो संपूर्ण संसार में भारी हाहाकार मच गया। तब हे मैया! आपने जीवों की रक्षा हेतु एक अद्भुत व अलौकिक रूप धारण किया; आपने अपने हाथों में मार्जनी (झाड़ू), सूप और मूसल धारण किया। आपने उस दुष्ट विस्फोटक दैत्य को बलपूर्वक पकड़ लिया और उस पर मूसल से अनेक भीषण प्रहार किए। तब उस दैत्य ने भयभीत होकर माता के चरणों में गिरकर अनेक प्रकार से विनीत प्रार्थना की—हे मैया! मैंने अज्ञानवश आपको नहीं पहचाना था, मुझे क्षमा कीजिए।

१६-२०. "अबनहिं मातु, काहुगृह जइहौं... द्विज से विधिवत पाठ करावै॥"
भावार्थ: दैत्य ने वचन दिया कि हे माता! अब मैं कभी किसी ऐसे घर में नहीं जाऊँगा जहाँ स्वच्छता और आपकी पावन पूजा होगी, और मैं समस्त दुखों का हरण करूँगा। जो भी व्यक्ति जलते हुए शरीर से पीड़ित होगा, वह आपकी कृपा से शीतल हो जाएगा और उसका भयानक विस्फोटक-भय सदा के लिए नष्ट हो जाएगा। स्वयं भगवान शिव ने यह सत्य वचन कहा है कि जो भी मनुष्य भगवती शीतला का भजन करता है, उसका सर्वथा कल्याण होता है। हे भाई! जिस भी घर में चेचक या त्वचा रोगों का भय हो, उस घर में शीतला माता का पूजन करना ही एकमात्र अचूक उपाय है। जातक अपने घर में माता शीतला का पावन कलश स्थापित करवाए और योग्य ब्राह्मण से विधिपूर्वक चालीसा का पाठ करवाए।

२१-२४. "तुम्हीं शीतला, जग की माता... दुखदारिद्रादिक कन्दिनी॥"
भावार्थ: हे शीतला माता! आप ही इस चराचर जगत की माता हैं, और आप ही पिता के समान जगत को समस्त सुख प्रदान करने वाली हैं। आप ही संपूर्ण विश्व का भरण-पोषण करने वाली जगद्धात्री हैं; हे शीतले देवी! मैं आपके श्रीचरणों में बारंबार साष्टांग नमन करता हूँ। समस्त सुखों को देने वाली और समस्त दुखों को हरने वाली हे माँ! आपको नमस्कार है; संसार-सागर से पार उतारने वाली तरणी (नौका) स्वरूपा माँ, आपको प्रणाम है। तीनों लोकों द्वारा वंदनीय, और दुख, दरिद्रता व क्लेशों को समूल उखाड़ फेंकने वाली हे देवी! आपको बारंबार नमस्कार है।

२५-२८. "श्री शीतला, शेढ़ला, महला... जाहि सकल दुख दूर पराई॥"
भावार्थ: लोक-संस्कृति में आपको शीतला, सेढ़ला, महला, रुणली-हुणली और मंदला आदि अनेक पावन नामों से जाना जाता है। आप दिशाओं को ही वस्त्र रूप में धारण करने वाली (दिगम्बरा/निर्मला) हैं और आपकी सवारी गर्दभ (गधा) है जिसे रासभ, खर, वैशाख-सुनंदन, गर्दभ और दूर्वाकंद-निकंदन कहा जाता है। माता शीतला के साथ इस पावन वाहन का स्मरण करने मात्र से भी साधक के समस्त दुख दूर भाग जाते हैं।

२९-३३. "गलका, गलगन्डादि जुहोई... जन्म दरिद्र धनी होई जावै॥"
भावार्थ: गलका, गलगंड (घेंघा/गले की सूजन), फुंसी, फोड़े और त्वचा के अन्य चर्म रोगों के निवारण के लिए संसार में कोई अन्य तंत्र-मंत्र या औषधि काम नहीं आती। केवल और केवल एक माता शीतला जी की आराधना ही इनका परम रामबाण साधन है। जो मनुष्य पूर्ण विश्वास के साथ माता की शरण में आता है, वह निर्भय होकर अपने मनवांछित समस्त फलों को प्राप्त करता है। कोढ़ी व्यक्ति भी माता की कृपा से निर्मल, कंचन जैसी काया प्राप्त कर लेता है; और नेत्रहीन व्यक्ति को दिव्य दृष्टि सुलभ हो जाती है। बंध्या (निःसंतान) स्त्री को सुयोग्य पुत्र रत्न की प्राप्ति होती है और जन्म का दरिद्र मनुष्य भी विपुल धन-धान्य का स्वामी बन जाता है।

३४-३९. "मातु शीतला के गुण गावत... रक्षा करहु शीतला माई॥"
भावार्थ: माता शीतला के अलौकिक गुणों का गान करते ही मूक (गूंगा) व्यक्ति भी सुंदर छंद और कविताएं रचने लगता है। इसमें किसी को भी लेशमात्र संशय नहीं करना चाहिए; क्योंकि इस संपूर्ण संसार में मैया शीतला की शक्ति का ही डंका बजता है। प्रभु के अनन्य दास कवि रामसुन्दर कहते हैं कि तीर्थराज प्रयाग के तट से पूर्व दिशा में, ककरा गंगा तट पर दुर्वासा ऋषि के पावन क्षेत्र में तिवारी पुरी मेरा निवास है। हे माता! मैं अत्यधिक दीन-भाव से आपको पुकार रहा हूँ और आपकी दया-दृष्टि की बाट जोह रहा हूँ। हे माँ शीतला! मैं आपकी शरण में पड़ा हुआ हूँ और आपकी ही आस लगाई है; कृपा करके मेरी सर्वतोभावेन रक्षा कीजिए!

【समापन दोहा】
• "घट-घट वासी शीतला, शीतल प्रभा तुम्हार। शीतल छइयां में झुलई, मइया पलना डार॥"
भावार्थ: हे माता शीतला! आप प्रत्येक घट (हृदय) में निवास करने वाली हैं और आपकी दिव्य प्रभा परम शीतल व शांतिकारी है। हे मैया! अपने वात्सल्य का झूला डालकर मुझे अपनी परम शीतल व पावन छाया में नित्य झुलाती रहिए।"""

vidhi = """॥ श्री शीतला चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल सूर्योदय वेला।
- सर्वोत्तम वार: प्रत्येक मंगलवार (देवी दिन), तथा सोमवार।
- महापर्व व पावन तिथियां: शीतला अष्टमी (बसौड़ा / बासोड़ा — चैत्र मास के कृष्ण पक्ष की अष्टमी तिथि), वैशाख, ज्येष्ठ और आषाढ़ मास के कृष्ण पक्ष की सप्तमी व अष्टमी, तथा चैत्र व शारदीय नवरात्रि।

२. बासोड़ा (बासी भोजन) का विशेष शास्त्रोक्त नियम:
- शीतला अष्टमी के दिन घर में चूल्हा नहीं जलाया जाता (अग्नि प्रज्वलन वर्जित है)।
- एक दिन पूर्व (सप्तमी की सांध्य) को तैयार किया गया भोजन (मीठे चावल/ओलिया, बाजरे की राबड़ी, पूरी, खाजा, हलवा, कढ़ी, दही) ही माता को नैवेद्य के रूप में अर्पित किया जाता है और घर के सभी सदस्य ठंडा (बासी) भोजन ही प्रसाद रूप में ग्रहण करते हैं।

३. दिशा, आसन व वस्त्र:
- दिशा: पूर्व अथवा उत्तर दिशा की ओर मुख करके बैठें।
- आसन: लाल अथवा पीले रंग का स्वच्छ ऊनी आसन बिछाएं।
- वस्त्र: साधक को स्वच्छ लाल, पीले अथवा श्वेत वस्त्र धारण करने चाहिए।

४. दीपक, कलश व नीम पत्र पूजन सामग्री:
- दीपक: गाय के शुद्ध देशी घी का अथवा तिल के तेल का दीपक प्रज्वलित करें।
- कलश: शीतल जल से भरा हुआ तांबे या मिट्टी का कलश स्थापित करें।
- नीम मार्जनी: माता शीतला के पूजन में नीम की टहनी/पत्ते (मार्जनी) अत्यंत अनिवार्य हैं, क्योंकि नीम शीतलता प्रदान करने वाली और समस्त रोगाणुओं का नाश करने वाली महाऔषधि है।
- तिलक: कुंकुम, हल्दी और रोली का तिलक लगाएं।
- प्रिय नैवेद्य: बासी मीठे चावल, दही, राबड़ी, बताशे, खाजा, तथा शीतल जल।

५. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन व पवित्रीकरण करें।
- माता शीतला का ध्यान करें: 'वन्देऽहं शीतलां देवीं रासभस्थां दिगम्बराम्। मार्जनीकलशोपेतां शूर्पालंकृतमस्तकाम्॥'
- शीतला मन्त्र: 'ॐ ह्रीं श्रीं शीतलायै नमः' का कम से कम १ माला (१०८ बार) जप करें।
- इसके पश्चात एकाग्रचित्त होकर 'श्री शीतला चालीसा' का १, ३, अथवा ७ बार पाठ करें।
- पाठ के उपरांत कलश के पावन शीतल जल से घर के सभी सदस्यों एवं पूरे घर में छिड़काव करें और माता शीतला की आरती गाएं।"""

significance = """॥ श्री शीतला चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. विस्फोटक (चेचक, खसरा) व चर्म रोगों से मुक्ति:
"विस्फोटक से जलत शरीरा। शीतल करत हरत सब पीरा॥ भभकत तन, शीतल ह्वै जइहैं। विस्फोटक भयघोर नसइहैं॥"
माता शीतला दाह, ज्वर, त्वचा रोग, चेचक (Smallpox/Chickenpox) और शारीरिक जलन को शांत करने वाली परम देवी हैं। चालीसा के पाठ से शरीर शीतल, निरोगी और कंचन के समान कांतिवान बन जाता है।

२. शिशु एवं बाल-रक्षा (बाल-प्राणरक्षी):
"शोकहरी शंकरी भवानी। बाल-प्राणरक्षी सुख दानी॥"
नवजात शिशुओं और छोटे बच्चों की अकाल व्याधियों, नजर दोष और संक्रामक रोगों से रक्षा होती है। माता शीतला बालकों की प्राण-रक्षिका हैं।

३. मन की शांति व क्रोध-दाह का शमन:
शरीर के साथ-साथ मन में उठने वाले क्रोध, ईर्ष्या, मानसिक तनाव और अशांति की अग्नि को शांत कर यह चालीसा मन को परम शीतलता व शांति प्रदान करती है।

४. संतान सुख व दारिद्र्य नाश:
"वन्ध्या नारि पुत्र को पावै। जन्म दरिद्र धनी होई जावै॥"
निःसंतान स्त्रियों को सुयोग्य संतान और निर्धन साधकों को धन-धान्य की समृद्धि प्राप्त होती है।

५. नेत्र ज्योति व अंग विकार सुधार:
नेत्र विकारों और शारीरिक कष्टों से पीड़ित जातक यदि श्रद्धा से पाठ करें तो उन्हें स्वास्थ्य लाभ और दिव्य दृष्टि की प्राप्ति होती है।"""

english_lyrics = """॥ Shri Shitala Chalisa ॥

॥ Doha ॥
Jaya-Jaya Maataa Sheetalaa, Tumahin Dharai Jo Dhyaana।
Hoya Vimala Sheetala Hridaya, Vikasai Buddhi Bala-Gyaana॥

॥ Chaupai ॥
Jaya-Jaya-Jaya Sheetalaa Bhavaanee। Jaya Jaga Janani Sakala Gunakhaanee॥1॥
Griha-Griha Shakti Tumhaaree Raajita। Poorana Sharadachandra Samasaajita॥2॥
Visphotaka Se Jalata Shareeraa। Sheetala Karata Harata Saba Peeraa॥3॥
Maatu Sheetalaa Tava Shubhanaamaa। Sabake Gaadhe Aavahin Kaamaa॥4॥
Shokaharee Shankaree Bhavaanee। Baala-Praanarakshce Sukha Daanee॥5॥
Shuchi Maarjanee Kalasha Kararaajai। Mastaka Teja Soorya Samaraajai॥6॥
Chausatha Yogina Sanga Men Gaavain। Veenaa Taala Mridanga Bajaavai॥7॥
Nritya Naatha Bhairo Dikharaavain। Sahaja Shesha Shiva Paara Naa Paavain॥8॥
Dhanya-Dhanya Dhaatree Mahaaraanee। Suranara Muni Taba Suyasha Bakhaanee॥9॥
Jvaalaa Roopa Mahaa Balakaaree। Daitya Eka Visphotaka Bhaaree॥10॥
Ghara-Ghara Pravishata Ko-ee Na Rakshata। Roga Roopa Dhari Baalaka Bhakshata॥11॥
Haahaakaara Machyo Jagabhaaree। Sakyo Na Jaba Sankata Taaree॥12॥
Taba Maiyaa Dhari Adbhuta Roopaa। Karamena Liye Maarjanee Soopaa॥13॥
Visphotakahin Pakadi Kara Leenhyo। Musala Prahaara Bahuvidhi Keenhyo॥14॥
Bahuta Prakaara Vaha Vinatee Keenhaa। Maiyaa Naheen Bhala Main Kachhu Cheenhaa॥15॥
Abanaheen Maatu, Kaahugriha Jaihaun। Jahan Apavitra Sakala Duhkha Harihaun॥16॥
Bhabhakata Tana, Sheetala Hvai Jaihain। Visphotaka Bhayaghora Nasaihain॥17॥
Shree Sheetalahin Bhaje Kalyaanaa। Vachana Satya Bhaashe Bhagavaanaa॥18॥
Visphotaka Bhaya Jihi Griha Bhaa-ee। Bhajai Devi Kahan Yahee Upaa-ee॥19॥
Kalasha Sheetalaa Kaa Sajavaavai। Dvija Se Vidhivata Paatha Karaavai॥20॥
Tumheen Sheetalaa, Jaga Kee Maataa। Tumheen Pitaa Jaga Kee Sukhadaataa॥21॥
Tumheen Jagaddhaatree Sukhasevee। Namo Namaami Sheetale Devee॥22॥
Namo Sukkhakaranee Duhkhaharanee। Namo-Namo Jagataarani Taranee॥23॥
Namo-Namo Trailokya Vandinlee। Duhkhadaaridraadika Kandinlee॥24॥
Shree Sheetalaa, Sedhala, Mahalaa। Runaleehunanee Maatu Mandalaa॥25॥
Ho Tuma Digambara Tanudhaaree। Shobhita PanChanaama Asovaaree॥26॥
Raasabha, Khara Baishaakha Sunandana। Gardabha Durvaakanda Nikandana॥27॥
Sumirata Sanga Sheetalaa Maa-ee। Jaahi Sakala Dukha Doora Paraa-ee॥28॥
Galakaa, Galagandaadi Juho-ee। Taakara Mantra Na Aushadhi Ko-ee॥29॥
Eka Maatu Jee Kaa Aaraadhana। Aura Nahin Ko-ee Hai Saadhana॥30॥
Nishchaya Maatu Sharana Jo Aavai। Nirbhaya Mana Ichhita Phala Paavai॥31॥
Kodhee, Nirmala Kaayaa Dhaarai। Andhaa, Driga-Nija Drishti Nihaarai॥32॥
Vandhyaa Naari Putra Ko Paavai। Janma Daridra Dhanee Ho-ee Jaavai॥33॥
Maatu Sheetalaa Ke Guna Gaavata। Lakhaa Mooka Ko Chhanda Banaavata॥34॥
Yaame Ko-ee Karai Jani Shankaa। Jaga Me Maiyaa Kaa Hee Dankaa॥35॥
Bhanata Raamasundara Prabhudaasaa। Tata Prayaaga Se Pooraba Paasaa॥36॥
Puree Tivaaree Mora Nivaasaa। Kakaraa Gangaa Tata Durvaasaa॥37॥
Aba Vilamba Main Tohi Pukaarata। Maatu Kripaa Kau Baata Nihaarata॥38॥
Padaa Kshara Tava Aasa Lagaa-ee। Rakshaa Karahu Sheetalaa Maa-ee॥39॥

॥ Doha ॥
Ghata-Ghata Vaasee Sheetalaa, Sheetala Prabhaa Tumhaara।
Sheetala Chhaiyaan Men Jhula-ee, Maiyaa Palanaa Daara॥"""

# 1. Update drik_chalisa_31 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

for item in cols["devi"]["items"]:
    if item["id"] == "drik_chalisa_31":
        item["title"] = "शीतला माता चालीसा"
        item["title_en"] = "Shitala Mata Chalisa"
        item["en_line"] = "Jai Jai Jai Shitala Bhawani"
        item["hi_line"] = "जय जय जय शीतला भवानी"
        item["sub"] = "जय जय जय शीतला भवानी • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_shitala_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=aKZyXeUZHnM"
        item["video_id"] = "aKZyXeUZHnM"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/shitala-mata/shitala-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "आरोग्य व शीतलता प्रदायिनी भगवती शीतला माता"
        item["section"] = "दिव्य देवी माता चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        break

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_31 in drik_chalisa_collections.json successfully!")

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

# 3. Add or update chalisa_shitala in CONTENT in app.js
content_obj = {
    "title": "श्री शीतला माता चालीसा",
    "title_en": "Shri Shitala Mata Chalisa",
    "en_line": "Jai Jai Jai Shitala Bhawani",
    "hi_line": "जय जय जय शीतला भवानी",
    "sub": "जय जय जय शीतला भवानी • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_shitala_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=aKZyXeUZHnM",
    "video_id": "aKZyXeUZHnM",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/shitala-mata/shitala-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "आरोग्य व शीतलता प्रदायिनी भगवती शीतला माता",
    "section": "दिव्य देवी माता चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

shitala_content_js = "  chalisa_shitala: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_shitala: {" in app_text:
    pos_s = app_text.find("  chalisa_shitala: {")
    pos_next = app_text.find("\n  chalisa_", pos_s + 1)
    if pos_next == -1:
        pos_next = app_text.find("\n  sundarkand:", pos_s + 1)
    app_text = app_text[:pos_s] + shitala_content_js + app_text[pos_next+1:]
    print("Replaced existing chalisa_shitala in CONTENT!")
else:
    # Insert right after chalisa_lalita
    pos_l = app_text.find("  chalisa_lalita: {")
    if pos_l != -1:
        pos_saras = app_text.find("  chalisa_saraswati: {", pos_l)
        if pos_saras != -1:
            app_text = app_text[:pos_saras] + shitala_content_js + app_text[pos_saras:]
            print("Inserted chalisa_shitala after chalisa_lalita in CONTENT!")
        else:
            print("ERROR: Could not find chalisa_saraswati!")
    else:
        print("ERROR: Could not find chalisa_lalita!")

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
