import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

# 1. Add Upload Bhajan Modal to index.html and wire drawer-upload
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update drawer-upload button
html = html.replace(
    '<button class="drawer-item" id="drawer-upload"><span class="di">➕</span><span>भजन अपलोड</span></button>',
    '<button class="drawer-item" id="drawer-upload" onclick="openUploadBhajanModal()"><span class="di">➕</span><span>भजन अपलोड</span></button>'
)

# Upload Modal HTML
upload_modal_html = """
  <!-- ➕ DEDICATED BHAJAN & DEVOTIONAL CREATION UPLOAD MODAL ➕ -->
  <div id="upload-bhajan-modal" style="display:none; position:fixed; inset:0; z-index:100180; background:rgba(10,2,18,0.94); backdrop-filter:blur(22px); -webkit-backdrop-filter:blur(22px); align-items:center; justify-content:center; padding:1.2rem; overflow-y:auto;">
    <div style="width:100%; max-width:420px; background:linear-gradient(160deg, #2E104A 0%, #1A052E 60%, #0D0218 100%); border:2px solid #F8C83B; border-radius:28px; padding:1.5rem 1.3rem; text-align:left; box-shadow:0 25px 70px rgba(0,0,0,0.95); position:relative; animation:fadeInUp 0.3s ease; max-height:92vh; overflow-y:auto;">
      
      <!-- Close Button -->
      <button onclick="closeUploadBhajanModal()" style="position:absolute; top:14px; right:14px; background:rgba(255,255,255,0.1); border:none; color:#FDE68A; width:32px; height:32px; border-radius:50%; font-size:1.1rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">✕</button>

      <!-- Header -->
      <div style="text-align:center; margin-bottom:14px;">
        <div style="width:60px; height:60px; border-radius:50%; background:linear-gradient(135deg, #F8C83B, #D97706); display:flex; align-items:center; justify-content:center; font-size:1.8rem; margin:0 auto 8px; box-shadow:0 0 20px rgba(248,200,59,0.5);">
          🎶
        </div>
        <h3 style="font-size:1.25rem; font-weight:900; color:#FFFDF8; margin:0 0 2px 0;">
          भजन व भक्ति रचना समर्पित करें
        </h3>
        <p style="font-size:0.75rem; color:#CBD5E1; margin:0;">
          अपनी स्वरचित या पसंदीदा भक्ति रचना प्रभु के चरणों में अर्पित करें
        </p>
      </div>

      <!-- Form Inputs -->
      <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:14px;">
        
        <!-- 1. Title -->
        <div>
          <label style="font-size:0.75rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            📝 भजन का शीर्षक (Title) *
          </label>
          <input type="text" id="upload-bhajan-title" placeholder="उदा. मेरो राधा रमण गिरधारी..." style="width:100%; background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.35); border-radius:14px; padding:9px 12px; color:#FFFDF8; font-size:0.85rem; outline:none; box-sizing:border-box;" />
        </div>

        <!-- 2. Deity Category -->
        <div>
          <label style="font-size:0.75rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            🕉️ इष्टदेव / श्रेणी (Deity / Category) *
          </label>
          <select id="upload-bhajan-deity" style="width:100%; background:rgba(42,13,78,0.9); border:1.2px solid rgba(248,200,59,0.35); border-radius:14px; padding:9px 12px; color:#FFFDF8; font-size:0.85rem; outline:none; box-sizing:border-box; cursor:pointer;">
            <option value="krishna">🪷 श्री कृष्ण / राधा रानी</option>
            <option value="shiva">🔱 भगवान शिव (महाकाल)</option>
            <option value="hanuman">🚩 हनुमान जी (बजरंगबली)</option>
            <option value="ram">🏹 मर्यादा पुरुषोत्तम श्री राम</option>
            <option value="ganesh">🌺 श्री गणेश जी</option>
            <option value="durga">🌺 माँ भगवती दुर्गा</option>
            <option value="laxmi">🪷 माँ लक्ष्मी</option>
            <option value="khatushyam">🪔 श्री खाटू श्याम जी</option>
            <option value="general">✨ अन्य सनातन भजन</option>
          </select>
        </div>

        <!-- 3. Singer / Author -->
        <div>
          <label style="font-size:0.75rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            👤 गायक / रचयिता का नाम (Singer / Author)
          </label>
          <input type="text" id="upload-bhajan-singer" placeholder="उदा. भक्त कबीर, अनूप जलोटा या स्वरचित..." style="width:100%; background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.35); border-radius:14px; padding:9px 12px; color:#FFFDF8; font-size:0.85rem; outline:none; box-sizing:border-box;" />
        </div>

        <!-- 4. Audio File Upload or URL -->
        <div>
          <label style="font-size:0.75rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            🎵 ऑडियो फ़ाइल (.MP3) या लिंक
          </label>
          <div style="border:1.5px dashed rgba(248,200,59,0.45); border-radius:16px; padding:12px; text-align:center; background:rgba(0,0,0,0.25); cursor:pointer;" onclick="document.getElementById('upload-bhajan-file-input').click()">
            <input type="file" id="upload-bhajan-file-input" accept="audio/*" onchange="handleBhajanFileSelected(this)" style="display:none;" />
            <div style="font-size:1.6rem; margin-bottom:2px;">📁</div>
            <div id="upload-file-status-label" style="font-size:0.78rem; font-weight:800; color:#FDE68A;">
              ऑडियो फ़ाइल चुनें (MP3 / M4A)
            </div>
            <div style="font-size:0.65rem; color:#CBD5E1; margin-top:2px;">या सीधे डिवाइस से अपलोड करें</div>
          </div>
        </div>

        <!-- 5. Lyrics -->
        <div>
          <label style="font-size:0.75rem; font-weight:800; color:#FDE68A; display:block; margin-bottom:4px;">
            📜 भजन के बोल / लिरिक्स (Lyrics)
          </label>
          <textarea id="upload-bhajan-lyrics" rows="3" placeholder="भजन के पावन बोल यहाँ लिखें..." style="width:100%; background:rgba(255,255,255,0.08); border:1.2px solid rgba(248,200,59,0.35); border-radius:14px; padding:9px 12px; color:#FFFDF8; font-size:0.82rem; outline:none; box-sizing:border-box; resize:none; font-family:inherit;"></textarea>
        </div>

      </div>

      <!-- Reward Badge -->
      <div style="background:rgba(248,200,59,0.15); border:1px solid #F8C83B; border-radius:12px; padding:6px 12px; text-align:center; margin-bottom:14px;">
        <span style="font-size:0.75rem; font-weight:900; color:#FDE68A;">🎁 सफल समर्पण पर +25 साधना अंक प्राप्त होंगे!</span>
      </div>

      <!-- Action Buttons -->
      <button onclick="submitBhajanUpload()" style="width:100%; background:linear-gradient(135deg, #F8C83B 0%, #D97706 100%); color:#1A0B2E; border:none; font-size:0.95rem; font-weight:900; padding:12px 0; border-radius:16px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); text-align:center; display:flex; align-items:center; justify-content:center; gap:6px;">
        <span>🚩</span> प्रभु को समर्पित करें (Upload & Publish) ➔
      </button>

    </div>
  </div>
"""

