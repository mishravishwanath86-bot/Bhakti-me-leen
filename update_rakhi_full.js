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

        <!-- Description -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <p style="font-size:0.95rem; color:#334155; line-height:1.7; margin:0 0 1rem;">
            Rakhi, which is also known as <strong>Raksha Bandhan</strong>, is a Hindu festival celebrated across India. It is recognized among Hindus for its symbolic significance of the sacred bond between brother and sister.
          </p>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.9rem; color:#475569;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Raksha Bandhan</div>
            <div><strong style="color:var(--maroon);">Significance:</strong> Tying the sacred thread by sisters to their brothers</div>
            <div><strong style="color:var(--maroon);">Deity(s):</strong> Goddess Indrani, Lord Indra</div>
            <div><strong style="color:var(--maroon);">Key Rituals:</strong> Raksha Bandhan Puja, Thread ceremony</div>
            <div><strong style="color:var(--maroon);">Mythological Figures:</strong> Lord Krishna, Yudhishthira, Draupadi, Goddess Indrani, Lord Indra</div>
          </div>
        </div>

        <!-- Date Card 2026 -->
        <div class="sk-date-card" style="background:linear-gradient(135deg,#4a5e2a,#6b8c3a); color:white; padding:1.2rem; border-radius:16px; margin-bottom:1.2rem; text-align:center;">
          <div style="font-size:1rem; font-weight:600; opacity:0.9;">रक्षा बंधन 2026</div>
          <div style="font-size:3rem; font-weight:900; line-height:1.1; margin: 0.3rem 0;">28</div>
          <div style="font-size:1.2rem; font-weight:700;">अगस्त 2026</div>
          <div style="font-size:0.95rem; opacity:0.85; margin-top:0.3rem;">शुक्रवार / Friday</div>
        </div>

        <!-- All years dates -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 रक्षा बंधन तिथियाँ</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.92rem;">
            <div style="color:#475569;">2025: <strong>August 09 (Saturday)</strong></div>
            <div style="color:#a50000; font-weight:700;">2026: August 28 (Friday) ← Current</div>
            <div style="color:#475569;">2027: <strong>August 17 (Tuesday)</strong></div>
            <div style="color:#475569;">2028: <strong>August 05 (Saturday)</strong></div>
          </div>
          <div style="margin-top:1rem; border-top:1px solid #e2e8f0; padding-top:0.8rem; font-size:0.88rem; color:#475569;">
            <div><strong>Hindu Calendar Date:</strong></div>
            <div>Purnimanta - Purnima of Shravana month (Shukla Paksha)</div>
            <div>Amanta - Purnima of Shravana month (Shukla Paksha)</div>
          </div>
        </div>

        <!-- Muhurat Box -->
        <div class="sk-date-card" style="border-left:4px solid var(--saffron); padding:1.2rem; border-radius:12px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">⏰ 2026 राखी बांधने का मुहूर्त</div>
          <div style="font-size:1.05rem; color:#a50000; font-weight:700;">05:57 AM से 09:48 AM</div>
          <div style="font-size:0.85rem; color:#2d6a4f; font-weight:600; margin-top:0.4rem;">✅ भद्रा सूर्योदय से पहले ही समाप्त</div>
          <div style="margin-top:1rem; border-top:1px solid #e2e8f0; padding-top:0.8rem;">
            <div style="font-size:0.85rem; color:#475569; margin-bottom:0.5rem;">📍 पूर्णिमा तिथि आरंभ - 09:08 AM, 27 अगस्त 2026</div>
            <div style="font-size:0.85rem; color:#475569;">📍 पूर्णिमा तिथि समाप्त - 09:48 AM, 28 अगस्त 2026</div>
          </div>
        </div>

        <!-- City-wise Muhurat -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🏙️ 2026 शहर-वार मुहूर्त</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.82rem;">
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">New Delhi</div><div style="color:#334155;">05:57 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Noida</div><div style="color:#334155;">05:56 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Pune</div><div style="color:#334155;">06:19 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Jaipur</div><div style="color:#334155;">06:04 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Mumbai</div><div style="color:#334155;">06:23 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Gurgaon</div><div style="color:#334155;">05:58 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Chennai</div><div style="color:#334155;">05:58 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Bengaluru</div><div style="color:#334155;">06:08 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Kolkata</div><div style="color:#334155;">05:18 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Hyderabad</div><div style="color:#334155;">06:01 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Ahmedabad</div><div style="color:#334155;">06:21 AM – 09:48 AM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Chandigarh</div><div style="color:#334155;">05:57 AM – 09:48 AM</div></div>
          </div>
        </div>

        <!-- Observances -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🙏 अनुष्ठान (Observances)</div>
          <div style="font-size:0.9rem; color:#334155; display:flex; flex-direction:column; gap:0.5rem;">
            <div>💛 Sisters tie Rakhi to their brothers</div>
            <div>🪔 Aarti for brothers with prayers for their long life</div>
            <div>🎁 Brothers offer gifts to their sisters</div>
            <div>🍬 Preparation of delicious recipes</div>
          </div>
        </div>

        <!-- Recipes -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🍬 पारंपरिक व्यंजन (Recipes)</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.9rem;">
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px; text-align:center;">🍮 Gulab Jamun</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px; text-align:center;">🍚 Kheer</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px; text-align:center;">🥥 Coconut Barfi</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px; text-align:center;">🪙 Kaju Katli</div>
          </div>
        </div>

      </div>
    </section>`;

html = html.replace(oldRakhiPage, newRakhiPage);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Updated Rakhi page with complete summary data!');
