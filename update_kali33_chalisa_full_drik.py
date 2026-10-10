import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

content = """॥ श्री काली चालीसा ॥

॥ दोहा ॥
जय काली जगदम्ब जय, हरनि ओघ अघ पुंज।
वास करहु निज दास के, निशदिन हृदय निकुंज॥
जयति कपाली कालिका, कंकाली सुख दानि।
कृपा करहु वरदायिनी, निज सेवक अनुमानि॥

॥ चौपाई ॥
जय जय जय काली कंकाली। जय कपालिनी, जयति कराली॥१॥
शंकर प्रिया, अपर्णा, अम्बा। जय कपर्दिनी, जय जगदम्बा॥२॥
आर्या, हला, अम्बिका, माया। कात्यायनी उमा जगजाया॥३॥
गिरिजा गौरी दुर्गा चण्डी। दाक्षाणायिनी शाम्भवी प्रचंडी॥४॥
पार्वती मंगला भवानी। विश्वकारिणी सती मृडानी॥५॥
सर्वमंगला शैल नन्दिनी। हेमवती तुम जगत वन्दिनी॥६॥
ब्रह्मचारिणी कालरात्रि जय। महारात्रि जय मोहरात्रि जय॥७॥
तुम त्रिमूर्ति रोहिणी कालिका। कूष्माण्डा कार्तिका चण्डिका॥८॥
तारा भुवनेश्वरी अनन्या। तुम्हीं छिन्नमस्ता शुचिधन्या॥९॥
धूमावती षोडशी माता। बगला मातंगी विख्याता॥१०॥
तुम भैरवी मातु तुम कमला। रक्तदन्तिका कीरति अमला॥११॥
शाकम्भरी कौशिकी भीमा। महातमा अग जग की सीमा॥१२॥
चन्द्रघण्टिका तुम सावित्री। ब्रह्मवादिनी मां गायत्री॥१३॥
रूद्राणी तुम कृष्ण पिंगला। अग्निज्वाला तुम सर्वमंगला॥१४॥
मेघस्वना तपस्विनि योगिनी। सहस्राक्षि तुम अगजग भोगिनी॥१५॥
जलोदरी सरस्वती डाकिनी। त्रिदशेश्वरी अजेय लाकिनी॥१६॥
पुष्टि तुष्टि धृति स्मृति शिव दूती। कामाक्षी लज्जा आहूती॥१७॥
महोदरी कामाक्षि हारिणी। विनायकी श्रुति महा शाकिनी॥१८॥
अजा कर्ममोही ब्रह्माणी। धात्री वाराही शर्वाणी॥१९॥
स्कन्द मातु तुम सिंह वाहिनी। मातु सुभद्रा रहहु दाहिनी॥२०॥
नाम रूप गुण अमित तुम्हारे। शेष शारदा बरणत हारे॥२१॥
तनु छवि श्यामवर्ण तव माता। नाम कालिका जग विख्याता॥२२॥
अष्टादश तब भुजा मनोहर। तिनमहँ अस्त्र विराजत सुन्दर॥२३॥
शंख चक्र अरू गदा सुहावन। परिघ भुशण्डी घण्टा पावन॥२४॥
शूल बज्र धनुबाण उठाए। निशिचर कुल सब मारि गिराए॥२५॥
शुंभ निशुंभ दैत्य संहारे। रक्तबीज के प्राण निकारे॥२६॥
चौंसठ योगिनी नाचत संगा। मद्यपान कीन्हैउ रण गंगा॥२७॥
कटि किंकिणी मधुर नूपुर धुनि। दैत्यवंश कांपत जेहि सुनि-सुनि॥२८॥
कर खप्पर त्रिशूल भयकारी। अहै सदा सन्तन सुखकारी॥२९॥
शव आरूढ़ नृत्य तुम साजा। बजत मृदंग भेरी के बाजा॥३०॥
रक्त पान अरिदल को कीन्हा। प्राण तजेउ जो तुम्हिं न चीन्हा॥३१॥
लपलपाति जिव्हा तव माता। भक्तन सुख दुष्टन दुःख दाता॥३२॥
लसत भाल सेंदुर को टीको। बिखरे केश रूप अति नीको॥३३॥
मुंडमाल गल अतिशय सोहत। भुजामल किंकण मनमोहन॥३४॥
प्रलय नृत्य तुम करहु भवानी। जगदम्बा कहि वेद बखानी॥३५॥
तुम मशान वासिनी कराला। भजत तुरत काटहु भवजाला॥३६॥
बावन शक्ति पीठ तव सुन्दर। जहाँ बिराजत विविध रूप धर॥३७॥
विन्धवासिनी कहूँ बड़ाई। कहँ कालिका रूप सुहाई॥३८॥
शाकम्भरी बनी कहँ ज्वाला। महिषासुर मर्दिनी कराला॥३९॥
कामाख्या तव नाम मनोहर। पुजवहिं मनोकामना द्रुततर॥४०॥
चंड मुंड वध छिन महं करेउ। देवन के उर आनन्द भरेउ॥४१॥
सर्व व्यापिनी तुम माँ तारा। अरिदल दलन लेहु अवतारा॥४२॥
खलबल मचत सुनत हुँकारी। अगजग व्यापक देह तुम्हारी॥४३॥
तुम विराट रूपा गुणखानी। विश्व स्वरूपा तुम महारानी॥४४॥
उत्पत्ति स्थिति लय तुम्हरे कारण। करहु दास के दोष निवारण॥४५॥
माँ उर वास करहू तुम अंबा। सदा दीन जन की अवलंबा॥४६॥
तुम्हारो ध्यान धरै जो कोई। ता कहँ भीति कतहुँ नहिं होई॥४७॥
विश्वरूप तुम आदि भवानी। महिमा वेद पुराण बखानी॥४८॥
अति अपार तव नाम प्रभावा। जपत न रहन रंच दुःख दावा॥४९॥
महाकालिका जय कल्याणी। जयति सदा सेवक सुखदानी॥५०॥
तुम अनन्त औदार्य विभूषण। कीजिए कृपा क्षमिये सब दूषण॥५१॥
दास जानि निज दया दिखावहु। सुत अनुमानित सहित अपनावहु॥५२॥
जननी तुम सेवक प्रति पाली। करहु कृपा सब विधि माँ काली॥५३॥
पाठ करै चालीसा जोई। तापर कृपा तुम्हारी होई॥५४॥

॥ दोहा ॥
जय तारा, जय दक्षिणा, कलावती सुखमूल।
शरणागत 'भक्त' है, रहहु सदा अनुकूल॥"""

