# Multilingual mapping generator for all 100 Swipe Game cards
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
DATA_FILE = os.path.join(BASE_DIR, "assets", "cards", "swipe_game_data.json")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Comprehensive dictionary for all 100 character slugs
CHARACTER_TRANSLATIONS = {
    # Category 1: Ramayana (Ayodhya vs Mithila)
    "ram": {
        "en": ("Lord Rama", "Eldest son of Dasharatha and Kaushalya, pinnacle of Raghu dynasty."),
        "te": ("శ్రీ రాముడు", "దశరథ మహారాజు, కౌసల్యల జ్యేష్ఠ పుత్రుడు, రఘువంశ తిలకుడు.")
    },
    "sita": {
        "en": ("Goddess Sita", "Daughter of King Janaka, Earth-born princess of Mithila."),
        "te": ("సీతాదేవి", "జనక మహారాజు ప్రియపుత్రిక, భూమిజ, మిథిలా రాకుమారి.")
    },
    "lakshman": {
        "en": ("Lakshmana", "Son of Sumitra, devoted brother ever ready in Rama's service."),
        "te": ("లక్ష్మణుడు", "సుమిత్ర కుమారుడు, శ్రీరామునికి అత్యంత ప్రియమైన సోదరుడు.")
    },
    "urmila": {
        "en": ("Urmila", "Daughter of King Janaka, faithful wife of Lakshmana."),
        "te": ("ఊర్మిళ", "జనక మహారాజు పుత్రిక, లక్ష్మణుని ధర్మపత్ని.")
    },
    "bharat": {
        "en": ("Bharata", "Son of Kaikeyi, supreme devotee and righteous ruler of Ayodhya."),
        "te": ("భరతుడు", "కైకేయి కుమారుడు, శ్రీరామ భక్తుడు, ధర్మపాలన చేసిన సోదరుడు.")
    },
    "mandavi": {
        "en": ("Mandavi", "Daughter of Kushadhwaja, devoted wife of Bharata."),
        "te": ("మాండవి", "కుశధ్వజుని కుమార్తె, భరతుని ప్రియ భార్య.")
    },
    "shatrughna": {
        "en": ("Shatrughna", "Younger son of Sumitra, valiant vanquisher of demon Lavanasura."),
        "te": ("శత్రుఘ్నుడు", "సుమిత్ర కనిష్ఠ పుత్రుడు, లవణాసుర సంహారకుడు.")
    },
    "shrutakirti": {
        "en": ("Shrutakirti", "Daughter of Kushadhwaja, faithful wife of Shatrughna."),
        "te": ("శ్రుతకీర్తి", "కుశధ్వజుని పుత్రిక, శత్రుఘ్నుని అర్ధాంగి.")
    },
    "dasharatha": {
        "en": ("King Dasharatha", "Chakravarti emperor of Ayodhya, father of Lord Rama."),
        "te": ("దశరథ మహారాజు", "అయోధ్యా సూర్యవంశ చక్రవర్తి, శ్రీరాముని తండ్రి.")
    },
    "janak": {
        "en": ("King Janaka", "Philosopher king of Mithila, father of Goddess Sita."),
        "te": ("జనక మహారాజు", "మిథిలాధిపతి, విదేహ రాజు, తత్వజ్ఞాని, సీతాదేవి తండ్రి.")
    },
    "kaushalya": {
        "en": ("Queen Kaushalya", "Senior Queen of Ayodhya, compassionate mother of Lord Rama."),
        "te": ("కౌసల్యా దేవి", "అయోధ్య పట్టమహిషి, శ్రీరాముని మాతృమూర్తి.")
    },
    "sunayana": {
        "en": ("Queen Sunayana", "Queen of Mithila, loving mother of Goddess Sita."),
        "te": ("సునయన దేవి", "మిథిలా రాణి, జనకుని భార్య, సీతాదేవి తల్లి.")
    },
    "kaikeyi": {
        "en": ("Queen Kaikeyi", "Warrior queen of Ayodhya, mother of Prince Bharata."),
        "te": ("కైకేయి దేవి", "అయోధ్య రాణి, శౌర్యవంతురాలు, భరతుని తల్లి.")
    },
    "kushadhwaja": {
        "en": ("King Kushadhwaja", "King of Sankashya, younger brother of King Janaka."),
        "te": ("కుశధ్వజ మహారాజు", "జనక మహారాజు సోదరుడు, సంకాశ్యాధిపతి.")
    },
    "sumitra": {
        "en": ("Queen Sumitra", "Wise queen of Ayodhya, mother of Lakshmana & Shatrughna."),
        "te": ("సుమిత్రా దేవి", "లక్ష్మణ, శత్రుఘ్నుల మాతృమూర్తి, విజ్ఞాన సంపన్నురాలు.")
    },
    "vashishtha": {
        "en": ("Sage Vashistha", "Royal Kulaguru of the Ikshvaku dynasty in Ayodhya."),
        "te": ("వసిష్ఠ మహర్షి", "అయోధ్య రఘువంశ కులగురువు, బ్రహ్మర్షి.")
    },
    "shatananda": {
        "en": ("Sage Shatananda", "Royal priest and preceptor of the court of Mithila."),
        "te": ("శతానంద మహర్షి", "మిథిలా రాజపురోహితుడు, గౌతమ మహర్షి కుమారుడు.")
    },
    "sumanta": {
        "en": ("Sumantra", "Chief Prime Minister and loyal royal charioteer of Ayodhya."),
        "te": ("సుమంత్రుడు", "అయోధ్య రాజ్య ప్రధానమంత్రి, నమ్మకమైన రథసారథి.")
    },
    "ahilya": {
        "en": ("Devi Ahalya", "Wife of Sage Gautama, redeemed from stone by Rama's feet in Mithila."),
        "te": ("అహల్యా దేవి", "గౌతమ మహర్షి పత్ని, శ్రీరాముని పాదస్పర్శతో శాపవిముక్తురాలు.")
    },
    "manthara": {
        "en": ("Manthara", "Handmaiden of Kaikeyi who plotted Rama's forest exile in Ayodhya."),
        "te": ("మంధర", "కైకేయి దాసి, అయోధ్యలో కుట్ర పన్ని రాముని వనవాసానికి కారణమైంది.")
    },
    "yajnavalkya": {
        "en": ("Sage Yajnavalkya", "Great Vedic philosopher presiding over the scholarly court of Mithila."),
        "te": ("యాజ్ఞవల్క్య మహర్షి", "మిథిలా సభలో ప్రధాన వేదాంత బ్రహ్మర్షి.")
    },
    "rishyashringa": {
        "en": ("Sage Rishyashringa", "Venerable sage who conducted the Putrakameshti Yajna in Ayodhya."),
        "te": ("ఋష్యశృంగ మహర్షి", "అయోధ్యలో పుత్రకామేష్టి యాగం జరిపించిన పవిత్ర ముని.")
    },
    "gargi": {
        "en": ("Gargi Vachaknavi", "Renowned female Vedic philosopher in the assembly of Mithila."),
        "te": ("గార్గి", "మిథిలా జనక మహారాజు సభలో ప్రసిద్ధ విదుషీమణి, బ్రహ్మజ్ఞాని.")
    },
    "shanta": {
        "en": ("Princess Shanta", "Eldest daughter of Dasharatha, sister of Lord Rama."),
        "te": ("శాంతా దేవి", "దశరథుని జ్యేష్ఠ పుత్రిక, శ్రీరాముని అగ్రసోదరి.")
    },
    "maitreyi": {
        "en": ("Maitreyi", "Philosopher sage of Mithila, seeker of immortal spiritual wisdom."),
        "te": ("మైత్రేయి", "మిథిలా వేదాంత తత్వవేత్త, మోక్ష సాధకురాలు.")
    },
    "pinaka": {
        "en": ("Pinaka Bow", "Mighty divine bow of Lord Shiva broken by Lord Rama in Mithila."),
        "te": ("పినాక ధనుస్సు", "శివధనుస్సు, మిథిలలో శ్రీరాముడు భగ్నం చేసిన దివ్య ధనుస్సు.")
    },
    "pushpavatika": {
        "en": ("Pushpa Vatika", "Sacred royal garden of Mithila where Rama and Sita first met."),
        "te": ("పుష్పవాటిక", "మిథిలా రాజ ఉద్యానవనం, శ్రీరామ సీతల ప్రథమ దర్శన ప్రదేశం.")
    },
    "sarayu_nadi": {
        "en": ("Sarayu River", "Sacred holy river flowing gracefully alongside holy Ayodhya."),
        "te": ("సరయూ నది", "అయోధ్య తీరాన ప్రవహించే పవిత్ర పుణ్యనది.")
    },
    "nandigram": {
        "en": ("Nandigram", "Sacred hermitage near Ayodhya where Bharata ruled through Rama's sandals."),
        "te": ("నందిగ్రామం", "శ్రీరాముని పాదుకలు ఉంచి భరతుడు తపస్సు చేస్తూ పాలించిన ప్రదేశం.")
    },
    "swayamvar_mandap": {
        "en": ("Swayamvar Pavilion", "Grand royal wedding pavilion in Mithila where Sita chose Rama."),
        "te": ("స్వయంవర మండపం", "మిథిలా నగరంలో సీతా స్వయంవరం జరిగిన దివ్య మండపం.")
    },
    "kanak_bhavan": {
        "en": ("Kanak Bhavan", "Golden palace presented to Sita by Kaikeyi in Ayodhya."),
        "te": ("కనక భవనం", "సీతారాముల కోసం అయోధ్యలో కైకేయి బహూకరించిన స్వర్ణ మహల్.")
    },
    "ganga_son_sangam": {
        "en": ("Ganga-Son Confluence", "Sacred holy river confluence crossed during journey to Mithila."),
        "te": ("గంగా-శోణ సంగమం", "మిథిలా ప్రయాణంలో విశ్వామిత్ర రామ లక్ష్మణులు దర్శించిన సంగమం.")
    },
    "suryavanshi_dhwaja": {
        "en": ("Suryavanshi Standard", "Glorious royal sun-emblem banner of the solar dynasty of Ayodhya."),
        "te": ("సూర్యవంశ ధ్వజం", "అయోధ్య రఘువంశానికి చెందిన ప్రసిద్ధ సూర్య పతాకం.")
    },
    "videha_rajpataka": {
        "en": ("Videha Royal Banner", "Sovereign royal flag fluttering above the ramparts of Mithila."),
        "te": ("విదేహ రాజపతాకం", "మిథిలా రాజ్య మహోన్నత రాజధ్వజం.")
    },
    "tadaka_vana": {
        "en": ("Tadaka Forest", "Forest near Ayodhya where young Rama vanquished demoness Tadaka."),
        "te": ("తాటకా వనం", "అయోధ్య మార్గంలో శ్రీరాముడు తాటకను సంహరించిన వనం.")
    },
    "jayamala": {
        "en": ("Victory Garland", "Divine wedding garland placed by Princess Sita on Rama's neck in Mithila."),
        "te": ("వరమాల", "మిథిలా స్వయంవరంలో సీతాదేవి శ్రీరాముని మెడలో వేసిన దివ్యమాల.")
    },
    "halkarshan_utsav": {
        "en": ("Sacred Plough Festival", "Auspicious ploughing ceremony in Mithila where infant Sita was found."),
        "te": ("హలకర్షణ ఉత్సవం", "మిథిలలో జనక మహారాజు భూమి దున్నుతుండగా సీతాదేవి లభించిన ఉత్సవం.")
    },
    "sumitra_prasad": {
        "en": ("Sumitra Palace", "Peaceful royal residence of Queen Sumitra in Ayodhya."),
        "te": ("సుమిత్రా ప్రాసాదం", "అయోధ్య అంతఃపురంలో సుమిత్రా దేవి నివాస భవనం.")
    },
    "ashwamedha_ashwa": {
        "en": ("Ashwamedha Steed", "Consecrated white steed released by Lord Rama from Ayodhya."),
        "te": ("అశ్వమేధ అశ్వం", "శ్రీరాముడు అయోధ్యలో అశ్వమేధ యాగం చేసిన దివ్య అశ్వం.")
    },
    "vishwamitra": {
        "en": ("Sage Vishwamitra", "Brahmarshi who brought Rama and Lakshmana to Mithila."),
        "te": ("విశ్వామిత్ర మహర్షి", "శ్రీరామ లక్ష్మణులను మిథిలా స్వయంవరానికి తీసుకువచ్చిన బ్రహ్మర్షి.")
    },

    # Category 2: Lanka War (Rama Army vs Ravana Army)
    "hanuman": {
        "en": ("Lord Hanuman", "Vayuputra, supreme devotion incarnate leading the Vanara army."),
        "te": ("హనుమంతుడు", "వాయుపుత్రుడు, అంజనీనందనుడు, శ్రీరామ భక్తాగ్రగణ్యుడు.")
    },
    "ravan": {
        "en": ("King Ravana", "Mighty ten-headed Dashanana emperor of Golden Lanka."),
        "te": ("రావణాసురుడు", "దశకంఠుడు, లంకాధిపతి, త్రైలోక్య విజేత.")
    },
    "sugriva": {
        "en": ("King Sugriva", "King of the Vanaras, valiant ally of Lord Rama."),
        "te": ("సుగ్రీవుడు", "వానర రాజు, కిష్కింధాధిపతి, శ్రీరాముని మిత్రుడు.")
    },
    "meghnad": {
        "en": ("Meghnada (Indrajit)", "Prince of Lanka, conqueror of Indra wielding celestial weapons."),
        "te": ("మేఘనాథుడు (ఇంద్రజిత్తు)", "రావణుని వీరపుత్రుడు, ఇంద్రుని జయించిన మహావీరుడు.")
    },
    "jambavant": {
        "en": ("King Jambavan", "Wise and immortal King of the Bears in Rama's army."),
        "te": ("జాంబవంతుడు", "ఋక్షరాజ, చిరంజీవి, రామసైన్యంలో అత్యంత జ్ఞానియైన వీరుడు.")
    },
    "kumbhkaran": {
        "en": ("Kumbhakarna", "Giant brother of Ravana possessing colossal, world-shaking might."),
        "te": ("కుంభకర్ణుడు", "రావణుని తమ్ముడు, మహాకాయుడు, నిద్రాప్రియుడైన రాక్షస వీరుడు.")
    },
    "angada": {
        "en": ("Prince Angada", "Son of Vali, fearless youth ambassador to Ravana's court."),
        "te": ("అంగదుడు", "వాలి కుమారుడు, లంకా సభలో రాముని వీర దూత.")
    },
    "shurpanakha": {
        "en": ("Shurpanakha", "Sister of Ravana who ignited the war between Rama and Lanka."),
        "te": ("శూర్పణఖ", "రావణుని చెల్లెలు, రామ-రావణ సంగ్రామానికి మూల కారణం.")
    },
    "vibhishan": {
        "en": ("Vibhishana", "Righteous brother of Ravana who surrendered to Rama's shelter."),
        "te": ("విభీషణుడు", "రావణుని ధర్మాత్ముడైన సోదరుడు, శ్రీరామ శరణాగతుడు.")
    },
    "maricha": {
        "en": ("Maricha", "Uncle of Ravana who took the form of the elusive Golden Deer."),
        "te": ("మారీచుడు", "రావణుని మేనమామ, మాయా బంగారు జింకగా మారిన రాక్షసుడు.")
    },
    "nala": {
        "en": ("Nala", "Divine architect Vanara who engineered the holy floating bridge."),
        "te": ("నలుడు", "వానర శిల్పి, విశ్వకర్మ పుత్రుడు, రామసేతువును నిర్మించినవాడు.")
    },
    "mandodari": {
        "en": ("Queen Mandodari", "Chaste, virtuous queen consort of King Ravana in Lanka."),
        "te": ("మండోదరి", "రావణుని పట్టమహిషి, పతివ్రతారత్నం, మయబ్రహ్మ పుత్రిక.")
    },
    "neela": {
        "en": ("Neela", "Supreme Commander-in-Chief of the Vanara armed forces."),
        "te": ("నీలుడు", "వానర సేనాధిపతి, అగ్నిదేవుని పుత్రుడు, యుద్ధవీరుడు.")
    },
    "prahasta": {
        "en": ("Prahasta", "Chief General of the Rakshasa armed forces of Lanka."),
        "te": ("ప్రహస్తుడు", "లంకా సేనాధిపతి, రావణునికి నమ్మకమైన ప్రధాన యోధుడు.")
    },
    "jatayu": {
        "en": ("Jatayu", "Noble divine vulture King who gave his life defending Sita."),
        "te": ("జటాయువు", "గద్దల రాజు, సీతా సంరక్షణలో ప్రాణాలు అర్పించిన పక్షి శ్రేష్ఠుడు.")
    },
    "khara": {
        "en": ("Khara", "Demon governor of Janasthana slain by Lord Rama."),
        "te": ("ఖరుడు", "జనస్థాన రాక్షస పాలకుడు, శ్రీరాముని చేతిలో హతమైనవాడు.")
    },
    "sampati": {
        "en": ("Sampati", "Elder brother of Jatayu who spotted Sita across the southern ocean."),
        "te": ("సంపాతి", "జటాయువు సోదరుడు, సముద్రం దాటి లంకలో సీతను దర్శించినవాడు.")
    },
    "dushana": {
        "en": ("Dushana", "Fierce demon commander serving under Khara in Dandakaranya."),
        "te": ("దూషణుడు", "ఖరుని సేనాని, దండకారణ్యంలో రాముని చేత సంహరింపబడ్డాడు.")
    },
    "shabari": {
        "en": ("Shabari", "Devoted forest ascetic who offered sweet berries to Lord Rama."),
        "te": ("శబరి", "మతంగ మహర్షి శిష్యురాలు, రామునికి ఎంగిలి పండ్లు సమర్పించిన భక్తురాలు.")
    },
    "akshayakumara": {
        "en": ("Akshayakumara", "Valiant youngest prince of Ravana slain by Hanuman in Ashok Vatika."),
        "te": ("అక్షయకుమారుడు", "రావణుని చిన్న కుమారుడు, అశోకవాటికలో హనుమంతుని చేత హతుడయ్యాడు.")
    },
    "sushena": {
        "en": ("Sushena", "Chief royal physician of the Vanara army, father of Queen Tara."),
        "te": ("సుషేణుడు", "వానర రాజ్య ప్రధాన వైద్యుడు, తార యొక్క తండ్రి.")
    },
    "atikaya": {
        "en": ("Atikaya", "Colossal Rakshasa warrior of Lanka vanquished by Lakshmana."),
        "te": ("అతికాయుడు", "రావణుని వీరపుత్రుడు, లక్ష్మణుని బాణానికి కూలిన మహాకాయుడు.")
    },
    "kesari": {
        "en": ("Kesari", "Mighty Vanara chieftain, heroic father of Lord Hanuman."),
        "te": ("కేసరి", "వానర వీరుడు, హనుమంతుని తండ్రి.")
    },
    "trishira": {
        "en": ("Trishira", "Three-headed Rakshasa warrior in Ravana's imperial army."),
        "te": ("త్రిశిరుడు", "మూడు తలల రాక్షస వీరుడు, రావణుని సేనలో ప్రసిద్ధుడు.")
    },
    "dadhimukha": {
        "en": ("Dadhimukha", "Guardian chieftain of the sacred royal Madhuvana of Sugriva."),
        "te": ("దధిముఖుడు", "సుగ్రీవుని మధువన రక్షకుడు, వానర నాయకుడు.")
    },
    "mahiravana": {
        "en": ("Mahiravana", "Sorcerer king of Patala Lanka who abducted Rama and Lakshmana."),
        "te": ("మహిరావణుడు", "పాతాళ లంకాధిపతి, మాయావి రాక్షసుడు.")
    },
    "tara": {
        "en": ("Queen Tara", "Wise and diplomatic Queen of Kishkindha, mother of Angada."),
        "te": ("తారా దేవి", "కిష్కింధ రాణి, వాలి భార్య, అంగదుని తల్లి, మహా వివేకవంతురాలు.")
    },
    "kalanemi": {
        "en": ("Kalanemi", "Cunning demon sent by Ravana to intercept Hanuman's herb quest."),
        "te": ("కాలనేమి", "సంజీవిని తేకుండా హనుమంతుడిని అడ్డుకోవడానికి వచ్చిన రాక్షసుడు.")
    },
    "ruma": {
        "en": ("Ruma", "Queen consort of King Sugriva in Kishkindha."),
        "te": ("రుమ", "సుగ్రీవుని ప్రియ భార్య, కిష్కింధ రాణి.")
    },
    "trijata": {
        "en": ("Trijata", "Kind Rakshasi in Ashok Vatika who comforted and protected Sita."),
        "te": ("త్రిజట", "అశోకవాటికలో సీతాదేవికి సాంత్వన చేకూర్చిన ధర్మాత్మురాలైన రాక్షసి.")
    },
    "sanjeevani_booti": {
        "en": ("Sanjeevani Herb", "Miraculous life-saving celestial herb retrieved by Hanuman."),
        "te": ("సంజీవిని మూలిక", "లక్ష్మణుని ప్రాణాలను కాపాడిన దివ్య ఔషధ పర్వతం.")
    },
    "swarna_lanka": {
        "en": ("Golden Lanka", "Magnificent island fortress of King Ravana crafted from gold."),
        "te": ("స్వర్ణ లంక", "రావణుని రాజధాని, బంగారు లంకా నగరం.")
    },
    "ram_setu": {
        "en": ("Ram Setu Bridge", "Legendary causeway built by Vanaras across the ocean to Lanka."),
        "te": ("రామసేతువు", "వానరులు సముద్రంపై నిర్మించిన అద్భుత దివ్య వంతెన.")
    },
    "pushpak_viman": {
        "en": ("Pushpaka Vimana", "Celestial flying aerial chariot used by Ravana and Lord Rama."),
        "te": ("పుష్పక విమానం", "కుబేరుని దివ్య విమానం, రాముడు అయోధ్యకు తిరిగొచ్చిన రథం.")
    },
    "ashok_vatika": {
        "en": ("Ashok Vatika", "Pleasure garden in Lanka where Goddess Sita was held captive."),
        "te": ("అశోకవాటిక", "లంకలో సీతాదేవిని బంధించిన అశోక వృక్షాల తోట.")
    },

    # Category 3: Mahabharata (Pandavas vs Kauravas)
    "arjun": {
        "en": ("Arjuna", "Unrivaled archer of the Pandavas, wielder of the celestial Gandiva bow."),
        "te": ("అర్జునుడు", "గాండీవధారి, పాండవ మధ్యముడు, శ్రీకృష్ణుని ఆత్మమిత్రుడు.")
    },
    "duryodhan": {
        "en": ("Duryodhana", "Eldest of the hundred Kauravas, ambitious prince of Hastinapura."),
        "te": ("దుర్యోధనుడు", "కౌరవ జ్యేష్ఠుడు, హస్తినాపుర రాజకుమారుడు, గదాయుద్ధ నిపుణుడు.")
    },
    "yudhisthir": {
        "en": ("Yudhishthira (Dharmaraja)", "Eldest Pandava, embodiment of truth, righteousness, and justice."),
        "te": ("యుధిష్ఠిరుడు (ధర్మరాజు)", "పాండవాగ్రజుడు, సత్య ధర్మాల ప్రతీక, ఇంద్రప్రస్థ చక్రవర్తి.")
    },
    "dushasan": {
        "en": ("Dushasana", "Second Kaurava brother, enforcer of Duryodhana's wicked schemes."),
        "te": ("దుశ్శాసనుడు", "దుర్యోధనుని అనుజుడు, ద్రౌపదీ వస్త్రాపహరణం చేసిన పాపి.")
    },
    "bheem": {
        "en": ("Bheemasena", "Second Pandava possessing the formidable strength of ten thousand elephants."),
        "te": ("భీమసేనుడు", "వాయుపుత్రుడు, పదివేల ఏనుగుల బలం గల పాండవ వీరుడు.")
    },
    "shakuni": {
        "en": ("Shakuni", "King of Gandhara, master of dice and cunning strategist of the Kauravas."),
        "te": ("శకుని", "గాంధార రాజు, పాచికల మాయావి, కౌరవుల కుట్రల రూపకర్త.")
    },
    "karna": {
        "en": ("Karna (Radheya)", "Mighty sun-born warrior, supreme donor and steadfast champion of Duryodhana."),
        "te": ("కర్ణుడు", "సూర్యపుత్రుడు, దానవీరుడు, దుర్యోధనుని ప్రాణమిత్రుడు.")
    },
    "draupadi": {
        "en": ("Draupadi (Panchali)", "Fire-born Empress of the Pandavas, queen of Indraprastha."),
        "te": ("ద్రౌపది (పాంచాలి)", "యజ్ఞసేని, అగ్ని సంభవ, పాండవుల పట్టమహిషి.")
    },
    "dronacharya": {
        "en": ("Dronacharya", "Supreme military preceptor of both the Pandavas and Kauravas."),
        "te": ("ద్రోణాచార్యుడు", "కౌరవ పాండవుల గురువు, దివ్యాస్త్ర కోవిదుడు.")
    },
    "abhimanyu": {
        "en": ("Abhimanyu", "Valiant son of Arjuna and Subhadra who penetrated the deadly Chakravyuha."),
        "te": ("అభిమన్యుడు", "అర్జునుని కుమారుడు, చక్రవ్యూహాన్ని ఛేదించిన అజేయ బాలవీరుడు.")
    },
    "ashwatthama": {
        "en": ("Ashwatthama", "Immortal son of Drona fighting fiercely on the Kaurava side."),
        "te": ("అశ్వత్థామ", "ద్రోణుని కుమారుడు, చిరంజీవి, కౌరవ సేనాని.")
    },
    "kunti": {
        "en": ("Mother Kunti", "Devoted queen mother of the Pandavas, mother of Karna."),
        "te": ("కుంతీదేవి", "పాండవుల మాతృమూర్తి, కర్ణుని కన్నతల్లి.")
    },
    "gandhari": {
        "en": ("Queen Gandhari", "Devoted, blindfolded Queen of Hastinapura, mother of the Kauravas."),
        "te": ("గాంధారి", "ధృతరాష్ట్రుని పత్ని, కన్నులకు గంతలు కట్టుకున్న పతివ్రత, కౌరవుల తల్లి.")
    },
    "sahadev": {
        "en": ("Sahadeva", "Youngest Pandava, supreme astrologer and master of wisdom."),
        "te": ("సహదేవుడు", "పాండవులలో చిన్నవాడు, త్రికాలజ్ఞాని, జ్యోతిష్య నిపుణుడు.")
    },
    "jayadrath": {
        "en": ("Jayadratha", "King of Sindhu, brother-in-law of Duryodhana on the Kaurava side."),
        "te": ("జయద్రథుడు", "సింధు రాజు, దుర్యోధనుని బావ, కౌరవ పక్ష యోధుడు.")
    },
    "nakul": {
        "en": ("Nakula", "Fourth Pandava, incomparable in physical beauty and equestrian skills."),
        "te": ("నకులుడు", "మాద్రి పుత్రుడు, పాండవులలో అత్యంత రూపవంతుడు, అశ్వవిద్యానిపుణుడు.")
    },
    "kripacharya": {
        "en": ("Kripacharya", "Immortal family priest and guru serving Hastinapura."),
        "te": ("కృపాచార్యుడు", "హస్తినాపుర కులగురువు, చిరంజీవి, కౌరవ పక్ష మహారథి.")
    },
    "vidur": {
        "en": ("Mahatma Vidura", "Prime Minister of Hastinapura, incarnation of Dharma."),
        "te": ("విదురుడు", "హస్తినాపుర ప్రధాన మంత్రి, ధర్మ స్వరూపుడు, నీతి శాస్త్రవేత్త.")
    },
    "jarasandh": {
        "en": ("King Jarasandha", "Mighty emperor of Magadha allied with the enemies of Krishna."),
        "te": ("జరాసంధుడు", "మగధ రాజు, అజేయ బలశాలి, భీమునితో ద్వంద్వయుద్ధం చేసినవాడు.")
    },
    "ghatotkach": {
        "en": ("Ghatotkacha", "Giant Rakshasa son of Bheema who fought heroically for the Pandavas."),
        "te": ("ఘటోత్కచుడు", "భీమ-హిడింబల కుమారుడు, కురుక్షేత్రంలో పాండవుల వైపు పోరాడిన రాక్షస వీరుడు.")
    },
    "shishupal": {
        "en": ("Shishupala", "King of Chedi slain by Krishna at the Rajasuya Yajna."),
        "te": ("శిశుపాలుడు", "చేది రాజు, రాజసూయ యాగంలో శ్రీకృష్ణుని సుదర్శన చక్రానికి హతుడైనవాడు.")
    },
    "satyaki": {
        "en": ("Satyaki", "Valiant Vrishni chieftain and disciple of Arjuna fighting for Pandavas."),
        "te": ("సాత్యకి", "శ్రీకృష్ణుని యాదవ సేనాని, అర్జునుని ప్రియ శిష్యుడు, పాండవ పక్ష యోధుడు.")
    },
    "keechak": {
        "en": ("Keechaka", "Arrogant general of Matsya kingdom slain by Bheema during exile."),
        "te": ("కీచకుడు", "మత్స్య దేశ సేనాని, అజ్ఞాతవాసంలో భీముని చేతిలో హతమైనవాడు.")
    },
    "dhrishtadyumna": {
        "en": ("Dhrishtadyumna", "Fire-born Commander-in-Chief of the Pandava army, brother of Draupadi."),
        "te": ("ధృష్టద్యుమ్నుడు", "పాండవ సేనాధిపతి, ద్రౌపది సోదరుడు, ద్రోణుని సంహరించినవాడు.")
    },
    "kansa": {
        "en": ("King Kamsa", "Tyrant ruler of Mathura and uncle of Lord Krishna."),
        "te": ("కంసుడు", "మధురా పాలకుడు, శ్రీకృష్ణుని మేనమామ, క్రూర రాక్షస రాక్షస గుణ చక్రవర్తి.")
    }
}

# Attach translations to each card
for cat in data['categories']:
    for card in cat['cards']:
        slug = card.get('slug', '').lower()
        if slug in CHARACTER_TRANSLATIONS:
            en_name, en_desc = CHARACTER_TRANSLATIONS[slug]["en"]
            te_name, te_desc = CHARACTER_TRANSLATIONS[slug]["te"]
            card['name_en'] = en_name
            card['desc_en'] = en_desc
            card['name_te'] = te_name
            card['desc_te'] = te_desc
            card['name_hi'] = card.get('name', '')
            card['desc_hi'] = card.get('desc', '')
        else:
            card['name_en'] = card.get('name', '')
            card['desc_en'] = card.get('desc', '')
            card['name_te'] = card.get('name', '')
            card['desc_te'] = card.get('desc', '')
            card['name_hi'] = card.get('name', '')
            card['desc_hi'] = card.get('desc', '')

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully injected translations for all {sum(len(c['cards']) for c in data['categories'])} cards!")
