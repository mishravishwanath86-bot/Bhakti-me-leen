const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const holiPage = `
    <!-- 🌺 HOLI PAGE 🌺 -->
    <section id="page-holi" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-top10">❮</button>
        <h2>होली (Holi)</h2>
        <span style="width:36px"></span>
      </div>
      
      <div class="sankashti-hero">
        <img src="assets/top10_2.jpg" alt="Holi Hero" style="width:100%; height:220px; object-fit:cover;">
        <div class="sh-overlay">
          <h1>होली (Holi)</h1>
          <p>रंगों का महापर्व</p>
        </div>
      </div>

      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding: 1.5rem 1rem 4rem;">
        
        <!-- Holika Dahan Date Card -->
        <div class="sk-date-card" style="background:linear-gradient(135deg,#8B0000,#c0392b); color:white; padding:1.2rem; border-radius:16px; margin-bottom:1.2rem; text-align:center;">
          <div style="font-size:1rem; font-weight:600; opacity:0.9;">होलिका दहन (Holika Dahan)</div>
          <div style="font-size:3rem; font-weight:900; line-height:1.1; margin: 0.3rem 0;">21</div>
          <div style="font-size:1.2rem; font-weight:700;">मार्च 2027</div>
          <div style="font-size:0.95rem; opacity:0.85; margin-top:0.3rem;">रविवार / Sunday</div>
        </div>

        <!-- Muhurat Box -->
        <div class="sk-date-card" style="border-left:4px solid var(--saffron); padding:1.2rem; border-radius:12px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🔥 होलिका दहन मुहूर्त</div>
          <div style="font-size:1.05rem; color:#a50000; font-weight:700;">06:33 PM से 08:55 PM</div>
          <div style="font-size:0.85rem; color:#475569; margin-top:0.3rem;">अवधि - 2 घंटे 22 मिनट</div>
          <div style="border-top:1px solid #e2e8f0; margin-top:1rem; padding-top:1rem; display:flex; flex-direction:column; gap:0.5rem;">
            <div style="font-size:0.88rem; color:#475569;">📍 भद्रा पुंछा - 01:26 AM से 02:31 AM, मार्च 22</div>
            <div style="font-size:0.88rem; color:#475569;">📍 भद्रा मुखा - 02:31 AM से 04:20 AM, मार्च 22</div>
            <div style="font-size:0.88rem; color:#475569;">📍 पूर्णिमा तिथि आरंभ - 06:21 PM, मार्च 21</div>
            <div style="font-size:0.88rem; color:#475569;">📍 पूर्णिमा तिथि समाप्त - 04:13 PM, मार्च 22</div>
          </div>
        </div>

        <!-- Rangwali Holi -->
        <div class="sk-date-card" style="background:linear-gradient(135deg,#e74c3c,#f39c12); color:white; padding:1.2rem; border-radius:16px; margin-bottom:1.2rem; text-align:center;">
          <div style="font-size:0.95rem; font-weight:600; opacity:0.9;">रंगवाली होली (Dhulandi)</div>
          <div style="font-size:1.8rem; font-weight:900; margin: 0.3rem 0;">सोमवार, 22 मार्च 2027</div>
        </div>

        <!-- Links Section -->
        <div style="display:flex; flex-direction:column; gap:0.8rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.4rem;">📎 अधिक जानकारी</div>
          <a href="https://www.Sanatan Panchang.com/festivals/holi/info/holi.html" style="display:flex; align-items:center; gap:0.8rem; background:#fff; padding:1rem; border-radius:12px; text-decoration:none; border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.07);">
            <span style="font-size:1.4rem;">🎨</span>
            <div><div style="font-size:0.95rem; font-weight:700; color:var(--maroon);">होली (Holi) Dhulandi</div><div style="font-size:0.8rem; color:#64748b;">Sanatan Panchang.com</div></div>
          </a>
          <a href="https://www.Sanatan Panchang.com/festivals/holi/festivals-holika-dahan-timings.html" style="display:flex; align-items:center; gap:0.8rem; background:#fff; padding:1rem; border-radius:12px; text-decoration:none; border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.07);">
            <span style="font-size:1.4rem;">🔥</span>
            <div><div style="font-size:0.95rem; font-weight:700; color:var(--maroon);">Holika Dahan Muhurat</div><div style="font-size:0.8rem; color:#64748b;">Sanatan Panchang.com</div></div>
          </a>
        </div>

      </div>
    </section>
`;

html = html.replace(/<\/body>/, holiPage + '\n  </body>');
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Holi page to index.html!');
