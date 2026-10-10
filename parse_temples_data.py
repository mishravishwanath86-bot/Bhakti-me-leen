import re, sys, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")

# The user prompt text containing all parts
raw_data = """
भाग 1: भारत के महत्वपूर्ण मंदिर (The Soul of India)
1. महाकालेश्वर ज्योतिर्लिंग (Mahakaleshwar Jyotirlinga)
स्थान: [Ujjain, Madhya Pradesh](https://www.google.com/maps/search/?api=1&query=Mahakaleshwar+Temple+Ujjain&authuser=4)
प्रसिद्ध: 'दक्षिणमुखी' ज्योतिर्लिंग और विश्व प्रसिद्ध भस्म आरती।
भोजन/प्रसाद: पेड़ा प्रसाद, उज्जैनी पोहा-जलेबी, दाल-बाफला।
AI Image Prompt: "An atmospheric, highly detailed photorealistic image of the Mahakaleshwar Temple in Ujjain at dawn, showing the sacred Shikhara bathed in golden light, smoke rising from the holy fire, traditional oil lamps, 8k resolution, cinematic lighting."
2. काशी विश्वनाथ मंदिर (Kashi Vishwanath Temple)
स्थान: [Varanasi, Uttar Pradesh](https://www.google.com/maps/search/?api=1&query=Kashi+Vishwanath+Temple+Varanasi&authuser=4)
प्रसिद्ध: भगवान शिव का सबसे पवित्र धाम, मोक्षदायिनी काशी का हृदय।
भोजन/प्रसाद: बनारसी पेड़ा, मलइयो, कचौरी-जलेबी, लस्सी।
AI Image Prompt: "A realistic, deep blue hour shot of the Kashi Vishwanath Temple in Varanasi, the glowing golden spire reflecting in a wet marble pathway, traditional oil lamps, spiritual atmosphere, ultra-detailed 8k photography."
3. सोमनाथ मंदिर (Somnath Temple)
स्थान: [Prabhas Patan, Gujarat](https://www.google.com/maps/search/?api=1&query=Somnath+Temple+Prabhas+Patan+Gujarat&authuser=4)
प्रसिद्ध: भारत का 'प्रथम' ज्योतिर्लिंग, अरब सागर के तट पर स्थित।
भोजन/प्रसाद: बेसन लड्डू प्रसाद, गुजराती दाल-ढोकली, खमण-ढोकला.
AI Image Prompt: "Majestic Somnath Temple standing right on the Arabian Sea coast, photorealistic, dramatic crashing waves, golden sunset light illuminating the intricate sandstone architecture, hyper-detailed 8k rendering."
4. जगन्नाथ मंदिर (Jagannath Temple)
स्थान: [Puri, Odisha](https://www.google.com/maps/search/?api=1&query=Shri+Jagannath+Temple+Puri+Odisha&authuser=4)
प्रसिद्ध: चार धामों में से एक और विश्व प्रसिद्ध रथ यात्रा।
भोजन/प्रसाद: छप्पन भोग (महाप्रसाद), खाजा मिठाई, दालमा।
AI Image Prompt: "A highly accurate realistic wide-angle view of the Jagannath Temple in Puri, showing the iconic main spire with the flag fluttering, the grand Lion Gate, bustling temple courtyard, divine atmosphere, 8k professional photography."
5. रामनाथस्वामी मंदिर (Ramanathaswamy Temple)
स्थान: [Rameswaram, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Ramanathaswamy+Temple+Rameswaram&authuser=4)
प्रसिद्ध: दक्षिण का चार धाम तीर्थ और विश्व का सबसे लंबा मंदिर गलियारा।
भोजन/प्रसाद: पंचामृत, रसम सादम, मदुरै-शैली की दक्षिण भारतीय थाली।
AI Image Prompt: "A stunningly realistic, symmetrical photo down the infinite grand pillared corridor of Ramanathaswamy Temple, Rameswaram, thousands of intricate carved columns, glowing oil lamps, spiritual depth, photorealistic 8k."
6. स्वर्ण मंदिर / हरमंदिर साहिब (Golden Temple)
स्थान: [Amritsar, Punjab](https://www.google.com/maps/search/?api=1&query=Golden+Temple+Amritsar&authuser=4)
प्रसिद्ध: शुद्ध सोने से मढ़ा पवित्र गुरुद्वारा, शांति और लंगर का केंद्र।
भोजन/प्रसाद: कड़ा प्रसाद (देसी घी का हलवा), लंगर, अमृतसरी कुलचा.
AI Image Prompt: "Gleaming pure gold Golden Temple reflecting perfectly in the sacred sarovar lake at twilight, soft magical lighting, marble walkway, spiritual aura, hyper-realistic, 8k resolution masterwork."
7. खजुराहो के मंदिर (Khajuraho Temples)
स्थान: [Chhatarpur, Madhya Pradesh](https://www.google.com/maps/search/?api=1&query=Khajuraho+Group+of+Monuments&authuser=4)
प्रसिद्ध: यूनेस्को धरोहर स्थल, अपनी विस्तृत और जटिल कामुक मूर्तियों के लिए प्रसिद्ध।
भोजन/प्रसाद: बुंदेली भोजन, मवेशी की खीर।
AI Image Prompt: "Highly detailed realistic view of the Kandariya Mahadeva Temple at Khajuraho, sandstone architecture catching dramatic sunset rays, intricate sculptures of figures, hyper-accurate textures, photorealistic 8k."
8. मदुरै मीनाक्षी मंदिर (Meenakshi Amman Temple)
स्थान: [Madurai, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Meenakshi+Amman+Temple+Madurai&authuser=4)
प्रसिद्ध: द्रविड़ वास्तुकला का शिखर, हजार स्तंभों का हॉल और विशाल नक्काशीदार गोपुरम।
भोजन/प्रसाद: मदुरै जिगरथंडा, मीनाक्षी अम्मन लड्डू, कल्कंडू सादम.
AI Image Prompt: "The breathtaking colorful sculpted gopurams of Madurai Meenakshi Temple at dusk, illuminated, stunning reflection in the sacred pond, highly detailed realistic 8k rendering."
9. तिरुपति बालाजी (Sri Venkateswara Swamy Temple)
स्थान: [Tirumala, Andhra Pradesh](https://www.google.com/maps/search/?api=1&query=Tirumala+Tirupati+Devasthanam&authuser=4)
प्रसिद्ध: भगवान वेंकटेश्वर का पवित्र धाम और विश्व का सबसे अमीर मंदिर।
भोजन/प्रसाद: विश्व प्रसिद्ध तिरुपति लड्डू (GI टैग).
AI Image Prompt: "An immaculate realistic shot of the Tirupati Balaji temple complex at golden hour, the sacred shikhara and 'Ananda Nilayam' glowing, bustling with devotees, spiritual divine atmosphere, highly detailed 8k photography."
10. अक्षरधाम मंदिर (Swaminarayan Akshardham)
स्थान: [New Jersey, USA (भारत के बाहर सबसे बड़ा)](https://www.google.com/maps/search/?api=1&query=BAPS+Swaminarayan+Akshardham+Robbinsville+NJ&authuser=4)
प्रसिद्ध: आधुनिक युग का स्थापत्य चमत्कार, पूरी तरह से हाथ से नक्काशीदार संगमरमर से निर्मित।
भोजन/प्रसाद: सात्विक महाप्रसाद, गुजराती थाली, मोहनथाल.
AI Image Prompt: "The massive, incredibly intricately carved white marble Swaminarayan Akshardham Temple in Robbinsville, New Jersey, New York skyline faintly in the far distance, glowing illuminated water features, photorealistic, ultra-detailed 8k architecture photography."
भाग 2: विश्व के महत्वपूर्ण मंदिर (Wonders of the World)
1. अंकोरवाट मंदिर (Angkor Wat)
स्थान: [Siem Reap, Cambodia](https://www.google.com/maps/search/?api=1&query=Angkor+Wat+Siem+Reap+Cambodia&authuser=4)
प्रसिद्ध: विश्व का सबसे बड़ा धार्मिक स्मारक, खमेर वास्तुकला की उत्कृष्ट कृति।
भोजन/प्रसाद: Amok (कम्बोडियन डिश), Bai Sach Chrouk।
AI Image Prompt: "A breathtaking realistic wide-angle sunrise view of the ancient Angkor Wat temple in Cambodia, reflection of the lotus towers in the surrounding pond, golden morning mist, hyper-detailed architecture, 8k cinematic photography."
2. प्रम्बानन मंदिर (Prambanan Temple)
स्थान: [Yogyakarta, Indonesia](https://www.google.com/maps/search/?api=1&query=Prambanan+Temple+Yogyakarta+Indonesia&authuser=4)
प्रसिद्ध: इंडोनेशिया का सबसे बड़ा हिंदू मंदिर परिसर, त्रिदेव (ब्रह्मा, विष्णु, शिव) को समर्पित।
भोजन/प्रसाद: Gudeg (कटहल की मीठी डिश), Bakpia.
AI Image Prompt: "Majestic towering stone spires of the 9th century Prambanan Shiva temple compound in Java, Indonesia, dramatic sunset sky, detailed carvings, hyper-detailed photorealistic 8k shot."
3. पशुपतिनाथ मंदिर (Pashupatinath Temple)
स्थान: [Kathmandu, Nepal](https://www.google.com/maps/search/?api=1&query=Pashupatinath+Temple+Kathmandu+Nepal&authuser=4)
प्रसिद्ध: बागमती नदी के तट पर स्थित भगवान शिव का सबसे पवित्र पगोडा शैली का मंदिर।
भोजन/प्रसाद: रुद्राक्ष प्रसाद, सेल रोटी, योमरी.
AI Image Prompt: "Sacred pashupatinath temple pagoda with golden roof on the Bagmati River bank in Kathmandu Nepal, misty evening aarti with lamps, holy smoke, authentic spiritual atmosphere, hyper-detailed photorealistic 8k."
4. मुन्नेश्वरम मंदिर (Munneswaram Temple)
स्थान: [Chilaw, Sri Lanka](https://www.google.com/maps/search/?api=1&query=Munneswaram+Temple+Chilaw+Sri+Lanka&authuser=4)
प्रसिद्ध: रामायण काल से जुड़ा श्रीलंका का प्राचीन 'पंच ईश्वरम' मंदिर।
भोजन/प्रसाद: श्रीलंकाई भोजन, पोंगल, मोदक.
AI Image Prompt: "Ancient Dravidian style Munneswaram Shiva Temple complex in Sri Lanka, traditional architecture, sacred temple tank with floating lotus blossoms, warm afternoon light, highly detailed realistic shot."
5. बाटू गुफाएं (Batu Caves Sri Subramaniar Temple)
स्थान: [Selangor, Malaysia](https://www.google.com/maps/search/?api=1&query=Batu+Caves+Selangor+Malaysia&authuser=4)
प्रसिद्ध: विशाल प्राकृतिक गुफा और बाहर भगवान मुरुगन की 140 फीट ऊंची विशाल स्वर्ण प्रतिमा।
भोजन/प्रसाद: पंचामृत प्रसादम, Roti Canai, दक्षिण भारतीय शाकाहारी भोजन.
AI Image Prompt: "Breathtaking realistic shot of the massive golden Murugan statue standing proudly next to the colorful 272 steps leading into the massive limestone Batu Caves in Malaysia, lush green surroundings, photorealistic 8k."
भाग 1: भारत के अन्य प्रमुख मंदिर (Temples of India)
1. Trimbakeshwar Shiva Temple (त्र्यंबकेश्वर ज्योतिर्लिंग)
स्थान: [Nashik, Maharashtra](https://www.google.com/maps/search/?api=1&query=Trimbakeshwar+Shiva+Temple+Nashik&authuser=4)
प्रसिद्ध: बारह ज्योतिर्लिंगों में अद्वितीय, जहाँ शिवलिंग में ब्रह्मा, विष्णु और महेश तीनों के तीन मुख विद्यमान हैं।
भोजन/प्रसाद: पेड़ा प्रसाद, मिसल पाव, कांदा पोहा।
AI Image Prompt: "A realistic atmospheric shot of the ancient black stone Trimbakeshwar Temple in Nashik at sunrise, Brahmagiri hills in the backdrop with waterfalls, glowing brass lamps in the wet stone courtyard, hyper-detailed 8k photorealistic."
2. Shore Temple (शोर मंदिर / तट मंदिर)
Location: [Mahabalipuram, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Shore+Temple+Mahabalipuram&authuser=4)
Famous For: 8वीं सदी का यूनेस्को धरोहर स्थल, पल्लव वास्तुकला की ग्रेनाइट संरचना जो बंगाल की खाड़ी के किनारे खड़ी है।
Famous Local Food / Prasadam: दक्षिण भारतीय फिल्टर कॉफी, नारियल पानी, कुरकुरा मेदु वड़ा।
AI Image Prompt: "Historic 8th-century granite Shore Temple of Mahabalipuram perched on the ocean coastline, crashing sea waves of the Bay of Bengal catching evening golden light, weathered ancient rock carvings, 8k cinematic travel photo."
3. Dakshineswar Kali Temple (दक्षिणेश्वर काली मंदिर)
Location: [Kolkata, West Bengal](https://www.google.com/maps/search/?api=1&query=Dakshineswar+Kali+Temple+Kolkata&authuser=4)
Famous For: हुगली नदी के तट पर स्थित 12 शिव मंदिरों वाला माँ भवतारिणी काली का पावन धाम, जो श्री रामकृष्ण परमहंस से जुड़ा है।
Famous Local Food / Prasadam: खिचड़ी भोग, लबड़ा (सब्जी), रसगुल्ला, मिष्टी दोई।
AI Image Prompt: "Majestic Navaratna-style Dakshineswar Kali Temple on the banks of the Hooghly River in Kolkata, row of twelve small Shiva shrines along the ghat, floating wooden boats, soft early morning mist and sunrise, photorealistic."
4. Virupaksha Temple (विरुपाक्ष मंदिर, हम्पी)
Location: [Hampi, Karnataka](https://www.google.com/maps/search/?api=1&query=Virupaksha+Temple+Hampi&authuser=4)
Famous For: विजयनगर साम्राज्य की राजधानी हम्पी का मुख्य सक्रिय मंदिर और इसका विशाल नक्काशीदार 160 फीट ऊंचा गोपुरम।
Famous Local Food / Prasadam: जोलाड रोटी (ज्वार की रोटी), बिसी बेले भात, मैसूर पाक।
AI Image Prompt: "Monumental 50-meter Gopuram of the ancient Virupaksha Temple towering amidst the surreal boulder-strewn landscape of Hampi, Tungabhadra River nearby, warm sunset rays on ancient stone ruins, hyper-detailed 8k photography."
5. Golden Temple of Vellore / Sripuram (श्रीपुरम स्वर्ण मंदिर)
Location: [Vellore, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Sripuram+Golden+Temple+Vellore&authuser=4)
Famous For: 1500 किलो से अधिक शुद्ध सोने की परतों से ढका महालक्ष्मी का तारा-आकार (Star-shaped path) मंदिर।
Famous Local Food / Prasadam: महालक्ष्मी लड्डू, पुलियोदरे, घी रोस्ट डोसा।
AI Image Prompt: "Breathtaking wide-angle view of the golden Sripuram Mahalakshmi Temple in Vellore, exterior covered in pure hand-crafted gold foils, surrounded by a lush green star-shaped walking corridor and water moat, shimmering under midday sun, 8k realism."
6. Sun Temple, Modhera (मोढेरा सूर्य मंदिर)
Location: [Mehsana, Gujarat](https://www.google.com/maps/search/?api=1&query=Sun+Temple+Modhera+Gujarat&authuser=4)
Famous For: सोलंकी राजवंश की वास्तुकला और इसका विशाल 'सूर्य कुंड' (Stepwell) जिसमें 108 लघु मंदिर हैं।
Famous Local Food / Prasadam: गुजराती खमण, सुखड़ी (गुड़-आटे की मिठाई), थेपला।
AI Image Prompt: "Intricately carved sandstone Sun Temple of Modhera in Gujarat, symmetrical stone steps of the magnificent Surya Kund stepwell in foreground, golden morning light striking the pillared Sabha Mandap, ultra-realistic 8k architectural shot."
7. Murudeshwar Temple (मुरुदेश्वर मंदिर)
Location: [Bhatkal, Karnataka](https://www.google.com/maps/search/?api=1&query=Murudeshwar+Temple+Karnataka&authuser=4)
Famous For: अरब सागर के प्रायद्वीप पर स्थित विश्व की दूसरी सबसे ऊंची (123 फीट) विशाल भगवान शिव की प्रतिमा और 20-मंजिला राजा गोपुरम।
Famous Local Food / Prasadam: नीर डोसा, मैंगलोर बन, नारियल की चटनी।
AI Image Prompt: "Colossal 123-foot silver and blue statue of Lord Shiva seated on a cliff surrounded on three sides by the turquoise Arabian Sea at Murudeshwar, massive 20-story Rajagopuram in foreground, dramatic clouds, cinematic 8k."
8. Kalighat Kali Temple (कालीघाट काली मंदिर)
Location: [Kolkata, West Bengal](https://www.google.com/maps/search/?api=1&query=Kalighat+Kali+Temple+Kolkata&authuser=4)
Famous For: 51 शक्तिपीठों में से एक, जहाँ माता सती के दाहिने पैर की उंगलियां गिरी थीं।
Famous Local Food / Prasadam: पेड़ा भोग, संदेश, कचौरी।
AI Image Prompt: "Traditional Bengal-style curved roof architecture of Kalighat Kali Temple, bustling courtyard with devotees holding red hibiscus garlands, brass lamps glowing at dusk, authentic cultural realism."
9. Omkareshwar Jyotirlinga (ओंकारेश्वर ज्योतिर्लिंग)
Location: [Khandwa, Madhya Pradesh](https://www.google.com/maps/search/?api=1&query=Omkareshwar+Temple+Madhya+Pradesh&authuser=4)
Famous For: नर्मदा नदी के बीच 'ॐ' (Om) के आकार के मांधाता द्वीप पर स्थित पावन ज्योतिर्लिंग।
Famous Local Food / Prasadam: बेसन लड्डू, मालवा की जलेबी, पोहा।
AI Image Prompt: "Aerial wide-angle view of the sacred Omkareshwar Jyotirlinga Temple on the Om-shaped island in the middle of the sacred Narmada River, suspension bridge, evening aarti lamps floating on water, 8k photorealistic."
10. Sri Venkateswara Temple, Tirumala Foot - Sri Padmavathi Ammavari Temple (पद्मावती मंदिर)
Location: [Tiruchanur, Andhra Pradesh](https://www.google.com/maps/search/?api=1&query=Sri+Padmavathi+Ammavari+Temple+Tiruchanur&authuser=4)
Famous For: भगवान वेंकटेश्वर की अर्धांगिनी देवी पद्मावती का दिव्य मंदिर, पद्मा सरोवर तीर्थ।
Famous Local Food / Prasadam: चक्र पोंगल, वड़ा प्रसादम, रवा केसरी।
AI Image Prompt: "Grand South Indian Dravidian Temple of Goddess Padmavathi in Tiruchanur, golden flag mast (Dhwajasthambham), intricate gopuram illuminated at dusk, serene temple tank reflecting temple lights, ultra-detailed."
भाग 2: विश्व के अन्य प्रमुख मंदिर (Temples Across the World)
11. Banteay Srei (बांतेय स्रेई मंदिर)
Location: [Siem Reap, Cambodia](https://www.google.com/maps/search/?api=1&query=Banteay+Srei+Cambodia&authuser=4)
Famous For: 'खमेर कला का रत्न', 10वीं सदी का भगवान शिव को समर्पित मंदिर जो लाल बलुआ पत्थर की अत्यंत बारीक नक्काशी के लिए जाना जाता है।
Famous Local Food / Prasadam: Num Pang (कम्बोडियन सैंडविच), नारियल चावल।
AI Image Prompt: "Hyper-detailed close-up view of the 10th-century pink sandstone temple of Banteay Srei in Cambodia, intricate miniature bas-reliefs of Hindu epics and devatas, dappled jungle sunlight filtering through tropical canopy, 8k photography."
12. Pura Besakih - Mother Temple of Bali (पुरा बेसाकिह)
Location: [Bali, Indonesia](https://www.google.com/maps/search/?api=1&query=Pura+Besakih+Bali+Indonesia&authuser=4)
Famous For: बाली का सबसे बड़ा और सबसे पवित्र हिंदू मंदिर परिसर, जो सक्रिय ज्वालामुखी माउंट अगुंग की ढलान पर स्थित है।
Famous Local Food / Prasadam: Dadar Gulung (नारियल पैनकेक), Nasi Kuning (हल्दी चावल)।
AI Image Prompt: "The grand terraced Balinese Meru shrines of Pura Besakih on the mist-covered slopes of Mount Agung volcano in Bali, colorful ceremonial umbrellas, stone dragon stairs, dramatic mystic mountain atmosphere, ultra-realistic 8k."
13. Nallur Kandaswamy Kovil (नल्लूर कंदास्वामी मंदिर)
Location: [Jaffna, Sri Lanka](https://www.google.com/maps/search/?api=1&query=Nallur+Kandaswamy+Kovil+Jaffna&authuser=4)
Famous For: श्रीलंका के उत्तरी भाग में स्थित भगवान मुरुगन का सबसे भव्य और ऐतिहासिक द्रविड़ मंदिर।
Famous Local Food / Prasadam: जाफना आम, मोदकम, पोंगल प्रसादम।
AI Image Prompt: "Vibrant golden Gopuram and grand brass bell tower of the Nallur Kandaswamy Murugan Kovil in Jaffna, red and white striped courtyard walls, evening ceremonial lights and oil lamps, highly detailed travel photography."
14. Sri Mariamman Temple (श्री मरियम्मन मंदिर)
Location: [Chinatown, Singapore](https://www.google.com/maps/search/?api=1&query=Sri+Mariamman+Temple+Singapore&authuser=4)
Famous For: 1827 में बना सिंगापुर का सबसे पुराना हिंदू मंदिर और इसका बहुरंगी 6-मंजिला गोपुरम।
Famous Local Food / Prasadam: सिंगापुरियन सात्विक थाली, पुलियोदरे, अप्पम।
AI Image Prompt: "The ornate and colorful six-tiered Gopuram of Singapore's oldest Hindu shrine, Sri Mariamman Temple, surrounded by Chinatown's classic heritage shophouses, sharp modern-meets-traditional contrast, bright sunny day, 8k photorealistic."
15. Shri Swaminarayan Mandir (नीसडेन मंदिर)
Location: [London, United Kingdom](https://www.google.com/maps/search/?api=1&query=BAPS+Shri+Swaminarayan+Mandir+London&authuser=4)
Famous For: यूरोप का पहला पारंपरिक हाथ से तराशा गया संगमरमर और चूना पत्थर का हिंदू मंदिर।
Famous Local Food / Prasadam: गुजराती कढ़ी-खिचड़ी, जलेबी, सात्विक थाली।
AI Image Prompt: "A stunning architectural photograph of the white Carrara marble and Bulgarian limestone BAPS Shri Swaminarayan Mandir in Neasden London, perfectly manicured traditional lawns and fountains in foreground, golden evening light, 8k resolution."
भाग 1: भारत के प्रमुख मंदिर (Temples of India)
1. Kailasa Temple, Ellora Caves (कैलाश मंदिर, एलोरा)
Location: [Ellora Caves, Aurangabad, Maharashtra](https://www.google.com/maps/search/?api=1&query=Kailasa+Temple+Ellora+Caves+Aurangabad&authuser=4)
Famous For: विश्व की सबसे बड़ी एकल चट्टान को ऊपर से नीचे काटकर बनाई गई अखंड पाषाण (Monolithic) गुफा वास्तुकला।
Famous Local Food / Prasadam: औरंगाबादी नान-खलिया (शाकाहारी संस्करण), इमर्ती, पिठला भाकरी।
AI Image Prompt: "A breathtaking wide-angle realistic photograph of the colossal monolithic rock-cut Kailasa Temple carved out of a single basalt cliff at Ellora Caves, intricate multi-story elephant carvings and pillars, dramatic morning light cutting through the rock gorge, 8k ultra-detailed."
2. Chennakeshava Temple (चेन्नाकेशव मंदिर, बेलूर)
Location: [Belur, Hassan, Karnataka](https://www.google.com/maps/search/?api=1&query=Chennakeshava+Temple+Belur+Karnataka&authuser=4)
Famous For: 12वीं सदी की होयसला वास्तुकला की अत्यंत बारीक सोपस्टोन नक्काशी और तारा-आकार का मंदिर आधार।
Famous Local Food / Prasadam: केसरी भात, जोलाड रोटी, मड्डुर वड़ा।
AI Image Prompt: "Extremely detailed shot of the 12th-century star-shaped Hoysala soapstone Chennakeshava Temple in Belur, intricate micro-carvings of dancing celestial nymphs (Madanikas) and mythological friezes, soft golden afternoon sun, hyper-realistic 8k."
3. Mallikarjuna Jyotirlinga (मल्लिकार्जुन ज्योतिर्लिंग)
Location: [Srisailam, Andhra Pradesh](https://www.google.com/maps/search/?api=1&query=Mallikarjuna+Jyotirlinga+Srisailam&authuser=4)
Famous For: भारत का एकमात्र ऐसा पवित्र स्थल जो एक साथ ज्योतिर्लिंग और शक्तिपीठ (भ्रमराम्बा) दोनों है।
Famous Local Food / Prasadam: लाडू प्रसादम, पुलिहोरा (इमली चावल), पुथारेकुलु (आंध्र की प्रसिद्ध मिठाई)।
AI Image Prompt: "The fortified ancient stone fortress and Dravidian Gopuram of Mallikarjuna Swamy Temple on the lush Nallamala Hills overlooking the Krishna River, evening aarti lamps illuminated, misty jungle mountain horizon, photorealistic."
4. Baidyanath Jyotirlinga (बैद्यनाथ धाम)
Location: [Deoghar, Jharkhand](https://www.google.com/maps/search/?api=1&query=Baidyanath+Temple+Deoghar+Jharkhand&authuser=4)
Famous For: पावन ज्योतिर्लिंग और श्रावण मास में लाखों कांवरियों की कांवड़ यात्रा का केंद्र।
Famous Local Food / Prasadam: देवघर का प्रसिद्ध पेड़ा, चने की घुघनी, तिलकुट।
AI Image Prompt: "Traditional pyramid-shaped stone spire of Baba Baidyanath Temple in Deoghar adorned with red flags and sacred Panchashul on top, bustling courtyard filled with glowing diyas and holy water pots, divine atmosphere, 8k realism."
5. Tungnath Temple (तुंगनाथ मंदिर)
Location: [Rudraprayag, Uttarakhand](https://www.google.com/maps/search/?api=1&query=Tungnath+Temple+Chopta+Uttarakhand&authuser=4)
Famous For: विश्व का सबसे ऊंचा शिव मंदिर (3,680 मीटर की ऊंचाई पर स्थित पंच केदार तीर्थ)।
Famous Local Food / Prasadam: बुरांश (Rhododendron) का शरबत, मंडुआ की रोटी, पहाड़ी दाल।
AI Image Prompt: "Ancient weathered stone Tungnath temple perched high on the alpine alpine meadows of Chandrashila in the Himalayas, surrounded by blooming red rhododendron trees and snow-capped mountain peaks under crisp blue skies, hyper-realistic travel photography."
6. Grishneshwar Jyotirlinga (घृष्णेश्वर ज्योतिर्लिंग)
Location: [Verul, Maharashtra](https://www.google.com/maps/search/?api=1&query=Grishneshwar+Jyotirlinga+Temple+Verul&authuser=4)
Famous For: भारत का 12वां और अंतिम ज्योतिर्लिंग, जो लाल बेसाल्ट पत्थर से बनी बारीक नक्काशी के लिए प्रसिद्ध है।
Famous Local Food / Prasadam: पेड़ा, पूरन पोली, मिसल।
AI Image Prompt: "Warm reddish-brown stone spire of Grishneshwar Jyotirlinga Temple glowing at sunset, ornate 5-tiered shikhara with intricate sculptures of deities, stone courtyard reflecting temple lamps, high-detail 8k."
7. Nageshwar Jyotirlinga (नागेश्वर ज्योतिर्लिंग)
Location: [Daarukavanam, Dwarka, Gujarat](https://www.google.com/maps/search/?api=1&query=Nageshwar+Jyotirlinga+Dwarka+Gujarat&authuser=4)
Famous For: 'दारुकावन' में स्थित पावन ज्योतिर्लिंग और मंदिर प्रांगण में स्थापित भगवान शिव की 85 फीट ऊंची विशालकाय ध्यानस्थ प्रतिमा।
Famous Local Food / Prasadam: माखन-मिश्री, गुजराती लापसी, कचौरी।
AI Image Prompt: "Colossal 85-foot seated statue of Lord Shiva in meditation posture overlooking the Nageshwar Temple complex in Gujarat, clear blue coastal sky, lush green temple garden with colorful floral borders, hyper-realistic 8k."
8. Bhimashankar Jyotirlinga (भीमाशंकर ज्योतिर्लिंग)
Location: [Khed, Pune, Maharashtra](https://www.google.com/maps/search/?api=1&query=Bhimashankar+Jyotirlinga+Temple+Maharashtra&authuser=4)
Famous For: भीमा नदी के उद्गम पर सह्याद्रि की घनी पहाड़ियों में स्थित नागर शैली का पावन ज्योतिर्लिंग।
Famous Local Food / Prasadam: पेड़ा, पिठला भाकरी, ठेचा।
AI Image Prompt: "Black stone medieval Nagara-style Bhimashankar Temple tucked inside dense mist-covered Western Ghats rainforest, water droplets dripping from moss-covered ancient stones, dramatic atmospheric fog, photorealistic."
9. Shri Siddhivinayak Temple (सिद्धिविनायक मंदिर)
Location: [Prabhadevi, Mumbai, Maharashtra](https://www.google.com/maps/search/?api=1&query=Siddhivinayak+Temple+Prabhadevi+Mumbai&authuser=4)
Famous For: भगवान गणेश का स्वयंभू विग्रह, जिनकी सूंड दाईं ओर मुड़ी है (सिद्धि पीठ)।
Famous Local Food / Prasadam: मोदक प्रसादम, नारियल लड्डू, मुंबई वड़ा पाव।
AI Image Prompt: "Illuminated golden multi-domed architecture of the modern Shri Siddhivinayak Temple in Mumbai during night festivities, vibrant flower market stalls with marigold garlands outside the entrance, 8k realistic urban devotional photography."
10. Tarapith Temple (तारापीठ मंदिर)
Location: [Birbhum, West Bengal](https://www.google.com/maps/search/?api=1&query=Tarapith+Temple+Birbhum+West+Bengal&authuser=4)
Famous For: प्रसिद्ध तांत्रिक शक्तिपीठ, माँ तारा का धाम और वामाखेपा की पावन साधना भूमि।
Famous Local Food / Prasadam: खिचड़ी भोग, लबड़ा, मिष्टी दोई, बंगाली संदेश।
AI Image Prompt: "Traditional terracotta-influenced red brick temple of Goddess Tara at Tarapith, holy smoke rising from ceremonial havankunds, sacred red hibiscus flower garlands draped on sanctum doors, authentic cultural realism."
भाग 2: विश्व के अन्य प्रमुख मंदिर (Temples Across the World)
11. Pura Ulun Danu Bratan (पुरा उलुन दानु ब्रतन)
Location: [Bedugul, Bali, Indonesia](https://www.google.com/maps/search/?api=1&query=Pura+Ulun+Danu+Bratan+Bali+Indonesia&authuser=4)
Famous For: झील के शांत पानी पर तैरता हुआ सा दिखने वाला 11-मंजिला ऐतिहासिक बालिनीज शिव-जल मंदिर।
Famous Local Food / Prasadam: Pisang Goreng (केले के पकोड़े), शाकाहारी Nasi Goreng।
AI Image Prompt: "Iconic 11-tiered thatched roof Meru tower of Pura Ulun Danu Bratan temple floating gracefully on the reflective surface of Lake Bratan, mist rolling over emerald volcanic mountains in the background, tranquil sunrise light, 8k nature photography."
12. Sri Thendayuthapani Temple (श्री थेंडायुथापानी मंदिर)
Location: [Tank Road, Singapore](https://www.google.com/maps/search/?api=1&query=Sri+Thendayuthapani+Temple+Singapore&authuser=4)
Famous For: चेट्टियार समुदाय द्वारा 1859 में निर्मित भगवान मुरुगन का भव्य मंदिर, जो थाईपुसम उत्सव का मुख्य केंद्र है।
Famous Local Food / Prasadam: पंचामृत, मसाला डोसा, सात्विक दक्षिण भारतीय भोजन।
AI Image Prompt: "Stunning grand Rajagopuram of Sri Thendayuthapani Temple illuminated with colorful modern lights against the Singapore night sky, intricately sculpted devatas on the tower, spotless marble courtyard, photorealistic."
13. BAPS Shri Swaminarayan Mandir (स्वामीनारायण मंदिर, टोरंटो)
Location: [Toronto, Ontario, Canada](https://www.google.com/maps/search/?api=1&query=BAPS+Shri+Swaminarayan+Mandir+Toronto&authuser=4)
Famous For: कनाडाई परिदृश्य में हाथ से तराशे गए इतालियन संगमरमर और तुर्की चूना पत्थर से बना भव्य मंदिर।
Famous Local Food / Prasadam: स्वामीनारायण खिचड़ी, मोहनथाल, कढ़ी।
AI Image Prompt: "Hand-carved white Italian Carrara marble domes of BAPS Shri Swaminarayan Mandir in Toronto covered in a delicate layer of fresh winter snow, sparkling ice accents, pristine golden sunset glow, ultra-detailed 8k architecture photography."
14. Sri Venkateswara Balaji Temple (श्री वेंकटेश्वर बालाजी मंदिर)
Location: [Tividale, West Midlands, United Kingdom](https://www.google.com/maps/search/?api=1&query=Sri+Venkateswara+Balaji+Temple+Tividale+UK&authuser=4)
Famous For: यूरोप में भगवान तिरुपति बालाजी का सबसे बड़ा और प्रमुख मंदिर परिसर।
Famous Local Food / Prasadam: तिरुपति-शैली लड्डू, पोंगल, वड़ा।
AI Image Prompt: "Traditional South Indian granite and stone Gopuram of the Sri Venkateswara Balaji Temple in the United Kingdom, set against green English countryside meadows, soft overcast cinematic daylight, photorealistic."
15. Shri Shiva Vishnu Temple (शिव विष्णु मंदिर, विक्टोरिया)
Location: [Carrum Downs, Victoria, Australia](https://www.google.com/maps/search/?api=1&query=Shri+Shiva+Vishnu+Temple+Carrum+Downs+Victoria&authuser=4)
Famous For: ऑस्ट्रेलिया का सबसे बड़ा हिंदू मंदिर, जहाँ द्रविड़ और हिंदू-शैव-वैष्णव परंपराओं का सुंदर संगम दिखता है।
Famous Local Food / Prasadam: पुलियोदरे, सांभर वड़ा, मैसूर पाक।
AI Image Prompt: "Majestic towering white and pastel sculpted Gopurams of the Shiva Vishnu Temple in Victoria Australia, clear southern sky, eucalyptus trees in background, bright sunny midday lighting, 8k realistic architectural shot."
भाग 1: भारत के प्रमुख मंदिर (Temples of India)
1. Sun Temple, Martand (मार्तंड सूर्य मंदिर)
Location: [Anantnag, Jammu & Kashmir](https://www.google.com/maps/search/?api=1&query=Martand+Sun+Temple+Anantnag&authuser=4)
Famous For: 8वीं सदी के राजा ललितादित्य द्वारा निर्मित कश्मीरी और ग्रीक-गांधार स्थापत्य शैली के भव्य पाषाण खंडहर।
Famous Local Food / Prasadam: कश्मीरी कहवा (केसर चाय), मोदुर पुलाव, नदरू (कमल ककड़ी) व्यंजन।
AI Image Prompt: "A cinematic wide-angle view of the ancient Martand Sun Temple stone ruins in Kashmir valley, dramatic stone colonnades and central sanctum catching the golden rays of dawn, snow-capped Pir Panjal mountains in the background, 8k hyper-realistic."
2. Gommateshwara Temple (गोमटेश्वर / बाहुबली मंदिर)
Location: [Shravanabelagola, Karnataka](https://www.google.com/maps/search/?api=1&query=Gommateshwara+Statue+Shravanabelagola&authuser=4)
Famous For: विंध्यगिरि पहाड़ी पर स्थित 57 फीट ऊंची विश्व की सबसे बड़ी एकल ग्रेनाइट पाषाण प्रतिमा और महामस्तकाभिषेक।
Famous Local Food / Prasadam: मैसूर पाक, जोलाड रोटी, कोसंम्बरी।
AI Image Prompt: "Colossal 57-foot monolithic granite statue of Lord Bahubali atop the rocky hill of Shravanabelagola, clear blue sky, soft morning sunlight illuminating the peaceful meditative face, photorealistic 8k architectural shot."
3. Brahma Temple (जगतपिता ब्रह्मा मंदिर)
Location: [Pushkar, Rajasthan](https://www.google.com/maps/search/?api=1&query=Brahma+Temple+Pushkar+Rajasthan&authuser=4)
Famous For: विश्व में भगवान ब्रह्मा के चुनिंदा और सबसे प्रमुख सक्रिय ऐतिहासिक मंदिरों में से एक।
Famous Local Food / Prasadam: पुष्कर का प्रसिद्ध मालपुआ, गुलाब जामुन, दाल बाटी चूरमा।
AI Image Prompt: "Historic red-spire Brahma Temple in Pushkar with the sacred silver turtle motif in the stone courtyard, view extending towards the holy Pushkar Sarovar lake, colorful Rajasthani turbans, warm sunset glow, 8k realistic."
4. Chidambaram Nataraja Temple (चिदंबरम नटराज मंदिर)
Location: [Chidambaram, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Thillai+Nataraja+Temple+Chidambaram&authuser=4)
Famous For: पंचभूत स्थलों में 'आकाश' तत्व का प्रतिनिधित्व करने वाला भगवान शिव के आनंद तांडव स्वरूप का स्वर्ण-छत मंदिर।
Famous Local Food / Prasadam: कट्टू पोंगल, पुलियोदरे, अप्पम।
AI Image Prompt: "Golden roof of the Kanakasabha sanctum inside the grand Chidambaram Nataraja Temple, massive stone gopurams reflecting in the sacred Sivaganga tank, classical Bharatanatyam sculptures carved into granite pillars, hyper-detailed 8k."
5. Hoysaleswara Temple (होयसलेश्वर मंदिर)
Location: [Halebidu, Hassan, Karnataka](https://www.google.com/maps/search/?api=1&query=Hoysaleswara+Temple+Halebidu&authuser=4)
Famous For: होयसला साम्राज्य की सोपस्टोन मूर्तिकला का शिखर, जिसमें एक भी मूर्ति दूसरी जैसी नहीं है।
Famous Local Food / Prasadam: बिसी बेले भात, अक्की रोटी, फिल्टर कॉफी।
AI Image Prompt: "Extremely intricate stone relief friezes of charging elephants, mythical lions, and celestial dancers along the outer walls of Hoysaleswara Temple in Halebidu, soft directional afternoon light, 8k macro architectural photography."
6. Suchindram Thanumalayan Temple (शुचींद्रम थानुमलायन मंदिर)
Location: [Kanyakumari District, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Thanumalayan+Temple+Suchindram&authuser=4)
Famous For: त्रिदेव (स्थानु-शिव, मल-विष्णु, अयन-ब्रह्मा) की एक साथ पूजा और अद्भुत संगीतमय पत्थर के खंभे (Musical Pillars)।
Famous Local Food / Prasadam: अवियल, केले के चिप्स, पायसम।
AI Image Prompt: "Majestic 134-foot white Gopuram of Suchindram Temple glowing in early morning light, grand pillared mandapam with polished granite musical columns, reflection in the sacred temple tank, ultra-realistic."
7. Lepakshi Veerabhadra Temple (लेपाक्षी वीरभद्र मंदिर)
Location: [Lepakshi, Andhra Pradesh](https://www.google.com/maps/search/?api=1&query=Veerabhadra+Temple+Lepakshi&authuser=4)
Famous For: विजयनगर शैली का चमत्कार, हवा में झूलता हुआ खंभा (Hanging Pillar) और विशाल नंदी की अखंड मूर्ति।
Famous Local Food / Prasadam: आंध्र पुलीहोरा, पेसरट्टू, गोंगुरा चावल।
AI Image Prompt: "Mystical hanging pillar defying gravity inside the carved stone halls of the Lepakshi Veerabhadra Temple, warm sunlight slanting through the stone lattice, hyper-detailed ancient Vijayanagara frescoes on the ceiling, 8k realistic."
8. Karni Mata Temple (करणी माता मंदिर / चूहों का मंदिर)
Location: [Deshnoke, Bikaner, Rajasthan](https://www.google.com/maps/search/?api=1&query=Karni+Mata+Temple+Deshnoke&authuser=4)
Famous For: मंदिर परिसर में 25,000 से अधिक पवित्र काले चूहों (काबा) का स्वतंत्र विचरण और सफेद चूहे के दर्शन का महत्व।
Famous Local Food / Prasadam: कढ़ाह प्रसाद, बीकानेरी भुजिया, घेवर।
AI Image Prompt: "Intricately carved silver doors and white marble facade of the historic Karni Mata Temple in Deshnoke, ornate courtyard with bowls of milk, soft morning haze, authentic cultural realism."
9. Padmavathi Devi / Tirupati Govindaraja Swamy Temple (गोविंदराज स्वामी मंदिर)
Location: [Tirupati, Andhra Pradesh](https://www.google.com/maps/search/?api=1&query=Sri+Govindaraja+Swamy+Temple+Tirupati&authuser=4)
Famous For: तिरुपति शहर के मध्य स्थित भगवान विष्णु के शयन स्वरूप का प्राचीन विशाल द्रविड़ मंदिर।
Famous Local Food / Prasadam: तिरुपति लड्डू, दही चावल प्रसादम, रवा केसरी।
AI Image Prompt: "Grand towering multi-tiered Rajagopuram of Sri Govindaraja Swamy Temple rising above the bustling holy town of Tirupati, illuminated by warm evening city lights, vibrant temple flag flying high, 8k photorealistic."
10. Trirashmi / Pandavleni Buddhist Caves & Shrines (पांडवलेनी गुफाएं)
Location: [Nashik, Maharashtra](https://www.google.com/maps/search/?api=1&query=Pandavleni+Caves+Nashik&authuser=4)
Famous For: ईसा पूर्व दूसरी सदी की 24 प्राचीन शैलकृत हीनयान बौद्ध गुफाएं और जल संचयन प्रणाली।
Famous Local Food / Prasadam: मिसल पाव, साबूदाना वड़ा, अंगूर।
AI Image Prompt: "Ancient rock-cut facades of the Pandavleni caves carved into the green tabletop plateau of Nashik hills, detailed chaitya arches and pillars catching warm morning sunlight, misty valley below, photorealistic."
भाग 2: विश्व के प्रमुख मंदिर (Temples Across the World)
11. Prasat Hin Phimai (प्रसात हिन फिमाई)
Location: [Nakhon Ratchasima, Thailand](https://www.google.com/maps/search/?api=1&query=Phimai+Historical+Park+Thailand&authuser=4)
Famous For: थाईलैंड का सबसे महत्वपूर्ण और प्राचीन खमेर हिंदू-बौद्ध मंदिर परिसर, जो अंगकोर वाट के समकालीन है।
Famous Local Food / Prasadam: Pad Thai (शाकाहारी रूप), आम और स्टिकी राइस।
AI Image Prompt: "Ancient white and red sandstone towers of Prasat Hin Phimai historical park in Thailand, ornate naga balustrades and carved lintels, lush tropical lawns under dramatic monsoon clouds, 8k photography."
12. Sri Srinivasa Perumal Temple (श्री श्रीनिवास पेरुमल मंदिर)
Location: [Little India, Singapore](https://www.google.com/maps/search/?api=1&query=Sri+Srinivasa+Perumal+Temple+Singapore&authuser=4)
Famous For: 1855 में स्थापित यूनेस्को राष्ट्रीय स्मारक, भगवान विष्णु के दशावतारों को दर्शाता 20-मीटर ऊंचा रंगीन गोपुरम।
Famous Local Food / Prasadam: वड़ा, पोंगल, मसाला चाय।
AI Image Prompt: "Vividly painted towering Gopuram depicting the Dashavatara of Lord Vishnu at Sri Srinivasa Perumal Temple in Singapore, vibrant Little India street atmosphere, clear tropical sky, ultra-detailed 8k."
13. Sri Siva Vishnu Temple (श्री शिव विष्णु मंदिर)
Location: [Lanham, Maryland, USA](https://www.google.com/maps/search/?api=1&query=Sri+Siva+Vishnu+Temple+Lanham+Maryland&authuser=4)
Famous For: संयुक्त राज्य अमेरिका के सबसे बड़े और सबसे पुराने पारंपरिक हिंदू मंदिरों में से एक।
Famous Local Food / Prasadam: पुलिहोरा, सांभर इडली, मैसूर पाक।
AI Image Prompt: "Authentic South Indian stone Gopuram and traditional carved pillars of the Sri Siva Vishnu Temple in Maryland, set against autumn-colored American oak trees, soft golden evening light, 8k realistic architectural shot."
14. Pura Lempuyang Luhur - Gates of Heaven (पुरा लेम्पुयांग)
Location: [Karangasem, Bali, Indonesia](https://www.google.com/maps/search/?api=1&query=Pura+Lempuyang+Bali+Indonesia&authuser=4)
Famous For: बादलों के बीच माउंट अगुंग ज्वालामुखी को फ्रेम करता प्रसिद्ध 'गेट ऑफ हेवन' (Candigentar)।
Famous Local Food / Prasadam: Pisang Rai (उबले नारियल केले), बालिनीज चाय।
AI Image Prompt: "The iconic split gateway (Candi Bentar) of Pura Lempuyang in Bali framing the active Mount Agung volcano, reflective still water pool in the foreground, morning pink and gold clouds, 8k hyper-realistic nature photography."
15. Shri Radha Krishna Mandir / Hare Krishna Temple (हरे कृष्ण मंदिर)
Location: [Watford, London, United Kingdom](https://www.google.com/maps/search/?api=1&query=Bhaktivedanta+Manor+Watford&authuser=4)
Famous For: जॉर्ज हैरिसन (द बीटल्स) द्वारा दान की गई 'भक्तिवेदांत मनोर' संपत्ति पर स्थित भव्य कृष्ण मंदिर और जैविक गोशाला।
Famous Local Food / Prasadam: सात्विक इस्कॉन महाप्रसाद, हलवा, मटर पनीर, समोसा।
AI Image Prompt: "Charming mock-Tudor estate converted into the sacred Bhaktivedanta Manor Krishna temple in the lush English countryside of Watford, colorful flower gardens, peacocks roaming the lawn, serene afternoon sunlight, photorealistic."
भाग 1: भारत के प्रमुख मंदिर (Temples of India)
1. Koneswaram Temple of Gokarna / Mahabaleshwar (महाबलेश्वर मंदिर)
Location: [Gokarna, Uttara Kannada, Karnataka](https://www.google.com/maps/search/?api=1&query=Mahabaleshwar+Temple+Gokarna&authuser=4)
Famous For: रावण द्वारा लाए गए आत्मलिंग का मूल स्थान और अरब सागर के तट पर स्थित पावन मुक्ति क्षेत्र।
Famous Local Food / Prasadam: तोडदेवु (पारंपरिक मीठा व्यंजन), नीर डोसा, मैंगलोर रसम।
AI Image Prompt: "Ancient Dravidian granite stone architecture of Mahabaleshwar Temple in Gokarna, crashing Arabian Sea waves visible on the nearby rocky coastline, sacred cows and brass oil lamps in the stone corridors, golden sunset lighting, 8k photorealistic."
2. Dilwara Temples (दिलवाड़ा जैन मंदिर)
Location: [Mount Abu, Rajasthan](https://www.google.com/maps/search/?api=1&query=Dilwara+Temples+Mount+Abu&authuser=4)
Famous For: 11वीं से 13वीं सदी की दुनिया की सबसे जटिल और पारदर्शी जैसी दिखने वाली संगमरमर नक्काशी।
Famous Local Food / Prasadam: माउंट आबू की रबड़ी, घेवर, दाल बाटी चूरमा।
AI Image Prompt: "Astonishingly intricate ceiling dome carved from pure white marble at Dilwara Temples in Mount Abu, razor-sharp lotus pendant carvings hanging from the ceiling, soft directional museum lighting, macro architectural photography, 8k realism."
3. Ambaji Mata Temple (अंबाजी माता मंदिर)
Location: [Banaskantha, Gujarat](https://www.google.com/maps/search/?api=1&query=Ambaji+Temple+Gujarat&authuser=4)
Famous For: 51 शक्तिपीठों में प्रमुख, जहाँ कोई मूर्ति नहीं बल्कि पवित्र 'श्री विसा यंत्र' की पूजा की जाती है।
Famous Local Food / Prasadam: मोहनथाल प्रसादम, गुजराती थेपला, पेड़ा।
AI Image Prompt: "Magnificent white marble and gold-plated Shikhara of Ambaji Temple on the Gabbar Hill background, vibrant red festival flags fluttering, illuminated marble courtyard crowded with devotees at dusk, hyper-detailed 8k."
4. Srikalahasteeswara Temple (श्रीकालहस्ती मंदिर)
Location: [Srikalahasti, Tirupati District, Andhra Pradesh](https://www.google.com/maps/search/?api=1&query=Srikalahasti+Temple+Andhra+Pradesh&authuser=4)
Famous For: पंचभूत स्थलों में 'वायु' तत्व का प्रतिनिधित्व करने वाला मंदिर, जहाँ गर्भगृह का दीपक निरंतर हिलता रहता है।
Famous Local Food / Prasadam: पुलीहोरा, केसरी भात, आंध्र भोजन थाली।
AI Image Prompt: "Massive South Indian stone gopuram of Srikalahasti Temple on the banks of Swarnamukhi River, glowing oil lamps in the ancient monolithic pillared mandapams, gentle flickering flame atmosphere, ultra-realistic 8k."
5. Sree Krishna Temple, Guruvayur (गुरुवायुर मंदिर)
Location: [Guruvayur, Thrissur, Kerala](https://www.google.com/maps/search/?api=1&query=Guruvayur+Sri+Krishna+Temple&authuser=4)
Famous For: 'भूलोक वैकुंठ' के रूप में प्रसिद्ध, केरल शैली की तांबे की छत और 'दीपास्तंभ' का दिव्य प्रकाश।
Famous Local Food / Prasadam: पाल पायसम (दूध की खीर), नेई पायसम, उण्णियप्पम।
AI Image Prompt: "Traditional Kerala-style Guruvayur Temple with sloping copper roofs and wooden gables, magnificent brass Deepastambham illuminated by hundreds of coconut oil lamps in the evening, serene golden reflections, photorealistic."
6. Ranakpur Jain Temple (रणकपुर जैन मंदिर)
Location: [Pali District, Rajasthan](https://www.google.com/maps/search/?api=1&query=Ranakpur+Jain+Temple+Rajasthan&authuser=4)
Famous For: 1,444 संगमरमर के खंभे, जिनमें से कोई भी दो खंभे एक जैसे नहीं हैं और प्रकाश के अनुसार रंग बदलते हैं।
Famous Local Food / Prasadam: राजस्थानी कढ़ी, बाजरे की रोटी, गट्टे की सब्जी।
AI Image Prompt: "A symmetrical deep perspective view down the forest of 1444 intricately carved light-amber marble pillars inside Ranakpur Temple, sunlight casting soft geometric shadows across the polished floor, 8k architectural shot."
7. Murugan Temple / Subramaniya Swamy Temple (तिरुचेंदूर मुरुगन मंदिर)
Location: [Tiruchendur, Thoothukudi, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Tiruchendur+Murugan+Temple&authuser=4)
Famous For: भगवान मुरुगन के छह निवासों (आरुपदै वीडु) में एकमात्र ऐसा मंदिर जो सीधे समुद्र तट पर स्थित है।
Famous Local Food / Prasadam: करुपट्टी (ताड़ का गुड़) मिठाई, पंचामृत, रसम सादम।
AI Image Prompt: "Towering 9-tiered ancient Rajagopuram of Tiruchendur Murugan Temple standing firmly on the golden sand beach of the Gulf of Mannar, azure ocean waves rolling onto the shore, bright sunny coastal lighting, photorealistic."
8. Chamundeshwari Temple (चामुंडेश्वरी मंदिर)
Location: [Chamundi Hill, Mysuru, Karnataka](https://www.google.com/maps/search/?api=1&query=Chamundeshwari+Temple+Mysore&authuser=4)
Famous For: चामुंडी पहाड़ी की चोटी पर स्थित 1000 साल पुराना मंदिर और पहाड़ी के रास्ते पर स्थित विशाल अखंड नंदी।
Famous Local Food / Prasadam: मैसूर पाक, मैसूर मसाला डोसा, केसरी भात।
AI Image Prompt: "Ornate multi-colored Dravidian Gopuram of Chamundeshwari Temple perched atop the Chamundi Hills, panoramic view of Mysore city in the background, soft golden morning haze, ultra-detailed 8k."
9. Jawala Ji Temple (ज्वाला जी शक्तिपीठ)
Location: [Kangra, Himachal Pradesh](https://www.google.com/maps/search/?api=1&query=Jwala+Ji+Temple+Kangra&authuser=4)
Famous For: चट्टानों से बिना किसी ईंधन के निकलने वाली 9 प्राकृतिक अखंड ज्वालाओं का पावन शक्तिपीठ।
Famous Local Food / Prasadam: बेसन के लड्डू, पहाड़ी धाम (चावल और मदरा), सेब।
AI Image Prompt: "Golden dome of the historic Jwala Ji Temple nestled against the pine-covered Kangra valley hills, sacred golden lamps, prayer flags fluttering in the mountain wind, photorealistic cinematic realism."
10. Airavatesvara Temple (ऐरावतेश्वर मंदिर, दरासुरम)
Location: [Darasuram, Kumbakonam, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Airavatesvara+Temple+Darasuram&authuser=4)
Famous For: महान जीवित चोल मंदिरों में शामिल, पत्थर के पहियों पर बना रथ-आकार का मंडप और संगीतमय सीढ़ियां।
Famous Local Food / Prasadam: कुंभकोणम डिग्री कॉफी, पुलियोदरे, मीठा पोंगल।
AI Image Prompt: "Chola dynasty stone chariot mandapam pulled by stone horses at Airavatesvara Temple in Darasuram, hyper-detailed granite relief carvings of musicians and dancers, warm late-afternoon sunbeams, 8k photography."
भाग 2: विश्व के प्रमुख मंदिर (Temples Across the World)
11. Phnom Bakheng (फ्नोम बखेन्ग)
Location: [Angkor, Siem Reap, Cambodia](https://www.google.com/maps/search/?api=1&query=Phnom+Bakheng+Cambodia&authuser=4)
Famous For: 9वीं सदी का मेरु पर्वत के स्वरूप पर बना पिरामिड-शैली का शिव मंदिर, जो सनसेट व्यू के लिए विश्व प्रसिद्ध है।
Famous Local Food / Prasadam: कम्बोडियन फ्रेश फ्रूट प्लैटर, लप खमेर।
AI Image Prompt: "Stepped stone pyramid of Phnom Bakheng temple perched on a hill above the Angkor jungle, stunning fiery orange sunset view overlooking the distant towers of Angkor Wat, ancient weathered stones, 8k travel photography."
12. Prasat Sikhoraphum (प्रसात सिखोंराफुम)
Location: [Surin Province, Thailand](https://www.google.com/maps/search/?api=1&query=Prasat+Sikhoraphum+Thailand&authuser=4)
Famous For: 12वीं सदी का 5 ईंटों के टावरों वाला मंदिर, जिसमें नटराज और अप्सराओं की अत्यंत सुंदर नक्काशी है।
Famous Local Food / Prasadam: थाई नारियल सूप (Tom Kha - शाकाहारी), मैंगो स्टिकी राइस।
AI Image Prompt: "Five ancient reddish brick and sandstone spires of Prasat Sikhoraphum reflecting in a surrounding lotus-filled moat, intricate carved stone lintel of dancing Shiva, soft daytime tropical light, hyper-detailed."
13. Sri Ranganatha Temple (श्री रंगनाथ मंदिर, पोमोना)
Location: [Pomona, New York, USA](https://www.google.com/maps/search/?api=1&query=Sri+Ranganatha+Temple+Pomona+NY&authuser=4)
Famous For: उत्तरी अमेरिका में भगवान रंगनाथ का सबसे बड़ा और सबसे प्रामाणिक द्रविड़ शैली का मंदिर परिसर।
Famous Local Food / Prasadam: पुलिहोरा (इमली चावल), पोंगल, मैसूर पाक।
AI Image Prompt: "Authentic South Indian Rajagopuram of the Sri Ranganatha Temple in Pomona New York, surrounded by lush American maple forest in vibrant autumn red and orange foliage, crisp morning sunlight, 8k realism."
14. Pura Taman Ayun (पुरा तमन अयुन)
Location: [Mengwi, Badung, Bali, Indonesia](https://www.google.com/maps/search/?api=1&query=Pura+Taman+Ayun+Bali&authuser=4)
Famous For: यूनेस्को धरोहर, चारों ओर जल नहरों और खिले हुए कमल के फूलों से घिरा 'शाही उद्यान मंदिर'।
Famous Local Food / Prasadam: बालिनीज पपीता सलाद, नारियल पानी, लक्सा (शाकाहारी)।
AI Image Prompt: "Picturesque multi-tiered black thatched roof Meru shrines of Pura Taman Ayun rising above a serene lotus-covered water moat, lush tropical garden with manicured frangipani trees, tranquil morning reflection, photorealistic."
15. Shri Shiva Vishnu Temple (शिव विष्णु मंदिर, साउथ फ्लोरिडा)
Location: [Southwest Ranches, Florida, USA](https://www.google.com/maps/search/?api=1&query=Shiva+Vishnu+Temple+South+Florida&authuser=4)
Famous For: फ्लोरिडा के पाम के पेड़ों के बीच स्थित पारंपरिक सफेद और पेस्टल नक्काशीदार गोपुरम वाला भव्य मंदिर।
Famous Local Food / Prasadam: मसाला डोसा, वड़ा, पायसम।
AI Image Prompt: "Pristine white hand-sculpted Dravidian temple towers of the Shiva Vishnu Temple in Florida, tropical palm trees against a clear blue sky, bright sunny reflection in the temple entrance pond, hyper-realistic 8k architectural shot."
भाग 1: भारत के प्रमुख मंदिर (Temples of India)
1. Ekambareswarar Temple (एकांबरेश्वर मंदिर)
Location: [Kanchipuram, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Ekambareswarar+Temple+Kanchipuram&authuser=4)
Famous For: पंचभूत स्थलों में 'पृथ्वी' (Earth) तत्व का प्रतिनिधित्व करने वाला मंदिर, जहाँ कांचीपुरम का 194 फीट ऊंचा विशाल राजगोपुरम और 3500 साल पुराना पवित्र आम का पेड़ स्थित है।
Famous Local Food / Prasadam: कांचीपुरम इडली (काली मिर्च और अदरक के स्वाद वाली), पुलियोदरे, मैसूर पाक।
AI Image Prompt: "Towering 59-meter white Dravidian Rajagopuram of the ancient Ekambareswarar Temple in Kanchipuram, a sprawling stone courtyard with thousand-pillar hall details, morning sunlight casting dramatic shadows on ancient granite, 8k hyper-realistic."
2. Trimbakeshwar / Grishneshwar style - Jambukeswarar Temple (जंबुकेश्वर मंदिर, थिरुवानाईकवल)
Location: [Tiruchirappalli, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Jambukeswarar+Temple+Thiruvanaikaval&authuser=4)
Famous For: पंचभूत स्थलों में 'जल' (Water) तत्व का प्रतिनिधित्व करने वाला मंदिर, जहाँ गर्भगृह के शिवलिंग के नीचे से निरंतर प्राकृतिक जल की धारा बहती है।
Famous Local Food / Prasadam: अप्पम, मधुर पोंगल, त्रिची फिल्टर कॉफी।
AI Image Prompt: "Atmospheric stone sanctum of Jambukeswarar Temple with clear spring water gently bubbling around the base of the sacred Shivalinga, flickering brass oil lamps reflecting in water ripples, ancient Chola stone carvings, photorealistic."
3. Annamalaiyar Temple (अरुणाचलेश्वर मंदिर, तिरुवन्नामलाई)
Location: [Tiruvannamalai, Tamil Nadu](https://www.google.com/maps/search/?api=1&query=Annamalaiyar+Temple+Tiruvannamalai&authuser=4)
Famous For: पंचभूत स्थलों में 'अग्नि' (Fire) तत्व का प्रतिनिधित्व करने वाला विशाल मंदिर, जो पवित्र अरुणाचल पहाड़ी की तलहटी में स्थित है और 'कार्तिकई दीपम' के लिए प्रसिद्ध है।
Famous Local Food / Prasadam: पोंगल, वड़ा, केले के पत्ते पर परोसी गई पारंपरिक तमिल सात्विक थाली।
AI Image Prompt: "A sweeping wide-angle view of the massive Annamalaiyar Temple complex with its four giant gopurams standing before the sacred, mist-veiled red-hued Arunachala Hill, golden dusk light, glowing temple lamps, ultra-detailed 8k."
4. Sarnath Mulagandha Kuti Vihara & Dhamek Stupa (सारनाथ मंदिर व स्तूप)
Location: [Sarnath, Varanasi, Uttar Pradesh](https://www.google.com/maps/search/?api=1&query=Dhamek+Stupa+Sarnath&authuser=4)
Famous For: वह पावन भूमि जहाँ भगवान बुद्ध ने ज्ञान प्राप्ति के बाद अपना पहला उपदेश (धर्मचक्र प्रवर्तन) दिया था।
Famous Local Food / Prasadam: बनारसी कचौरी, लाल पेड़ा, सत्तू पराठा।
AI Image Prompt: "Ancient cylindrical stone-carved Dhamek Stupa and the neighboring Mulagandha Kuti Vihara in Sarnath, surrounded by manicured green deer park lawns, soft golden morning haze, monks in saffron robes praying, photorealistic 8k."
5. Shrinathji Temple (श्रीनाथजी मंदिर, नाथद्वारा)
Location: [Nathdwara, Rajsamand, Rajasthan](https://www.google.com/maps/search/?api=1&query=Shrinathji+Temple+Nathdwara&authuser=4)
Famous For: पुष्टिमार्ग का प्रमुख वैष्णव पीठ, जहाँ भगवान श्री कृष्ण के 7 वर्षीय बाल स्वरूप की 'हवेली संगीत' और 'पिछवाई कला' के साथ पूजा होती है।
Famous Local Food / Prasadam: थोर (पारंपरिक मीठा प्रसाद), पुदीना चाय, नाथद्वारा की प्रसिद्ध कंदोई जलेबी और खमण।
AI Image Prompt: "Traditional Rajasthani Haveli style facade of Shrinathji Temple in Nathdwara decorated with intricate Pichwai lotus paintings on white lime-washed walls, brass lamps glowing at sandhya aarti, vibrant festive atmosphere, 8k realistic."
6. Mahalakshmi Temple, Kolhapur (कोल्हापुर महालक्ष्मी / अंबाबाई मंदिर)
Location: [Kolhapur, Maharashtra](https://www.google.com/maps/search/?api=1&query=Mahalakshmi+Temple+Kolhapur&authuser=4)
Famous For: 18 महा शक्तिपीठों में शामिल, जहाँ 'किरणोत्सव' के दौरान सूर्य की किरणें सीधे माँ महालक्ष्मी के विग्रह के चरणों से मुख तक जाती हैं।
Famous Local Food / Prasadam: लाडू प्रसादम, कोल्हापुरी मिसल (झणझणीत), भाकरी।
AI Image Prompt: "Hemadpanthi black basalt stone shikhara of the historic Mahalakshmi Temple in Kolhapur, dramatic sunbeam cutting through the stone entrance pillars directly illuminating the inner courtyard, 8k architectural photo."
7. Vadakkunnathan Temple (वडक्कुन्नाथन मंदिर)
Location: [Thrissur, Kerala](https://www.google.com/maps/search/?api=1&query=Vadakkunnathan+Temple+Thrissur&authuser=4)
Famous For: यूनेस्को एशिया-पैसिफिक हेरिटेज पुरस्कार विजेता, 1000 साल पुराना केरल काष्ठ-वास्तुकला और विशाल 'त्रिशूर पूरम' उत्सव का केंद्र।
Famous Local Food / Prasadam: नेई-अप्पम, पाल पायसम, अवियल।
AI Image Prompt: "Iconic Kerala-style sloping multi-tiered tiled roofs and massive wooden pillars of Vadakkunnathan Temple inside its vast circular green ground (Thekkinkadu Maidan), traditional bronze oil lamps glowing at dusk, authentic cultural realism."
8. Kashi Kalbhairav Temple (काल भैरव मंदिर, काशी)
Location: [Varanasi, Uttar Pradesh](https://www.google.com/maps/search/?api=1&query=Kaal+Bhairav+Temple+Varanasi&authuser=4)
Famous For: काशी के 'कोतवाल' (रक्षक देव) के रूप में पूजित, जिनके दर्शन के बिना काशी यात्रा अधूरी मानी जाती है।
Famous Local Food / Prasadam: काला तिल-गुड़ा प्रसाद, बनारसी लस्सी, कचौरी।
AI Image Prompt: "Mystical stone doorway of the ancient Kaal Bhairav Temple in the narrow atmospheric alleys of Varanasi, deep orange vermilion and black offerings, thick aromatic dhoop smoke swirling, glowing brass diyas, photorealistic."
9. Alandi Sant Dnyaneshwar Samadhi Mandir (आलंदी समाधि मंदिर)
Location: [Alandi, Pune, Maharashtra](https://www.google.com/maps/search/?api=1&query=Sant+Dnyaneshwar+Maharaj+Samadhi+Mandir+Alandi&authuser=4)
Famous For: 13वीं सदी के महान संत ज्ञानेश्वर महाराज की संजीवन समाधि और इंद्रायणी नदी का पावन तट।
Famous Local Food / Prasadam: पेड़ा, पूरन पोली, खिचड़ी महाप्रसाद।
AI Image Prompt: "Gold-plated pinnacle of the Sant Dnyaneshwar Samadhi Mandir reflecting in the calm waters of the Indrayani River at Alandi, rows of devotees with saffron flags (Warkari varkari tradition), soft evening lights, hyper-realistic."
10. Thousand Pillar Temple (रुद्रेश्वर / हजार स्तंभ मंदिर)
Location: [Hanamkonda, Warangal, Telangana](https://www.google.com/maps/search/?api=1&query=Thousand+Pillar+Temple+Warangal&authuser=4)
Famous For: 12वीं सदी की काकतीय वास्तुकला का अद्भुत उदाहरण, त्रिकूट मंदिर (शिव, विष्णु, सूर्य) और जटिल नक्काशीदार पॉलिश किए गए बेसाल्ट खंभे।
Famous Local Food / Prasadam: सर्वपिंडी (चावल के आटे का पारंपरिक नमकीन पैनकेक), पुलिहोरा, बोब्बातुलु।
AI Image Prompt: "Magnificent star-shaped stone platform and carved monolith Nandi bull of the Kakatiya Thousand Pillar Temple in Warangal, intricate interlocking basalt stone pillars, crisp sunny sky, 8k travel photography."
भाग 2: विश्व के प्रमुख मंदिर (Temples Across the World)
11. Prasat Preah Vihear (प्रियाह विहियर मंदिर)
Location: [Preah Vihear Province, Cambodia](https://www.google.com/maps/search/?api=1&query=Preah+Vihear+Temple+Cambodia&authuser=4)
Famous For: यूनेस्को विश्व धरोहर, डैंग्रेक पर्वत की 525 मीटर ऊंची खड़ी चट्टान (Cliff) के शीर्ष पर बना अद्भुत खमेर शिव मंदिर।
Famous Local Food / Prasadam: नम बान चोक (कम्बोडियन राइस नूडल्स), नारियल पानी।
AI Image Prompt: "Ancient sandstone sanctuary of Preah Vihear Temple perched on the very edge of a sheer cliff overlooking the vast misty plains of Cambodia and Thailand, morning sunrise breaking through clouds, 8k epic landscape photography."
12. Sri Senpaga Vinayagar Temple (श्री सेन्पागा विनायगर मंदिर)
Location: [Katong, Singapore](https://www.google.com/maps/search/?api=1&query=Sri+Senpaga+Vinayagar+Temple+Singapore&authuser=4)
Famous For: 1850 के दशक में चंपक के पेड़ के नीचे स्थापित भगवान गणेश का मंदिर, जो अपनी अनूठी चोल-शैली की वास्तुकला और संगीत मंडप के लिए प्रसिद्ध है।
Famous Local Food / Prasadam: मोदक, वड़ा, मसाला चाय।
AI Image Prompt: "Grand 68-foot tall golden-crested Gopuram of Sri Senpaga Vinayagar Temple in Katong Singapore, clean tropical street in foreground, detailed relief sculptures of Ganesha forms, bright sunny day, photorealistic."
13. BAPS Shri Swaminarayan Mandir (स्वामीनारायण मंदिर, शिकागो)
Location: [Bartlett, Illinois, USA](https://www.google.com/maps/search/?api=1&query=BAPS+Shri+Swaminarayan+Mandir+Chicago&authuser=4)
Famous For: इतालियन करारा संगमरमर और तुर्की चूना पत्थर से मध्य-पश्चिम अमेरिका में बना विशाल नक्काशीदार मंदिर।
Famous Local Food / Prasadam: स्वामीनारायण खिचड़ी, मोहनथाल, ढोकला।
AI Image Prompt: "Incredible hand-carved white marble Shikharas of the BAPS Shri Swaminarayan Mandir in Bartlett Chicago, surrounded by lush manicured garden walkways and sparkling fountains at golden hour, ultra-detailed 8k."
14. Pura Goa Gajah - Elephant Cave Temple (पुरा गोवा गजाह)
Location: [Ubud, Gianyar, Bali, Indonesia](https://www.google.com/maps/search/?api=1&query=Goa+Gajah+Ubud+Bali&authuser=4)
Famous For: 9वीं सदी का प्राचीन शैलकृत गुफा मंदिर, जिसके प्रवेश द्वार पर राक्षसी मुखौटे (Bhoma) की डरावनी-आकर्षक नक्काशी और पवित्र स्नान कुंड हैं।
Famous Local Food / Prasadam: बालिनीज नारियल केक, ताजा ड्रैगन फ्रूट, हर्बल चाय।
AI Image Prompt: "Ancient demonic stone face entrance carved into a solid rock cliff at Goa Gajah (Elephant Cave) in Ubud Bali, moss-covered stone bathing pools with female fountain figures in foreground, dense tropical jungle surroundings, 8k realism."
15. Shri Shiva Mandir (श्री शिव मंदिर, मिंटो)
Location: [Minto, New South Wales, Australia](https://www.google.com/maps/search/?api=1&query=Shri+Shiva+Mandir+Minto+NSW&authuser=4)
Famous For: ऑस्ट्रेलिया के सबसे पुराने हिंदू मंदिरों में से एक, जो प्राकृतिक बुशशैल (Eucalyptus bushland) की शांति के बीच स्थित है।
Famous Local Food / Prasadam: पोंगल, पंचामृत, सात्विक खिचड़ी।
AI Image Prompt: "White and saffron painted traditional temple dome of the Shri Shiva Mandir in Minto, nestled amidst natural Australian eucalyptus bushland, kangaroos grazing peacefully in the distance, warm evening sunlight, photorealistic."
भाग 1: भारत के प्रमुख मंदिर (Temples of India)
1. Jagannath Temple, Ahmedabad (जगन्नाथ मंदिर, अहमदाबाद)
Location: [Jamalpur, Ahmedabad, Gujarat](https://www.google.com/maps/search/?api=1&query=Shree+Jagannath+Mandir+Ahmedabad&authuser=4)
Famous For: पुरी (ओडिशा) के बाद भारत की दूसरी सबसे बड़ी और ऐतिहासिक 'रथ यात्रा' उत्सव का केंद्र।
Famous Local Food / Prasadam: खिचड़ी भोग, गुजराती मोहनथाल, फाफड़ा-जलेबी।
AI Image Prompt: "A realistic, atmospheric shot of the intricately carved sandstone Jagannath Temple in Ahmedabad, depicting the three grand chariots (Raths) starting the procession, thousands of devotees gathering with flags, bright traditional lighting at dusk, 8k professional photography."
2. Dwarkadhish Temple (गोमती द्वारका / जगत मंदिर)
Location: [Dwarka, Devbhumi Dwarka, Gujarat](https://www.google.com/maps/search/?api=1&query=Dwarkadhish+Temple+Dwarka&authuser=4)
Famous For: चार धामों में प्रमुख पश्चिमी धाम, जहाँ 72 स्तंभों वाला 5-मंजिला 'जगत मंदिर' गोमती नदी के संगम पर स्थित है और इसका 52-गज का ध्वज विशेष है।
Famous Local Food / Prasadam: माखन-मिश्री भोग, द्वारका का पेड़ा, गुजराती कढ़ी-खिचड़ी।
AI Image Prompt: "Monumental 72-pillared sandstone Dwarkadhish Temple towering above the confluence of Gomti River and Arabian Sea, giant 52-yard sacred flag fluttering vigorously in the sea breeze, dramatic clear sunny day, hyper-realistic 8k."
3. Dakor Ranchhodraiji Temple (डाकोर रणछोड़रायजी मंदिर)
Location: [Dakor, Kheda District, Gujarat](https://www.google.com/maps/search/?api=1&query=Ranchhodraiji+Temple+Dakor&authuser=4)
Famous For: गुजरात का महत्वपूर्ण कृष्ण मंदिर, जहाँ भगवान श्री कृष्ण के 'रणछोड़' स्वरूप की भव्य नक्काशीदार चाँदी के सिंहासन पर पूजा होती है।
Famous Local Food / Prasadam: डाकोर के गोटे (मेथी के भजिये), पेड़ा, श्रीखंड.
AI Image Prompt: "A stunning architectural photograph of the ornate silver doors and carved white lime-washed facade of Dakor Ranchhodraiji Temple, bathed in warm sandhya aarti lamp light, golden glow, intricate details, photorealistic."
4. Pavagadh Kalika Mata Temple (पावागढ़ कालिका माता मंदिर)
Location: [Pavagadh, Panchmahal District, Gujarat](https://www.google.com/maps/search/?api=1&query=Pavagadh+Mahakali+Temple&authuser=4)
Famous For: पावागढ़ पहाड़ी की चोटी पर स्थित प्रमुख शक्तिपीठ, जहाँ नवनिर्मित शिखर और ध्वज का विशेष महत्व है, यह यूनेस्को धरोहर चंपानेर परिसर का हिस्सा है।
Famous Local Food / Prasadam: माताजी की चुनरी और लाल सिंदूर, गुजराती सुखड़ी, खिचड़ी भोग.
AI Image Prompt: "Colossal red and gold Shikhara of Kalika Mata Temple perched atop the rugged Pavagadh hill cliff, glowing brilliantly under twilight sky, panoramic view of historical Champaner plains far below, 8k epic landscape realism."
5. Shamlaji Temple (शामलाजी मंदिर / गदाधर मंदिर)
Location: [Sabarkantha District, Gujarat](https://www.google.com/maps/search/?api=1&query=Shamlaji+Temple+Gujarat&authuser=4)
Famous For: 11वीं सदी का भगवान विष्णु के 'शामलाजी' (काले विग्रह) स्वरूप का प्राचीन मंदिर, जो मही नदी के तट पर स्थित है और अपने कार्तिक पूर्णिमा मेले के लिए प्रसिद्ध है।
Famous Local Food / Prasadam: गुजराती दाल-ढोकली, खमण, बेसन के लड्डू.
AI Image Prompt: "Historic ancient Shamlaji temple built with black stone and limestone on the banks of Mahi river in Gujarat, intricate carvings, soft golden hour sunlight, traditional oil lamps, highly detailed photorealistic shot."
6. Sun Temple, Modhera (मोढेरा सूर्य मंदिर)
Location: [Mehsana District, Gujarat](https://www.google.com/maps/search/?api=1&query=Sun+Temple+Modhera+Gujarat&authuser=4)
Famous For: सोलंकी राजवंश की स्थापत्य कला का शिखर, जहाँ 'सूर्य कुंड' (विशाल बावड़ी) में 108 लघु मंदिर हैं और गर्भगृह में सूर्य की पहली किरण सीधे विग्रह पर पड़ती है (अब केवल कुंड)।
Famous Local Food / Prasadam: गुजराती खमण, थेपला, सुखड़ी मिठाई.
AI Image Prompt: "Intricately carved sandstone Sun Temple of Modhera in Gujarat, symmetrical stone steps of the magnificent Surya Kund stepwell in foreground, golden morning light striking the pillared Sabha Mandap, ultra-realistic 8k architectural shot."
7. Hutheesing Jain Temple (हठीसिंह जैन मंदिर)
Location: [Ahmedabad, Gujarat](https://www.google.com/maps/search/?api=1&query=Hutheesing+Jain+Temple&authuser=4)
Famous For: 19वीं सदी का पूरी तरह से नक्काशीदार सफेद संगमरमर से बना भव्य जैन मंदिर, जो अपनी बेजोड़ कला और शांति के लिए जाना जाता है।
Famous Local Food / Prasadam: शुद्ध शाकाहारी भोजन, गुजराती मोहनथाल, पेड़ा.
AI Image Prompt: "A symmetrical deep perspective view down the forest of light-amber marble pillars inside Hutheesing Jain Temple in Ahmedabad, sunlight casting soft geometric shadows across the polished floor, detailed sculptures, 8k."
8. Akshardham, Gandhinagar (अक्षरधाम मंदिर, गांधीनगर)
Location: [Gandhinagar, Gujarat](https://www.google.com/maps/search/?api=1&query=BAPS+Shri+Swaminarayan+Akshardham+Gandhinagar&authuser=4)
Famous For: आधुनिक युग का स्थापत्य चमत्कार, हाथ से नक्काशीदार गुलाबी बलुआ पत्थर से बना मंदिर और प्रसिद्ध 'सत्-चित्-आनंद' वाटर शो।
Famous Local Food / Prasadam: सात्विक महाप्रसाद, गुजराती थाली, लड्डू प्रसादम.
AI Image Prompt: "Colossal Swaminarayan Akshardham Temple in Gandhinagar, hand-carved pink sandstone architecture glowing with warm light, reflecting in surrounding water moat at twilight, clear starry sky, hyper-detailed photorealistic rendering."
9. Bileshwar Mahadev Temple (बिलेश्वर महादेव मंदिर)
Location: [Bileshwar, Devbhumi Dwarka, Gujarat](https://www.google.com/maps/search/?api=1&query=Bileshwar+Mahadev+Temple&authuser=4)
Famous For: 7वीं सदी का प्राचीन शिव मंदिर, जो बिल्व पत्रों के ढेर (बिलेश्वर) से शिवलिंग प्रकट होने की मान्यता के लिए प्रसिद्ध है, यह अपनी प्राचीन स्थापत्य कला के लिए संरक्षित है।
Famous Local Food / Prasadam: पेड़ा, सुखड़ी मिठाई, गुजराती खिचड़ी.
AI Image Prompt: "Historic ancient gray stone Bileshwar Mahadev temple in Dwarka district of Gujarat, intricately carved pillars, surrounded by sacred banyan trees, soft early morning mist, highly accurate architectural details, realistic."
10. Bhalka Tirtha (भालका तीर्थ)
Location: [Veraval, Gir Somnath District, Gujarat](https://www.google.com/maps/search/?api=1&query=Bhalka+Tirtha+Somnath&authuser=4)
Famous For: वह पावन स्थान जहाँ भगवान श्री कृष्ण को 'जरा' नामक शिकारी ने हिरण समझकर तीर मारा था और उन्होंने अपनी देह लीला समाप्त की थी।
Famous Local Food / Prasadam: लड्डू प्रसादम, गुजराती भोजन थाली, सोमनाथ पेड़ा.
AI Image Prompt: "Vibrant colored arched facade of Bhalka Tirtha temple where Lord Krishna left his body, pristine coastline rushing beside the shrine, morning sun rays piercing coastal mist, hyper-detailed 8k photorealistic."
भाग 2: विश्व के प्रमुख मंदिर (Temples Across the World)
11. BAPS Shri Swaminarayan Mandir, Houston (अक्षरधाम मंदिर, ह्यूस्टन)
Location: [Stafford, Texas, USA](https://www.google.com/maps/search/?api=1&query=BAPS+Shri+Swaminarayan+Mandir+Stafford+TX&authuser=4)
Famous For: उत्तरी अमेरिका का पहला पारंपरिक हाथ से नक्काशीदार गुलाबी बलुआ पत्थर और इतालियन संगमरमर से बना हिंदू मंदिर।
Famous Local Food / Prasadam: सात्विक महाप्रसाद, गुजराती थाली, मोहनथाल मिठाई.
AI Image Prompt: "Massive, incredibly intricately carved pink sandstone Swaminarayan Akshardham Temple in Stafford, Texas, illuminated water fountains in the courtyard, clear twilight sky with faint Houston skyline, photorealistic architectural photo."
12. Sri Meenakshi Devasthanam (मीनाक्षी अम्मन मंदिर, ह्यूस्टन)
Location: [Pearland, Texas, USA](https://www.google.com/maps/search/?api=1&query=Sri+Meenakshi+Devasthanam+Pearland+TX&authuser=4)
Famous For: उत्तरी अमेरिका में देवी मीनाक्षी और सुंदरेश्वर का द्रविड़ शैली का पारंपरिक मंदिर, जो मदुरै (भारत) के मूल मंदिर की याद दिलाता है।
Famous Local Food / Prasadam: दक्षिण भारतीय फिल्टर कॉफी, नारियल पानी, कुरकुरा मेदु वड़ा.
AI Image Prompt: "Grand multi-colored Rajagopuram tower of Sri Meenakshi Temple in Pearland, Texas, intricate richly painted deity carvings, tropical palm trees against a deep blue Texas sky, highly detailed realistic shot."
13. Shri Swaminarayan Mandir, Lilburn-Atlanta (अक्षरधाम मंदिर, अटलांटा)
Location: [Lilburn, Georgia, USA](https://www.google.com/maps/search/?api=1&query=BAPS+Shri+Swaminarayan+Mandir+Lilburn&authuser=4)
Famous For: दक्षिण-पूर्व अमेरिका में हाथ से नक्काशीदार गुलाबी बलुआ पत्थर और सफेद संगमरमर से बना भव्य मंदिर, जो अपनी बेजोड़ कला और शांति के लिए प्रसिद्ध है।
Famous Local Food / Prasadam: गुजराती कढ़ी-खिचड़ी, जलेबी, सात्विक थाली.
AI Image Prompt: "A stunning architectural photograph of the white Carrara marble and Bulgarian limestone BAPS Shri Swaminarayan Mandir in Lilburn, Georgia, perfectly manicured traditional lawns and fountains in foreground, golden evening light, 8k resolution."
14. Prasat Prasat Ta Krabey (प्रसात ता क्राबे)
Location: [Preah Vihear Province, Cambodia](https://www.google.com/maps/search/?api=1&query=Prasat+Ta+Krabey+Cambodia&authuser=4)
Famous For: खमेर राजवंश द्वारा 10वीं सदी में लाल बलुआ पत्थर से बनाया गया भगवान शिव को समर्पित मंदिर, जो अपनी बारीक नक्काशी और ऐतिहासिक महत्व के लिए जाना जाता है।
Famous Local Food / Prasadam: Num Pang (कम्बोडियन सैंडविच), नारियल चावल.
AI Image Prompt: "Hyper-detailed close-up view of the 10th-century pink sandstone temple of Prasat Ta Krabey in Cambodia, intricate miniature bas-reliefs of Hindu epics, dappled jungle sunlight filtering through tropical canopy, 8k photography."
15. Shri Shiva Vishnu Temple (शिव विष्णु मंदिर, डलास)
Location: [Carrollton, Texas, USA](https://www.google.com/maps/search/?api=1&query=Shri+Shiva+Vishnu+Temple+Carrollton+TX&authuser=4)
Famous For: डलास-फोर्ट वर्थ क्षेत्र में स्थित पारंपरिक द्रविड़ शैली का भव्य मंदिर, जहाँ भगवान शिव और विष्णु की एक साथ पूजा होती है।
Famous Local Food / Prasadam: पोंगल, पंचामृत, सात्विक खिचड़ी.
AI Image Prompt: "White and saffron painted traditional temple domes of the Shri Shiva Mandir in Carrollton, Texas, nestled amidst natural Texas oak trees, a warm evening sunlight, highly realistic architectural shot."
"""

