import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

puja_thali_controller_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 8-SAMAGRI DIGITAL PUJA THALI ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.pujaSamagriList = [
  { id: 'deep', name: 'दीप', emoji: '🪔', actionText: 'दीप ज्योति प्रज्वलित हुई! ✨', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'ghanti', name: 'घंटी', emoji: '🔔', actionText: 'दिव्य घंटा नाद... 🔔', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'shankh', name: 'शंख', emoji: '🐚', actionText: 'शुभ शंखनाद! 🕉️', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'pushp', name: 'पुष्प', emoji: '🌸', actionText: 'पुष्प वृष्टि प्रभु चरणों में! 🌺', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'dhoop', name: 'धूप', emoji: '💨', actionText: 'सुगंधित धूप अर्पित हुई! 🪔', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'gangajal', name: 'गंगाजल', emoji: '🌊', actionText: 'पवित्र गंगाजल से आचमन! 💧', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'tilak', name: 'चंदन', emoji: '🏵️', actionText: 'दिव्य हरिचंदन तिलक अर्पित! 🌟', sound: 'assets/audio/correct.mp3', isOffered: false },
  { id: 'bhog', name: 'भोग', emoji: '🥥', actionText: 'माखन-मिश्री व नैवेद्य अर्पित! 🍯', sound: 'assets/audio/correct.mp3', isOffered: false }
];

window.offerSamagriItem = function(index) {
  const item = window.pujaSamagriList[index];
  if (!item) return;

  item.isOffered = true;

  // Haptic feedback if available
  if (navigator.vibrate) navigator.vibrate(30);

  // Play Bell sound
  if (typeof playSoundEffect === 'function') {
    playSoundEffect('correct');
  }

  // Update UI node
  const node = document.getElementById(`samagri-node-${item.id}`);
  if (node) {
    node.style.background = 'rgba(16, 185, 129, 0.35)';
    node.style.borderColor = '#10B981';
    node.style.boxShadow = '0 0 14px rgba(16, 185, 129, 0.6)';
    const nameSpan = node.querySelector('.p-name');
    if (nameSpan) {
      nameSpan.style.color = '#34D399';
    }
  }

  // Update Message
  const msgEl = document.getElementById('puja-action-message');
  if (msgEl) {
    msgEl.textContent = item.actionText;
    msgEl.style.color = '#34D399';
  }

  // Update Count
  const offeredCount = window.pujaSamagriList.filter(s => s.isOffered).length;
  const badge = document.getElementById('puja-thali-badge');
  if (badge) {
    badge.textContent = `${offeredCount}/8 अर्पित`;
    if (offeredCount === 8) {
      badge.style.background = 'rgba(16, 185, 129, 0.25)';
      badge.style.borderColor = '#10B981';
      badge.style.color = '#34D399';
    }
  }

  // 8/8 Complete Check
  if (offeredCount === 8) {
    if (typeof triggerFlowerShower === 'function') {
      triggerFlowerShower();
    }
    if (typeof playSoundEffect === 'function') {
      playSoundEffect('victory');
    }
    setTimeout(() => {
      window.showPujaCompletedModal();
    }, 400);
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
      const nameSpan = node.querySelector('.p-name');
      if (nameSpan) {
        nameSpan.style.color = '#FFF';
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
    msgEl.textContent = 'पुनः सामग्री स्पर्श करके पूजन आरंभ करें 🙏';
    msgEl.style.color = '#FDE68A';
  }

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

js += "\n\n" + puja_thali_controller_js

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Bump version in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Appended 8-Samagri Puja Thali Controller to app.js (v={ts})")
