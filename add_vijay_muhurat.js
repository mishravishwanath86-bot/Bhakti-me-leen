const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const muhurateSection = `
        <!-- Vijayadashami Date 2026 -->
        <div class="sk-date-card" style="background:linear-gradient(135deg,#4a5e2a,#6b8c3a); color:white; padding:1.2rem; border-radius:16px; margin-bottom:1.2rem; text-align:center;">
          <div style="font-size:1rem; font-weight:600; opacity:0.9;">विजयादशमी (Vijayadashami) 2026</div>
          <div style="font-size:3rem; font-weight:900; line-height:1.1; margin: 0.3rem 0;">20</div>
          <div style="font-size:1.2rem; font-weight:700;">अक्टूबर 2026</div>
          <div style="font-size:0.95rem; opacity:0.85; margin-top:0.3rem;">मंगलवार / Tuesday</div>
        </div>

        <!-- Vijay Muhurat -->
        <div class="sk-date-card" style="border-left:4px solid var(--saffron); padding:1.2rem; border-radius:12px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">⏰ विजय मुहूर्त (Vijay Muhurat)</div>
          <div style="font-size:1.05rem; color:#a50000; font-weight:700;">01:59 PM से 02:45 PM</div>
          <div style="font-size:0.85rem; color:#475569; margin-top:0.3rem; margin-bottom:1rem;">अवधि - 45 मिनट</div>

          <div style="background:#fef3c7; padding:0.8rem; border-radius:8px; margin-bottom:0.8rem;">
            <div style="font-size:0.9rem; font-weight:700; color:var(--maroon);">Bengal Vijayadashami - Wednesday, Oct 21, 2026</div>
            <div style="font-size:0.88rem; color:#a50000; font-weight:600;">Aparahna Puja Time - 01:14 PM to 03:30 PM</div>
            <div style="font-size:0.8rem; color:#475569;">Duration - 2 Hours 16 Mins</div>
          </div>

          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.85rem; color:#475569; border-top:1px solid #e2e8f0; padding-top:0.8rem;">
            <div>📍 Dashami Tithi Begins - 12:50 PM on Oct 20, 2026</div>
            <div>📍 Dashami Tithi Ends - 02:11 PM on Oct 21, 2026</div>
            <div>📍 Shravana Nakshatra Begins - 03:38 PM on Oct 19, 2026</div>
            <div>📍 Shravana Nakshatra Ends - 06:02 PM on Oct 20, 2026</div>
          </div>
        </div>

        <!-- About Vijayadashami -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📖 विजयादशमी के बारे में</div>
          <p style="font-size:0.9rem; color:#334155; line-height:1.75; margin:0;">
            Vijayadashami is celebrated as victory of <strong>Lord Rama</strong> over Demon Ravana and also triumph of <strong>Goddess Durga</strong> over the buffalo Demon Mahishasura. <strong>Shami Puja</strong>, <strong>Aparajita Puja</strong> (अपराजिता पूजा) and <strong>Seema Avalanghan</strong> (सीमा अवलंघन) are some of the rituals which should be done during <strong>Aparahna time</strong>.
          </p>
        </div>`;

// Inject right after the opening of Dussehra section content div
html = html.replace(
  /(<section id="page-dussehra"[\s\S]*?<div class="section-content"[^>]*>)/,
  '$1' + muhurateSection
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Vijayadashami 2026 muhurat to Dussehra page!');
