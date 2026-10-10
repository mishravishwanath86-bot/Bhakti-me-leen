import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html Settings Page with rich Font Size Controls & Live Preview
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_font_row = """        <div class="setting-row"><span>🔤 फॉन्ट साइज़</span>
          <select class="inline-select" id="font-size-select"><option value="1">सामान्य</option><option value="1.15">बड़ा</option><option value="1.3">बहुत बड़ा</option></select>
        </div>"""

new_font_row = """        <!-- 🔤 ADVANCED UNIVERSAL FONT SIZE SCALER & LIVE PREVIEW 🔤 -->
        <div style="background:rgba(255,255,255,0.06); border:1.2px solid rgba(248,200,59,0.3); border-radius:20px; padding:14px; margin-bottom:10px; box-shadow:0 4px 15px rgba(0,0,0,0.3);">
          <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
            <div style="font-weight:900; font-size:0.92rem; color:var(--text-main, #FFFDF8); display:flex; align-items:center; gap:6px;">
              <span>🔤</span> पाठ का आकार (Font Size)
            </div>
            <span id="current-font-label" style="font-size:0.75rem; font-weight:800; color:#FDE68A; background:rgba(248,200,59,0.2); padding:2px 8px; border-radius:8px; border:1px solid rgba(248,200,59,0.4);">
              100% सामान्य
            </span>
          </div>

          <p style="font-size:0.72rem; color:var(--text-sub, #CBD5E1); margin:0 0 10px 0; line-height:1.3;">
            आरती, चालीसा, भजन, श्लोक व संपूर्ण ऐप के अक्षरों का आकार अपनी सुविधानुसार बदलें:
          </p>

          <!-- 4 Font Size Target Chips -->
          <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:6px; margin-bottom:12px;">
            <button type="button" onclick="setGlobalFontSize(0.88, this, '88% छोटा')" class="font-scale-chip" data-scale="0.88" style="padding:8px 2px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:var(--text-sub, #CBD5E1); border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center;">
              <div style="font-size:0.95rem; font-weight:900;">A-</div>
              <div style="font-size:0.65rem; margin-top:2px;">छोटा</div>
            </button>

            <button type="button" onclick="setGlobalFontSize(1.0, this, '100% सामान्य')" class="font-scale-chip active" data-scale="1.0" style="padding:8px 2px; border-radius:12px; font-size:0.75rem; font-weight:900; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; cursor:pointer; text-align:center; box-shadow:0 0 12px rgba(248,200,59,0.4);">
              <div style="font-size:1.05rem; font-weight:900;">A</div>
              <div style="font-size:0.65rem; margin-top:2px;">सामान्य ⭐</div>
            </button>

            <button type="button" onclick="setGlobalFontSize(1.15, this, '115% बड़ा')" class="font-scale-chip" data-scale="1.15" style="padding:8px 2px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:var(--text-sub, #CBD5E1); border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center;">
              <div style="font-size:1.15rem; font-weight:900;">A+</div>
              <div style="font-size:0.65rem; margin-top:2px;">बड़ा</div>
            </button>

            <button type="button" onclick="setGlobalFontSize(1.30, this, '130% विशाल')" class="font-scale-chip" data-scale="1.30" style="padding:8px 2px; border-radius:12px; font-size:0.75rem; font-weight:800; background:rgba(255,255,255,0.08); color:var(--text-sub, #CBD5E1); border:1px solid rgba(255,255,255,0.15); cursor:pointer; text-align:center;">
              <div style="font-size:1.25rem; font-weight:900;">A++</div>
              <div style="font-size:0.65rem; margin-top:2px;">विशाल</div>
            </button>
          </div>

          <!-- Live Font Scale Preview Box -->
          <div style="background:rgba(0,0,0,0.3); border:1px dashed rgba(248,200,59,0.35); border-radius:14px; padding:10px; text-align:center;">
            <div style="font-size:0.68rem; color:#FDE68A; margin-bottom:4px; font-weight:800;">👁️ लाइव प्रिव्यू (Live Text Preview):</div>
            <div id="font-live-preview-text" style="font-family:'Tiro Devanagari Hindi', serif; font-size:1rem; font-weight:700; color:var(--text-main, #FFFDF8); line-height:1.5; transition:font-size 0.2s ease;">
              ॥ ॐ नमो भगवते वासुदेवाय नमः ॥<br>
              <span style="font-size:0.85em; opacity:0.9;">श्री राम जय राम जय जय राम</span>
            </div>
          </div>
        </div>"""

