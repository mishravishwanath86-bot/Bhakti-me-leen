// ══════════════════════════════════════════════════════════════════════════════
// 🏺 BHAKTI AMRIT KALASH — 3D INTERACTIVE & AI VOICE REVEAL ENGINE
// Powered by Three.js WebGL, Web Speech Recognition & Vedic Semantic Matcher
// ══════════════════════════════════════════════════════════════════════════════

window.AMRIT_SHLOKA_DATASET = {
  'anxious': {
    id: 'shloka_anxious',
    mood: 'अशांत / व्याकुल (Anxiety • Overthink)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 2, श्लोक 47)',
    sanskrit: 'कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।\nमा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥',
    hindiMeaning: 'तुम्हारा अधिकार केवल अपने कर्तव्य कर्म पर है, उसके फल पर कभी नहीं। भविष्य के परिणाम की चिंता छोड़कर शांत चित्त से वर्तमान कर्म करो।',
    actionKarma: '2 मिनट आंखें बंद करके गहरी सांस लें और 11 बार ॐ का उच्चारण करके अपनी सारी चिंता प्रभु को समर्पित करें।',
    themeColor: '#EF4444'
  },
  'peace': {
    id: 'shloka_peace',
    mood: 'शांति / ध्यान (Peace • Stillness)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 6, श्लोक 5)',
    sanskrit: 'उद्धरेदात्मनात्मानं नात्मानमवसादयेत्।\nआत्मैव ह्यात्मनो बन्धुरात्मैव रिपुरात्मनः॥',
    hindiMeaning: 'मनुष्य को अपने मन के द्वारा अपना उद्धार करना चाहिए, मन को नीचे न गिरने दे। क्योंकि मन ही मनुष्य का सबसे बड़ा मित्र और मन ही शत्रु है।',
    actionKarma: '5 मिनट मौन रहकर अपने भीतर परमात्मा की उपस्थिति का अनुभव करें और आभार व्यक्त करें।',
    themeColor: '#10B981'
  },
  'sad': {
    id: 'shloka_sad',
    mood: 'निराशा / दुःख (Sadness • Low Energy)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 2, श्लोक 14)',
    sanskrit: 'मात्रास्पर्शास्तु कौन्तेय शीतोष्णसुखदुःखदाः।\nआगमापायिनोऽनित्यास्तांस्तितिक्षस्व भारत॥',
    hindiMeaning: 'हे कुंतीपुत्र! सुख और दुःख सर्दी-गर्मी की तरह आते और जाते रहते हैं। ये अनित्य हैं, अतः धैर्यपूर्वक इन्हें सहन करना सीखो, यह समय भी बीत जाएगा।',
    actionKarma: 'एक गिलास पवित्र जल पिएं और मन में दोहराएं: "यह कठिन समय भी प्रभु कृपा से सुखद बन जाएगा।"',
    themeColor: '#8B5CF6'
  },
  'fear': {
    id: 'shloka_fear',
    mood: 'भय / साहस (Fear • Courage Needed)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 18, श्लोक 66)',
    sanskrit: 'सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज।\nअहं त्वां सर्वपापेभ्यो मोक्षयिष्यामि मा शुचः॥',
    hindiMeaning: 'सब चिंताओं व भयों को त्यागकर केवल मेरी शरण में आ जाओ। मैं तुम्हें समस्त संकटों व भयों से मुक्त कर दूंगा, तनिक भी शोक मत करो।',
    actionKarma: 'श्री हनुमान चालीसा की चौपाई का स्मरण करें: "भूत पिशाच निकट नहिं आवै, महाबीर जब नाम सुनावै।"',
    themeColor: '#F59E0B'
  },
  'grateful': {
    id: 'shloka_grateful',
    mood: 'कृतज्ञ / आनंद (Grateful • Joyful)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 12, श्लोक 15)',
    sanskrit: 'यस्मान्नोद्विजते लोको लोकान्नोद्विजते च यः।\nहर्षामर्षभयोद्वेगैर्मुक्तो यः स च मे प्रियः॥',
    hindiMeaning: 'जिससे किसी को कष्ट नहीं पहुंचता और जो किसी से उद्विग्न नहीं होता, जो हर्ष, अमर्ष और भय से मुक्त है—ऐसा भक्त मुझे अत्यंत प्रिय है।',
    actionKarma: 'आज किसी एक जरूरतमंद या पशु-पक्षी को भोजन अर्पित कर प्रभु के प्रति अपनी कृतज्ञता प्रकट करें।',
    themeColor: '#EC4899'
  },
  'doubt': {
    id: 'shloka_doubt',
    mood: 'अनिर्णय / भ्रम (Doubt • Clarity)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 4, श्लोक 39)',
    sanskrit: 'श्रद्धावाँल्लभते ज्ञानं तत्परः संयतेन्द्रियः।\nज्ञानं लब्ध्वा परां शान्तिमचिरेणाधिगच्छति॥',
    hindiMeaning: 'श्रद्धावान और संयमी मनुष्य ही दिव्य ज्ञान प्राप्त करता है। ज्ञान प्राप्त होते ही सारे संशय और भ्रम मिट जाते हैं तथा परम शांति की प्राप्ति होती है।',
    actionKarma: 'अपने इष्टदेव के सम्मुख 1 दीपक प्रज्वलित कर निर्णय प्रभु की इच्छा पर छोड़ दें, सही मार्ग स्वयं दिखेगा।',
    themeColor: '#3B82F6'
  }
};

