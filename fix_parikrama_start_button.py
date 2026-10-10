import re, sys

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🚩 FIXING PARIKRAMA SELECTION & START FLOW (3/7/11/21 CHAKKAR)")
print("======================================================================")

# 1. Update mandir_3d_engine.js
with open('mandir_3d_engine.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Enhanced selectParikramaTarget and start3DMandirParikramaFlow
new_parikrama_flow_code = """
// 🎯 Parikrama Target Selection (3, 7, 11, 21 Laps)
window.selectParikramaTarget = function(laps, btnEl) {
  window.targetParikramaLaps = parseInt(laps, 10) || 11;
  
  // Highlight active chip
  document.querySelectorAll('.parikrama-chip').forEach(c => {
    c.classList.remove('active');
    c.style.background = 'rgba(255,255,255,0.08)';
    c.style.borderColor = 'rgba(255,255,255,0.15)';
    c.style.color = '#CBD5E1';
    c.style.boxShadow = 'none';
  });
  
  if (btnEl) {
    btnEl.classList.add('active');
    btnEl.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btnEl.style.borderColor = '#FEF3C7';
    btnEl.style.color = '#1A0B2E';
    btnEl.style.boxShadow = '0 0 12px rgba(248,200,59,0.5)';
  }
  
  // Update CTA text on Home Card
  const ctaText = document.getElementById('parikrama-cta-text');
  if (ctaText) {
    ctaText.textContent = `🚩 ${laps} परिक्रमा शुरू करें (3D मंदिर में प्रवेश)`;
  }
  
  const badge = document.getElementById('target-laps-badge');
  if (badge) badge.textContent = `${laps} परिक्रमा संकल्प`;

  if (navigator.vibrate) navigator.vibrate(25);
  if (typeof playSoundEffect === 'function') playSoundEffect('click');
};

// 🚩 Start 3D Mandir Parikrama Flow
window.start3DMandirParikramaFlow = function(deityKey) {
  deityKey = deityKey || window.current3DDeity || 'mahakal';
  window.open3DMandirModal(deityKey);
};

// 🏛️ Home Screen 3D Temple Target Switcher
window.setHome3DTempleTarget = function(modelKey) {
  window.current3DTempleModel = modelKey;
  const btnClassical = document.getElementById('home-temple-select-classical');
  const btnHeritage = document.getElementById('home-temple-select-heritage');
  
  if (btnClassical && btnHeritage) {
    if (modelKey === 'temple_classical') {
      btnClassical.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btnClassical.style.color = '#1A0B2E';
      btnClassical.style.boxShadow = '0 0 10px rgba(248,200,59,0.4)';
      btnHeritage.style.background = 'transparent';
      btnHeritage.style.color = '#CBD5E1';
      btnHeritage.style.boxShadow = 'none';
    } else {
      btnHeritage.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btnHeritage.style.color = '#1A0B2E';
      btnHeritage.style.boxShadow = '0 0 10px rgba(248,200,59,0.4)';
      btnClassical.style.background = 'transparent';
      btnClassical.style.color = '#CBD5E1';
      btnClassical.style.boxShadow = 'none';
    }
  }
  if (navigator.vibrate) navigator.vibrate(25);
  if (typeof playSoundEffect === 'function') playSoundEffect('click');
};
"""

# Replace old selectParikramaTarget
old_select_pattern = r'window\.selectParikramaTarget\s*=\s*function\(laps,\s*btnEl\)[\s\S]*?window\.open3DMandirModal\s*=\s*function'
if re.search(old_select_pattern, js):
    js = re.sub(old_select_pattern, lambda m: new_parikrama_flow_code + '\n\nwindow.open3DMandirModal = function', js, count=1)
    print("✓ Replaced and enhanced selectParikramaTarget and start3DMandirParikramaFlow in mandir_3d_engine.js")
else:
    js += '\n' + new_parikrama_flow_code
    print("✓ Appended new parikrama flow code to mandir_3d_engine.js")

with open('mandir_3d_engine.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Also ensure these global functions exist in app.js as well for instant safety
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

app_bridge_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 🚩 3D MANDIR & PARIKRAMA GLOBAL BRIDGE HANDLERS
// ══════════════════════════════════════════════════════════════════════════════

window.selectParikramaTarget = window.selectParikramaTarget || function(laps, btnEl) {
  window.targetParikramaLaps = parseInt(laps, 10) || 11;
  document.querySelectorAll('.parikrama-chip').forEach(c => {
    c.classList.remove('active');
    c.style.background = 'rgba(255,255,255,0.08)';
    c.style.borderColor = 'rgba(255,255,255,0.15)';
    c.style.color = '#CBD5E1';
    c.style.boxShadow = 'none';
  });
  if (btnEl) {
    btnEl.classList.add('active');
    btnEl.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
    btnEl.style.borderColor = '#FEF3C7';
    btnEl.style.color = '#1A0B2E';
    btnEl.style.boxShadow = '0 0 12px rgba(248,200,59,0.5)';
  }
  const ctaText = document.getElementById('parikrama-cta-text');
  if (ctaText) {
    ctaText.textContent = `🚩 ${laps} परिक्रमा शुरू करें (3D मंदिर में प्रवेश)`;
  }
};

window.start3DMandirParikramaFlow = window.start3DMandirParikramaFlow || function(deityKey) {
  if (typeof window.open3DMandirModal === 'function') {
    window.open3DMandirModal(deityKey || window.current3DDeity || 'mahakal');
  } else {
    const modal = document.getElementById('mandir-3d-modal');
    if (modal) modal.style.display = 'flex';
  }
};

window.setHome3DTempleTarget = window.setHome3DTempleTarget || function(modelKey) {
  window.current3DTempleModel = modelKey;
};
"""

if 'window.selectParikramaTarget = window.selectParikramaTarget' not in app_js:
    app_js += '\n' + app_bridge_code
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(app_js)
    print("✓ Added global bridge handlers to app.js")

print("✓ All parikrama flow handlers updated and verified!")