meaning = """॥ श्री काली चालीसा — पद्यवार सम्पूर्ण पावन भावार्थ ॥

【प्रारम्भिक दोहे】
• "जय काली जगदम्ब जय, हरनि ओघ अघ पुंज। वास करहु निज दास के, निशदिन हृदय निकुंज॥"
भावार्थ: हे माँ काली! हे जगदम्बा! आपकी सदा सर्वदा जय हो। आप पापों, तापों और संतापों के घने समूह (ओघ अघ पुंज) का समूल हरण करने वाली हैं। हे करुणामयी जननी! अपने इस दीन दास के हृदय रूपी पावन निकुंज में आप दिन-रात (निशदिन) सदैव वास कीजिए।

• "जयति कपाली कालिका, कंकाली सुख दानि। कृपा करहु वरदायिनी, निज सेवक अनुमानि॥"
भावार्थ: हे कपाली, हे कालिका, हे कंकाली! आपकी जय हो, आप अपने भक्तों को परम आनंद व सुख प्रदान करने वाली हैं। हे समस्त वरदानों को देने वाली वरदायिनी माँ! मुझे अपना अनन्य सेवक व बालक जानकर मुझ पर अपनी अहैतुकी कृपा दृष्टि बनाए रखिए।

【चौपाइयां — पद्यवार भावार्थ】
१-१०. "जय जय जय काली कंकाली... बगला मातंगी विख्याता॥"
भावार्थ: हे माँ काली, कंकाली, कपालिनी और कराली! आपकी जय हो, जय हो, जय हो; आप दुष्टों के लिए संहारिणी और भक्तों के लिए परम कल्याणी हैं। आप देवाधिदेव भगवान शंकर की परम प्रिया, घोर तपस्या करने वाली अपर्णा, जगदम्बा और कपर्दिनी (जटाजूट धारिणी) हैं। आप ही आर्या, हला, अम्बिका, महामाया, कात्यायनी और उमा के रूप में संपूर्ण जगत की जननी हैं। आप गिरिराज किशोरी गिरिजा, गौरी, संहारकारिणी दुर्गा, चण्डी, दक्ष-पुत्री दाक्षायणी, शाम्भवी और प्रचण्ड पराक्रम वाली शक्ति हैं। आप पार्वती, मंगलमयी भवानी, विश्व की उत्पत्ति करने वाली विश्वकारिणी, सती और शिवप्रिया मृडानी हैं। आप सर्वमंगला, शैलपुत्री शैलनन्दिनी, हेमवती और समस्त चराचर जगत द्वारा नित्य वन्दनीया हैं। ब्रह्मचारिणी, कालरात्रि, महारात्रि और मोहरात्रि के रूप में आपकी सदा जय हो। आप त्रिदेवों की मूल त्रिमूर्ति, रोहिणी, कालिका, कूष्माण्डा, कार्तिका और महाचण्डिका हैं। दस महाविद्याओं में आप ही तारा, अनुपम भुवनेश्वरी, परम पवित्र व धन्य छिन्नमस्ता, धूमावती, षोडशी (त्रिपुर सुन्दरी), बगलामुखी और मातंगी के नाम से सर्वत्र विख्यात हैं।

११-२०. "तुम भैरवी मातु तुम कमला... मातु सुभद्रा रहहु दाहिनी॥"
भावार्थ: महाविद्याओं में आप ही भैरवी, कमला (महालक्ष्मी), और निर्मल कीर्ति वाली रक्तदन्तिका हैं। आप ही शाकम्भरी, कौशिकी, भीमा, और अंधकार का नाश करने वाली अगम-सृष्टि की परम सीमा हैं। आप चन्द्रघण्टा, सूर्य-स्वरूपा सावित्री, ब्रह्मज्ञान का उपदेश देने वाली ब्रह्मवादिनी माँ गायत्री हैं। आप रूद्राणी, कृष्ण-पिंगला, धधकती अग्निज्वाला और सर्वकल्याणमयी सर्वमंगला हैं। मेघों के समान गंभीर गर्जना करने वाली मेघस्वना, परम तपस्विनी योगिनी, सहस्रों नेत्रों से विश्व को निहारने वाली सहस्राक्षी और संपूर्ण जगत का भोग व मोक्ष देने वाली हैं। जलोदरी, ज्ञानदायिनी सरस्वती, डाकिनी, देवताओं की ईश्वरी त्रिदशेश्वरी और अजेय लाकिनी आप ही हैं। पुष्टि (पोषण), तुष्टि (संतोष), धृति (धैर्य), स्मृति (स्मरण शक्ति), शिवदूती, कामाक्षी, लज्जा और यज्ञों की आहुति आप ही हैं। महोदरी, काम-इच्छाओं का हरण करने वाली कामहारिणी, विनायकी (गणेश-शक्ति), श्रुति (वेद) और महा शाकिनी आपका ही स्वरूप हैं। आप अजन्मा अजा, कर्म-मोह को हरने वाली ब्रह्माणी, सृष्टि का पोषण करने वाली धात्री, वराह-शक्ति वाराही और शिवप्रिया शर्वाणी हैं। आप स्कन्दमाता और सिंहवाहिनी हैं; हे माता सुभद्रा! आप सदा मेरे दाहिने रहकर मेरी रक्षा कीजिए।

२१-३१. "नाम रूप गुण अमित तुम्हारे... प्राण तजेउ जो तुम्हिं न चीन्हा॥"
भावार्थ: हे माता! आपके पावन नाम, अलौकिक रूप और दिव्य गुण असीम व अनंत हैं; स्वयं सहस्रमुख शेषनाग और विद्या की देवी शारदा भी आपकी महिमा का संपूर्ण वर्णन करने में पार नहीं पा सके। हे माता! आपका दिव्य वर्ण सघन श्याम (नील-श्याम) है और आप संपूर्ण जगत में 'कालिका' के नाम से विख्यात हैं। आपकी अठारह (अष्टादश) मनोहर भुजाएं हैं, जिनमें परम सुंदर व तेजस्वी दिव्य अस्त्र-शस्त्र सुशोभित हैं। आपके कर-कमलों में शंख, सुदर्शन चक्र, गदा, परिघ, भुशुण्डी और पावन घण्टा विराजमान है। आपने त्रिशूल, वज्र और धनुष-बाण उठाकर संपूर्ण राक्षस कुल का संहार कर उन्हें रणभूमि में मार गिराया। आपने शुंभ और निशुंभ जैसे महादैत्यों का वध किया और रक्तबीज के एक-एक रक्त बिंदु को पीकर उसके प्राण हर लिए। रणभूमि में चौंसठ योगिनियां आपके संग उन्मत्त होकर नृत्य कर रही थीं और आपने रण-गंगा में असुरों के मद का पान किया। आपकी कमर में बंधी करधनी (किंकिणी) और पैरों के नूपुरों की मधुर झंकार सुनकर दैत्यों के वंश भय से कांप उठते हैं। आपके हाथों में नर-कपाल (खप्पर) और भयकारी त्रिशूल है, जो दुष्टों के लिए प्रलयंकारी है किन्तु संतों और भक्तों के लिए सदा परम सुखकारी है। आपने शव (शिव) पर आरूढ़ होकर तांडव नृत्य रचाया, जहां मृदंग और भेरी जैसे रणवाद्य बज रहे थे। आपने शत्रु-दल के रक्त का पान किया; जिसने भी आपकी पराशक्ति को नहीं पहचाना, उसने अपने प्राण गंवा दिए।

३२-४१. "लपलपाति जिव्हा तव माता... देवन के उर आनन्द भरेउ॥"
भावार्थ: हे माता! आपकी लपलपाती लाल जिह्वा भक्तों को अभय व सुख देने वाली और दुष्टों को दारुण दुख देने वाली है। आपके सुंदर ललाट पर सिन्दूर का लाल तिलक सुशोभित है और आपके बिखरे हुए काले घुंघराले केश अत्यंत मनोहारी हैं। आपके गले में मुंडों की माला अतिशय शोभा पा रही है और आपकी बाहुओं पर किंकण (कंगन) मन को मोहित करने वाले हैं। हे भवानी! आप महाप्रलय के समय संहारक तांडव नृत्य करती हैं, वेदों ने आपकी स्तुति में आपको ही परम जगदम्बा कहा है। आप श्मशान में निवास करने वाली कराला हैं, जो भी आपका स्मरण करता है, आप उसके जन्म-मरण रूपी संसार के बंधन (भवजाल) को तुरंत काट देती हैं। इस पावन धरा पर आपके बावन (५२) सुंदर शक्तिपीठ प्रतिष्ठित हैं, जहाँ आप विविध अलौकिक रूपों में विराजमान हैं। कहीं आप विंध्यवासिनी के रूप में पूजी जाती हैं, तो कहीं आपका कालिका रूप मन को मोह लेता है। कहीं आप शाकम्भरी बनी हैं, तो कहीं ज्वाला देवी और कहीं महिषासुर मर्दिनी के रूप में प्रकट हुई हैं। कामरूप में आपका 'कामाख्या' नाम अत्यंत मनोहर है, जो भक्तों की मनोकामनाओं को अत्यंत शीघ्र (द्रुततर) पूरा करता है। आपने चंड और मुंड दैत्यों का क्षण भर में वध कर दिया और समस्त देवताओं के हृदय में परमानंद भर दिया।

४२-५४. "सर्व व्यापिनी तुम माँ तारा... तापर कृपा तुम्हारी होई॥"
भावार्थ: हे माँ! आप सर्वव्यापिनी माँ तारा हैं; शत्रुओं के दल का दलन करने के लिए आप समय-समय पर अवतार लेती हैं। आपकी एक प्रचंड हुंकार सुनते ही दसों दिशाओं में खलबली मच जाती है; आपका विराट शरीर इस चराचर जगत में व्याप्त है। आप अनंत गुणों की खान और विराट रूपा हैं; आप ही इस संपूर्ण विश्व की स्वामिनी महारानी हैं। इस सृष्टि की उत्पत्ति, स्थिति (पालन) और लय (प्रलय) सब आपके ही अधीन हैं; हे माँ! मुझ दीन दास के समस्त दोषों का निवारण कीजिए। हे जगदम्बा! आप सदा मेरे हृदय में वास कीजिए, आप ही हम दीन-हीन जनों का एकमात्र सहारा (अवलंब) हैं। जो कोई भी मनुष्य आपका ध्यान धरता है, उसे संसार में किसी भी वस्तु या संकट से कभी कोई भय नहीं रहता। आप आदि भवानी और विश्वस्वरूपा हैं, आपकी दिव्य महिमा का वेदों और पुराणों ने मुक्तकंठ से बखान किया है। आपके पावन नाम का प्रभाव अत्यंत अपार है; इसका स्मरण-जप करते ही दुख और दावानल का लेशमात्र अंश भी शेष नहीं रहता। हे महाकालिका! हे कल्याणी! आपकी सदा जय हो; आप अपने सेवकों को सदा-सदा सुख देने वाली हैं। अनंत उदारता और क्षमा आपका स्वाभाविक आभूषण है; कृपा करके मुझ पर दया कीजिए और मेरे सभी अपराधों व दूषणों को क्षमा कर दीजिए। मुझे अपना अनन्य सेवक जानकर दया दिखाइए और अपने पुत्र के समान मानकर मुझे अपनी शरण में अपना लीजिए। हे जननी! आप ही अपने सेवकों का पालन-पोषण करने वाली हैं; हे माँ काली! सब प्रकार से मुझ पर अपनी अहैतुकी कृपा कीजिए। जो भी व्यक्ति श्रद्धा और भक्ति से इस पावन चालीसा का नित्य पाठ करता है, उस पर आपकी परम कृपा नित्य बनी रहती है।

【समापन दोहा】
• "जय तारा, जय दक्षिणा, कलावती सुखमूल। शरणागत 'भक्त' है, रहहु सदा अनुकूल॥"
भावार्थ: हे माँ तारा! हे दक्षिणा कालिका! हे कलावती! आप ही समस्त आनंद और सुखों की मूल कारण हैं। आपका यह 'भक्त' आपकी पावन शरण में पड़ा हुआ है; हे माँ! आप उस पर सदा-सदा अनुकूल (प्रसन्न) रहिए।"""

