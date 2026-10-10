import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('mandir_3d_engine.js', 'r', encoding='utf-8') as f:
    js = f.read()

aliases_code = """
// Aliases for HTML modal buttons
window.toggle3DAutoOrbit = window.toggleAutoOrbit;
window.reset3DCameraView = function() { window.setCameraViewPreset('front'); };
window.trigger3DDiyaGlow = function() {
  if (typeof playSoundEffect === 'function') playSoundEffect('correct');
  if (typeof showToast === 'function') showToast('🪔 दीप प्रज्ज्वलित किया गया!');
  if (navigator.vibrate) navigator.vibrate(30);
};
window.trigger3DPushpaVarsha = window.triggerFlowerShower3D;
window.trigger3DGhantiNaad = function() {
  if (typeof ringTempleBell === 'function') ringTempleBell();
  if (typeof showToast === 'function') showToast('🔔 मंदिर महाघंट नाद गुंजायमान!');
  if (navigator.vibrate) navigator.vibrate([0, 60, 30, 80]);
};
window.close3DParikramaCompletedModal = function() {
  const m = document.getElementById('parikrama-completed-modal');
  if (m) m.style.display = 'none';
};
window.share3DParikramaWhatsApp = function() {
  const text = `🚩 मैंने "Bhakti Me Leen" ऐप में भव्य 3D मंदिर की ${window.targetParikramaLaps} परिक्रमा और दिव्य दर्शन पूर्ण किए! आप भी दर्शन करें ➔ https://bhaktimeleen.app`;
  window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, '_blank');
};
"""

if 'window.toggle3DAutoOrbit' not in js:
    js += '\n' + aliases_code

with open('mandir_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Added aliases and helper functions to mandir_3d_engine.js")
