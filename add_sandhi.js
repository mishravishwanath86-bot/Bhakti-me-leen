const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const sandhiSection = `
        <!-- Sandhi Puja 2026 -->
        <div class="sk-date-card" style="background:linear-gradient(135deg,#4a0e0e,#7B1C1C); color:white; padding:1.2rem; border-radius:16px; margin-bottom:1.2rem; text-align:center;">
          <div style="font-size:1rem; font-weight:600; opacity:0.9;">संधि पूजा (Sandhi Puja) 2026</div>
          <div style="font-size:3rem; font-weight:900; line-height:1.1; margin: 0.3rem 0;">19</div>
          <div style="font-size:1.2rem; font-weight:700;">अक्टूबर 2026</div>
          <div style="font-size:0.95rem; opacity:0.85; margin-top:0.3rem;">सोमवार / Monday</div>
        </div>

        <!-- Sandhi Puja Muhurat -->
        <div class="sk-date-card" style="border-left:4px solid #a50000; padding:1.2rem; border-radius:12px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">⏰ संधि पूजा मुहूर्त</div>
          <div style="font-size:1.05rem; color:#a50000; font-weight:700;">10:27 AM से 11:15 AM</div>
          <div style="font-size:0.85rem; color:#475569; margin-top:0.3rem; margin-bottom:1rem;">अवधि - 48 मिनट</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.85rem; color:#475569; border-top:1px solid #e2e8f0; padding-top:0.8rem;">
            <div>📍 Ashtami Tithi Begins - 08:27 AM on Oct 18, 2026</div>
            <div>📍 Ashtami Tithi Ends - 10:51 AM on Oct 19, 2026</div>
          </div>
        </div>

        <!-- About Sandhi Puja -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📖 संधि पूजा के बारे में</div>
          <div style="font-size:0.9rem; color:#334155; line-height:1.75; display:flex; flex-direction:column; gap:0.8rem;">
            <p style="margin:0;"><strong>Sandhi Puja</strong> has special significance during Navratri Puja. It is done at the juncture when <strong>Ashtami Tithi</strong> ends and <strong>Navami Tithi</strong> starts.</p>
            <p style="margin:0; background:#fef9ec; padding:0.8rem; border-radius:8px;">It is believed that <strong>Devi Chamunda</strong> appeared during this time to kill demons <strong>Chanda</strong> and <strong>Munda</strong>.</p>
            <p style="margin:0;">Sandhi Puja prevails for two Ghatis which approximately lasts for <strong>48 minutes</strong>. Sandhi Puja Muhurta might fall at any time during the day and Sandhi Puja is done during that time only.</p>
          </div>
        </div>`;

// Inject right after the opening content div in Durga Puja page
html = html.replace(
  /(<section id="page-durgapuja"[\s\S]*?<div class="section-content"[^>]*>)/,
  '$1' + sandhiSection
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Sandhi Puja muhurat to Durga Puja page!');
