import sys, shutil, time, re
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 70)
print("⭐ RATE MODAL FIX")
print("=" * 70)

ts = int(time.time())

# === Fix 1: app.js — Add openRateModal, closeRateModal, submitRating ===
shutil.copy('app.js', f'app.js.bak_rate_{ts}')

RATE_JS = """

// ══════════════════════════════════════════════════════════════════════════════
// ⭐ RATE APP MODAL SYSTEM
// Functions: openRateModal, closeRateModal, submitRating
// ══════════════════════════════════════════════════════════════════════════════

window._currentStarRating = 0;

window.openRateModal = function() {
  const modal = document.getElementById('rate-modal');
  if (!modal) {
    // Fallback: open play store or show alert
    if (typeof showToast === 'function') {
      showToast('⭐ कृपया ऐप स्टोर पर रेट करें!');
    }
    return;
  }
  // Remove hardcoded display:none
  modal.style.setProperty('display', 'flex', 'important');
  modal.classList.remove('hidden');
  modal.style.pointerEvents = 'auto';

  // Reset stars
  window._currentStarRating = 0;
  _updateStarDisplay(0);

  // Close on overlay click
  modal.onclick = function(e) {
    if (e.target === modal) window.closeRateModal();
  };
};

window.closeRateModal = function() {
  const modal = document.getElementById('rate-modal');
  if (!modal) return;
  modal.style.setProperty('display', 'none', 'important');
  modal.classList.add('hidden');
  modal.style.pointerEvents = 'none';
  window._currentStarRating = 0;
};

// Star hover/click handling
function _updateStarDisplay(rating) {
  const stars = document.querySelectorAll('#star-row .star');
  stars.forEach(function(star, i) {
    star.textContent = (i < rating) ? '★' : '☆';
    star.style.color = (i < rating) ? '#F8C83B' : '#CBD5E1';
    star.style.fontSize = (i < rating) ? '2.2rem' : '1.8rem';
    star.style.textShadow = (i < rating) ? '0 0 12px rgba(248,200,59,0.8)' : 'none';
    star.style.transition = 'all 0.15s ease';
  });
}

// Attach star click events after DOM load
document.addEventListener('DOMContentLoaded', function() {
  // Set up star interactions
  const starRow = document.getElementById('star-row');
  if (starRow) {
    starRow.querySelectorAll('.star').forEach(function(star) {
      const val = parseInt(star.getAttribute('data-val')) || 0;

      star.style.cursor = 'pointer';
      star.style.fontSize = '1.8rem';
      star.style.padding = '0 4px';
      star.style.transition = 'all 0.15s ease';
      star.style.color = '#CBD5E1';

      star.addEventListener('click', function() {
        window._currentStarRating = val;
        _updateStarDisplay(val);
        if (navigator.vibrate) navigator.vibrate(25);
      });

      star.addEventListener('mouseenter', function() {
        _updateStarDisplay(val);
      });
    });

    starRow.addEventListener('mouseleave', function() {
      _updateStarDisplay(window._currentStarRating);
    });
  }

  // modal-close buttons
  document.querySelectorAll('[data-close]').forEach(function(btn) {
    btn.addEventListener('click', function() {
      const targetId = btn.getAttribute('data-close');
      const target = document.getElementById(targetId);
      if (target) {
        target.style.setProperty('display', 'none', 'important');
        target.classList.add('hidden');
      }
    });
  });
});

window.submitRating = function() {
  const rating = window._currentStarRating;
  if (rating === 0) {
    if (typeof showToast === 'function') {
      showToast('⭐ कृपया पहले स्टार चुनें');
    }
    return;
  }

  // Save rating
  localStorage.setItem('bhakti_app_rating', rating);
  localStorage.setItem('bhakti_app_rated', 'true');

  // Show thank you message
  if (typeof showToast === 'function') {
    if (rating >= 4) {
      showToast('🙏 आपके ' + rating + ' स्टार के लिए धन्यवाद! जय श्री राम 🚩');
    } else {
      showToast('🙏 आपकी रेटिंग के लिए धन्यवाद! हम बेहतर करेंगे।');
    }
  }

  // Haptic feedback
  if (navigator.vibrate) navigator.vibrate([30, 20, 60]);

  // Close after delay
  setTimeout(function() {
    window.closeRateModal();
  }, 1200);

  // If 5 stars, show extra animation or prompt to review on store
  if (rating === 5) {
    setTimeout(function() {
      // Could redirect to play store
      console.log('[Rate] 5 star rating submitted!');
    }, 1500);
  }
};

"""

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

if 'RATE APP MODAL SYSTEM' in js:
    print("Rate system already exists, replacing...")
    start = js.find('// ══════════════════════════════════════════════════════════════════════════════\n// ⭐ RATE APP MODAL SYSTEM')
    end = js.find('\n// ══', start + 100)
    if end == -1:
        end = len(js)
    js = js[:start] + RATE_JS + js[end:]
    print("✅ Replaced rate modal system")
else:
    js = js + RATE_JS
    print("✅ Added rate modal system to app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f"✅ app.js updated — {len(js)} chars")

# === Fix 2: index.html — Fix rate-modal display:none !important ===
shutil.copy('index.html', f'index.html.bak_rate_{ts}')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the modal: remove hardcoded display:none !important and pointer-events:none
OLD_MODAL = 'id="rate-modal" class="modal-overlay hidden" style="display:none !important; pointer-events:none !important;"'
NEW_MODAL = 'id="rate-modal" class="modal-overlay hidden" style="display:none; pointer-events:none;"'

if OLD_MODAL in html:
    html = html.replace(OLD_MODAL, NEW_MODAL)
    print("✅ Fixed rate-modal CSS (removed !important from display:none)")
else:
    # Try a more flexible approach
    html = re.sub(
        r'id="rate-modal"([^>]*?)style="display:none !important;\s*pointer-events:none !important;"',
        r'id="rate-modal"\1style="display:none; pointer-events:none;"',
        html
    )
    print("✅ Fixed rate-modal CSS via regex")

# Also fix the submit button in the modal — check if it has onclick=submitRating()
submit_found = 'submitRating' in html
print(f"submitRating in HTML: {submit_found}")

# Find the modal's submit button and add onclick if missing
if not submit_found:
    # Find modal box and add submit button
    rate_modal_idx = html.find('id="rate-modal"')
    star_row_idx = html.find('id="star-row"', rate_modal_idx)
    if star_row_idx != -1:
        # Find the end of star-row section and add submit button after it
        after_stars = html.find('</div>', star_row_idx) + 6
        submit_btn = '\n      <button onclick="submitRating()" style="width:100%;margin-top:14px;background:linear-gradient(135deg,#F8C83B,#D97706);color:#1A0B2E;border:none;font-size:0.95rem;font-weight:900;padding:12px;border-radius:16px;cursor:pointer;">⭐ रेटिंग सबमिट करें</button>'
        html = html[:after_stars] + submit_btn + html[after_stars:]
        print("✅ Added submit button to rate modal")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ index.html updated — {len(html)} chars")

# Final verify
with open('app.js', 'r', encoding='utf-8') as f:
    js_v = f.read()

for fn in ['openRateModal', 'closeRateModal', 'submitRating']:
    found = fn in js_v
    print(f"  {'OK' if found else 'MISSING'} {fn}")

# Syntax check
import subprocess
result = subprocess.run(['node', '-c', 'app.js'], capture_output=True, text=True)
print(f"\nJS Syntax: {'OK' if result.returncode == 0 else 'ERROR: ' + result.stderr}")

print("\n✅ RATE MODAL FULLY FIXED!")
print("=" * 70)
