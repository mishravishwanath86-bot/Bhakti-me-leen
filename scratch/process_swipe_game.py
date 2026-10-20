import os
import sys
import glob
import json
import shutil
from PIL import Image, ImageDraw, ImageFont

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
CARDS_DIR = os.path.join(BASE_DIR, "assets", "cards")
GATES_DIR = os.path.join(BASE_DIR, "assets", "gates")

os.makedirs(CARDS_DIR, exist_ok=True)
os.makedirs(GATES_DIR, exist_ok=True)

# 1. CATEGORY 1: रामायण आरंभ (40 Cards)
cat1_raw = [
  {"id": "c1_01", "name": "राम", "desc": "दशरथ और कौशल्या के ज्येष्ठ पुत्र, रघुकुल शिरोमणि।", "correctSwipe": "LEFT", "slug": "ram"},
  {"id": "c1_02", "name": "सीता", "desc": "राजा जनक की कन्या, भूमिपुत्री वैदेही।", "correctSwipe": "RIGHT", "slug": "sita"},
  {"id": "c1_03", "name": "लक्ष्मण", "desc": "सुमित्रा के पुत्र, सदैव राम की सेवा में तत्पर।", "correctSwipe": "LEFT", "slug": "lakshman"},
  {"id": "c1_04", "name": "उर्मिला", "desc": "राजा जनक की कन्या, लक्ष्मण की पत्नी।", "correctSwipe": "RIGHT", "slug": "urmila"},
  {"id": "c1_05", "name": "भरत", "desc": "कैकेयी के पुत्र, राम के परम भक्त।", "correctSwipe": "LEFT", "slug": "bharat"},
  {"id": "c1_06", "name": "मांडवी", "desc": "कुशध्वज की पुत्री, भरत की पत्नी।", "correctSwipe": "RIGHT", "slug": "mandavi"},
  {"id": "c1_07", "name": "शत्रुघ्न", "desc": "सुमित्रा के कनिष्ठ पुत्र, लवणासुर वधक।", "correctSwipe": "LEFT", "slug": "shatrughna"},
  {"id": "c1_08", "name": "श्रुतकीर्ति", "desc": "कुशध्वज की कन्या, शत्रुघ्न की पत्नी।", "correctSwipe": "RIGHT", "slug": "shrutakirti"},
  {"id": "c1_09", "name": "दशरथ", "desc": "अयोध्या के सूर्यवंशी चक्रवर्ती सम्राट।", "correctSwipe": "LEFT", "slug": "dasharatha"},
  {"id": "c1_10", "name": "जनक", "desc": "विदेह राज, सीता के दार्शनिक पिता।", "correctSwipe": "RIGHT", "slug": "janak"},
  {"id": "c1_11", "name": "कौशल्या", "desc": "दशरथ की पटरानी, श्रीराम की माता।", "correctSwipe": "LEFT", "slug": "kaushalya"},
  {"id": "c1_12", "name": "सुनयना", "desc": "जनक की पटरानी, सीता की वात्सल्यमयी माता।", "correctSwipe": "RIGHT", "slug": "sunayana"},
  {"id": "c1_13", "name": "कैकेयी", "desc": "दशरथ की दूसरी रानी, भरत की माता।", "correctSwipe": "LEFT", "slug": "kaikeyi"},
  {"id": "c1_14", "name": "कुशध्वज", "desc": "राजा जनक के अनुज, सांकाश्य के राजा।", "correctSwipe": "RIGHT", "slug": "kushadhwaja"},
  {"id": "c1_15", "name": "सुमित्रा", "desc": "लक्ष्मण और शत्रुघ्न की बुद्धिमती माता।", "correctSwipe": "LEFT", "slug": "sumitra"},
  {"id": "c1_16", "name": "वशिष्ठ", "desc": "रघुकुल के कुलगुरु, सप्तर्षि में से एक।", "correctSwipe": "LEFT", "slug": "vashishtha"},
  {"id": "c1_17", "name": "शतानंद", "desc": "महर्षि गौतम और अहल्या के पुत्र, जनक के कुलगुरु।", "correctSwipe": "RIGHT", "slug": "shatananda"},
  {"id": "c1_18", "name": "सुमंत", "desc": "राजा दशरथ के अत्यंत निष्ठावान महामात्य व सारथी।", "correctSwipe": "LEFT", "slug": "sumanta"},
  {"id": "c1_19", "name": "अहल्या", "desc": "मिथिला उपवन में राम के चरण स्पर्श से मुक्त हुई ऋषि पत्नी।", "correctSwipe": "RIGHT", "slug": "ahilya"},
  {"id": "c1_20", "name": "मंथरा", "desc": "कैकेयी की कुबड़ी दासी, जिसने कुमंत्रणा दी।", "correctSwipe": "LEFT", "slug": "manthara"},
  {"id": "c1_21", "name": "याज्ञवल्क्य", "desc": "राजा जनक की सभा के महानतम दार्शनिक ऋषि।", "correctSwipe": "RIGHT", "slug": "yajnavalkya"},
  {"id": "c1_22", "name": "ऋष्यशृंग", "desc": "दशरथ का पुत्रकामेष्टि यज्ञ कराने वाले मुनि।", "correctSwipe": "LEFT", "slug": "rishyashringa"},
  {"id": "c1_23", "name": "गार्गी", "desc": "जनक के दरबार में शास्त्रार्थ करने वाली ब्रह्मवादिनी।", "correctSwipe": "RIGHT", "slug": "gargi"},
  {"id": "c1_24", "name": "शांता", "desc": "राजा दशरथ व कौशल्या की ज्येष्ठ पुत्री।", "correctSwipe": "LEFT", "slug": "shanta"},
  {"id": "c1_25", "name": "मैत्रेयी", "desc": "मिथिला की विदुषी, याज्ञवल्क्य की ज्ञानपिपासु पत्नी।", "correctSwipe": "RIGHT", "slug": "maitreyi"},
  {"id": "c1_26", "name": "पिनाक (शिव धनुष)", "desc": "राजा जनक के राजभवन में रखा गया महाधनुष।", "correctSwipe": "RIGHT", "slug": "pinaka"},
  {"id": "c1_27", "name": "पुष्पवाटिका", "desc": "मिथिला का वह उपवन जहाँ सीता-राम का प्रथम मिलन हुआ।", "correctSwipe": "RIGHT", "slug": "pushpavatika"},
  {"id": "c1_28", "name": "सरयू नदी", "desc": "अयोध्या की पावन जीवनदायिनी नदी।", "correctSwipe": "LEFT", "slug": "sarayu_nadi"},
  {"id": "c1_29", "name": "नंदीग्राम", "desc": "वह स्थान जहाँ भरत ने पादुका रखकर राजकाज संभाला।", "correctSwipe": "LEFT", "slug": "nandigram"},
  {"id": "c1_30", "name": "स्वयंवर मंडप", "desc": "मिथिला का विशाल राजदरबार जहाँ धनुष यज्ञ हुआ।", "correctSwipe": "RIGHT", "slug": "swayamvar_mandap"},
  {"id": "c1_31", "name": "कनक भवन", "desc": "अयोध्या में सीता के स्वागत हेतु भेंट किया गया स्वर्ण महल।", "correctSwipe": "LEFT", "slug": "kanak_bhavan"},
  {"id": "c1_32", "name": "गंगा-सोन संगम", "desc": "विश्वामित्र संग यात्रा का मिथिला मार्ग पड़ाव।", "correctSwipe": "RIGHT", "slug": "ganga_son_sangam"},
  {"id": "c1_33", "name": "सूर्यवंशी ध्वज", "desc": "अयोध्या की राजप्राचीर पर लहराने वाला ध्वज।", "correctSwipe": "LEFT", "slug": "suryavanshi_dhwaja"},
  {"id": "c1_34", "name": "विदेह राजपताका", "desc": "मिथिला का पवित्र राज्य चिह्न ध्वज।", "correctSwipe": "RIGHT", "slug": "videha_rajpataka"},
  {"id": "c1_35", "name": "ताड़का वन", "desc": "अयोध्या से मिथिला जाते समय मुक्त कराया गया भयावह वन।", "correctSwipe": "LEFT", "slug": "tadaka_vana"},
  {"id": "c1_36", "name": "जयमाला", "desc": "सीता द्वारा प्रभु राम के गले में डाली गई वरमाला।", "correctSwipe": "RIGHT", "slug": "jayamala"},
  {"id": "c1_37", "name": "हलकर्षण उत्सव", "desc": "जनक द्वारा धरती जोतने का मंगलकारी उत्सव।", "correctSwipe": "RIGHT", "slug": "halkarshan_utsav"},
  {"id": "c1_38", "name": "सुमित्रा प्रासाद", "desc": "अयोध्या का शांत और साधनायुक्त राजमहल।", "correctSwipe": "LEFT", "slug": "sumitra_prasad"},
  {"id": "c1_39", "name": "अश्वमेध अश्व", "desc": "अयोध्या के दिग्विजय का दिव्य श्वेत अश्व।", "correctSwipe": "LEFT", "slug": "ashwamedha_ashwa"},
  {"id": "c1_40", "name": "विश्वामित्र", "desc": "राम-लक्ष्मण को यज्ञ रक्षा और मिथिला ले जाने वाले गुरु।", "correctSwipe": "LEFT", "slug": "vishwamitra"}
]

