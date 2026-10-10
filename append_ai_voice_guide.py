import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('amrit_kalash_3d_engine.js', 'r', encoding='utf-8') as f:
    js = f.read()

upgrade_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 🎤 SMART AI VEDIC VOICE GUIDE & SEMANTIC SHLOKA MATCHER
// ══════════════════════════════════════════════════════════════════════════════

window.isAIVoiceListening = false;

window.startAIVoiceMoodRecognition = function() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const btn = document.getElementById('amrit-mic-btn');
  const subtext = document.getElementById('ai-voice-bar-subtext');

  if (!SpeechRecognition) {
    if (typeof showToast === 'function') {
      showToast('🎤 आपके ब्राउज़र में सीधे वॉइस इनपुट समर्थित नहीं है, नीचे दिए गए भावों में से चुनें');
    }
    const promptMood = prompt('अपनी मनोदशा या समस्या लिखें (उदा. चिंता, दुःख, भय, शांति, भ्रम):', 'चिंता');
    if (promptMood) {
      window.matchSpokenTextToVedicWisdom(promptMood);
    }
    return;
  }

  if (window.isAIVoiceListening) return;
  window.isAIVoiceListening = true;

  if (btn) {
    btn.style.background = 'linear-gradient(135deg, #10B981, #059669)';
    btn.style.boxShadow = '0 0 25px rgba(16,185,129,0.85)';
    btn.style.animation = 'pulseGlow 1.2s infinite';
  }

  if (subtext) {
    subtext.textContent = '🎙️ सुन रहे हैं... अपनी समस्या या मनोभाव बोलें (उदा. "मुझे बहुत चिंता हो रही है")';
    subtext.style.color = '#34D399';
    subtext.style.fontWeight = '800';
  }

  if (navigator.vibrate) navigator.vibrate(40);
  if (typeof showToast === 'function') showToast('🎙️ बोलिए... AI वैदिक गाइड आपकी बात सुन रहा है');

  try {
    const rec = new SpeechRecognition();
    rec.lang = 'hi-IN';
    rec.continuous = false;
    rec.interimResults = false;

    rec.onresult = function(e) {
      window.isAIVoiceListening = false;
      resetMicUI();

      if (e.results && e.results[0] && e.results[0][0]) {
        const spokenText = e.results[0][0].transcript;
        if (typeof showToast === 'function') {
          showToast(`✨ पहचानी गई वाणी: "${spokenText}"`);
        }
        window.matchSpokenTextToVedicWisdom(spokenText);
      }
    };

    rec.onerror = function(err) {
      console.warn('Speech recognition error:', err);
      window.isAIVoiceListening = false;
      resetMicUI();
      if (typeof showToast === 'function') {
        showToast('⚠️ ध्वनि स्पष्ट नहीं थी, पुनः प्रयास करें या नीचे दिए भावों पर स्पर्श करें');
      }
    };

    rec.onend = function() {
      window.isAIVoiceListening = false;
      resetMicUI();
    };

    rec.start();
  } catch (ex) {
    window.isAIVoiceListening = false;
    resetMicUI();
    console.error('Speech init error:', ex);
  }

  function resetMicUI() {
    if (btn) {
      btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btn.style.boxShadow = '0 4px 15px rgba(248,200,59,0.5)';
      btn.style.animation = 'none';
    }
    if (subtext) {
      subtext.textContent = 'अपनी समस्या बोलकर बताएं (उदा. "मुझे भविष्य की चिंता है")';
      subtext.style.color = '#CBD5E1';
      subtext.style.fontWeight = 'normal';
    }
  }
};

window.matchSpokenTextToVedicWisdom = function(text) {
  if (!text) return;
  const t = text.toLowerCase();

  let matchedMood = 'anxious';

  if (t.includes('शांति') || t.includes('ध्यान') || t.includes('सुकून') || t.includes('peace') || t.includes('still')) {
    matchedMood = 'peace';
  } else if (t.includes('दुःख') || t.includes('दुख') || t.includes('निराश') || t.includes('उदासी') || t.includes('sad') || t.includes('रो')) {
    matchedMood = 'sad';
  } else if (t.includes('डर') || t.includes('भय') || t.includes('साहस') || t.includes('संकट') || t.includes('fear') || t.includes('scared')) {
    matchedMood = 'fear';
  } else if (t.includes('आनंद') || t.includes('खुश') || t.includes('कृतज्ञ') || t.includes('आभार') || t.includes('धन्यवाद') || t.includes('happy')) {
    matchedMood = 'grateful';
  } else if (t.includes('भ्रम') || t.includes('समझ नहीं') || t.includes('अनिर्णय') || t.includes('रास्ता') || t.includes('doubt') || t.includes('confus')) {
    matchedMood = 'doubt';
  } else {
    matchedMood = 'anxious';
  }

  if (typeof window.revealAmritWisdom === 'function') {
    window.revealAmritWisdom(matchedMood);
  }
};
"""

with open('amrit_kalash_3d_engine.js', 'a', encoding='utf-8') as f:
    f.write(upgrade_code)

print("✓ Appended AI Vedic Voice Guide to amrit_kalash_3d_engine.js successfully")