window.currentActiveShloka = window.AMRIT_SHLOKA_DATASET['anxious'];

// ══════════════════════════════════════════════════════════════════════════════
// 3D FLOATING GOLDEN KALASH THREE.JS ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.Kalash3D = {
  scene: null,
  camera: null,
  renderer: null,
  kalashGroup: null,
  sparkles: null,
  isTilting: false
};

window.init3DKalashCanvas = function() {
  const container = document.getElementById('kalash-3d-canvas-container');
  if (!container) return;
  
  // If iframe already exists, preserve it!
  const iframe = container.querySelector('iframe');
  if (iframe) return;

  // Render Clean Cropped Viewport (Hiding all Sketchfab corner UI/watermarks)
  container.innerHTML = `
    <div style="position:absolute; inset:-48px -42px -54px -42px; overflow:hidden; pointer-events:auto;">
      <iframe title="Kalash with coconut and marigolds" 
              id="kalash-sketchfab-iframe"
              frameborder="0" 
              allowfullscreen 
              mozallowfullscreen="true" 
              webkitallowfullscreen="true" 
              allow="autoplay; fullscreen; xr-spatial-tracking" 
              xr-spatial-tracking 
              execution-while-out-of-viewport 
              execution-while-not-rendered 
              web-share 
              src="https://sketchfab.com/models/2c56e05aad4b4372a8f2e240398810db/embed?autostart=1&preload=1&transparent=1&ui_theme=dark&ui_controls=0&ui_infos=0&ui_watermark=0&ui_stop=0&ui_hint=0" 
              style="width: 100%; height: 100%; border: none; transform: scale(1.12); transform-origin: center center;">
      </iframe>
    </div>
    <div style="position:absolute; top:0; left:0; width:80px; height:80px; background:radial-gradient(circle at 0% 0%, #1A052E 55%, transparent 100%); pointer-events:none; z-index:5;"></div>
    <div style="position:absolute; top:0; right:0; width:80px; height:80px; background:radial-gradient(circle at 100% 0%, #1A052E 55%, transparent 100%); pointer-events:none; z-index:5;"></div>
    <div style="position:absolute; bottom:0; left:0; width:85px; height:80px; background:radial-gradient(circle at 0% 100%, #1A052E 60%, transparent 100%); pointer-events:none; z-index:5;"></div>
    <div style="position:absolute; bottom:0; right:0; width:140px; height:70px; background:radial-gradient(circle at 100% 100%, #1A052E 70%, transparent 100%); pointer-events:none; z-index:5;"></div>
    <div id="kalash-touch-shield" style="position:absolute; inset:0; z-index:10; cursor:pointer;" onclick="trigger3DKalashInteraction()"></div>
  `;
};

function animate3DKalash() {
  window.kalash3DAnimFrame = requestAnimationFrame(animate3DKalash);

  const K = window.Kalash3D;
  if (!K.renderer || !K.scene || !K.camera) return;

  // Gentle Floating & Rotation
  if (K.kalashGroup && !K.isTilting) {
    K.kalashGroup.rotation.y += 0.008;
    K.kalashGroup.position.y = -0.2 + Math.sin(Date.now() * 0.002) * 0.08;
  }

  if (K.sparkles) {
    K.sparkles.rotation.y += 0.004;
  }

  K.renderer.render(K.scene, K.camera);
}

// ══════════════════════════════════════════════════════════════════════════════
// INTERACTION: KALASH TILT & BHOJPATRA REVEAL FLOW
// ══════════════════════════════════════════════════════════════════════════════