if 'id="upload-bhajan-modal"' not in html:
    html = html.replace('<!-- ===== SPLASH SCREEN ===== -->', upload_modal_html + '\n  <!-- ===== SPLASH SCREEN ===== -->')
    print("✓ Added #upload-bhajan-modal into index.html")

ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Add Bhajan Upload JS Controller in app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

upload_js_code = """
// ══════════════════════════════════════════════════════════════════════════════
// ➕ BHAJAN & DEVOTIONAL UPLOAD ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.uploadedBhajanBlobUrl = null;

window.openUploadBhajanModal = function() {
  const drawer = document.querySelector('.app-drawer');
  if (drawer) drawer.classList.remove('open');
  const overlay = document.querySelector('.drawer-overlay');
  if (overlay) overlay.style.display = 'none';

  const modal = document.getElementById('upload-bhajan-modal');
  if (modal) modal.style.display = 'flex';
};

window.closeUploadBhajanModal = function() {
  const modal = document.getElementById('upload-bhajan-modal');
  if (modal) modal.style.display = 'none';
};

window.handleBhajanFileSelected = function(input) {
  if (input.files && input.files[0]) {
    const file = input.files[0];
    window.uploadedBhajanBlobUrl = URL.createObjectURL(file);
    const lbl = document.getElementById('upload-file-status-label');
    if (lbl) {
      lbl.textContent = `✓ फ़ाइल चुनी गई: ${file.name} (${(file.size / (1024*1024)).toFixed(1)} MB)`;
      lbl.style.color = '#34D399';
    }
    if (navigator.vibrate) navigator.vibrate(30);
  }
};

window.submitBhajanUpload = function() {
  const title = document.getElementById('upload-bhajan-title')?.value.trim();
  const deity = document.getElementById('upload-bhajan-deity')?.value || 'krishna';
  const singer = document.getElementById('upload-bhajan-singer')?.value.trim() || 'भक्त रचना';
  const lyrics = document.getElementById('upload-bhajan-lyrics')?.value.trim() || '';

  if (!title) {
    if (typeof showToast === 'function') showToast('⚠️ कृपया भजन का शीर्षक दर्ज करें');
    return;
  }

  const audioSrc = window.uploadedBhajanBlobUrl || 'assets/audio/bhajan_achyutam_keshavam.mp3';

  const newBhajan = {
    id: 'user_bhajan_' + Date.now(),
    title: title,
    deity: deity,
    sub: `${singer} • समर्पित रचना`,
    img: 'assets/gallery/bal_krishna_little.jpg',
    src: audioSrc,
    lyrics: lyrics,
    uploadedAt: new Date().toISOString()
  };

  // Save to localStorage
  let uploadedList = JSON.parse(localStorage.getItem('sanatan_user_uploaded_bhajans') || '[]');
  uploadedList.unshift(newBhajan);
  localStorage.setItem('sanatan_user_uploaded_bhajans', JSON.stringify(uploadedList));

  // Add 25 Punya points
  let currentPoints = parseInt(localStorage.getItem('sanatan_sadhana_points') || '108');
  currentPoints += 25;
  localStorage.setItem('sanatan_sadhana_points', currentPoints.toString());

  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
  if (typeof playSoundEffect === 'function') playSoundEffect('victory');

  window.closeUploadBhajanModal();

  if (typeof showToast === 'function') {
    showToast(`🚩 भजन "${title}" सफलतापूर्वक समर्पित! (+25 अंक अर्जित 🙏)`);
  }

  // Play newly uploaded bhajan immediately in audio player
  if (typeof window.playTrack === 'function') {
    setTimeout(() => {
      window.playTrack(newBhajan);
    }, 600);
  }
};
"""

if 'BHAJAN & DEVOTIONAL UPLOAD ENGINE' not in app_js:
    with open('app.js', 'a', encoding='utf-8') as f:
        f.write(upload_js_code)
    print("✓ Added Bhajan Upload Engine to app.js")
else:
    print("Bhajan Upload Engine already in app.js")

print(f"✓ Bhajan Upload fully synchronized and live (v={ts})")