# 2. CATEGORY 2: लंका युद्ध (35 Cards)
cat2_raw = [
  {"id": "c2_01", "name": "हनुमान", "desc": "अतुलितबलधामं, लंका दहन करने वाले पवनपुत्र।", "correctSwipe": "LEFT", "slug": "hanuman"},
  {"id": "c2_02", "name": "रावण", "desc": "दस सिरों और बीस भुजाओं वाला लंकाधिपति।", "correctSwipe": "RIGHT", "slug": "ravan"},
  {"id": "c2_03", "name": "सुग्रीव", "desc": "किष्किंधा के वानर राज, राम के मित्र।", "correctSwipe": "LEFT", "slug": "sugriva"},
  {"id": "c2_04", "name": "मेघनाद (इंद्रजीत)", "desc": "रावण का ज्येष्ठ पुत्र, ब्रह्मास्त्र धारक।", "correctSwipe": "RIGHT", "slug": "meghnad"},
  {"id": "c2_05", "name": "जाम्बवंत", "desc": "ऋक्ष राज, ज्ञान और धैर्य के सागर।", "correctSwipe": "LEFT", "slug": "jambavant"},
  {"id": "c2_06", "name": "कुंभकर्ण", "desc": "छह माह तक सोने वाला विशालकाय राक्षस।", "correctSwipe": "RIGHT", "slug": "kumbhkaran"},
  {"id": "c2_07", "name": "अंगद", "desc": "बालि-पुत्र, जिनका पाँव लंका सभा में अडिग रहा।", "correctSwipe": "LEFT", "slug": "angada"},
  {"id": "c2_08", "name": "शूर्पणखा", "desc": "रावण की बहन, जिसकी नाक लक्ष्मण ने काटी थी।", "correctSwipe": "RIGHT", "slug": "shurpanakha"},
  {"id": "c2_09", "name": "विभीषण", "desc": "धर्म की राह चुनकर राम की शरण में आए रावण-भ्राता।", "correctSwipe": "LEFT", "slug": "vibhishan"},
  {"id": "c2_10", "name": "मारीच", "desc": "स्वर्ण मृग बनकर छल करने वाला मायावी असुर।", "correctSwipe": "RIGHT", "slug": "maricha"},
  {"id": "c2_11", "name": "नल", "desc": "समुद्र पर तैरने वाले पत्थरों से सेतु बनाने वाले शिल्पी।", "correctSwipe": "LEFT", "slug": "nala"},
  {"id": "c2_12", "name": "मन्दोदरी", "desc": "रावण की नीतिवान और पतिव्रता पटरानी।", "correctSwipe": "RIGHT", "slug": "mandodari"},
  {"id": "c2_13", "name": "नील", "desc": "वानर सेना के मुख्य युद्ध सेनापति।", "correctSwipe": "LEFT", "slug": "neela"},
  {"id": "c2_14", "name": "प्रहस्त", "desc": "रावण का मुख्य सेनापति और मामा।", "correctSwipe": "RIGHT", "slug": "prahasta"},
  {"id": "c2_15", "name": "जटायु", "desc": "सीता हरण के समय प्राणों की आहुति देने वाले गृध्र राज।", "correctSwipe": "LEFT", "slug": "jatayu"},
  {"id": "c2_16", "name": "खर", "desc": "जनस्थान का सेनापति, चौदह सहस्र राक्षसों का नायक।", "correctSwipe": "RIGHT", "slug": "khara"},
  {"id": "c2_17", "name": "सम्पाती", "desc": "जटायु के ज्येष्ठ भ्राता, जिन्होंने समुद्र पार लंका देखी।", "correctSwipe": "LEFT", "slug": "sampati"},
  {"id": "c2_18", "name": "दूषण", "desc": "जनस्थान में खर का सह-सेनापति।", "correctSwipe": "RIGHT", "slug": "dushana"},
  {"id": "c2_19", "name": "शबरी", "desc": "मतंग आश्रम की तपस्विनी, बेर खिलाने वाली अनन्य भक्त।", "correctSwipe": "LEFT", "slug": "shabari"},
  {"id": "c2_20", "name": "अक्षयकुमार", "desc": "रावण का कनिष्ठ पुत्र, अशोक वाटिका में वीरगति पाने वाला।", "correctSwipe": "RIGHT", "slug": "akshayakumara"},
  {"id": "c2_21", "name": "सुषेण", "desc": "लंका युद्ध के मुख्य वानर वैद्य, संजीवनी के ज्ञाता।", "correctSwipe": "LEFT", "slug": "sushena"},
  {"id": "c2_22", "name": "अतिकाय", "desc": "रावण और धन्यमालिनी का पर्वतकाय पुत्र।", "correctSwipe": "RIGHT", "slug": "atikaya"},
  {"id": "c2_23", "name": "केसरी", "desc": "हनुमान जी के पराक्रमी वानर पिता।", "correctSwipe": "LEFT", "slug": "kesari"},
  {"id": "c2_24", "name": "त्रिशिरा", "desc": "तीन सिरों वाला शक्तिशाली राक्षस योद्धा।", "correctSwipe": "RIGHT", "slug": "trishira"},
  {"id": "c2_25", "name": "दधिमुख", "desc": "सुग्रीव के मधुवन के रक्षक वानर।", "correctSwipe": "LEFT", "slug": "dadhimukha"},
  {"id": "c2_26", "name": "महिरावण", "desc": "पाताल लोक का स्वामी, तंत्र-मंत्र का मायावी।", "correctSwipe": "RIGHT", "slug": "mahiravana"},
  {"id": "c2_27", "name": "तारा", "desc": "किष्किंधा की महारानी, बालि की बुद्धिमती पत्नी।", "correctSwipe": "LEFT", "slug": "tara"},
  {"id": "c2_28", "name": "कालनेमि", "desc": "हनुमान जी का मार्ग रोकने वाला छली मायावी।", "correctSwipe": "RIGHT", "slug": "kalanemi"},
  {"id": "c2_29", "name": "रुमा", "desc": "सुग्रीव की पत्नी, किष्किंधा की राजमहिषी।", "correctSwipe": "LEFT", "slug": "ruma"},
  {"id": "c2_30", "name": "त्रिजटा", "desc": "अशोक वाटिका में सीता की रक्षा व ढांढस बंधाने वाली राक्षसी।", "correctSwipe": "LEFT", "slug": "trijata"},
  {"id": "c2_31", "name": "संजीवनी बूटी", "desc": "लक्ष्मण के प्राण बचाने वाली द्रोणागिरि की दिव्य औषधि।", "correctSwipe": "LEFT", "slug": "sanjeevani_booti"},
  {"id": "c2_32", "name": "स्वर्ण लंका", "desc": "रावण की अभेद्य त्रिकूट पर्वत पर बसी सोने की नगरी।", "correctSwipe": "RIGHT", "slug": "swarna_lanka"},
  {"id": "c2_33", "name": "राम सेतु", "desc": "भारत से लंका तक निर्मित पाषाण मार्ग।", "correctSwipe": "LEFT", "slug": "ram_setu"},
  {"id": "c2_34", "name": "पुष्पक विमान", "desc": "आकाश में उड़ने वाला मन की गति से चलने वाला विमान।", "correctSwipe": "RIGHT", "slug": "pushpak_viman"},
  {"id": "c2_35", "name": "अशोक वाटिका", "desc": "रावण का वह उद्यान जहाँ सीता जी को बंदी रखा गया।", "correctSwipe": "RIGHT", "slug": "ashok_vatika"}
]