window.trigger3DKalashInteraction = function() {
  window.tilt3DKalashAndEmitNectar(() => {
    // Pick random wisdom
    const keys = Object.keys(window.AMRIT_SHLOKA_DATASET);
    const randKey = keys[Math.floor(Math.random() * keys.length)];
    window.revealAmritWisdom(randKey);
  });
};

window.tilt3DKalashAndEmitNectar = function(callback) {
  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (typeof playSoundEffect === 'function') playSoundEffect('correct');
  if (navigator.vibrate) navigator.vibrate([40, 60, 40]);

  const iframe = document.getElementById('kalash-sketchfab-iframe');
  if (iframe) {
    iframe.style.transition = 'transform 0.3s ease';
    iframe.style.transform = 'scale(1.05) rotate(-3deg)';
    setTimeout(() => {
      iframe.style.transform = 'scale(1) rotate(0deg)';
      if (callback) callback();
    }, 350);
  } else {
    if (callback) callback();
  }
};

window.revealAmritWisdom = function(moodKey) {
  const shloka = window.AMRIT_SHLOKA_DATASET[moodKey] || window.AMRIT_SHLOKA_DATASET['anxious'];
  window.currentActiveShloka = shloka;

  const sourceTag = document.getElementById('bhojpatra-source-tag');
  const sanskritEl = document.getElementById('bhojpatra-sanskrit-text');
  const hindiEl = document.getElementById('bhojpatra-hindi-meaning');
  const actionEl = document.getElementById('bhojpatra-action-karma');

  if (sourceTag) sourceTag.textContent = shloka.source;
  if (sanskritEl) sanskritEl.innerHTML = shloka.sanskrit.replace(/\n/g, '<br>');
  if (hindiEl) hindiEl.textContent = shloka.hindiMeaning;
  if (actionEl) actionEl.textContent = shloka.actionKarma;

  // Open Bhojpatra Modal
  const modal = document.getElementById('amrit-bhojpatra-modal');
  if (modal) modal.style.display = 'flex';
};

window.closeAmritBhojpatraModal = function() {
  const modal = document.getElementById('amrit-bhojpatra-modal');
  if (modal) modal.style.display = 'none';
};

// ══════════════════════════════════════════════════════════════════════════════
// ══════════════════════════════════════════════════════════════════════════════
// 🎙️ SUPERCHARGED AI VEDIC VOICE GUIDE & SEMANTIC SHLOKA ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.voiceRecognitionInstance = null;
window.isAIVoiceRecording = false;

window.startAIVoiceMoodRecognition = function() {
  const modal = document.getElementById('vedic-ai-voice-modal');
  if (modal) modal.style.display = 'flex';

  window.startListeningSpeechEngine();
};

window.closeAIVoiceModal = function() {
  window.stopListeningSpeechEngine();
  const modal = document.getElementById('vedic-ai-voice-modal');
  if (modal) modal.style.display = 'none';
};

window.toggleSpeechRecording = function() {
  if (window.isAIVoiceRecording) {
    window.stopListeningSpeechEngine();
  } else {
    window.startListeningSpeechEngine();
  }
};

