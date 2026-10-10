import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

print("======================================================================")
print("🎵 IMPLEMENTING COMPLETE BHAJAN UPLOAD & PLAYBACK SYSTEM")
print("======================================================================")

# 1. Update index.html: Set high z-index on upload modal and add upload button on Bhajan page
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update z-index of upload modal
html = html.replace('id="upload-bhajan-modal" style="display:none; position:fixed; inset:0; z-index:100180;', 'id="upload-bhajan-modal" style="display:none; position:fixed; inset:0; z-index:100250;')

# Add Upload Button to Bhajan Page Header
old_bhajan_header = """    <!-- ══════════ BHAJAN DEITY GRID ══════════ -->
    <section id="page-bhajan" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-home">←</button>
        <h2>भजन</h2>
      </div>"""

new_bhajan_header = """    <!-- ══════════ BHAJAN DEITY GRID ══════════ -->
    <section id="page-bhajan" class="page">
      <div class="page-header-bar" style="display:flex; align-items:center; justify-content:space-between;">
        <div style="display:flex; align-items:center; gap:8px;">
          <button class="back-btn" data-back="page-home">←</button>
          <h2>भजन</h2>
        </div>
        <button onclick="openUploadBhajanModal()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-size:0.75rem; font-weight:900; padding:6px 12px; border-radius:12px; cursor:pointer; display:flex; align-items:center; gap:4px; box-shadow:0 2px 10px rgba(248,200,59,0.35);">
          <span>➕</span> भजन अपलोड
        </button>
      </div>
      
      <!-- User Uploaded Dedicated Bhajans Banner Container -->
      <div id="user-uploaded-bhajans-section" style="display:none; margin: 0 1.1rem 1rem;">
        <div style="font-size:0.85rem; font-weight:900; color:#FDE68A; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
          <span>🎶</span> आपकी समर्पित रचनाएं (My Uploads)
        </div>
        <div id="user-uploaded-bhajans-list" style="display:flex; flex-direction:column; gap:8px;"></div>
      </div>"""

if old_bhajan_header in html:
    html = html.replace(old_bhajan_header, new_bhajan_header)
    print("✓ Added Bhajan Upload Button & Container to page-bhajan in index.html")

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Add complete Bhajan Upload controller into app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