# 3. CATEGORY 3: महाभारत (25 Cards)
cat3_raw = [
  {"id": "c3_01", "name": "अर्जुन", "desc": "गांडीवधारी, श्रीकृष्ण के प्रिय सखा पार्थ।", "correctSwipe": "LEFT", "slug": "arjun"},
  {"id": "c3_02", "name": "दुर्योधन", "desc": "हस्तिनापुर का अहंकारी ज्येष्ठ कौरव युवराज।", "correctSwipe": "RIGHT", "slug": "duryodhan"},
  {"id": "c3_03", "name": "युधिष्ठिर", "desc": "धर्मराज, सत्य और न्याय के अटूट प्रतीक।", "correctSwipe": "LEFT", "slug": "yudhisthir"},
  {"id": "c3_04", "name": "दुःशासन", "desc": "दुर्योधन का आज्ञाकारी और क्रूर अनुज।", "correctSwipe": "RIGHT", "slug": "dushasan"},
  {"id": "c3_05", "name": "भीम", "desc": "दस सहस्र हाथियों के बल वाले गदाधारी पाण्डव।", "correctSwipe": "LEFT", "slug": "bheem"},
  {"id": "c3_06", "name": "शकुनि", "desc": "गांधार नरेश, चौसर के कपटी पांसों का स्वामी।", "correctSwipe": "RIGHT", "slug": "shakuni"},
  {"id": "c3_07", "name": "कर्ण", "desc": "दानवीर अंगराज, सूर्यपुत्र (कौरव सेनापति)।", "correctSwipe": "RIGHT", "slug": "karna"},
  {"id": "c3_08", "name": "द्रौपदी", "desc": "पांचाल राजकुमारी, पाण्डवों की पटरानी यज्ञसेनी।", "correctSwipe": "LEFT", "slug": "draupadi"},
  {"id": "c3_09", "name": "द्रोणाचार्य", "desc": "कौरव-पाण्डव दोनों के गुरु, कौरव सेना के प्रधान सेनापति।", "correctSwipe": "RIGHT", "slug": "dronacharya"},
  {"id": "c3_10", "name": "अभिमन्यु", "desc": "अर्जुन पुत्र, जिसने अकेले चक्रव्यूह को भेदा।", "correctSwipe": "LEFT", "slug": "abhimanyu"},
  {"id": "c3_11", "name": "अश्वत्थामा", "desc": "गुरु द्रोण के अमर पुत्र, माथे पर दिव्य मणि धारक।", "correctSwipe": "RIGHT", "slug": "ashwatthama"},
  {"id": "c3_12", "name": "कुंती", "desc": "पाण्डवों की पूज्य राजमाता, पांडु की पटरानी।", "correctSwipe": "LEFT", "slug": "kunti"},
  {"id": "c3_13", "name": "गांधारी", "desc": "पतिव्रता महारानी, जिन्होंने आँखों पर पट्टी बांधी।", "correctSwipe": "RIGHT", "slug": "gandhari"},
  {"id": "c3_14", "name": "सहदेव", "desc": "त्रिकालदर्शी कनिष्ठ पाण्डव, नीति और ज्योतिष के ज्ञाता।", "correctSwipe": "LEFT", "slug": "sahadev"},
  {"id": "c3_15", "name": "जयद्रथ", "desc": "सिंधु नरेश, जिसने चक्रव्यूह का द्वार पाण्डवों के लिए रोका।", "correctSwipe": "RIGHT", "slug": "jayadrath"},
  {"id": "c3_16", "name": "नकुल", "desc": "अश्व विद्या और अनुपम सौंदर्य के स्वामी पाण्डव।", "correctSwipe": "LEFT", "slug": "nakul"},
  {"id": "c3_17", "name": "कृपाचार्य", "desc": "कुरु राज्य के कुलगुरु और महारथी।", "correctSwipe": "RIGHT", "slug": "kripacharya"},
  {"id": "c3_18", "name": "विदुर", "desc": "सत्य और नीति के ज्ञाता धर्मनिष्ठ महामति।", "correctSwipe": "LEFT", "slug": "vidur"},
  {"id": "c3_19", "name": "जरासंध", "desc": "मगध का क्रूर सम्राट, कंस का श्वसुर।", "correctSwipe": "RIGHT", "slug": "jarasandh"},
  {"id": "c3_20", "name": "घटोत्कच", "desc": "भीम और हिडिम्बा का महाबली मायावी असुर पुत्र।", "correctSwipe": "LEFT", "slug": "ghatotkach"},
  {"id": "c3_21", "name": "शिशुपाल", "desc": "चेदि राज, श्रीकृष्ण के हाथों सुदर्शन चक्र से दंड पाने वाला।", "correctSwipe": "RIGHT", "slug": "shishupal"},
  {"id": "c3_22", "name": "सात्यकि", "desc": "श्रीकृष्ण की नारायणी सेना के निष्ठावान यदुवंशी वीर।", "correctSwipe": "LEFT", "slug": "satyaki"},
  {"id": "c3_23", "name": "कीचक", "desc": "मत्स्य देश का कामी और अभिमानी सेनापति।", "correctSwipe": "RIGHT", "slug": "keechak"},
  {"id": "c3_24", "name": "धृष्टद्युम्न", "desc": "पाण्डव सेना का मुख्य सेनापति, द्रोण वधक।", "correctSwipe": "LEFT", "slug": "dhrishtadyumna"},
  {"id": "c3_25", "name": "कंस", "desc": "मथुरा का अत्याचारी राजा, श्रीकृष्ण के मामा।", "correctSwipe": "RIGHT", "slug": "kansa"}
]