window.startListeningSpeechEngine = function() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const transcriptEl = document.getElementById('vedic-voice-live-transcript');
  const micBtn = document.getElementById('vedic-voice-mic-main-btn');
  const ring = document.getElementById('vedic-voice-pulse-ring');

  if (!SpeechRecognition) {
    if (transcriptEl) {
      transcriptEl.textContent = '💡 माइक समर्थित नहीं है — कृपया नीचे दिए गए 1-टैप भावों में से चुनें या टेक्स्ट लिखें';
      transcriptEl.style.color = '#FDE68A';
    }
    return;
  }

  // Stop any existing instance
  try {
    if (window.voiceRecognitionInstance) {
      window.voiceRecognitionInstance.stop();
    }
  } catch(e) {}

  try {
    const rec = new SpeechRecognition();
    window.voiceRecognitionInstance = rec;
    rec.lang = 'hi-IN';
    rec.continuous = false;
    rec.interimResults = true;

    rec.onstart = function() {
      window.isAIVoiceRecording = true;
      if (transcriptEl) {
        transcriptEl.textContent = '🎙️ सुन रहे हैं... प्रभु से अपनी समस्या या मनोदशा कहें...';
        transcriptEl.style.color = '#34D399';
      }
      if (micBtn) {
        micBtn.style.background = 'linear-gradient(135deg, #10B981 0%, #059669 100%)';
        micBtn.style.boxShadow = '0 0 35px rgba(16,185,129,0.9)';
      }
      if (ring) {
        ring.style.animation = 'pulseGlow 0.8s infinite';
        ring.style.borderColor = '#34D399';
      }
      if (navigator.vibrate) navigator.vibrate(30);
    };

    rec.onresult = function(e) {
      let currentText = '';
      for (let i = e.resultIndex; i < e.results.length; ++i) {
        currentText += e.results[i][0].transcript;
      }
      if (transcriptEl && currentText) {
        transcriptEl.textContent = `"${currentText}"`;
      }

      if (e.results[0] && e.results[0].isFinal) {
        setTimeout(() => {
          window.stopListeningSpeechEngine();
          window.processAIVoiceText(currentText);
        }, 600);
      }
    };

    rec.onerror = function(err) {
      console.warn("Speech recognition error:", err);
      window.isAIVoiceRecording = false;
      if (transcriptEl) {
        transcriptEl.textContent = '⚠️ ध्वनि स्पष्ट नहीं थी, पुनः बोलें या नीचे दिए गए भाव चुनें';
        transcriptEl.style.color = '#FCA5A5';
      }
      resetMicBtnVisuals();
    };

    rec.onend = function() {
      window.isAIVoiceRecording = false;
      resetMicBtnVisuals();
    };

    rec.start();
  } catch(ex) {
    console.error("Speech Recognition Start Error:", ex);
    window.isAIVoiceRecording = false;
    if (transcriptEl) {
      transcriptEl.textContent = '💡 कृपया नीचे दिए गए 1-टैप भावों में से चुनें या टेक्स्ट बॉक्स में लिखें';
    }
    resetMicBtnVisuals();
  }

  function resetMicBtnVisuals() {
    if (micBtn) {
      micBtn.style.background = 'linear-gradient(135deg, #F8C83B 0%, #D97706 100%)';
      micBtn.style.boxShadow = '0 0 30px rgba(248,200,59,0.8)';
    }
    if (ring) {
      ring.style.animation = 'pulseGlow 1.4s infinite';
      ring.style.borderColor = '#F8C83B';
    }
  }
};

window.stopListeningSpeechEngine = function() {
  if (window.voiceRecognitionInstance) {
    try { window.voiceRecognitionInstance.stop(); } catch(e) {}
  }
  window.isAIVoiceRecording = false;
  const micBtn = document.getElementById('vedic-voice-mic-main-btn');
  if (micBtn) {
    micBtn.style.background = 'linear-gradient(135deg, #F8C83B 0%, #D97706 100%)';
  }
};

window.selectQuickVoicePrompt = function(promptText) {
  window.closeAIVoiceModal();
  window.processAIVoiceText(promptText);
};

window.submitManualVedicQuery = function() {
  const input = document.getElementById('vedic-voice-text-input');
  if (!input) return;
  const val = input.value.trim();
  if (!val) {
    if (typeof showToast === 'function') showToast('⚠️ कृपया अपनी समस्या दर्ज करें');
    return;
  }
  input.value = '';
  window.closeAIVoiceModal();
  window.processAIVoiceText(val);
};

// Semantic Natural Language Processor (Hindi & English Keyword NLP Matcher)
window.processAIVoiceText = function(text) {
  if (!text) return;
  const t = text.toLowerCase();

  let matchedMood = 'anxious'; // Default

  if (t.includes('शांति') || t.includes('ध्यान') || t.includes('सुकून') || t.includes('peace') || t.includes('still') || t.includes('calm') || t.includes('मौन')) {
    matchedMood = 'peace';
  } else if (t.includes('दुःख') || t.includes('दुख') || t.includes('निराश') || t.includes('उदासी') || t.includes('उदास') || t.includes('sad') || t.includes('रो') || t.includes('अकेला') || t.includes('alone')) {
    matchedMood = 'sad';
  } else if (t.includes('डर') || t.includes('भय') || t.includes('साहस') || t.includes('संकट') || t.includes('fear') || t.includes('scared') || t.includes('हिम्मत') || t.includes('मुसीबत')) {
    matchedMood = 'fear';
  } else if (t.includes('आनंद') || t.includes('खुश') || t.includes('कृतज्ञ') || t.includes('आभार') || t.includes('धन्यवाद') || t.includes('happy') || t.includes('प्रसन्न') || t.includes('gratitude')) {
    matchedMood = 'grateful';
  } else if (t.includes('भ्रम') || t.includes('समझ नहीं') || t.includes('अनिर्णय') || t.includes('रास्ता') || t.includes('निर्णय') || t.includes('doubt') || t.includes('confus') || t.includes('क्या करूं') || t.includes('मार्ग')) {
    matchedMood = 'doubt';
  } else {
    // Overthinking, anxiety, future, career, tension
    matchedMood = 'anxious';
  }

  if (typeof showToast === 'function') {
    showToast(`🤖 AI मार्गदर्शन प्राप्त हुआ: "${text.substring(0, 24)}..."`);
  }

  window.tilt3DKalashAndEmitNectar(() => {
    window.revealAmritWisdom(matchedMood);
    setTimeout(() => {
      window.playCurrentShlokaVoice();
    }, 500);
  });
};