bhajan_upload_code = """
// ══════════════════════════════════════════════════════════════════════════════
// ➕ BHAJAN & DEVOTIONAL CREATION UPLOAD CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.uploadedBhajanBlobUrl = null;
window.uploadedBhajanFileName = null;

window.openUploadBhajanModal = function() {
  const drawer = document.querySelector('.side-drawer');
  if (drawer) drawer.classList.remove('open');
  const overlay = document.getElementById('overlay');
  if (overlay) overlay.style.display = 'none';

  const modal = document.getElementById('upload-bhajan-modal');
  if (modal) {
    modal.style.display = 'flex';
    modal.style.zIndex = '100250';
  }
};

window.closeUploadBhajanModal = function() {
  const modal = document.getElementById('upload-bhajan-modal');
  if (modal) modal.style.display = 'none';
};

window.handleBhajanFileSelected = function(input) {
  if (input.files && input.files[0]) {
    const file = input.files[0];
    window.uploadedBhajanBlobUrl = URL.createObjectURL(file);
    window.uploadedBhajanFileName = file.name;
    const lbl = document.getElementById('upload-file-status-label');
    if (lbl) {
      lbl.textContent = `✓ फ़ाइल चुनी गई: ${file.name} (${(file.size / (1024*1024)).toFixed(1)} MB)`;
      lbl.style.color = '#34D399';
      lbl.style.fontWeight = '900';
    }
    if (navigator.vibrate) navigator.vibrate(30);
    if (typeof showToast === 'function') {
      showToast(`🎵 ऑडियो फ़ाइल चुनी गई: ${file.name}`);
    }
  }
};

window.submitBhajanUpload = function() {
  const titleInput = document.getElementById('upload-bhajan-title');
  const deitySelect = document.getElementById('upload-bhajan-deity');
  const singerInput = document.getElementById('upload-bhajan-singer');
  const lyricsInput = document.getElementById('upload-bhajan-lyrics');

  const title = titleInput ? titleInput.value.trim() : '';
  const deity = deitySelect ? deitySelect.value : 'krishna';
  const singer = singerInput ? singerInput.value.trim() || 'भक्त रचना' : 'भक्त रचना';
  const lyrics = lyricsInput ? lyricsInput.value.trim() : '';

  if (!title) {
    if (typeof showToast === 'function') {
      showToast('⚠️ कृपया भजन का शीर्षक दर्ज करें!');
    } else {
      alert('कृपया भजन का शीर्षक दर्ज करें');
    }
    if (titleInput) titleInput.focus();
    return;
  }

  // Audio source (blob url or fallback devotional track)
  const audioSrc = window.uploadedBhajanBlobUrl || 'assets/audio/bhajan_achyutam_keshavam.mp3';

  // Deity images
  const deityImgs = {
    krishna: 'assets/gallery/bal_krishna_little.jpg',
    shiva: 'assets/gallery/divya_shiva.jpg',
    hanuman: 'assets/gallery/bal_balarama_little.jpg',
    ram: 'assets/gallery/bal_rama.jpg',
    ganesh: 'assets/gallery/bal_ganesha_little.jpg',
    durga: 'assets/gallery/bal_durga_little.jpg',
    laxmi: 'assets/gallery/bal_lakshmi_little.jpg',
    khatushyam: 'assets/gallery/bal_krishna_little.jpg',
    general: 'assets/gallery/bal_vishnu_little.jpg'
  };

  const newBhajan = {
    id: 'user_bhajan_' + Date.now(),
    title: title,
    deity: deity,
    sub: `${singer} • समर्पित रचना`,
    singer: singer,
    img: deityImgs[deity] || 'assets/gallery/bal_krishna_little.jpg',
    src: audioSrc,
    audio_url: audioSrc,
    lyrics: lyrics || `${title}\\n\\n॥ ॐ नमो भगवते वासुदेवाय ॥\\nहरि ॐ तत्सत्`,
    uploadedAt: new Date().toISOString()
  };

  // Save to localStorage
  let userBhajans = [];
  try {
    userBhajans = JSON.parse(localStorage.getItem('sanatan_user_uploaded_bhajans') || '[]');
  } catch(e) { userBhajans = []; }
  userBhajans.unshift(newBhajan);
  localStorage.setItem('sanatan_user_uploaded_bhajans', JSON.stringify(userBhajans));

  // Award +25 Punya Points
  if (typeof window.awardPunyaPoints === 'function') {
    window.awardPunyaPoints(25, 'भजन समर्पण');
  } else if (window.SadhanaProfile) {
    window.SadhanaProfile.punya_points += 25;
    if (typeof window.saveSadhanaProfileState === 'function') window.saveSadhanaProfileState();
    if (typeof window.renderSadhanaShieldVaultUI === 'function') window.renderSadhanaShieldVaultUI();
  }

  // Reset Form
  if (titleInput) titleInput.value = '';
  if (singerInput) singerInput.value = '';
  if (lyricsInput) lyricsInput.value = '';
  const lbl = document.getElementById('upload-file-status-label');
  if (lbl) {
    lbl.textContent = 'ऑडियो फ़ाइल चुनें (MP3 / M4A)';
    lbl.style.color = '#FDE68A';
  }

  window.closeUploadBhajanModal();

  // Play Victory FX
  if (navigator.vibrate) navigator.vibrate([60, 40, 100]);
  if (typeof playSoundEffect === 'function') playSoundEffect('victory');
  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();

  if (typeof showToast === 'function') {
    showToast(`🚩 भजन "${title}" प्रभु को समर्पित! (+25 अंक अर्जित 🙏)`);
  }

  // Refresh User Uploads Section on Bhajan Page
  window.renderUserUploadedBhajans();

  // Play the newly uploaded bhajan immediately
  setTimeout(() => {
    window.playUserUploadedBhajan(newBhajan);
  }, 500);
};

window.renderUserUploadedBhajans = function() {
  const section = document.getElementById('user-uploaded-bhajans-section');
  const list = document.getElementById('user-uploaded-bhajans-list');
  if (!section || !list) return;

  let userBhajans = [];
  try {
    userBhajans = JSON.parse(localStorage.getItem('sanatan_user_uploaded_bhajans') || '[]');
  } catch(e) { userBhajans = []; }

  if (userBhajans.length === 0) {
    section.style.display = 'none';
    return;
  }

  section.style.display = 'block';
  list.innerHTML = '';

  userBhajans.forEach(item => {
    const card = document.createElement('div');
    card.style.cssText = 'background:linear-gradient(135deg, rgba(248,200,59,0.15) 0%, rgba(217,119,6,0.08) 100%); border:1.3px solid #F8C83B; border-radius:16px; padding:10px 12px; display:flex; align-items:center; justify-content:space-between; cursor:pointer; box-shadow:0 4px 15px rgba(0,0,0,0.3);';
    card.onclick = () => window.playUserUploadedBhajan(item);

    card.innerHTML = `
      <div style="display:flex; align-items:center; gap:10px;">
        <img src="${item.img}" style="width:44px; height:44px; border-radius:12px; object-fit:cover; border:1px solid #F8C83B;" onerror="this.src='assets/gallery/bal_krishna_little.jpg'" />
        <div>
          <div style="color:#FFFDF8; font-size:0.88rem; font-weight:900;">${item.title}</div>
          <div style="color:#FDE68A; font-size:0.7rem; margin-top:2px;">${item.sub}</div>
        </div>
      </div>
      <div style="width:34px; height:34px; border-radius:50%; background:linear-gradient(135deg, #F8C83B, #D97706); display:flex; align-items:center; justify-content:center; color:#1A0B2E; font-size:0.95rem; font-weight:900; box-shadow:0 2px 8px rgba(248,200,59,0.4);">
        ▶
      </div>
    `;

    list.appendChild(card);
  });
};

window.playUserUploadedBhajan = function(item) {
  if (!item) return;

  // If audio element exists, play audio
  let audio = document.getElementById('core-app-audio');
  if (!audio) {
    audio = new Audio();
    audio.id = 'core-app-audio';
    document.body.appendChild(audio);
  }

  audio.src = item.src || item.audio_url;
  audio.play().catch(e => console.log('Audio autoplay prevented:', e));

  // Open Glass Player if available
  if (typeof window.openGlassPlayer === 'function') {
    window.openGlassPlayer();
  }

  // Update Mini Player / Glass Player titles
  const titleEls = document.querySelectorAll('#player-katha-title, #mini-player-title, #glass-player-title');
  titleEls.forEach(el => { if (el) el.textContent = item.title; });

  const subEls = document.querySelectorAll('#player-katha-deity, #mini-player-sub, #glass-player-subtitle');
  subEls.forEach(el => { if (el) el.textContent = item.sub || item.singer; });

  if (typeof showToast === 'function') {
    showToast(`🎶 अब बज रहा है: ${item.title}`);
  }
};

// Initialize render on page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', window.renderUserUploadedBhajans);
} else {
  window.renderUserUploadedBhajans();
}
"""

if 'BHAJAN & DEVOTIONAL CREATION UPLOAD CONTROLLER' in app_js:
    app_js = re.sub(r'// ══════════════════════════════════════════════════════════════════════════════\s*// ➕ BHAJAN & DEVOTIONAL CREATION UPLOAD CONTROLLER[\s\S]*', '', app_js)

app_js += '\n\n' + bhajan_upload_code

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("✓ Added complete Bhajan Upload Controller to app.js")
print("✓ Bhajan Upload System fully synchronized!")
