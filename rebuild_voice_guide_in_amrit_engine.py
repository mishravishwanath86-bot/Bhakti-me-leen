import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('amrit_kalash_3d_engine.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the voice recognition block from line 313 onwards with the supercharged engine
pos = js.find('// AI VOICE INPUT & NATURAL LANGUAGE SEMANTIC MATCHER')
if pos == -1:
    pos = js.find('window.startAIVoiceMoodRecognition')

new_voice_engine = """// ══════════════════════════════════════════════════════════════════════════════
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
        <div style="font-size:0.92rem; font-weight:700; color:#FFFDF8; line-height:1.4; margin-bottom:6px;">${item.sanskrit.replace(/\\n/g, '<br>')}</div>
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

  const text = `🌸 *भक्ति अमृत कलश — दिव्य मार्गदर्शन* 🌸\\n\\n📜 ${shloka.source}\\n\\n🕉️ ${shloka.sanskrit}\\n\\n💡 *सरल भावार्थ:* ${shloka.hindiMeaning}\\n\\n🎯 *आज का संकल्प:* ${shloka.actionKarma}\\n\\n🙏 भक्ति में लीन ऐप पर संपूर्ण सनातन ज्ञान का अनुभव करें।`;
  
  const url = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
  window.open(url, '_blank');
};
"""

if pos != -1:
    js = js[:pos] + new_voice_engine
    with open('amrit_kalash_3d_engine.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✓ Successfully replaced voice guide engine in amrit_kalash_3d_engine.js")
else:
    with open('amrit_kalash_3d_engine.js', 'a', encoding='utf-8') as f:
        f.write("\n\n" + new_voice_engine)
    print("✓ Appended new voice guide engine to amrit_kalash_3d_engine.js")
