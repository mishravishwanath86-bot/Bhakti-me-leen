/**
 * ══════════════════════════════════════════════════════════════════════════════
 * 🎮 EPIC GAMES ENGINE (भक्ति महाकाव्य खेल)
 * Faithfully recreating the WhatsApp Video "Swipe" Game & 3 Related Epic Games
 * ══════════════════════════════════════════════════════════════════════════════
 */

(function () {
  'use strict';

  // ── Web Audio Synthesizer (Vedic Chimes, Whooshes & Fanfares) ──
  var audioCtx = null;
  function getAudioCtx() {
    if (!audioCtx) {
      var AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) audioCtx = new AudioContext();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    return audioCtx;
  }

  function playSound(type) {
    try {
      var ctx = getAudioCtx();
      if (!ctx) return;
      var now = ctx.currentTime;

      if (type === 'swipe') {
        var osc = ctx.createOscillator();
        var gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.exponentialRampToValueAtTime(440, now + 0.12);
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.linearRampToValueAtTime(0.01, now + 0.12);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.12);
      } else if (type === 'correct') {
        // Double bell chime (E5 -> G#5)
        [659.25, 830.61].forEach(function (freq, i) {
          var osc = ctx.createOscillator();
          var gain = ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + i * 0.08);
          gain.gain.setValueAtTime(0.2, now + i * 0.08);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.4);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + i * 0.08);
          osc.stop(now + i * 0.08 + 0.4);
        });
      } else if (type === 'wrong') {
        // Low woodblock thud
        var osc = ctx.createOscillator();
        var gain = ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(140, now);
        osc.frequency.exponentialRampToValueAtTime(80, now + 0.18);
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.linearRampToValueAtTime(0.01, now + 0.18);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.18);
      } else if (type === 'victory') {
        // Royal Fanfare: C5 - E5 - G5 - C6
        [523.25, 659.25, 783.99, 1046.50].forEach(function (freq, i) {
          var osc = ctx.createOscillator();
          var gain = ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + i * 0.1);
          gain.gain.setValueAtTime(0.25, now + i * 0.1);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.1 + 0.6);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + i * 0.1);
          osc.stop(now + i * 0.1 + 0.6);
        });
      }
    } catch (e) {
      console.warn("Audio error:", e);
    }
  }

  // ── Global Coins & Progress State ──
  var epicGameState = {
    coins: 1000,
    currentCategory: 'ayodhya_mithila',
    ayodhyaScore: 0,
    mithilaScore: 0,
    currentIndex: 0,
    correctCount: 0,
    swipedHistory: [],
    deck: []
  };
  window.epicGameState = epicGameState;

  function loadCoins() {
    try {
      var saved = localStorage.getItem('epic_game_coins');
      if (saved) epicGameState.coins = parseInt(saved, 10);
    } catch (e) {}
    updateCoinsDisplay();
  }

  function addCoins(amount) {
    epicGameState.coins += amount;
    try {
      localStorage.setItem('epic_game_coins', epicGameState.coins);
    } catch (e) {}
    updateCoinsDisplay();
  }

  function updateCoinsDisplay() {
    var els = document.querySelectorAll('.epic-coins-val');
    els.forEach(function (el) {
      el.textContent = epicGameState.coins >= 1000 ? Math.floor(epicGameState.coins / 1000) + 'K' : epicGameState.coins;
    });
  }

  // ══════════════════════════════════════════════════════════════════════════════
  // 1. SWIPE GAME: DATASETS
  var SWIPE_CATEGORIES = {
  "cat_1_ramayana": {
    "id": "cat_1_ramayana",
    "title": "अयोध्या या मिथिला",
    "instruction": "अयोध्या या मिथिला के पक्ष की ओर स्वाइप करें",
    "leftSide": {
      "label": "बाएँ (अयोध्या)",
      "name": "अयोध्या",
      "bgColor": "#6B21A8",
      "gateAsset": "assets/gates/gate_ayodhya.png",
      "name_en": "Ayodhya",
      "name_hi": "अयोध्या",
      "name_te": "అయోధ్య"
    },
    "rightSide": {
      "label": "दाएँ (मिथिला)",
      "name": "मिथिला",
      "bgColor": "#DC2626",
      "gateAsset": "assets/gates/gate_mithila.png",
      "name_en": "Mithila",
      "name_hi": "मिथिला",
      "name_te": "మిథిల"
    },
    "cards": [
      {
        "id": "c1_01",
        "name": "राम",
        "desc": "दशरथ और कौशल्या के ज्येष्ठ पुत्र, रघुकुल शिरोमणि।",
        "correctSwipe": "LEFT",
        "slug": "ram",
        "image": "assets/cards/ram.jpg",
        "name_en": "Lord Rama",
        "desc_en": "Eldest son of Dasharatha and Kaushalya, pinnacle of Raghu dynasty.",
        "name_te": "శ్రీ రాముడు",
        "desc_te": "దశరథ మహారాజు, కౌసల్యల జ్యేష్ఠ పుత్రుడు, రఘువంశ తిలకుడు.",
        "name_hi": "राम",
        "desc_hi": "दशरथ और कौशल्या के ज्येष्ठ पुत्र, रघुकुल शिरोमणि।"
      },
      {
        "id": "c1_02",
        "name": "सीता",
        "desc": "राजा जनक की कन्या, भूमिपुत्री वैदेही।",
        "correctSwipe": "RIGHT",
        "slug": "sita",
        "image": "assets/cards/sita.jpg",
        "name_en": "Goddess Sita",
        "desc_en": "Daughter of King Janaka, Earth-born princess of Mithila.",
        "name_te": "సీతాదేవి",
        "desc_te": "జనక మహారాజు ప్రియపుత్రిక, భూమిజ, మిథిలా రాకుమారి.",
        "name_hi": "सीता",
        "desc_hi": "राजा जनक की कन्या, भूमिपुत्री वैदेही।"
      },
      {
        "id": "c1_03",
        "name": "लक्ष्मण",
        "desc": "सुमित्रा के पुत्र, सदैव राम की सेवा में तत्पर।",
        "correctSwipe": "LEFT",
        "slug": "lakshman",
        "image": "assets/cards/lakshman.jpg",
        "name_en": "Lakshmana",
        "desc_en": "Son of Sumitra, devoted brother ever ready in Rama's service.",
        "name_te": "లక్ష్మణుడు",
        "desc_te": "సుమిత్ర కుమారుడు, శ్రీరామునికి అత్యంత ప్రియమైన సోదరుడు.",
        "name_hi": "लक्ष्मण",
        "desc_hi": "सुमित्रा के पुत्र, सदैव राम की सेवा में तत्पर।"
      },
      {
        "id": "c1_04",
        "name": "उर्मिला",
        "desc": "राजा जनक की कन्या, लक्ष्मण की पत्नी।",
        "correctSwipe": "RIGHT",
        "slug": "urmila",
        "image": "assets/cards/urmila.jpg",
        "name_en": "Urmila",
        "desc_en": "Daughter of King Janaka, faithful wife of Lakshmana.",
        "name_te": "ఊర్మిళ",
        "desc_te": "జనక మహారాజు పుత్రిక, లక్ష్మణుని ధర్మపత్ని.",
        "name_hi": "उर्मिला",
        "desc_hi": "राजा जनक की कन्या, लक्ष्मण की पत्नी।"
      },
      {
        "id": "c1_05",
        "name": "भरत",
        "desc": "कैकेयी के पुत्र, राम के परम भक्त।",
        "correctSwipe": "LEFT",
        "slug": "bharat",
        "image": "assets/cards/bharat.jpg",
        "name_en": "Bharata",
        "desc_en": "Son of Kaikeyi, supreme devotee and righteous ruler of Ayodhya.",
        "name_te": "భరతుడు",
        "desc_te": "కైకేయి కుమారుడు, శ్రీరామ భక్తుడు, ధర్మపాలన చేసిన సోదరుడు.",
        "name_hi": "भरत",
        "desc_hi": "कैकेयी के पुत्र, राम के परम भक्त।"
      },
      {
        "id": "c1_06",
        "name": "मांडवी",
        "desc": "कुशध्वज की पुत्री, भरत की पत्नी।",
        "correctSwipe": "RIGHT",
        "slug": "mandavi",
        "image": "assets/cards/mandavi.jpg",
        "name_en": "Mandavi",
        "desc_en": "Daughter of Kushadhwaja, devoted wife of Bharata.",
        "name_te": "మాండవి",
        "desc_te": "కుశధ్వజుని కుమార్తె, భరతుని ప్రియ భార్య.",
        "name_hi": "मांडवी",
        "desc_hi": "कुशध्वज की पुत्री, भरत की पत्नी।"
      },
      {
        "id": "c1_07",
        "name": "शत्रुघ्न",
        "desc": "सुमित्रा के कनिष्ठ पुत्र, लवणासुर वधक।",
        "correctSwipe": "LEFT",
        "slug": "shatrughna",
        "image": "assets/cards/shatrughna.jpg",
        "name_en": "Shatrughna",
        "desc_en": "Younger son of Sumitra, valiant vanquisher of demon Lavanasura.",
        "name_te": "శత్రుఘ్నుడు",
        "desc_te": "సుమిత్ర కనిష్ఠ పుత్రుడు, లవణాసుర సంహారకుడు.",
        "name_hi": "शत्रुघ्न",
        "desc_hi": "सुमित्रा के कनिष्ठ पुत्र, लवणासुर वधक।"
      },
      {
        "id": "c1_08",
        "name": "श्रुतकीर्ति",
        "desc": "कुशध्वज की कन्या, शत्रुघ्न की पत्नी।",
        "correctSwipe": "RIGHT",
        "slug": "shrutakirti",
        "image": "assets/cards/shrutakirti.jpg",
        "name_en": "Shrutakirti",
        "desc_en": "Daughter of Kushadhwaja, faithful wife of Shatrughna.",
        "name_te": "శ్రుతకీర్తి",
        "desc_te": "కుశధ్వజుని పుత్రిక, శత్రుఘ్నుని అర్ధాంగి.",
        "name_hi": "श्रुतकीर्ति",
        "desc_hi": "कुशध्वज की कन्या, शत्रुघ्न की पत्नी।"
      },
      {
        "id": "c1_09",
        "name": "दशरथ",
        "desc": "अयोध्या के सूर्यवंशी चक्रवर्ती सम्राट।",
        "correctSwipe": "LEFT",
        "slug": "dasharatha",
        "image": "assets/cards/dasharatha.jpg",
        "name_en": "King Dasharatha",
        "desc_en": "Chakravarti emperor of Ayodhya, father of Lord Rama.",
        "name_te": "దశరథ మహారాజు",
        "desc_te": "అయోధ్యా సూర్యవంశ చక్రవర్తి, శ్రీరాముని తండ్రి.",
        "name_hi": "दशरथ",
        "desc_hi": "अयोध्या के सूर्यवंशी चक्रवर्ती सम्राट।"
      },
      {
        "id": "c1_10",
        "name": "जनक",
        "desc": "विदेह राज, सीता के दार्शनिक पिता।",
        "correctSwipe": "RIGHT",
        "slug": "janak",
        "image": "assets/cards/janak.jpg",
        "name_en": "King Janaka",
        "desc_en": "Philosopher king of Mithila, father of Goddess Sita.",
        "name_te": "జనక మహారాజు",
        "desc_te": "మిథిలాధిపతి, విదేహ రాజు, తత్వజ్ఞాని, సీతాదేవి తండ్రి.",
        "name_hi": "जनक",
        "desc_hi": "विदेह राज, सीता के दार्शनिक पिता।"
      },
      {
        "id": "c1_11",
        "name": "कौशल्या",
        "desc": "दशरथ की पटरानी, श्रीराम की माता।",
        "correctSwipe": "LEFT",
        "slug": "kaushalya",
        "image": "assets/cards/kaushalya.jpg",
        "name_en": "Queen Kaushalya",
        "desc_en": "Senior Queen of Ayodhya, compassionate mother of Lord Rama.",
        "name_te": "కౌసల్యా దేవి",
        "desc_te": "అయోధ్య పట్టమహిషి, శ్రీరాముని మాతృమూర్తి.",
        "name_hi": "कौशल्या",
        "desc_hi": "दशरथ की पटरानी, श्रीराम की माता।"
      },
      {
        "id": "c1_12",
        "name": "सुनयना",
        "desc": "जनक की पटरानी, सीता की वात्सल्यमयी माता।",
        "correctSwipe": "RIGHT",
        "slug": "sunayana",
        "image": "assets/cards/sunayana.jpg",
        "name_en": "Queen Sunayana",
        "desc_en": "Queen of Mithila, loving mother of Goddess Sita.",
        "name_te": "సునయన దేవి",
        "desc_te": "మిథిలా రాణి, జనకుని భార్య, సీతాదేవి తల్లి.",
        "name_hi": "सुनयना",
        "desc_hi": "जनक की पटरानी, सीता की वात्सल्यमयी माता।"
      },
      {
        "id": "c1_13",
        "name": "कैकेयी",
        "desc": "दशरथ की दूसरी रानी, भरत की माता।",
        "correctSwipe": "LEFT",
        "slug": "kaikeyi",
        "image": "assets/cards/kaikeyi.jpg",
        "name_en": "Queen Kaikeyi",
        "desc_en": "Warrior queen of Ayodhya, mother of Prince Bharata.",
        "name_te": "కైకేయి దేవి",
        "desc_te": "అయోధ్య రాణి, శౌర్యవంతురాలు, భరతుని తల్లి.",
        "name_hi": "कैकेयी",
        "desc_hi": "दशरथ की दूसरी रानी, भरत की माता।"
      },
      {
        "id": "c1_14",
        "name": "कुशध्वज",
        "desc": "राजा जनक के अनुज, सांकाश्य के राजा।",
        "correctSwipe": "RIGHT",
        "slug": "kushadhwaja",
        "image": "assets/cards/kushadhwaja.jpg",
        "name_en": "King Kushadhwaja",
        "desc_en": "King of Sankashya, younger brother of King Janaka.",
        "name_te": "కుశధ్వజ మహారాజు",
        "desc_te": "జనక మహారాజు సోదరుడు, సంకాశ్యాధిపతి.",
        "name_hi": "कुशध्वज",
        "desc_hi": "राजा जनक के अनुज, सांकाश्य के राजा।"
      },
      {
        "id": "c1_15",
        "name": "सुमित्रा",
        "desc": "लक्ष्मण और शत्रुघ्न की बुद्धिमती माता।",
        "correctSwipe": "LEFT",
        "slug": "sumitra",
        "image": "assets/cards/sumitra.jpg",
        "name_en": "Queen Sumitra",
        "desc_en": "Wise queen of Ayodhya, mother of Lakshmana & Shatrughna.",
        "name_te": "సుమిత్రా దేవి",
        "desc_te": "లక్ష్మణ, శత్రుఘ్నుల మాతృమూర్తి, విజ్ఞాన సంపన్నురాలు.",
        "name_hi": "सुमित्रा",
        "desc_hi": "लक्ष्मण और शत्रुघ्न की बुद्धिमती माता।"
      },
      {
        "id": "c1_16",
        "name": "वशिष्ठ",
        "desc": "रघुकुल के कुलगुरु, सप्तर्षि में से एक।",
        "correctSwipe": "LEFT",
        "slug": "vashishtha",
        "image": "assets/cards/vashishtha.jpg",
        "name_en": "Sage Vashistha",
        "desc_en": "Royal Kulaguru of the Ikshvaku dynasty in Ayodhya.",
        "name_te": "వసిష్ఠ మహర్షి",
        "desc_te": "అయోధ్య రఘువంశ కులగురువు, బ్రహ్మర్షి.",
        "name_hi": "वशिष्ठ",
        "desc_hi": "रघुकुल के कुलगुरु, सप्तर्षि में से एक।"
      },
      {
        "id": "c1_17",
        "name": "शतानंद",
        "desc": "महर्षि गौतम और अहल्या के पुत्र, जनक के कुलगुरु।",
        "correctSwipe": "RIGHT",
        "slug": "shatananda",
        "image": "assets/cards/shatananda.jpg",
        "name_en": "Sage Shatananda",
        "desc_en": "Royal priest and preceptor of the court of Mithila.",
        "name_te": "శతానంద మహర్షి",
        "desc_te": "మిథిలా రాజపురోహితుడు, గౌతమ మహర్షి కుమారుడు.",
        "name_hi": "शतानंद",
        "desc_hi": "महर्षि गौतम और अहल्या के पुत्र, जनक के कुलगुरु।"
      },
      {
        "id": "c1_18",
        "name": "सुमंत",
        "desc": "राजा दशरथ के अत्यंत निष्ठावान महामात्य व सारथी।",
        "correctSwipe": "LEFT",
        "slug": "sumanta",
        "image": "assets/cards/sumanta.jpg",
        "name_en": "Sumantra",
        "desc_en": "Chief Prime Minister and loyal royal charioteer of Ayodhya.",
        "name_te": "సుమంత్రుడు",
        "desc_te": "అయోధ్య రాజ్య ప్రధానమంత్రి, నమ్మకమైన రథసారథి.",
        "name_hi": "सुमंत",
        "desc_hi": "राजा दशरथ के अत्यंत निष्ठावान महामात्य व सारथी।"
      },
      {
        "id": "c1_19",
        "name": "अहल्या",
        "desc": "मिथिला उपवन में राम के चरण स्पर्श से मुक्त हुई ऋषि पत्नी।",
        "correctSwipe": "RIGHT",
        "slug": "ahilya",
        "image": "assets/cards/ahilya.jpg",
        "name_en": "Devi Ahalya",
        "desc_en": "Wife of Sage Gautama, redeemed from stone by Rama's feet in Mithila.",
        "name_te": "అహల్యా దేవి",
        "desc_te": "గౌతమ మహర్షి పత్ని, శ్రీరాముని పాదస్పర్శతో శాపవిముక్తురాలు.",
        "name_hi": "अहल्या",
        "desc_hi": "मिथिला उपवन में राम के चरण स्पर्श से मुक्त हुई ऋषि पत्नी।"
      },
      {
        "id": "c1_20",
        "name": "मंथरा",
        "desc": "कैकेयी की कुबड़ी दासी, जिसने कुमंत्रणा दी।",
        "correctSwipe": "LEFT",
        "slug": "manthara",
        "image": "assets/cards/manthara.jpg",
        "name_en": "Manthara",
        "desc_en": "Handmaiden of Kaikeyi who plotted Rama's forest exile in Ayodhya.",
        "name_te": "మంధర",
        "desc_te": "కైకేయి దాసి, అయోధ్యలో కుట్ర పన్ని రాముని వనవాసానికి కారణమైంది.",
        "name_hi": "मंथरा",
        "desc_hi": "कैकेयी की कुबड़ी दासी, जिसने कुमंत्रणा दी।"
      },
      {
        "id": "c1_21",
        "name": "याज्ञवल्क्य",
        "desc": "राजा जनक की सभा के महानतम दार्शनिक ऋषि।",
        "correctSwipe": "RIGHT",
        "slug": "yajnavalkya",
        "image": "assets/cards/yajnavalkya.jpg",
        "name_en": "Sage Yajnavalkya",
        "desc_en": "Great Vedic philosopher presiding over the scholarly court of Mithila.",
        "name_te": "యాజ్ఞవల్క్య మహర్షి",
        "desc_te": "మిథిలా సభలో ప్రధాన వేదాంత బ్రహ్మర్షి.",
        "name_hi": "याज्ञवल्क्य",
        "desc_hi": "राजा जनक की सभा के महानतम दार्शनिक ऋषि।"
      },
      {
        "id": "c1_22",
        "name": "ऋष्यशृंग",
        "desc": "दशरथ का पुत्रकामेष्टि यज्ञ कराने वाले मुनि।",
        "correctSwipe": "LEFT",
        "slug": "rishyashringa",
        "image": "assets/cards/rishyashringa.jpg",
        "name_en": "Sage Rishyashringa",
        "desc_en": "Venerable sage who conducted the Putrakameshti Yajna in Ayodhya.",
        "name_te": "ఋష్యశృంగ మహర్షి",
        "desc_te": "అయోధ్యలో పుత్రకామేష్టి యాగం జరిపించిన పవిత్ర ముని.",
        "name_hi": "ऋष्यशृंग",
        "desc_hi": "दशरथ का पुत्रकामेष्टि यज्ञ कराने वाले मुनि।"
      },
      {
        "id": "c1_23",
        "name": "गार्गी",
        "desc": "जनक के दरबार में शास्त्रार्थ करने वाली ब्रह्मवादिनी।",
        "correctSwipe": "RIGHT",
        "slug": "gargi",
        "image": "assets/cards/gargi.jpg",
        "name_en": "Gargi Vachaknavi",
        "desc_en": "Renowned female Vedic philosopher in the assembly of Mithila.",
        "name_te": "గార్గి",
        "desc_te": "మిథిలా జనక మహారాజు సభలో ప్రసిద్ధ విదుషీమణి, బ్రహ్మజ్ఞాని.",
        "name_hi": "गार्गी",
        "desc_hi": "जनक के दरबार में शास्त्रार्थ करने वाली ब्रह्मवादिनी।"
      },
      {
        "id": "c1_24",
        "name": "शांता",
        "desc": "राजा दशरथ व कौशल्या की ज्येष्ठ पुत्री।",
        "correctSwipe": "LEFT",
        "slug": "shanta",
        "image": "assets/cards/shanta.jpg",
        "name_en": "Princess Shanta",
        "desc_en": "Eldest daughter of Dasharatha, sister of Lord Rama.",
        "name_te": "శాంతా దేవి",
        "desc_te": "దశరథుని జ్యేష్ఠ పుత్రిక, శ్రీరాముని అగ్రసోదరి.",
        "name_hi": "शांता",
        "desc_hi": "राजा दशरथ व कौशल्या की ज्येष्ठ पुत्री।"
      },
      {
        "id": "c1_25",
        "name": "मैत्रेयी",
        "desc": "मिथिला की विदुषी, याज्ञवल्क्य की ज्ञानपिपासु पत्नी।",
        "correctSwipe": "RIGHT",
        "slug": "maitreyi",
        "image": "assets/cards/maitreyi.jpg",
        "name_en": "Maitreyi",
        "desc_en": "Philosopher sage of Mithila, seeker of immortal spiritual wisdom.",
        "name_te": "మైత్రేయి",
        "desc_te": "మిథిలా వేదాంత తత్వవేత్త, మోక్ష సాధకురాలు.",
        "name_hi": "मैत्रेयी",
        "desc_hi": "मिथिला की विदुषी, याज्ञवल्क्य की ज्ञानपिपासु पत्नी।"
      },
      {
        "id": "c1_26",
        "name": "पिनाक (शिव धनुष)",
        "desc": "राजा जनक के राजभवन में रखा गया महाधनुष।",
        "correctSwipe": "RIGHT",
        "slug": "pinaka",
        "image": "assets/cards/pinaka.jpg",
        "name_en": "Pinaka Bow",
        "desc_en": "Mighty divine bow of Lord Shiva broken by Lord Rama in Mithila.",
        "name_te": "పినాక ధనుస్సు",
        "desc_te": "శివధనుస్సు, మిథిలలో శ్రీరాముడు భగ్నం చేసిన దివ్య ధనుస్సు.",
        "name_hi": "पिनाक (शिव धनुष)",
        "desc_hi": "राजा जनक के राजभवन में रखा गया महाधनुष।"
      },
      {
        "id": "c1_27",
        "name": "पुष्पवाटिका",
        "desc": "मिथिला का वह उपवन जहाँ सीता-राम का प्रथम मिलन हुआ।",
        "correctSwipe": "RIGHT",
        "slug": "pushpavatika",
        "image": "assets/cards/pushpavatika.jpg",
        "name_en": "Pushpa Vatika",
        "desc_en": "Sacred royal garden of Mithila where Rama and Sita first met.",
        "name_te": "పుష్పవాటిక",
        "desc_te": "మిథిలా రాజ ఉద్యానవనం, శ్రీరామ సీతల ప్రథమ దర్శన ప్రదేశం.",
        "name_hi": "पुष्पवाटिका",
        "desc_hi": "मिथिला का वह उपवन जहाँ सीता-राम का प्रथम मिलन हुआ।"
      },
      {
        "id": "c1_28",
        "name": "सरयू नदी",
        "desc": "अयोध्या की पावन जीवनदायिनी नदी।",
        "correctSwipe": "LEFT",
        "slug": "sarayu_nadi",
        "image": "assets/cards/sarayu_nadi.jpg",
        "name_en": "Sarayu River",
        "desc_en": "Sacred holy river flowing gracefully alongside holy Ayodhya.",
        "name_te": "సరయూ నది",
        "desc_te": "అయోధ్య తీరాన ప్రవహించే పవిత్ర పుణ్యనది.",
        "name_hi": "सरयू नदी",
        "desc_hi": "अयोध्या की पावन जीवनदायिनी नदी।"
      },
      {
        "id": "c1_29",
        "name": "नंदीग्राम",
        "desc": "वह स्थान जहाँ भरत ने पादुका रखकर राजकाज संभाला।",
        "correctSwipe": "LEFT",
        "slug": "nandigram",
        "image": "assets/cards/nandigram.jpg",
        "name_en": "Nandigram",
        "desc_en": "Sacred hermitage near Ayodhya where Bharata ruled through Rama's sandals.",
        "name_te": "నందిగ్రామం",
        "desc_te": "శ్రీరాముని పాదుకలు ఉంచి భరతుడు తపస్సు చేస్తూ పాలించిన ప్రదేశం.",
        "name_hi": "नंदीग्राम",
        "desc_hi": "वह स्थान जहाँ भरत ने पादुका रखकर राजकाज संभाला।"
      },
      {
        "id": "c1_30",
        "name": "स्वयंवर मंडप",
        "desc": "मिथिला का विशाल राजदरबार जहाँ धनुष यज्ञ हुआ।",
        "correctSwipe": "RIGHT",
        "slug": "swayamvar_mandap",
        "image": "assets/cards/swayamvar_mandap.jpg",
        "name_en": "Swayamvar Pavilion",
        "desc_en": "Grand royal wedding pavilion in Mithila where Sita chose Rama.",
        "name_te": "స్వయంవర మండపం",
        "desc_te": "మిథిలా నగరంలో సీతా స్వయంవరం జరిగిన దివ్య మండపం.",
        "name_hi": "स्वयंवर मंडप",
        "desc_hi": "मिथिला का विशाल राजदरबार जहाँ धनुष यज्ञ हुआ।"
      },
      {
        "id": "c1_31",
        "name": "कनक भवन",
        "desc": "अयोध्या में सीता के स्वागत हेतु भेंट किया गया स्वर्ण महल।",
        "correctSwipe": "LEFT",
        "slug": "kanak_bhavan",
        "image": "assets/cards/kanak_bhavan.jpg",
        "name_en": "Kanak Bhavan",
        "desc_en": "Golden palace presented to Sita by Kaikeyi in Ayodhya.",
        "name_te": "కనక భవనం",
        "desc_te": "సీతారాముల కోసం అయోధ్యలో కైకేయి బహూకరించిన స్వర్ణ మహల్.",
        "name_hi": "कनक भवन",
        "desc_hi": "अयोध्या में सीता के स्वागत हेतु भेंट किया गया स्वर्ण महल।"
      },
      {
        "id": "c1_32",
        "name": "गंगा-सोन संगम",
        "desc": "विश्वामित्र संग यात्रा का मिथिला मार्ग पड़ाव।",
        "correctSwipe": "RIGHT",
        "slug": "ganga_son_sangam",
        "image": "assets/cards/ganga_son_sangam.jpg",
        "name_en": "Ganga-Son Confluence",
        "desc_en": "Sacred holy river confluence crossed during journey to Mithila.",
        "name_te": "గంగా-శోణ సంగమం",
        "desc_te": "మిథిలా ప్రయాణంలో విశ్వామిత్ర రామ లక్ష్మణులు దర్శించిన సంగమం.",
        "name_hi": "गंगा-सोन संगम",
        "desc_hi": "विश्वामित्र संग यात्रा का मिथिला मार्ग पड़ाव।"
      },
      {
        "id": "c1_33",
        "name": "सूर्यवंशी ध्वज",
        "desc": "अयोध्या की राजप्राचीर पर लहराने वाला ध्वज।",
        "correctSwipe": "LEFT",
        "slug": "suryavanshi_dhwaja",
        "image": "assets/cards/suryavanshi_dhwaja.jpg",
        "name_en": "Suryavanshi Standard",
        "desc_en": "Glorious royal sun-emblem banner of the solar dynasty of Ayodhya.",
        "name_te": "సూర్యవంశ ధ్వజం",
        "desc_te": "అయోధ్య రఘువంశానికి చెందిన ప్రసిద్ధ సూర్య పతాకం.",
        "name_hi": "सूर्यवंशी ध्वज",
        "desc_hi": "अयोध्या की राजप्राचीर पर लहराने वाला ध्वज।"
      },
      {
        "id": "c1_34",
        "name": "विदेह राजपताका",
        "desc": "मिथिला का पवित्र राज्य चिह्न ध्वज।",
        "correctSwipe": "RIGHT",
        "slug": "videha_rajpataka",
        "image": "assets/cards/videha_rajpataka.jpg",
        "name_en": "Videha Royal Banner",
        "desc_en": "Sovereign royal flag fluttering above the ramparts of Mithila.",
        "name_te": "విదేహ రాజపతాకం",
        "desc_te": "మిథిలా రాజ్య మహోన్నత రాజధ్వజం.",
        "name_hi": "विदेह राजपताका",
        "desc_hi": "मिथिला का पवित्र राज्य चिह्न ध्वज।"
      },
      {
        "id": "c1_35",
        "name": "ताड़का वन",
        "desc": "अयोध्या से मिथिला जाते समय मुक्त कराया गया भयावह वन।",
        "correctSwipe": "LEFT",
        "slug": "tadaka_vana",
        "image": "assets/cards/tadaka_vana.jpg",
        "name_en": "Tadaka Forest",
        "desc_en": "Forest near Ayodhya where young Rama vanquished demoness Tadaka.",
        "name_te": "తాటకా వనం",
        "desc_te": "అయోధ్య మార్గంలో శ్రీరాముడు తాటకను సంహరించిన వనం.",
        "name_hi": "ताड़का वन",
        "desc_hi": "अयोध्या से मिथिला जाते समय मुक्त कराया गया भयावह वन।"
      },
      {
        "id": "c1_36",
        "name": "जयमाला",
        "desc": "सीता द्वारा प्रभु राम के गले में डाली गई वरमाला।",
        "correctSwipe": "RIGHT",
        "slug": "jayamala",
        "image": "assets/cards/jayamala.jpg",
        "name_en": "Victory Garland",
        "desc_en": "Divine wedding garland placed by Princess Sita on Rama's neck in Mithila.",
        "name_te": "వరమాల",
        "desc_te": "మిథిలా స్వయంవరంలో సీతాదేవి శ్రీరాముని మెడలో వేసిన దివ్యమాల.",
        "name_hi": "जयमाला",
        "desc_hi": "सीता द्वारा प्रभु राम के गले में डाली गई वरमाला।"
      },
      {
        "id": "c1_37",
        "name": "हलकर्षण उत्सव",
        "desc": "जनक द्वारा धरती जोतने का मंगलकारी उत्सव।",
        "correctSwipe": "RIGHT",
        "slug": "halkarshan_utsav",
        "image": "assets/cards/halkarshan_utsav.jpg",
        "name_en": "Sacred Plough Festival",
        "desc_en": "Auspicious ploughing ceremony in Mithila where infant Sita was found.",
        "name_te": "హలకర్షణ ఉత్సవం",
        "desc_te": "మిథిలలో జనక మహారాజు భూమి దున్నుతుండగా సీతాదేవి లభించిన ఉత్సవం.",
        "name_hi": "हलकर्षण उत्सव",
        "desc_hi": "जनक द्वारा धरती जोतने का मंगलकारी उत्सव।"
      },
      {
        "id": "c1_38",
        "name": "सुमित्रा प्रासाद",
        "desc": "अयोध्या का शांत और साधनायुक्त राजमहल।",
        "correctSwipe": "LEFT",
        "slug": "sumitra_prasad",
        "image": "assets/cards/sumitra_prasad.jpg",
        "name_en": "Sumitra Palace",
        "desc_en": "Peaceful royal residence of Queen Sumitra in Ayodhya.",
        "name_te": "సుమిత్రా ప్రాసాదం",
        "desc_te": "అయోధ్య అంతఃపురంలో సుమిత్రా దేవి నివాస భవనం.",
        "name_hi": "सुमित्रा प्रासाद",
        "desc_hi": "अयोध्या का शांत और साधनायुक्त राजमहल।"
      },
      {
        "id": "c1_39",
        "name": "अश्वमेध अश्व",
        "desc": "अयोध्या के दिग्विजय का दिव्य श्वेत अश्व।",
        "correctSwipe": "LEFT",
        "slug": "ashwamedha_ashwa",
        "image": "assets/cards/ashwamedha_ashwa.jpg",
        "name_en": "Ashwamedha Steed",
        "desc_en": "Consecrated white steed released by Lord Rama from Ayodhya.",
        "name_te": "అశ్వమేధ అశ్వం",
        "desc_te": "శ్రీరాముడు అయోధ్యలో అశ్వమేధ యాగం చేసిన దివ్య అశ్వం.",
        "name_hi": "अश्वमेध अश्व",
        "desc_hi": "अयोध्या के दिग्विजय का दिव्य श्वेत अश्व।"
      },
      {
        "id": "c1_40",
        "name": "विश्वामित्र",
        "desc": "राम-लक्ष्मण को यज्ञ रक्षा और मिथिला ले जाने वाले गुरु।",
        "correctSwipe": "LEFT",
        "slug": "vishwamitra",
        "image": "assets/cards/vishwamitra.jpg",
        "name_en": "Sage Vishwamitra",
        "desc_en": "Brahmarshi who brought Rama and Lakshmana to Mithila.",
        "name_te": "విశ్వామిత్ర మహర్షి",
        "desc_te": "శ్రీరామ లక్ష్మణులను మిథిలా స్వయంవరానికి తీసుకువచ్చిన బ్రహ్మర్షి.",
        "name_hi": "विश्वामित्र",
        "desc_hi": "राम-लक्ष्मण को यज्ञ रक्षा और मिथिला ले जाने वाले गुरु।"
      }
    ],
    "thumb": "assets/games/cat_split_ayodhya.jpg",
    "title_en": "Ayodhya or Mithila",
    "title_hi": "अयोध्या या मिथिला",
    "title_te": "అయోధ్య లేదా మిథిల",
    "instruction_en": "Swipe towards Ayodhya or Mithila",
    "instruction_hi": "अयोध्या या मिथिला के पक्ष की ओर स्वाइप करें",
    "instruction_te": "అయోధ్య లేదా మిథిల వైపు స్వైప్ చేయండి",
    "vs_en": "Ayodhya VS Mithila",
    "vs_hi": "अयोध्या VS मिथिला",
    "vs_te": "అయోధ్య VS మిథిల"
  },
  "cat_2_lanka_war": {
    "id": "cat_2_lanka_war",
    "title": "राम सेना या रावण सेना",
    "instruction": "श्रीराम सेना या रावण सेना की ओर स्वाइप करें",
    "leftSide": {
      "label": "बाएँ (राम सेना)",
      "name": "राम सेना",
      "bgColor": "#EA580C",
      "gateAsset": "assets/gates/gate_ram_sena.png",
      "name_en": "Rama Army",
      "name_hi": "राम सेना",
      "name_te": "రామ సైన్యం"
    },
    "rightSide": {
      "label": "दाएँ (रावण सेना)",
      "name": "रावण सेना",
      "bgColor": "#7F1D1D",
      "gateAsset": "assets/gates/gate_ravan_sena.png",
      "name_en": "Ravana Army",
      "name_hi": "रावण सेना",
      "name_te": "రావణ సైన్యం"
    },
    "cards": [
      {
        "id": "c2_01",
        "name": "हनुमान",
        "desc": "अतुलितबलधामं, लंका दहन करने वाले पवनपुत्र।",
        "correctSwipe": "LEFT",
        "slug": "hanuman",
        "image": "assets/cards/hanuman.jpg",
        "name_en": "Lord Hanuman",
        "desc_en": "Vayuputra, supreme devotion incarnate leading the Vanara army.",
        "name_te": "హనుమంతుడు",
        "desc_te": "వాయుపుత్రుడు, అంజనీనందనుడు, శ్రీరామ భక్తాగ్రగణ్యుడు.",
        "name_hi": "हनुमान",
        "desc_hi": "अतुलितबलधामं, लंका दहन करने वाले पवनपुत्र।"
      },
      {
        "id": "c2_02",
        "name": "रावण",
        "desc": "दस सिरों और बीस भुजाओं वाला लंकाधिपति।",
        "correctSwipe": "RIGHT",
        "slug": "ravan",
        "image": "assets/cards/ravan.jpg",
        "name_en": "King Ravana",
        "desc_en": "Mighty ten-headed Dashanana emperor of Golden Lanka.",
        "name_te": "రావణాసురుడు",
        "desc_te": "దశకంఠుడు, లంకాధిపతి, త్రైలోక్య విజేత.",
        "name_hi": "रावण",
        "desc_hi": "दस सिरों और बीस भुजाओं वाला लंकाधिपति।"
      },
      {
        "id": "c2_03",
        "name": "सुग्रीव",
        "desc": "किष्किंधा के वानर राज, राम के मित्र।",
        "correctSwipe": "LEFT",
        "slug": "sugriva",
        "image": "assets/cards/sugriva.jpg",
        "name_en": "King Sugriva",
        "desc_en": "King of the Vanaras, valiant ally of Lord Rama.",
        "name_te": "సుగ్రీవుడు",
        "desc_te": "వానర రాజు, కిష్కింధాధిపతి, శ్రీరాముని మిత్రుడు.",
        "name_hi": "सुग्रीव",
        "desc_hi": "किष्किंधा के वानर राज, राम के मित्र।"
      },
      {
        "id": "c2_04",
        "name": "मेघनाद (इंद्रजीत)",
        "desc": "रावण का ज्येष्ठ पुत्र, ब्रह्मास्त्र धारक।",
        "correctSwipe": "RIGHT",
        "slug": "meghnad",
        "image": "assets/cards/meghnad.jpg",
        "name_en": "Meghnada (Indrajit)",
        "desc_en": "Prince of Lanka, conqueror of Indra wielding celestial weapons.",
        "name_te": "మేఘనాథుడు (ఇంద్రజిత్తు)",
        "desc_te": "రావణుని వీరపుత్రుడు, ఇంద్రుని జయించిన మహావీరుడు.",
        "name_hi": "मेघनाद (इंद्रजीत)",
        "desc_hi": "रावण का ज्येष्ठ पुत्र, ब्रह्मास्त्र धारक।"
      },
      {
        "id": "c2_05",
        "name": "जाम्बवंत",
        "desc": "ऋक्ष राज, ज्ञान और धैर्य के सागर।",
        "correctSwipe": "LEFT",
        "slug": "jambavant",
        "image": "assets/cards/jambavant.jpg",
        "name_en": "King Jambavan",
        "desc_en": "Wise and immortal King of the Bears in Rama's army.",
        "name_te": "జాంబవంతుడు",
        "desc_te": "ఋక్షరాజ, చిరంజీవి, రామసైన్యంలో అత్యంత జ్ఞానియైన వీరుడు.",
        "name_hi": "जाम्बवंत",
        "desc_hi": "ऋक्ष राज, ज्ञान और धैर्य के सागर।"
      },
      {
        "id": "c2_06",
        "name": "कुंभकर्ण",
        "desc": "छह माह तक सोने वाला विशालकाय राक्षस।",
        "correctSwipe": "RIGHT",
        "slug": "kumbhkaran",
        "image": "assets/cards/kumbhkaran.jpg",
        "name_en": "Kumbhakarna",
        "desc_en": "Giant brother of Ravana possessing colossal, world-shaking might.",
        "name_te": "కుంభకర్ణుడు",
        "desc_te": "రావణుని తమ్ముడు, మహాకాయుడు, నిద్రాప్రియుడైన రాక్షస వీరుడు.",
        "name_hi": "कुंभकर्ण",
        "desc_hi": "छह माह तक सोने वाला विशालकाय राक्षस।"
      },
      {
        "id": "c2_07",
        "name": "अंगद",
        "desc": "बालि-पुत्र, जिनका पाँव लंका सभा में अडिग रहा।",
        "correctSwipe": "LEFT",
        "slug": "angada",
        "image": "assets/cards/angada.jpg",
        "name_en": "Prince Angada",
        "desc_en": "Son of Vali, fearless youth ambassador to Ravana's court.",
        "name_te": "అంగదుడు",
        "desc_te": "వాలి కుమారుడు, లంకా సభలో రాముని వీర దూత.",
        "name_hi": "अंगद",
        "desc_hi": "बालि-पुत्र, जिनका पाँव लंका सभा में अडिग रहा।"
      },
      {
        "id": "c2_08",
        "name": "शूर्पणखा",
        "desc": "रावण की बहन, जिसकी नाक लक्ष्मण ने काटी थी।",
        "correctSwipe": "RIGHT",
        "slug": "shurpanakha",
        "image": "assets/cards/shurpanakha.jpg",
        "name_en": "Shurpanakha",
        "desc_en": "Sister of Ravana who ignited the war between Rama and Lanka.",
        "name_te": "శూర్పణఖ",
        "desc_te": "రావణుని చెల్లెలు, రామ-రావణ సంగ్రామానికి మూల కారణం.",
        "name_hi": "शूर्पणखा",
        "desc_hi": "रावण की बहन, जिसकी नाक लक्ष्मण ने काटी थी।"
      },
      {
        "id": "c2_09",
        "name": "विभीषण",
        "desc": "धर्म की राह चुनकर राम की शरण में आए रावण-भ्राता।",
        "correctSwipe": "LEFT",
        "slug": "vibhishan",
        "image": "assets/cards/vibhishan.jpg",
        "name_en": "Vibhishana",
        "desc_en": "Righteous brother of Ravana who surrendered to Rama's shelter.",
        "name_te": "విభీషణుడు",
        "desc_te": "రావణుని ధర్మాత్ముడైన సోదరుడు, శ్రీరామ శరణాగతుడు.",
        "name_hi": "विभीषण",
        "desc_hi": "धर्म की राह चुनकर राम की शरण में आए रावण-भ्राता।"
      },
      {
        "id": "c2_10",
        "name": "मारीच",
        "desc": "स्वर्ण मृग बनकर छल करने वाला मायावी असुर।",
        "correctSwipe": "RIGHT",
        "slug": "maricha",
        "image": "assets/cards/maricha.jpg",
        "name_en": "Maricha",
        "desc_en": "Uncle of Ravana who took the form of the elusive Golden Deer.",
        "name_te": "మారీచుడు",
        "desc_te": "రావణుని మేనమామ, మాయా బంగారు జింకగా మారిన రాక్షసుడు.",
        "name_hi": "मारीच",
        "desc_hi": "स्वर्ण मृग बनकर छल करने वाला मायावी असुर।"
      },
      {
        "id": "c2_11",
        "name": "नल",
        "desc": "समुद्र पर तैरने वाले पत्थरों से सेतु बनाने वाले शिल्पी।",
        "correctSwipe": "LEFT",
        "slug": "nala",
        "image": "assets/cards/nala.jpg",
        "name_en": "Nala",
        "desc_en": "Divine architect Vanara who engineered the holy floating bridge.",
        "name_te": "నలుడు",
        "desc_te": "వానర శిల్పి, విశ్వకర్మ పుత్రుడు, రామసేతువును నిర్మించినవాడు.",
        "name_hi": "नल",
        "desc_hi": "समुद्र पर तैरने वाले पत्थरों से सेतु बनाने वाले शिल्पी।"
      },
      {
        "id": "c2_12",
        "name": "मन्दोदरी",
        "desc": "रावण की नीतिवान और पतिव्रता पटरानी।",
        "correctSwipe": "RIGHT",
        "slug": "mandodari",
        "image": "assets/cards/mandodari.jpg",
        "name_en": "Queen Mandodari",
        "desc_en": "Chaste, virtuous queen consort of King Ravana in Lanka.",
        "name_te": "మండోదరి",
        "desc_te": "రావణుని పట్టమహిషి, పతివ్రతారత్నం, మయబ్రహ్మ పుత్రిక.",
        "name_hi": "मन्दोदरी",
        "desc_hi": "रावण की नीतिवान और पतिव्रता पटरानी।"
      },
      {
        "id": "c2_13",
        "name": "नील",
        "desc": "वानर सेना के मुख्य युद्ध सेनापति।",
        "correctSwipe": "LEFT",
        "slug": "neela",
        "image": "assets/cards/neela.jpg",
        "name_en": "Neela",
        "desc_en": "Supreme Commander-in-Chief of the Vanara armed forces.",
        "name_te": "నీలుడు",
        "desc_te": "వానర సేనాధిపతి, అగ్నిదేవుని పుత్రుడు, యుద్ధవీరుడు.",
        "name_hi": "नील",
        "desc_hi": "वानर सेना के मुख्य युद्ध सेनापति।"
      },
      {
        "id": "c2_14",
        "name": "प्रहस्त",
        "desc": "रावण का मुख्य सेनापति और मामा।",
        "correctSwipe": "RIGHT",
        "slug": "prahasta",
        "image": "assets/cards/prahasta.jpg",
        "name_en": "Prahasta",
        "desc_en": "Chief General of the Rakshasa armed forces of Lanka.",
        "name_te": "ప్రహస్తుడు",
        "desc_te": "లంకా సేనాధిపతి, రావణునికి నమ్మకమైన ప్రధాన యోధుడు.",
        "name_hi": "प्रहस्त",
        "desc_hi": "रावण का मुख्य सेनापति और मामा।"
      },
      {
        "id": "c2_15",
        "name": "जटायु",
        "desc": "सीता हरण के समय प्राणों की आहुति देने वाले गृध्र राज।",
        "correctSwipe": "LEFT",
        "slug": "jatayu",
        "image": "assets/cards/jatayu.jpg",
        "name_en": "Jatayu",
        "desc_en": "Noble divine vulture King who gave his life defending Sita.",
        "name_te": "జటాయువు",
        "desc_te": "గద్దల రాజు, సీతా సంరక్షణలో ప్రాణాలు అర్పించిన పక్షి శ్రేష్ఠుడు.",
        "name_hi": "जटायु",
        "desc_hi": "सीता हरण के समय प्राणों की आहुति देने वाले गृध्र राज।"
      },
      {
        "id": "c2_16",
        "name": "खर",
        "desc": "जनस्थान का सेनापति, चौदह सहस्र राक्षसों का नायक।",
        "correctSwipe": "RIGHT",
        "slug": "khara",
        "image": "assets/cards/khara.jpg",
        "name_en": "Khara",
        "desc_en": "Demon governor of Janasthana slain by Lord Rama.",
        "name_te": "ఖరుడు",
        "desc_te": "జనస్థాన రాక్షస పాలకుడు, శ్రీరాముని చేతిలో హతమైనవాడు.",
        "name_hi": "खर",
        "desc_hi": "जनस्थान का सेनापति, चौदह सहस्र राक्षसों का नायक।"
      },
      {
        "id": "c2_17",
        "name": "सम्पाती",
        "desc": "जटायु के ज्येष्ठ भ्राता, जिन्होंने समुद्र पार लंका देखी।",
        "correctSwipe": "LEFT",
        "slug": "sampati",
        "image": "assets/cards/sampati.jpg",
        "name_en": "Sampati",
        "desc_en": "Elder brother of Jatayu who spotted Sita across the southern ocean.",
        "name_te": "సంపాతి",
        "desc_te": "జటాయువు సోదరుడు, సముద్రం దాటి లంకలో సీతను దర్శించినవాడు.",
        "name_hi": "सम्पाती",
        "desc_hi": "जटायु के ज्येष्ठ भ्राता, जिन्होंने समुद्र पार लंका देखी।"
      },
      {
        "id": "c2_18",
        "name": "दूषण",
        "desc": "जनस्थान में खर का सह-सेनापति।",
        "correctSwipe": "RIGHT",
        "slug": "dushana",
        "image": "assets/cards/dushana.jpg",
        "name_en": "Dushana",
        "desc_en": "Fierce demon commander serving under Khara in Dandakaranya.",
        "name_te": "దూషణుడు",
        "desc_te": "ఖరుని సేనాని, దండకారణ్యంలో రాముని చేత సంహరింపబడ్డాడు.",
        "name_hi": "दूषण",
        "desc_hi": "जनस्थान में खर का सह-सेनापति।"
      },
      {
        "id": "c2_19",
        "name": "शबरी",
        "desc": "मतंग आश्रम की तपस्विनी, बेर खिलाने वाली अनन्य भक्त।",
        "correctSwipe": "LEFT",
        "slug": "shabari",
        "image": "assets/cards/shabari.jpg",
        "name_en": "Shabari",
        "desc_en": "Devoted forest ascetic who offered sweet berries to Lord Rama.",
        "name_te": "శబరి",
        "desc_te": "మతంగ మహర్షి శిష్యురాలు, రామునికి ఎంగిలి పండ్లు సమర్పించిన భక్తురాలు.",
        "name_hi": "शबरी",
        "desc_hi": "मतंग आश्रम की तपस्विनी, बेर खिलाने वाली अनन्य भक्त।"
      },
      {
        "id": "c2_20",
        "name": "अक्षयकुमार",
        "desc": "रावण का कनिष्ठ पुत्र, अशोक वाटिका में वीरगति पाने वाला।",
        "correctSwipe": "RIGHT",
        "slug": "akshayakumara",
        "image": "assets/cards/akshayakumara.jpg",
        "name_en": "Akshayakumara",
        "desc_en": "Valiant youngest prince of Ravana slain by Hanuman in Ashok Vatika.",
        "name_te": "అక్షయకుమారుడు",
        "desc_te": "రావణుని చిన్న కుమారుడు, అశోకవాటికలో హనుమంతుని చేత హతుడయ్యాడు.",
        "name_hi": "अक्षयकुमार",
        "desc_hi": "रावण का कनिष्ठ पुत्र, अशोक वाटिका में वीरगति पाने वाला।"
      },
      {
        "id": "c2_21",
        "name": "सुषेण",
        "desc": "लंका युद्ध के मुख्य वानर वैद्य, संजीवनी के ज्ञाता।",
        "correctSwipe": "LEFT",
        "slug": "sushena",
        "image": "assets/cards/sushena.jpg",
        "name_en": "Sushena",
        "desc_en": "Chief royal physician of the Vanara army, father of Queen Tara.",
        "name_te": "సుషేణుడు",
        "desc_te": "వానర రాజ్య ప్రధాన వైద్యుడు, తార యొక్క తండ్రి.",
        "name_hi": "सुषेण",
        "desc_hi": "लंका युद्ध के मुख्य वानर वैद्य, संजीवनी के ज्ञाता।"
      },
      {
        "id": "c2_22",
        "name": "अतिकाय",
        "desc": "रावण और धन्यमालिनी का पर्वतकाय पुत्र।",
        "correctSwipe": "RIGHT",
        "slug": "atikaya",
        "image": "assets/cards/atikaya.jpg",
        "name_en": "Atikaya",
        "desc_en": "Colossal Rakshasa warrior of Lanka vanquished by Lakshmana.",
        "name_te": "అతికాయుడు",
        "desc_te": "రావణుని వీరపుత్రుడు, లక్ష్మణుని బాణానికి కూలిన మహాకాయుడు.",
        "name_hi": "अतिकाय",
        "desc_hi": "रावण और धन्यमालिनी का पर्वतकाय पुत्र।"
      },
      {
        "id": "c2_23",
        "name": "केसरी",
        "desc": "हनुमान जी के पराक्रमी वानर पिता।",
        "correctSwipe": "LEFT",
        "slug": "kesari",
        "image": "assets/cards/kesari.jpg",
        "name_en": "Kesari",
        "desc_en": "Mighty Vanara chieftain, heroic father of Lord Hanuman.",
        "name_te": "కేసరి",
        "desc_te": "వానర వీరుడు, హనుమంతుని తండ్రి.",
        "name_hi": "केसरी",
        "desc_hi": "हनुमान जी के पराक्रमी वानर पिता।"
      },
      {
        "id": "c2_24",
        "name": "त्रिशिरा",
        "desc": "तीन सिरों वाला शक्तिशाली राक्षस योद्धा।",
        "correctSwipe": "RIGHT",
        "slug": "trishira",
        "image": "assets/cards/trishira.jpg",
        "name_en": "Trishira",
        "desc_en": "Three-headed Rakshasa warrior in Ravana's imperial army.",
        "name_te": "త్రిశిరుడు",
        "desc_te": "మూడు తలల రాక్షస వీరుడు, రావణుని సేనలో ప్రసిద్ధుడు.",
        "name_hi": "त्रिशिरा",
        "desc_hi": "तीन सिरों वाला शक्तिशाली राक्षस योद्धा।"
      },
      {
        "id": "c2_25",
        "name": "दधिमुख",
        "desc": "सुग्रीव के मधुवन के रक्षक वानर।",
        "correctSwipe": "LEFT",
        "slug": "dadhimukha",
        "image": "assets/cards/dadhimukha.jpg",
        "name_en": "Dadhimukha",
        "desc_en": "Guardian chieftain of the sacred royal Madhuvana of Sugriva.",
        "name_te": "దధిముఖుడు",
        "desc_te": "సుగ్రీవుని మధువన రక్షకుడు, వానర నాయకుడు.",
        "name_hi": "दधिमुख",
        "desc_hi": "सुग्रीव के मधुवन के रक्षक वानर।"
      },
      {
        "id": "c2_26",
        "name": "महिरावण",
        "desc": "पाताल लोक का स्वामी, तंत्र-मंत्र का मायावी।",
        "correctSwipe": "RIGHT",
        "slug": "mahiravana",
        "image": "assets/cards/mahiravana.jpg",
        "name_en": "Mahiravana",
        "desc_en": "Sorcerer king of Patala Lanka who abducted Rama and Lakshmana.",
        "name_te": "మహిరావణుడు",
        "desc_te": "పాతాళ లంకాధిపతి, మాయావి రాక్షసుడు.",
        "name_hi": "महिरावण",
        "desc_hi": "पाताल लोक का स्वामी, तंत्र-मंत्र का मायावी।"
      },
      {
        "id": "c2_27",
        "name": "तारा",
        "desc": "किष्किंधा की महारानी, बालि की बुद्धिमती पत्नी।",
        "correctSwipe": "LEFT",
        "slug": "tara",
        "image": "assets/cards/tara.jpg",
        "name_en": "Queen Tara",
        "desc_en": "Wise and diplomatic Queen of Kishkindha, mother of Angada.",
        "name_te": "తారా దేవి",
        "desc_te": "కిష్కింధ రాణి, వాలి భార్య, అంగదుని తల్లి, మహా వివేకవంతురాలు.",
        "name_hi": "तारा",
        "desc_hi": "किष्किंधा की महारानी, बालि की बुद्धिमती पत्नी।"
      },
      {
        "id": "c2_28",
        "name": "कालनेमि",
        "desc": "हनुमान जी का मार्ग रोकने वाला छली मायावी।",
        "correctSwipe": "RIGHT",
        "slug": "kalanemi",
        "image": "assets/cards/kalanemi.jpg",
        "name_en": "Kalanemi",
        "desc_en": "Cunning demon sent by Ravana to intercept Hanuman's herb quest.",
        "name_te": "కాలనేమి",
        "desc_te": "సంజీవిని తేకుండా హనుమంతుడిని అడ్డుకోవడానికి వచ్చిన రాక్షసుడు.",
        "name_hi": "कालनेमि",
        "desc_hi": "हनुमान जी का मार्ग रोकने वाला छली मायावी।"
      },
      {
        "id": "c2_29",
        "name": "रुमा",
        "desc": "सुग्रीव की पत्नी, किष्किंधा की राजमहिषी।",
        "correctSwipe": "LEFT",
        "slug": "ruma",
        "image": "assets/cards/ruma.jpg",
        "name_en": "Ruma",
        "desc_en": "Queen consort of King Sugriva in Kishkindha.",
        "name_te": "రుమ",
        "desc_te": "సుగ్రీవుని ప్రియ భార్య, కిష్కింధ రాణి.",
        "name_hi": "रुमा",
        "desc_hi": "सुग्रीव की पत्नी, किष्किंधा की राजमहिषी।"
      },
      {
        "id": "c2_30",
        "name": "त्रिजटा",
        "desc": "अशोक वाटिका में सीता की रक्षा व ढांढस बंधाने वाली राक्षसी।",
        "correctSwipe": "LEFT",
        "slug": "trijata",
        "image": "assets/cards/trijata.jpg",
        "name_en": "Trijata",
        "desc_en": "Kind Rakshasi in Ashok Vatika who comforted and protected Sita.",
        "name_te": "త్రిజట",
        "desc_te": "అశోకవాటికలో సీతాదేవికి సాంత్వన చేకూర్చిన ధర్మాత్మురాలైన రాక్షసి.",
        "name_hi": "त्रिजटा",
        "desc_hi": "अशोक वाटिका में सीता की रक्षा व ढांढस बंधाने वाली राक्षसी।"
      },
      {
        "id": "c2_31",
        "name": "संजीवनी बूटी",
        "desc": "लक्ष्मण के प्राण बचाने वाली द्रोणागिरि की दिव्य औषधि।",
        "correctSwipe": "LEFT",
        "slug": "sanjeevani_booti",
        "image": "assets/cards/sanjeevani_booti.jpg",
        "name_en": "Sanjeevani Herb",
        "desc_en": "Miraculous life-saving celestial herb retrieved by Hanuman.",
        "name_te": "సంజీవిని మూలిక",
        "desc_te": "లక్ష్మణుని ప్రాణాలను కాపాడిన దివ్య ఔషధ పర్వతం.",
        "name_hi": "संजीवनी बूटी",
        "desc_hi": "लक्ष्मण के प्राण बचाने वाली द्रोणागिरि की दिव्य औषधि।"
      },
      {
        "id": "c2_32",
        "name": "स्वर्ण लंका",
        "desc": "रावण की अभेद्य त्रिकूट पर्वत पर बसी सोने की नगरी।",
        "correctSwipe": "RIGHT",
        "slug": "swarna_lanka",
        "image": "assets/cards/swarna_lanka.jpg",
        "name_en": "Golden Lanka",
        "desc_en": "Magnificent island fortress of King Ravana crafted from gold.",
        "name_te": "స్వర్ణ లంక",
        "desc_te": "రావణుని రాజధాని, బంగారు లంకా నగరం.",
        "name_hi": "स्वर्ण लंका",
        "desc_hi": "रावण की अभेद्य त्रिकूट पर्वत पर बसी सोने की नगरी।"
      },
      {
        "id": "c2_33",
        "name": "राम सेतु",
        "desc": "भारत से लंका तक निर्मित पाषाण मार्ग।",
        "correctSwipe": "LEFT",
        "slug": "ram_setu",
        "image": "assets/cards/ram_setu.jpg",
        "name_en": "Ram Setu Bridge",
        "desc_en": "Legendary causeway built by Vanaras across the ocean to Lanka.",
        "name_te": "రామసేతువు",
        "desc_te": "వానరులు సముద్రంపై నిర్మించిన అద్భుత దివ్య వంతెన.",
        "name_hi": "राम सेतु",
        "desc_hi": "भारत से लंका तक निर्मित पाषाण मार्ग।"
      },
      {
        "id": "c2_34",
        "name": "पुष्पक विमान",
        "desc": "आकाश में उड़ने वाला मन की गति से चलने वाला विमान।",
        "correctSwipe": "RIGHT",
        "slug": "pushpak_viman",
        "image": "assets/cards/pushpak_viman.jpg",
        "name_en": "Pushpaka Vimana",
        "desc_en": "Celestial flying aerial chariot used by Ravana and Lord Rama.",
        "name_te": "పుష్పక విమానం",
        "desc_te": "కుబేరుని దివ్య విమానం, రాముడు అయోధ్యకు తిరిగొచ్చిన రథం.",
        "name_hi": "पुष्पक विमान",
        "desc_hi": "आकाश में उड़ने वाला मन की गति से चलने वाला विमान।"
      },
      {
        "id": "c2_35",
        "name": "अशोक वाटिका",
        "desc": "रावण का वह उद्यान जहाँ सीता जी को बंदी रखा गया।",
        "correctSwipe": "RIGHT",
        "slug": "ashok_vatika",
        "image": "assets/cards/ashok_vatika.jpg",
        "name_en": "Ashok Vatika",
        "desc_en": "Pleasure garden in Lanka where Goddess Sita was held captive.",
        "name_te": "అశోకవాటిక",
        "desc_te": "లంకలో సీతాదేవిని బంధించిన అశోక వృక్షాల తోట.",
        "name_hi": "अशोक वाटिका",
        "desc_hi": "रावण का वह उद्यान जहाँ सीता जी को बंदी रखा गया।"
      }
    ],
    "thumb": "assets/games/cat_split_lanka.jpg",
    "title_en": "Rama Army or Ravana Army",
    "title_hi": "राम सेना या रावण सेना",
    "title_te": "రామ సైన్యం లేదా రావణ సైన్యం",
    "instruction_en": "Swipe towards Rama Army or Ravana Army",
    "instruction_hi": "राम सेना या रावण सेना की ओर स्वाइप करें",
    "instruction_te": "రామ సైన్యం లేదా రావణ సైన్యం వైపు స్వైప్ చేయండి",
    "vs_en": "Vanaras VS Rakshasas",
    "vs_hi": "वानर सेना VS राक्षस सेना",
    "vs_te": "వానర సైన్యం VS రాక్షసులు"
  },
  "cat_3_mahabharat": {
    "id": "cat_3_mahabharat",
    "title": "पाण्डव या कौरव",
    "instruction": "पाण्डव पक्ष या कौरव पक्ष की ओर स्वाइप करें",
    "leftSide": {
      "label": "बाएँ (पाण्डव)",
      "name": "पाण्डव",
      "bgColor": "#15803D",
      "gateAsset": "assets/gates/gate_pandav.png",
      "name_en": "Pandavas",
      "name_hi": "पाण्डव",
      "name_te": "పాండవులు"
    },
    "rightSide": {
      "label": "दाएँ (कौरव)",
      "name": "कौरव",
      "bgColor": "#991B1B",
      "gateAsset": "assets/gates/gate_kaurav.png",
      "name_en": "Kauravas",
      "name_hi": "कौरव",
      "name_te": "కౌరవులు"
    },
    "cards": [
      {
        "id": "c3_01",
        "name": "अर्जुन",
        "desc": "गांडीवधारी, श्रीकृष्ण के प्रिय सखा पार्थ।",
        "correctSwipe": "LEFT",
        "slug": "arjun",
        "image": "assets/cards/arjun.jpg",
        "name_en": "Arjuna",
        "desc_en": "Unrivaled archer of the Pandavas, wielder of the celestial Gandiva bow.",
        "name_te": "అర్జునుడు",
        "desc_te": "గాండీవధారి, పాండవ మధ్యముడు, శ్రీకృష్ణుని ఆత్మమిత్రుడు.",
        "name_hi": "अर्जुन",
        "desc_hi": "गांडीवधारी, श्रीकृष्ण के प्रिय सखा पार्थ।"
      },
      {
        "id": "c3_02",
        "name": "दुर्योधन",
        "desc": "हस्तिनापुर का अहंकारी ज्येष्ठ कौरव युवराज।",
        "correctSwipe": "RIGHT",
        "slug": "duryodhan",
        "image": "assets/cards/duryodhan.jpg",
        "name_en": "Duryodhana",
        "desc_en": "Eldest of the hundred Kauravas, ambitious prince of Hastinapura.",
        "name_te": "దుర్యోధనుడు",
        "desc_te": "కౌరవ జ్యేష్ఠుడు, హస్తినాపుర రాజకుమారుడు, గదాయుద్ధ నిపుణుడు.",
        "name_hi": "दुर्योधन",
        "desc_hi": "हस्तिनापुर का अहंकारी ज्येष्ठ कौरव युवराज।"
      },
      {
        "id": "c3_03",
        "name": "युधिष्ठिर",
        "desc": "धर्मराज, सत्य और न्याय के अटूट प्रतीक।",
        "correctSwipe": "LEFT",
        "slug": "yudhisthir",
        "image": "assets/cards/yudhisthir.jpg",
        "name_en": "Yudhishthira (Dharmaraja)",
        "desc_en": "Eldest Pandava, embodiment of truth, righteousness, and justice.",
        "name_te": "యుధిష్ఠిరుడు (ధర్మరాజు)",
        "desc_te": "పాండవాగ్రజుడు, సత్య ధర్మాల ప్రతీక, ఇంద్రప్రస్థ చక్రవర్తి.",
        "name_hi": "युधिष्ठिर",
        "desc_hi": "धर्मराज, सत्य और न्याय के अटूट प्रतीक।"
      },
      {
        "id": "c3_04",
        "name": "दुःशासन",
        "desc": "दुर्योधन का आज्ञाकारी और क्रूर अनुज।",
        "correctSwipe": "RIGHT",
        "slug": "dushasan",
        "image": "assets/cards/dushasan.jpg",
        "name_en": "Dushasana",
        "desc_en": "Second Kaurava brother, enforcer of Duryodhana's wicked schemes.",
        "name_te": "దుశ్శాసనుడు",
        "desc_te": "దుర్యోధనుని అనుజుడు, ద్రౌపదీ వస్త్రాపహరణం చేసిన పాపి.",
        "name_hi": "दुःशासन",
        "desc_hi": "दुर्योधन का आज्ञाकारी और क्रूर अनुज।"
      },
      {
        "id": "c3_05",
        "name": "भीम",
        "desc": "दस सहस्र हाथियों के बल वाले गदाधारी पाण्डव।",
        "correctSwipe": "LEFT",
        "slug": "bheem",
        "image": "assets/cards/bheem.jpg",
        "name_en": "Bheemasena",
        "desc_en": "Second Pandava possessing the formidable strength of ten thousand elephants.",
        "name_te": "భీమసేనుడు",
        "desc_te": "వాయుపుత్రుడు, పదివేల ఏనుగుల బలం గల పాండవ వీరుడు.",
        "name_hi": "भीम",
        "desc_hi": "दस सहस्र हाथियों के बल वाले गदाधारी पाण्डव।"
      },
      {
        "id": "c3_06",
        "name": "शकुनि",
        "desc": "गांधार नरेश, चौसर के कपटी पांसों का स्वामी।",
        "correctSwipe": "RIGHT",
        "slug": "shakuni",
        "image": "assets/cards/shakuni.jpg",
        "name_en": "Shakuni",
        "desc_en": "King of Gandhara, master of dice and cunning strategist of the Kauravas.",
        "name_te": "శకుని",
        "desc_te": "గాంధార రాజు, పాచికల మాయావి, కౌరవుల కుట్రల రూపకర్త.",
        "name_hi": "शकुनि",
        "desc_hi": "गांधार नरेश, चौसर के कपटी पांसों का स्वामी।"
      },
      {
        "id": "c3_07",
        "name": "कर्ण",
        "desc": "दानवीर अंगराज, सूर्यपुत्र (कौरव सेनापति)।",
        "correctSwipe": "RIGHT",
        "slug": "karna",
        "image": "assets/cards/karna.jpg",
        "name_en": "Karna (Radheya)",
        "desc_en": "Mighty sun-born warrior, supreme donor and steadfast champion of Duryodhana.",
        "name_te": "కర్ణుడు",
        "desc_te": "సూర్యపుత్రుడు, దానవీరుడు, దుర్యోధనుని ప్రాణమిత్రుడు.",
        "name_hi": "कर्ण",
        "desc_hi": "दानवीर अंगराज, सूर्यपुत्र (कौरव सेनापति)।"
      },
      {
        "id": "c3_08",
        "name": "द्रौपदी",
        "desc": "पांचाल राजकुमारी, पाण्डवों की पटरानी यज्ञसेनी।",
        "correctSwipe": "LEFT",
        "slug": "draupadi",
        "image": "assets/cards/draupadi.jpg",
        "name_en": "Draupadi (Panchali)",
        "desc_en": "Fire-born Empress of the Pandavas, queen of Indraprastha.",
        "name_te": "ద్రౌపది (పాంచాలి)",
        "desc_te": "యజ్ఞసేని, అగ్ని సంభవ, పాండవుల పట్టమహిషి.",
        "name_hi": "द्रौपदी",
        "desc_hi": "पांचाल राजकुमारी, पाण्डवों की पटरानी यज्ञसेनी।"
      },
      {
        "id": "c3_09",
        "name": "द्रोणाचार्य",
        "desc": "कौरव-पाण्डव दोनों के गुरु, कौरव सेना के प्रधान सेनापति।",
        "correctSwipe": "RIGHT",
        "slug": "dronacharya",
        "image": "assets/cards/dronacharya.jpg",
        "name_en": "Dronacharya",
        "desc_en": "Supreme military preceptor of both the Pandavas and Kauravas.",
        "name_te": "ద్రోణాచార్యుడు",
        "desc_te": "కౌరవ పాండవుల గురువు, దివ్యాస్త్ర కోవిదుడు.",
        "name_hi": "द्रोणाचार्य",
        "desc_hi": "कौरव-पाण्डव दोनों के गुरु, कौरव सेना के प्रधान सेनापति।"
      },
      {
        "id": "c3_10",
        "name": "अभिमन्यु",
        "desc": "अर्जुन पुत्र, जिसने अकेले चक्रव्यूह को भेदा।",
        "correctSwipe": "LEFT",
        "slug": "abhimanyu",
        "image": "assets/cards/abhimanyu.jpg",
        "name_en": "Abhimanyu",
        "desc_en": "Valiant son of Arjuna and Subhadra who penetrated the deadly Chakravyuha.",
        "name_te": "అభిమన్యుడు",
        "desc_te": "అర్జునుని కుమారుడు, చక్రవ్యూహాన్ని ఛేదించిన అజేయ బాలవీరుడు.",
        "name_hi": "अभिमन्यु",
        "desc_hi": "अर्जुन पुत्र, जिसने अकेले चक्रव्यूह को भेदा।"
      },
      {
        "id": "c3_11",
        "name": "अश्वत्थामा",
        "desc": "गुरु द्रोण के अमर पुत्र, माथे पर दिव्य मणि धारक।",
        "correctSwipe": "RIGHT",
        "slug": "ashwatthama",
        "image": "assets/cards/ashwatthama.jpg",
        "name_en": "Ashwatthama",
        "desc_en": "Immortal son of Drona fighting fiercely on the Kaurava side.",
        "name_te": "అశ్వత్థామ",
        "desc_te": "ద్రోణుని కుమారుడు, చిరంజీవి, కౌరవ సేనాని.",
        "name_hi": "अश्वत्थामा",
        "desc_hi": "गुरु द्रोण के अमर पुत्र, माथे पर दिव्य मणि धारक।"
      },
      {
        "id": "c3_12",
        "name": "कुंती",
        "desc": "पाण्डवों की पूज्य राजमाता, पांडु की पटरानी।",
        "correctSwipe": "LEFT",
        "slug": "kunti",
        "image": "assets/cards/kunti.jpg",
        "name_en": "Mother Kunti",
        "desc_en": "Devoted queen mother of the Pandavas, mother of Karna.",
        "name_te": "కుంతీదేవి",
        "desc_te": "పాండవుల మాతృమూర్తి, కర్ణుని కన్నతల్లి.",
        "name_hi": "कुंती",
        "desc_hi": "पाण्डवों की पूज्य राजमाता, पांडु की पटरानी।"
      },
      {
        "id": "c3_13",
        "name": "गांधारी",
        "desc": "पतिव्रता महारानी, जिन्होंने आँखों पर पट्टी बांधी।",
        "correctSwipe": "RIGHT",
        "slug": "gandhari",
        "image": "assets/cards/gandhari.jpg",
        "name_en": "Queen Gandhari",
        "desc_en": "Devoted, blindfolded Queen of Hastinapura, mother of the Kauravas.",
        "name_te": "గాంధారి",
        "desc_te": "ధృతరాష్ట్రుని పత్ని, కన్నులకు గంతలు కట్టుకున్న పతివ్రత, కౌరవుల తల్లి.",
        "name_hi": "गांधारी",
        "desc_hi": "पतिव्रता महारानी, जिन्होंने आँखों पर पट्टी बांधी।"
      },
      {
        "id": "c3_14",
        "name": "सहदेव",
        "desc": "त्रिकालदर्शी कनिष्ठ पाण्डव, नीति और ज्योतिष के ज्ञाता।",
        "correctSwipe": "LEFT",
        "slug": "sahadev",
        "image": "assets/cards/sahadev.jpg",
        "name_en": "Sahadeva",
        "desc_en": "Youngest Pandava, supreme astrologer and master of wisdom.",
        "name_te": "సహదేవుడు",
        "desc_te": "పాండవులలో చిన్నవాడు, త్రికాలజ్ఞాని, జ్యోతిష్య నిపుణుడు.",
        "name_hi": "सहदेव",
        "desc_hi": "त्रिकालदर्शी कनिष्ठ पाण्डव, नीति और ज्योतिष के ज्ञाता।"
      },
      {
        "id": "c3_15",
        "name": "जयद्रथ",
        "desc": "सिंधु नरेश, जिसने चक्रव्यूह का द्वार पाण्डवों के लिए रोका।",
        "correctSwipe": "RIGHT",
        "slug": "jayadrath",
        "image": "assets/cards/jayadrath.jpg",
        "name_en": "Jayadratha",
        "desc_en": "King of Sindhu, brother-in-law of Duryodhana on the Kaurava side.",
        "name_te": "జయద్రథుడు",
        "desc_te": "సింధు రాజు, దుర్యోధనుని బావ, కౌరవ పక్ష యోధుడు.",
        "name_hi": "जयद्रथ",
        "desc_hi": "सिंधु नरेश, जिसने चक्रव्यूह का द्वार पाण्डवों के लिए रोका।"
      },
      {
        "id": "c3_16",
        "name": "नकुल",
        "desc": "अश्व विद्या और अनुपम सौंदर्य के स्वामी पाण्डव।",
        "correctSwipe": "LEFT",
        "slug": "nakul",
        "image": "assets/cards/nakul.jpg",
        "name_en": "Nakula",
        "desc_en": "Fourth Pandava, incomparable in physical beauty and equestrian skills.",
        "name_te": "నకులుడు",
        "desc_te": "మాద్రి పుత్రుడు, పాండవులలో అత్యంత రూపవంతుడు, అశ్వవిద్యానిపుణుడు.",
        "name_hi": "नकुल",
        "desc_hi": "अश्व विद्या और अनुपम सौंदर्य के स्वामी पाण्डव।"
      },
      {
        "id": "c3_17",
        "name": "कृपाचार्य",
        "desc": "कुरु राज्य के कुलगुरु और महारथी।",
        "correctSwipe": "RIGHT",
        "slug": "kripacharya",
        "image": "assets/cards/kripacharya.jpg",
        "name_en": "Kripacharya",
        "desc_en": "Immortal family priest and guru serving Hastinapura.",
        "name_te": "కృపాచార్యుడు",
        "desc_te": "హస్తినాపుర కులగురువు, చిరంజీవి, కౌరవ పక్ష మహారథి.",
        "name_hi": "कृपाचार्य",
        "desc_hi": "कुरु राज्य के कुलगुरु और महारथी।"
      },
      {
        "id": "c3_18",
        "name": "विदुर",
        "desc": "सत्य और नीति के ज्ञाता धर्मनिष्ठ महामति।",
        "correctSwipe": "LEFT",
        "slug": "vidur",
        "image": "assets/cards/vidur.jpg",
        "name_en": "Mahatma Vidura",
        "desc_en": "Prime Minister of Hastinapura, incarnation of Dharma.",
        "name_te": "విదురుడు",
        "desc_te": "హస్తినాపుర ప్రధాన మంత్రి, ధర్మ స్వరూపుడు, నీతి శాస్త్రవేత్త.",
        "name_hi": "विदुर",
        "desc_hi": "सत्य और नीति के ज्ञाता धर्मनिष्ठ महामति।"
      },
      {
        "id": "c3_19",
        "name": "जरासंध",
        "desc": "मगध का क्रूर सम्राट, कंस का श्वसुर।",
        "correctSwipe": "RIGHT",
        "slug": "jarasandh",
        "image": "assets/cards/jarasandh.jpg",
        "name_en": "King Jarasandha",
        "desc_en": "Mighty emperor of Magadha allied with the enemies of Krishna.",
        "name_te": "జరాసంధుడు",
        "desc_te": "మగధ రాజు, అజేయ బలశాలి, భీమునితో ద్వంద్వయుద్ధం చేసినవాడు.",
        "name_hi": "जरासंध",
        "desc_hi": "मगध का क्रूर सम्राट, कंस का श्वसुर।"
      },
      {
        "id": "c3_20",
        "name": "घटोत्कच",
        "desc": "भीम और हिडिम्बा का महाबली मायावी असुर पुत्र।",
        "correctSwipe": "LEFT",
        "slug": "ghatotkach",
        "image": "assets/cards/ghatotkach.jpg",
        "name_en": "Ghatotkacha",
        "desc_en": "Giant Rakshasa son of Bheema who fought heroically for the Pandavas.",
        "name_te": "ఘటోత్కచుడు",
        "desc_te": "భీమ-హిడింబల కుమారుడు, కురుక్షేత్రంలో పాండవుల వైపు పోరాడిన రాక్షస వీరుడు.",
        "name_hi": "घटोत्कच",
        "desc_hi": "भीम और हिडिम्बा का महाबली मायावी असुर पुत्र।"
      },
      {
        "id": "c3_21",
        "name": "शिशुपाल",
        "desc": "चेदि राज, श्रीकृष्ण के हाथों सुदर्शन चक्र से दंड पाने वाला।",
        "correctSwipe": "RIGHT",
        "slug": "shishupal",
        "image": "assets/cards/shishupal.jpg",
        "name_en": "Shishupala",
        "desc_en": "King of Chedi slain by Krishna at the Rajasuya Yajna.",
        "name_te": "శిశుపాలుడు",
        "desc_te": "చేది రాజు, రాజసూయ యాగంలో శ్రీకృష్ణుని సుదర్శన చక్రానికి హతుడైనవాడు.",
        "name_hi": "शिशुपाल",
        "desc_hi": "चेदि राज, श्रीकृष्ण के हाथों सुदर्शन चक्र से दंड पाने वाला।"
      },
      {
        "id": "c3_22",
        "name": "सात्यकि",
        "desc": "श्रीकृष्ण की नारायणी सेना के निष्ठावान यदुवंशी वीर।",
        "correctSwipe": "LEFT",
        "slug": "satyaki",
        "image": "assets/cards/satyaki.jpg",
        "name_en": "Satyaki",
        "desc_en": "Valiant Vrishni chieftain and disciple of Arjuna fighting for Pandavas.",
        "name_te": "సాత్యకి",
        "desc_te": "శ్రీకృష్ణుని యాదవ సేనాని, అర్జునుని ప్రియ శిష్యుడు, పాండవ పక్ష యోధుడు.",
        "name_hi": "सात्यकि",
        "desc_hi": "श्रीकृष्ण की नारायणी सेना के निष्ठावान यदुवंशी वीर।"
      },
      {
        "id": "c3_23",
        "name": "कीचक",
        "desc": "मत्स्य देश का कामी और अभिमानी सेनापति।",
        "correctSwipe": "RIGHT",
        "slug": "keechak",
        "image": "assets/cards/keechak.jpg",
        "name_en": "Keechaka",
        "desc_en": "Arrogant general of Matsya kingdom slain by Bheema during exile.",
        "name_te": "కీచకుడు",
        "desc_te": "మత్స్య దేశ సేనాని, అజ్ఞాతవాసంలో భీముని చేతిలో హతమైనవాడు.",
        "name_hi": "कीचक",
        "desc_hi": "मत्स्य देश का कामी और अभिमानी सेनापति।"
      },
      {
        "id": "c3_24",
        "name": "धृष्टद्युम्न",
        "desc": "पाण्डव सेना का मुख्य सेनापति, द्रोण वधक।",
        "correctSwipe": "LEFT",
        "slug": "dhrishtadyumna",
        "image": "assets/cards/dhrishtadyumna.jpg",
        "name_en": "Dhrishtadyumna",
        "desc_en": "Fire-born Commander-in-Chief of the Pandava army, brother of Draupadi.",
        "name_te": "ధృష్టద్యుమ్నుడు",
        "desc_te": "పాండవ సేనాధిపతి, ద్రౌపది సోదరుడు, ద్రోణుని సంహరించినవాడు.",
        "name_hi": "धृष्टद्युम्न",
        "desc_hi": "पाण्डव सेना का मुख्य सेनापति, द्रोण वधक।"
      },
      {
        "id": "c3_25",
        "name": "कंस",
        "desc": "मथुरा का अत्याचारी राजा, श्रीकृष्ण के मामा।",
        "correctSwipe": "RIGHT",
        "slug": "kansa",
        "image": "assets/cards/kansa.jpg",
        "name_en": "King Kamsa",
        "desc_en": "Tyrant ruler of Mathura and uncle of Lord Krishna.",
        "name_te": "కంసుడు",
        "desc_te": "మధురా పాలకుడు, శ్రీకృష్ణుని మేనమామ, క్రూర రాక్షస రాక్షస గుణ చక్రవర్తి.",
        "name_hi": "कंस",
        "desc_hi": "मथुरा का अत्याचारी राजा, श्रीकृष्ण के मामा।"
      }
    ],
    "thumb": "assets/games/cat_split_mahabharata.jpg",
    "title_en": "Pandavas or Kauravas",
    "title_hi": "पाण्डव या कौरव",
    "title_te": "పాండవులు లేదా కౌరవులు",
    "instruction_en": "Swipe towards Pandavas or Kauravas",
    "instruction_hi": "पाण्डव या कौरव पक्ष की ओर स्वाइप करें",
    "instruction_te": "పాండవులు లేదా కౌరవుల వైపు స్వైప్ చేయండి",
    "vs_en": "Pandavas VS Kauravas",
    "vs_hi": "पाण्डव VS कौरव",
    "vs_te": "పాండవులు VS కౌరవులు"
  },
  "ayodhya_mithila": {
    "id": "cat_1_ramayana",
    "title": "अयोध्या या मिथिला",
    "instruction": "अयोध्या या मिथिला के पक्ष की ओर स्वाइप करें",
    "leftSide": {
      "label": "बाएँ (अयोध्या)",
      "name": "अयोध्या",
      "bgColor": "#6B21A8",
      "gateAsset": "assets/gates/gate_ayodhya.png",
      "name_en": "Ayodhya",
      "name_hi": "अयोध्या",
      "name_te": "అయోధ్య"
    },
    "rightSide": {
      "label": "दाएँ (मिथिला)",
      "name": "मिथिला",
      "bgColor": "#DC2626",
      "gateAsset": "assets/gates/gate_mithila.png",
      "name_en": "Mithila",
      "name_hi": "मिथिला",
      "name_te": "మిథిల"
    },
    "cards": [
      {
        "id": "c1_01",
        "name": "राम",
        "desc": "दशरथ और कौशल्या के ज्येष्ठ पुत्र, रघुकुल शिरोमणि।",
        "correctSwipe": "LEFT",
        "slug": "ram",
        "image": "assets/cards/ram.jpg",
        "name_en": "Lord Rama",
        "desc_en": "Eldest son of Dasharatha and Kaushalya, pinnacle of Raghu dynasty.",
        "name_te": "శ్రీ రాముడు",
        "desc_te": "దశరథ మహారాజు, కౌసల్యల జ్యేష్ఠ పుత్రుడు, రఘువంశ తిలకుడు.",
        "name_hi": "राम",
        "desc_hi": "दशरथ और कौशल्या के ज्येष्ठ पुत्र, रघुकुल शिरोमणि।"
      },
      {
        "id": "c1_02",
        "name": "सीता",
        "desc": "राजा जनक की कन्या, भूमिपुत्री वैदेही।",
        "correctSwipe": "RIGHT",
        "slug": "sita",
        "image": "assets/cards/sita.jpg",
        "name_en": "Goddess Sita",
        "desc_en": "Daughter of King Janaka, Earth-born princess of Mithila.",
        "name_te": "సీతాదేవి",
        "desc_te": "జనక మహారాజు ప్రియపుత్రిక, భూమిజ, మిథిలా రాకుమారి.",
        "name_hi": "सीता",
        "desc_hi": "राजा जनक की कन्या, भूमिपुत्री वैदेही।"
      },
      {
        "id": "c1_03",
        "name": "लक्ष्मण",
        "desc": "सुमित्रा के पुत्र, सदैव राम की सेवा में तत्पर।",
        "correctSwipe": "LEFT",
        "slug": "lakshman",
        "image": "assets/cards/lakshman.jpg",
        "name_en": "Lakshmana",
        "desc_en": "Son of Sumitra, devoted brother ever ready in Rama's service.",
        "name_te": "లక్ష్మణుడు",
        "desc_te": "సుమిత్ర కుమారుడు, శ్రీరామునికి అత్యంత ప్రియమైన సోదరుడు.",
        "name_hi": "लक्ष्मण",
        "desc_hi": "सुमित्रा के पुत्र, सदैव राम की सेवा में तत्पर।"
      },
      {
        "id": "c1_04",
        "name": "उर्मिला",
        "desc": "राजा जनक की कन्या, लक्ष्मण की पत्नी।",
        "correctSwipe": "RIGHT",
        "slug": "urmila",
        "image": "assets/cards/urmila.jpg",
        "name_en": "Urmila",
        "desc_en": "Daughter of King Janaka, faithful wife of Lakshmana.",
        "name_te": "ఊర్మిళ",
        "desc_te": "జనక మహారాజు పుత్రిక, లక్ష్మణుని ధర్మపత్ని.",
        "name_hi": "उर्मिला",
        "desc_hi": "राजा जनक की कन्या, लक्ष्मण की पत्नी।"
      },
      {
        "id": "c1_05",
        "name": "भरत",
        "desc": "कैकेयी के पुत्र, राम के परम भक्त।",
        "correctSwipe": "LEFT",
        "slug": "bharat",
        "image": "assets/cards/bharat.jpg",
        "name_en": "Bharata",
        "desc_en": "Son of Kaikeyi, supreme devotee and righteous ruler of Ayodhya.",
        "name_te": "భరతుడు",
        "desc_te": "కైకేయి కుమారుడు, శ్రీరామ భక్తుడు, ధర్మపాలన చేసిన సోదరుడు.",
        "name_hi": "भरत",
        "desc_hi": "कैकेयी के पुत्र, राम के परम भक्त।"
      },
      {
        "id": "c1_06",
        "name": "मांडवी",
        "desc": "कुशध्वज की पुत्री, भरत की पत्नी।",
        "correctSwipe": "RIGHT",
        "slug": "mandavi",
        "image": "assets/cards/mandavi.jpg",
        "name_en": "Mandavi",
        "desc_en": "Daughter of Kushadhwaja, devoted wife of Bharata.",
        "name_te": "మాండవి",
        "desc_te": "కుశధ్వజుని కుమార్తె, భరతుని ప్రియ భార్య.",
        "name_hi": "मांडवी",
        "desc_hi": "कुशध्वज की पुत्री, भरत की पत्नी।"
      },
      {
        "id": "c1_07",
        "name": "शत्रुघ्न",
        "desc": "सुमित्रा के कनिष्ठ पुत्र, लवणासुर वधक।",
        "correctSwipe": "LEFT",
        "slug": "shatrughna",
        "image": "assets/cards/shatrughna.jpg",
        "name_en": "Shatrughna",
        "desc_en": "Younger son of Sumitra, valiant vanquisher of demon Lavanasura.",
        "name_te": "శత్రుఘ్నుడు",
        "desc_te": "సుమిత్ర కనిష్ఠ పుత్రుడు, లవణాసుర సంహారకుడు.",
        "name_hi": "शत्रुघ्न",
        "desc_hi": "सुमित्रा के कनिष्ठ पुत्र, लवणासुर वधक।"
      },
      {
        "id": "c1_08",
        "name": "श्रुतकीर्ति",
        "desc": "कुशध्वज की कन्या, शत्रुघ्न की पत्नी।",
        "correctSwipe": "RIGHT",
        "slug": "shrutakirti",
        "image": "assets/cards/shrutakirti.jpg",
        "name_en": "Shrutakirti",
        "desc_en": "Daughter of Kushadhwaja, faithful wife of Shatrughna.",
        "name_te": "శ్రుతకీర్తి",
        "desc_te": "కుశధ్వజుని పుత్రిక, శత్రుఘ్నుని అర్ధాంగి.",
        "name_hi": "श्रुतकीर्ति",
        "desc_hi": "कुशध्वज की कन्या, शत्रुघ्न की पत्नी।"
      },
      {
        "id": "c1_09",
        "name": "दशरथ",
        "desc": "अयोध्या के सूर्यवंशी चक्रवर्ती सम्राट।",
        "correctSwipe": "LEFT",
        "slug": "dasharatha",
        "image": "assets/cards/dasharatha.jpg",
        "name_en": "King Dasharatha",
        "desc_en": "Chakravarti emperor of Ayodhya, father of Lord Rama.",
        "name_te": "దశరథ మహారాజు",
        "desc_te": "అయోధ్యా సూర్యవంశ చక్రవర్తి, శ్రీరాముని తండ్రి.",
        "name_hi": "दशरथ",
        "desc_hi": "अयोध्या के सूर्यवंशी चक्रवर्ती सम्राट।"
      },
      {
        "id": "c1_10",
        "name": "जनक",
        "desc": "विदेह राज, सीता के दार्शनिक पिता।",
        "correctSwipe": "RIGHT",
        "slug": "janak",
        "image": "assets/cards/janak.jpg",
        "name_en": "King Janaka",
        "desc_en": "Philosopher king of Mithila, father of Goddess Sita.",
        "name_te": "జనక మహారాజు",
        "desc_te": "మిథిలాధిపతి, విదేహ రాజు, తత్వజ్ఞాని, సీతాదేవి తండ్రి.",
        "name_hi": "जनक",
        "desc_hi": "विदेह राज, सीता के दार्शनिक पिता।"
      },
      {
        "id": "c1_11",
        "name": "कौशल्या",
        "desc": "दशरथ की पटरानी, श्रीराम की माता।",
        "correctSwipe": "LEFT",
        "slug": "kaushalya",
        "image": "assets/cards/kaushalya.jpg",
        "name_en": "Queen Kaushalya",
        "desc_en": "Senior Queen of Ayodhya, compassionate mother of Lord Rama.",
        "name_te": "కౌసల్యా దేవి",
        "desc_te": "అయోధ్య పట్టమహిషి, శ్రీరాముని మాతృమూర్తి.",
        "name_hi": "कौशल्या",
        "desc_hi": "दशरथ की पटरानी, श्रीराम की माता।"
      },
      {
        "id": "c1_12",
        "name": "सुनयना",
        "desc": "जनक की पटरानी, सीता की वात्सल्यमयी माता।",
        "correctSwipe": "RIGHT",
        "slug": "sunayana",
        "image": "assets/cards/sunayana.jpg",
        "name_en": "Queen Sunayana",
        "desc_en": "Queen of Mithila, loving mother of Goddess Sita.",
        "name_te": "సునయన దేవి",
        "desc_te": "మిథిలా రాణి, జనకుని భార్య, సీతాదేవి తల్లి.",
        "name_hi": "सुनयना",
        "desc_hi": "जनक की पटरानी, सीता की वात्सल्यमयी माता।"
      },
      {
        "id": "c1_13",
        "name": "कैकेयी",
        "desc": "दशरथ की दूसरी रानी, भरत की माता।",
        "correctSwipe": "LEFT",
        "slug": "kaikeyi",
        "image": "assets/cards/kaikeyi.jpg",
        "name_en": "Queen Kaikeyi",
        "desc_en": "Warrior queen of Ayodhya, mother of Prince Bharata.",
        "name_te": "కైకేయి దేవి",
        "desc_te": "అయోధ్య రాణి, శౌర్యవంతురాలు, భరతుని తల్లి.",
        "name_hi": "कैकेयी",
        "desc_hi": "दशरथ की दूसरी रानी, भरत की माता।"
      },
      {
        "id": "c1_14",
        "name": "कुशध्वज",
        "desc": "राजा जनक के अनुज, सांकाश्य के राजा।",
        "correctSwipe": "RIGHT",
        "slug": "kushadhwaja",
        "image": "assets/cards/kushadhwaja.jpg",
        "name_en": "King Kushadhwaja",
        "desc_en": "King of Sankashya, younger brother of King Janaka.",
        "name_te": "కుశధ్వజ మహారాజు",
        "desc_te": "జనక మహారాజు సోదరుడు, సంకాశ్యాధిపతి.",
        "name_hi": "कुशध्वज",
        "desc_hi": "राजा जनक के अनुज, सांकाश्य के राजा।"
      },
      {
        "id": "c1_15",
        "name": "सुमित्रा",
        "desc": "लक्ष्मण और शत्रुघ्न की बुद्धिमती माता।",
        "correctSwipe": "LEFT",
        "slug": "sumitra",
        "image": "assets/cards/sumitra.jpg",
        "name_en": "Queen Sumitra",
        "desc_en": "Wise queen of Ayodhya, mother of Lakshmana & Shatrughna.",
        "name_te": "సుమిత్రా దేవి",
        "desc_te": "లక్ష్మణ, శత్రుఘ్నుల మాతృమూర్తి, విజ్ఞాన సంపన్నురాలు.",
        "name_hi": "सुमित्रा",
        "desc_hi": "लक्ष्मण और शत्रुघ्न की बुद्धिमती माता।"
      },
      {
        "id": "c1_16",
        "name": "वशिष्ठ",
        "desc": "रघुकुल के कुलगुरु, सप्तर्षि में से एक।",
        "correctSwipe": "LEFT",
        "slug": "vashishtha",
        "image": "assets/cards/vashishtha.jpg",
        "name_en": "Sage Vashistha",
        "desc_en": "Royal Kulaguru of the Ikshvaku dynasty in Ayodhya.",
        "name_te": "వసిష్ఠ మహర్షి",
        "desc_te": "అయోధ్య రఘువంశ కులగురువు, బ్రహ్మర్షి.",
        "name_hi": "वशिष्ठ",
        "desc_hi": "रघुकुल के कुलगुरु, सप्तर्षि में से एक।"
      },
      {
        "id": "c1_17",
        "name": "शतानंद",
        "desc": "महर्षि गौतम और अहल्या के पुत्र, जनक के कुलगुरु।",
        "correctSwipe": "RIGHT",
        "slug": "shatananda",
        "image": "assets/cards/shatananda.jpg",
        "name_en": "Sage Shatananda",
        "desc_en": "Royal priest and preceptor of the court of Mithila.",
        "name_te": "శతానంద మహర్షి",
        "desc_te": "మిథిలా రాజపురోహితుడు, గౌతమ మహర్షి కుమారుడు.",
        "name_hi": "शतानंद",
        "desc_hi": "महर्षि गौतम और अहल्या के पुत्र, जनक के कुलगुरु।"
      },
      {
        "id": "c1_18",
        "name": "सुमंत",
        "desc": "राजा दशरथ के अत्यंत निष्ठावान महामात्य व सारथी।",
        "correctSwipe": "LEFT",
        "slug": "sumanta",
        "image": "assets/cards/sumanta.jpg",
        "name_en": "Sumantra",
        "desc_en": "Chief Prime Minister and loyal royal charioteer of Ayodhya.",
        "name_te": "సుమంత్రుడు",
        "desc_te": "అయోధ్య రాజ్య ప్రధానమంత్రి, నమ్మకమైన రథసారథి.",
        "name_hi": "सुमंत",
        "desc_hi": "राजा दशरथ के अत्यंत निष्ठावान महामात्य व सारथी।"
      },
      {
        "id": "c1_19",
        "name": "अहल्या",
        "desc": "मिथिला उपवन में राम के चरण स्पर्श से मुक्त हुई ऋषि पत्नी।",
        "correctSwipe": "RIGHT",
        "slug": "ahilya",
        "image": "assets/cards/ahilya.jpg",
        "name_en": "Devi Ahalya",
        "desc_en": "Wife of Sage Gautama, redeemed from stone by Rama's feet in Mithila.",
        "name_te": "అహల్యా దేవి",
        "desc_te": "గౌతమ మహర్షి పత్ని, శ్రీరాముని పాదస్పర్శతో శాపవిముక్తురాలు.",
        "name_hi": "अहल्या",
        "desc_hi": "मिथिला उपवन में राम के चरण स्पर्श से मुक्त हुई ऋषि पत्नी।"
      },
      {
        "id": "c1_20",
        "name": "मंथरा",
        "desc": "कैकेयी की कुबड़ी दासी, जिसने कुमंत्रणा दी।",
        "correctSwipe": "LEFT",
        "slug": "manthara",
        "image": "assets/cards/manthara.jpg",
        "name_en": "Manthara",
        "desc_en": "Handmaiden of Kaikeyi who plotted Rama's forest exile in Ayodhya.",
        "name_te": "మంధర",
        "desc_te": "కైకేయి దాసి, అయోధ్యలో కుట్ర పన్ని రాముని వనవాసానికి కారణమైంది.",
        "name_hi": "मंथरा",
        "desc_hi": "कैकेयी की कुबड़ी दासी, जिसने कुमंत्रणा दी।"
      },
      {
        "id": "c1_21",
        "name": "याज्ञवल्क्य",
        "desc": "राजा जनक की सभा के महानतम दार्शनिक ऋषि।",
        "correctSwipe": "RIGHT",
        "slug": "yajnavalkya",
        "image": "assets/cards/yajnavalkya.jpg",
        "name_en": "Sage Yajnavalkya",
        "desc_en": "Great Vedic philosopher presiding over the scholarly court of Mithila.",
        "name_te": "యాజ్ఞవల్క్య మహర్షి",
        "desc_te": "మిథిలా సభలో ప్రధాన వేదాంత బ్రహ్మర్షి.",
        "name_hi": "याज्ञवल्क्य",
        "desc_hi": "राजा जनक की सभा के महानतम दार्शनिक ऋषि।"
      },
      {
        "id": "c1_22",
        "name": "ऋष्यशृंग",
        "desc": "दशरथ का पुत्रकामेष्टि यज्ञ कराने वाले मुनि।",
        "correctSwipe": "LEFT",
        "slug": "rishyashringa",
        "image": "assets/cards/rishyashringa.jpg",
        "name_en": "Sage Rishyashringa",
        "desc_en": "Venerable sage who conducted the Putrakameshti Yajna in Ayodhya.",
        "name_te": "ఋష్యశృంగ మహర్షి",
        "desc_te": "అయోధ్యలో పుత్రకామేష్టి యాగం జరిపించిన పవిత్ర ముని.",
        "name_hi": "ऋष्यशृंग",
        "desc_hi": "दशरथ का पुत्रकामेष्टि यज्ञ कराने वाले मुनि।"
      },
      {
        "id": "c1_23",
        "name": "गार्गी",
        "desc": "जनक के दरबार में शास्त्रार्थ करने वाली ब्रह्मवादिनी।",
        "correctSwipe": "RIGHT",
        "slug": "gargi",
        "image": "assets/cards/gargi.jpg",
        "name_en": "Gargi Vachaknavi",
        "desc_en": "Renowned female Vedic philosopher in the assembly of Mithila.",
        "name_te": "గార్గి",
        "desc_te": "మిథిలా జనక మహారాజు సభలో ప్రసిద్ధ విదుషీమణి, బ్రహ్మజ్ఞాని.",
        "name_hi": "गार्गी",
        "desc_hi": "जनक के दरबार में शास्त्रार्थ करने वाली ब्रह्मवादिनी।"
      },
      {
        "id": "c1_24",
        "name": "शांता",
        "desc": "राजा दशरथ व कौशल्या की ज्येष्ठ पुत्री।",
        "correctSwipe": "LEFT",
        "slug": "shanta",
        "image": "assets/cards/shanta.jpg",
        "name_en": "Princess Shanta",
        "desc_en": "Eldest daughter of Dasharatha, sister of Lord Rama.",
        "name_te": "శాంతా దేవి",
        "desc_te": "దశరథుని జ్యేష్ఠ పుత్రిక, శ్రీరాముని అగ్రసోదరి.",
        "name_hi": "शांता",
        "desc_hi": "राजा दशरथ व कौशल्या की ज्येष्ठ पुत्री।"
      },
      {
        "id": "c1_25",
        "name": "मैत्रेयी",
        "desc": "मिथिला की विदुषी, याज्ञवल्क्य की ज्ञानपिपासु पत्नी।",
        "correctSwipe": "RIGHT",
        "slug": "maitreyi",
        "image": "assets/cards/maitreyi.jpg",
        "name_en": "Maitreyi",
        "desc_en": "Philosopher sage of Mithila, seeker of immortal spiritual wisdom.",
        "name_te": "మైత్రేయి",
        "desc_te": "మిథిలా వేదాంత తత్వవేత్త, మోక్ష సాధకురాలు.",
        "name_hi": "मैत्रेयी",
        "desc_hi": "मिथिला की विदुषी, याज्ञवल्क्य की ज्ञानपिपासु पत्नी।"
      },
      {
        "id": "c1_26",
        "name": "पिनाक (शिव धनुष)",
        "desc": "राजा जनक के राजभवन में रखा गया महाधनुष।",
        "correctSwipe": "RIGHT",
        "slug": "pinaka",
        "image": "assets/cards/pinaka.jpg",
        "name_en": "Pinaka Bow",
        "desc_en": "Mighty divine bow of Lord Shiva broken by Lord Rama in Mithila.",
        "name_te": "పినాక ధనుస్సు",
        "desc_te": "శివధనుస్సు, మిథిలలో శ్రీరాముడు భగ్నం చేసిన దివ్య ధనుస్సు.",
        "name_hi": "पिनाक (शिव धनुष)",
        "desc_hi": "राजा जनक के राजभवन में रखा गया महाधनुष।"
      },
      {
        "id": "c1_27",
        "name": "पुष्पवाटिका",
        "desc": "मिथिला का वह उपवन जहाँ सीता-राम का प्रथम मिलन हुआ।",
        "correctSwipe": "RIGHT",
        "slug": "pushpavatika",
        "image": "assets/cards/pushpavatika.jpg",
        "name_en": "Pushpa Vatika",
        "desc_en": "Sacred royal garden of Mithila where Rama and Sita first met.",
        "name_te": "పుష్పవాటిక",
        "desc_te": "మిథిలా రాజ ఉద్యానవనం, శ్రీరామ సీతల ప్రథమ దర్శన ప్రదేశం.",
        "name_hi": "पुष्पवाटिका",
        "desc_hi": "मिथिला का वह उपवन जहाँ सीता-राम का प्रथम मिलन हुआ।"
      },
      {
        "id": "c1_28",
        "name": "सरयू नदी",
        "desc": "अयोध्या की पावन जीवनदायिनी नदी।",
        "correctSwipe": "LEFT",
        "slug": "sarayu_nadi",
        "image": "assets/cards/sarayu_nadi.jpg",
        "name_en": "Sarayu River",
        "desc_en": "Sacred holy river flowing gracefully alongside holy Ayodhya.",
        "name_te": "సరయూ నది",
        "desc_te": "అయోధ్య తీరాన ప్రవహించే పవిత్ర పుణ్యనది.",
        "name_hi": "सरयू नदी",
        "desc_hi": "अयोध्या की पावन जीवनदायिनी नदी।"
      },
      {
        "id": "c1_29",
        "name": "नंदीग्राम",
        "desc": "वह स्थान जहाँ भरत ने पादुका रखकर राजकाज संभाला।",
        "correctSwipe": "LEFT",
        "slug": "nandigram",
        "image": "assets/cards/nandigram.jpg",
        "name_en": "Nandigram",
        "desc_en": "Sacred hermitage near Ayodhya where Bharata ruled through Rama's sandals.",
        "name_te": "నందిగ్రామం",
        "desc_te": "శ్రీరాముని పాదుకలు ఉంచి భరతుడు తపస్సు చేస్తూ పాలించిన ప్రదేశం.",
        "name_hi": "नंदीग्राम",
        "desc_hi": "वह स्थान जहाँ भरत ने पादुका रखकर राजकाज संभाला।"
      },
      {
        "id": "c1_30",
        "name": "स्वयंवर मंडप",
        "desc": "मिथिला का विशाल राजदरबार जहाँ धनुष यज्ञ हुआ।",
        "correctSwipe": "RIGHT",
        "slug": "swayamvar_mandap",
        "image": "assets/cards/swayamvar_mandap.jpg",
        "name_en": "Swayamvar Pavilion",
        "desc_en": "Grand royal wedding pavilion in Mithila where Sita chose Rama.",
        "name_te": "స్వయంవర మండపం",
        "desc_te": "మిథిలా నగరంలో సీతా స్వయంవరం జరిగిన దివ్య మండపం.",
        "name_hi": "स्वयंवर मंडप",
        "desc_hi": "मिथिला का विशाल राजदरबार जहाँ धनुष यज्ञ हुआ।"
      },
      {
        "id": "c1_31",
        "name": "कनक भवन",
        "desc": "अयोध्या में सीता के स्वागत हेतु भेंट किया गया स्वर्ण महल।",
        "correctSwipe": "LEFT",
        "slug": "kanak_bhavan",
        "image": "assets/cards/kanak_bhavan.jpg",
        "name_en": "Kanak Bhavan",
        "desc_en": "Golden palace presented to Sita by Kaikeyi in Ayodhya.",
        "name_te": "కనక భవనం",
        "desc_te": "సీతారాముల కోసం అయోధ్యలో కైకేయి బహూకరించిన స్వర్ణ మహల్.",
        "name_hi": "कनक भवन",
        "desc_hi": "अयोध्या में सीता के स्वागत हेतु भेंट किया गया स्वर्ण महल।"
      },
      {
        "id": "c1_32",
        "name": "गंगा-सोन संगम",
        "desc": "विश्वामित्र संग यात्रा का मिथिला मार्ग पड़ाव।",
        "correctSwipe": "RIGHT",
        "slug": "ganga_son_sangam",
        "image": "assets/cards/ganga_son_sangam.jpg",
        "name_en": "Ganga-Son Confluence",
        "desc_en": "Sacred holy river confluence crossed during journey to Mithila.",
        "name_te": "గంగా-శోణ సంగమం",
        "desc_te": "మిథిలా ప్రయాణంలో విశ్వామిత్ర రామ లక్ష్మణులు దర్శించిన సంగమం.",
        "name_hi": "गंगा-सोन संगम",
        "desc_hi": "विश्वामित्र संग यात्रा का मिथिला मार्ग पड़ाव।"
      },
      {
        "id": "c1_33",
        "name": "सूर्यवंशी ध्वज",
        "desc": "अयोध्या की राजप्राचीर पर लहराने वाला ध्वज।",
        "correctSwipe": "LEFT",
        "slug": "suryavanshi_dhwaja",
        "image": "assets/cards/suryavanshi_dhwaja.jpg",
        "name_en": "Suryavanshi Standard",
        "desc_en": "Glorious royal sun-emblem banner of the solar dynasty of Ayodhya.",
        "name_te": "సూర్యవంశ ధ్వజం",
        "desc_te": "అయోధ్య రఘువంశానికి చెందిన ప్రసిద్ధ సూర్య పతాకం.",
        "name_hi": "सूर्यवंशी ध्वज",
        "desc_hi": "अयोध्या की राजप्राचीर पर लहराने वाला ध्वज।"
      },
      {
        "id": "c1_34",
        "name": "विदेह राजपताका",
        "desc": "मिथिला का पवित्र राज्य चिह्न ध्वज।",
        "correctSwipe": "RIGHT",
        "slug": "videha_rajpataka",
        "image": "assets/cards/videha_rajpataka.jpg",
        "name_en": "Videha Royal Banner",
        "desc_en": "Sovereign royal flag fluttering above the ramparts of Mithila.",
        "name_te": "విదేహ రాజపతాకం",
        "desc_te": "మిథిలా రాజ్య మహోన్నత రాజధ్వజం.",
        "name_hi": "विदेह राजपताका",
        "desc_hi": "मिथिला का पवित्र राज्य चिह्न ध्वज।"
      },
      {
        "id": "c1_35",
        "name": "ताड़का वन",
        "desc": "अयोध्या से मिथिला जाते समय मुक्त कराया गया भयावह वन।",
        "correctSwipe": "LEFT",
        "slug": "tadaka_vana",
        "image": "assets/cards/tadaka_vana.jpg",
        "name_en": "Tadaka Forest",
        "desc_en": "Forest near Ayodhya where young Rama vanquished demoness Tadaka.",
        "name_te": "తాటకా వనం",
        "desc_te": "అయోధ్య మార్గంలో శ్రీరాముడు తాటకను సంహరించిన వనం.",
        "name_hi": "ताड़का वन",
        "desc_hi": "अयोध्या से मिथिला जाते समय मुक्त कराया गया भयावह वन।"
      },
      {
        "id": "c1_36",
        "name": "जयमाला",
        "desc": "सीता द्वारा प्रभु राम के गले में डाली गई वरमाला।",
        "correctSwipe": "RIGHT",
        "slug": "jayamala",
        "image": "assets/cards/jayamala.jpg",
        "name_en": "Victory Garland",
        "desc_en": "Divine wedding garland placed by Princess Sita on Rama's neck in Mithila.",
        "name_te": "వరమాల",
        "desc_te": "మిథిలా స్వయంవరంలో సీతాదేవి శ్రీరాముని మెడలో వేసిన దివ్యమాల.",
        "name_hi": "जयमाला",
        "desc_hi": "सीता द्वारा प्रभु राम के गले में डाली गई वरमाला।"
      },
      {
        "id": "c1_37",
        "name": "हलकर्षण उत्सव",
        "desc": "जनक द्वारा धरती जोतने का मंगलकारी उत्सव।",
        "correctSwipe": "RIGHT",
        "slug": "halkarshan_utsav",
        "image": "assets/cards/halkarshan_utsav.jpg",
        "name_en": "Sacred Plough Festival",
        "desc_en": "Auspicious ploughing ceremony in Mithila where infant Sita was found.",
        "name_te": "హలకర్షణ ఉత్సవం",
        "desc_te": "మిథిలలో జనక మహారాజు భూమి దున్నుతుండగా సీతాదేవి లభించిన ఉత్సవం.",
        "name_hi": "हलकर्षण उत्सव",
        "desc_hi": "जनक द्वारा धरती जोतने का मंगलकारी उत्सव।"
      },
      {
        "id": "c1_38",
        "name": "सुमित्रा प्रासाद",
        "desc": "अयोध्या का शांत और साधनायुक्त राजमहल।",
        "correctSwipe": "LEFT",
        "slug": "sumitra_prasad",
        "image": "assets/cards/sumitra_prasad.jpg",
        "name_en": "Sumitra Palace",
        "desc_en": "Peaceful royal residence of Queen Sumitra in Ayodhya.",
        "name_te": "సుమిత్రా ప్రాసాదం",
        "desc_te": "అయోధ్య అంతఃపురంలో సుమిత్రా దేవి నివాస భవనం.",
        "name_hi": "सुमित्रा प्रासाद",
        "desc_hi": "अयोध्या का शांत और साधनायुक्त राजमहल।"
      },
      {
        "id": "c1_39",
        "name": "अश्वमेध अश्व",
        "desc": "अयोध्या के दिग्विजय का दिव्य श्वेत अश्व।",
        "correctSwipe": "LEFT",
        "slug": "ashwamedha_ashwa",
        "image": "assets/cards/ashwamedha_ashwa.jpg",
        "name_en": "Ashwamedha Steed",
        "desc_en": "Consecrated white steed released by Lord Rama from Ayodhya.",
        "name_te": "అశ్వమేధ అశ్వం",
        "desc_te": "శ్రీరాముడు అయోధ్యలో అశ్వమేధ యాగం చేసిన దివ్య అశ్వం.",
        "name_hi": "अश्वमेध अश्व",
        "desc_hi": "अयोध्या के दिग्विजय का दिव्य श्वेत अश्व।"
      },
      {
        "id": "c1_40",
        "name": "विश्वामित्र",
        "desc": "राम-लक्ष्मण को यज्ञ रक्षा और मिथिला ले जाने वाले गुरु।",
        "correctSwipe": "LEFT",
        "slug": "vishwamitra",
        "image": "assets/cards/vishwamitra.jpg",
        "name_en": "Sage Vishwamitra",
        "desc_en": "Brahmarshi who brought Rama and Lakshmana to Mithila.",
        "name_te": "విశ్వామిత్ర మహర్షి",
        "desc_te": "శ్రీరామ లక్ష్మణులను మిథిలా స్వయంవరానికి తీసుకువచ్చిన బ్రహ్మర్షి.",
        "name_hi": "विश्वामित्र",
        "desc_hi": "राम-लक्ष्मण को यज्ञ रक्षा और मिथिला ले जाने वाले गुरु।"
      }
    ],
    "thumb": "assets/games/cat_split_ayodhya.jpg",
    "title_en": "Ayodhya or Mithila",
    "title_hi": "अयोध्या या मिथिला",
    "title_te": "అయోధ్య లేదా మిథిల",
    "instruction_en": "Swipe towards Ayodhya or Mithila",
    "instruction_hi": "अयोध्या या मिथिला के पक्ष की ओर स्वाइप करें",
    "instruction_te": "అయోధ్య లేదా మిథిల వైపు స్వైప్ చేయండి",
    "vs_en": "Ayodhya VS Mithila",
    "vs_hi": "अयोध्या VS मिथिला",
    "vs_te": "అయోధ్య VS మిథిల"
  },
  "lanka_war": {
    "id": "cat_2_lanka_war",
    "title": "राम सेना या रावण सेना",
    "instruction": "श्रीराम सेना या रावण सेना की ओर स्वाइप करें",
    "leftSide": {
      "label": "बाएँ (राम सेना)",
      "name": "राम सेना",
      "bgColor": "#EA580C",
      "gateAsset": "assets/gates/gate_ram_sena.png",
      "name_en": "Rama Army",
      "name_hi": "राम सेना",
      "name_te": "రామ సైన్యం"
    },
    "rightSide": {
      "label": "दाएँ (रावण सेना)",
      "name": "रावण सेना",
      "bgColor": "#7F1D1D",
      "gateAsset": "assets/gates/gate_ravan_sena.png",
      "name_en": "Ravana Army",
      "name_hi": "रावण सेना",
      "name_te": "రావణ సైన్యం"
    },
    "cards": [
      {
        "id": "c2_01",
        "name": "हनुमान",
        "desc": "अतुलितबलधामं, लंका दहन करने वाले पवनपुत्र।",
        "correctSwipe": "LEFT",
        "slug": "hanuman",
        "image": "assets/cards/hanuman.jpg",
        "name_en": "Lord Hanuman",
        "desc_en": "Vayuputra, supreme devotion incarnate leading the Vanara army.",
        "name_te": "హనుమంతుడు",
        "desc_te": "వాయుపుత్రుడు, అంజనీనందనుడు, శ్రీరామ భక్తాగ్రగణ్యుడు.",
        "name_hi": "हनुमान",
        "desc_hi": "अतुलितबलधामं, लंका दहन करने वाले पवनपुत्र।"
      },
      {
        "id": "c2_02",
        "name": "रावण",
        "desc": "दस सिरों और बीस भुजाओं वाला लंकाधिपति।",
        "correctSwipe": "RIGHT",
        "slug": "ravan",
        "image": "assets/cards/ravan.jpg",
        "name_en": "King Ravana",
        "desc_en": "Mighty ten-headed Dashanana emperor of Golden Lanka.",
        "name_te": "రావణాసురుడు",
        "desc_te": "దశకంఠుడు, లంకాధిపతి, త్రైలోక్య విజేత.",
        "name_hi": "रावण",
        "desc_hi": "दस सिरों और बीस भुजाओं वाला लंकाधिपति।"
      },
      {
        "id": "c2_03",
        "name": "सुग्रीव",
        "desc": "किष्किंधा के वानर राज, राम के मित्र।",
        "correctSwipe": "LEFT",
        "slug": "sugriva",
        "image": "assets/cards/sugriva.jpg",
        "name_en": "King Sugriva",
        "desc_en": "King of the Vanaras, valiant ally of Lord Rama.",
        "name_te": "సుగ్రీవుడు",
        "desc_te": "వానర రాజు, కిష్కింధాధిపతి, శ్రీరాముని మిత్రుడు.",
        "name_hi": "सुग्रीव",
        "desc_hi": "किष्किंधा के वानर राज, राम के मित्र।"
      },
      {
        "id": "c2_04",
        "name": "मेघनाद (इंद्रजीत)",
        "desc": "रावण का ज्येष्ठ पुत्र, ब्रह्मास्त्र धारक।",
        "correctSwipe": "RIGHT",
        "slug": "meghnad",
        "image": "assets/cards/meghnad.jpg",
        "name_en": "Meghnada (Indrajit)",
        "desc_en": "Prince of Lanka, conqueror of Indra wielding celestial weapons.",
        "name_te": "మేఘనాథుడు (ఇంద్రజిత్తు)",
        "desc_te": "రావణుని వీరపుత్రుడు, ఇంద్రుని జయించిన మహావీరుడు.",
        "name_hi": "मेघनाद (इंद्रजीत)",
        "desc_hi": "रावण का ज्येष्ठ पुत्र, ब्रह्मास्त्र धारक।"
      },
      {
        "id": "c2_05",
        "name": "जाम्बवंत",
        "desc": "ऋक्ष राज, ज्ञान और धैर्य के सागर।",
        "correctSwipe": "LEFT",
        "slug": "jambavant",
        "image": "assets/cards/jambavant.jpg",
        "name_en": "King Jambavan",
        "desc_en": "Wise and immortal King of the Bears in Rama's army.",
        "name_te": "జాంబవంతుడు",
        "desc_te": "ఋక్షరాజ, చిరంజీవి, రామసైన్యంలో అత్యంత జ్ఞానియైన వీరుడు.",
        "name_hi": "जाम्बवंत",
        "desc_hi": "ऋक्ष राज, ज्ञान और धैर्य के सागर।"
      },
      {
        "id": "c2_06",
        "name": "कुंभकर्ण",
        "desc": "छह माह तक सोने वाला विशालकाय राक्षस।",
        "correctSwipe": "RIGHT",
        "slug": "kumbhkaran",
        "image": "assets/cards/kumbhkaran.jpg",
        "name_en": "Kumbhakarna",
        "desc_en": "Giant brother of Ravana possessing colossal, world-shaking might.",
        "name_te": "కుంభకర్ణుడు",
        "desc_te": "రావణుని తమ్ముడు, మహాకాయుడు, నిద్రాప్రియుడైన రాక్షస వీరుడు.",
        "name_hi": "कुंभकर्ण",
        "desc_hi": "छह माह तक सोने वाला विशालकाय राक्षस।"
      },
      {
        "id": "c2_07",
        "name": "अंगद",
        "desc": "बालि-पुत्र, जिनका पाँव लंका सभा में अडिग रहा।",
        "correctSwipe": "LEFT",
        "slug": "angada",
        "image": "assets/cards/angada.jpg",
        "name_en": "Prince Angada",
        "desc_en": "Son of Vali, fearless youth ambassador to Ravana's court.",
        "name_te": "అంగదుడు",
        "desc_te": "వాలి కుమారుడు, లంకా సభలో రాముని వీర దూత.",
        "name_hi": "अंगद",
        "desc_hi": "बालि-पुत्र, जिनका पाँव लंका सभा में अडिग रहा।"
      },
      {
        "id": "c2_08",
        "name": "शूर्पणखा",
        "desc": "रावण की बहन, जिसकी नाक लक्ष्मण ने काटी थी।",
        "correctSwipe": "RIGHT",
        "slug": "shurpanakha",
        "image": "assets/cards/shurpanakha.jpg",
        "name_en": "Shurpanakha",
        "desc_en": "Sister of Ravana who ignited the war between Rama and Lanka.",
        "name_te": "శూర్పణఖ",
        "desc_te": "రావణుని చెల్లెలు, రామ-రావణ సంగ్రామానికి మూల కారణం.",
        "name_hi": "शूर्पणखा",
        "desc_hi": "रावण की बहन, जिसकी नाक लक्ष्मण ने काटी थी।"
      },
      {
        "id": "c2_09",
        "name": "विभीषण",
        "desc": "धर्म की राह चुनकर राम की शरण में आए रावण-भ्राता।",
        "correctSwipe": "LEFT",
        "slug": "vibhishan",
        "image": "assets/cards/vibhishan.jpg",
        "name_en": "Vibhishana",
        "desc_en": "Righteous brother of Ravana who surrendered to Rama's shelter.",
        "name_te": "విభీషణుడు",
        "desc_te": "రావణుని ధర్మాత్ముడైన సోదరుడు, శ్రీరామ శరణాగతుడు.",
        "name_hi": "विभीषण",
        "desc_hi": "धर्म की राह चुनकर राम की शरण में आए रावण-भ्राता।"
      },
      {
        "id": "c2_10",
        "name": "मारीच",
        "desc": "स्वर्ण मृग बनकर छल करने वाला मायावी असुर।",
        "correctSwipe": "RIGHT",
        "slug": "maricha",
        "image": "assets/cards/maricha.jpg",
        "name_en": "Maricha",
        "desc_en": "Uncle of Ravana who took the form of the elusive Golden Deer.",
        "name_te": "మారీచుడు",
        "desc_te": "రావణుని మేనమామ, మాయా బంగారు జింకగా మారిన రాక్షసుడు.",
        "name_hi": "मारीच",
        "desc_hi": "स्वर्ण मृग बनकर छल करने वाला मायावी असुर।"
      },
      {
        "id": "c2_11",
        "name": "नल",
        "desc": "समुद्र पर तैरने वाले पत्थरों से सेतु बनाने वाले शिल्पी।",
        "correctSwipe": "LEFT",
        "slug": "nala",
        "image": "assets/cards/nala.jpg",
        "name_en": "Nala",
        "desc_en": "Divine architect Vanara who engineered the holy floating bridge.",
        "name_te": "నలుడు",
        "desc_te": "వానర శిల్పి, విశ్వకర్మ పుత్రుడు, రామసేతువును నిర్మించినవాడు.",
        "name_hi": "नल",
        "desc_hi": "समुद्र पर तैरने वाले पत्थरों से सेतु बनाने वाले शिल्पी।"
      },
      {
        "id": "c2_12",
        "name": "मन्दोदरी",
        "desc": "रावण की नीतिवान और पतिव्रता पटरानी।",
        "correctSwipe": "RIGHT",
        "slug": "mandodari",
        "image": "assets/cards/mandodari.jpg",
        "name_en": "Queen Mandodari",
        "desc_en": "Chaste, virtuous queen consort of King Ravana in Lanka.",
        "name_te": "మండోదరి",
        "desc_te": "రావణుని పట్టమహిషి, పతివ్రతారత్నం, మయబ్రహ్మ పుత్రిక.",
        "name_hi": "मन्दोदरी",
        "desc_hi": "रावण की नीतिवान और पतिव्रता पटरानी।"
      },
      {
        "id": "c2_13",
        "name": "नील",
        "desc": "वानर सेना के मुख्य युद्ध सेनापति।",
        "correctSwipe": "LEFT",
        "slug": "neela",
        "image": "assets/cards/neela.jpg",
        "name_en": "Neela",
        "desc_en": "Supreme Commander-in-Chief of the Vanara armed forces.",
        "name_te": "నీలుడు",
        "desc_te": "వానర సేనాధిపతి, అగ్నిదేవుని పుత్రుడు, యుద్ధవీరుడు.",
        "name_hi": "नील",
        "desc_hi": "वानर सेना के मुख्य युद्ध सेनापति।"
      },
      {
        "id": "c2_14",
        "name": "प्रहस्त",
        "desc": "रावण का मुख्य सेनापति और मामा।",
        "correctSwipe": "RIGHT",
        "slug": "prahasta",
        "image": "assets/cards/prahasta.jpg",
        "name_en": "Prahasta",
        "desc_en": "Chief General of the Rakshasa armed forces of Lanka.",
        "name_te": "ప్రహస్తుడు",
        "desc_te": "లంకా సేనాధిపతి, రావణునికి నమ్మకమైన ప్రధాన యోధుడు.",
        "name_hi": "प्रहस्त",
        "desc_hi": "रावण का मुख्य सेनापति और मामा।"
      },
      {
        "id": "c2_15",
        "name": "जटायु",
        "desc": "सीता हरण के समय प्राणों की आहुति देने वाले गृध्र राज।",
        "correctSwipe": "LEFT",
        "slug": "jatayu",
        "image": "assets/cards/jatayu.jpg",
        "name_en": "Jatayu",
        "desc_en": "Noble divine vulture King who gave his life defending Sita.",
        "name_te": "జటాయువు",
        "desc_te": "గద్దల రాజు, సీతా సంరక్షణలో ప్రాణాలు అర్పించిన పక్షి శ్రేష్ఠుడు.",
        "name_hi": "जटायु",
        "desc_hi": "सीता हरण के समय प्राणों की आहुति देने वाले गृध्र राज।"
      },
      {
        "id": "c2_16",
        "name": "खर",
        "desc": "जनस्थान का सेनापति, चौदह सहस्र राक्षसों का नायक।",
        "correctSwipe": "RIGHT",
        "slug": "khara",
        "image": "assets/cards/khara.jpg",
        "name_en": "Khara",
        "desc_en": "Demon governor of Janasthana slain by Lord Rama.",
        "name_te": "ఖరుడు",
        "desc_te": "జనస్థాన రాక్షస పాలకుడు, శ్రీరాముని చేతిలో హతమైనవాడు.",
        "name_hi": "खर",
        "desc_hi": "जनस्थान का सेनापति, चौदह सहस्र राक्षसों का नायक।"
      },
      {
        "id": "c2_17",
        "name": "सम्पाती",
        "desc": "जटायु के ज्येष्ठ भ्राता, जिन्होंने समुद्र पार लंका देखी।",
        "correctSwipe": "LEFT",
        "slug": "sampati",
        "image": "assets/cards/sampati.jpg",
        "name_en": "Sampati",
        "desc_en": "Elder brother of Jatayu who spotted Sita across the southern ocean.",
        "name_te": "సంపాతి",
        "desc_te": "జటాయువు సోదరుడు, సముద్రం దాటి లంకలో సీతను దర్శించినవాడు.",
        "name_hi": "सम्पाती",
        "desc_hi": "जटायु के ज्येष्ठ भ्राता, जिन्होंने समुद्र पार लंका देखी।"
      },
      {
        "id": "c2_18",
        "name": "दूषण",
        "desc": "जनस्थान में खर का सह-सेनापति।",
        "correctSwipe": "RIGHT",
        "slug": "dushana",
        "image": "assets/cards/dushana.jpg",
        "name_en": "Dushana",
        "desc_en": "Fierce demon commander serving under Khara in Dandakaranya.",
        "name_te": "దూషణుడు",
        "desc_te": "ఖరుని సేనాని, దండకారణ్యంలో రాముని చేత సంహరింపబడ్డాడు.",
        "name_hi": "दूषण",
        "desc_hi": "जनस्थान में खर का सह-सेनापति।"
      },
      {
        "id": "c2_19",
        "name": "शबरी",
        "desc": "मतंग आश्रम की तपस्विनी, बेर खिलाने वाली अनन्य भक्त।",
        "correctSwipe": "LEFT",
        "slug": "shabari",
        "image": "assets/cards/shabari.jpg",
        "name_en": "Shabari",
        "desc_en": "Devoted forest ascetic who offered sweet berries to Lord Rama.",
        "name_te": "శబరి",
        "desc_te": "మతంగ మహర్షి శిష్యురాలు, రామునికి ఎంగిలి పండ్లు సమర్పించిన భక్తురాలు.",
        "name_hi": "शबरी",
        "desc_hi": "मतंग आश्रम की तपस्विनी, बेर खिलाने वाली अनन्य भक्त।"
      },
      {
        "id": "c2_20",
        "name": "अक्षयकुमार",
        "desc": "रावण का कनिष्ठ पुत्र, अशोक वाटिका में वीरगति पाने वाला।",
        "correctSwipe": "RIGHT",
        "slug": "akshayakumara",
        "image": "assets/cards/akshayakumara.jpg",
        "name_en": "Akshayakumara",
        "desc_en": "Valiant youngest prince of Ravana slain by Hanuman in Ashok Vatika.",
        "name_te": "అక్షయకుమారుడు",
        "desc_te": "రావణుని చిన్న కుమారుడు, అశోకవాటికలో హనుమంతుని చేత హతుడయ్యాడు.",
        "name_hi": "अक्षयकुमार",
        "desc_hi": "रावण का कनिष्ठ पुत्र, अशोक वाटिका में वीरगति पाने वाला।"
      },
      {
        "id": "c2_21",
        "name": "सुषेण",
        "desc": "लंका युद्ध के मुख्य वानर वैद्य, संजीवनी के ज्ञाता।",
        "correctSwipe": "LEFT",
        "slug": "sushena",
        "image": "assets/cards/sushena.jpg",
        "name_en": "Sushena",
        "desc_en": "Chief royal physician of the Vanara army, father of Queen Tara.",
        "name_te": "సుషేణుడు",
        "desc_te": "వానర రాజ్య ప్రధాన వైద్యుడు, తార యొక్క తండ్రి.",
        "name_hi": "सुषेण",
        "desc_hi": "लंका युद्ध के मुख्य वानर वैद्य, संजीवनी के ज्ञाता।"
      },
      {
        "id": "c2_22",
        "name": "अतिकाय",
        "desc": "रावण और धन्यमालिनी का पर्वतकाय पुत्र।",
        "correctSwipe": "RIGHT",
        "slug": "atikaya",
        "image": "assets/cards/atikaya.jpg",
        "name_en": "Atikaya",
        "desc_en": "Colossal Rakshasa warrior of Lanka vanquished by Lakshmana.",
        "name_te": "అతికాయుడు",
        "desc_te": "రావణుని వీరపుత్రుడు, లక్ష్మణుని బాణానికి కూలిన మహాకాయుడు.",
        "name_hi": "अतिकाय",
        "desc_hi": "रावण और धन्यमालिनी का पर्वतकाय पुत्र।"
      },
      {
        "id": "c2_23",
        "name": "केसरी",
        "desc": "हनुमान जी के पराक्रमी वानर पिता।",
        "correctSwipe": "LEFT",
        "slug": "kesari",
        "image": "assets/cards/kesari.jpg",
        "name_en": "Kesari",
        "desc_en": "Mighty Vanara chieftain, heroic father of Lord Hanuman.",
        "name_te": "కేసరి",
        "desc_te": "వానర వీరుడు, హనుమంతుని తండ్రి.",
        "name_hi": "केसरी",
        "desc_hi": "हनुमान जी के पराक्रमी वानर पिता।"
      },
      {
        "id": "c2_24",
        "name": "त्रिशिरा",
        "desc": "तीन सिरों वाला शक्तिशाली राक्षस योद्धा।",
        "correctSwipe": "RIGHT",
        "slug": "trishira",
        "image": "assets/cards/trishira.jpg",
        "name_en": "Trishira",
        "desc_en": "Three-headed Rakshasa warrior in Ravana's imperial army.",
        "name_te": "త్రిశిరుడు",
        "desc_te": "మూడు తలల రాక్షస వీరుడు, రావణుని సేనలో ప్రసిద్ధుడు.",
        "name_hi": "त्रिशिरा",
        "desc_hi": "तीन सिरों वाला शक्तिशाली राक्षस योद्धा।"
      },
      {
        "id": "c2_25",
        "name": "दधिमुख",
        "desc": "सुग्रीव के मधुवन के रक्षक वानर।",
        "correctSwipe": "LEFT",
        "slug": "dadhimukha",
        "image": "assets/cards/dadhimukha.jpg",
        "name_en": "Dadhimukha",
        "desc_en": "Guardian chieftain of the sacred royal Madhuvana of Sugriva.",
        "name_te": "దధిముఖుడు",
        "desc_te": "సుగ్రీవుని మధువన రక్షకుడు, వానర నాయకుడు.",
        "name_hi": "दधिमुख",
        "desc_hi": "सुग्रीव के मधुवन के रक्षक वानर।"
      },
      {
        "id": "c2_26",
        "name": "महिरावण",
        "desc": "पाताल लोक का स्वामी, तंत्र-मंत्र का मायावी।",
        "correctSwipe": "RIGHT",
        "slug": "mahiravana",
        "image": "assets/cards/mahiravana.jpg",
        "name_en": "Mahiravana",
        "desc_en": "Sorcerer king of Patala Lanka who abducted Rama and Lakshmana.",
        "name_te": "మహిరావణుడు",
        "desc_te": "పాతాళ లంకాధిపతి, మాయావి రాక్షసుడు.",
        "name_hi": "महिरावण",
        "desc_hi": "पाताल लोक का स्वामी, तंत्र-मंत्र का मायावी।"
      },
      {
        "id": "c2_27",
        "name": "तारा",
        "desc": "किष्किंधा की महारानी, बालि की बुद्धिमती पत्नी।",
        "correctSwipe": "LEFT",
        "slug": "tara",
        "image": "assets/cards/tara.jpg",
        "name_en": "Queen Tara",
        "desc_en": "Wise and diplomatic Queen of Kishkindha, mother of Angada.",
        "name_te": "తారా దేవి",
        "desc_te": "కిష్కింధ రాణి, వాలి భార్య, అంగదుని తల్లి, మహా వివేకవంతురాలు.",
        "name_hi": "तारा",
        "desc_hi": "किष्किंधा की महारानी, बालि की बुद्धिमती पत्नी।"
      },
      {
        "id": "c2_28",
        "name": "कालनेमि",
        "desc": "हनुमान जी का मार्ग रोकने वाला छली मायावी।",
        "correctSwipe": "RIGHT",
        "slug": "kalanemi",
        "image": "assets/cards/kalanemi.jpg",
        "name_en": "Kalanemi",
        "desc_en": "Cunning demon sent by Ravana to intercept Hanuman's herb quest.",
        "name_te": "కాలనేమి",
        "desc_te": "సంజీవిని తేకుండా హనుమంతుడిని అడ్డుకోవడానికి వచ్చిన రాక్షసుడు.",
        "name_hi": "कालनेमि",
        "desc_hi": "हनुमान जी का मार्ग रोकने वाला छली मायावी।"
      },
      {
        "id": "c2_29",
        "name": "रुमा",
        "desc": "सुग्रीव की पत्नी, किष्किंधा की राजमहिषी।",
        "correctSwipe": "LEFT",
        "slug": "ruma",
        "image": "assets/cards/ruma.jpg",
        "name_en": "Ruma",
        "desc_en": "Queen consort of King Sugriva in Kishkindha.",
        "name_te": "రుమ",
        "desc_te": "సుగ్రీవుని ప్రియ భార్య, కిష్కింధ రాణి.",
        "name_hi": "रुमा",
        "desc_hi": "सुग्रीव की पत्नी, किष्किंधा की राजमहिषी।"
      },
      {
        "id": "c2_30",
        "name": "त्रिजटा",
        "desc": "अशोक वाटिका में सीता की रक्षा व ढांढस बंधाने वाली राक्षसी।",
        "correctSwipe": "LEFT",
        "slug": "trijata",
        "image": "assets/cards/trijata.jpg",
        "name_en": "Trijata",
        "desc_en": "Kind Rakshasi in Ashok Vatika who comforted and protected Sita.",
        "name_te": "త్రిజట",
        "desc_te": "అశోకవాటికలో సీతాదేవికి సాంత్వన చేకూర్చిన ధర్మాత్మురాలైన రాక్షసి.",
        "name_hi": "त्रिजटा",
        "desc_hi": "अशोक वाटिका में सीता की रक्षा व ढांढस बंधाने वाली राक्षसी।"
      },
      {
        "id": "c2_31",
        "name": "संजीवनी बूटी",
        "desc": "लक्ष्मण के प्राण बचाने वाली द्रोणागिरि की दिव्य औषधि।",
        "correctSwipe": "LEFT",
        "slug": "sanjeevani_booti",
        "image": "assets/cards/sanjeevani_booti.jpg",
        "name_en": "Sanjeevani Herb",
        "desc_en": "Miraculous life-saving celestial herb retrieved by Hanuman.",
        "name_te": "సంజీవిని మూలిక",
        "desc_te": "లక్ష్మణుని ప్రాణాలను కాపాడిన దివ్య ఔషధ పర్వతం.",
        "name_hi": "संजीवनी बूटी",
        "desc_hi": "लक्ष्मण के प्राण बचाने वाली द्रोणागिरि की दिव्य औषधि।"
      },
      {
        "id": "c2_32",
        "name": "स्वर्ण लंका",
        "desc": "रावण की अभेद्य त्रिकूट पर्वत पर बसी सोने की नगरी।",
        "correctSwipe": "RIGHT",
        "slug": "swarna_lanka",
        "image": "assets/cards/swarna_lanka.jpg",
        "name_en": "Golden Lanka",
        "desc_en": "Magnificent island fortress of King Ravana crafted from gold.",
        "name_te": "స్వర్ణ లంక",
        "desc_te": "రావణుని రాజధాని, బంగారు లంకా నగరం.",
        "name_hi": "स्वर्ण लंका",
        "desc_hi": "रावण की अभेद्य त्रिकूट पर्वत पर बसी सोने की नगरी।"
      },
      {
        "id": "c2_33",
        "name": "राम सेतु",
        "desc": "भारत से लंका तक निर्मित पाषाण मार्ग।",
        "correctSwipe": "LEFT",
        "slug": "ram_setu",
        "image": "assets/cards/ram_setu.jpg",
        "name_en": "Ram Setu Bridge",
        "desc_en": "Legendary causeway built by Vanaras across the ocean to Lanka.",
        "name_te": "రామసేతువు",
        "desc_te": "వానరులు సముద్రంపై నిర్మించిన అద్భుత దివ్య వంతెన.",
        "name_hi": "राम सेतु",
        "desc_hi": "भारत से लंका तक निर्मित पाषाण मार्ग।"
      },
      {
        "id": "c2_34",
        "name": "पुष्पक विमान",
        "desc": "आकाश में उड़ने वाला मन की गति से चलने वाला विमान।",
        "correctSwipe": "RIGHT",
        "slug": "pushpak_viman",
        "image": "assets/cards/pushpak_viman.jpg",
        "name_en": "Pushpaka Vimana",
        "desc_en": "Celestial flying aerial chariot used by Ravana and Lord Rama.",
        "name_te": "పుష్పక విమానం",
        "desc_te": "కుబేరుని దివ్య విమానం, రాముడు అయోధ్యకు తిరిగొచ్చిన రథం.",
        "name_hi": "पुष्पक विमान",
        "desc_hi": "आकाश में उड़ने वाला मन की गति से चलने वाला विमान।"
      },
      {
        "id": "c2_35",
        "name": "अशोक वाटिका",
        "desc": "रावण का वह उद्यान जहाँ सीता जी को बंदी रखा गया।",
        "correctSwipe": "RIGHT",
        "slug": "ashok_vatika",
        "image": "assets/cards/ashok_vatika.jpg",
        "name_en": "Ashok Vatika",
        "desc_en": "Pleasure garden in Lanka where Goddess Sita was held captive.",
        "name_te": "అశోకవాటిక",
        "desc_te": "లంకలో సీతాదేవిని బంధించిన అశోక వృక్షాల తోట.",
        "name_hi": "अशोक वाटिका",
        "desc_hi": "रावण का वह उद्यान जहाँ सीता जी को बंदी रखा गया।"
      }
    ],
    "thumb": "assets/games/cat_split_lanka.jpg",
    "title_en": "Rama Army or Ravana Army",
    "title_hi": "राम सेना या रावण सेना",
    "title_te": "రామ సైన్యం లేదా రావణ సైన్యం",
    "instruction_en": "Swipe towards Rama Army or Ravana Army",
    "instruction_hi": "राम सेना या रावण सेना की ओर स्वाइप करें",
    "instruction_te": "రామ సైన్యం లేదా రావణ సైన్యం వైపు స్వైప్ చేయండి",
    "vs_en": "Vanaras VS Rakshasas",
    "vs_hi": "वानर सेना VS राक्षस सेना",
    "vs_te": "వానర సైన్యం VS రాక్షసులు"
  },
  "pandav_kaurav": {
    "id": "cat_3_mahabharat",
    "title": "पाण्डव या कौरव",
    "instruction": "पाण्डव पक्ष या कौरव पक्ष की ओर स्वाइप करें",
    "leftSide": {
      "label": "बाएँ (पाण्डव)",
      "name": "पाण्डव",
      "bgColor": "#15803D",
      "gateAsset": "assets/gates/gate_pandav.png",
      "name_en": "Pandavas",
      "name_hi": "पाण्डव",
      "name_te": "పాండవులు"
    },
    "rightSide": {
      "label": "दाएँ (कौरव)",
      "name": "कौरव",
      "bgColor": "#991B1B",
      "gateAsset": "assets/gates/gate_kaurav.png",
      "name_en": "Kauravas",
      "name_hi": "कौरव",
      "name_te": "కౌరవులు"
    },
    "cards": [
      {
        "id": "c3_01",
        "name": "अर्जुन",
        "desc": "गांडीवधारी, श्रीकृष्ण के प्रिय सखा पार्थ।",
        "correctSwipe": "LEFT",
        "slug": "arjun",
        "image": "assets/cards/arjun.jpg",
        "name_en": "Arjuna",
        "desc_en": "Unrivaled archer of the Pandavas, wielder of the celestial Gandiva bow.",
        "name_te": "అర్జునుడు",
        "desc_te": "గాండీవధారి, పాండవ మధ్యముడు, శ్రీకృష్ణుని ఆత్మమిత్రుడు.",
        "name_hi": "अर्जुन",
        "desc_hi": "गांडीवधारी, श्रीकृष्ण के प्रिय सखा पार्थ।"
      },
      {
        "id": "c3_02",
        "name": "दुर्योधन",
        "desc": "हस्तिनापुर का अहंकारी ज्येष्ठ कौरव युवराज।",
        "correctSwipe": "RIGHT",
        "slug": "duryodhan",
        "image": "assets/cards/duryodhan.jpg",
        "name_en": "Duryodhana",
        "desc_en": "Eldest of the hundred Kauravas, ambitious prince of Hastinapura.",
        "name_te": "దుర్యోధనుడు",
        "desc_te": "కౌరవ జ్యేష్ఠుడు, హస్తినాపుర రాజకుమారుడు, గదాయుద్ధ నిపుణుడు.",
        "name_hi": "दुर्योधन",
        "desc_hi": "हस्तिनापुर का अहंकारी ज्येष्ठ कौरव युवराज।"
      },
      {
        "id": "c3_03",
        "name": "युधिष्ठिर",
        "desc": "धर्मराज, सत्य और न्याय के अटूट प्रतीक।",
        "correctSwipe": "LEFT",
        "slug": "yudhisthir",
        "image": "assets/cards/yudhisthir.jpg",
        "name_en": "Yudhishthira (Dharmaraja)",
        "desc_en": "Eldest Pandava, embodiment of truth, righteousness, and justice.",
        "name_te": "యుధిష్ఠిరుడు (ధర్మరాజు)",
        "desc_te": "పాండవాగ్రజుడు, సత్య ధర్మాల ప్రతీక, ఇంద్రప్రస్థ చక్రవర్తి.",
        "name_hi": "युधिष्ठिर",
        "desc_hi": "धर्मराज, सत्य और न्याय के अटूट प्रतीक।"
      },
      {
        "id": "c3_04",
        "name": "दुःशासन",
        "desc": "दुर्योधन का आज्ञाकारी और क्रूर अनुज।",
        "correctSwipe": "RIGHT",
        "slug": "dushasan",
        "image": "assets/cards/dushasan.jpg",
        "name_en": "Dushasana",
        "desc_en": "Second Kaurava brother, enforcer of Duryodhana's wicked schemes.",
        "name_te": "దుశ్శాసనుడు",
        "desc_te": "దుర్యోధనుని అనుజుడు, ద్రౌపదీ వస్త్రాపహరణం చేసిన పాపి.",
        "name_hi": "दुःशासन",
        "desc_hi": "दुर्योधन का आज्ञाकारी और क्रूर अनुज।"
      },
      {
        "id": "c3_05",
        "name": "भीम",
        "desc": "दस सहस्र हाथियों के बल वाले गदाधारी पाण्डव।",
        "correctSwipe": "LEFT",
        "slug": "bheem",
        "image": "assets/cards/bheem.jpg",
        "name_en": "Bheemasena",
        "desc_en": "Second Pandava possessing the formidable strength of ten thousand elephants.",
        "name_te": "భీమసేనుడు",
        "desc_te": "వాయుపుత్రుడు, పదివేల ఏనుగుల బలం గల పాండవ వీరుడు.",
        "name_hi": "भीम",
        "desc_hi": "दस सहस्र हाथियों के बल वाले गदाधारी पाण्डव।"
      },
      {
        "id": "c3_06",
        "name": "शकुनि",
        "desc": "गांधार नरेश, चौसर के कपटी पांसों का स्वामी।",
        "correctSwipe": "RIGHT",
        "slug": "shakuni",
        "image": "assets/cards/shakuni.jpg",
        "name_en": "Shakuni",
        "desc_en": "King of Gandhara, master of dice and cunning strategist of the Kauravas.",
        "name_te": "శకుని",
        "desc_te": "గాంధార రాజు, పాచికల మాయావి, కౌరవుల కుట్రల రూపకర్త.",
        "name_hi": "शकुनि",
        "desc_hi": "गांधार नरेश, चौसर के कपटी पांसों का स्वामी।"
      },
      {
        "id": "c3_07",
        "name": "कर्ण",
        "desc": "दानवीर अंगराज, सूर्यपुत्र (कौरव सेनापति)।",
        "correctSwipe": "RIGHT",
        "slug": "karna",
        "image": "assets/cards/karna.jpg",
        "name_en": "Karna (Radheya)",
        "desc_en": "Mighty sun-born warrior, supreme donor and steadfast champion of Duryodhana.",
        "name_te": "కర్ణుడు",
        "desc_te": "సూర్యపుత్రుడు, దానవీరుడు, దుర్యోధనుని ప్రాణమిత్రుడు.",
        "name_hi": "कर्ण",
        "desc_hi": "दानवीर अंगराज, सूर्यपुत्र (कौरव सेनापति)।"
      },
      {
        "id": "c3_08",
        "name": "द्रौपदी",
        "desc": "पांचाल राजकुमारी, पाण्डवों की पटरानी यज्ञसेनी।",
        "correctSwipe": "LEFT",
        "slug": "draupadi",
        "image": "assets/cards/draupadi.jpg",
        "name_en": "Draupadi (Panchali)",
        "desc_en": "Fire-born Empress of the Pandavas, queen of Indraprastha.",
        "name_te": "ద్రౌపది (పాంచాలి)",
        "desc_te": "యజ్ఞసేని, అగ్ని సంభవ, పాండవుల పట్టమహిషి.",
        "name_hi": "द्रौपदी",
        "desc_hi": "पांचाल राजकुमारी, पाण्डवों की पटरानी यज्ञसेनी।"
      },
      {
        "id": "c3_09",
        "name": "द्रोणाचार्य",
        "desc": "कौरव-पाण्डव दोनों के गुरु, कौरव सेना के प्रधान सेनापति।",
        "correctSwipe": "RIGHT",
        "slug": "dronacharya",
        "image": "assets/cards/dronacharya.jpg",
        "name_en": "Dronacharya",
        "desc_en": "Supreme military preceptor of both the Pandavas and Kauravas.",
        "name_te": "ద్రోణాచార్యుడు",
        "desc_te": "కౌరవ పాండవుల గురువు, దివ్యాస్త్ర కోవిదుడు.",
        "name_hi": "द्रोणाचार्य",
        "desc_hi": "कौरव-पाण्डव दोनों के गुरु, कौरव सेना के प्रधान सेनापति।"
      },
      {
        "id": "c3_10",
        "name": "अभिमन्यु",
        "desc": "अर्जुन पुत्र, जिसने अकेले चक्रव्यूह को भेदा।",
        "correctSwipe": "LEFT",
        "slug": "abhimanyu",
        "image": "assets/cards/abhimanyu.jpg",
        "name_en": "Abhimanyu",
        "desc_en": "Valiant son of Arjuna and Subhadra who penetrated the deadly Chakravyuha.",
        "name_te": "అభిమన్యుడు",
        "desc_te": "అర్జునుని కుమారుడు, చక్రవ్యూహాన్ని ఛేదించిన అజేయ బాలవీరుడు.",
        "name_hi": "अभिमन्यु",
        "desc_hi": "अर्जुन पुत्र, जिसने अकेले चक्रव्यूह को भेदा।"
      },
      {
        "id": "c3_11",
        "name": "अश्वत्थामा",
        "desc": "गुरु द्रोण के अमर पुत्र, माथे पर दिव्य मणि धारक।",
        "correctSwipe": "RIGHT",
        "slug": "ashwatthama",
        "image": "assets/cards/ashwatthama.jpg",
        "name_en": "Ashwatthama",
        "desc_en": "Immortal son of Drona fighting fiercely on the Kaurava side.",
        "name_te": "అశ్వత్థామ",
        "desc_te": "ద్రోణుని కుమారుడు, చిరంజీవి, కౌరవ సేనాని.",
        "name_hi": "अश्वत्थामा",
        "desc_hi": "गुरु द्रोण के अमर पुत्र, माथे पर दिव्य मणि धारक।"
      },
      {
        "id": "c3_12",
        "name": "कुंती",
        "desc": "पाण्डवों की पूज्य राजमाता, पांडु की पटरानी।",
        "correctSwipe": "LEFT",
        "slug": "kunti",
        "image": "assets/cards/kunti.jpg",
        "name_en": "Mother Kunti",
        "desc_en": "Devoted queen mother of the Pandavas, mother of Karna.",
        "name_te": "కుంతీదేవి",
        "desc_te": "పాండవుల మాతృమూర్తి, కర్ణుని కన్నతల్లి.",
        "name_hi": "कुंती",
        "desc_hi": "पाण्डवों की पूज्य राजमाता, पांडु की पटरानी।"
      },
      {
        "id": "c3_13",
        "name": "गांधारी",
        "desc": "पतिव्रता महारानी, जिन्होंने आँखों पर पट्टी बांधी।",
        "correctSwipe": "RIGHT",
        "slug": "gandhari",
        "image": "assets/cards/gandhari.jpg",
        "name_en": "Queen Gandhari",
        "desc_en": "Devoted, blindfolded Queen of Hastinapura, mother of the Kauravas.",
        "name_te": "గాంధారి",
        "desc_te": "ధృతరాష్ట్రుని పత్ని, కన్నులకు గంతలు కట్టుకున్న పతివ్రత, కౌరవుల తల్లి.",
        "name_hi": "गांधारी",
        "desc_hi": "पतिव्रता महारानी, जिन्होंने आँखों पर पट्टी बांधी।"
      },
      {
        "id": "c3_14",
        "name": "सहदेव",
        "desc": "त्रिकालदर्शी कनिष्ठ पाण्डव, नीति और ज्योतिष के ज्ञाता।",
        "correctSwipe": "LEFT",
        "slug": "sahadev",
        "image": "assets/cards/sahadev.jpg",
        "name_en": "Sahadeva",
        "desc_en": "Youngest Pandava, supreme astrologer and master of wisdom.",
        "name_te": "సహదేవుడు",
        "desc_te": "పాండవులలో చిన్నవాడు, త్రికాలజ్ఞాని, జ్యోతిష్య నిపుణుడు.",
        "name_hi": "सहदेव",
        "desc_hi": "त्रिकालदर्शी कनिष्ठ पाण्डव, नीति और ज्योतिष के ज्ञाता।"
      },
      {
        "id": "c3_15",
        "name": "जयद्रथ",
        "desc": "सिंधु नरेश, जिसने चक्रव्यूह का द्वार पाण्डवों के लिए रोका।",
        "correctSwipe": "RIGHT",
        "slug": "jayadrath",
        "image": "assets/cards/jayadrath.jpg",
        "name_en": "Jayadratha",
        "desc_en": "King of Sindhu, brother-in-law of Duryodhana on the Kaurava side.",
        "name_te": "జయద్రథుడు",
        "desc_te": "సింధు రాజు, దుర్యోధనుని బావ, కౌరవ పక్ష యోధుడు.",
        "name_hi": "जयद्रथ",
        "desc_hi": "सिंधु नरेश, जिसने चक्रव्यूह का द्वार पाण्डवों के लिए रोका।"
      },
      {
        "id": "c3_16",
        "name": "नकुल",
        "desc": "अश्व विद्या और अनुपम सौंदर्य के स्वामी पाण्डव।",
        "correctSwipe": "LEFT",
        "slug": "nakul",
        "image": "assets/cards/nakul.jpg",
        "name_en": "Nakula",
        "desc_en": "Fourth Pandava, incomparable in physical beauty and equestrian skills.",
        "name_te": "నకులుడు",
        "desc_te": "మాద్రి పుత్రుడు, పాండవులలో అత్యంత రూపవంతుడు, అశ్వవిద్యానిపుణుడు.",
        "name_hi": "नकुल",
        "desc_hi": "अश्व विद्या और अनुपम सौंदर्य के स्वामी पाण्डव।"
      },
      {
        "id": "c3_17",
        "name": "कृपाचार्य",
        "desc": "कुरु राज्य के कुलगुरु और महारथी।",
        "correctSwipe": "RIGHT",
        "slug": "kripacharya",
        "image": "assets/cards/kripacharya.jpg",
        "name_en": "Kripacharya",
        "desc_en": "Immortal family priest and guru serving Hastinapura.",
        "name_te": "కృపాచార్యుడు",
        "desc_te": "హస్తినాపుర కులగురువు, చిరంజీవి, కౌరవ పక్ష మహారథి.",
        "name_hi": "कृपाचार्य",
        "desc_hi": "कुरु राज्य के कुलगुरु और महारथी।"
      },
      {
        "id": "c3_18",
        "name": "विदुर",
        "desc": "सत्य और नीति के ज्ञाता धर्मनिष्ठ महामति।",
        "correctSwipe": "LEFT",
        "slug": "vidur",
        "image": "assets/cards/vidur.jpg",
        "name_en": "Mahatma Vidura",
        "desc_en": "Prime Minister of Hastinapura, incarnation of Dharma.",
        "name_te": "విదురుడు",
        "desc_te": "హస్తినాపుర ప్రధాన మంత్రి, ధర్మ స్వరూపుడు, నీతి శాస్త్రవేత్త.",
        "name_hi": "विदुर",
        "desc_hi": "सत्य और नीति के ज्ञाता धर्मनिष्ठ महामति।"
      },
      {
        "id": "c3_19",
        "name": "जरासंध",
        "desc": "मगध का क्रूर सम्राट, कंस का श्वसुर।",
        "correctSwipe": "RIGHT",
        "slug": "jarasandh",
        "image": "assets/cards/jarasandh.jpg",
        "name_en": "King Jarasandha",
        "desc_en": "Mighty emperor of Magadha allied with the enemies of Krishna.",
        "name_te": "జరాసంధుడు",
        "desc_te": "మగధ రాజు, అజేయ బలశాలి, భీమునితో ద్వంద్వయుద్ధం చేసినవాడు.",
        "name_hi": "जरासंध",
        "desc_hi": "मगध का क्रूर सम्राट, कंस का श्वसुर।"
      },
      {
        "id": "c3_20",
        "name": "घटोत्कच",
        "desc": "भीम और हिडिम्बा का महाबली मायावी असुर पुत्र।",
        "correctSwipe": "LEFT",
        "slug": "ghatotkach",
        "image": "assets/cards/ghatotkach.jpg",
        "name_en": "Ghatotkacha",
        "desc_en": "Giant Rakshasa son of Bheema who fought heroically for the Pandavas.",
        "name_te": "ఘటోత్కచుడు",
        "desc_te": "భీమ-హిడింబల కుమారుడు, కురుక్షేత్రంలో పాండవుల వైపు పోరాడిన రాక్షస వీరుడు.",
        "name_hi": "घटोत्कच",
        "desc_hi": "भीम और हिडिम्बा का महाबली मायावी असुर पुत्र।"
      },
      {
        "id": "c3_21",
        "name": "शिशुपाल",
        "desc": "चेदि राज, श्रीकृष्ण के हाथों सुदर्शन चक्र से दंड पाने वाला।",
        "correctSwipe": "RIGHT",
        "slug": "shishupal",
        "image": "assets/cards/shishupal.jpg",
        "name_en": "Shishupala",
        "desc_en": "King of Chedi slain by Krishna at the Rajasuya Yajna.",
        "name_te": "శిశుపాలుడు",
        "desc_te": "చేది రాజు, రాజసూయ యాగంలో శ్రీకృష్ణుని సుదర్శన చక్రానికి హతుడైనవాడు.",
        "name_hi": "शिशुपाल",
        "desc_hi": "चेदि राज, श्रीकृष्ण के हाथों सुदर्शन चक्र से दंड पाने वाला।"
      },
      {
        "id": "c3_22",
        "name": "सात्यकि",
        "desc": "श्रीकृष्ण की नारायणी सेना के निष्ठावान यदुवंशी वीर।",
        "correctSwipe": "LEFT",
        "slug": "satyaki",
        "image": "assets/cards/satyaki.jpg",
        "name_en": "Satyaki",
        "desc_en": "Valiant Vrishni chieftain and disciple of Arjuna fighting for Pandavas.",
        "name_te": "సాత్యకి",
        "desc_te": "శ్రీకృష్ణుని యాదవ సేనాని, అర్జునుని ప్రియ శిష్యుడు, పాండవ పక్ష యోధుడు.",
        "name_hi": "सात्यकि",
        "desc_hi": "श्रीकृष्ण की नारायणी सेना के निष्ठावान यदुवंशी वीर।"
      },
      {
        "id": "c3_23",
        "name": "कीचक",
        "desc": "मत्स्य देश का कामी और अभिमानी सेनापति।",
        "correctSwipe": "RIGHT",
        "slug": "keechak",
        "image": "assets/cards/keechak.jpg",
        "name_en": "Keechaka",
        "desc_en": "Arrogant general of Matsya kingdom slain by Bheema during exile.",
        "name_te": "కీచకుడు",
        "desc_te": "మత్స్య దేశ సేనాని, అజ్ఞాతవాసంలో భీముని చేతిలో హతమైనవాడు.",
        "name_hi": "कीचक",
        "desc_hi": "मत्स्य देश का कामी और अभिमानी सेनापति।"
      },
      {
        "id": "c3_24",
        "name": "धृष्टद्युम्न",
        "desc": "पाण्डव सेना का मुख्य सेनापति, द्रोण वधक।",
        "correctSwipe": "LEFT",
        "slug": "dhrishtadyumna",
        "image": "assets/cards/dhrishtadyumna.jpg",
        "name_en": "Dhrishtadyumna",
        "desc_en": "Fire-born Commander-in-Chief of the Pandava army, brother of Draupadi.",
        "name_te": "ధృష్టద్యుమ్నుడు",
        "desc_te": "పాండవ సేనాధిపతి, ద్రౌపది సోదరుడు, ద్రోణుని సంహరించినవాడు.",
        "name_hi": "धृष्टद्युम्न",
        "desc_hi": "पाण्डव सेना का मुख्य सेनापति, द्रोण वधक।"
      },
      {
        "id": "c3_25",
        "name": "कंस",
        "desc": "मथुरा का अत्याचारी राजा, श्रीकृष्ण के मामा।",
        "correctSwipe": "RIGHT",
        "slug": "kansa",
        "image": "assets/cards/kansa.jpg",
        "name_en": "King Kamsa",
        "desc_en": "Tyrant ruler of Mathura and uncle of Lord Krishna.",
        "name_te": "కంసుడు",
        "desc_te": "మధురా పాలకుడు, శ్రీకృష్ణుని మేనమామ, క్రూర రాక్షస రాక్షస గుణ చక్రవర్తి.",
        "name_hi": "कंस",
        "desc_hi": "मथुरा का अत्याचारी राजा, श्रीकृष्ण के मामा।"
      }
    ],
    "thumb": "assets/games/cat_split_mahabharata.jpg",
    "title_en": "Pandavas or Kauravas",
    "title_hi": "पाण्डव या कौरव",
    "title_te": "పాండవులు లేదా కౌరవులు",
    "instruction_en": "Swipe towards Pandavas or Kauravas",
    "instruction_hi": "पाण्डव या कौरव पक्ष की ओर स्वाइप करें",
    "instruction_te": "పాండవులు లేదా కౌరవుల వైపు స్వైప్ చేయండి",
    "vs_en": "Pandavas VS Kauravas",
    "vs_hi": "पाण्डव VS कौरव",
    "vs_te": "పాండవులు VS కౌరవులు"
  }
};

  var SWIPE_UI_I18N = {
    en: {
      chooseLanguage: "Choose Game Language",
      chooseCategory: "Choose Category",
      play: "Play",
      correct: "Correct Side! +50 🪙",
      wrong: "Wrong Side!",
      cardsLeft: "Cards Left",
      score: "Score",
      charReview: "Character Review",
      replay: "Play Again",
      nextCategory: "Next Category",
      close: "Close"
    },
    hi: {
      chooseLanguage: "खेल की भाषा चुनें",
      chooseCategory: "श्रेणी चुनें",
      play: "खेलें",
      correct: "सही पक्ष! +50 🪙",
      wrong: "गलत पक्ष!",
      cardsLeft: "शेष कार्ड",
      score: "स्कोर",
      charReview: "चरित्र समीक्षा",
      replay: "पुनः खेलें",
      nextCategory: "अगली श्रेणी",
      close: "बंद करें"
    },
    te: {
      chooseLanguage: "ఆట భాషను ఎంచుకోండి",
      chooseCategory: "వర్గాన్ని ఎంచుకోండి",
      play: "ఆడండి",
      correct: "సరైన వైపు! +50 🪙",
      wrong: "తప్పు వైపు!",
      cardsLeft: "మిగిలిన కార్డులు",
      score: "స్కోరు",
      charReview: "పాత్రల సమీక్ష",
      replay: "మళ్లీ ఆడండి",
      nextCategory: "తదుపరి వర్గం",
      close: "మూసివేయి"
    }
  };


  // ══════════════════════════════════════════════════════════════════════════════
  // 🏹 SWIPE GAME LAUNCHER SCREEN (Exact Match to Image 1)
  // ══════════════════════════════════════════════════════════════════════════════
  epicGameState.currentLanguage = localStorage.getItem('swipe_game_lang') || 'en';
  epicGameState.selectedLauncherCategory = 'cat_1_ramayana';

  var LAUNCHER_CATEGORY_LIST = ['cat_1_ramayana', 'cat_2_lanka_war', 'cat_3_mahabharat'];

  window.openSwipeLauncher = function(categoryKey) {
    if (categoryKey && SWIPE_CATEGORIES[categoryKey]) {
      epicGameState.selectedLauncherCategory = SWIPE_CATEGORIES[categoryKey].id;
    }
    hideBottomNavForGames();

    var launcher = document.getElementById('swipe-launcher-screen');
    if (launcher) {
      launcher.style.display = 'flex';
      launcher.classList.add('active');
    }

    // Hide gameplay arena and review screen while in launcher
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'none';
    var rev = document.getElementById('swipe-review-arena');
    if (rev) rev.style.display = 'none';

    // Synchronize UI
    updateLauncherLanguageUI();
    renderLauncherCarousel();
  };

  window.openSwipeGame = function(categoryKey) {
    window.openSwipeLauncher(categoryKey);
  };

  window.closeSwipeLauncher = function() {
    var launcher = document.getElementById('swipe-launcher-screen');
    if (launcher) {
      launcher.style.display = 'none';
      launcher.classList.remove('active');
    }
    restoreBottomNavIfExited();
  };

  window.selectSwipeLanguage = function(langCode) {
    if (!['en', 'hi', 'te'].includes(langCode)) langCode = 'en';
    epicGameState.currentLanguage = langCode;
    try {
      localStorage.setItem('swipe_game_lang', langCode);
    } catch(e) {}

    playSound('click');
    if (navigator.vibrate) navigator.vibrate(20);

    updateLauncherLanguageUI();
    renderLauncherCarousel();
  };

  function updateLauncherLanguageUI() {
    var lang = epicGameState.currentLanguage || 'en';
    var i18n = SWIPE_UI_I18N[lang] || SWIPE_UI_I18N.en;

    // Update active highlight and wings on language cards
    document.querySelectorAll('.swipe-lang-card').forEach(function(card) {
      var cardLang = card.getAttribute('data-lang');
      if (cardLang === lang) {
        card.classList.add('active');
      } else {
        card.classList.remove('active');
      }
    });

    // Update ribbon texts
    var langRibbon = document.getElementById('swipe-launch-lang-ribbon-text');
    if (langRibbon) langRibbon.textContent = i18n.chooseLanguage;

    var catHeader = document.getElementById('swipe-launch-cat-header-text');
    if (catHeader) catHeader.textContent = i18n.chooseCategory;

    var playText = document.getElementById('swipe-launch-play-btn-text');
    if (playText) playText.textContent = i18n.play;

    // Update coins
    var coinVals = document.querySelectorAll('.epic-coins-val');
    coinVals.forEach(function(el) {
      el.textContent = (epicGameState.coins >= 1000) ? Math.floor(epicGameState.coins / 1000) + 'K' : epicGameState.coins;
    });
  }

  function renderLauncherCarousel() {
    var lang = epicGameState.currentLanguage || 'en';
    var currentCat = epicGameState.selectedLauncherCategory || 'cat_1_ramayana';

    // Update Category VS texts
    LAUNCHER_CATEGORY_LIST.forEach(function(cid, idx) {
      var cat = SWIPE_CATEGORIES[cid];
      if (!cat) return;
      var num = idx + 1;
      var leftEl = document.getElementById('vs-cat-' + num + '-left');
      var rightEl = document.getElementById('vs-cat-' + num + '-right');
      if (leftEl) {
        leftEl.textContent = (lang === 'te' && cat.leftSide.name_te) ? cat.leftSide.name_te : ((lang === 'en' && cat.leftSide.name_en) ? cat.leftSide.name_en : (cat.leftSide.name_hi || cat.leftSide.name));
      }
      if (rightEl) {
        rightEl.textContent = (lang === 'te' && cat.rightSide.name_te) ? cat.rightSide.name_te : ((lang === 'en' && cat.rightSide.name_en) ? cat.rightSide.name_en : (cat.rightSide.name_hi || cat.rightSide.name));
      }
    });

    // Update 3D carousel position & active classes
    var cards = document.querySelectorAll('.swipe-cat-slide-card');
    var activeIdx = LAUNCHER_CATEGORY_LIST.indexOf(currentCat);
    if (activeIdx === -1) activeIdx = 0;

    cards.forEach(function(card, idx) {
      card.classList.remove('active', 'peek-left', 'peek-right');
      if (idx === activeIdx) {
        card.classList.add('active');
      } else if (idx < activeIdx) {
        card.classList.add('peek-left');
      } else {
        card.classList.add('peek-right');
      }
    });
  }

  function selectSwipeCategory(catId) {
    if (epicGameState.selectedLauncherCategory === catId) return;
    epicGameState.selectedLauncherCategory = catId;
    playSound('click');
    if (navigator.vibrate) navigator.vibrate(15);
    renderLauncherCarousel();
  }
  window.selectSwipeCategory = selectSwipeCategory;

  function nextSwipeCategory() {
    var currIdx = LAUNCHER_CATEGORY_LIST.indexOf(epicGameState.selectedLauncherCategory);
    var nextIdx = (currIdx + 1) % LAUNCHER_CATEGORY_LIST.length;
    selectSwipeCategory(LAUNCHER_CATEGORY_LIST[nextIdx]);
  }
  window.nextSwipeCategory = nextSwipeCategory;

  function prevSwipeCategory() {
    var currIdx = LAUNCHER_CATEGORY_LIST.indexOf(epicGameState.selectedLauncherCategory);
    var prevIdx = (currIdx - 1 + LAUNCHER_CATEGORY_LIST.length) % LAUNCHER_CATEGORY_LIST.length;
    selectSwipeCategory(LAUNCHER_CATEGORY_LIST[prevIdx]);
  }
  window.prevSwipeCategory = prevSwipeCategory;

  // Add Touch Gestures for Category Carousel Slider
  (function initCarouselSwipeGestures() {
    var startX = 0;
    var startY = 0;
    var isMoving = false;

    function attach() {
      var stage = document.getElementById('swipe-cat-carousel-stage');
      if (!stage) return;

      stage.addEventListener('touchstart', function(e) {
        if (!e.touches || e.touches.length === 0) return;
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        isMoving = true;
      }, { passive: true });

      stage.addEventListener('touchend', function(e) {
        if (!isMoving || !e.changedTouches || e.changedTouches.length === 0) return;
        isMoving = false;
        var diffX = e.changedTouches[0].clientX - startX;
        var diffY = e.changedTouches[0].clientY - startY;

        if (Math.abs(diffX) > 40 && Math.abs(diffX) > Math.abs(diffY)) {
          if (diffX < 0) {
            window.nextSwipeCategory();
          } else {
            window.prevSwipeCategory();
          }
        }
      }, { passive: true });
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', attach);
    } else {
      attach();
    }
  })();

  window.startSwipeGameFromLauncher = function() {
    playSound('select');
    if (navigator.vibrate) navigator.vibrate(30);

    // Close Launcher
    var launcher = document.getElementById('swipe-launcher-screen');
    if (launcher) {
      launcher.style.display = 'none';
      launcher.classList.remove('active');
    }

    // Open Arena
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'flex';
    hideBottomNavForGames();

    // Start Game with chosen category and chosen language
    initSwipeGame(epicGameState.selectedLauncherCategory, epicGameState.currentLanguage);
  };

  // ══════════════════════════════════════════════════════════════════════════════
  // 2. SWIPE GAME LOGIC & MULTILINGUAL BASE PHYSICS
  // ══════════════════════════════════════════════════════════════════════════════
  var activeCardEl = null;
  var isDragging = false;
  var startX = 0;
  var startY = 0;
  var currentX = 0;
  var currentY = 0;

  function initSwipeGame(categoryKey, langCode) {
    categoryKey = categoryKey || epicGameState.selectedLauncherCategory || 'cat_1_ramayana';
    var cat = SWIPE_CATEGORIES[categoryKey] || SWIPE_CATEGORIES.cat_1_ramayana;
    epicGameState.currentCategory = cat.id;

    var lang = langCode || epicGameState.currentLanguage || 'en';
    epicGameState.currentLanguage = lang;

    epicGameState.ayodhyaScore = 0;
    epicGameState.mithilaScore = 0;
    epicGameState.currentIndex = 0;
    epicGameState.correctCount = 0;
    epicGameState.swipedHistory = [];

    // Shuffle characters for replayability
    var list = (cat.cards || []).slice();
    for (var i = list.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var temp = list[i];
      list[i] = list[j];
      list[j] = temp;
    }
    epicGameState.deck = list;

    // Multilingual Category Title & Instructions
    var titleText = (lang === 'te' && cat.title_te) ? cat.title_te : ((lang === 'en' && cat.title_en) ? cat.title_en : (cat.title_hi || cat.title));
    var instText = (lang === 'te' && cat.instruction_te) ? cat.instruction_te : ((lang === 'en' && cat.instruction_en) ? cat.instruction_en : (cat.instruction_hi || cat.instruction));
    var leftName = (lang === 'te' && cat.leftSide.name_te) ? cat.leftSide.name_te : ((lang === 'en' && cat.leftSide.name_en) ? cat.leftSide.name_en : (cat.leftSide.name_hi || cat.leftSide.name));
    var rightName = (lang === 'te' && cat.rightSide.name_te) ? cat.rightSide.name_te : ((lang === 'en' && cat.rightSide.name_en) ? cat.rightSide.name_en : (cat.rightSide.name_hi || cat.rightSide.name));

    // Update Arena labels & header
    var titleEl = document.getElementById('swipe-cat-title');
    if (titleEl) titleEl.textContent = titleText;

    var instEl = document.getElementById('swipe-instruction');
    if (instEl) instEl.textContent = instText;

    var leftLabel = document.getElementById('swipe-left-portal-label');
    if (leftLabel) leftLabel.textContent = leftName;

    var rightLabel = document.getElementById('swipe-right-portal-label');
    if (rightLabel) rightLabel.textContent = rightName;

    var leftScore = document.getElementById('swipe-left-score');
    if (leftScore) {
      leftScore.textContent = '0';
      leftScore.style.background = cat.leftSide.bgColor;
    }

    var rightScore = document.getElementById('swipe-right-score');
    if (rightScore) {
      rightScore.textContent = '0';
      rightScore.style.background = cat.rightSide.bgColor;
    }

    // Update Gates / Portals
    var leftGateImg = document.getElementById('swipe-gate-left') || document.querySelector('#swipe-portal-left .swipe-portal-bg');
    if (leftGateImg) {
      leftGateImg.src = 'assets/games/portal_left_sun.png';
      leftGateImg.onerror = function () { this.src = 'assets/games/portal_ayodhya.jpg'; };
    }

    var rightGateImg = document.getElementById('swipe-gate-right') || document.querySelector('#swipe-portal-right .swipe-portal-bg');
    if (rightGateImg) {
      rightGateImg.src = 'assets/games/portal_right_demon.png';
      rightGateImg.onerror = function () { this.src = 'assets/games/portal_mithila.jpg'; };
    }

    // Update Quick Desktop Accessibility Buttons
    var btnLeft = document.getElementById('swipe-btn-left');
    if (btnLeft) {
      btnLeft.textContent = '⟵ ' + leftName;
      btnLeft.style.background = cat.leftSide.bgColor;
    }
    var btnRight = document.getElementById('swipe-btn-right');
    if (btnRight) {
      btnRight.textContent = rightName + ' ⟶';
      btnRight.style.background = cat.rightSide.bgColor;
    }

    renderCurrentCard();
  }

  function renderCurrentCard() {
    var stage = document.getElementById('swipe-card-deck');
    if (!stage) return;

    if (epicGameState.currentIndex >= epicGameState.deck.length) {
      setTimeout(showCharacterReviewScreen, 400);
      return;
    }

    var char = epicGameState.deck[epicGameState.currentIndex];
    var lang = epicGameState.currentLanguage || 'en';
    var charName = (lang === 'te' && char.name_te) ? char.name_te : ((lang === 'en' && char.name_en) ? char.name_en : (char.name_hi || char.name));

    stage.innerHTML = `
      <div class="swipe-card-underlay swipe-card-underlay-2"></div>
      <div class="swipe-card-underlay swipe-card-underlay-1"></div>
      
      <div class="swipe-main-card" id="swipe-active-card">
        <div class="swipe-char-portrait-container">
          <img src="${char.image}" alt="${charName}" class="swipe-char-portrait" onerror="this.src='assets/games/char_sunaina.jpg';">
        </div>
        <img src="assets/games/card_gold_winged_frame.png" alt="Frame" class="swipe-card-winged-overlay">
        <div class="swipe-char-name-bar">${charName}</div>
      </div>
    `;

    activeCardEl = document.getElementById('swipe-active-card');
    if (activeCardEl) {
      attachCardSwipeListeners(activeCardEl);
    }
  }

  function attachCardSwipeListeners(el) {
    el.addEventListener('mousedown', onDragStart);
    document.addEventListener('mousemove', onDragMove);
    document.addEventListener('mouseup', onDragEnd);

    el.addEventListener('touchstart', onDragStart, { passive: false });
    document.addEventListener('touchmove', onDragMove, { passive: false });
    document.addEventListener('touchend', onDragEnd);
  }

  function onDragStart(e) {
    if (!activeCardEl) return;
    isDragging = true;
    var point = e.touches ? e.touches[0] : e;
    startX = point.clientX;
    startY = point.clientY;
    currentX = startX;
    currentY = startY;
    activeCardEl.style.transition = 'none';
  }

  function onDragMove(e) {
    if (!isDragging || !activeCardEl) return;
    var point = e.touches ? e.touches[0] : e;
    currentX = point.clientX;
    currentY = point.clientY;

    var deltaX = currentX - startX;
    var deltaY = currentY - startY;
    var rotation = deltaX * 0.08;

    activeCardEl.style.transform = `translate(${deltaX}px, ${deltaY}px) rotate(${rotation}deg)`;

    // Visual portal feedback highlight
    var leftPortal = document.getElementById('swipe-portal-left');
    var rightPortal = document.getElementById('swipe-portal-right');

    if (deltaX < -50) {
      if (leftPortal) leftPortal.classList.add('portal-pulse-active');
      if (rightPortal) rightPortal.classList.remove('portal-pulse-active');
    } else if (deltaX > 50) {
      if (rightPortal) rightPortal.classList.add('portal-pulse-active');
      if (leftPortal) leftPortal.classList.remove('portal-pulse-active');
    } else {
      if (leftPortal) leftPortal.classList.remove('portal-pulse-active');
      if (rightPortal) rightPortal.classList.remove('portal-pulse-active');
    }
  }

  function onDragEnd() {
    if (!isDragging || !activeCardEl) return;
    isDragging = false;

    var leftPortal = document.getElementById('swipe-portal-left');
    var rightPortal = document.getElementById('swipe-portal-right');
    if (leftPortal) leftPortal.classList.remove('portal-pulse-active');
    if (rightPortal) rightPortal.classList.remove('portal-pulse-active');

    var deltaX = currentX - startX;
    var threshold = window.innerWidth * 0.22;

    if (deltaX < -threshold) {
      handleSwipeCommit('left');
    } else if (deltaX > threshold) {
      handleSwipeCommit('right');
    } else {
      // Snap back with spring animation
      activeCardEl.style.transition = 'transform 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
      activeCardEl.style.transform = 'translate(0px, 0px) rotate(0deg)';
    }
  }

  window.swipeCardManual = function(direction) {
    handleSwipeCommit(direction);
  };

  function handleSwipeCommit(direction) {
    if (!activeCardEl) return;
    var char = epicGameState.deck[epicGameState.currentIndex];
    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var lang = epicGameState.currentLanguage || 'en';
    var i18n = SWIPE_UI_I18N[lang] || SWIPE_UI_I18N.en;

    var isLeft = direction === 'left';
    var chosenSide = isLeft ? 'LEFT' : 'RIGHT';
    var isCorrect = (char.correctSwipe === chosenSide);

    // Animate Card out towards Portal
    var flyX = isLeft ? -window.innerWidth * 1.2 : window.innerWidth * 1.2;
    var flyY = 220;
    var flyRot = isLeft ? -45 : 45;

    activeCardEl.style.transition = 'transform 0.32s ease-in, opacity 0.28s ease-in';
    activeCardEl.style.transform = `translate(${flyX}px, ${flyY}px) rotate(${flyRot}deg) scale(0.65)`;
    activeCardEl.style.opacity = '0';

    setTimeout(function () {
      if (isCorrect) {
        playSound('correct');
        epicGameState.correctCount++;
        addCoins(50);

        if (isLeft) {
          epicGameState.ayodhyaScore++;
          var sEl = document.getElementById('swipe-left-score');
          if (sEl) sEl.textContent = epicGameState.ayodhyaScore;
        } else {
          epicGameState.mithilaScore++;
          var sEl = document.getElementById('swipe-right-score');
          if (sEl) sEl.textContent = epicGameState.mithilaScore;
        }

        showSwipeFeedbackBanner(true, char, chosenSide);
        showCoinToast('+50 🪙');
      } else {
        playSound('wrong');
        showSwipeFeedbackBanner(false, char, chosenSide);
      }

      epicGameState.swipedHistory.push({
        character: char,
        direction: direction,
        chosenSide: chosenSide,
        isCorrect: isCorrect
      });

      epicGameState.currentIndex++;
      renderCurrentCard();
    }, 280);
  }

  function showSwipeFeedbackBanner(isCorrect, char, chosenSide) {
    var arena = document.getElementById('swipe-arena');
    if (!arena) return;

    var existing = document.getElementById('swipe-feedback-banner');
    if (existing && existing.parentNode) {
      existing.parentNode.removeChild(existing);
    }

    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var lang = epicGameState.currentLanguage || 'en';
    
    // Correct side details
    var correctIsLeft = char.correctSwipe === 'LEFT';
    var correctSideObj = correctIsLeft ? cat.leftSide : cat.rightSide;
    var correctSideName = (lang === 'te' && correctSideObj.name_te) ? correctSideObj.name_te : 
                          ((lang === 'en' && correctSideObj.name_en) ? correctSideObj.name_en : 
                          (correctSideObj.name_hi || correctSideObj.name));

    var headingText = "";
    var subText = "";

    if (isCorrect) {
      if (lang === 'te') {
        headingText = "సరైనది!";
        subText = `<span style="color:#C2410C; font-weight:900;">${correctSideName}</span> కోసం పోరాడారు`;
      } else if (lang === 'en') {
        headingText = "Correct!";
        subText = `Fought for <span style="color:#C2410C; font-weight:900;">${correctSideName}</span>`;
      } else {
        headingText = "सही!";
        subText = `<span style="color:#C2410C; font-weight:900;">${correctSideName}</span> के लिए लड़े`;
      }
    } else {
      if (lang === 'te') {
        headingText = "తప్పు!";
        subText = `సరైన పక్షం: <span style="color:#15803D; font-weight:900;">${correctSideName}</span>`;
      } else if (lang === 'en') {
        headingText = "Incorrect!";
        subText = `Correct side: <span style="color:#15803D; font-weight:900;">${correctSideName}</span>`;
      } else {
        headingText = "गलत!";
        subText = `सही पक्ष: <span style="color:#15803D; font-weight:900;">${correctSideName}</span>`;
      }
    }

    var banner = document.createElement('div');
    banner.id = 'swipe-feedback-banner';
    banner.className = 'swipe-feedback-banner ' + (isCorrect ? 'feedback-correct' : 'feedback-wrong');
    banner.innerHTML = `
      <img src="assets/games/banner_feedback_base.png" alt="Feedback Base" class="feedback-banner-base-img">
      <div class="feedback-banner-text-content">
        <div class="feedback-banner-heading ${isCorrect ? 'text-correct' : 'text-wrong'}">${headingText}</div>
        <div class="feedback-banner-subtext">${subText}</div>
      </div>
    `;

    arena.appendChild(banner);

    // Auto remove after 1.35 seconds
    setTimeout(function() {
      if (banner && banner.parentNode) {
        banner.classList.add('feedback-banner-fadeout');
        setTimeout(function() {
          if (banner.parentNode) banner.parentNode.removeChild(banner);
        }, 300);
      }
    }, 1250);
  }

  function showCoinToast(msg) {
    var toast = document.createElement('div');
    toast.textContent = msg;
    toast.style.position = 'fixed';
    toast.style.top = '40%';
    toast.style.left = '50%';
    toast.style.transform = 'translate(-50%, -50%)';
    toast.style.background = 'rgba(26, 11, 46, 0.9)';
    toast.style.color = '#FDE68A';
    toast.style.border = '1.5px solid #F59E0B';
    toast.style.borderRadius = '16px';
    toast.style.padding = '6px 16px';
    toast.style.fontSize = '1.1rem';
    toast.style.fontWeight = '900';
    toast.style.zIndex = '35000';
    toast.style.pointerEvents = 'none';
    toast.style.boxShadow = '0 6px 20px rgba(0,0,0,0.5)';
    toast.style.animation = 'coinPop 0.8s ease forwards';
    document.body.appendChild(toast);

    setTimeout(function () {
      if (toast.parentNode) toast.parentNode.removeChild(toast);
    }, 850);
  }

  function showCharacterReviewScreen() {
    hideBottomNavForGames();
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'none';

    var rev = document.getElementById('swipe-review-arena');
    if (!rev) return;
    rev.style.display = 'flex';

    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var characters = cat.cards || [];
    var lang = epicGameState.currentLanguage || 'en';

    // Render tokens list in bottom rail
    var rail = document.getElementById('swipe-review-tokens-rail');
    if (rail) {
      rail.innerHTML = '';
      characters.forEach(function (c, idx) {
        var token = document.createElement('div');
        token.className = 'swipe-char-token' + (idx === 0 ? ' active-token' : '');
        var tokenName = (lang === 'te' && c.name_te) ? c.name_te : ((lang === 'en' && c.name_en) ? c.name_en : (c.name_hi || c.name));
        token.innerHTML = `
          <div class="swipe-token-circle">
            <img src="${c.image}" alt="${tokenName}" class="swipe-token-avatar" onerror="this.src='assets/games/char_sunaina.jpg';">
            <div class="swipe-token-check">✓</div>
          </div>
          <div class="swipe-token-label">${tokenName}</div>
        `;
        token.onclick = function () {
          document.querySelectorAll('.swipe-char-token').forEach(t => t.classList.remove('active-token'));
          token.classList.add('active-token');
          renderReviewCard(c);
        };
        rail.appendChild(token);
      });
    }

    // Default select first character
    if (characters.length > 0) {
      renderReviewCard(characters[0]);
    }
  }

  function renderReviewCard(char) {
    var card = document.getElementById('swipe-review-card-container');
    if (!card) return;

    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var lang = epicGameState.currentLanguage || 'en';
    var isLeft = char.correctSwipe === 'LEFT';
    var sideName = isLeft ? 
      ((lang === 'te' && cat.leftSide.name_te) ? cat.leftSide.name_te : ((lang === 'en' && cat.leftSide.name_en) ? cat.leftSide.name_en : (cat.leftSide.name_hi || cat.leftSide.name))) :
      ((lang === 'te' && cat.rightSide.name_te) ? cat.rightSide.name_te : ((lang === 'en' && cat.rightSide.name_en) ? cat.rightSide.name_en : (cat.rightSide.name_hi || cat.rightSide.name)));
    var sideBg = isLeft ? cat.leftSide.bgColor : cat.rightSide.bgColor;

    var charName = (lang === 'te' && char.name_te) ? char.name_te : ((lang === 'en' && char.name_en) ? char.name_en : (char.name_hi || char.name));
    var charDesc = (lang === 'te' && char.desc_te) ? char.desc_te : ((lang === 'en' && char.desc_en) ? char.desc_en : (char.desc_hi || char.desc));

    card.innerHTML = `
      <div class="swipe-review-card">
        <div class="swipe-review-img-wrap">
          <img src="${char.image}" alt="${charName}" class="swipe-review-img" onerror="this.src='assets/games/char_sunaina.jpg';">
          <div class="swipe-review-team-badge" style="background:${sideBg}; color:#FFF;">${sideName}</div>
        </div>
        <div class="swipe-review-info-body">
          <div class="swipe-review-char-name">${charName}</div>
          <div class="swipe-review-divider"></div>
          <div class="swipe-review-char-desc">${charDesc}</div>
          <button class="swipe-review-network-btn" onclick="window.openCharacterNetworkModal('${char.id}')">📖 ${lang === 'te' ? 'వివరాలు' : (lang === 'en' ? 'Context' : 'महाकाव्य संदर्भ')}</button>
        </div>
      </div>
    `;
  }


  // ── Bottom Navigation Bar Management for Epic Games ──
  function hideBottomNavForGames() {
    var nav = document.getElementById('curved-fluid-bottom-nav');
    if (nav) nav.classList.add('nav-hidden');
    var allNavs = document.querySelectorAll('.curved-fluid-bottom-nav, .app-bottom-nav, .bottom-nav');
    allNavs.forEach(function (el) { el.classList.add('nav-hidden'); });
  }

  function restoreBottomNavIfExited() {
    var activePage = '';
    if (typeof window.currentPage !== 'undefined' && window.currentPage) {
      activePage = window.currentPage;
    } else {
      var p = document.querySelector('.page.active');
      if (p) activePage = p.id;
    }
    // If still in Epic Games page or reader or 3d mandir, keep it hidden
    if (activePage === 'page-epic-games' || activePage === 'page-reader' || activePage === 'page-3d-mandir') {
      return;
    }
    var nav = document.getElementById('curved-fluid-bottom-nav');
    if (nav) nav.classList.remove('nav-hidden');
    var allNavs = document.querySelectorAll('.curved-fluid-bottom-nav, .app-bottom-nav, .bottom-nav');
    allNavs.forEach(function (el) { el.classList.remove('nav-hidden'); });
  }

  // Listen for page navigation events in the app
  document.addEventListener('bhakti-page-change', function (e) {
    if (e.detail === 'page-epic-games') {
      hideBottomNavForGames();
    } else if (e.detail !== 'page-reader' && e.detail !== 'page-3d-mandir') {
      restoreBottomNavIfExited();
    }
  });

  // If already on page-epic-games at load
  if (typeof window.currentPage !== 'undefined' && window.currentPage === 'page-epic-games') {
    hideBottomNavForGames();
  }

  // ══════════════════════════════════════════════════════════════════════════════

  // 4. RESULT / TRY AGAIN MODAL (frame_84s.jpg)
  // ══════════════════════════════════════════════════════════════════════════════
  function showSwipeResultModal() {
    hideBottomNavForGames();
    var modal = document.getElementById('swipe-result-modal');
    if (!modal) return;

    var total = epicGameState.deck.length;
    var correct = epicGameState.correctCount;
    var isVictory = correct >= Math.floor(total * 0.7);

    if (isVictory) playSound('victory');

    var lang = epicGameState.currentLanguage || 'en';

    // Dynamic Ribbon text
    var ribbonText = isVictory ? (lang === 'te' ? 'విజయవంతమైనది!' : (lang === 'en' ? 'VICTORY!' : 'बधाई हो!')) : 'TRY AGAIN';
    var ribbonEl = document.getElementById('swipe-result-ribbon-text');
    if (ribbonEl) ribbonEl.textContent = ribbonText;

    // Coins Earned
    var coinsEarnedEl = document.getElementById('swipe-result-coins-earned');
    if (coinsEarnedEl) coinsEarnedEl.textContent = `+${correct * 50}`;

    // Heading
    var headEl = document.getElementById('swipe-result-heading');
    if (headEl) headEl.textContent = isVictory ? 
      (lang === 'te' ? 'అద్భుతమైన జ్ఞానం!' : (lang === 'en' ? 'Brilliant Knowledge!' : 'अद्भुत ज्ञान!')) : 
      (lang === 'te' ? 'మంచి ప్రయత్నం!' : (lang === 'en' ? 'Good Effort!' : 'बढ़िया प्रयास!'));

    // Score text
    var scoreTextEl = document.getElementById('swipe-result-score-text');
    if (scoreTextEl) scoreTextEl.textContent = (lang === 'te') ? 
      `మీరు ${correct}/${total} పాత్రలను పూర్తి చేసారు` : 
      ((lang === 'en') ? `Completed ${correct}/${total} characters` : `आपने पूरे किए ${correct}/${total} पात्र`);

    // Stat chips
    var streakEl = document.getElementById('swipe-result-streak-count');
    if (streakEl) streakEl.textContent = correct * 50;

    var totalEl = document.getElementById('swipe-result-total-val');
    if (totalEl) totalEl.textContent = `${correct}/${total}`;

    // Motivational Message
    var msgEl = document.getElementById('swipe-result-message');
    if (msgEl) msgEl.textContent = isVictory ? 
      (lang === 'te' ? 'మీరు అన్ని పాత్రలను సరైన వైపు చేర్చారు.' : (lang === 'en' ? 'You guided all characters to their true side!' : 'आपने सभी पात्रों को उनके सही पक्ष में पहुँचाया।')) : 
      (lang === 'te' ? 'కొన్ని पात्रలకి మరో ప్రయత్నం అవసరం.' : (lang === 'en' ? 'Some characters need another try.' : 'कुछ पात्रों को एक और कोशिश चाहिए।'));

    // Buttons Multilingual Text
    var btnNew = document.getElementById('swipe-res-btn-new');
    if (btnNew) btnNew.textContent = (lang === 'te') ? 'కొత్త ఆట' : ((lang === 'en') ? 'Play Again' : 'नया खेल');

    var btnLore = document.getElementById('swipe-res-btn-lore');
    if (btnLore) btnLore.textContent = (lang === 'te') ? 'తెలుసుకోండి' : ((lang === 'en') ? 'Learn Lore' : 'जानें');

    var btnRetry = document.getElementById('swipe-res-btn-retry');
    if (btnRetry) btnRetry.textContent = (lang === 'te') ? 'మళ్లీ' : ((lang === 'en') ? 'Retry' : 'दोबारा');

    modal.style.display = 'flex';
  }

  function hideSwipeResultModal() {
    var modal = document.getElementById('swipe-result-modal');
    if (modal) modal.style.display = 'none';
    restoreBottomNavIfExited();
  }

  // ══════════════════════════════════════════════════════════════════════════════
  // 5. RELATED GAMES (Match, JigSaw, PadaBandham)
  // ══════════════════════════════════════════════════════════════════════════════

  // ══════════════════════════════════════════════════════════════════════════════
  // 5. RELATED GAMES (Match, JigSaw, PadaBandham) WITH COMPREHENSIVE APP DEITY IMAGES
  // ══════════════════════════════════════════════════════════════════════════════

  // Master Repository of all authentic sacred deity images in the app
  var ALL_APP_DEITIES = [
    { id: 'ganesh', name: 'श्री गणेश', title: 'विघ्नहर्ता श्री गणेश जी', img: 'assets/deity_ganesh.jpg' },
    { id: 'krishna', name: 'श्री कृष्ण', title: 'मुरलीधर श्री कृष्ण जी', img: 'assets/deity_krishna.jpg' },
    { id: 'hanuman', name: 'श्री हनुमान', title: 'संकटमोचन हनुमान जी', img: 'assets/deity_hanuman.jpg' },
    { id: 'shiva', name: 'महादेव शिव', title: 'देवों के देव महादेव', img: 'assets/deity_shiva.jpg' },
    { id: 'durga', name: 'माँ दुर्गा', title: 'सिंहवाहिनी माँ दुर्गा', img: 'assets/deity_durga_hd.jpg' },
    { id: 'lakshmi', name: 'माँ लक्ष्मी', title: 'महालक्ष्मी माता', img: 'assets/deity_lakshmi.jpg' },
    { id: 'ram', name: 'श्री राम', title: 'मर्यादा पुरुषोत्तम श्री राम', img: 'assets/deity_ram.jpg' },
    { id: 'saraswati', name: 'माँ सरस्वती', title: 'विद्या दायिनी माँ सरस्वती', img: 'assets/deity_saraswati.jpg' },
    { id: 'radha_krishna', name: 'राधा कृष्ण', title: 'युगल सरकार राधा-कृष्ण', img: 'assets/deity_radha_krishna.jpg' },
    { id: 'vishnu', name: 'श्री विष्णु', title: 'वैकुंठनाथ श्री हरि विष्णु', img: 'assets/deity_vishnu.jpg' },
    { id: 'gayatri', name: 'माँ गायत्री', title: 'वेदमाता माँ गायत्री', img: 'assets/deity_gayatri.jpg' },
    { id: 'khatushyam', name: 'खाटू श्याम', title: 'हारे का सहारा खाटू श्याम जी', img: 'assets/deity_khatushyam.jpg' },
    { id: 'narasimha', name: 'श्री नरसिंह', title: 'भक्तवत्सल नरसिंह भगवान', img: 'assets/deity_narasimha.jpg' },
    { id: 'sai', name: 'साईं बाबा', title: 'शिर्डी के साईं नाथ', img: 'assets/deity_sai.jpg' },
    { id: 'shanidev', name: 'शनिदेव', title: 'कर्मफल दाता सूर्यपुत्र शनिदेव', img: 'assets/deity_shanidev.jpg' },
    { id: 'shiva_parvati', name: 'शिव पार्वती', title: 'कल्याणकारी शिव-पार्वती जी', img: 'assets/shiva_parvati.jpg' },
    { id: 'surya', name: 'सूर्य देव', title: 'प्रत्यक्ष देव भगवान भास्कर', img: 'assets/deity_surya.jpg' },
    { id: 'kali', name: 'माँ काली', title: 'असुर संहारिणी माँ महाकाली', img: 'assets/deity_kali.jpg' }
  ];

  // ── Game 2: Bhakti Card Match - 30 Sacred Levels (16 Sacred Bhakti Symbols) ──
  const bhaktiSymbols = [
    { id: 'om', name: 'पावन ॐ', img: 'assets/symbols/cards/symbol_om.webp' },
    { id: 'trishul', name: 'त्रिशूल व डमरू', img: 'assets/symbols/cards/symbol_trishul.webp' },
    { id: 'bansuri', name: 'मोरपंख व बाँसुरी', img: 'assets/symbols/cards/symbol_bansuri.webp' },
    { id: 'swastik_kalash', name: 'मंगल स्वास्तिक कलश', img: 'assets/symbols/cards/symbol_swastik_kalash.webp' },
    { id: 'shrifal_kalash', name: 'श्रीफल कलश व दीप', img: 'assets/symbols/cards/symbol_shrifal_kalash.webp' },
    { id: 'diya', name: 'पावन दीपक', img: 'assets/symbols/cards/symbol_diya.webp' },
    { id: 'ghanti', name: 'मंदिर घंटी', img: 'assets/symbols/cards/symbol_ghanti.webp' },
    { id: 'rudraksha', name: 'रुद्राक्ष माला', img: 'assets/symbols/cards/symbol_rudraksha.webp' },
    { id: 'surya', name: 'भगवान सूर्य देव', img: 'assets/symbols/cards/symbol_surya.webp' },
    { id: 'dhwaja', name: 'भगवा धर्म ध्वजा', img: 'assets/symbols/cards/symbol_dhwaja.webp' },
    { id: 'grantha', name: 'पवित्र ग्रंथ', img: 'assets/symbols/cards/symbol_grantha.webp' },
    { id: 'havan', name: 'हवन कुंड', img: 'assets/symbols/cards/symbol_havan.webp' },
    { id: 'tulsi', name: 'तुलसी व बेलपत्र', img: 'assets/symbols/cards/symbol_tulsi.webp' },
    { id: 'gaumata', name: 'कामधेनु गौ माता', img: 'assets/symbols/cards/symbol_gaumata.webp' },
    { id: 'kamal', name: 'कमल पुष्प', img: 'assets/symbols/cards/symbol_kamal.webp' },
    { id: 'brahmakamal', name: 'दिव्य ब्रह्मकमल', img: 'assets/symbols/cards/symbol_brahmakamal.webp' }
  ];

  // Function to generate 30 Levels with dynamic card scaling
  function getMatchLevelConfig(lvl) {
    if (lvl <= 5)   return { pairs: 4,  cols: 4, cardW: 75, cardH: 85 }; // 8 cards (4x2)
    if (lvl <= 10)  return { pairs: 6,  cols: 4, cardW: 75, cardH: 85 }; // 12 cards (4x3)
    if (lvl <= 15)  return { pairs: 8,  cols: 4, cardW: 70, cardH: 78 }; // 16 cards (4x4)
    if (lvl <= 20)  return { pairs: 10, cols: 5, cardW: 60, cardH: 68 }; // 20 cards (5x4)
    if (lvl <= 25)  return { pairs: 12, cols: 6, cardW: 50, cardH: 60 }; // 24 cards (6x4)
    return                 { pairs: 14, cols: 7, cardW: 44, cardH: 54 }; // 28 cards (7x4) Level 26-30
  }

  let currentMatchLevel = 1;
  let savedMatchStars = JSON.parse(localStorage.getItem('match_level_stars_30') || '{}');

  let matchFlippedCards = [];
  let matchMatchedPairs = 0;
  let matchLockBoard = false;
  let matchMovesCount = 0;

  function getMatchTotalStars() {
    return Object.values(savedMatchStars).reduce((sum, s) => sum + s, 0);
  }

  function isMatchLevelUnlocked(lvl) {
    if (lvl === 1) return true;
    const requiredStars = (lvl - 1) * 3;
    return getMatchTotalStars() >= requiredStars;
  }

  function showMatchLockAlert(req) {
    const toast = document.getElementById('matchLockToast');
    const msgEl = document.getElementById('matchLockMsg');
    if (msgEl) {
      msgEl.innerText = `खोलने के लिए कम से कम ${req} ⭐ चाहिए!\n(आपके पास: ${getMatchTotalStars()} ⭐ हैं)`;
    }
    if (toast) {
      toast.style.display = 'block';
      setTimeout(() => { toast.style.display = 'none'; }, 2200);
    }
    if (typeof playSound === 'function') playSound('wrong');
  }

  function calculateMatchStarsByMoves(moves, pairs) {
    if (moves <= pairs + 2) return 5;
    if (moves <= pairs + 5) return 4;
    if (moves <= pairs + 8) return 3;
    if (moves <= pairs + 12) return 2;
    return 1;
  }

  function initMatchLevel(lvl) {
    if (!isMatchLevelUnlocked(lvl)) {
      showMatchLockAlert((lvl - 1) * 3);
      return;
    }

    currentMatchLevel = lvl;
    matchMatchedPairs = 0;
    matchMovesCount = 0;
    matchFlippedCards = [];
    matchLockBoard = false;

    const winModal = document.getElementById('matchWinModal');
    if (winModal) winModal.style.display = 'none';

    const cfg = getMatchLevelConfig(lvl);
    const titleEl = document.getElementById('match-level-title');
    if (titleEl) titleEl.innerText = `स्तर ${lvl} / 30`;
    const matchesInfoEl = document.getElementById('match-matches-info');
    if (matchesInfoEl) matchesInfoEl.innerText = `जोड़ी: 0 / ${cfg.pairs}`;
    const movesDispEl = document.getElementById('match-moves-display');
    if (movesDispEl) movesDispEl.innerText = matchMovesCount;
    const starsDispEl = document.getElementById('match-total-stars-display');
    if (starsDispEl) starsDispEl.innerText = getMatchTotalStars();

    const grid = document.getElementById('match-card-grid');
    if (!grid) return;
    grid.innerHTML = '';

    // Responsive width calculation so cards never overflow narrow screens
    const screenMaxW = Math.min(window.innerWidth * 0.92, 420);
    const gap = 8;
    const totalGaps = (cfg.cols - 1) * gap;
    const maxCardW = Math.floor((screenMaxW - totalGaps) / cfg.cols);
    const actualCardW = Math.min(cfg.cardW, maxCardW);
    const actualCardH = Math.round(actualCardW * (cfg.cardH / cfg.cardW));

    grid.style.gridTemplateColumns = `repeat(${cfg.cols}, ${actualCardW}px)`;

    // Select and shuffle cards from the 16 sacred symbols
    const shuffledSymbols = [...bhaktiSymbols].sort(() => Math.random() - 0.5);
    const chosenSymbols = shuffledSymbols.slice(0, cfg.pairs);
    const deck = [...chosenSymbols, ...chosenSymbols].sort(() => Math.random() - 0.5);

    deck.forEach(symbol => {
      const card = document.createElement('div');
      card.classList.add('card');
      card.style.width = actualCardW + 'px';
      card.style.height = actualCardH + 'px';
      card.dataset.icon = symbol.id;
      card.dataset.name = symbol.name;

      card.innerHTML = `
        <div class="card-face card-back">ॐ</div>
        <div class="card-face card-front">
          <img src="${symbol.img}" alt="${symbol.name}" class="match-card-img" draggable="false" />
        </div>
      `;

      card.addEventListener('click', onMatchCardClick);
      grid.appendChild(card);
    });
  }

  function onMatchCardClick() {
    if (matchLockBoard) return;
    if (this === matchFlippedCards[0]) return;
    if (this.classList.contains('flipped') || this.classList.contains('matched')) return;

    if (typeof playSound === 'function') playSound('swipe');
    this.classList.add('flipped');
    matchFlippedCards.push(this);

    if (matchFlippedCards.length === 2) {
      matchMovesCount++;
      const movesDisp = document.getElementById('match-moves-display');
      if (movesDisp) movesDisp.innerText = matchMovesCount;
      checkMatchPairMatch();
    }
  }

  function checkMatchPairMatch() {
    const [c1, c2] = matchFlippedCards;
    const isMatch = c1.dataset.icon === c2.dataset.icon;

    if (isMatch) {
      if (typeof playSound === 'function') playSound('correct');
      c1.classList.add('matched');
      c2.classList.add('matched');

      matchMatchedPairs++;
      const cfg = getMatchLevelConfig(currentMatchLevel);
      const matchesInfo = document.getElementById('match-matches-info');
      const matchedName = c1.dataset.name ? ` (${c1.dataset.name})` : '';
      if (matchesInfo) matchesInfo.innerText = `जोड़ी: ${matchMatchedPairs} / ${cfg.pairs}${matchedName}`;
      matchFlippedCards = [];

      if (matchMatchedPairs === cfg.pairs) {
        setTimeout(onMatchLevelWon, 600);
      }
    } else {
      if (typeof playSound === 'function') playSound('wrong');
      matchLockBoard = true;
      setTimeout(() => {
        c1.classList.remove('flipped');
        c2.classList.remove('flipped');
        matchFlippedCards = [];
        matchLockBoard = false;
      }, 850);
    }
  }

  function onMatchLevelWon() {
    if (typeof playSound === 'function') playSound('victory');
    const cfg = getMatchLevelConfig(currentMatchLevel);
    const stars = calculateMatchStarsByMoves(matchMovesCount, cfg.pairs);
    const best = savedMatchStars[currentMatchLevel] || 0;
    
    if (stars > best) {
      savedMatchStars[currentMatchLevel] = stars;
      localStorage.setItem('match_level_stars_30', JSON.stringify(savedMatchStars));
    }

    const isBoss = (currentMatchLevel % 10 === 0 || currentMatchLevel === 30);
    const coinsEarned = isBoss ? 200 : 100;
    if (typeof addCoins === 'function') addCoins(coinsEarned);

    const totalStarsEl = document.getElementById('match-total-stars-display');
    if (totalStarsEl) totalStarsEl.innerText = getMatchTotalStars();
    const starsAwardedEl = document.getElementById('match-stars-awarded');
    if (starsAwardedEl) starsAwardedEl.innerText = '⭐'.repeat(stars) + '☆'.repeat(5 - stars);
    const winMovesTextEl = document.getElementById('match-win-moves-text');
    if (winMovesTextEl) winMovesTextEl.innerText = `आपने कुल ${matchMovesCount} चालों में यह स्तर पूर्ण किया!`;
    const coinsEarnedEl = document.getElementById('match-coins-earned-text');
    if (coinsEarnedEl) coinsEarnedEl.innerText = `+${coinsEarned} सिक्के मिले! 🪙`;
    const winModal = document.getElementById('matchWinModal');
    if (winModal) winModal.style.display = 'flex';
  }

  function nextMatchLevel() {
    if (currentMatchLevel < 30) {
      initMatchLevel(currentMatchLevel + 1);
    } else {
      initMatchLevel(1);
    }
  }

  function prevMatchLevel() {
    if (currentMatchLevel > 1) {
      initMatchLevel(currentMatchLevel - 1);
    }
  }

  function restartMatchLevel() {
    initMatchLevel(currentMatchLevel);
  }

  window.initMatchLevel = initMatchLevel;
  window.nextMatchLevel = nextMatchLevel;
  window.prevMatchLevel = prevMatchLevel;
  window.restartMatchLevel = restartMatchLevel;
  window.initMatchGame = function (lvl) { initMatchLevel(lvl || 1); };

  // ── Game 3: JigSaw (Bhakti Jigsaw Puzzle - 50 Sacred Levels with Boss Levels) ──
  let currentLevel = 1;
  let totalCoins = parseInt(localStorage.getItem('bhakti_coins') || localStorage.getItem('epic_game_coins') || '0', 10);
  let levelStars = JSON.parse(localStorage.getItem('bhakti_level_stars') || '{}'); 

  let timerInterval = null;
  let secondsElapsed = 0;
  let isSolved = false;

  // Bhakti images pool - 50 spiritual visuals with local deity fallbacks
  var bgImages = [
    "assets/deity_ganesh.jpg",
    "assets/deity_krishna.jpg",
    "assets/deity_hanuman.jpg",
    "assets/deity_shiva.jpg",
    "assets/deity_durga_hd.jpg",
    "assets/deity_lakshmi.jpg",
    "assets/deity_ram.jpg",
    "assets/deity_saraswati.jpg",
    "assets/deity_radha_krishna.jpg",
    "assets/deity_vishnu.jpg",
    "assets/deity_gayatri.jpg",
    "assets/deity_khatushyam.jpg",
    "assets/deity_narasimha.jpg",
    "assets/deity_sai.jpg",
    "assets/deity_shanidev.jpg",
    "assets/shiva_parvati.jpg",
    "assets/deity_surya.jpg",
    "assets/deity_kali.jpg",
    "assets/deity_laxmi_ganesh.jpg",
    "assets/deity_ganga.jpg",
    "assets/deity_gauri.jpg",
    "assets/deity_murugan.jpg",
    "assets/deity_nataraja.jpg",
    "assets/deity_amavasya.jpg",
    "assets/deity_bhairav.jpg",
    "assets/deity_brihaspati.jpg",
    "assets/deity_chandra.jpg",
    "assets/gallery/bal_rama.jpg",
    "assets/gallery/bal_hanuman.jpg",
    "assets/gallery/bal_krishna.jpg",
    "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=600",
    "https://images.unsplash.com/photo-1609342122563-a43ac8917a3a?w=600"
  ];

  // Return total stars collected across all levels
  function getTotalStars() {
    return Object.values(levelStars).reduce((sum, s) => sum + s, 0);
  }

  // Timer functionality
  function startTimer() {
    clearInterval(timerInterval);
    secondsElapsed = 0;
    updateTimerUI();
    timerInterval = setInterval(() => {
      secondsElapsed++;
      updateTimerUI();
    }, 1000);
  }

  function stopTimer() {
    clearInterval(timerInterval);
  }

  function updateTimerUI() {
    const mins = String(Math.floor(secondsElapsed / 60)).padStart(2, '0');
    const secs = String(secondsElapsed % 60).padStart(2, '0');
    const timerEl = document.getElementById('game-timer');
    if (timerEl) timerEl.innerText = `${mins}:${secs}`;
  }

  // Calculate stars based on speed
  function calculateStars(timeSec) {
    if (timeSec <= 30) return 5;
    if (timeSec <= 60) return 4;
    if (timeSec <= 90) return 3;
    if (timeSec <= 120) return 2;
    return 1;
  }

  // Check level unlock status: Required Stars = (Level - 1) * 3
  function isLevelUnlocked(lvl) {
    if (lvl === 1) return true;
    const requiredStars = (lvl - 1) * 3;
    return getTotalStars() >= requiredStars;
  }

  function showLockAlert(reqStars) {
    const toast = document.getElementById('lockToast');
    const reqText = document.getElementById('lock-required-text');
    if (reqText) {
      reqText.innerText = `खोलने के लिए कम से कम ${reqStars} स्टार चाहिए! (वर्तमान: ${getTotalStars()} ⭐)`;
    }
    if (toast) {
      toast.style.display = 'block';
      setTimeout(() => { toast.style.display = 'none'; }, 2200);
    }
    if (typeof playSound === 'function') playSound('wrong');
  }

  // 50 Levels Grid Config
  function getLevelConfig(lvl) {
    if (lvl === 1) return { cols: 3, rows: 2, isBoss: false };
    if (lvl >= 2 && lvl <= 9) return { cols: 3, rows: 3, isBoss: false };
    if (lvl === 10) return { cols: 5, rows: 3, isBoss: true };
    if (lvl >= 11 && lvl <= 19) return { cols: 4, rows: 3, isBoss: false };
    if (lvl === 20) return { cols: 6, rows: 3, isBoss: true };
    if (lvl >= 21 && lvl <= 29) return { cols: 5, rows: 3, isBoss: false };
    if (lvl === 30) return { cols: 7, rows: 3, isBoss: true };
    if (lvl >= 31 && lvl <= 39) return { cols: 6, rows: 3, isBoss: false };
    if (lvl === 40) return { cols: 6, rows: 4, isBoss: true };
    if (lvl >= 41 && lvl <= 49) return { cols: 5, rows: 4, isBoss: false };
    return { cols: 7, rows: 4, isBoss: true }; // Level 50
  }

  // Curved Jigsaw path with organic interlocking tabs
  function createJigsawPath(w, h, top, right, bottom, left) {
    const tab = Math.min(w, h) * 0.22;
    let p = `M 0 0`;
    if (top !== 0) {
      p += ` L ${w * 0.38} 0 C ${w * 0.38} ${-top * tab}, ${w * 0.62} ${-top * tab}, ${w * 0.62} 0`;
    }
    p += ` L ${w} 0`;
    if (right !== 0) {
      p += ` L ${w} ${h * 0.38} C ${w + right * tab} ${h * 0.38}, ${w + right * tab} ${h * 0.62}, ${w} ${h * 0.62}`;
    }
    p += ` L ${w} ${h}`;
    if (bottom !== 0) {
      p += ` L ${w * 0.62} ${h} C ${w * 0.62} ${h + bottom * tab}, ${w * 0.38} ${h + bottom * tab}, ${w * 0.38} ${h}`;
    }
    p += ` L 0 ${h}`;
    if (left !== 0) {
      p += ` L 0 ${h * 0.62} C ${-left * tab} ${h * 0.62}, ${-left * tab} ${h * 0.38}, 0 ${h * 0.38}`;
    }
    p += ` Z`;
    return p;
  }

  let boardSlots = []; 
  let currentPieces = [];

  function initLevel(lvl) {
    if (!isLevelUnlocked(lvl)) {
      showLockAlert((lvl - 1) * 3);
      return;
    }

    currentLevel = lvl;
    isSolved = false;
    const winModal = document.getElementById('winModal');
    if (winModal) winModal.style.display = 'none';

    totalCoins = parseInt(localStorage.getItem('bhakti_coins') || localStorage.getItem('epic_game_coins') || '0', 10);
    levelStars = JSON.parse(localStorage.getItem('bhakti_level_stars') || '{}');

    const userCoinsEl = document.getElementById('user-coins');
    if (userCoinsEl) userCoinsEl.innerText = totalCoins;
    const totalStarsEl = document.getElementById('total-stars');
    if (totalStarsEl) totalStarsEl.innerText = getTotalStars();

    const cfg = getLevelConfig(lvl);
    const totalPiecesCount = cfg.cols * cfg.rows;

    const levelTitleEl = document.getElementById('level-title');
    if (levelTitleEl) levelTitleEl.innerText = `स्तर ${lvl} / 50`;
    const piecesCountEl = document.getElementById('pieces-count');
    if (piecesCountEl) piecesCountEl.innerText = `खण्ड: ${totalPiecesCount} (${cfg.cols}x${cfg.rows})`;
    const bossEl = document.getElementById('boss-container');
    if (bossEl) {
      bossEl.innerHTML = cfg.isBoss ? `<span class="boss-badge">🔥 BOSS LEVEL</span>` : '';
    }

    const board = document.getElementById('puzzle-board');
    if (!board) return;
    board.innerHTML = '';

    const maxW = Math.min(window.innerWidth * 0.9, 360);
    const cellW = Math.floor(maxW / cfg.cols);
    const cellH = cellW;
    const boardW = cellW * cfg.cols;
    const boardH = cellH * cfg.rows;

    board.style.width = boardW + 'px';
    board.style.height = boardH + 'px';

    const currentImgUrl = bgImages[(lvl - 1) % bgImages.length];

    // Hint / Peek image
    let guideImg = document.createElement('img');
    guideImg.id = 'puzzle-guide-image';
    guideImg.src = currentImgUrl;
    guideImg.alt = 'guide';
    guideImg.style.cssText = 'position:absolute; inset:0; width:100%; height:100%; opacity:0; pointer-events:none; z-index:2; transition:opacity 0.3s; border-radius:10px; object-fit:fill;';
    board.appendChild(guideImg);

    // Compute tabs structure
    const hTabs = Array.from({length: cfg.rows}, () => Array.from({length: cfg.cols - 1}, () => Math.random() < 0.5 ? 1 : -1));
    const vTabs = Array.from({length: cfg.rows - 1}, () => Array.from({length: cfg.cols}, () => Math.random() < 0.5 ? 1 : -1));

    boardSlots = [];
    currentPieces = [];

    // 1. Generate slots and pieces
    let index = 0;
    for (let r = 0; r < cfg.rows; r++) {
      for (let c = 0; c < cfg.cols; c++) {
        const correctX = c * cellW;
        const correctY = r * cellH;

        const top = r === 0 ? 0 : -vTabs[r - 1][c];
        const right = c === cfg.cols - 1 ? 0 : hTabs[r][c];
        const bottom = r === cfg.rows - 1 ? 0 : vTabs[r][c];
        const left = c === 0 ? 0 : -hTabs[r][c - 1];

        const path = createJigsawPath(cellW, cellH, top, right, bottom, left);
        const pad = cellW * 0.35;
        const svgW = cellW + pad * 2;
        const svgH = cellH + pad * 2;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("class", "jigsaw-piece");
        svg.setAttribute("width", svgW);
        svg.setAttribute("height", svgH);
        svg.style.width = svgW + "px";
        svg.style.height = svgH + "px";

        const clipId = `clip_${lvl}_${r}_${c}_${Date.now()}`;
        svg.innerHTML = `
          <defs>
            <clipPath id="${clipId}">
              <path d="${path}" transform="translate(${pad}, ${pad})" />
            </clipPath>
          </defs>
          <g clip-path="url(#${clipId})">
            <image href="${currentImgUrl}" x="${-correctX + pad}" y="${-correctY + pad}" width="${boardW}" height="${boardH}" preserveAspectRatio="none"/>
          </g>
          <path d="${path}" transform="translate(${pad}, ${pad})" fill="none" stroke="rgba(255,215,0,0.8)" stroke-width="1.8" />
        `;

        boardSlots.push({ id: index, x: correctX, y: correctY, pad, cellW, cellH });
        currentPieces.push({ id: index, originalSlot: index, currentSlot: index, el: svg, pad, cellW, cellH });
        board.appendChild(svg);
        index++;
      }
    }

    // 2. Scramble pieces randomly on the board
    shuffleBoardPositions();
    startTimer();
  }

  // Scramble positions on the board
  function shuffleBoardPositions() {
    let slotIndices = boardSlots.map((_, i) => i);
    // Shuffle array
    for (let i = slotIndices.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [slotIndices[i], slotIndices[j]] = [slotIndices[j], slotIndices[i]];
    }

    // Ensure pieces are genuinely scrambled and not already solved
    if (slotIndices.length > 1 && slotIndices.every((val, idx) => val === idx)) {
      [slotIndices[0], slotIndices[1]] = [slotIndices[1], slotIndices[0]];
    }

    currentPieces.forEach((piece, idx) => {
      const assignedSlot = slotIndices[idx];
      piece.currentSlot = assignedSlot;
      renderPieceAtSlot(piece, assignedSlot);
      enableSwapDrag(piece);
    });
  }

  function renderPieceAtSlot(piece, slotIndex) {
    const slot = boardSlots[slotIndex];
    if (!slot) return;
    piece.el.style.left = (slot.x - piece.pad) + 'px';
    piece.el.style.top = (slot.y - piece.pad) + 'px';
  }

  // Drag piece to swap with another piece
  function enableSwapDrag(piece) {
    let startX, startY, origLeft, origTop;
    let isDragging = false;

    function onPointerDown(e) {
      if (isSolved || isDragging) return;
      isDragging = true;
      const evt = e.touches ? e.touches[0] : e;
      startX = evt.clientX;
      startY = evt.clientY;
      origLeft = parseFloat(piece.el.style.left) || 0;
      origTop = parseFloat(piece.el.style.top) || 0;

      piece.el.classList.add('dragging');

      window.addEventListener('pointermove', onPointerMove, { passive: false });
      window.addEventListener('pointerup', onPointerUp);
      window.addEventListener('touchmove', onPointerMove, { passive: false });
      window.addEventListener('touchend', onPointerUp);
    }

    function onPointerMove(e) {
      if (!isDragging) return;
      if (e.cancelable) e.preventDefault();
      const evt = e.touches ? e.touches[0] : e;
      const dx = evt.clientX - startX;
      const dy = evt.clientY - startY;
      piece.el.style.left = (origLeft + dx) + 'px';
      piece.el.style.top = (origTop + dy) + 'px';
    }

    function onPointerUp(e) {
      if (!isDragging) return;
      isDragging = false;

      window.removeEventListener('pointermove', onPointerMove);
      window.removeEventListener('pointerup', onPointerUp);
      window.removeEventListener('touchmove', onPointerMove);
      window.removeEventListener('touchend', onPointerUp);

      piece.el.classList.remove('dragging');

      // Check which slot center is closest to dropped position
      const currentCenterX = parseFloat(piece.el.style.left) + piece.pad + (piece.cellW / 2);
      const currentCenterY = parseFloat(piece.el.style.top) + piece.pad + (piece.cellH / 2);

      let closestSlotIdx = piece.currentSlot;
      let minDist = 999999;

      boardSlots.forEach((slot, sIdx) => {
        const slotCenterX = slot.x + (slot.cellW / 2);
        const slotCenterY = slot.y + (slot.cellH / 2);
        const dist = Math.hypot(currentCenterX - slotCenterX, currentCenterY - slotCenterY);
        if (dist < minDist) {
          minDist = dist;
          closestSlotIdx = sIdx;
        }
      });

      // Swap if dropped on a different slot
      if (closestSlotIdx !== piece.currentSlot) {
        const targetPiece = currentPieces.find(p => p.currentSlot === closestSlotIdx);
        if (targetPiece) {
          const oldSlot = piece.currentSlot;
          targetPiece.currentSlot = oldSlot;
          renderPieceAtSlot(targetPiece, oldSlot);
          if (typeof playSound === 'function') playSound('swipe');
        }
        piece.currentSlot = closestSlotIdx;
      }

      renderPieceAtSlot(piece, piece.currentSlot);
      checkBoardSolved();
    }

    piece.el.onpointerdown = onPointerDown;
    piece.el.ontouchstart = onPointerDown;
  }

  // Verify if every piece is in its correct original slot
  function checkBoardSolved() {
    const allCorrect = currentPieces.every(p => p.currentSlot === p.originalSlot);
    if (allCorrect) {
      isSolved = true;
      stopTimer();

      if (typeof playSound === 'function') playSound('victory');

      const starsEarned = calculateStars(secondsElapsed);
      const prevBestStars = levelStars[currentLevel] || 0;
      if (starsEarned > prevBestStars) {
        levelStars[currentLevel] = starsEarned;
        localStorage.setItem('bhakti_level_stars', JSON.stringify(levelStars));
      }

      const cfg = getLevelConfig(currentLevel);
      const rewardCoins = cfg.isBoss ? 250 : 100;
      totalCoins += rewardCoins;
      localStorage.setItem('bhakti_coins', totalCoins.toString());
      localStorage.setItem('epic_game_coins', totalCoins.toString());
      if (typeof addCoins === 'function') {
        try { epicGameState.coins = totalCoins; } catch (e) {}
      }

      const userCoinsEl = document.getElementById('user-coins');
      if (userCoinsEl) userCoinsEl.innerText = totalCoins;
      const totalStarsEl = document.getElementById('total-stars');
      if (totalStarsEl) totalStarsEl.innerText = getTotalStars();

      // Show Modal
      const starsAwardedEl = document.getElementById('stars-awarded');
      if (starsAwardedEl) starsAwardedEl.innerText = '⭐'.repeat(starsEarned) + '☆'.repeat(5 - starsEarned);
      const winHeadingEl = document.getElementById('win-heading');
      if (winHeadingEl) {
        winHeadingEl.innerText = cfg.isBoss ? "बॉस स्तर पराजित! 🔱" : "दर्शन सफल हुआ! 🌸";
      }
      const winDescEl = document.getElementById('win-desc');
      if (winDescEl) winDescEl.innerText = `समय: ${secondsElapsed} सेकंड में पूरा किया!`;
      const coinsEarnedEl = document.getElementById('coins-earned-text');
      if (coinsEarnedEl) coinsEarnedEl.innerText = `+${rewardCoins} सिक्के प्राप्त हुए! 🪙`;
      const winModal = document.getElementById('winModal');
      if (winModal) winModal.style.display = 'flex';
    }
  }

  function goToNextLevel() {
    if (currentLevel < 50) {
      initLevel(currentLevel + 1);
    } else {
      initLevel(1);
    }
  }

  function goToPrevLevel() {
    if (currentLevel > 1) {
      initLevel(currentLevel - 1);
    } else {
      initLevel(50);
    }
  }

  function resetCurrentLevel() {
    initLevel(currentLevel);
  }

  var peekTimer = null;
  function togglePeek() {
    var guideImg = document.getElementById('puzzle-guide-image');
    if (!guideImg) return;
    if (guideImg.style.opacity === '0.85') {
      guideImg.style.opacity = '0';
      if (peekTimer) clearTimeout(peekTimer);
    } else {
      guideImg.style.opacity = '0.85';
      if (typeof showToast === 'function') showToast('👁️ दिव्य दर्शन: संकेत 3 सेकंड सक्रिय');
      if (peekTimer) clearTimeout(peekTimer);
      peekTimer = setTimeout(function() {
        if (guideImg) guideImg.style.opacity = '0';
      }, 3000);
    }
  }

  // ══════════════════════════════════════════════════════════════════════════════
  // 🔤 GAME 4: PADABANDHAM (वैदिक शब्द संधान) 5 SACRED LEVELS ENGINE
  // ══════════════════════════════════════════════════════════════════════════════
  var PADA_LEVELS = [
    {
      level: 1,
      title: "स्तर १: प्रमुख देव",
      words: [
        { word: 'राम', chars: ['रा', 'म'], deity: 'श्री राम', img: 'assets/deity_ram.jpg' },
        { word: 'कृष्ण', chars: ['कृ', 'ष्ण'], deity: 'श्री कृष्ण', img: 'assets/deity_krishna.jpg' },
        { word: 'शिव', chars: ['शि', 'व'], deity: 'महादेव शिव', img: 'assets/deity_shiva.jpg' },
        { word: 'गणेश', chars: ['ग', 'णे', 'श'], deity: 'श्री गणेश', img: 'assets/deity_ganesh.jpg' },
        { word: 'हनुमान', chars: ['ह', 'नु', 'मा', 'न'], deity: 'श्री हनुमान', img: 'assets/deity_hanuman.jpg' },
        { word: 'दुर्गा', chars: ['दु', 'र्गा'], deity: 'माँ दुर्गा', img: 'assets/deity_durga_hd.jpg' },
        { word: 'ॐ', chars: ['ॐ'], deity: 'प्रणव ॐ', img: 'assets/symbols/cards/symbol_om.webp' }
      ],
      // 16 letters in 4x4 grid (exact layout matching user device screenshot)
      grid: [
        'रा', 'म', 'कृ', 'ष्ण',
        'शि', 'व', 'ग', 'णे',
        'श', 'ह', 'नु', 'मा',
        'न', 'दु', 'र्गा', 'ॐ'
      ]
    },
    {
      level: 2,
      title: "स्तर २: पावन धाम",
      words: [
        { word: 'अयोध्या', chars: ['अ', 'यो', 'ध्या'], deity: 'राम लला', img: 'assets/deity_ram.jpg' },
        { word: 'काशी', chars: ['का', 'शी'], deity: 'विश्वनाथ', img: 'assets/deity_shiva.jpg' },
        { word: 'मथुरा', chars: ['म', 'थु', 'रा'], deity: 'गोपाल', img: 'assets/deity_krishna.jpg' },
        { word: 'केदार', chars: ['के', 'दा', 'र'], deity: 'केदारनाथ', img: 'assets/deity_shiva.jpg' },
        { word: 'बद्री', chars: ['ब', 'द्री'], deity: 'बद्रीनाथ', img: 'assets/deity_vishnu.jpg' },
        { word: 'प्रयाग', chars: ['प्र', 'या', 'ग'], deity: 'त्रिवेणी', img: 'assets/symbols/cards/symbol_ganga.webp' }
      ],
      grid: [
        'अ', 'यो', 'ध्या', 'का',
        'शी', 'म', 'थु', 'रा',
        'के', 'दा', 'र', 'ब',
        'द्री', 'प्र', 'या', 'ग'
      ]
    },
    {
      level: 3,
      title: "स्तर ३: दिव्य अवतार",
      words: [
        { word: 'नरसिंह', chars: ['न', 'र', 'सिं', 'ह'], deity: 'प्रह्लाद रक्षक', img: 'assets/deity_vishnu.jpg' },
        { word: 'वामन', chars: ['वा', 'म', 'न'], deity: 'त्रिविक्रम', img: 'assets/deity_vishnu.jpg' },
        { word: 'वराह', chars: ['व', 'रा', 'ह'], deity: 'धरणीधर', img: 'assets/deity_vishnu.jpg' },
        { word: 'परशुराम', chars: ['प', 'र', 'शु', 'रा', 'म'], deity: 'भार्गव', img: 'assets/deity_vishnu.jpg' }
      ],
      grid: [
        'न', 'र', 'सिं', 'ह',
        'वा', 'म', 'न', 'व',
        'रा', 'ह', 'प', 'र',
        'शु', 'रा', 'म', 'ॐ'
      ]
    },
    {
      level: 4,
      title: "स्तर ४: पवित्र प्रतीक",
      words: [
        { word: 'त्रिशूल', chars: ['त्रि', 'शू', 'ल'], deity: 'शिव अस्त्र', img: 'assets/symbols/cards/symbol_trishul.webp' },
        { word: 'डमरू', chars: ['ड', 'म', 'रू'], deity: 'नाद ब्रह्म', img: 'assets/symbols/cards/symbol_damru.webp' },
        { word: 'शंख', chars: ['शं', 'ख'], deity: 'पाञ्चजन्य', img: 'assets/symbols/cards/symbol_shankh.webp' },
        { word: 'चक्र', chars: ['च', 'क्र'], deity: 'सुदर्शन', img: 'assets/symbols/cards/symbol_chakra.webp' },
        { word: 'गदा', chars: ['ग', 'दा'], deity: 'कौमोदकी', img: 'assets/symbols/cards/symbol_gadda.webp' },
        { word: 'पद्म', chars: ['प', 'द्म'], deity: 'कमल दल', img: 'assets/symbols/cards/symbol_lotus.webp' }
      ],
      grid: [
        'त्रि', 'शू', 'ल', 'ड',
        'म', 'रू', 'शं', 'ख',
        'च', 'क्र', 'ग', 'दा',
        'प', 'द्म', 'श्री', 'ॐ'
      ]
    },
    {
      level: 5,
      title: "स्तर ५: पावन तीर्थ",
      words: [
        { word: 'हरिद्वार', chars: ['ह', 'रि', 'द्वा', 'र'], deity: 'गंगा द्वार', img: 'assets/symbols/cards/symbol_ganga.webp' },
        { word: 'उज्जैन', chars: ['उ', 'ज्जै', 'न'], deity: 'महाकाल', img: 'assets/deity_shiva.jpg' },
        { word: 'गोकुल', chars: ['गो', 'कु', 'ल'], deity: 'नंदग्राम', img: 'assets/deity_krishna.jpg' },
        { word: 'द्वारका', chars: ['द्वा', 'र', 'का'], deity: 'द्वारकाधीश', img: 'assets/deity_krishna.jpg' },
        { word: 'ऋषिकेश', chars: ['ऋ', 'षि', 'के', 'श'], deity: 'तपोभूमि', img: 'assets/deity_shiva.jpg' }
      ],
      grid: [
        'ह', 'रि', 'द्वा', 'र',
        'उ', 'ज्जै', 'न', 'गो',
        'कु', 'ल', 'द्वा', 'र',
        'का', 'ऋ', 'षि', 'केश'
      ]
    }
  ];

  var currentPadaLevelIdx = 0;
  var foundWords = [];
  var currentSelectedCells = [];
  var solvedCellIndices = [];
  var padaTimerInterval = null;
  var padaTimerSeconds = 0;
  var padaHintsRemaining = 3;

  function startPadaTimer() {
    stopPadaTimer();
    padaTimerSeconds = 0;
    updatePadaTimerDisplay();
    padaTimerInterval = setInterval(function () {
      padaTimerSeconds++;
      updatePadaTimerDisplay();
    }, 1000);
  }

  function stopPadaTimer() {
    if (padaTimerInterval) {
      clearInterval(padaTimerInterval);
      padaTimerInterval = null;
    }
  }

  function updatePadaTimerDisplay() {
    var timerEl = document.getElementById('pada-timer');
    if (!timerEl) return;
    var mins = Math.floor(padaTimerSeconds / 60);
    var secs = padaTimerSeconds % 60;
    var mm = mins < 10 ? '0' + mins : '' + mins;
    var ss = secs < 10 ? '0' + secs : '' + secs;
    timerEl.textContent = '⏱️ ' + mm + ':' + ss;
  }

  function initPadabandhamGame(lvlIdx) {
    if (typeof lvlIdx === 'number' && lvlIdx >= 0 && lvlIdx < PADA_LEVELS.length) {
      currentPadaLevelIdx = lvlIdx;
    }
    foundWords = [];
    currentSelectedCells = [];
    solvedCellIndices = [];
    padaHintsRemaining = 3;

    var curLvl = PADA_LEVELS[currentPadaLevelIdx];
    var titleEl = document.getElementById('pada-level-name');
    if (titleEl) titleEl.textContent = curLvl.title;

    var hintTextEl = document.getElementById('pada-hint-text');
    if (hintTextEl) hintTextEl.textContent = 'संकेत (Hint: ' + padaHintsRemaining + ')';

    var statusEl = document.getElementById('padabandham-status');
    if (statusEl) statusEl.textContent = 'अक्षरों को क्रम में स्पर्श करें...';

    renderPadabandham();
    startPadaTimer();
  }

  function renderPadabandham() {
    var curLvl = PADA_LEVELS[currentPadaLevelIdx];

    // 1. Level Name without Truncation
    var titleEl = document.getElementById('pada-level-name');
    if (titleEl) titleEl.textContent = curLvl.title;

    // 2. Score Counter
    var scoreEl = document.getElementById('pada-score-counter');
    if (scoreEl) {
      scoreEl.textContent = '🌸 ' + foundWords.length + '/' + curLvl.words.length;
    }

    // 3. Targets Tray
    var targetsEl = document.getElementById('padabandham-word-targets') || document.getElementById('padabandham-word-list');
    if (targetsEl) {
      targetsEl.innerHTML = curLvl.words.map(function (item) {
        var isFound = foundWords.includes(item.word);
        return `<span class="pada-word-badge ${isFound ? 'is-found' : ''}"><img src="${item.img}" class="pada-badge-avatar" onerror="this.src='assets/symbols/cards/symbol_om.webp';"> ${item.word} ${isFound ? '✓' : ''}</span>`;
      }).join(' ');
    }

    // 4. Grid Cells
    var gridEl = document.getElementById('padabandham-grid');
    if (gridEl) {
      gridEl.innerHTML = '';
      curLvl.grid.forEach(function (char, idx) {
        var cell = document.createElement('div');
        var isSel = currentSelectedCells.includes(idx);
        var isSolved = solvedCellIndices.includes(idx);
        cell.className = 'pada-cell' + (isSel ? ' is-selected' : '') + (isSolved ? ' is-solved' : '');
        cell.setAttribute('data-idx', idx);
        cell.textContent = char;
        cell.onclick = function () { handlePadabandhamTap(idx); };
        gridEl.appendChild(cell);
      });
    }
  }

  function handlePadabandhamTap(idx) {
    var curLvl = PADA_LEVELS[currentPadaLevelIdx];

    // Remove any active hint pulse on click
    document.querySelectorAll('.pada-cell.has-hint').forEach(function (el) {
      el.classList.remove('has-hint');
    });

    if (currentSelectedCells.includes(idx)) {
      // Toggle off if tapping an already selected cell
      currentSelectedCells = currentSelectedCells.filter(function (i) { return i !== idx; });
    } else {
      currentSelectedCells.push(idx);
    }

    var formedStr = currentSelectedCells.map(function (i) { return curLvl.grid[i]; }).join('');
    var statusEl = document.getElementById('padabandham-status');

    if (currentSelectedCells.length === 0) {
      if (statusEl) statusEl.textContent = 'अक्षरों को क्रम में स्पर्श करें...';
    } else {
      if (statusEl) {
        statusEl.innerHTML = 'चयनित: <span class="pada-selected-tile">' + formedStr + '</span>';
      }
    }

    // Check if formed string matches any unsolved word
    var matched = curLvl.words.find(function (w) {
      return (w.chars.join('') === formedStr || w.word === formedStr);
    });

    if (matched && !foundWords.includes(matched.word)) {
      foundWords.push(matched.word);
      // Mark selected cells as solved
      currentSelectedCells.forEach(function (i) {
        if (!solvedCellIndices.includes(i)) solvedCellIndices.push(i);
      });
      currentSelectedCells = [];

      if (typeof playSound === 'function') playSound('correct');
      if (statusEl) statusEl.textContent = '🎉 अद्भुत! खोजा: ' + matched.word + ' (' + matched.deity + ')';
      renderPadabandham();

      // Check Level Victory Condition
      if (foundWords.length === curLvl.words.length) {
        stopPadaTimer();
        setTimeout(function () {
          if (typeof playSound === 'function') playSound('victory');
          if (typeof addCoins === 'function') addCoins(150);
          showPadabandhamWinDialog();
        }, 400);
      }
    } else {
      renderPadabandham();
      if (currentSelectedCells.length > 0 && statusEl) {
        statusEl.innerHTML = 'चयनित: <span class="pada-selected-tile">' + formedStr + '</span>';
      }
    }
  }

  function backspacePadabandham() {
    if (currentSelectedCells.length > 0) {
      currentSelectedCells.pop();
      var curLvl = PADA_LEVELS[currentPadaLevelIdx];
      var formedStr = currentSelectedCells.map(function (i) { return curLvl.grid[i]; }).join('');
      var statusEl = document.getElementById('padabandham-status');
      if (currentSelectedCells.length === 0) {
        if (statusEl) statusEl.textContent = 'अक्षरों को क्रम में स्पर्श करें...';
      } else {
        if (statusEl) {
          statusEl.innerHTML = 'चयनित: <span class="pada-selected-tile">' + formedStr + '</span>';
        }
      }
      renderPadabandham();
    }
  }

  function clearPadabandhamSelection() {
    currentSelectedCells = [];
    var statusEl = document.getElementById('padabandham-status');
    if (statusEl) statusEl.textContent = 'अक्षरों को क्रम में स्पर्श करें...';
    renderPadabandham();
  }

  function usePadabandhamHint() {
    if (padaHintsRemaining <= 0) {
      if (typeof showToast === 'function') showToast('💡 इस स्तर के सभी संकेत उपयोग हो चुके हैं!');
      return;
    }

    var curLvl = PADA_LEVELS[currentPadaLevelIdx];
    var firstUnfound = curLvl.words.find(function (w) { return !foundWords.includes(w.word); });
    if (!firstUnfound) return;

    var firstChar = firstUnfound.chars[0];
    var targetIdx = curLvl.grid.indexOf(firstChar);

    if (targetIdx !== -1) {
      var gridEl = document.getElementById('padabandham-grid');
      if (gridEl && gridEl.children[targetIdx]) {
        gridEl.children[targetIdx].classList.add('has-hint');
        padaHintsRemaining--;
        var hintTextEl = document.getElementById('pada-hint-text');
        if (hintTextEl) hintTextEl.textContent = 'संकेत (Hint: ' + padaHintsRemaining + ')';
        if (typeof showToast === 'function') {
          showToast('💡 संकेत: "' + firstUnfound.word + '" का प्रथम अक्षर "' + firstChar + '" चमक रहा है!');
        }
      }
    }
  }

  function nextPadabandhamLevel() {
    var winDlg = document.getElementById('pada-level-win-dialog');
    if (winDlg) winDlg.style.display = 'none';

    if (currentPadaLevelIdx < PADA_LEVELS.length - 1) {
      initPadabandhamGame(currentPadaLevelIdx + 1);
    } else {
      if (typeof showToast === 'function') showToast('🏆 बधाई! आपने सभी ५ पावन स्तर पूर्ण कर लिए हैं!');
      initPadabandhamGame(0);
    }
  }

  function prevPadabandhamLevel() {
    if (currentPadaLevelIdx > 0) {
      initPadabandhamGame(currentPadaLevelIdx - 1);
    } else {
      initPadabandhamGame(PADA_LEVELS.length - 1);
    }
  }

  function replayCurrentPadabandhamLevel() {
    var winDlg = document.getElementById('pada-level-win-dialog');
    if (winDlg) winDlg.style.display = 'none';
    initPadabandhamGame(currentPadaLevelIdx);
  }

  function showPadabandhamWinDialog() {
    var curLvl = PADA_LEVELS[currentPadaLevelIdx];
    var winDlg = document.getElementById('pada-level-win-dialog');
    var winMsg = document.getElementById('pada-win-message');
    if (winMsg) {
      winMsg.textContent = 'आपने ' + curLvl.title + ' के सभी ' + curLvl.words.length + ' पावन नाम खोज लिए हैं!';
    }
    if (winDlg) {
      winDlg.style.display = 'flex';
      winDlg.classList.add('active');
    }
  }

  // Hook global functions to window
  window.initPadabandhamGame = initPadabandhamGame;
  window.nextPadabandhamLevel = nextPadabandhamLevel;
  window.prevPadabandhamLevel = prevPadabandhamLevel;
  window.replayCurrentPadabandhamLevel = replayCurrentPadabandhamLevel;
  window.backspacePadabandham = backspacePadabandham;
  window.clearPadabandhamSelection = clearPadabandhamSelection;
  window.usePadabandhamHint = usePadabandhamHint;
  window.handlePadabandhamTap = handlePadabandhamTap;

  window.openPadabandhamGame = function () {
    var modal = document.getElementById('padabandham-game-modal');
    if (modal) {
      modal.classList.add('active');
      modal.classList.add('is-open');
      modal.style.setProperty('display', 'flex', 'important');
      modal.style.setProperty('opacity', '1', 'important');
      modal.style.setProperty('pointer-events', 'auto', 'important');
      modal.style.setProperty('visibility', 'visible', 'important');
    }
    document.body.classList.add('game-modal-open');
    var appHeader = document.querySelector('.app-header');
    if (appHeader) appHeader.style.setProperty('display', 'none', 'important');
    hideBottomNavForGames();
    initPadabandhamGame(0);
  };

  window.closePadabandhamGame = function () {
    stopPadaTimer();
    var modal = document.getElementById('padabandham-game-modal');
    if (modal) {
      modal.classList.remove('active');
      modal.classList.remove('is-open');
      modal.style.setProperty('display', 'none', 'important');
      modal.style.setProperty('opacity', '0', 'important');
      modal.style.setProperty('pointer-events', 'none', 'important');
    }
    var winDlg = document.getElementById('pada-level-win-dialog');
    if (winDlg) winDlg.style.display = 'none';

    document.body.classList.remove('game-modal-open');
    var appHeader = document.querySelector('.app-header');
    if (appHeader) appHeader.style.removeProperty('display');
    restoreBottomNavIfExited();
  };


  // ══════════════════════════════════════════════════════════════════════════════
  // 6. GLOBAL NAVIGATION & EXPOSURE TO WINDOW
  // ══════════════════════════════════════════════════════════════════════════════
  window.openSwipeGame = function (categoryKey) {
    window.openSwipeLauncher(categoryKey);
  };

  window.closeSwipeGame = function () {
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'none';
    var launcher = document.getElementById('swipe-launcher-screen');
    if (launcher) {
      launcher.style.display = 'none';
      launcher.classList.remove('active');
    }
    restoreBottomNavIfExited();
  };

  window.closeSwipeReview = function () {
    var rev = document.getElementById('swipe-review-arena');
    if (rev) rev.style.display = 'none';
    showSwipeResultModal();
  };

  window.openMatchGame = function (lvlIdx) {
    if (typeof lvlIdx === 'number' && lvlIdx >= 1) {
      startMatchGameAtLevel(lvlIdx);
    } else {
      openMatchLevelHub();
    }
  };

  window.closeMatchGame = function () {
    var modal = document.getElementById('match-game-modal');
    if (modal) {
      modal.classList.remove('active');
      modal.classList.remove('is-open');
      modal.style.setProperty('display', 'none', 'important');
      modal.style.setProperty('opacity', '0', 'important');
      modal.style.setProperty('pointer-events', 'none', 'important');
    }
    var winModal = document.getElementById('matchWinModal');
    if (winModal) winModal.style.display = 'none';
    var lockToast = document.getElementById('matchLockToast');
    if (lockToast) lockToast.style.display = 'none';
    restoreBottomNavIfExited();
  };

  window.openJigsawGame = function (levelIdx) {
    var modal = document.getElementById('jigsaw-game-modal');
    if (modal) {
      modal.classList.add('active');
      modal.classList.add('is-open');
      modal.style.setProperty('display', 'flex', 'important');
      modal.style.setProperty('opacity', '1', 'important');
      modal.style.setProperty('pointer-events', 'auto', 'important');
      modal.style.setProperty('visibility', 'visible', 'important');
    }
    hideBottomNavForGames();
    var lvl = (typeof levelIdx === 'number' && levelIdx >= 1) ? levelIdx : (currentLevel || 1);
    initLevel(lvl);
  };

  window.closeJigsawGame = function () {
    stopTimer();
    var modal = document.getElementById('jigsaw-game-modal');
    if (modal) {
      modal.classList.remove('active');
      modal.classList.remove('is-open');
      modal.style.setProperty('display', 'none', 'important');
      modal.style.setProperty('opacity', '0', 'important');
      modal.style.setProperty('pointer-events', 'none', 'important');
    }
    var winModal = document.getElementById('winModal');
    if (winModal) winModal.style.display = 'none';
    var lockToast = document.getElementById('lockToast');
    if (lockToast) lockToast.style.display = 'none';
    var peekModal = document.getElementById('jigsaw-peek-modal');
    if (peekModal) peekModal.style.display = 'none';
    restoreBottomNavIfExited();
  };

  window.initLevel = initLevel;
  window.goToNextLevel = goToNextLevel;
  window.nextLevel = goToNextLevel;
  window.skipToNextLevel = goToNextLevel;
  window.goToPrevLevel = goToPrevLevel;
  window.prevLevel = goToPrevLevel;
  window.resetCurrentLevel = resetCurrentLevel;
  window.togglePeek = togglePeek;
  window.toggleJigsawPreviewModal = togglePeek;
  window.isLevelUnlocked = isLevelUnlocked;
  window.getTotalStars = getTotalStars;
  window.calculateStars = calculateStars;
  window.showLockAlert = showLockAlert;



    window.swipeCardManual = function (direction) {
    handleSwipeCommit(direction);
  };

  window.retrySwipeRound = function () {
    hideSwipeResultModal();
    var rev = document.getElementById('swipe-review-arena');
    if (rev) rev.style.display = 'none';
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'flex';
    initSwipeGame(epicGameState.currentCategory);
  };

  window.newSwipeGame = function () {
    hideSwipeResultModal();
    // Switch between Ayodhya/Mithila and Pandav/Kaurav
    var nextCat = epicGameState.currentCategory === 'ayodhya_mithila' ? 'pandav_kaurav' : 'ayodhya_mithila';
    var rev = document.getElementById('swipe-review-arena');
    if (rev) rev.style.display = 'none';
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'flex';
    initSwipeGame(nextCat);
  };

  window.openCharacterNetworkModal = function (charId) {
    alert(`📜 महाकाव्य वंशावली: ${charId}\n\nसूर्यवंश व जनक वंश के पवित्र सम्बन्धों का दिव्य आरेख।`);
  };

  // Initialize coins on load
  document.addEventListener('DOMContentLoaded', loadCoins);
  setTimeout(loadCoins, 100);

  // ── UNLOCKED PRODUCTION STATE (No Locks!) ──

  // ══════════════════════════════════════════════════════════════════════════════
  // 🌸 GAME 5: PHOOL ARPAN (Flower & Prasad Offering Game)
  // ══════════════════════════════════════════════════════════════════════════════
  var arpanState = {
    canvas: null,
    ctx: null,
    container: null,
    scoreDisplay: null,
    livesDisplay: null,
    gameOverModal: null,
    finalScore: null,
    earnedCoins: null,
    width: 0,
    height: 0,
    score: 0,
    lives: 3,
    isGameOver: false,
    animFrameId: null,
    basket: {
      width: 85,
      height: 26,
      x: 100,
      y: 300,
      speed: 8
    },
    items: [],
    particles: [],
    floatTexts: [],
    itemTypes: [
      { char: "🌸", name: "कमल", type: "good", points: 10 },
      { char: "🌺", name: "गुड़हल", type: "good", points: 10 },
      { char: "🥥", name: "श्रीफल", type: "good", points: 20 },
      { char: "🪔", name: "दीपक", type: "good", points: 15 },
      { char: "🍃", name: "तुलसी", type: "good", points: 15 },
      { char: "🪨", name: "कंकड़", type: "bad", points: 0 }
    ],
    spawnInterval: 55,
    frameCount: 0,
    initialized: false
  };

  function moveArpanBasket(clientX) {
    if (!arpanState.canvas || arpanState.isGameOver) return;
    var rect = arpanState.canvas.getBoundingClientRect();
    var touchX = clientX - rect.left;
    arpanState.basket.x = touchX - arpanState.basket.width / 2;

    if (arpanState.basket.x < 0) arpanState.basket.x = 0;
    if (arpanState.basket.x + arpanState.basket.width > arpanState.width) {
      arpanState.basket.x = arpanState.width - arpanState.basket.width;
    }
  }

  function resizeArpanCanvas() {
    if (!arpanState.container || !arpanState.canvas) return;
    arpanState.width = arpanState.container.clientWidth;
    arpanState.height = arpanState.container.clientHeight;
    arpanState.canvas.width = arpanState.width;
    arpanState.canvas.height = arpanState.height;
    arpanState.basket.width = Math.max(76, Math.min(100, arpanState.width * 0.22));
    arpanState.basket.y = arpanState.height - 75;
  }

  function spawnArpanItem() {
    var randomItem = arpanState.itemTypes[Math.floor(Math.random() * arpanState.itemTypes.length)];
    var xPos = Math.random() * (arpanState.width - 50) + 25;
    var speedBonus = Math.min(3.5, arpanState.score / 250);
    arpanState.items.push({
      x: xPos,
      y: -25,
      char: randomItem.char,
      type: randomItem.type,
      points: randomItem.points,
      speed: Math.random() * 2 + 3 + speedBonus,
      rot: Math.random() * Math.PI,
      rotSpeed: (Math.random() - 0.5) * 0.05
    });
  }

  function addArpanParticles(x, y, count, color) {
    for (var i = 0; i < count; i++) {
      arpanState.particles.push({
        x: x,
        y: y,
        vx: (Math.random() - 0.5) * 5,
        vy: (Math.random() - 0.5) * 5 - 2,
        life: 1.0,
        decay: Math.random() * 0.04 + 0.03,
        size: Math.random() * 4 + 2,
        color: color || '#FFD700'
      });
    }
  }

  function addArpanFloatText(x, y, text, color) {
    arpanState.floatTexts.push({
      x: x,
      y: y,
      text: text,
      color: color || '#8B0000',
      life: 1.0,
      vy: -1.5
    });
  }

  function updateArpan() {
    if (arpanState.isGameOver) return;

    arpanState.frameCount++;
    var interval = Math.max(32, arpanState.spawnInterval - Math.floor(arpanState.score / 150) * 3);
    if (arpanState.frameCount % interval === 0) {
      spawnArpanItem();
    }

    var b = arpanState.basket;

    for (var i = arpanState.items.length - 1; i >= 0; i--) {
      var item = arpanState.items[i];
      item.y += item.speed;
      item.rot += item.rotSpeed;

      // Collision Detection with Thali
      if (
        item.y + 16 >= b.y &&
        item.y - 16 <= b.y + b.height &&
        item.x >= b.x - 10 &&
        item.x <= b.x + b.width + 10
      ) {
        if (item.type === "good") {
          arpanState.score += item.points;
          if (arpanState.scoreDisplay) arpanState.scoreDisplay.innerText = "Prasad: " + arpanState.score;
          playSound('correct');
          addArpanParticles(item.x, item.y, 8, '#FFD700');
          addArpanFloatText(item.x, item.y, "+" + item.points, "#8B0000");
        } else {
          arpanState.lives--;
          playSound('wrong');
          if (navigator.vibrate) navigator.vibrate([60, 40, 60]);
          addArpanParticles(item.x, item.y, 10, '#64748B');
          addArpanFloatText(item.x, item.y, "💔 -1", "#DC2626");
          updateArpanLivesUI();
        }
        arpanState.items.splice(i, 1);
        continue;
      }

      // Missed item falling off bottom
      if (item.y > arpanState.height) {
        if (item.type === "good") {
          arpanState.lives--;
          playSound('wrong');
          addArpanFloatText(item.x, arpanState.height - 30, "चूका! -1", "#DC2626");
          updateArpanLivesUI();
        }
        arpanState.items.splice(i, 1);
      }
    }

    // Update Particles
    for (var pIdx = arpanState.particles.length - 1; pIdx >= 0; pIdx--) {
      var p = arpanState.particles[pIdx];
      p.x += p.vx;
      p.y += p.vy;
      p.life -= p.decay;
      if (p.life <= 0) arpanState.particles.splice(pIdx, 1);
    }

    // Update Float Texts
    for (var fIdx = arpanState.floatTexts.length - 1; fIdx >= 0; fIdx--) {
      var ft = arpanState.floatTexts[fIdx];
      ft.y += ft.vy;
      ft.life -= 0.025;
      if (ft.life <= 0) arpanState.floatTexts.splice(fIdx, 1);
    }
  }

  function updateArpanLivesUI() {
    var hearts = "";
    for (var i = 0; i < arpanState.lives; i++) hearts += "❤️";
    if (arpanState.livesDisplay) arpanState.livesDisplay.innerText = "Lives: " + (hearts || "💔");

    if (arpanState.lives <= 0) {
      arpanState.isGameOver = true;
      playSound('victory');
      var earnedCoins = Math.max(10, Math.floor(arpanState.score * 0.75));
      addCoins(earnedCoins);
      if (arpanState.finalScore) arpanState.finalScore.innerText = arpanState.score;
      if (arpanState.earnedCoins) arpanState.earnedCoins.innerText = "+" + earnedCoins + " 🪙";
      if (arpanState.gameOverModal) arpanState.gameOverModal.style.display = "flex";
    }
  }

  function drawArpan() {
    var ctx = arpanState.ctx;
    var w = arpanState.width;
    var h = arpanState.height;
    if (!ctx) return;

    ctx.clearRect(0, 0, w, h);

    // Subtle background temple ray glow
    var glow = ctx.createRadialGradient(w / 2, 80, 20, w / 2, 80, w * 0.8);
    glow.addColorStop(0, 'rgba(255, 255, 255, 0.45)');
    glow.addColorStop(0.5, 'rgba(255, 230, 150, 0.2)');
    glow.addColorStop(1, 'rgba(255, 255, 255, 0)');
    ctx.fillStyle = glow;
    ctx.fillRect(0, 0, w, h);

    // Draw Falling Items
    ctx.font = "28px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    for (var i = 0; i < arpanState.items.length; i++) {
      var it = arpanState.items[i];
      ctx.save();
      ctx.translate(it.x, it.y);
      ctx.rotate(it.rot);
      ctx.fillText(it.char, 0, 0);
      ctx.restore();
    }

    // Draw Particles
    for (var pi = 0; pi < arpanState.particles.length; pi++) {
      var pt = arpanState.particles[pi];
      ctx.fillStyle = pt.color;
      ctx.globalAlpha = Math.max(0, pt.life);
      ctx.beginPath();
      ctx.arc(pt.x, pt.y, pt.size, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1.0;

    // Draw Float Texts
    ctx.font = "bold 16px sans-serif";
    for (var fi = 0; fi < arpanState.floatTexts.length; fi++) {
      var ft = arpanState.floatTexts[fi];
      ctx.fillStyle = ft.color;
      ctx.globalAlpha = Math.max(0, ft.life);
      ctx.fillText(ft.text, ft.x, ft.y);
    }
    ctx.globalAlpha = 1.0;

    // Draw Basket / Golden Pooja Thali
    var b = arpanState.basket;
    b.y = h - 75;

    // Outer Glow under Thali
    ctx.shadowColor = "rgba(245, 158, 11, 0.55)";
    ctx.shadowBlur = 12;

    // Golden metallic gradient
    var thaliGrad = ctx.createLinearGradient(b.x, b.y, b.x, b.y + b.height);
    thaliGrad.addColorStop(0, '#FFE066');
    thaliGrad.addColorStop(0.3, '#FFD700');
    thaliGrad.addColorStop(0.7, '#D4AF37');
    thaliGrad.addColorStop(1, '#996515');

    ctx.fillStyle = thaliGrad;
    ctx.beginPath();
    if (typeof ctx.roundRect === 'function') {
      ctx.roundRect(b.x, b.y, b.width, b.height, [4, 4, 16, 16]);
    } else {
      ctx.rect(b.x, b.y, b.width, b.height);
    }
    ctx.fill();

    // Metallic Rim Stroke
    ctx.shadowBlur = 0;
    ctx.lineWidth = 2.5;
    ctx.strokeStyle = '#8B5A00';
    ctx.stroke();

    // Inner rim shine
    ctx.lineWidth = 1;
    ctx.strokeStyle = '#FFFBEB';
    ctx.beginPath();
    ctx.moveTo(b.x + 6, b.y + 3);
    ctx.lineTo(b.x + b.width - 6, b.y + 3);
    ctx.stroke();

    // Sacred Tilak dot in center
    ctx.fillStyle = "#DC2626";
    ctx.beginPath();
    ctx.arc(b.x + b.width / 2, b.y + b.height / 2 - 1, 3, 0, Math.PI * 2);
    ctx.fill();

    // Thali Label
    ctx.fillStyle = "#3D1E03";
    ctx.font = "bold 11px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("थाली 🌸", b.x + b.width / 2, b.y + b.height - 8);
  }

  function arpanGameLoop() {
    updateArpan();
    drawArpan();
    if (!arpanState.isGameOver) {
      arpanState.animFrameId = requestAnimationFrame(arpanGameLoop);
    }
  }

  function initPhoolArpanDOM() {
    arpanState.canvas = document.getElementById("arpanCanvas");
    if (!arpanState.canvas) return;
    arpanState.ctx = arpanState.canvas.getContext("2d");
    arpanState.container = document.getElementById("arpan-container");
    arpanState.scoreDisplay = document.getElementById("arpan-score");
    arpanState.livesDisplay = document.getElementById("arpan-lives");
    arpanState.gameOverModal = document.getElementById("arpan-game-over-modal");
    arpanState.finalScore = document.getElementById("arpan-final-score");
    arpanState.earnedCoins = document.getElementById("arpan-earned-coins");

    if (!arpanState.initialized) {
      arpanState.initialized = true;

      window.addEventListener("resize", function () {
        var arena = document.getElementById('phool-arpan-arena');
        if (arena && arena.style.display === 'flex') {
          resizeArpanCanvas();
        }
      });

      // Touch & Mouse
      arpanState.container.addEventListener("touchmove", function (e) {
        if (!arpanState.isGameOver && e.touches.length > 0) {
          moveArpanBasket(e.touches[0].clientX);
        }
      }, { passive: false });

      arpanState.container.addEventListener("touchstart", function (e) {
        if (!arpanState.isGameOver && e.touches.length > 0) {
          moveArpanBasket(e.touches[0].clientX);
        }
      }, { passive: false });

      arpanState.container.addEventListener("mousemove", function (e) {
        if (!arpanState.isGameOver) {
          moveArpanBasket(e.clientX);
        }
      });

      // Keyboard Controls for desktop
      window.addEventListener("keydown", function(e) {
        var arena = document.getElementById('phool-arpan-arena');
        if (!arena || arena.style.display !== 'flex' || arpanState.isGameOver) return;
        if (e.key === 'ArrowLeft' || e.key === 'a') {
          arpanState.basket.x = Math.max(0, arpanState.basket.x - 24);
        } else if (e.key === 'ArrowRight' || e.key === 'd') {
          arpanState.basket.x = Math.min(arpanState.width - arpanState.basket.width, arpanState.basket.x + 24);
        }
      });
    }
  }

  window.openPhoolArpanGame = function () {
    var arena = document.getElementById('phool-arpan-arena');
    if (!arena) return;
    arena.style.display = 'flex';
    hideBottomNavForGames();

    initPhoolArpanDOM();
    resizeArpanCanvas();
    window.restartPhoolArpanGame();
  };

  window.closePhoolArpanGame = function () {
    if (arpanState.animFrameId) {
      cancelAnimationFrame(arpanState.animFrameId);
      arpanState.animFrameId = null;
    }
    var arena = document.getElementById('phool-arpan-arena');
    if (arena) arena.style.display = 'none';
    restoreBottomNavIfExited();
  };

  var arpanDeityIdx = 0;
  window.restartPhoolArpanGame = function () {
    if (arpanState.animFrameId) {
      cancelAnimationFrame(arpanState.animFrameId);
      arpanState.animFrameId = null;
    }
    arpanState.score = 0;
    arpanState.lives = 3;
    arpanState.items.length = 0;
    arpanState.particles.length = 0;
    arpanState.floatTexts.length = 0;
    arpanState.isGameOver = false;
    arpanState.frameCount = 0;

    // Cycle worshipped deity at top altar
    if (typeof ALL_APP_DEITIES !== 'undefined' && ALL_APP_DEITIES.length > 0) {
      var curD = ALL_APP_DEITIES[arpanDeityIdx % ALL_APP_DEITIES.length];
      arpanDeityIdx++;
      var dImg = document.getElementById('arpan-deity-img');
      if (dImg) dImg.src = curD.img;
      var dName = document.getElementById('arpan-deity-name');
      if (dName) dName.textContent = curD.name;
    }

    if (arpanState.scoreDisplay) arpanState.scoreDisplay.innerText = "Prasad: 0";
    if (arpanState.livesDisplay) arpanState.livesDisplay.innerText = "Lives: ❤️❤️❤️";
    if (arpanState.gameOverModal) arpanState.gameOverModal.style.display = "none";

    resizeArpanCanvas();
    if (arpanState.basket && arpanState.width) {
      arpanState.basket.x = arpanState.width / 2 - arpanState.basket.width / 2;
    }
    arpanGameLoop();
  };

    window.IS_EPIC_GAMES_LOCKED = false;
  window.showEpicGameLockedNotice = function() {};
  window.closeEpicLockedModal = function() {};
  window.showEpicLockedToast = function() {};
  window.unlockEpicGames = function() {};
  window.addCoins = addCoins;
  window.loadCoins = loadCoins;

})();


