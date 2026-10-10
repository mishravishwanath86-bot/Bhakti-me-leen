const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const navamiSection = `
        <!-- Navami Homa 2026 -->
        <div class="sk-date-card" style="background:linear-gradient(135deg,#4a5e2a,#6b8c3a); color:white; padding:1.2rem; border-radius:16px; margin-bottom:1.2rem; text-align:center;">
          <div style="font-size:1rem; font-weight:600; opacity:0.9;">नवमी हवन (Navami Homa) 2026</div>
          <div style="font-size:2.5rem; font-weight:900; line-height:1.1; margin: 0.3rem 0;">19 व 20</div>
          <div style="font-size:1.2rem; font-weight:700;">अक्टूबर 2026</div>
          <div style="font-size:0.9rem; opacity:0.85; margin-top:0.3rem;">सोमवार / Monday &amp; मंगलवार / Tuesday</div>
        </div>

        <!-- Navami Homa Muhurat -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">⏰ नवमी हवन मुहूर्त</div>

          <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; margin-bottom:0.8rem;">
            <div style="font-size:0.85rem; font-weight:700; color:#475569; margin-bottom:0.3rem;">Monday, October 19, 2026 (Sayana Homa)</div>
            <div style="font-size:1rem; color:#a50000; font-weight:700;">10:51 AM से 05:48 PM</div>
            <div style="font-size:0.82rem; color:#475569; margin-top:0.2rem;">अवधि - 6 घंटे 56 मिनट</div>
          </div>

          <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; margin-bottom:0.8rem;">
            <div style="font-size:0.85rem; font-weight:700; color:#475569; margin-bottom:0.3rem;">Tuesday, October 20, 2026 (Pratah Homa)</div>
            <div style="font-size:1rem; color:#a50000; font-weight:700;">06:25 AM से 12:50 PM</div>
            <div style="font-size:0.82rem; color:#475569; margin-top:0.2rem;">अवधि - 6 घंटे 25 मिनट</div>
          </div>

          <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.83rem; color:#475569; border-top:1px solid #e2e8f0; padding-top:0.8rem;">
            <div>📍 Navami Tithi Begins - 10:51 AM on Oct 19, 2026</div>
            <div>📍 Navami Tithi Ends - 12:50 PM on Oct 20, 2026</div>
            <div>📍 Maha Navami - Monday, October 19, 2026</div>
          </div>
        </div>

        <!-- About Navami Homa -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📖 नवमी हवन के बारे में</div>
          <div style="font-size:0.88rem; color:#334155; line-height:1.75; display:flex; flex-direction:column; gap:0.7rem;">
            <p style="margin:0;"><strong>Navami Homa</strong> is also known as <strong>Chandi Homa</strong>, <strong>Chandi Homam</strong> or <strong>Navami Hawan</strong>. People perform it to please Goddess Durga and seek Her blessings for good health and victory over all obstacles in life.</p>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;">
              🔥 Most people perform Navami Homa while chanting <strong>700 verses from Durga Saptashati</strong>. <strong>Aahuti (आहुति)</strong> is done on each verse. Hence one needs at least <strong>2 to 3 hours</strong> to perform ritualistically minimum Homam.
            </div>
            <p style="margin:0; font-size:0.85rem; color:#475569;">Note: Navami Homa is done during <strong>day time only</strong> as Homa done during night is not fruitful.</p>
          </div>
        </div>`;

// Inject after the opening content div of Navratri page
html = html.replace(
  /(<section id="page-navratri"[\s\S]*?<div class="section-content"[^>]*>)/,
  '$1' + navamiSection
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Navami Homa data to Navratri page!');