vidhi = """॥ श्री काली चालीसा — शास्त्रोक्त प्रामाणिक पाठ विधि व नियम ॥

१. पाठ का सर्वोत्तम समय व पावन तिथियां:
- नित्य समय: प्रातःकाल ब्रह्ममुहूर्त अथवा सांध्यकाल (प्रदोष काल / रात्रि काल — काली साधना हेतु निशीथ काल विशेष फलदायी माना गया है)।
- सर्वोत्तम वार: मंगलवार एवं शनिवार (भगवती काली एवं कालभैरव पूजन के सर्वश्रेष्ठ दिन)।
- महापर्व व पावन तिथियां: नरक चतुर्दशी/दीपावली (कालरात्रि महानिशा), प्रत्येक मास की कृष्ण पक्ष की अमावस्या, गुप्त एवं प्रकट नवरात्रि (विशेषकर महाष्टमी व महानवमी), तथा तारा रात्रि।

२. दिशा, आसन व वस्त्र:
- दिशा: पूर्व अथवा दक्षिण दिशा की ओर मुख करके बैठें (दक्षिण काली साधना में दक्षिणमुखी होना शास्त्रसम्मत है)।
- आसन: लाल अथवा काले रंग का स्वच्छ ऊनी आसन या कुशासन बिछाएं।
- वस्त्र: साधक को लाल अथवा गहरे रंग के शुद्ध, धुले हुए सूती/ऊनी वस्त्र धारण करने चाहिए।

३. दीपक, पुष्प व नैवेद्य पूजन सामग्री:
- दीपक: सरसों के तेल का अथवा शुद्ध देशी घी का दीपक प्रज्वलित करें।
- प्रिय पुष्प: माता काली को गुड़हल (लाल जबा-कुसुम) के ताजे लाल पुष्प अथवा १०८ गुड़हल के फूलों की माला अत्यंत प्रिय है।
- तिलक: रक्त चंदन, कुंकुम, रोली, और सिन्दूर का तिलक लगाएं।
- प्रिय नैवेद्य: हलवा-पूरी, खीर, अनार, काले अंगूर, बताशे, लौंग का जोड़ा, पान का बीड़ा और नारियल का भोग लगाएं।

४. प्रामाणिक पाठ क्रम:
- सर्वप्रथम आचमन, पवित्रीकरण एवं संकल्प करें।
- माँ काली का ध्यान करें:
  'ॐ खड्गं चक्रगदेषुचापपरिघाञ्छूलं भुशुण्डीं शिरः शङ्खं संदधतीं करैस्त्रिनयनां सर्वाङ्गभूषावृताम्।
   नीलाश्मद्युतिमास्यपाददशकां सेवे महाकालिकां यामस्तौत्स्वपिते हरौ कमलजो हन्तुं मधुं कैटभम्॥'
- काली एकाक्षरी अथवा नर्वाण मन्त्र का १०८ बार जप करें: 'ॐ क्रीं कालिकायै नमः' अथवा 'ॐ ऐं ह्रीं क्लीं चामुण्डायै विच्चे'।
- इसके पश्चात पूर्ण श्रद्धा एवं एकाग्रता से 'श्री काली चालीसा' का १, ३, ७ अथवा ११ बार पाठ करें।
- पाठ के उपरांत कर्पूर से आरती करें और अनजाने में हुई भूलों के लिए क्षमा-प्रार्थना करें।"""

