const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const oldRakhiPage = html.match(/<!-- 🌺 RAKHI PAGE 🌺 -->[\s\S]*?<\/section>/)[0];

const newRakhiPage = `<!-- 🌺 RAKHI PAGE 🌺 -->
    <section id="page-rakhi" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-top10">❮</button>
        <h2>रक्षा बंधन (Rakhi)</h2>
        <span style="width:36px"></span>
      </div>
      
      <div class="sankashti-hero">
        <img src="assets/top10_3.jpg" alt="Raksha Bandhan" style="width:100%; height:220px; object-fit:cover;">
        <div class="sh-overlay">
          <h1>रक्षा बंधन</h1>
          <p>भाई-बहन के प्रेम का पावन पर्व</p>
        </div>
      </div>

      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding: 1.5rem 1rem 4rem;">

        <!-- 2026 Date Card -->
        <div class="sk-date-card" style="background:linear-gradient(135deg,#4a5e2a,#6b8c3a); color:white; padding:1.2rem; border-radius:16px; margin-bottom:1.2rem; text-align:center;">
          <div style="font-size:1rem; font-weight:600; opacity:0.9;">रक्षा बंधन (Raksha Bandhan)</div>
          <div style="font-size:3rem; font-weight:900; line-height:1.1; margin: 0.3rem 0;">28</div>
          <div style="font-size:1.2rem; font-weight:700;">अगस्त 2026</div>
          <div style="font-size:0.95rem; opacity:0.85; margin-top:0.3rem;">शुक्रवार / Friday</div>
        </div>

        <!-- Muhurat Box -->
        <div class="sk-date-card" style="border-left:4px solid var(--saffron); padding:1.2rem; border-radius:12px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">⏰ राखी बांधने का मुहूर्त</div>
          <div style="font-size:1.1rem; color:#a50000; font-weight:700;">05:57 AM से 09:48 AM</div>
          <div style="font-size:0.85rem; color:#475569; margin-top:0.3rem;">अवधि - 3 घंटे 51 मिनट</div>
          <div style="margin-top:1rem; border-top:1px solid #e2e8f0; padding-top:1rem; display:flex; flex-direction:column; gap:0.6rem;">
            <div style="font-size:0.88rem; color:#2d6a4f; font-weight:600;">✅ रक्षा बंधन भद्रा - सूर्योदय से पहले समाप्त</div>
            <div style="font-size:0.88rem; color:#475569;">📍 पूर्णिमा तिथि आरंभ - 09:08 AM, 27 अगस्त 2026</div>
            <div style="font-size:0.88rem; color:#475569;">📍 पूर्णिमा तिथि समाप्त - 09:48 AM, 28 अगस्त 2026</div>
          </div>
        </div>

        <!-- About -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📖 राखी के बारे में</div>
          <div style="font-size:0.9rem; color:#334155; line-height:1.75; display:flex; flex-direction:column; gap:0.8rem;">
            <p style="margin:0;">Raksha Bandhan is celebrated in <strong>Shravana month</strong> during full moon day or Purnima day.</p>
            <p style="margin:0;">The best time to tie Rakhi is during <strong>Aparahna</strong> (late afternoon). If Aparahna time is not available then <strong>Pradosh time</strong> is also suitable.</p>
            <p style="margin:0;">Raksha Bandhan rituals should <strong style="color:#a50000;">NOT</strong> be done during <strong>Bhadra</strong>. Bhadra is malicious time which should be avoided for all auspicious work.</p>
          </div>
        </div>

        <!-- Key Info -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">✨ मुख्य जानकारी</div>
          <div style="font-size:0.9rem; color:#334155; display:flex; flex-direction:column; gap:0.6rem;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Rakhi Purnima, Rakhi</div>
            <div><strong style="color:var(--maroon);">Hindu Calendar:</strong> Purnima of Shravana month</div>
            <div><strong style="color:var(--maroon);">Significance:</strong> Sacred bond of love between brother and sister</div>
            <div><strong style="color:var(--maroon);">Key Ritual:</strong> Sister ties Rakhi on brother's wrist, brother vows to protect sister</div>
            <div><strong style="color:var(--maroon);">Vrat Katha:</strong> Story of Lord Indra and his wife Shachi</div>
          </div>
        </div>

      </div>
    </section>`;

html = html.replace(oldRakhiPage, newRakhiPage);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Updated Rakhi page with full 2026 data!');
