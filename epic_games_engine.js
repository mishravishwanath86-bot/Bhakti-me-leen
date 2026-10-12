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
  // 1. SWIPE GAME: DATASETS (Ayodhya vs Mithila + Mahabharata + Samudra Manthan)
  // ══════════════════════════════════════════════════════════════════════════════
  var SWIPE_CATEGORIES = {
    ayodhya_mithila: {
      id: 'ayodhya_mithila',
      name: 'अयोध्या या मिथिला',
      instruction: 'अयोध्या या मिथिला के पक्ष की ओर स्वाइप करें',
      leftTeam: { id: 'ayodhya', name: 'अयोध्या', scoreClass: 'score-ayodhya', portalImg: 'assets/games/portal_ayodhya.jpg' },
      rightTeam: { id: 'mithila', name: 'मिथिला', scoreClass: 'score-mithila', portalImg: 'assets/games/portal_mithila.jpg' },
      characters: [
        {
          id: 'sunaina',
          name: 'सुनेना',
          team: 'mithila',
          teamLabel: 'मिथिला',
          img: 'assets/games/char_sunaina.jpg',
          avatar: 'assets/games/char_sunaina.jpg',
          desc: 'मिथिला की महारानी, राजा जनक की पत्नी और माता सीता की पूज्य माता।'
        },
        {
          id: 'janak',
          name: 'जनक',
          team: 'mithila',
          teamLabel: 'मिथिला',
          img: 'assets/games/char_janak.jpg',
          avatar: 'assets/games/avatar_janak.jpg',
          desc: 'मिथिला के विदेह राजा, ब्रह्मज्ञानी और माता सीता के पिता।'
        },
        {
          id: 'manthara',
          name: 'मंथरा',
          team: 'ayodhya',
          teamLabel: 'अयोध्या',
          img: 'assets/games/char_manthara.jpg',
          avatar: 'assets/games/avatar_manthara.jpg',
          desc: 'रानी कैकेयी की कुबड़ी दासी, जिसने राम के वनवास की योजना बनाई।'
        },
        {
          id: 'sita',
          name: 'सीता',
          team: 'mithila',
          teamLabel: 'मिथिला',
          img: 'assets/games/char_sita.jpg',
          avatar: 'assets/games/avatar_sita.jpg',
          desc: 'जनकनन्दिनी, मिथिला की राजकुमारी और मर्यादा पुरुषोत्तम श्री राम की धर्मपत्नी।'
        },
        {
          id: 'shatrughna',
          name: 'शत्रुघ्न',
          team: 'ayodhya',
          teamLabel: 'अयोध्या',
          img: 'assets/games/char_shatrughna.jpg',
          avatar: 'assets/games/char_shatrughna.jpg',
          desc: 'दशरथ और सुमित्रा के सबसे छोटे पुत्र, लवणवध कर्ता।'
        },
        {
          id: 'urmila',
          name: 'उर्मिला',
          team: 'mithila',
          teamLabel: 'मिथिला',
          img: 'assets/games/char_urmila.jpg',
          avatar: 'assets/games/avatar_urmila.jpg',
          desc: 'लक्ष्मण की पत्नी। राजा जनक और रानी सुनयना की पुत्री।'
        },
        {
          id: 'kaikeyi',
          name: 'कैकेयी',
          team: 'ayodhya',
          teamLabel: 'अयोध्या',
          img: 'assets/games/card_kaikeyi.jpg',
          avatar: 'assets/games/avatar_kaikeyi.jpg',
          desc: 'दशरथ की दूसरी रानी, भरत की माता।'
        },
        {
          id: 'mandavi',
          name: 'मांडवी',
          team: 'mithila',
          teamLabel: 'मिथिला',
          img: 'assets/games/avatar_mandavi.jpg',
          avatar: 'assets/games/avatar_mandavi.jpg',
          desc: 'राजा जनक के अनुज कुशध्वज की पुत्री, धर्मात्मा भरत की धर्मपत्नी।'
        },
        {
          id: 'shrutakirti',
          name: 'श्रुतकीर्ति',
          team: 'mithila',
          teamLabel: 'मिथिला',
          img: 'assets/games/avatar_shrutakirti.jpg',
          avatar: 'assets/games/avatar_shrutakirti.jpg',
          desc: 'कुशध्वज की कनिष्ठ पुत्री, पराक्रमी शत्रुघ्न की धर्मपत्नी।'
        },
        {
          id: 'kushadhwaja',
          name: 'कुशध्वज',
          team: 'mithila',
          teamLabel: 'मिथिला',
          img: 'assets/games/avatar_kushadhwaja.jpg',
          avatar: 'assets/games/avatar_kushadhwaja.jpg',
          desc: 'राजा जनक के छोटे भाई, सांकाश्य नगर के नरेश।'
        },
        {
          id: 'kaushalya',
          name: 'कौशल्या',
          team: 'ayodhya',
          teamLabel: 'अयोध्या',
          img: 'assets/games/avatar_kaushalya.jpg',
          avatar: 'assets/games/avatar_kaushalya.jpg',
          desc: 'अयोध्या की पट्टमहिषी, मर्यादा पुरुषोत्तम श्री राम की ममतामयी माता।'
        },
        {
          id: 'sumitra',
          name: 'सुमित्रा',
          team: 'ayodhya',
          teamLabel: 'अयोध्या',
          img: 'assets/games/avatar_sumitra.jpg',
          avatar: 'assets/games/avatar_sumitra.jpg',
          desc: 'अयोध्या नरेश दशरथ की रानी, लक्ष्मण और शत्रुघ्न की माता।'
        }
      ]
    },
    pandav_kaurav: {
      id: 'pandav_kaurav',
      name: 'पाण्डव या कौरव',
      instruction: 'पाण्डव या कौरव के पक्ष की ओर स्वाइप करें',
      leftTeam: { id: 'pandav', name: 'पाण्डव', scoreClass: 'score-ayodhya', portalImg: 'assets/games/portal_ayodhya.jpg' },
      rightTeam: { id: 'kaurav', name: 'कौरव', scoreClass: 'score-mithila', portalImg: 'assets/games/portal_mithila.jpg' },
      characters: [
        { id: 'arjun', name: 'अर्जुन', team: 'pandav', teamLabel: 'पाण्डव', img: 'assets/gallery/bal_rama.jpg', avatar: 'assets/gallery/bal_rama_little.jpg', desc: 'गाण्डीवधारी, कुंतीपुत्र और भगवान श्री कृष्ण के परम सखा।' },
        { id: 'duryodhan', name: 'दुर्योधन', team: 'kaurav', teamLabel: 'कौरव', img: 'assets/games/char_janak.jpg', avatar: 'assets/games/avatar_janak.jpg', desc: 'हस्तिनापुर के धृतराष्ट्र के ज्येष्ठ पुत्र, कौरव सेनापति।' },
        { id: 'bheem', name: 'भीमसेन', team: 'pandav', teamLabel: 'पाण्डव', img: 'assets/gallery/bal_hanuman.jpg', avatar: 'assets/gallery/bal_hanuman.jpg', desc: 'दस हज़ार हाथियों का बल रखने वाले, गदायुद्ध में निष्णात।' },
        { id: 'karna', name: 'सूर्यपुत्र कर्ण', team: 'kaurav', teamLabel: 'कौरव', img: 'assets/gallery/bal_surya_little.jpg', avatar: 'assets/gallery/bal_surya_little.jpg', desc: 'दानवीर महारथी, अंगराज और दुर्योधन के अभिन्न मित्र।' },
        { id: 'yudhisthir', name: 'धर्मराज युधिष्ठिर', team: 'pandav', teamLabel: 'पाण्डव', img: 'assets/games/char_janak.jpg', avatar: 'assets/games/avatar_janak.jpg', desc: 'सत्यवादी धर्मराज, पाण्डवों में सबसे बड़े भ्राता।' },
        { id: 'shakuni', name: 'शकुनि मामा', team: 'kaurav', teamLabel: 'कौरव', img: 'assets/games/char_manthara.jpg', avatar: 'assets/games/avatar_manthara.jpg', desc: 'गांधार नरेश, पांसों के खेल में निपुण कौरवों के सलाहकार।' }
      ]
    }
  };

  // ══════════════════════════════════════════════════════════════════════════════
  // 2. SWIPE GAME LOGIC & TOUCH PHYSICS
  // ══════════════════════════════════════════════════════════════════════════════
  var activeCardEl = null;
  var isDragging = false;
  var startX = 0;
  var startY = 0;
  var currentX = 0;
  var currentY = 0;

  function initSwipeGame(categoryKey) {
    var cat = SWIPE_CATEGORIES[categoryKey] || SWIPE_CATEGORIES.ayodhya_mithila;
    epicGameState.currentCategory = cat.id;
    epicGameState.ayodhyaScore = 0;
    epicGameState.mithilaScore = 0;
    epicGameState.currentIndex = 0;
    epicGameState.correctCount = 0;
    epicGameState.swipedHistory = [];

    // Shuffle characters for replayability
    var list = cat.characters.slice();
    for (var i = list.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var temp = list[i];
      list[i] = list[j];
      list[j] = temp;
    }
    epicGameState.deck = list;

    // Update Arena labels
    document.getElementById('swipe-instruction').textContent = cat.instruction;
    document.getElementById('swipe-left-portal-label').textContent = cat.leftTeam.name;
    document.getElementById('swipe-right-portal-label').textContent = cat.rightTeam.name;
    document.getElementById('swipe-left-score').textContent = '0';
    document.getElementById('swipe-right-score').textContent = '0';

    renderCurrentCard();
  }

  function renderCurrentCard() {
    var stage = document.getElementById('swipe-card-deck');
    if (!stage) return;

    if (epicGameState.currentIndex >= epicGameState.deck.length) {
      // Round Complete! Transition to Character Review Screen (like in WhatsApp video 56s)
      setTimeout(showCharacterReviewScreen, 400);
      return;
    }

    var char = epicGameState.deck[epicGameState.currentIndex];

    stage.innerHTML = `
      <div class="swipe-card-underlay swipe-card-underlay-2"></div>
      <div class="swipe-card-underlay swipe-card-underlay-1"></div>
      
      <div class="swipe-main-card" id="swipe-active-card">
        <div class="swipe-card-jewel-top"></div>
        <div class="swipe-card-jewel-left"></div>
        <div class="swipe-card-jewel-right"></div>
        <img src="${char.img}" alt="${char.name}" class="swipe-char-portrait" onerror="this.src='assets/games/char_sunaina.jpg';">
        <div class="swipe-char-name-bar">${char.name}</div>
      </div>
    `;

    activeCardEl = document.getElementById('swipe-active-card');
    attachDragListeners(activeCardEl);
  }

  function attachDragListeners(el) {
    if (!el) return;

    el.onpointerdown = function (e) {
      isDragging = true;
      startX = e.clientX;
      startY = e.clientY;
      currentX = startX;
      currentY = startY;
      el.classList.add('dragging');
      el.setPointerCapture(e.pointerId);
    };

    el.onpointermove = function (e) {
      if (!isDragging) return;
      currentX = e.clientX;
      currentY = e.clientY;
      var dx = currentX - startX;
      var dy = currentY - startY;

      // Rotate card slightly with drag
      var rotate = dx * 0.08;
      el.style.transform = `translate(${dx}px, ${dy}px) rotate(${rotate}deg)`;

      // Highlight target portals
      var leftPortal = document.getElementById('swipe-portal-left');
      var rightPortal = document.getElementById('swipe-portal-right');

      if (dx < -40) {
        if (leftPortal) leftPortal.classList.add('active-target');
        if (rightPortal) rightPortal.classList.remove('active-target');
      } else if (dx > 40) {
        if (rightPortal) rightPortal.classList.add('active-target');
        if (leftPortal) leftPortal.classList.remove('active-target');
      } else {
        if (leftPortal) leftPortal.classList.remove('active-target');
        if (rightPortal) rightPortal.classList.remove('active-target');
      }
    };

    el.onpointerup = function (e) {
      if (!isDragging) return;
      isDragging = false;
      el.classList.remove('dragging');
      try { el.releasePointerCapture(e.pointerId); } catch (err) {}

      var dx = currentX - startX;
      var leftPortal = document.getElementById('swipe-portal-left');
      var rightPortal = document.getElementById('swipe-portal-right');
      if (leftPortal) leftPortal.classList.remove('active-target');
      if (rightPortal) rightPortal.classList.remove('active-target');

      // Swipe Threshold: 70px
      if (dx < -70) {
        handleSwipeCommit('left');
      } else if (dx > 70) {
        handleSwipeCommit('right');
      } else {
        // Spring back to center
        el.style.transition = 'transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
        el.style.transform = 'translate(0px, 0px) rotate(0deg)';
      }
    };
  }

  function handleSwipeCommit(direction) {
    var char = epicGameState.deck[epicGameState.currentIndex];
    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var chosenTeam = direction === 'left' ? cat.leftTeam.id : cat.rightTeam.id;
    var isCorrect = (chosenTeam === char.team);

    playSound('swipe');

    // Throw animation
    if (activeCardEl) {
      activeCardEl.style.transition = 'transform 0.3s ease-out, opacity 0.3s ease-out';
      var throwX = direction === 'left' ? -380 : 380;
      var throwY = 160;
      activeCardEl.style.transform = `translate(${throwX}px, ${throwY}px) rotate(${direction === 'left' ? -30 : 30}deg) scale(0.4)`;
      activeCardEl.style.opacity = '0';
    }

    setTimeout(function () {
      if (isCorrect) {
        playSound('correct');
        epicGameState.correctCount++;
        addCoins(50);

        // Update portal counter
        if (chosenTeam === cat.leftTeam.id) {
          epicGameState.ayodhyaScore++;
          var sEl = document.getElementById('swipe-left-score');
          if (sEl) sEl.textContent = epicGameState.ayodhyaScore;
        } else {
          epicGameState.mithilaScore++;
          var sEl = document.getElementById('swipe-right-score');
          if (sEl) sEl.textContent = epicGameState.mithilaScore;
        }

        // Floating Toast
        showCoinToast('+50 🪙');
      } else {
        playSound('wrong');
        showCoinToast('गलत पक्ष!');
      }

      epicGameState.swipedHistory.push({
        character: char,
        chosenTeam: chosenTeam,
        isCorrect: isCorrect
      });

      epicGameState.currentIndex++;
      renderCurrentCard();
    }, 280);
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

  // ══════════════════════════════════════════════════════════════════════════════
  // 3. CHARACTER REVIEW SCREEN (frame_018_71s.jpg & frame_020_79s.jpg)
  // ══════════════════════════════════════════════════════════════════════════════
  function showCharacterReviewScreen() {
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'none';

    var rev = document.getElementById('swipe-review-arena');
    if (!rev) return;
    rev.style.display = 'flex';

    var cat = SWIPE_CATEGORIES[epicGameState.currentCategory];
    var characters = cat.characters;

    // Render tokens list in bottom rail
    var rail = document.getElementById('swipe-review-tokens-rail');
    if (rail) {
      rail.innerHTML = '';
      characters.forEach(function (c, idx) {
        var token = document.createElement('div');
        token.className = 'swipe-char-token' + (idx === 0 ? ' active-token' : '');
        token.innerHTML = `
          <div class="swipe-token-circle">
            <img src="${c.avatar || c.img}" alt="${c.name}" class="swipe-token-avatar" onerror="this.src='assets/games/char_sunaina.jpg';">
            <div class="swipe-token-check">✓</div>
          </div>
          <div class="swipe-token-label">${c.name}</div>
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

    card.innerHTML = `
      <div class="swipe-review-card">
        <div class="swipe-review-img-wrap">
          <img src="${char.img}" alt="${char.name}" class="swipe-review-img" onerror="this.src='assets/games/char_sunaina.jpg';">
          <div class="swipe-review-team-badge">${char.teamLabel}</div>
        </div>
        <div class="swipe-review-info-body">
          <div class="swipe-review-char-name">${char.name}</div>
          <div class="swipe-review-divider"></div>
          <div class="swipe-review-char-desc">${char.desc}</div>
          <button class="swipe-review-network-btn" onclick="window.openCharacterNetworkModal('${char.id}')">📖 नेटवर्क देखें</button>
        </div>
      </div>
    `;
  }

  // ══════════════════════════════════════════════════════════════════════════════
  // 4. RESULT / TRY AGAIN MODAL (frame_84s.jpg)
  // ══════════════════════════════════════════════════════════════════════════════
  function showSwipeResultModal() {
    var modal = document.getElementById('swipe-result-modal');
    if (!modal) return;

    var total = epicGameState.deck.length;
    var correct = epicGameState.correctCount;
    var isVictory = correct >= Math.floor(total * 0.7);

    if (isVictory) playSound('victory');

    document.getElementById('swipe-result-ribbon-text').textContent = isVictory ? 'शानदार विजय!' : 'TRY AGAIN';
    document.getElementById('swipe-result-score-text').textContent = `आपने पूरे किए ${correct}/${total} पात्र`;
    document.getElementById('swipe-result-streak-count').textContent = correct;
    document.getElementById('swipe-result-heading').textContent = isVictory ? 'अद्भुत ज्ञान!' : 'बढ़िया प्रयास!';
    document.getElementById('swipe-result-message').textContent = isVictory ? 'आपने सभी पात्रों को उनके सही पक्ष में पहुँचाया।' : 'कुछ पात्रों को एक और कोशिश चाहिए।';

    modal.style.display = 'flex';
  }

  function hideSwipeResultModal() {
    var modal = document.getElementById('swipe-result-modal');
    if (modal) modal.style.display = 'none';
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

  // ── Game 2: Bhakti Jodi Milao (Bhakti Card Match with Levels) ──
  var allIcons = ['🕉️', '🪔', '📿', '🌸', '🔱', '🥥', '🦚', '🪷'];
  
  // Levels configuration
  var levels = [
    { level: 1, name: "Sugam", pairs: 4 },
    { level: 2, name: "Madhyam", pairs: 6 },
    { level: 3, name: "Kathin", pairs: 8 }
  ];

  var currentLevelIndex = 0;
  var flippedCards = [];
  var matchedCount = 0;
  var moves = 0;
  var lockBoard = false;

  function shuffle(array) {
    return array.slice().sort(function () { return Math.random() - 0.5; });
  }

  function startLevel(lvlIndex) {
    currentLevelIndex = lvlIndex;
    var currentLevel = levels[currentLevelIndex];
    
    var grid = document.getElementById('grid');
    var levelDisplay = document.getElementById('level-display');
    var movesText = document.getElementById('moves');
    var matchesText = document.getElementById('matches');
    var totalMatchesText = document.getElementById('total-matches');
    var modal = document.getElementById('modal');

    if (grid) grid.innerHTML = '';
    flippedCards = [];
    matchedCount = 0;
    moves = 0;
    lockBoard = false;
    
    if (levelDisplay) levelDisplay.innerText = currentLevel.level + " (" + currentLevel.name + ")";
    if (movesText) movesText.innerText = moves;
    if (matchesText) matchesText.innerText = matchedCount;
    if (totalMatchesText) totalMatchesText.innerText = currentLevel.pairs;
    if (modal) modal.style.display = 'none';

    // Select icons for current level
    var selectedIcons = allIcons.slice(0, currentLevel.pairs);
    var cardDeck = shuffle(selectedIcons.concat(selectedIcons));

    cardDeck.forEach(function (icon) {
      var card = document.createElement('div');
      card.classList.add('card');
      card.dataset.icon = icon;

      card.innerHTML = 
        '<div class="card-face card-back">ॐ</div>' +
        '<div class="card-face card-front">' + icon + '</div>';

      card.addEventListener('click', flipCard);
      if (grid) grid.appendChild(card);
    });
  }

  function flipCard() {
    if (lockBoard) return;
    if (this === flippedCards[0]) return;
    if (this.classList.contains('flipped')) return;

    if (typeof playSound === 'function') playSound('swipe');
    this.classList.add('flipped');
    flippedCards.push(this);

    if (flippedCards.length === 2) {
      moves++;
      var movesText = document.getElementById('moves');
      if (movesText) movesText.innerText = moves;
      checkMatch();
    }
  }

  function checkMatch() {
    var card1 = flippedCards[0];
    var card2 = flippedCards[1];
    var isMatch = card1.dataset.icon === card2.dataset.icon;

    if (isMatch) {
      if (typeof playSound === 'function') playSound('correct');
      if (typeof addCoins === 'function') addCoins(25);
      matchedCount++;
      var matchesText = document.getElementById('matches');
      if (matchesText) matchesText.innerText = matchedCount;
      flippedCards = [];

      if (matchedCount === levels[currentLevelIndex].pairs) {
        setTimeout(handleLevelComplete, 500);
      }
    } else {
      if (typeof playSound === 'function') playSound('wrong');
      lockBoard = true;
      setTimeout(function () {
        card1.classList.remove('flipped');
        card2.classList.remove('flipped');
        flippedCards = [];
        lockBoard = false;
      }, 750);
    }
  }

  function handleLevelComplete() {
    if (typeof playSound === 'function') playSound('victory');
    if (typeof addCoins === 'function') addCoins(100);
    var modal = document.getElementById('modal');
    var modalTitle = document.getElementById('modal-title');
    var modalDesc = document.getElementById('modal-desc');
    var modalBtn = document.getElementById('modal-btn');

    if (!modal) return;

    if (currentLevelIndex < levels.length - 1) {
      if (modalTitle) modalTitle.innerText = "Level Puru Thayu! 🎉";
      if (modalDesc) modalDesc.innerText = "Tame " + moves + " moves ma aa charan puru karyu. Have aagalna level ma vadho.";
      if (modalBtn) modalBtn.innerText = "Pachhina Level Par Jao";
    } else {
      if (modalTitle) modalTitle.innerText = "Sampurna Vijayi! 🏆";
      if (modalDesc) modalDesc.innerText = "Tame badha j devotional levels safaltapurvak pura kari lidha!";
      if (modalBtn) modalBtn.innerText = "Fari Thi Sharu Karo";
    }
    modal.style.display = 'flex';
  }

  function nextAction() {
    if (currentLevelIndex < levels.length - 1) {
      startLevel(currentLevelIndex + 1);
    } else {
      startLevel(0);
    }
  }

  window.startLevel = startLevel;
  window.nextAction = nextAction;
  window.initMatchGame = function () { startLevel(0); };

  // ── Game 3: JigSaw (Bhakti Jigsaw Puzzle - 50 Sacred Levels with Boss Levels) ──
  function getLevelConfig(lvl) {
    if (lvl === 1) return { cols: 3, rows: 2, isBoss: false }; // 6 boxes
    if (lvl >= 2 && lvl <= 9) return { cols: 3, rows: 3, isBoss: false }; // 9 boxes
    if (lvl === 10) return { cols: 5, rows: 3, isBoss: true }; // 15 boxes Boss
    if (lvl >= 11 && lvl <= 19) return { cols: 4, rows: 3, isBoss: false }; // 12 boxes
    if (lvl === 20) return { cols: 6, rows: 3, isBoss: true }; // 18 boxes Boss
    if (lvl >= 21 && lvl <= 29) return { cols: 5, rows: 3, isBoss: false }; // 15 boxes
    if (lvl === 30) return { cols: 7, rows: 3, isBoss: true }; // 21 boxes Boss
    if (lvl >= 31 && lvl <= 39) return { cols: 6, rows: 3, isBoss: false }; // 18 boxes
    if (lvl === 40) return { cols: 6, rows: 4, isBoss: true }; // 24 boxes Boss
    if (lvl >= 41 && lvl <= 49) return { cols: 5, rows: 4, isBoss: false }; // 20 boxes
    if (lvl === 50) return { cols: 7, rows: 4, isBoss: true }; // 28 boxes Maha Boss
    return { cols: 3, rows: 3, isBoss: false };
  }

  var currentLevel = 1;
  var placedPieces = 0;
  var totalPieces = 6;

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

  function getLevelImage(lvl) {
    return bgImages[(lvl - 1) % bgImages.length];
  }

  function createJigsawPath(w, h, top, right, bottom, left) {
    // Generates organic jigsaw tabs & blanks curve
    var tabSize = Math.min(w, h) * 0.22;
    var p = "M 0 0";

    // Top edge
    if (top !== 0) {
      p += ` L ${w * 0.38} 0`;
      p += ` C ${w * 0.38} ${-top * tabSize}, ${w * 0.62} ${-top * tabSize}, ${w * 0.62} 0`;
    }
    p += ` L ${w} 0`;

    // Right edge
    if (right !== 0) {
      p += ` L ${w} ${h * 0.38}`;
      p += ` C ${w + right * tabSize} ${h * 0.38}, ${w + right * tabSize} ${h * 0.62}, ${w} ${h * 0.62}`;
    }
    p += ` L ${w} ${h}`;

    // Bottom edge
    if (bottom !== 0) {
      p += ` L ${w * 0.62} ${h}`;
      p += ` C ${w * 0.62} ${h + bottom * tabSize}, ${w * 0.38} ${h + bottom * tabSize}, ${w * 0.38} ${h}`;
    }
    p += " L 0 " + h;

    // Left edge
    if (left !== 0) {
      p += ` L 0 ${h * 0.62}`;
      p += ` C ${-left * tabSize} ${h * 0.62}, ${-left * tabSize} ${h * 0.38}, 0 ${h * 0.38}`;
    }
    p += " Z";
    return p;
  }

  function setPiecePos(el, x, y) {
    el.style.left = x + 'px';
    el.style.top = y + 'px';
  }

  var peekTimer = null;
  function togglePeek() {
    var guideImg = document.getElementById('puzzle-guide-image');
    if (!guideImg) return;
    if (guideImg.style.opacity === '0.85') {
      guideImg.style.opacity = '0.18';
      if (peekTimer) clearTimeout(peekTimer);
    } else {
      guideImg.style.opacity = '0.85';
      if (typeof showToast === 'function') showToast('👁️ दिव्य दर्शन: संकेत 3 सेकंड सक्रिय');
      if (peekTimer) clearTimeout(peekTimer);
      peekTimer = setTimeout(function() {
        if (guideImg) guideImg.style.opacity = '0.18';
      }, 3000);
    }
  }

  function initLevel(lvl) {
    currentLevel = lvl;
    placedPieces = 0;

    var board = document.getElementById('puzzle-board');
    var tray = document.getElementById('puzzle-tray-area');
    var guideImg = document.getElementById('puzzle-guide-image');
    if (!board || !tray || !guideImg) return;

    // Board clear
    board.querySelectorAll('.jigsaw-piece').forEach(function(e) { e.remove(); });
    tray.querySelectorAll('.jigsaw-piece').forEach(function(e) { e.remove(); });
    tray.innerHTML = '';
    var winModal = document.getElementById('winModal');
    if (winModal) winModal.style.display = 'none';

    var cfg = getLevelConfig(lvl);
    totalPieces = cfg.cols * cfg.rows;

    // Header updates
    var titleEl = document.getElementById('level-title');
    if (titleEl) titleEl.innerText = `स्तर ${lvl} / 50`;
    var countEl = document.getElementById('pieces-count');
    if (countEl) countEl.innerText = `खण्ड: ${totalPieces} (${cfg.cols}x${cfg.rows})`;
    var bossEl = document.getElementById('boss-container');
    if (bossEl) {
      bossEl.innerHTML = cfg.isBoss 
        ? `<span class="boss-badge">🔥 BOSS LEVEL</span>` 
        : '';
    }

    // Board Dimensions
    var maxW = Math.min(window.innerWidth * 0.88, 360);
    var cellW = Math.floor(maxW / cfg.cols);
    var cellH = cellW;
    var boardW = cellW * cfg.cols;
    var boardH = cellH * cfg.rows;

    board.style.width = boardW + 'px';
    board.style.height = boardH + 'px';

    var currentImgUrl = bgImages[(lvl - 1) % bgImages.length];
    guideImg.src = currentImgUrl;
    guideImg.style.opacity = '0.18';

    // Compute tabs
    var hTabs = Array.from({length: cfg.rows}, function() {
      return Array.from({length: cfg.cols - 1}, function() { return Math.random() < 0.5 ? 1 : -1; });
    });
    var vTabs = Array.from({length: cfg.rows - 1}, function() {
      return Array.from({length: cfg.cols}, function() { return Math.random() < 0.5 ? 1 : -1; });
    });

    var pieces = [];

    for (var r = 0; r < cfg.rows; r++) {
      for (var c = 0; c < cfg.cols; c++) {
        var top = r === 0 ? 0 : -vTabs[r - 1][c];
        var right = c === cfg.cols - 1 ? 0 : hTabs[r][c];
        var bottom = r === cfg.rows - 1 ? 0 : vTabs[r][c];
        var left = c === 0 ? 0 : -hTabs[r][c - 1];

        var path = createJigsawPath(cellW, cellH, top, right, bottom, left);
        var pad = cellW * 0.35;
        var svgW = cellW + pad * 2;
        var svgH = cellH + pad * 2;

        var targetX = c * cellW;
        var targetY = r * cellH;

        var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("class", "jigsaw-piece");
        svg.setAttribute("width", svgW);
        svg.setAttribute("height", svgH);
        svg.style.width = svgW + "px";
        svg.style.height = svgH + "px";

        var clipId = `clip_${lvl}_${r}_${c}`;
        svg.innerHTML = `
          <defs>
            <clipPath id="${clipId}">
              <path d="${path}" transform="translate(${pad}, ${pad})" />
            </clipPath>
          </defs>
          <g clip-path="url(#${clipId})">
            <image href="${currentImgUrl}" x="${-targetX + pad}" y="${-targetY + pad}" width="${boardW}" height="${boardH}" preserveAspectRatio="none"/>
          </g>
          <path d="${path}" transform="translate(${pad}, ${pad})" fill="none" stroke="rgba(255,215,0,0.85)" stroke-width="1.8" />
        `;

        pieces.push({ svg: svg, targetX: targetX - pad, targetY: targetY - pad, snapDist: cellW * 0.35, pad: pad, cellW: cellW, cellH: cellH });
      }
    }

    // Shuffle pieces into bottom tray
    pieces.sort(function() { return Math.random() - 0.5; }).forEach(function(p, idx) {
      board.appendChild(p.svg);
      // Initially set scattered or tray positions
      p.svg.style.left = (idx * 25) + 'px';
      p.svg.style.top = (boardH + 20) + 'px';
      setupDrag(p.svg, p.targetX, p.targetY, p.snapDist);
    });
  }

  function setupDrag(el, correctX, correctY, snapDist) {
    var startX, startY, origX, origY;
    var isDraggingPiece = false;

    function onPointerDown(e) {
      if (isDraggingPiece) return;
      if (el.classList.contains('locked')) return;

      isDraggingPiece = true;
      var evt = e.touches ? e.touches[0] : e;
      startX = evt.clientX;
      startY = evt.clientY;
      origX = parseFloat(el.style.left) || 0;
      origY = parseFloat(el.style.top) || 0;

      el.style.zIndex = 100;
      if (e.pointerId && el.setPointerCapture) {
        try { el.setPointerCapture(e.pointerId); } catch (err) {}
      }

      window.addEventListener('pointermove', onPointerMove);
      window.addEventListener('pointerup', onPointerUp);
      window.addEventListener('touchmove', onPointerMove, { passive: false });
      window.addEventListener('touchend', onPointerUp);
    }

    function onPointerMove(e) {
      if (!isDraggingPiece) return;
      if (e.preventDefault && e.cancelable) e.preventDefault();

      var evt = e.touches ? e.touches[0] : e;
      var dx = evt.clientX - startX;
      var dy = evt.clientY - startY;
      el.style.left = (origX + dx) + 'px';
      el.style.top = (origY + dy) + 'px';
    }

    function onPointerUp(e) {
      if (!isDraggingPiece) return;
      isDraggingPiece = false;

      window.removeEventListener('pointermove', onPointerMove);
      window.removeEventListener('pointerup', onPointerUp);
      window.removeEventListener('touchmove', onPointerMove);
      window.removeEventListener('touchend', onPointerUp);

      if (e.pointerId && el.releasePointerCapture) {
        try { el.releasePointerCapture(e.pointerId); } catch (err) {}
      }

      var currX = parseFloat(el.style.left) || 0;
      var currY = parseFloat(el.style.top) || 0;
      var dist = Math.hypot(currX - correctX, currY - correctY);

      // Snapping mechanism
      if (dist < snapDist) {
        el.style.left = correctX + 'px';
        el.style.top = correctY + 'px';
        el.classList.add('locked');
        el.style.zIndex = 10;
        if (typeof playSound === 'function') playSound('correct');
        placedPieces++;

        if (placedPieces === totalPieces) {
          if (typeof playSound === 'function') playSound('victory');
          var cfg = getLevelConfig(currentLevel);
          var bonusCoins = cfg.isBoss ? 250 : 100;
          if (typeof addCoins === 'function') addCoins(bonusCoins);
          setTimeout(onLevelComplete, 400);
        }
      } else {
        el.style.zIndex = 20;
        if (typeof playSound === 'function') playSound('swipe');
      }
    }

    el.addEventListener('pointerdown', onPointerDown);
    el.addEventListener('touchstart', onPointerDown, { passive: true });
  }

  function onLevelComplete() {
    var modal = document.getElementById('winModal');
    var heading = document.getElementById('win-heading');
    var desc = document.getElementById('win-desc');
    var badge = document.getElementById('win-coins-badge');

    var cfg = getLevelConfig(currentLevel);
    var coinsEarned = cfg.isBoss ? 250 : 100;
    if (badge) badge.innerText = `+${coinsEarned} 🪙 सिक्के अर्जित किए!`;

    if (currentLevel >= 50) {
      if (heading) heading.innerText = "महा विजय! 🏆";
      if (desc) desc.innerText = "आपने सभी 50 भक्ति स्तर सफलतापूर्वक पूर्ण कर लिए!";
    } else {
      if (heading) heading.innerText = cfg.isBoss ? "बॉस स्तर पराजित! 🔱" : "दिव्य दर्शन पूर्ण! 🌸";
      if (desc) desc.innerText = `स्तर ${currentLevel} पूर्ण! अगले दिव्य स्तर के लिए आगे बढ़ें।`;
    }
    if (modal) modal.style.display = 'flex';
  }

  function nextLevel() {
    if (currentLevel < 50) {
      initLevel(currentLevel + 1);
    } else {
      initLevel(1);
    }
  }

  function prevLevel() {
    if (currentLevel > 1) {
      initLevel(currentLevel - 1);
    } else {
      initLevel(50);
    }
  }

  function resetCurrentLevel() {
    initLevel(currentLevel);
  }

  // ── Game 4: PadaBandham (Word Grid) ──
  var PADA_WORDS = [
    { word: 'राम', chars: ['रा', 'म'], deity: 'श्री राम', img: 'assets/deity_ram.jpg' },
    { word: 'कृष्ण', chars: ['कृ', 'ष्ण'], deity: 'श्री कृष्ण', img: 'assets/deity_krishna.jpg' },
    { word: 'शिव', chars: ['शि', 'व'], deity: 'महादेव शिव', img: 'assets/deity_shiva.jpg' },
    { word: 'गणेश', chars: ['ग', 'णे', 'श'], deity: 'श्री गणेश', img: 'assets/deity_ganesh.jpg' },
    { word: 'हनुमान', chars: ['ह', 'नु', 'मा', 'न'], deity: 'श्री हनुमान', img: 'assets/deity_hanuman.jpg' },
    { word: 'दुर्गा', chars: ['दु', 'र्गा'], deity: 'माँ दुर्गा', img: 'assets/deity_durga_hd.jpg' },
    { word: 'श्याम', chars: ['श्या', 'म'], deity: 'खाटू श्याम', img: 'assets/deity_khatushyam.jpg' }
  ];
  var foundWords = [];
  var currentSelectedCells = [];

  var PADA_LETTERS = [
    'रा', 'म', 'ॐ', 'शि',
    'कृ', 'ष्ण', 'व', 'ह',
    'ग', 'णे', 'श', 'नु',
    'दु', 'र्गा', 'श्या', 'म'
  ];

  function initPadabandhamGame() {
    foundWords = [];
    currentSelectedCells = [];
    var statusEl = document.getElementById('padabandham-status');
    if (statusEl) statusEl.textContent = 'अक्षरों को क्रम में स्पर्श करें...';
    renderPadabandham();
  }

  function renderPadabandham() {
    var targetsEl = document.getElementById('padabandham-word-targets') || document.getElementById('padabandham-word-list');
    if (targetsEl) {
      targetsEl.innerHTML = PADA_WORDS.map(function (item) {
        var isFound = foundWords.includes(item.word);
        return `<span style="display:inline-flex; align-items:center; gap:6px; background:${isFound ? '#10B981' : 'rgba(255,255,255,0.08)'}; color:${isFound ? '#FFF' : '#FDE68A'}; border:1px solid ${isFound ? '#34D399' : 'rgba(245,158,11,0.3)'}; padding:5px 12px; border-radius:14px; font-weight:800; font-size:0.82rem; transition:all 0.3s ease;"><img src="${item.img}" style="width:20px; height:20px; border-radius:50%; object-fit:cover;"> ${item.word} ${isFound ? '✓' : ''}</span>`;
      }).join(' ');
    }

    var gridEl = document.getElementById('padabandham-grid');
    if (gridEl) {
      gridEl.innerHTML = '';
      PADA_LETTERS.forEach(function (char, idx) {
        var cell = document.createElement('div');
        var isSel = currentSelectedCells.includes(idx);
        cell.className = 'padabandham-cell';
        cell.style.cssText = `background:${isSel ? 'linear-gradient(135deg, #F59E0B, #D97706)' : 'rgba(255,255,255,0.08)'}; border:1.5px solid ${isSel ? '#FEF3C7' : 'rgba(245,158,11,0.25)'}; color:${isSel ? '#1A0B2E' : '#FFFDF8'}; font-size:1.15rem; font-weight:900; height:56px; display:flex; align-items:center; justify-content:center; border-radius:12px; cursor:pointer; user-select:none; transition:transform 0.15s ease, background 0.2s ease; box-shadow:${isSel ? '0 0 12px rgba(245,158,11,0.6)' : 'none'};`;
        cell.textContent = char;
        cell.onclick = function () { handlePadabandhamTap(idx); };
        gridEl.appendChild(cell);
      });
    }
  }

  function handlePadabandhamTap(idx) {
    if (currentSelectedCells.includes(idx)) {
      currentSelectedCells = currentSelectedCells.filter(function (i) { return i !== idx; });
    } else {
      currentSelectedCells.push(idx);
    }
    renderPadabandham();

    var formedStr = currentSelectedCells.map(function (i) { return PADA_LETTERS[i]; }).join('');
    var statusEl = document.getElementById('padabandham-status');
    if (statusEl) statusEl.textContent = `चयनित: ${formedStr || '...'}`;

    // Check if formed string matches any word
    var matched = PADA_WORDS.find(function (w) {
      return w.chars.join('') === formedStr || w.word === formedStr;
    });

    if (matched && !foundWords.includes(matched.word)) {
      foundWords.push(matched.word);
      playSound('correct');
      currentSelectedCells = [];
      if (statusEl) statusEl.textContent = `🎉 अद्भुत! आपने खोजा: ${matched.word} (${matched.deity})`;
      renderPadabandham();

      if (foundWords.length === PADA_WORDS.length) {
        setTimeout(function () {
          playSound('victory');
          addCoins(200);
          if (statusEl) statusEl.textContent = '🏆 सम्पूर्ण विजय! समस्त पावन नाम खोजे गए! (+200 सिक्के)';
        }, 300);
      }
    }
  }

  // ══════════════════════════════════════════════════════════════════════════════
  // 6. GLOBAL NAVIGATION & EXPOSURE TO WINDOW
  // ══════════════════════════════════════════════════════════════════════════════
  window.openSwipeGame = function (categoryKey) {
    categoryKey = categoryKey || 'ayodhya_mithila';
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'flex';
    initSwipeGame(categoryKey);
  };

  window.closeSwipeGame = function () {
    var arena = document.getElementById('swipe-arena');
    if (arena) arena.style.display = 'none';
  };

  window.closeSwipeReview = function () {
    var rev = document.getElementById('swipe-review-arena');
    if (rev) rev.style.display = 'none';
    showSwipeResultModal();
  };

  window.openMatchGame = function () {
    var modal = document.getElementById('match-game-modal');
    if (modal) {
      modal.classList.add('active');
      modal.classList.add('is-open');
      modal.style.setProperty('display', 'flex', 'important');
      modal.style.setProperty('opacity', '1', 'important');
      modal.style.setProperty('pointer-events', 'auto', 'important');
      modal.style.setProperty('visibility', 'visible', 'important');
    }
    initMatchGame();
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
    var winModal = document.getElementById('modal');
    if (winModal) winModal.style.display = 'none';
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
    var lvl = (typeof levelIdx === 'number' && levelIdx >= 1) ? levelIdx : (currentLevel || 1);
    initLevel(lvl);
  };

  window.closeJigsawGame = function () {
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
    var peekModal = document.getElementById('jigsaw-peek-modal');
    if (peekModal) peekModal.style.display = 'none';
  };

  window.initLevel = initLevel;
  window.nextLevel = nextLevel;
  window.prevLevel = prevLevel;
  window.skipToNextLevel = nextLevel;
  window.resetCurrentLevel = resetCurrentLevel;
  window.togglePeek = togglePeek;
  window.toggleJigsawPreviewModal = togglePeek;

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
    initPadabandhamGame();
  };

  window.closePadabandhamGame = function () {
    var modal = document.getElementById('padabandham-game-modal');
    if (modal) {
      modal.classList.remove('active');
      modal.classList.remove('is-open');
      modal.style.setProperty('display', 'none', 'important');
      modal.style.setProperty('opacity', '0', 'important');
      modal.style.setProperty('pointer-events', 'none', 'important');
    }
  };

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

})();