significance = """॥ श्री काली चालीसा — आध्यात्मिक माहात्म्य व फलश्रुति ॥

१. शत्रु-बाधा, षड्यंत्र व विरोधी दमन:
"अरिदल दलन लेहु अवतारा... रक्त पान अरिदल को कीन्हा॥"
माँ काली दुष्टों और आसुरी शक्तियों का नाश करने वाली महाशक्ति हैं। चालीसा के पाठ से प्रत्यक्ष और अप्रत्यक्ष शत्रुओं के समस्त षड्यंत्र निष्फल हो जाते हैं और साधक सर्वत्र निर्भय व विजयी होता है।

२. तंत्र-मंत्र, नजर दोष व नकारात्मक शक्तियों से पूर्ण रक्षा:
"तुम मशान वासिनी कराला। भजत तुरत काटहु भवजाला॥"
घर, परिवार अथवा व्यापार स्थल पर किसी भी प्रकार का नजर-दोष, ऊपरी बाधा, नकारात्मक ऊर्जा या तंत्र-मंत्र का कुप्रभाव हो, काली चालीसा का पाठ अभेद्य दिव्य रक्षा-कवच का निर्माण करता है।

३. अकाल मृत्यु, दुर्घटना व भय का समूल निवारण:
"तुम्हारो ध्यान धरै जो कोई। ता कहँ भीति कतहुँ नहिं होई॥"
माता कालिका का ध्यान करने वाले साधक को मृत्यु-भय, दुर्घटना अथवा अंधकार का कोई भय नहीं सताता; महाकाल की शक्ति कालरात्रि स्वयं उसकी रक्षा करती हैं।

४. शनि की साढ़ेसाती, ढैय्या व राहु-केतु ग्रह शांति:
माता कालिका की उपासना से शनिदेव, राहु और केतु जैसे क्रूर ग्रहों के दुष्प्रभाव शांत हो जाते हैं और जीवन के अवरोध समाप्त होकर स्थिरता व समृद्धि आती है।

५. आत्मबल, कुण्डलिनी जागरण व मनोकामना सिद्धि:
"बावन शक्ति पीठ तव सुन्दर... पुजवहिं मनोकामना द्रुततर॥"
साधक को असीम आत्मबल, ओज, तेज, मानसिक दृढ़ता और आध्यात्मिक चेतना प्राप्त होती है तथा मनवांछित कार्यों में शीघ्र सफलता मिलती है।"""

