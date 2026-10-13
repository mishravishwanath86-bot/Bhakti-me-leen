/**
 * ══════════════════════════════════════════════════════════════════════════════
 * 🪔 AARTI & MANTRA DRAG-AND-DROP PUZZLE GAME ENGINE (आरती व मन्त्र पहेली इंजन)
 * Dynamic JSON Feeds • Desktop & Mobile Touch Drag-and-Drop • Visual Celebrations
 * ══════════════════════════════════════════════════════════════════════════════
 */

(function () {
  'use strict';

  // ── Fallback Embedded Data (Guarantees zero-failure in file:// or offline mode) ──
  var DEFAULT_DATA = {
    aartis: [
      {
        id: "aarti_ganesh",
        title: "जय गणेश जी",
        title_en: "Jai Ganesh Deva",
        category: "गणेश",
        level: 1,
        type: "aarti",
        thumb: "assets/deity_ganesh.jpg",
        lines: [
          "जय गणेश जय गणेश, जय गणेश देवा।",
          "माता जाकी पार्वती, पिता महादेवा।",
          "एक दंत दयावंत, चार भुजा धारी।",
          "माथे सिंदूर सोहे, मूसे की सवारी।",
          "पान चढ़े फल चढ़े, और चढ़े मेवा।",
          "लड्डुअन का भोग लगे, संत करें सेवा।",
          "अंधन को आंख देत, कोढ़िन को काया।",
          "बांझन को पुत्र देत, निर्धन को माया।",
          "'सूर' श्याम शरण आए, सफल कीजे सेवा।"
        ]
      },
      {
        id: "aarti_shiv",
        title: "जय शिव ओंकारा",
        title_en: "Jai Shiv Omkara",
        category: "शिव",
        level: 2,
        type: "aarti",
        thumb: "assets/deity_shiva.jpg",
        lines: [
          "जय शिव ओंकारा, हर ॐ शिवा ओंकारा।",
          "ब्रह्मा विष्णु सदाशिव अर्द्धांगी धारा॥",
          "एकानन चतुरानन पंचानन राजे।",
          "हंसासन गरुड़ासन वृषवाहन साजे॥",
          "दो भुज चार चतुर्भुज दस भुज अति सोहे।",
          "त्रिगुण रूपनिरखता त्रिभुवन जन मोहे॥",
          "अक्षमाला बनमाला रुण्डमाला धारी।",
          "चन्दन मृगमद सोहै, भाले शशिधारी॥"
        ]
      },
      {
        id: "aarti_jagdish",
        title: "ॐ जय जगदीश हरे",
        title_en: "Om Jai Jagdish Hare",
        category: "विष्णु",
        level: 3,
        type: "aarti",
        thumb: "assets/deity_vishnu.jpg",
        lines: [
          "ॐ जय जगदीश हरे, स्वामी जय जगदीश हरे।",
          "भक्त जनों के संकट, क्षण में दूर करे॥",
          "जो ध्यावे फल पावे, दुःख बिनसे मन का।",
          "सुख सम्पति घर आवे, कष्ट मिटे तन का॥",
          "मात पिता तुम मेरे, शरण गहूँ किसकी।",
          "तुम बिन और न दूजा, आस करूँ जिसकी॥",
          "तुम पूरण परमात्मा, तुम अन्तर्यामी।",
          "पारब्रह्म परमेश्वर, तुम सब के स्वामी॥"
        ]
      },
      {
        id: "aarti_hanuman",
        title: "आरती कीजै हनुमान लला की",
        title_en: "Aarti Kije Hanuman Lala Ki",
        category: "हनुमान",
        level: 4,
        type: "aarti",
        thumb: "assets/deity_hanuman.jpg",
        lines: [
          "आरती कीजै हनुमान लला की।",
          "दुष्ट दलन रघुनाथ कला की॥",
          "जाके बल से गिरिवर कांपै।",
          "रोग दोष जाके निकट न झांपै॥",
          "अंजनि पुत्र महा बलदाई।",
          "सन्तन के प्रभु सदा सहाई॥",
          "दे बीरा रघुनाथ पठाए।",
          "लंका जारि सिया सुधि लाए॥"
        ]
      },
      {
        id: "aarti_durga",
        title: "जय अम्बे गौरी",
        title_en: "Jai Ambe Gauri",
        category: "दुर्गा",
        level: 5,
        type: "aarti",
        thumb: "assets/deity_durga_hd.jpg",
        lines: [
          "जय अम्बे गौरी, मैया जय श्यामा गौरी।",
          "तुमको निशिदिन ध्यावत, हरि ब्रह्मा शिवरी॥",
          "मांग सिन्दूर विराजत, टीको मृगमद को।",
          "उज्ज्वल से दोउ नैना, चन्द्रवदन नीको॥",
          "कनक समान कलेवर, रक्ताम्बर राजै।",
          "रक्तपुष्प गल माला, कण्ठन पर साजै॥",
          "केहरि वाहन राजत, खड्ग खप्पर धारी।",
          "सुर-नर-मुनिजन सेवत, तिनके दुःखहारी॥"
        ]
      },
      {
        id: "aarti_kunjbihari",
        title: "आरती कुंजबिहारी की",
        title_en: "Aarti Kunjbihari Ki",
        category: "कृष्ण",
        level: 6,
        type: "aarti",
        thumb: "assets/deity_krishna.jpg",
        lines: [
          "आरती कुंजबिहारी की, श्री गिरधर कृष्ण मुरारी की।",
          "गले में बैजन्ती माला, बजावै मुरली मधुर बाला।",
          "श्रवण में कुण्डल झलकाता, पीत पट कटि तड़ित समाता।",
          "नील जलद तनु श्याम सुहावे, चरण कमल चितवन मन भावे।",
          "कनक कंकण कर सोहे, रूप लखि सुर नर मुनि मोहे।",
          "जयति जयति श्री राधा प्यारी, संग लकुट कर मुरलीधारी।"
        ]
      },
      {
        id: "aarti_ramchandra",
        title: "श्री रामचन्द्र कृपालु भजु मन",
        title_en: "Shri Ramchandra Kripalu Bhaju Man",
        category: "राम",
        level: 7,
        type: "aarti",
        thumb: "assets/deity_ram.jpg",
        lines: [
          "श्री रामचन्द्र कृपालु भजु मन हरण भवभय दारुणम्।",
          "नवकंज लोचन, कंज मुख, कर कंज, पद कंजारुणम्॥",
          "कन्दर्प अगणित अमित छवि, नवनील नीरद सुन्दरम्।",
          "पट पीत मानहु तड़ित रुचि शुचि नौमि जनक सुतावरम्॥",
          "भजु दीनबन्धु दिनेश दानव दैत्यवंश निकन्दनम्।",
          "रघुनन्द आनन्दकन्द कोशलचन्द दशरथ नन्दनम्॥",
          "सिर मुकुट कुण्डल तिलक चारु उदारु अंग विभूषणम्।",
          "आजानुभुज शर चाप धर, संग्राम जित खर दूषणम्॥"
        ]
      },
      {
        id: "aarti_lakshmi",
        title: "ॐ जय लक्ष्मी माता",
        title_en: "Om Jai Lakshmi Mata",
        category: "लक्ष्मी",
        level: 8,
        type: "aarti",
        thumb: "assets/gallery/divine_aura_light.jpg",
        lines: [
          "ॐ जय लक्ष्मी माता, मैया जय लक्ष्मी माता।",
          "तुमको निशिदिन सेवत, हर विष्णु विधाता॥",
          "उमा रमा ब्रह्माणी, तुम ही जग-माता।",
          "सूर्य-चन्द्रमा ध्यावत, नारद ऋषि गाता॥",
          "दुर्गा रूप निरंजनी, सुख सम्पति दाता।",
          "जो कोई तुमको ध्यावत, ऋद्धि-सिद्धि धन पाता॥",
          "जिस घर में तुम रहती, सब सद्गुण आता।",
          "सब सम्भव हो जाता, मन नहीं घबराता॥"
        ]
      }
    ],
    mantras: [
      {
        id: "mantra_gayatri",
        title: "गायत्री मंत्र",
        title_en: "Gayatri Mantra",
        category: "गायत्री",
        level: 1,
        type: "mantra",
        thumb: "assets/gallery/divine_aura_light.jpg",
        lines: [
          "ॐ भूर्भुवः स्वः",
          "तत्सवितुर्वरेण्यं",
          "भर्गो देवस्य धीमहि",
          "धियो यो नः प्रचोदयात्॥"
        ]
      },
      {
        id: "mantra_mahamrityunjaya",
        title: "महामृत्युंजय मंत्र",
        title_en: "Mahamrityunjaya Mantra",
        category: "शिव",
        level: 2,
        type: "mantra",
        thumb: "assets/deity_shiva.jpg",
        lines: [
          "ॐ त्र्यम्बकं यजामहे",
          "सुगन्धिं पुष्टिवर्धनम्",
          "उर्वारुकमिव बन्धनान्",
          "मृत्योर्मुक्षीय मामृतात्॥"
        ]
      },
      {
        id: "mantra_ganesh_mool",
        title: "श्री गणेश मूल मंत्र",
        title_en: "Ganesh Mool Mantra",
        category: "गणेश",
        level: 3,
        type: "mantra",
        thumb: "assets/deity_ganesh.jpg",
        lines: [
          "ॐ गं गणपतये नमः",
          "वक्रतुण्ड महाकाय",
          "सूर्यकोटि समप्रभ",
          "निर्विघ्नं कुरु मे देव",
          "सर्वकार्येषु सर्वदा॥"
        ]
      },
      {
        id: "mantra_shanti_path",
        title: "शांति पाठ मंत्र",
        title_en: "Shanti Paath Mantra",
        category: "शांति",
        level: 4,
        type: "mantra",
        thumb: "assets/gallery/morning_surya_namaskar.jpg",
        lines: [
          "ॐ द्यौः शान्तिरन्तरिक्षं शान्तिः",
          "पृथिवी शान्तिरापः शान्तिरोषधयः शान्तिः",
          "वनस्पतयः शान्तिर्विश्वेदेवाः शान्तिर्ब्रह्म शान्तिः",
          "सर्वं शान्तिः शान्तिरेव शान्तिः",
          "सा मा शान्तिरेधि॥ ॐ शान्तिः शान्तिः शान्तिः॥"
        ]
      },
      {
        id: "mantra_hanuman_mool",
        title: "हनुमान मूल मंत्र",
        title_en: "Hanuman Mool Mantra",
        category: "हनुमान",
        level: 5,
        type: "mantra",
        thumb: "assets/deity_hanuman.jpg",
        lines: [
          "ॐ हं हनुमते नमः",
          "मनोजवं मारुततुल्यवेगं",
          "जितेन्द्रियं बुद्धिमतां वरिष्ठम्",
          "वातात्मजं वानरयूथमुख्यं",
          "श्रीरामदूतं शरणं प्रपद्ये॥"
        ]
      },
      {
        id: "mantra_shiva_panchakshara",
        title: "शिव पंचाक्षर स्तोत्र / मंत्र",
        title_en: "Shiva Panchakshara Stotram",
        category: "शिव",
        level: 6,
        type: "mantra",
        thumb: "assets/deity_shiva.jpg",
        lines: [
          "नागेन्द्रहाराय त्रिलोचनाय",
          "भस्माङ्गरागाय महेश्वराय",
          "नित्याय शुद्धाय दिगम्बराय",
          "तस्मै 'न' काराय नमः शिवाय॥",
          "मन्दाकिनी सलिल चन्दन चर्चिताय",
          "नन्दीश्वर प्रमथनाथ महेश्वराय",
          "मन्दारपुष्प बहुपुष्प सुपूजिताय",
          "तस्मै 'म' काराय नमः शिवाय॥"
        ]
      },
      {
        id: "mantra_krishna_hare",
        title: "हरे कृष्ण महामंत्र",
        title_en: "Hare Krishna Mahamantra",
        category: "कृष्ण",
        level: 7,
        type: "mantra",
        thumb: "assets/deity_krishna.jpg",
        lines: [
          "हरे कृष्ण हरे कृष्ण",
          "कृष्ण कृष्ण हरे हरे",
          "हरे राम हरे राम",
          "राम राम हरे हरे॥"
        ]
      },
      {
        id: "mantra_durga_mool",
        title: "माँ दुर्गा नवार्ण मंत्र",
        title_en: "Durga Navarna Mantra",
        category: "दुर्गा",
        level: 8,
        type: "mantra",
        thumb: "assets/deity_durga_hd.jpg",
        lines: [
          "ॐ ऐं ह्रीं क्लीं",
          "चामुण्डायै विच्चे",
          "सर्वमंगल मांगल्ये",
          "शिवे सर्वार्थ साधिके",
          "शरण्ये त्र्यम्बके गौरि",
          "नारायणि नमोऽस्तु ते॥"
        ]
      }
    ]
  };

  // ── Engine State ──
  var state = {
    data: DEFAULT_DATA,
    currentType: 'aarti', // 'aarti' | 'mantra'
    selectedCategory: 'सभी',
    searchQuery: '',
    currentItem: null,
    currentLines: [],
    hintCount: 3,
    remainingSeconds: 180,
    startTimeSeconds: 180,
    fontScale: 16, // px
    timerInterval: null,
    previewTimerInterval: null,
    previewCountdown: 5,
    unlockedAartiLevel: 1,
    unlockedMantraLevel: 1,
    starsData: {},
    streak: 1,
    speechUtterance: null,
    isSpeaking: false,
    dragStartIndex: null
  };

  // ── Load Progression from LocalStorage ──
  function loadProgression() {
    try {
      var uAarti = localStorage.getItem('amp_unlocked_aarti');
      if (uAarti) state.unlockedAartiLevel = parseInt(uAarti, 10) || 1;

      var uMantra = localStorage.getItem('amp_unlocked_mantra');
      if (uMantra) state.unlockedMantraLevel = parseInt(uMantra, 10) || 1;

      var sData = localStorage.getItem('amp_stars_data');
      if (sData) state.starsData = JSON.parse(sData) || {};

      var strk = localStorage.getItem('amp_pooja_streak');
      if (strk) state.streak = parseInt(strk, 10) || 1;
    } catch (e) {
      console.warn("Storage load warning:", e);
    }
  }

  function saveProgression() {
    try {
      localStorage.setItem('amp_unlocked_aarti', state.unlockedAartiLevel);
      localStorage.setItem('amp_unlocked_mantra', state.unlockedMantraLevel);
      localStorage.setItem('amp_stars_data', JSON.stringify(state.starsData));
      localStorage.setItem('amp_pooja_streak', state.streak);
    } catch (e) {
      console.warn("Storage save warning:", e);
    }
  }

  // ── Fetch dynamic dataset if available ──
  function initDataset() {
    loadProgression();
    if (window.AARTI_MANTRA_PUZZLE_DATA) {
      state.data = window.AARTI_MANTRA_PUZZLE_DATA;
    } else {
      fetch('data/aarti_mantra_puzzle_data.json')
        .then(function (res) { return res.json(); })
        .then(function (json) {
          if (json && json.aartis && json.mantras) {
            state.data = json;
            renderSelectionList();
          }
        })
        .catch(function () {
          // Defaults gracefully retained
        });
    }
  }

  // ── Web Audio Synthesizer (Vedic Chimes & Win Fanfare) ──
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

  function playSfx(type) {
    try {
      var ctx = getAudioCtx();
      if (!ctx) return;
      var now = ctx.currentTime;

      if (type === 'swap') {
        var osc = ctx.createOscillator();
        var gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(320, now);
        osc.frequency.exponentialRampToValueAtTime(540, now + 0.08);
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.linearRampToValueAtTime(0.01, now + 0.08);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.08);
      } else if (type === 'hint') {
        [523.25, 659.25, 783.99].forEach(function (freq, i) {
          var osc = ctx.createOscillator();
          var gain = ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + i * 0.06);
          gain.gain.setValueAtTime(0.15, now + i * 0.06);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.06 + 0.3);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + i * 0.06);
          osc.stop(now + i * 0.06 + 0.3);
        });
      } else if (type === 'victory') {
        // Divine temple chime fanfare (C5, E5, G5, C6 + resonant bells)
        [523.25, 659.25, 783.99, 1046.50, 1318.51].forEach(function (freq, i) {
          var osc = ctx.createOscillator();
          var gain = ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + i * 0.12);
          gain.gain.setValueAtTime(0.25, now + i * 0.12);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.12 + 0.7);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + i * 0.12);
          osc.stop(now + i * 0.12 + 0.7);
        });
      } else if (type === 'timeup') {
        var osc = ctx.createOscillator();
        var gain = ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(160, now);
        osc.frequency.linearRampToValueAtTime(90, now + 0.4);
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.linearRampToValueAtTime(0.01, now + 0.4);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.4);
      }
    } catch (e) {
      console.warn("SFX error:", e);
    }
  }

  // ── Bottom Nav & Fullscreen Handling ──
  function hideNavs() {
    var nav = document.getElementById('curved-fluid-bottom-nav');
    if (nav) nav.classList.add('nav-hidden');
    var allNavs = document.querySelectorAll('.curved-fluid-bottom-nav, .app-bottom-nav, .bottom-nav');
    allNavs.forEach(function (el) { el.classList.add('nav-hidden'); });
  }

  function restoreNavsIfExited() {
    var selModal = document.getElementById('aarti-mantra-selection-modal');
    var gameArena = document.getElementById('aarti-mantra-game-arena');
    var isSelOpen = selModal && selModal.style.display === 'flex';
    var isGameOpen = gameArena && gameArena.style.display === 'flex';

    if (isSelOpen || isGameOpen) return;

    var activePage = '';
    if (typeof window.currentPage !== 'undefined' && window.currentPage) {
      activePage = window.currentPage;
    } else {
      var p = document.querySelector('.page.active');
      if (p) activePage = p.id;
    }
    if (activePage === 'page-epic-games' || activePage === 'page-reader' || activePage === 'page-3d-mandir') {
      return;
    }
    var nav = document.getElementById('curved-fluid-bottom-nav');
    if (nav) nav.classList.remove('nav-hidden');
    var allNavs = document.querySelectorAll('.curved-fluid-bottom-nav, .app-bottom-nav, .bottom-nav');
    allNavs.forEach(function (el) { el.classList.remove('nav-hidden'); });
  }

  // ══════════════════════════════════════════════════════════════════════════════
  // SCREEN 1 & SCREEN 2: SELECTION SCREEN LOGIC
  // ══════════════════════════════════════════════════════════════════════════════

  window.openAartiGame = function (itemId) {
    window.openAartiMantraHub('aarti', itemId);
  };

  window.openMantraGame = function (itemId) {
    window.openAartiMantraHub('mantra', itemId);
  };

  window.openAartiMantraHub = function (type, specificItemId) {
    hideNavs();
    var modal = document.getElementById('aarti-mantra-selection-modal');
    if (!modal) return;
    modal.style.display = 'flex';

    state.currentType = (type === 'mantra') ? 'mantra' : 'aarti';
    state.selectedCategory = 'सभी';
    state.searchQuery = '';

    var searchInput = document.getElementById('amp-search-input');
    if (searchInput) searchInput.value = '';

    updateSelectionUI();

    // If specific item requested and unlocked, open game immediately
    if (specificItemId) {
      var pool = (state.currentType === 'aarti') ? state.data.aartis : state.data.mantras;
      var target = pool.find(function (item) { return item.id === specificItemId; });
      if (target) {
        window.startAartiMantraGame(target);
      }
    }
  };

  window.closeAartiMantraHub = function () {
    var modal = document.getElementById('aarti-mantra-selection-modal');
    if (modal) modal.style.display = 'none';
    restoreNavsIfExited();
  };

  window.switchAartiMantraTab = function (type) {
    state.currentType = type;
    state.selectedCategory = 'सभी';
    state.searchQuery = '';
    var searchInput = document.getElementById('amp-search-input');
    if (searchInput) searchInput.value = '';
    updateSelectionUI();
  };

  function updateSelectionUI() {
    // Header title
    var titleEl = document.getElementById('amp-selection-title');
    if (titleEl) {
      titleEl.innerHTML = state.currentType === 'aarti' ? '🪔 आरती संग्रह' : '🕉️ मन्त्र संग्रह';
    }

    // Tabs
    var tabAarti = document.getElementById('amp-tab-aarti');
    var tabMantra = document.getElementById('amp-tab-mantra');
    if (tabAarti) tabAarti.classList.toggle('active', state.currentType === 'aarti');
    if (tabMantra) tabMantra.classList.toggle('active', state.currentType === 'mantra');

    // Streak pill
    var streakEl = document.getElementById('amp-streak-count');
    if (streakEl) streakEl.textContent = state.streak;

    renderCategoryChips();
    renderSelectionList();
  }

  function renderCategoryChips() {
    var bar = document.getElementById('amp-categories-bar');
    if (!bar) return;

    var pool = (state.currentType === 'aarti') ? state.data.aartis : state.data.mantras;
    var catsSet = new Set();
    catsSet.add('सभी');
    pool.forEach(function (item) {
      if (item.category) catsSet.add(item.category);
    });

    var cats = Array.from(catsSet);
    bar.innerHTML = cats.map(function (c) {
      var isAct = state.selectedCategory === c;
      return `<button class="amp-cat-chip ${isAct ? 'active' : ''}" onclick="window.filterAartiMantraCategory('${c}')">${c}</button>`;
    }).join('');
  }

  window.filterAartiMantraCategory = function (category) {
    state.selectedCategory = category;
    renderCategoryChips();
    renderSelectionList();
  };

  window.handleAartiMantraSearch = function (query) {
    state.searchQuery = (query || '').trim().toLowerCase();
    renderSelectionList();
  };

  function renderSelectionList() {
    var container = document.getElementById('amp-items-container');
    if (!container) return;

    var pool = (state.currentType === 'aarti') ? state.data.aartis : state.data.mantras;
    var highestUnlocked = (state.currentType === 'aarti') ? state.unlockedAartiLevel : state.unlockedMantraLevel;

    var filtered = pool.filter(function (item) {
      // Category filter
      if (state.selectedCategory !== 'सभी' && item.category !== state.selectedCategory) {
        return false;
      }
      // Search filter
      if (state.searchQuery) {
        var matchTitle = (item.title && item.title.toLowerCase().includes(state.searchQuery)) ||
                         (item.title_en && item.title_en.toLowerCase().includes(state.searchQuery)) ||
                         (item.category && item.category.toLowerCase().includes(state.searchQuery));
        var matchLines = item.lines && item.lines.some(function (l) { return l.toLowerCase().includes(state.searchQuery); });
        if (!matchTitle && !matchLines) return false;
      }
      return true;
    });

    if (filtered.length === 0) {
      container.innerHTML = `
        <div style="text-align:center; padding:40px 20px; color:#94A3B8;">
          <div style="font-size:2.5rem; margin-bottom:8px;">🔍</div>
          <div style="font-size:1rem; font-weight:800; color:#64748B;">कोई परिणाम नहीं मिला</div>
          <div style="font-size:0.82rem; margin-top:4px;">कृपया अन्य नाम या श्रेणी खोजें।</div>
        </div>`;
      return;
    }

    container.innerHTML = filtered.map(function (item) {
      var isUnlocked = item.level <= highestUnlocked;
      var starsEarned = state.starsData[item.id] || 0;
      var starsHtml = '';
      for (var s = 1; s <= 3; s++) {
        starsHtml += `<span style="color:${s <= starsEarned ? '#F59E0B' : 'rgba(148,163,184,0.4)'};">★</span>`;
      }

      var thumbSrc = item.thumb || 'assets/deity_ganesh.jpg';

      return `
        <div class="amp-item-card ${isUnlocked ? '' : 'is-locked'}" onclick="${isUnlocked ? "window.startAartiMantraGameById('" + item.id + "')" : "window.showLockedToast(" + item.level + ")"}">
          <div class="amp-item-card-left">
            <img src="${thumbSrc}" alt="${item.title}" class="amp-item-thumb" onerror="this.src='assets/deity_ganesh.jpg';">
            <div class="amp-item-info">
              <div class="amp-item-badge-row">
                <span class="amp-level-badge">स्तर ${item.level}</span>
                <span class="amp-cat-badge">${item.category}</span>
              </div>
              <h3 class="amp-item-title">${item.title}</h3>
              <div class="amp-item-meta">
                <span>📝 ${item.lines.length} पद/पंक्तियाँ</span>
                <span>•</span>
                <span>⏱️ 3 मिनट</span>
              </div>
            </div>
          </div>
          <div class="amp-item-card-right">
            <div class="amp-stars-row">${starsHtml}</div>
            ${isUnlocked 
              ? `<button class="amp-play-btn" onclick="event.stopPropagation(); window.startAartiMantraGameById('${item.id}');">🎮 खेलें</button>`
              : `<div class="amp-lock-icon" title="स्तर ${item.level} पर अनलॉक होगा">🔒</div>`
            }
          </div>
        </div>
      `;
    }).join('');
  }

  window.showLockedToast = function (level) {
    if (typeof showToast === 'function') {
      showToast(`🔒 यह स्तर अभी बंद है! पिछले स्तर पूरे करके स्तर ${level} अनलॉक करें।`);
    } else {
      alert(`यह स्तर अभी बंद है! पिछले स्तर पूरे करके स्तर ${level} अनलॉक करें।`);
    }
  };

  window.startAartiMantraGameById = function (id) {
    var pool = (state.currentType === 'aarti') ? state.data.aartis : state.data.mantras;
    var item = pool.find(function (it) { return it.id === id; });
    if (item) {
      window.startAartiMantraGame(item);
    }
  };

  // ══════════════════════════════════════════════════════════════════════════════
  // SCREEN 3: UNIVERSAL DRAG-AND-DROP GAMEPLAY ENGINE
  // ══════════════════════════════════════════════════════════════════════════════

  window.startAartiMantraGame = function (item) {
    hideNavs();
    state.currentItem = item;
    state.hintCount = 3;
    state.remainingSeconds = 180;
    state.startTimeSeconds = 180;

    // Shuffle lines until order differs from original
    var shuffled = item.lines.slice();
    if (shuffled.length > 1) {
      var attempts = 0;
      do {
        shuffled.sort(function () { return Math.random() - 0.5; });
        attempts++;
      } while (attempts < 10 && arraysEqual(shuffled, item.lines));
    }
    state.currentLines = shuffled;

    // Show Gameplay Arena
    var arena = document.getElementById('aarti-mantra-game-arena');
    if (!arena) return;
    arena.style.display = 'flex';

    // Update Header
    var titleEl = document.getElementById('amp-game-curr-title');
    if (titleEl) titleEl.textContent = item.title;
    var subEl = document.getElementById('amp-game-curr-sub');
    if (subEl) subEl.textContent = `${item.category} • स्तर ${item.level}`;

    updateHintDisplay();
    updateTimerDisplay();
    renderDragList();
    startTimer();
  };

  window.closeAartiMantraGame = function () {
    stopTimer();
    stopSpeechRecitation();
    var arena = document.getElementById('aarti-mantra-game-arena');
    if (arena) arena.style.display = 'none';

    var winDialog = document.getElementById('amp-win-dialog');
    if (winDialog) winDialog.style.display = 'none';

    var gameoverDialog = document.getElementById('amp-gameover-dialog');
    if (gameoverDialog) gameoverDialog.style.display = 'none';

    var previewModal = document.getElementById('amp-preview-modal');
    if (previewModal) previewModal.style.display = 'none';

    stopFlowerShower();
    renderSelectionList();
    restoreNavsIfExited();
  };

  // ── Timer Logic ──
  function startTimer() {
    stopTimer();
    state.timerInterval = setInterval(function () {
      if (state.remainingSeconds > 0) {
        state.remainingSeconds--;
        updateTimerDisplay();
      } else {
        stopTimer();
        playSfx('timeup');
        showGameOverDialog();
      }
    }, 1000);
  }

  function stopTimer() {
    if (state.timerInterval) {
      clearInterval(state.timerInterval);
      state.timerInterval = null;
    }
  }

  function updateTimerDisplay() {
    var timerEl = document.getElementById('amp-game-timer');
    if (!timerEl) return;
    var m = Math.floor(state.remainingSeconds / 60);
    var s = state.remainingSeconds % 60;
    var formatted = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    timerEl.textContent = formatted;

    if (state.remainingSeconds <= 30) {
      timerEl.classList.add('is-warning');
    } else {
      timerEl.classList.remove('is-warning');
    }
  }

  function showGameOverDialog() {
    var dlg = document.getElementById('amp-gameover-dialog');
    if (dlg) dlg.style.display = 'flex';
  }

  window.retryCurrentAartiMantraGame = function () {
    var dlg = document.getElementById('amp-gameover-dialog');
    if (dlg) dlg.style.display = 'none';

    if (state.currentItem) {
      window.startAartiMantraGame(state.currentItem);
    }
  };

  // ── Font Scaling Accessibility ──
  window.toggleAartiFontScale = function () {
    if (state.fontScale === 14) state.fontScale = 16;
    else if (state.fontScale === 16) state.fontScale = 18;
    else if (state.fontScale === 18) state.fontScale = 20;
    else state.fontScale = 14;

    var btn = document.getElementById('amp-font-scale-btn');
    if (btn) btn.textContent = state.fontScale + 'px';

    renderDragList();
  };

  // ── 5-Second Preview Dialog ("देखें") ──
  window.showAartiPreviewDialog = function () {
    if (!state.currentItem) return;
    var modal = document.getElementById('amp-preview-modal');
    if (!modal) return;
    modal.style.display = 'flex';

    var titleEl = document.getElementById('amp-preview-title');
    if (titleEl) titleEl.textContent = state.currentItem.title;

    var bodyEl = document.getElementById('amp-preview-body');
    if (bodyEl) {
      bodyEl.innerHTML = state.currentItem.lines.map(function (line, idx) {
        return `<div class="amp-preview-line-item">${idx + 1}. ${line}</div>`;
      }).join('');
    }

    state.previewCountdown = 5;
    var timerBadge = document.getElementById('amp-preview-timer-pill');
    if (timerBadge) timerBadge.textContent = 'समय शेष: 5s';

    if (state.previewTimerInterval) clearInterval(state.previewTimerInterval);
    state.previewTimerInterval = setInterval(function () {
      state.previewCountdown--;
      if (timerBadge) timerBadge.textContent = 'समय शेष: ' + state.previewCountdown + 's';
      if (state.previewCountdown <= 0) {
        window.closeAartiPreviewDialog();
      }
    }, 1000);
  };

  window.closeAartiPreviewDialog = function () {
    if (state.previewTimerInterval) {
      clearInterval(state.previewTimerInterval);
      state.previewTimerInterval = null;
    }
    var modal = document.getElementById('amp-preview-modal');
    if (modal) modal.style.display = 'none';
  };

  // ── Hint Button Logic ──
  window.useAartiHint = function () {
    if (state.hintCount <= 0 || !state.currentItem) return;

    var orig = state.currentItem.lines;
    var curr = state.currentLines;

    // Find the first index where currentLines[i] !== originalLines[i]
    var misplacedIdx = -1;
    for (var i = 0; i < orig.length; i++) {
      if (curr[i] !== orig[i]) {
        misplacedIdx = i;
        break;
      }
    }

    if (misplacedIdx !== -1) {
      var correctTarget = orig[misplacedIdx];
      var fromIdx = curr.indexOf(correctTarget);

      // Snap the next misplaced line to its correct index
      curr.splice(fromIdx, 1);
      curr.splice(misplacedIdx, 0, correctTarget);

      state.hintCount--;
      updateHintDisplay();
      playSfx('hint');
      renderDragList();

      // Highlight the snapped line card
      var cards = document.querySelectorAll('.amp-line-card');
      if (cards[misplacedIdx]) {
        cards[misplacedIdx].classList.add('is-correct-hint');
      }

      window.checkAartiOrder(false);
    }
  };

  function updateHintDisplay() {
    var btn = document.getElementById('amp-hint-btn');
    if (btn) {
      btn.innerHTML = `💡 हिंट ( ${state.hintCount} )`;
      btn.disabled = state.hintCount <= 0;
    }
  }

  // ── Reshuffle Button ──
  window.reshuffleCurrentAartiLines = function () {
    if (!state.currentItem) return;
    state.currentLines.sort(function () { return Math.random() - 0.5; });
    playSfx('swap');
    renderDragList();
  };

  // ── Nudge Line Accessible Controls (▲ / ▼) ──
  window.nudgeAartiLine = function (index, direction) {
    var targetIdx = index + direction;
    if (targetIdx < 0 || targetIdx >= state.currentLines.length) return;

    var temp = state.currentLines[index];
    state.currentLines[index] = state.currentLines[targetIdx];
    state.currentLines[targetIdx] = temp;

    playSfx('swap');
    renderDragList();
    window.checkAartiOrder(false);
  };

  // ══════════════════════════════════════════════════════════════════════════════
  // DRAG AND DROP RENDERING & EVENT HANDLING
  // ══════════════════════════════════════════════════════════════════════════════

  function renderDragList() {
    var container = document.getElementById('amp-drag-area');
    if (!container) return;

    container.innerHTML = state.currentLines.map(function (line, idx) {
      var isFirst = idx === 0;
      var isLast = idx === state.currentLines.length - 1;

      return `
        <div class="amp-line-card" 
             draggable="true" 
             data-index="${idx}"
             ondragstart="window.handleAartiDragStart(event, ${idx})"
             ondragover="window.handleAartiDragOver(event, ${idx})"
             ondragleave="window.handleAartiDragLeave(event, ${idx})"
             ondrop="window.handleAartiDrop(event, ${idx})"
             ondragend="window.handleAartiDragEnd(event)"
             ontouchstart="window.handleAartiTouchStart(event, ${idx})"
             ontouchmove="window.handleAartiTouchMove(event)"
             ontouchend="window.handleAartiTouchEnd(event)">
          <div class="amp-line-left">
            <span class="amp-drag-handle">⠿</span>
            <span class="amp-line-num">${idx + 1}</span>
            <span class="amp-line-text" style="font-size:${state.fontScale}px;">${line}</span>
          </div>
          <div class="amp-nudge-btns">
            <button class="amp-nudge-btn" onclick="window.nudgeAartiLine(${idx}, -1)" ${isFirst ? 'disabled style="opacity:0.3; cursor:default;"' : ''} title="ऊपर करें">▲</button>
            <button class="amp-nudge-btn" onclick="window.nudgeAartiLine(${idx}, 1)" ${isLast ? 'disabled style="opacity:0.3; cursor:default;"' : ''} title="नीचे करें">▼</button>
          </div>
        </div>
      `;
    }).join('');
  }

  // ── HTML5 Desktop Drag & Drop Handlers ──
  window.handleAartiDragStart = function (e, idx) {
    state.dragStartIndex = idx;
    e.currentTarget.classList.add('is-dragging');
    if (e.dataTransfer) {
      e.dataTransfer.effectAllowed = 'move';
      e.dataTransfer.setData('text/plain', idx);
    }
  };

  window.handleAartiDragOver = function (e, idx) {
    e.preventDefault();
    if (e.dataTransfer) e.dataTransfer.dropEffect = 'move';
    var card = e.currentTarget;
    if (!card.classList.contains('drag-over') && state.dragStartIndex !== idx) {
      card.classList.add('drag-over');
    }
  };

  window.handleAartiDragLeave = function (e, idx) {
    e.currentTarget.classList.remove('drag-over');
  };

  window.handleAartiDrop = function (e, targetIdx) {
    e.preventDefault();
    e.currentTarget.classList.remove('drag-over');
    if (state.dragStartIndex === null || state.dragStartIndex === targetIdx) return;

    var item = state.currentLines.splice(state.dragStartIndex, 1)[0];
    state.currentLines.splice(targetIdx, 0, item);

    state.dragStartIndex = null;
    playSfx('swap');
    renderDragList();
    window.checkAartiOrder(false);
  };

  window.handleAartiDragEnd = function (e) {
    state.dragStartIndex = null;
    document.querySelectorAll('.amp-line-card').forEach(function (card) {
      card.classList.remove('is-dragging', 'drag-over');
    });
  };

  // ── Mobile Touch Drag & Drop Handlers ──
  var touchState = {
    isDragging: false,
    dragIndex: null,
    ghostEl: null,
    currentOverIdx: null
  };

  window.handleAartiTouchStart = function (e, idx) {
    if (e.touches.length !== 1) return;
    touchState.dragIndex = idx;
    touchState.isDragging = true;
    touchState.currentOverIdx = idx;

    var card = e.currentTarget;
    card.classList.add('is-dragging');

    // Create a floating ghost card
    if (!touchState.ghostEl) {
      var ghost = card.cloneNode(true);
      ghost.style.position = 'fixed';
      ghost.style.pointerEvents = 'none';
      ghost.style.zIndex = '9999';
      ghost.style.width = card.offsetWidth + 'px';
      ghost.style.boxShadow = '0 12px 32px rgba(245, 158, 11, 0.45)';
      ghost.style.border = '2px solid #F59E0B';
      ghost.style.opacity = '0.92';
      ghost.style.transform = 'scale(1.03)';
      document.body.appendChild(ghost);
      touchState.ghostEl = ghost;
      updateGhostPos(e.touches[0].clientX, e.touches[0].clientY);
    }
  };

  window.handleAartiTouchMove = function (e) {
    if (!touchState.isDragging || !touchState.ghostEl) return;
    e.preventDefault(); // Prevent accidental page scrolling during touch drag

    var touch = e.touches[0];
    updateGhostPos(touch.clientX, touch.clientY);

    // Find card under finger
    touchState.ghostEl.style.display = 'none';
    var targetEl = document.elementFromPoint(touch.clientX, touch.clientY);
    touchState.ghostEl.style.display = 'flex';

    if (targetEl) {
      var lineCard = targetEl.closest('.amp-line-card');
      if (lineCard) {
        var hoverIdx = parseInt(lineCard.getAttribute('data-index'), 10);
        if (!isNaN(hoverIdx) && hoverIdx !== touchState.currentOverIdx) {
          touchState.currentOverIdx = hoverIdx;
          document.querySelectorAll('.amp-line-card').forEach(function (c) {
            c.classList.remove('drag-over');
          });
          lineCard.classList.add('drag-over');
        }
      }
    }
  };

  window.handleAartiTouchEnd = function (e) {
    if (!touchState.isDragging) return;

    if (touchState.ghostEl) {
      touchState.ghostEl.remove();
      touchState.ghostEl = null;
    }

    document.querySelectorAll('.amp-line-card').forEach(function (c) {
      c.classList.remove('is-dragging', 'drag-over');
    });

    if (touchState.dragIndex !== null && 
        touchState.currentOverIdx !== null && 
        touchState.dragIndex !== touchState.currentOverIdx) {
      var moved = state.currentLines.splice(touchState.dragIndex, 1)[0];
      state.currentLines.splice(touchState.currentOverIdx, 0, moved);

      playSfx('swap');
      if (navigator.vibrate) navigator.vibrate(25);
      renderDragList();
      window.checkAartiOrder(false);
    }

    touchState.isDragging = false;
    touchState.dragIndex = null;
    touchState.currentOverIdx = null;
  };

  function updateGhostPos(clientX, clientY) {
    if (!touchState.ghostEl) return;
    touchState.ghostEl.style.left = (clientX - 60) + 'px';
    touchState.ghostEl.style.top = (clientY - 30) + 'px';
  }

  // ══════════════════════════════════════════════════════════════════════════════
  // WIN VALIDATION & CELEBRATION
  // ══════════════════════════════════════════════════════════════════════════════

  function arraysEqual(a, b) {
    if (a.length !== b.length) return false;
    for (var i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) return false;
    }
    return true;
  }

  window.checkAartiOrder = function (manualCheck) {
    if (!state.currentItem) return;

    var isCorrect = arraysEqual(state.currentLines, state.currentItem.lines);

    if (isCorrect) {
      stopTimer();
      playSfx('victory');
      handleLevelWin();
    } else if (manualCheck) {
      // Gentle feedback on manual submit
      if (typeof showToast === 'function') {
        showToast("क्रम अभी सही नहीं है। हिंट 💡 का उपयोग करें!");
      } else {
        alert("क्रम अभी सही नहीं है। हिंट 💡 का उपयोग करें!");
      }
    }
  };

  function handleLevelWin() {
    var item = state.currentItem;
    var timeTaken = state.startTimeSeconds - state.remainingSeconds;

    // Calculate stars: <=60s: 3 stars, <=120s: 2 stars, otherwise 1 star
    var stars = 1;
    if (timeTaken <= 60) stars = 3;
    else if (timeTaken <= 120) stars = 2;

    // Save stars
    var prevStars = state.starsData[item.id] || 0;
    if (stars > prevStars) {
      state.starsData[item.id] = stars;
    }

    // Unlock next level sequentially
    if (state.currentType === 'aarti') {
      if (item.level >= state.unlockedAartiLevel && state.unlockedAartiLevel < state.data.aartis.length) {
        state.unlockedAartiLevel = item.level + 1;
      }
    } else {
      if (item.level >= state.unlockedMantraLevel && state.unlockedMantraLevel < state.data.mantras.length) {
        state.unlockedMantraLevel = item.level + 1;
      }
    }

    // Increase streak & award coins
    state.streak++;
    saveProgression();
    if (typeof window.addCoins === 'function') {
      window.addCoins(100);
    }

    // Trigger Particle Flower Shower
    startFlowerShower();

    // Show Win Celebration Modal
    var modal = document.getElementById('amp-win-dialog');
    if (!modal) return;
    modal.style.display = 'flex';

    // Populate modal details
    var headingEl = document.getElementById('amp-win-heading');
    if (headingEl) {
      headingEl.textContent = state.currentType === 'aarti' ? "अति सुंदर! आरती पूर्ण हुई 🪔" : "अति सुंदर! मन्त्र साधना पूर्ण हुई 🕉️";
    }

    var subEl = document.getElementById('amp-win-sub');
    if (subEl) subEl.textContent = item.title;

    var starsEl = document.getElementById('amp-win-stars');
    if (starsEl) {
      var stHtml = '';
      for (var i = 1; i <= 3; i++) {
        stHtml += `<span class="amp-star-item" style="color:${i <= stars ? '#F59E0B' : '#CBD5E1'}; animation-delay:${i * 0.15}s;">★</span>`;
      }
      starsEl.innerHTML = stHtml;
    }

    var statsEl = document.getElementById('amp-win-stats');
    if (statsEl) {
      statsEl.innerHTML = `<span>⏱️ समय: ${timeTaken}s</span> <span>•</span> <span>🪙 +100 सिक्के</span> <span>•</span> <span>🔥 स्ट्रीक: ${state.streak}</span>`;
    }

    var lyricsEl = document.getElementById('amp-win-lyrics');
    if (lyricsEl) {
      lyricsEl.innerHTML = item.lines.map(function (l) { return `<div>${l}</div>`; }).join('');
    }

    var listenBtn = document.getElementById('amp-listen-btn');
    if (listenBtn) {
      listenBtn.classList.remove('is-playing');
      listenBtn.innerHTML = '<span>🔊</span> <span>पाठ सुनें (Listen)</span>';
    }
  }

  // ── Next Level Progression ──
  window.goToNextAartiLevel = function () {
    var modal = document.getElementById('amp-win-dialog');
    if (modal) modal.style.display = 'none';
    stopFlowerShower();
    stopSpeechRecitation();

    if (!state.currentItem) return;

    var pool = (state.currentType === 'aarti') ? state.data.aartis : state.data.mantras;
    var nextItem = pool.find(function (it) { return it.level === state.currentItem.level + 1; });

    if (nextItem) {
      window.startAartiMantraGame(nextItem);
    } else {
      // Completed all levels
      window.closeAartiMantraGame();
      if (typeof showToast === 'function') {
        showToast("🎉 बधाई हो! आपने सभी पावन स्तर पूर्ण कर लिए हैं।");
      }
    }
  };

  // ── Audio Recitation (Speech Synthesis + Vedic Chime) ──
  window.toggleAartiSpeechRecitation = function () {
    if (!state.currentItem) return;

    if (state.isSpeaking) {
      stopSpeechRecitation();
      return;
    }

    var text = state.currentItem.lines.join('। ');
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      var utt = new SpeechSynthesisUtterance(text);
      utt.lang = 'hi-IN';
      utt.rate = 0.85; // Serene devotional tempo
      utt.pitch = 1.0;

      utt.onstart = function () {
        state.isSpeaking = true;
        var btn = document.getElementById('amp-listen-btn');
        if (btn) {
          btn.classList.add('is-playing');
          btn.innerHTML = '<span>⏸️</span> <span>रोकें (Pause)</span>';
        }
      };

      utt.onend = function () {
        stopSpeechRecitation();
      };

      utt.onerror = function () {
        stopSpeechRecitation();
      };

      state.speechUtterance = utt;
      window.speechSynthesis.speak(utt);
    } else {
      playSfx('victory');
    }
  };

  function stopSpeechRecitation() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    state.isSpeaking = false;
    var btn = document.getElementById('amp-listen-btn');
    if (btn) {
      btn.classList.remove('is-playing');
      btn.innerHTML = '<span>🔊</span> <span>पाठ सुनें (Listen)</span>';
    }
  }

  // ══════════════════════════════════════════════════════════════════════════════
  // PARTICLE FLOWER SHOWER (Confetti / Flower Petals Falling Down)
  // ══════════════════════════════════════════════════════════════════════════════

  var flowerAnimId = null;
  var flowerParticles = [];
  var FLOWER_SYMBOLS = ['🌸', '🌺', '🌼', '🏵️', '🪷', '✨'];

  function startFlowerShower() {
    var canvas = document.getElementById('amp-flower-canvas');
    if (!canvas) return;
    canvas.style.display = 'block';
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    var ctx = canvas.getContext('2d');
    flowerParticles = [];

    // Create 65 swirling petals
    for (var i = 0; i < 65; i++) {
      flowerParticles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * -canvas.height,
        symbol: FLOWER_SYMBOLS[Math.floor(Math.random() * FLOWER_SYMBOLS.length)],
        size: 18 + Math.random() * 22,
        speedY: 2.2 + Math.random() * 3.5,
        speedX: Math.sin(i) * 1.5,
        rotation: Math.random() * 360,
        rotSpeed: (Math.random() - 0.5) * 3,
        opacity: 0.8 + Math.random() * 0.2
      });
    }

    if (flowerAnimId) cancelAnimationFrame(flowerAnimId);

    function loop() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      flowerParticles.forEach(function (p) {
        p.y += p.speedY;
        p.x += Math.sin(p.y * 0.02) * 1.2;
        p.rotation += p.rotSpeed;

        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.font = p.size + 'px serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(p.symbol, 0, 0);
        ctx.restore();

        // Recycle petal to top
        if (p.y > canvas.height + 40) {
          p.y = -30;
          p.x = Math.random() * canvas.width;
        }
      });
      flowerAnimId = requestAnimationFrame(loop);
    }
    loop();
  }

  function stopFlowerShower() {
    if (flowerAnimId) {
      cancelAnimationFrame(flowerAnimId);
      flowerAnimId = null;
    }
    var canvas = document.getElementById('amp-flower-canvas');
    if (canvas) {
      canvas.style.display = 'none';
      var ctx = canvas.getContext('2d');
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }

  // ── Auto Init on DOM Ready ──
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDataset);
  } else {
    initDataset();
  }

})();