if old_font_row in html:
    html = html.replace(old_font_row, new_font_row)
    print("✓ Successfully replaced font size controls in index.html")
else:
    print("Old font row not found directly, checking regex replacement")
    html = re.sub(r'<div class="setting-row">\s*<span>🔤 फॉन्ट साइज़<\/span>[\s\S]*?<\/div>', new_font_row, html)
    print("✓ Replaced via Regex")

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Add Global Font Size Functionality to app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

font_js_code = """
// ══════════════════════════════════════════════════════════════════════════════
// 🔤 UNIVERSAL APP-WIDE FONT SIZE SCALER ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.currentFontScale = parseFloat(localStorage.getItem('sanatan_font_scale') || '1.0');

window.setGlobalFontSize = function(multiplier, btnEl, labelText) {
  window.currentFontScale = multiplier;
  localStorage.setItem('sanatan_font_scale', multiplier.toString());

  // 1. Scale Root HTML Font Size (16px base * multiplier)
  const basePx = 16 * multiplier;
  document.documentElement.style.fontSize = basePx + 'px';
  document.documentElement.style.setProperty('--reader-font', (1.1 * multiplier) + 'rem');
  document.documentElement.style.setProperty('--app-font-multiplier', multiplier.toString());

  // 2. Update Live Preview Text Box
  const preview = document.getElementById('font-live-preview-text');
  if (preview) {
    preview.style.fontSize = (1.0 * multiplier) + 'rem';
  }

  // 3. Update Label
  const lbl = document.getElementById('current-font-label');
  if (lbl) {
    lbl.textContent = labelText || Math.round(multiplier * 100) + '%';
  }

  // 4. Update Active Chip UI
  document.querySelectorAll('.font-scale-chip').forEach(chip => {
    const chipScale = parseFloat(chip.getAttribute('data-scale'));
    if (Math.abs(chipScale - multiplier) < 0.01) {
      chip.classList.add('active');
      chip.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      chip.style.color = '#1A0B2E';
      chip.style.border = 'none';
      chip.style.boxShadow = '0 0 12px rgba(248,200,59,0.4)';
    } else {
      chip.classList.remove('active');
      chip.style.background = 'rgba(255,255,255,0.08)';
      chip.style.color = 'var(--text-sub, #CBD5E1)';
      chip.style.border = '1px solid rgba(255,255,255,0.15)';
      chip.style.boxShadow = 'none';
    }
  });

  if (navigator.vibrate) navigator.vibrate(30);

  if (typeof showToast === 'function') {
    showToast(`🔤 फॉन्ट साइज़ सेट: ${Math.round(multiplier * 100)}%`);
  }
};

// Initialize Font Size on App Launch
window.initAppFontSize = function() {
  const savedScale = parseFloat(localStorage.getItem('sanatan_font_scale') || '1.0');
  const basePx = 16 * savedScale;
  document.documentElement.style.fontSize = basePx + 'px';
  document.documentElement.style.setProperty('--reader-font', (1.1 * savedScale) + 'rem');
  document.documentElement.style.setProperty('--app-font-multiplier', savedScale.toString());

  // Set active chip if settings page is loaded
  const matchingChip = document.querySelector(`.font-scale-chip[data-scale="${savedScale}"]`);
  if (matchingChip) {
    window.setGlobalFontSize(savedScale, matchingChip);
  }
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', window.initAppFontSize);
} else {
  window.initAppFontSize();
}
"""

if 'UNIVERSAL APP-WIDE FONT SIZE SCALER ENGINE' not in app_js:
    with open('app.js', 'a', encoding='utf-8') as f:
        f.write(font_js_code)
    print("✓ Added Universal Font Size Scaler to app.js")
else:
    print("Font Size Scaler already present in app.js")

print(f"✓ Font Size Engine fully synchronized (v={ts})")