english_lyrics = """॥ Shri Kali Chalisa ॥

॥ Doha ॥
Jaya Kaalee Jagadamba Jaya, Harani Ogha Agha Punja।
Vaasa Karahu Nija Daasa Ke, Nishadina Hridaya Nikunja॥
Jayati Kapaalee Kaalikaa, Kankaalee Sukha Daani।
Kripaa Karahu Varadaayinee, Nija Sevaka Anumaani॥

॥ Chaupai ॥
Jaya Jaya Jaya Kaalee Kankaalee। Jaya Kapaalinee, Jayati Karaalee॥1॥
Shankara Priyaa, Aparnaa, Ambaa। Jaya Kapardinee, Jaya Jagadambaa॥2॥
Aaryaa, Halaa, Ambikaa, Maayaa। Kaatyaayanee Umaa Jagajaayaa॥3॥
Girijaa Gauree Durgaa Chandee। Daakshaanaayinee Shaambhavee Prachandee॥4॥
Paarvatee Mangalaa Bhavaanee। Vishvakaarinee Satee Mridaanee॥5॥
Sarvamangalaa Shaila Nandinee। Hemavatee Tuma Jagata Vandinee॥6॥
Brahmachaarinee Kaalaraatri Jaya। Mahaaraatri Jaya Moharaatri Jaya॥7॥
Tuma Trimoorti Rohinee Kaalikaa। Kooshmaandaa Kaartikaa Chandikaa॥8॥
Taaraa Bhuvaneshwaree Ananyaa। Tumheen Chhinnamastaa Shuchidhanyaa॥9॥
Dhoomaavatee Shodhashee Maataa। Bagalaa Maatangee Vikhyaataa॥10॥
Tuma Bhairavee Maatu Tuma Kamalaa। Raktadantikaa Keerati Amalaa॥11॥
Shaakambharee Kaushikee Bheemaa। Mahaatamaa Aga Jaga Kee Seemaa॥12॥
Chandraghantikaa Tuma Saavitree। Brahmavaadinee Maan Gaayatree॥13॥
Roodraanee Tuma Krishna Pingalaa। Agnijvaalaa Tuma Sarvamangalaa॥14॥
Meghaswanaa Tapaswini Yoginee। Sahasraakshi Tuma Agajaga Bhoginee॥15॥
Jalodaree Saraswatee Daakinee। Tridasheshwaree Ajeya Laakinee॥16॥
Pushti Tushti Dhriti Smriti Shiva Dootee। Kaamaakshee Lajjaa Aahootee॥17॥
Mahodaree Kaamaakshi Haarinee। Vinaayakee Shruti Mahaa Shaakinee॥18॥
Ajaa Karmamohee Brahmaanee। Dhaatree Vaaraahee Sharvaanee॥19॥
Skanda Maatu Tuma Sinha Vaahinee। Maatu Subhadraa Rahahu Daahinee॥20॥
Naama Roopa Guna Amita Tumhaare। Shesha Shaaradaa Baranata Haare॥21॥
Tanu Chhavi Shyaamavarna Tava Maataa। Naama Kaalikaa Jaga Vikhyaataa॥22॥
Ashtaadasha Taba Bhujaa Manohara। Tinamahan Astra Viraajata Sundara॥23॥
Shankha Chakra Aroo Gadaa Suhaavana। Parigha Bhushandee Ghantaa Paavana॥24॥
Shoola Bajra Dhanubaana Uthaa-e। Nishichara Kula Saba Maari Giraa-e॥25॥
Shumbha Nishumbha Daitya Sanhaare। Raktabeeja Ke Praana Nikaare॥26॥
Chaunsatha Yoginee Naachata Sangaa। Madyapaana Keenhai-u Rana Gangaa॥27॥
Kati Kinkinee Madhura Noopura Dhuni। Daityavansha Kaanpata Jehi Suni-Suni॥28॥
Kara Khappara Trishoola Bhayakaaree। Ahai Sadaa Santana Sukhakaaree॥29॥
Shava Aaroodha Nritya Tuma Saajaa। Bajata Mridanga Bheree Ke Baajaa॥30॥
Rakta Paana Aridala Ko Keenhaa। Praana Taje-u Jo Tumhin Na Cheenhaa॥31॥
Lapalapaati Jivhaa Tava Maataa। Bhaktana Sukha Dushtana Duhkha Daataa॥32॥
Lasata Bhaala Sendura Ko Teeko। Bikhare Kesha Roopa Ati Neeko॥33॥
Mundamaala Gala Atishaya Sohata। Bhujaamala Kinkana Manamohana॥34॥
Pralaya Nritya Tuma Karahu Bhavaanee। Jagadambaa Kahi Veda Bakhaanee॥35॥
Tuma Mashaana Vaasinee Karaalaa। Bhajata Turata Kaatahu Bhavajaalaa॥36॥
Baavana Shakti Peetha Tava Sundara। Jahaan Biraajata Vividha Roopa Dhara॥37॥
Vindhyavaasinee Kahoong Badaa-ee। Kahan Kaalikaa Roopa Suhaa-ee॥38॥
Shaakambharee Baneen Kahan Jvaalaa। Mahishaasura Mardinee Karaalaa॥39॥
Kaamaakhyaa Tava Naama Manohara। Pujavahin Manokaamanaa Drutatara॥40॥
Chanda Munda Vadha Chhina Mahan Kare-u। Devana Ke Ura Aananda Bhare-u॥41॥
Sarva Vyaapinee Tuma Maan Taaraa। Aridala Dalana Lehu Avataaraa॥42॥
Khalabala Machata Sunata Hünkaaree। Agajaga Vyaapaka Deha Tumhaaree॥43॥
Tuma Viraata Roopaa Gunakhaanee। Vishwa Swaroopaa Tuma Mahaaraanee॥44॥
Utpatti Sthiti Laya Tumhare Kaarana। Karahu Daasa Ke Dosha Nivaarana॥45॥
Maan Ura Vaasa Karahoo Tuma Ambaa। Sadaa Deena Jana Kee Avalambaa॥46॥
Tumhaaro Dhyaana Dharai Jo Ko-ee। Taa Kahan Bheeti Katahoon Nahin Ho-ee॥47॥
Vishwaroopa Tuma Aadi Bhavaanee। Mahimaa Veda Puraana Bakhaanee॥48॥
Ati Apaara Tava Naama Prabhaavaa। Japata Na Rahana Rancha Duhkha Daavaa॥49॥
Mahaakaalikaa Jaya Kalyaanee। Jayati Sadaa Sevaka Sukhadaanee॥50॥
Tuma Ananta Audaarya Vibhooshana। Keejiye Kripaa Kshamiye Saba Dooshana॥51॥
Daasa Jaani Nija Dayaa Dikhaavahu। Suta Anumaanita Sahita Apanaavahu॥52॥
Jananee Tuma Sevaka Prati Paalee। Karahu Kripaa Saba Vidhi Maan Kaalee॥53॥
Paatha Karai Chaaleesaa Jo-ee। Taapara Kripaa Tumhaaree Ho-ee॥54॥

॥ Doha ॥
Jaya Taaraa, Jaya Dakshinaa, Kalaavatee Sukhamoola।
Sharanaagata 'Bhakta' Hai, Rahahu Sadaa Anukoola॥"""