// Text-to-Speech (TTS) Voice Audio Recitation
window.playCurrentShlokaVoice = function() {
  const shloka = window.currentActiveShloka;
  if (!shloka || !window.speechSynthesis) return;

  try {
    window.speechSynthesis.cancel();

    const textToSpeak = `${shloka.sanskrit}। भावार्थ: ${shloka.hindiMeaning}`;
    const utterance = new SpeechSynthesisUtterance(textToSpeak);
    utterance.lang = 'hi-IN';
    utterance.rate = 0.88;
    utterance.pitch = 1.05;

    window.speechSynthesis.speak(utterance);

    if (typeof showToast === 'function') {
      showToast('🔊 दिव्य वाणी का श्रवण करें...');
    }
  } catch(e) {
    console.warn("TTS speak error:", e);
  }
};

window.saveCurrentShlokaToVault = function() {
  const shloka = window.currentActiveShloka;
  if (!shloka) return;

  let vault = [];
  try {
    const raw = localStorage.getItem('sanatan_saved_amrit_shlokas');
    vault = raw ? JSON.parse(raw) : [];
  } catch(e) {}

  if (!vault.some(item => item.id === shloka.id)) {
    vault.push({
      ...shloka,
      savedAt: new Date().toLocaleDateString('hi-IN')
    });
    localStorage.setItem('sanatan_saved_amrit_shlokas', JSON.stringify(vault));
    if (typeof showToast === 'function') {
      showToast('💾 श्लोक अमृत संग्रह (Vault) में सहेजा गया!');
    }
  } else {
    if (typeof showToast === 'function') {
      showToast('✓ यह श्लोक पहले से ही संग्रह में मौजूद है');
    }
  }
};

window.openAmritVaultModal = function() {
  const modal = document.getElementById('amrit-vault-modal');
  const list = document.getElementById('amrit-vault-list');
  if (!modal || !list) return;

  list.innerHTML = '';

  let vault = [];
  try {
    const raw = localStorage.getItem('sanatan_saved_amrit_shlokas');
    vault = raw ? JSON.parse(raw) : [];
  } catch(e) {}

  if (vault.length === 0) {
    list.innerHTML = '<div style="text-align:center; padding:2rem 1rem; color:#CBD5E1; font-size:0.85rem;">अभी कोई श्लोक सहेजा नहीं गया है।</div>';
  } else {
    vault.forEach(item => {
      const card = document.createElement('div');
      card.style.cssText = 'background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px;';
      card.innerHTML = `
        <div style="font-size:0.75rem; font-weight:800; color:#FDE68A; margin-bottom:4px;">${item.source} • ${item.savedAt}</div>
        <div style="font-size:0.92rem; font-weight:700; color:#FFFDF8; line-height:1.4; margin-bottom:6px;">${item.sanskrit.replace(/\n/g, '<br>')}</div>
        <div style="font-size:0.78rem; color:#CBD5E1; line-height:1.4;">${item.hindiMeaning}</div>
      `;
      list.appendChild(card);
    });
  }

  modal.style.display = 'flex';
};

window.closeAmritVaultModal = function() {
  const modal = document.getElementById('amrit-vault-modal');
  if (modal) modal.style.display = 'none';
};

window.shareCurrentShlokaWhatsApp = function() {
  const shloka = window.currentActiveShloka;
  if (!shloka) return;

  const text = `🌸 *भक्ति अमृत कलश — दिव्य मार्गदर्शन* 🌸\n\n📜 ${shloka.source}\n\n🕉️ ${shloka.sanskrit}\n\n💡 *सरल भावार्थ:* ${shloka.hindiMeaning}\n\n🎯 *आज का संकल्प:* ${shloka.actionKarma}\n\n🙏 भक्ति में लीन ऐप पर संपूर्ण सनातन ज्ञान का अनुभव करें।`;
  
  const url = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
  window.open(url, '_blank');
};
