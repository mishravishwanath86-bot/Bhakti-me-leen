import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

amrit_kalash_engine_js = """// ══════════════════════════════════════════════════════════════════════════════
// 🏺 BHAKTI AMRIT KALASH — 3D INTERACTIVE & AI VOICE REVEAL ENGINE
// Powered by Three.js WebGL, Web Speech Recognition & Vedic Semantic Matcher
// ══════════════════════════════════════════════════════════════════════════════

window.AMRIT_SHLOKA_DATASET = {
  'anxious': {
    id: 'shloka_anxious',
    mood: 'अशांत / व्याकुल (Anxiety • Overthink)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 2, श्लोक 47)',
    sanskrit: 'कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।\\nमा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥',
    hindiMeaning: 'तुम्हारा अधिकार केवल अपने कर्तव्य कर्म पर है, उसके फल पर कभी नहीं। भविष्य के परिणाम की चिंता छोड़कर शांत चित्त से वर्तमान कर्म करो।',
    actionKarma: '2 मिनट आंखें बंद करके गहरी सांस लें और 11 बार ॐ का उच्चारण करके अपनी सारी चिंता प्रभु को समर्पित करें।',
    themeColor: '#EF4444'
  },
  'peace': {
    id: 'shloka_peace',
    mood: 'शांति / ध्यान (Peace • Stillness)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 6, श्लोक 5)',
    sanskrit: 'उद्धरेदात्मनात्मानं नात्मानमवसादयेत्।\\nआत्मैव ह्यात्मनो बन्धुरात्मैव रिपुरात्मनः॥',
    hindiMeaning: 'मनुष्य को अपने मन के द्वारा अपना उद्धार करना चाहिए, मन को नीचे न गिरने दे। क्योंकि मन ही मनुष्य का सबसे बड़ा मित्र और मन ही शत्रु है।',
    actionKarma: '5 मिनट मौन रहकर अपने भीतर परमात्मा की उपस्थिति का अनुभव करें और आभार व्यक्त करें।',
    themeColor: '#10B981'
  },
  'sad': {
    id: 'shloka_sad',
    mood: 'निराशा / दुःख (Sadness • Low Energy)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 2, श्लोक 14)',
    sanskrit: 'मात्रास्पर्शास्तु कौन्तेय शीतोष्णसुखदुःखदाः।\\nआगमापायिनोऽनित्यास्तांस्तितिक्षस्व भारत॥',
    hindiMeaning: 'हे कुंतीपुत्र! सुख और दुःख सर्दी-गर्मी की तरह आते और जाते रहते हैं। ये अनित्य हैं, अतः धैर्यपूर्वक इन्हें सहन करना सीखो, यह समय भी बीत जाएगा।',
    actionKarma: 'एक गिलास पवित्र जल पिएं और मन में दोहराएं: "यह कठिन समय भी प्रभु कृपा से सुखद बन जाएगा।"',
    themeColor: '#8B5CF6'
  },
  'fear': {
    id: 'shloka_fear',
    mood: 'भय / साहस (Fear • Courage Needed)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 18, श्लोक 66)',
    sanskrit: 'सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज।\\nअहं त्वां सर्वपापेभ्यो मोक्षयिष्यामि मा शुचः॥',
    hindiMeaning: 'सब चिंताओं व भयों को त्यागकर केवल मेरी शरण में आ जाओ। मैं तुम्हें समस्त संकटों व भयों से मुक्त कर दूंगा, तनिक भी शोक मत करो।',
    actionKarma: 'श्री हनुमान चालीसा की चौपाई का स्मरण करें: "भूत पिशाच निकट नहिं आवै, महाबीर जब नाम सुनावै।"',
    themeColor: '#F59E0B'
  },
  'grateful': {
    id: 'shloka_grateful',
    mood: 'कृतज्ञ / आनंद (Grateful • Joyful)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 12, श्लोक 15)',
    sanskrit: 'यस्मान्नोद्विजते लोको लोकान्नोद्विजते च यः।\\nहर्षामर्षभयोद्वेगैर्मुक्तो यः स च मे प्रियः॥',
    hindiMeaning: 'जिससे किसी को कष्ट नहीं पहुंचता और जो किसी से उद्विग्न नहीं होता, जो हर्ष, अमर्ष और भय से मुक्त है—ऐसा भक्त मुझे अत्यंत प्रिय है।',
    actionKarma: 'आज किसी एक जरूरतमंद या पशु-पक्षी को भोजन अर्पित कर प्रभु के प्रति अपनी कृतज्ञता प्रकट करें।',
    themeColor: '#EC4899'
  },
  'doubt': {
    id: 'shloka_doubt',
    mood: 'अनिर्णय / भ्रम (Doubt • Clarity)',
    source: '📜 श्रीमद्भगवद्गीता (अध्याय 4, श्लोक 39)',
    sanskrit: 'श्रद्धावाँल्लभते ज्ञानं तत्परः संयतेन्द्रियः।\\nज्ञानं लब्ध्वा परां शान्तिमचिरेणाधिगच्छति॥',
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

  container.innerHTML = '';

  const width = container.clientWidth || 320;
  const height = container.clientHeight || 190;

  // Scene & Camera
  const scene = new THREE.Scene();
  window.Kalash3D.scene = scene;

  const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
  camera.position.set(0, 0.8, 6.2);
  camera.lookAt(0, 0.5, 0);
  window.Kalash3D.camera = camera;

  // Renderer
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.3;
  container.appendChild(renderer.domElement);
  window.Kalash3D.renderer = renderer;

  // Lighting
  const ambient = new THREE.AmbientLight(0xFFF3E0, 1.2);
  scene.add(ambient);

  const mainLight = new THREE.PointLight(0xF8C83B, 2.5, 15);
  mainLight.position.set(3, 4, 4);
  scene.add(mainLight);

  const backGlow = new THREE.PointLight(0xF59E0B, 1.8, 10);
  backGlow.position.set(-3, 2, -2);
  scene.add(backGlow);

  // ══════════════════════════════════════════════════════════
  // BUILD 3D GOLDEN KALASH (POT, MANGO LEAVES, COCONUT)
  // ══════════════════════════════════════════════════════════
  const kalashMaster = new THREE.Group();

  const goldPBR = new THREE.MeshStandardMaterial({
    color: 0xF8C83B,
    metalness: 0.9,
    roughness: 0.18
  });

  const brassPBR = new THREE.MeshStandardMaterial({
    color: 0xD97706,
    metalness: 0.8,
    roughness: 0.25
  });

  const leafMat = new THREE.MeshStandardMaterial({
    color: 0x16A34A,
    roughness: 0.4,
    side: THREE.DoubleSide
  });

  const coconutMat = new THREE.MeshStandardMaterial({
    color: 0x78350F,
    roughness: 0.75
  });

  const mauliMat = new THREE.MeshStandardMaterial({
    color: 0xDC2626,
    roughness: 0.5
  });

  // 1. Kalash Pot Body (लौटा / कलश)
  const potBase = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.7, 0.3, 24), brassPBR);
  potBase.position.y = -0.65;
  kalashMaster.add(potBase);

  const potBody = new THREE.Mesh(new THREE.SphereGeometry(1.15, 32, 24), goldPBR);
  potBody.position.y = 0.2;
  kalashMaster.add(potBody);

  const potNeck = new THREE.Mesh(new THREE.CylinderGeometry(0.7, 0.85, 0.5, 24), goldPBR);
  potNeck.position.y = 1.0;
  kalashMaster.add(potNeck);

  const potRim = new THREE.Mesh(new THREE.TorusGeometry(0.75, 0.12, 16, 32), goldPBR);
  potRim.rotation.x = Math.PI / 2;
  potRim.position.y = 1.25;
  kalashMaster.add(potRim);

  // 2. Red Mauli Thread tied around Kalash Neck
  const mauliThread = new THREE.Mesh(new THREE.TorusGeometry(0.72, 0.06, 12, 32), mauliMat);
  mauliThread.rotation.x = Math.PI / 2;
  mauliThread.position.y = 1.0;
  kalashMaster.add(mauliThread);

  // 3. 5 Mango Leaves (आम्रपल्लव) radiating outwards
  for (let l = 0; l < 5; l++) {
    const lAng = (l / 5) * Math.PI * 2;
    const leaf = new THREE.Mesh(new THREE.ConeGeometry(0.28, 1.2, 4), leafMat);
    leaf.rotation.x = Math.PI / 3;
    leaf.rotation.y = lAng;
    leaf.position.set(Math.sin(lAng) * 0.45, 1.4, Math.cos(lAng) * 0.45);
    kalashMaster.add(leaf);
  }

  // 4. Sacred Coconut (श्रीफल)
  const coconut = new THREE.Mesh(new THREE.SphereGeometry(0.65, 24, 20), coconutMat);
  coconut.scale.set(1.0, 1.25, 1.0);
  coconut.position.y = 1.75;
  kalashMaster.add(coconut);

  kalashMaster.position.y = -0.2;
  scene.add(kalashMaster);
  window.Kalash3D.kalashGroup = kalashMaster;

  // ══════════════════════════════════════════════════════════
  // GOLDEN PARTICLES AURA
  // ══════════════════════════════════════════════════════
  const pCount = 80;
  const pPos = new Float32Array(pCount * 3);
  for (let p = 0; p < pCount * 3; p += 3) {
    pPos[p] = (Math.random() - 0.5) * 4;
    pPos[p + 1] = (Math.random() - 0.5) * 3 + 0.5;
    pPos[p + 2] = (Math.random() - 0.5) * 4;
  }
  const pGeo = new THREE.BufferGeometry();
  pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
  const pMat = new THREE.PointsMaterial({
    color: 0xF8C83B,
    size: 0.14,
    transparent: true,
    opacity: 0.85
  });
  const sparkles = new THREE.Points(pGeo, pMat);
  scene.add(sparkles);
  window.Kalash3D.sparkles = sparkles;

  animate3DKalash();
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
  const K = window.Kalash3D;
  if (!K.kalashGroup) {
    if (callback) callback();
    return;
  }

  K.isTilting = true;

  if (typeof gsap !== 'undefined') {
    gsap.to(K.kalashGroup.rotation, {
      z: -0.45,
      duration: 0.4,
      ease: "power2.out",
      onComplete: () => {
        if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
        if (typeof playSoundEffect === 'function') playSoundEffect('correct');
        if (navigator.vibrate) navigator.vibrate([40, 60, 40]);

        setTimeout(() => {
          gsap.to(K.kalashGroup.rotation, {
            z: 0,
            duration: 0.5,
            ease: "elastic.out(1, 0.4)",
            onComplete: () => {
              K.isTilting = false;
              if (callback) callback();
            }
          });
        }, 300);
      }
    });
  } else {
    K.isTilting = false;
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
  if (sanskritEl) sanskritEl.innerHTML = shloka.sanskrit.replace(/\\n/g, '<br>');
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
// AI VOICE INPUT & NATURAL LANGUAGE SEMANTIC MATCHER
// ══════════════════════════════════════════════════════════════════════════════

window.voiceRecognitionInstance = null;

window.startAIVoiceMoodRecognition = function() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

  const overlay = document.getElementById('voice-listening-overlay');
  const preview = document.getElementById('voice-transcript-preview');

  if (!SpeechRecognition) {
    if (typeof showToast === 'function') {
      showToast('⚠️ वॉइस पहचान ब्राउज़र में समर्थित नहीं है, कृपया कार्ड चुनें');
    }
    return;
  }

  if (overlay) overlay.style.display = 'flex';
  if (preview) preview.textContent = 'सुन रहे हैं... बोलना शुरू करें';

  const recognition = new SpeechRecognition();
  window.voiceRecognitionInstance = recognition;
  recognition.lang = 'hi-IN';
  recognition.continuous = false;
  recognition.interimResults = true;

  recognition.onresult = function(event) {
    let transcript = '';
    for (let i = event.resultIndex; i < event.results.length; ++i) {
      transcript += event.results[i][0].transcript;
    }
    if (preview) preview.textContent = transcript;

    if (event.results[0].isFinal) {
      setTimeout(() => {
        window.stopAIVoiceMoodRecognition();
        window.processAIVoiceText(transcript);
      }, 500);
    }
  };

  recognition.onerror = function(e) {
    console.warn("Speech error:", e);
    window.stopAIVoiceMoodRecognition();
    if (typeof showToast === 'function') {
      showToast('⚠️ आवाज़ स्पष्ट नहीं थी, पुनः प्रयास करें');
    }
  };

  recognition.start();
};

window.stopAIVoiceMoodRecognition = function() {
  if (window.voiceRecognitionInstance) {
    try { window.voiceRecognitionInstance.stop(); } catch(e) {}
  }
  const overlay = document.getElementById('voice-listening-overlay');
  if (overlay) overlay.style.display = 'none';
};

// Semantic Keyword & Context Matcher (Speech-to-Wisdom)
window.processAIVoiceText = function(text) {
  const t = text.toLowerCase();

  let matchedMood = 'anxious';

  if (t.includes('डर') || t.includes('भय') || t.includes('साहस') || t.includes('fear') || t.includes('scared') || t.includes('loss') || t.includes('नुकसान')) {
    matchedMood = 'fear';
  } else if (t.includes('शांति') || t.includes('ध्यान') || t.includes('peace') || t.includes('calm') || t.includes('मौन')) {
    matchedMood = 'peace';
  } else if (t.includes('दुख') || t.includes('दुःख') || t.includes('उदास') || t.includes('sad') || t.includes('निराश') || t.includes('alone') || t.includes('अकेला')) {
    matchedMood = 'sad';
  } else if (t.includes('आनंद') || t.includes('खुश') || t.includes('happy') || t.includes('कृतज्ञ') || t.includes('thank') || t.includes('प्रसन्न')) {
    matchedMood = 'grateful';
  } else if (t.includes('भ्रम') || t.includes('निर्णय') || t.includes('confus') || t.includes('doubt') || t.includes('क्या करूं') || t.includes('मार्ग')) {
    matchedMood = 'doubt';
  } else {
    // Default to anxiety/overthink for queries like chinta, tension, career, future
    matchedMood = 'anxious';
  }

  if (typeof showToast === 'function') {
    showToast(`🤖 AI ने पहचाना: '${text}' ➔ श्लोक प्राप्त हुआ!`);
  }

  window.tilt3DKalashAndEmitNectar(() => {
    window.revealAmritWisdom(matchedMood);
  });
};

// ══════════════════════════════════════════════════════════════════════════════
// AUDIO CHANTING VOICE (TEXT-TO-SPEECH)
// ══════════════════════════════════════════════════════════════════════════════

window.playCurrentShlokaVoice = function() {
  const shloka = window.currentActiveShloka;
  if (!shloka || !window.speechSynthesis) return;

  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(shloka.sanskrit + "। " + shloka.hindiMeaning);
  utterance.lang = 'hi-IN';
  utterance.rate = 0.88; // Gentle, reverent pace
  utterance.pitch = 1.05;

  window.speechSynthesis.speak(utterance);

  if (typeof showToast === 'function') {
    showToast('🔊 दिव्य वाणी का श्रवण करें...');
  }
};

// ══════════════════════════════════════════════════════════════════════════════
// VAULT STORAGE & WHATSAPP SHARING
// ══════════════════════════════════════════════════════════════════════════════

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
      showToast('✨ यह श्लोक पहले से आपके संग्रह में मौजूद है');
    }
  }
};

window.openAmritVaultModal = function() {
  const modal = document.getElementById('amrit-vault-modal');
  if (modal) modal.style.display = 'flex';
  window.renderAmritVaultList();
};

window.closeAmritVaultModal = function() {
  const modal = document.getElementById('amrit-vault-modal');
  if (modal) modal.style.display = 'none';
};

window.renderAmritVaultList = function() {
  const container = document.getElementById('amrit-vault-list');
  if (!container) return;

  let vault = [];
  try {
    const raw = localStorage.getItem('sanatan_saved_amrit_shlokas');
    vault = raw ? JSON.parse(raw) : [];
  } catch(e) {}

  if (vault.length === 0) {
    container.innerHTML = `
      <div style="text-align:center; padding:2rem 1rem; color:#CBD5E1;">
        <div style="font-size:2.5rem; margin-bottom:8px;">📜</div>
        <div style="font-size:0.9rem; font-weight:800; color:#FDE68A;">कोई श्लोक सहेजा नहीं गया है</div>
        <p style="font-size:0.75rem; margin-top:4px;">मनःस्थिति चुनकर श्लोक को 'अमृत संग्रह' में सहेजें।</p>
      </div>
    `;
    return;
  }

  let html = '';
  vault.forEach((item, idx) => {
    html += `
      <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:18px; padding:12px; position:relative;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
          <span style="font-size:0.75rem; font-weight:900; color:#F8C83B;">${item.source}</span>
          <button onclick="deleteShlokaFromVault('${item.id}')" style="background:none; border:none; color:#FCA5A5; font-size:0.8rem; cursor:pointer;" title="हटाएं">🗑️</button>
        </div>
        <div style="font-family:'Tiro Devanagari Hindi', serif; font-size:0.95rem; font-weight:700; color:#FFFDF8; line-height:1.5; margin-bottom:6px;">
          ${item.sanskrit.replace(/\\n/g, '<br>')}
        </div>
        <p style="font-size:0.78rem; color:#CBD5E1; margin:0 0 8px 0; line-height:1.4;">${item.hindiMeaning}</p>
        <div style="display:flex; justify-content:flex-end;">
          <button onclick="revealAmritWisdom('${item.id.replace('shloka_', '')}')" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-size:0.72rem; font-weight:900; padding:4px 10px; border-radius:10px; cursor:pointer;">
            विस्तार देखें ➔
          </button>
        </div>
      </div>
    `;
  });

  container.innerHTML = html;
};

window.deleteShlokaFromVault = function(id) {
  let vault = [];
  try {
    const raw = localStorage.getItem('sanatan_saved_amrit_shlokas');
    vault = raw ? JSON.parse(raw) : [];
  } catch(e) {}

  vault = vault.filter(item => item.id !== id);
  localStorage.setItem('sanatan_saved_amrit_shlokas', JSON.stringify(vault));
  window.renderAmritVaultList();
  if (typeof showToast === 'function') {
    showToast('🗑️ श्लोक संग्रह से हटाया गया');
  }
};

window.shareCurrentShlokaWhatsApp = function() {
  const shloka = window.currentActiveShloka;
  if (!shloka) return;

  const msg = `🚩 *भक्ति अमृत कलश — दिव्य मार्गदर्शन* 🚩\\n${shloka.source}\\n\\n"${shloka.sanskrit}"\\n\\n💡 *भावार्थ:* ${shloka.hindiMeaning}\\n\\n🎯 *आज का कर्म:* ${shloka.actionKarma}\\n\\nघर बैठे दिव्य श्लोक व समाधान पाएं: 'भक्ति में लीन' ऐप डाउनलोड करें 🕉️✨`;
  
  const shareUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`;
  window.open(shareUrl, '_blank');
};

// Auto-initialize 3D Kalash when opening page-jar
document.addEventListener('DOMContentLoaded', function() {
  const origShowPage = window.showPage;
  if (typeof origShowPage === 'function') {
    window.showPage = function(pageId) {
      origShowPage(pageId);
      if (pageId === 'page-jar') {
        setTimeout(window.init3DKalashCanvas, 100);
      }
    };
  }
});
"""

with open('amrit_kalash_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(amrit_kalash_engine_js)

print("✓ Created amrit_kalash_3d_engine.js with full 3D Kalash WebGL and AI Voice Engine")

# Link amrit_kalash_3d_engine.js in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ts = int(time.time())
if 'amrit_kalash_3d_engine.js' not in html:
    html = html.replace('<script src="app.js', f'<script src="amrit_kalash_3d_engine.js?v={ts}"></script>\n  <script src="app.js')

html = re.sub(r'amrit_kalash_3d_engine\.js\?v=\d+', f'amrit_kalash_3d_engine.js?v={ts}', html)
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Linked amrit_kalash_3d_engine.js in index.html (v={ts})")