# 1. Update drik_chalisa_33 in drik_chalisa_collections.json
with open("drik_chalisa_collections.json", "r", encoding="utf-8") as f:
    cols = json.load(f)

found = False
for item in cols["devi"]["items"]:
    if item["id"] == "drik_chalisa_33":
        item["title"] = "काली माता चालीसा"
        item["title_en"] = "Kali Mata Chalisa"
        item["en_line"] = "Jai Jai Jai Kali Kapali"
        item["hi_line"] = "जय जय जय काली कपाली"
        item["sub"] = "जय जय जय काली कपाली • Drik Panchang Verified"
        item["thumb"] = "assets/gallery/bal_kali_little.jpg"
        item["audio_url"] = "https://www.youtube.com/watch?v=ty_BRH3b9lY"
        item["video_id"] = "ty_BRH3b9lY"
        item["drik_url"] = "https://www.drikpanchang.com/lyrics/chalisa/kali-mata/kali-mata-chalisa.html?lang=hi&ck=1"
        item["source"] = "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)"
        item["deity"] = "शत्रुनाशिनी भयहारिणी भगवती महाकाली माता"
        item["section"] = "दिव्य देवी माता चालीसा संग्रह"
        item["content"] = content
        item["meaning"] = meaning
        item["vidhi"] = vidhi
        item["significance"] = significance
        item["english_lyrics"] = english_lyrics
        found = True
        break