# Parse sections
india_temples = []
world_temples = []

# Split by section markers
parts = re.split(r'भाग\s*[12]:', raw_data)

seen_names = set()

def normalize_key(name):
    # Strip brackets, english, whitespace
    name = re.sub(r'\(.*?\)', '', name)
    name = re.sub(r'[^a-zA-Z0-9\u0900-\u097F]', '', name).lower().strip()
    return name

def parse_entries(block, category):
    entries = []
    # match patterns like:
    # 1. Name (English)
    # स्थान/Location: [Loc](url)
    # प्रसिद्ध/Famous For: ...
    # भोजन/प्रसाद/Famous Local Food...: ...
    # AI Image Prompt: ...
    
    chunks = re.split(r'\n(?=\d+\.)', block)
    for c in chunks:
        c = c.strip()
        if not c or not re.match(r'^\d+\.', c):
            continue
        
        # Name
        name_line = c.split('\n')[0]
        m_name = re.search(r'^\d+\.\s*([^(]+)(?:\(([^)]+)\))?', name_line)
        if not m_name:
            continue
        name_hi = m_name.group(1).strip()
        name_en = m_name.group(2).strip() if m_name.group(2) else name_hi
        
        norm = normalize_key(name_hi)
        if norm in seen_names:
            print(f"Skipping duplicate: {name_hi}")
            continue
        seen_names.add(norm)
        
        # Location
        loc_text = ""
        map_url = ""
        m_loc = re.search(r'(?:स्थान|Location):\s*\[([^\]]+)\]\(([^)]+)\)', c)
        if m_loc:
            loc_text = m_loc.group(1).strip()
            map_url = m_loc.group(2).strip()
        else:
            m_loc2 = re.search(r'(?:स्थान|Location):\s*([^\n]+)', c)
            if m_loc2:
                loc_text = m_loc2.group(1).strip()
                map_url = f"https://www.google.com/maps/search/?api=1&query={loc_text.replace(' ', '+')}"
        
        # Famous for
        famous = ""
        m_fam = re.search(r'(?:प्रसिद्ध|Famous For):\s*([^\n]+)', c)
        if m_fam:
            famous = m_fam.group(1).strip()
            
        # Food / Prasadam
        food = ""
        m_food = re.search(r'(?:भोजन/प्रसाद|Famous Local Food[^:]*):\s*([^\n]+)', c)
        if m_food:
            food = m_food.group(1).strip()
            
        # Prompt
        prompt = ""
        m_prompt = re.search(r'AI Image Prompt:\s*"([^"]+)"', c)
        if m_prompt:
            prompt = m_prompt.group(1).strip()
            
        slug = re.sub(r'[^a-zA-Z0-9]', '_', name_en.lower()).strip('_')
        
        entries.append({
            'id': f"temple_{slug}_{len(seen_names)}",
            'nameHi': name_hi,
            'nameEn': name_en,
            'location': loc_text,
            'mapUrl': map_url,
            'famous': famous,
            'food': food,
            'prompt': prompt,
            'category': category,
            'img': 'assets/panchang_book.jpg', # placeholder default
            'fallbackImg': 'assets/app_logo_circle.png'
        })
    return entries

# Process parts
for p in parts:
    if 'भारत के' in p:
        india_temples.extend(parse_entries(p, 'india'))
    elif 'विश्व के' in p:
        world_temples.extend(parse_entries(p, 'world'))

print(f"Total Unique India Temples: {len(india_temples)}")
print(f"Total Unique World Temples: {len(world_temples)}")

# Save parsed JSON for reference
with open(BASE_DIR / "data_india_temples.json", "w", encoding="utf-8") as f:
    json.dump(india_temples, f, ensure_ascii=False, indent=2)

with open(BASE_DIR / "data_world_temples.json", "w", encoding="utf-8") as f:
    json.dump(world_temples, f, ensure_ascii=False, indent=2)

print("Saved JSON datasets successfully.")