/* ══════════════════════════════════════════════════════════════════════════════
   🎬 CINEMATIC EPIC GAMES INTRO VIDEO CONTROLLER
   ══════════════════════════════════════════════════════════════════════════════ */
var pendingGameDestination = 'page-epic-games';
var pendingGameCallback = null;

function triggerEpicGamesLaunchWithVideo(destination, callback) {
  pendingGameDestination = destination || 'page-epic-games';
  pendingGameCallback = (typeof callback === 'function') ? callback : null;

  var modal = document.getElementById('epic-games-video-modal');
  var video = document.getElementById('epic-games-intro-video');

  if (!modal || !video) {
    proceedToTargetGame();
    return;
  }

  // Attempt to pause any ambient audio
  if (typeof pauseAllAudio === 'function') {
    try { pauseAllAudio(); } catch (e) {}
  }
  if (typeof pauseMusic === 'function') {
    try { pauseMusic(); } catch (e) {}
  }

  modal.style.display = 'flex';
  // Trigger animation next frame
  requestAnimationFrame(function() {
    modal.classList.add('active');
  });

  // Video completion listener: automatically open game when finished
  video.onended = function() {
    closeVideoAndOpenGame();
  };

  // Error fallback: proceed directly if video fails to play
  video.onerror = function() {
    console.warn('Intro video error, proceeding directly to game.');
    closeVideoAndOpenGame();
  };

  // Play video
  try {
    video.currentTime = 0;
    var playPromise = video.play();
    if (playPromise !== undefined) {
      playPromise.catch(function(err) {
        console.warn('Autoplay error / user interaction required:', err);
      });
    }
  } catch (err) {
    console.warn('Video play exception:', err);
  }
}