# Source folders
dirs_map = [
  (cat1_raw, r"C:\Users\vishw\OneDrive\Videos\रामायण आरंभ"),
  (cat2_raw, r"C:\Users\vishw\OneDrive\Videos\लंका युद्ध"),
  (cat3_raw, r"C:\Users\vishw\OneDrive\Videos\महाभारत")
]

print("Starting Image Processing...")
for card_list, src_dir in dirs_map:
    files = glob.glob(os.path.join(src_dir, '*.png'))
    files.sort(key=lambda f: os.path.getctime(f))
    print(f"Directory {src_dir}: found {len(files)} files, mapping to {len(card_list)} cards")
    assert len(files) == len(card_list), f"Mismatch in count: {len(files)} vs {len(card_list)}"
    
    for i, card in enumerate(card_list):
        src_file = files[i]
        slug = card["slug"]
        cid = card["id"]
        
        # Target filenames:
        # 1. assets/cards/{slug}.jpg (as requested by user)
        # 2. assets/cards/{cid}_{slug}.jpg
        # 3. assets/cards/{slug}.png
        target_jpg = os.path.join(CARDS_DIR, f"{slug}.jpg")
        target_id_jpg = os.path.join(CARDS_DIR, f"{cid}_{slug}.jpg")
        target_png = os.path.join(CARDS_DIR, f"{slug}.png")
        
        # Load and resize for blazing-fast mobile & web performance
        # Original is 1536x2752, resize to width 720 (height ~1290)
        im = Image.open(src_file)
        w, h = im.size
        target_w = 720
        target_h = int(h * (target_w / w))
        im_resized = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        
        # Save as RGB JPEG
        im_rgb = im_resized.convert("RGB")
        im_rgb.save(target_jpg, "JPEG", quality=90, optimize=True)
        im_rgb.save(target_id_jpg, "JPEG", quality=90, optimize=True)
        # Also save web-optimized PNG
        im_resized.save(target_png, "PNG", optimize=True)
        
        # Set card image path in JSON
        card["image"] = f"assets/cards/{slug}.jpg"
        print(f"  Processed {cid} ({card['name']}) -> {card['image']}")

