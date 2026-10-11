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

  // ── Game 2: Match (Memory Card Game with Rotating Real Deity Images) ──
  var matchFlipped = [];
  var matchMatchedCount = 0;
  var matchMoves = 0;

  function initMatchGame() {
    matchFlipped = [];
    matchMatchedCount = 0;
    matchMoves = 0;
    var movesEl = document.getElementById('match-moves-count');
    if (movesEl) movesEl.textContent = '0';

    // Pick 6 random deities from master pool
    var shuffledPool = ALL_APP_DEITIES.slice();
    for (var p = shuffledPool.length - 1; p > 0; p--) {
      var r = Math.floor(Math.random() * (p + 1));
      var tmp = shuffledPool[p]; shuffledPool[p] = shuffledPool[r]; shuffledPool[r] = tmp;
    }
    var chosen6 = shuffledPool.slice(0, 6);

    // Create 12 cards (6 pairs)
    var cards = chosen6.concat(chosen6);
    // Fisher-Yates shuffle cards
    for (var i = cards.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = cards[i]; cards[i] = cards[j]; cards[j] = t;
    }

    var grid = document.getElementById('match-cards-grid');
    if (!grid) return;
    grid.innerHTML = '';

    cards.forEach(function (item, index) {
      var card = document.createElement('div');
      card.className = 'match-tile';
      card.dataset.id = item.id;
      card.dataset.index = index;
      card.innerHTML = `
        <div class="match-tile-inner">
          <div class="match-tile-back" style="background:linear-gradient(135deg, #3B1259 0%, #1A052E 100%); border:1.8px solid #F59E0B; border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
            <span style="font-size:1.6rem; filter:drop-shadow(0 0 6px #F59E0B);">🕉️</span>
            <span style="font-size:0.6rem; color:#FDE68A; font-weight:800; margin-top:2px;">भक्ति</span>
          </div>
          <div class="match-tile-front" style="background:#FFFDF8; border:2px solid #F59E0B; border-radius:12px; padding:4px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
            <img src="${item.img}" alt="${item.name}" style="width:100%; height:52px; object-fit:cover; border-radius:8px; border:1px solid rgba(245,158,11,0.3);">
            <div class="match-tile-name" style="font-size:0.65rem; font-weight:900; color:#2A0E44; margin-top:2px; text-align:center;">${item.name}</div>
          </div>
        </div>
      `;
      card.onclick = function () { handleMatchCardClick(card, item); };
      grid.appendChild(card);
    });
  }

  function handleMatchCardClick(card, item) {
    if (card.classList.contains('flipped') || card.classList.contains('matched') || matchFlipped.length >= 2) return;

    playSound('swipe');
    card.classList.add('flipped');
    matchFlipped.push({ card: card, item: item });

    if (matchFlipped.length === 2) {
      matchMoves++;
      var movesEl = document.getElementById('match-moves-count');
      if (movesEl) movesEl.textContent = matchMoves;

      var c1 = matchFlipped[0];
      var c2 = matchFlipped[1];

      if (c1.item.id === c2.item.id) {
        playSound('correct');
        c1.card.classList.add('matched');
        c2.card.classList.add('matched');
        matchFlipped = [];
        matchMatchedCount += 2;
        addCoins(25);

        if (matchMatchedCount === 12) {
          setTimeout(function () {
            playSound('victory');
            addCoins(100);
            alert(`🎉 बधाई हो! आपने ${matchMoves} चालों में दिव्य स्मृति खेल पूरा किया!\n+100 🪙 सिक्के अर्जित किए!`);
          }, 400);
        }
      } else {
        playSound('wrong');
        setTimeout(function () {
          c1.card.classList.remove('flipped');
          c2.card.classList.remove('flipped');
          matchFlipped = [];
        }, 800);
      }
    }
  }

  // ── Game 3: JigSaw (Divine Deity Picture Puzzle Game - 18 Sacred Levels) ──
  var JIGSAW_LEVELS = ALL_APP_DEITIES;
  var currentJigsawLevel = 0;
  // Solvable initial layouts for 3x3 sliding tile puzzle
  var JIGSAW_SOLVABLE_STARTS = [
    [1, 2, 3, 4, 0, 5, 7, 8, 6],
    [1, 2, 3, 0, 4, 6, 7, 5, 8],
    [2, 1, 3, 4, 5, 6, 7, 0, 8],
    [1, 3, 0, 4, 2, 5, 7, 8, 6],
    [1, 2, 0, 4, 5, 3, 7, 8, 6],
    [1, 2, 3, 4, 5, 0, 7, 8, 6],
    [1, 0, 3, 4, 2, 5, 7, 8, 6]
  ];
  var jigsawTiles = [1, 2, 3, 4, 0, 5, 7, 8, 6];
  var jigsawMoves = 0;
  var jigsawSolved = false;

  function renderJigsawLevelSelector() {
    var container = document.getElementById('jigsaw-levels-selector');
    if (!container) return;
    container.innerHTML = '';

    JIGSAW_LEVELS.forEach(function (lvl, idx) {
      var pill = document.createElement('div');
      pill.className = 'jigsaw-level-pill' + (idx === currentJigsawLevel ? ' active' : '');
      pill.innerHTML = `<img src="${lvl.img}" alt="${lvl.name}"> <span>${lvl.name}</span>`;
      pill.onclick = function () { switchJigsawLevel(idx); };
      container.appendChild(pill);
    });
  }

  function initJigsawGame() {
    jigsawMoves = 0;
    jigsawSolved = false;
    var movesEl = document.getElementById('jigsaw-moves-count');
    if (movesEl) movesEl.textContent = '0';

    var cur = JIGSAW_LEVELS[currentJigsawLevel];
    var titleEl = document.getElementById('jigsaw-deity-display-name');
    if (titleEl) titleEl.textContent = cur.title;
    var badgeEl = document.getElementById('jigsaw-current-level-badge');
    if (badgeEl) badgeEl.textContent = `स्तर ${currentJigsawLevel + 1}/${JIGSAW_LEVELS.length}`;
    var thumbEl = document.getElementById('jigsaw-target-preview-thumb');
    if (thumbEl) thumbEl.src = cur.img;
    var peekImg = document.getElementById('jigsaw-peek-full-image');
    if (peekImg) peekImg.src = cur.img;
    var victoryImg = document.getElementById('jigsaw-victory-full-img');
    if (victoryImg) victoryImg.src = cur.img;
    var victoryOverlay = document.getElementById('jigsaw-board-victory-overlay');
    if (victoryOverlay) victoryOverlay.style.display = 'none';

    // Pick solvable configuration
    var config = JIGSAW_SOLVABLE_STARTS[currentJigsawLevel % JIGSAW_SOLVABLE_STARTS.length];
    jigsawTiles = config.slice();

    renderJigsawLevelSelector();
    renderJigsawGrid();
  }

  function switchJigsawLevel(idx) {
    if (idx >= 0 && idx < JIGSAW_LEVELS.length) {
      currentJigsawLevel = idx;
      initJigsawGame();
    }
  }

  function nextJigsawLevel() {
    currentJigsawLevel = (currentJigsawLevel + 1) % JIGSAW_LEVELS.length;
    initJigsawGame();
  }

  function toggleJigsawPreviewModal() {
    var modal = document.getElementById('jigsaw-peek-modal');
    if (!modal) return;
    modal.style.display = (modal.style.display === 'flex' ? 'none' : 'flex');
  }

  function renderJigsawGrid() {
    var grid = document.getElementById('jigsaw-grid');
    if (!grid) return;
    grid.innerHTML = '';
    var cur = JIGSAW_LEVELS[currentJigsawLevel];

    jigsawTiles.forEach(function (val, idx) {
      var tile = document.createElement('div');
      tile.className = 'jigsaw-tile' + (val === 0 ? ' empty-slot' : '');

      if (val !== 0) {
        var pieceRow = Math.floor((val - 1) / 3);
        var pieceCol = (val - 1) % 3;
        var posX = pieceCol * 50;
        var posY = pieceRow * 50;

        tile.style.backgroundImage = `url("${cur.img}")`;
        tile.style.backgroundSize = '300% 300%';
        tile.style.backgroundPosition = `${posX}% ${posY}%`;
        tile.innerHTML = `<span class="jigsaw-tile-badge">${val}</span>`;
        tile.onclick = function () { moveJigsawTile(idx); };
      } else {
        tile.innerHTML = `
          <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; height:100%; color:rgba(245,158,11,0.5); font-size:0.75rem; font-weight:800;">
            <span>🪷</span>
            <span>खाली</span>
          </div>
        `;
      }
      grid.appendChild(tile);
    });
  }

  function moveJigsawTile(idx) {
    if (jigsawSolved) return;
    var emptyIdx = jigsawTiles.indexOf(0);
    var r1 = Math.floor(idx / 3), c1 = idx % 3;
    var r2 = Math.floor(emptyIdx / 3), c2 = emptyIdx % 3;

    if (Math.abs(r1 - r2) + Math.abs(c1 - c2) === 1) {
      playSound('swipe');
      jigsawTiles[emptyIdx] = jigsawTiles[idx];
      jigsawTiles[idx] = 0;
      jigsawMoves++;
      var movesEl = document.getElementById('jigsaw-moves-count');
      if (movesEl) movesEl.textContent = jigsawMoves;
      renderJigsawGrid();

      // Check win condition: [1, 2, 3, 4, 5, 6, 7, 8, 0]
      var won = jigsawTiles.every(function (v, i) {
        return (i === 8 && v === 0) || (v === i + 1);
      });

      if (won) {
        jigsawSolved = true;
        setTimeout(function () {
          playSound('victory');
          addCoins(150);
          var victoryOverlay = document.getElementById('jigsaw-board-victory-overlay');
          if (victoryOverlay) victoryOverlay.style.display = 'flex';
        }, 300);
      }
    }
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
    if (typeof levelIdx === 'number') {
      currentJigsawLevel = levelIdx;
    }
    initJigsawGame();
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
  };

  window.switchJigsawLevel = switchJigsawLevel;
  window.nextJigsawLevel = nextJigsawLevel;
  window.toggleJigsawPreviewModal = toggleJigsawPreviewModal;

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