if not found:
    print("ERROR: drik_chalisa_33 not found in devi category!")
    sys.exit(1)

with open("drik_chalisa_collections.json", "w", encoding="utf-8") as f:
    json.dump(cols, f, ensure_ascii=False, indent=2)
print("Updated drik_chalisa_33 in drik_chalisa_collections.json successfully!")

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

# 3. Add or update chalisa_kali in CONTENT in app.js
content_obj = {
    "title": "श्री काली माता चालीसा",
    "title_en": "Shri Kali Mata Chalisa",
    "en_line": "Jai Jai Jai Kali Kapali",
    "hi_line": "जय जय जय काली कपाली",
    "sub": "जय जय जय काली कपाली • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_kali_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=ty_BRH3b9lY",
    "video_id": "ty_BRH3b9lY",
    "drik_url": "https://www.drikpanchang.com/lyrics/chalisa/kali-mata/kali-mata-chalisa.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "deity": "शत्रुनाशिनी भयहारिणी भगवती महाकाली माता",
    "section": "दिव्य देवी माता चालीसा संग्रह",
    "content": content,
    "meaning": meaning,
    "vidhi": vidhi,
    "significance": significance,
    "english_lyrics": english_lyrics
}

kali_content_js = "  chalisa_kali: " + json.dumps(content_obj, ensure_ascii=False, indent=4) + ",\n"

if "  chalisa_kali: {" in app_text:
    pos_s = app_text.find("  chalisa_kali: {")
    pos_next = app_text.find("\n  chalisa_", pos_s + 1)
    if pos_next == -1:
        pos_next = app_text.find("\n  sundarkand:", pos_s + 1)
    app_text = app_text[:pos_s] + kali_content_js + app_text[pos_next+1:]
    print("Replaced existing chalisa_kali in CONTENT!")
else:
    # Insert right before chalisa_saraswati (after chalisa_shitala)
    pos_saras = app_text.find("  chalisa_saraswati: {")
    if pos_saras != -1:
        app_text = app_text[:pos_saras] + kali_content_js + app_text[pos_saras:]
        print("Inserted chalisa_kali before chalisa_saraswati in CONTENT!")
    else:
        # fallback: insert before sundarkand
        pos_sun = app_text.find("  sundarkand: {")
        if pos_sun != -1:
            app_text = app_text[:pos_sun] + kali_content_js + app_text[pos_sun:]
            print("Inserted chalisa_kali before sundarkand in CONTENT!")
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

print("ALL UPDATES COMPLETED!")