# Now build the full structured JSON
dataset = {
  "categories": [
    {
      "id": "cat_1_ramayana",
      "title": "अयोध्या या मिथिला",
      "instruction": "अयोध्या या मिथिला के पक्ष की ओर स्वाइप करें",
      "leftSide": {
        "label": "बाएँ (अयोध्या)",
        "name": "अयोध्या",
        "bgColor": "#6B21A8",
        "gateAsset": "assets/gates/gate_ayodhya.png"
      },
      "rightSide": {
        "label": "दाएँ (मिथिला)",
        "name": "मिथिला",
        "bgColor": "#DC2626",
        "gateAsset": "assets/gates/gate_mithila.png"
      },
      "cards": cat1_raw
    },
    {
      "id": "cat_2_lanka_war",
      "title": "राम सेना या रावण सेना",
      "instruction": "श्रीराम सेना या रावण सेना की ओर स्वाइप करें",
      "leftSide": {
        "label": "बाएँ (राम सेना)",
        "name": "राम सेना",
        "bgColor": "#EA580C",
        "gateAsset": "assets/gates/gate_ram_sena.png"
      },
      "rightSide": {
        "label": "दाएँ (रावण सेना)",
        "name": "रावण सेना",
        "bgColor": "#7F1D1D",
        "gateAsset": "assets/gates/gate_ravan_sena.png"
      },
      "cards": cat2_raw
    },
    {
      "id": "cat_3_mahabharat",
      "title": "पाण्डव या कौरव",
      "instruction": "पाण्डव पक्ष या कौरव पक्ष की ओर स्वाइप करें",
      "leftSide": {
        "label": "बाएँ (पाण्डव)",
        "name": "पाण्डव",
        "bgColor": "#15803D",
        "gateAsset": "assets/gates/gate_pandav.png"
      },
      "rightSide": {
        "label": "दाएँ (कौरव)",
        "name": "कौरव",
        "bgColor": "#991B1B",
        "gateAsset": "assets/gates/gate_kaurav.png"
      },
      "cards": cat3_raw
    }
  ]
}

# Save JSON file
json_path = os.path.join(CARDS_DIR, "swipe_game_data.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print(f"\n✓ Saved swipe_game_data.json with {len(cat1_raw) + len(cat2_raw) + len(cat3_raw)} total cards!")