function skipEpicGamesIntroVideo() {
  closeVideoAndOpenGame();
}

function closeVideoAndOpenGame() {
  var modal = document.getElementById('epic-games-video-modal');
  var video = document.getElementById('epic-games-intro-video');

  if (video) {
    try {
      video.pause();
      video.onended = null;
      video.onerror = null;
    } catch (e) {}
  }

  if (modal) {
    modal.classList.remove('active');
    setTimeout(function() {
      modal.style.display = 'none';
    }, 280);
  }

  proceedToTargetGame();
}

function proceedToTargetGame() {
  if (pendingGameCallback) {
    var cb = pendingGameCallback;
    pendingGameCallback = null;
    cb();
  } else if (pendingGameDestination) {
    var dest = pendingGameDestination;
    pendingGameDestination = 'page-epic-games';
    if (typeof showPage === 'function') {
      showPage(dest);
    }
  }
}

// Expose globally on window
window.triggerEpicGamesLaunchWithVideo = triggerEpicGamesLaunchWithVideo;
window.skipEpicGamesIntroVideo = skipEpicGamesIntroVideo;
window.closeVideoAndOpenGame = closeVideoAndOpenGame;


  /* ══════════════════════════════════════════════════════════════════════════════
     🎴 BHAKTI CARD MATCH LEVEL HUB (30 LEVELS CONTROLLER & SMOOTH SCROLL)
     ══════════════════════════════════════════════════════════════════════════════ */
  function openMatchLevelHub() {
    hideBottomNavForGames();
    var modal = document.getElementById('match-level-hub-modal');
    if (!modal) return;

    modal.style.setProperty('display', 'flex', 'important');
    modal.classList.add('active');

    // Update total stars in header
    var starsEl = document.getElementById('match-hub-total-stars');
    if (starsEl) starsEl.innerText = getMatchTotalStars();

    // Render 16 Sacred Symbols Strip
    renderMatchSymbolsStrip();

    // Render 30 Level Cards
    renderMatchLevelHubGrid();

    // Scroll to current active level smoothly
    setTimeout(function() {
      var scrollBody = document.getElementById('match-hub-scroll-body');
      var activeCard = document.querySelector('.match-level-card.is-current');
      if (scrollBody && activeCard) {
        var topPos = activeCard.offsetTop - 140;
        scrollBody.scrollTo({ top: Math.max(0, topPos), behavior: 'smooth' });
      }
    }, 120);
  }

  function closeMatchLevelHub() {
    var modal = document.getElementById('match-level-hub-modal');
    if (modal) {
      modal.classList.remove('active');
      modal.style.setProperty('display', 'none', 'important');
    }
    restoreBottomNavIfExited();
  }

  function renderMatchSymbolsStrip() {
    var strip = document.getElementById('match-symbols-strip');
    if (!strip || !bhaktiSymbols || !bhaktiSymbols.length) return;
    strip.innerHTML = '';

    bhaktiSymbols.forEach(function(sym) {
      var item = document.createElement('div');
      item.className = 'match-symbol-chip';
      item.onclick = function() {
        if (typeof showToast === 'function') {
          showToast('✨ पावन दर्शन: ' + sym.name);
        }
      };
      item.innerHTML = `
        <div class="symbol-chip-thumb-wrap">
          <img src="${sym.img}" alt="${sym.name}" class="symbol-chip-img" loading="lazy">
        </div>
        <span class="symbol-chip-label">${sym.name}</span>
      `;
      strip.appendChild(item);
    });
  }

  function renderMatchLevelHubGrid() {
    var grid = document.getElementById('match-level-hub-grid');
    if (!grid) return;
    grid.innerHTML = '';

    var totalStars = getMatchTotalStars();

    for (var lvl = 1; lvl <= 30; lvl++) {
      var cfg = getMatchLevelConfig(lvl);
      var starsEarned = savedMatchStars[lvl] || 0;
      var isBoss = (lvl % 10 === 0 || lvl === 30);

      // Unlock rule: Level 1 always unlocked. Level N unlocked if Level N-1 has >= 1 star OR totalStars >= (lvl-1)*2
      var prevWon = (lvl === 1) || (savedMatchStars[lvl - 1] && savedMatchStars[lvl - 1] > 0);
      var reqStars = (lvl - 1) * 2;
      var unlocked = (lvl === 1) || prevWon || (totalStars >= reqStars);
      var isCurrent = unlocked && (!savedMatchStars[lvl] || savedMatchStars[lvl] === 0) && (lvl === 1 || (savedMatchStars[lvl - 1] && savedMatchStars[lvl - 1] > 0));

      // Tier text & styling
      var tierName = '';
      var tierClass = '';
      if (lvl <= 10) {
        tierName = '🌱 प्रारंभिक';
        tierClass = 'tier-init';
      } else if (lvl <= 20) {
        tierName = '⚔️ महारथी';
        tierClass = 'tier-mid';
      } else {
        tierName = '🔱 दिव्य';
        tierClass = 'tier-divine';
      }

      var card = document.createElement('div');
      card.className = 'match-level-card' +
        (unlocked ? ' is-unlocked' : ' is-locked') +
        (isCurrent ? ' is-current' : '') +
        (isBoss ? ' is-boss' : '');

      card.setAttribute('data-level', lvl);

      // Card Header: Level Number (left) & Tier Badge (right)
      var bossBadgeHtml = isBoss ? `<span class="ml-boss-tag">👑 महा-स्तर</span>` : `<span class="ml-tier-tag ${tierClass}">${tierName}</span>`;

      // Footer: Stars or Play or Lock info
      var footerHtml = '';
      if (!unlocked) {
        footerHtml = `<div class="ml-status-locked"><span class="ml-lock-icon">🔒</span> <span>${reqStars} ⭐ चाहिए</span></div>`;
      } else if (starsEarned > 0) {
        var starsStr = '';
        for (var s = 1; s <= 5; s++) {
          starsStr += (s <= starsEarned) ? '⭐' : '☆';
        }
        footerHtml = `<div class="ml-stars-row"><span class="ml-stars-txt">${starsStr}</span></div>`;
      } else {
        footerHtml = `<div class="ml-status-play"><span class="ml-play-icon">▶</span> <span>खेलें</span></div>`;
      }

      card.innerHTML = `
        <div class="ml-card-header">
          <div class="ml-num-badge">${lvl}</div>
          ${bossBadgeHtml}
        </div>
        <div class="ml-card-body">
          <div class="ml-pairs-title">${cfg.pairs} जोड़ियाँ</div>
          <div class="ml-cards-sub">${cfg.pairs * 2} पावन कार्ड</div>
        </div>
        <div class="ml-card-footer">
          ${footerHtml}
        </div>
      `;

      // Click Handler
      (function(levelNum, isUnlocked, req) {
        card.onclick = function() {
          if (!isUnlocked) {
            showMatchLockAlert(req);
            return;
          }
          startMatchGameAtLevel(levelNum);
        };
      })(lvl, unlocked, reqStars);

      grid.appendChild(card);
    }
  }

  function startMatchGameAtLevel(lvl) {
    var hub = document.getElementById('match-level-hub-modal');
    if (hub) {
      hub.style.setProperty('display', 'none', 'important');
      hub.classList.remove('active');
    }

    var arena = document.getElementById('match-game-modal');
    if (arena) {
      arena.classList.add('active');
      arena.classList.add('is-open');
      arena.style.setProperty('display', 'flex', 'important');
      arena.style.setProperty('opacity', '1', 'important');
      arena.style.setProperty('pointer-events', 'auto', 'important');
      arena.style.setProperty('visibility', 'visible', 'important');
    }

    initMatchLevel(lvl);
  }

  function returnToMatchLevelHub() {
    var arena = document.getElementById('match-game-modal');
    if (arena) {
      arena.classList.remove('active');
      arena.classList.remove('is-open');
      arena.style.setProperty('display', 'none', 'important');
    }
    var winModal = document.getElementById('matchWinModal');
    if (winModal) winModal.style.display = 'none';

    openMatchLevelHub();
  }

  function closeMatchLevelArena() {
    returnToMatchLevelHub();
  }

  // Hook global functions
  window.openMatchLevelHub = openMatchLevelHub;
  window.closeMatchLevelHub = closeMatchLevelHub;
  window.renderMatchLevelHub = openMatchLevelHub;
  window.startMatchGameAtLevel = startMatchGameAtLevel;
  window.returnToMatchLevelHub = returnToMatchLevelHub;
  window.closeMatchLevelArena = closeMatchLevelArena;
