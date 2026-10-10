import re, time, sys

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🪔 INTEGRATING HIGH-FIDELITY DIGITAL PUJA THALI (8 SAMAGRI ENGINE)")
print("======================================================================")

# 1. Update app.js with rich Digital Puja Thali engine
puja_engine_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 8-SAMAGRI INTERACTIVE DIGITAL PUJA THALI ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.pujaSamagriList = [
  { id: 'deep', name: 'दीप', emoji: '🪔', actionText: '✨ दीप ज्योति प्रज्वलित हुई!', isOffered: false },
  { id: 'ghanti', name: 'घंटी', emoji: '🔔', actionText: '🔔 दिव्य घंटा नाद गुंजायमान...', isOffered: false },
  { id: 'shankh', name: 'शंख', emoji: '🐚', actionText: '🐚 पावन शंखनाद!', isOffered: false },
  { id: 'pushp', name: 'पुष्प', emoji: '🌸', actionText: '🌺 पुष्प वृष्टि प्रभु चरणों में!', isOffered: false },
  { id: 'dhoop', name: 'धूप', emoji: '💨', actionText: '💨 सुगंधित धूप व गुग्गुल अर्पित!', isOffered: false },
  { id: 'gangajal', name: 'गंगाजल', emoji: '🌊', actionText: '💧 पवित्र गंगाजल से आचमन व अभिषेक!', isOffered: false },
  { id: 'tilak', name: 'चंदन', emoji: '🏵️', actionText: '🌟 दिव्य हरिचंदन व कुमकुम तिलक अर्पित!', isOffered: false },
  { id: 'bhog', name: 'भोग', emoji: '🥥', actionText: '🍯 माखन-मिश्री व पंचामृत नैवेद्य अर्पित!', isOffered: false }
];

window.offerSamagriItem = function(index) {
  const item = window.pujaSamagriList[index];
  if (!item) return;

  item.isOffered = true;

  // Haptic feedback
  if (navigator.vibrate) {
    navigator.vibrate([0, 40, 20, 50]);
  }

  // Audio effects based on item
  if (item.id === 'ghanti' && typeof ringTempleBell === 'function') {
    ringTempleBell();
  } else if (item.id === 'shankh' && typeof blowTempleConch === 'function') {
    blowTempleConch();
  } else if (typeof playSoundEffect === 'function') {
    playSoundEffect('correct');
  }

  // Visual Node Animation
  const node = document.getElementById(`samagri-node-${item.id}`);
  if (node) {
    node.style.background = 'linear-gradient(135deg, rgba(16, 185, 129, 0.4) 0%, rgba(5, 150, 105, 0.25) 100%)';
    node.style.borderColor = '#10B981';
    node.style.boxShadow = '0 0 18px rgba(16, 185, 129, 0.8), 0 0 10px rgba(248,200,59,0.4) inset';
    node.style.transform = 'scale(1.12)';
    setTimeout(() => {
      if (node) node.style.transform = 'scale(1.0)';
    }, 200);

    const nameSpan = node.querySelector('.p-name');
    if (nameSpan) {
      nameSpan.style.color = '#34D399';
      nameSpan.textContent = '✓ ' + item.name;
    }
  }

  // Float flower petals for pushp item
  if (item.id === 'pushp' && typeof triggerFlowerShower === 'function') {
    triggerFlowerShower();
  }

  // Dynamic Action Message
  const msgEl = document.getElementById('puja-action-message');
  if (msgEl) {
    msgEl.textContent = item.actionText;
    msgEl.style.color = '#34D399';
  }

  // Counter Badge Update
  const offeredCount = window.pujaSamagriList.filter(s => s.isOffered).length;
  const badge = document.getElementById('puja-thali-badge');
  if (badge) {
    badge.textContent = `${offeredCount}/8 अर्पित`;
    if (offeredCount === 8) {
      badge.textContent = '✨ 8/8 संपूर्ण';
      badge.style.background = 'rgba(16, 185, 129, 0.3)';
      badge.style.borderColor = '#10B981';
      badge.style.color = '#34D399';
    }
  }

  // Check 8/8 Completion
  if (offeredCount === 8) {
    if (typeof triggerFlowerShower === 'function') {
      triggerFlowerShower();
    }
    if (typeof playSoundEffect === 'function') {
      playSoundEffect('victory');
    }

    // Award +10 Punya Points
    if (window.SadhanaProfile && typeof window.SadhanaProfile.addPunya === 'function') {
      window.SadhanaProfile.addPunya(10, 'डिजिटल पूजा थाली समर्पण');
    }

    setTimeout(() => {
      window.showPujaCompletedModal();
    }, 450);
  }
};

window.resetPujaThali = function() {
  window.pujaSamagriList.forEach((item) => {
    item.isOffered = false;
    const node = document.getElementById(`samagri-node-${item.id}`);
    if (node) {
      node.style.background = '#2E1C4E';
      node.style.borderColor = '#E89A3C';
      node.style.boxShadow = '0 3px 10px rgba(0,0,0,0.4)';
      node.style.transform = 'scale(1.0)';
      const nameSpan = node.querySelector('.p-name');
      if (nameSpan) {
        nameSpan.style.color = '#FFF';
        nameSpan.textContent = item.name;
      }
    }
  });

  const badge = document.getElementById('puja-thali-badge');
  if (badge) {
    badge.textContent = '0/8 अर्पित';
    badge.style.background = 'rgba(248,200,59,0.18)';
    badge.style.borderColor = '#F8C83B';
    badge.style.color = '#FDE68A';
  }

  const msgEl = document.getElementById('puja-action-message');
  if (msgEl) {
    msgEl.textContent = 'सामग्री पर स्पर्श करके प्रभु को अर्पित करें 🙏';
    msgEl.style.color = '#FDE68A';
  }

  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof playSoundEffect === 'function') playSoundEffect('correct');
  if (typeof showToast === 'function') {
    showToast('🔄 पूजा थाली पुनः तैयार की गई');
  }
};

window.showPujaCompletedModal = function() {
  const modal = document.getElementById('puja-completed-modal');
  if (modal) {
    modal.style.display = 'flex';
  }
};

window.closePujaCompletedModal = function() {
  const modal = document.getElementById('puja-completed-modal');
  if (modal) {
    modal.style.display = 'none';
  }
};
"""

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace or append puja engine
if 'window.offerSamagriItem' in js:
    js = re.sub(r'\/\/ ══════════════════════════════════════════════════════════════════════════════\s*\/\/ 🪔 8-SAMAGRI INTERACTIVE DIGITAL PUJA THALI ENGINE[\s\S]*?window\.closePujaCompletedModal\s*=\s*function\(\)[\s\S]*?\n\};', lambda m: puja_engine_code, js)
    print("✓ Replaced existing Puja Thali Engine in app.js")
else:
    js += '\n' + puja_engine_code
    print("✓ Appended Puja Thali Engine to app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ app.js saved successfully!")
