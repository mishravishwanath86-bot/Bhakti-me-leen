const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const muhurateSection = `
        <!-- Rama Navami Date 2027 -->
        <div class="sk-date-card" style="background:linear-gradient(135deg,#2d4a1e,#4a7a2e); color:white; padding:1.2rem; border-radius:16px; margin-bottom:1.2rem; text-align:center;">
          <div style="font-size:1rem; font-weight:600; opacity:0.9;">राम नवमी (Rama Navami) 2027</div>
          <div style="font-size:3rem; font-weight:900; line-height:1.1; margin: 0.3rem 0;">15</div>
          <div style="font-size:1.2rem; font-weight:700;">अप्रैल 2027</div>
          <div style="font-size:0.95rem; opacity:0.85; margin-top:0.3rem;">गुरुवार / Thursday</div>
          <div style="margin-top:0.6rem; font-size:0.85rem; opacity:0.85; background:rgba(255,255,255,0.15); padding:0.4rem 0.8rem; border-radius:8px; display:inline-block;">Sita Navami: Friday, May 14, 2027</div>
        </div>

        <!-- Madhyahna Muhurat -->
        <div class="sk-date-card" style="border-left:4px solid #4a7a2e; padding:1.2rem; border-radius:12px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">⏰ मध्याह्न पूजा मुहूर्त</div>
          <div style="font-size:1.05rem; color:#a50000; font-weight:700;">11:04 AM से 01:38 PM</div>
          <div style="font-size:0.85rem; color:#475569; margin-top:0.3rem; margin-bottom:1rem;">अवधि - 2 घंटे 34 मिनट</div>
          <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.83rem; color:#475569; border-top:1px solid #e2e8f0; padding-top:0.8rem;">
            <div>🕛 Rama Navami Madhyahna Moment - <strong>12:21 PM</strong></div>
            <div>📍 Navami Tithi Begins - 03:23 PM on Apr 14, 2027</div>
            <div>📍 Navami Tithi Ends - 01:20 PM on Apr 15, 2027</div>
            <div>📖 Vrat Katha: Story of the Birth of Lord Shri Rama</div>
          </div>
        </div>

        <!-- Madhyahna Explanation -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📖 मध्याह्न पूजा का महत्व</div>
          <div style="font-size:0.9rem; color:#334155; line-height:1.75; display:flex; flex-direction:column; gap:0.7rem;">
            <p style="margin:0;">Lord Rama was born during <strong>Madhyahna period</strong> — the middle of Hindu day. <strong>Madhyahna</strong> prevails for six Ghatis (approximately <strong>2 hours and 24 minutes</strong>). This is the most auspicious time to perform Rama Navami Puja rituals.</p>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; font-size:0.87rem; line-height:1.65;">The mid-point of Madhyahna marks the <strong>birth moment of Lord Rama</strong> and temples symbolize this moment. The chanting of Shri Rama and celebration reaches its peak during this time. Birth falls between <strong>11 AM and 1 PM</strong> for most Indian cities.
            </div>
          </div>
        </div>

        <!-- Fasting Info -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🍽️ व्रत के प्रकार (Types of Vrat)</div>
          <div style="font-size:0.88rem; color:#334155; margin-bottom:0.8rem;"><strong>Eight Prahar fasting</strong> is suggested — from sunrise to sunrise (next day).</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.87rem;">
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">Casual (नैमित्तिक):</strong> Can be observed without any specific cause</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">Continual (नित्य):</strong> Can be observed throughout life without any desire</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">Desirable (काम्य):</strong> Can be observed to fulfill any desire</div>
          </div>
        </div>`;

// Inject at the start of Ram Navami page content
html = html.replace(
  /(<section id="page-ramnavami"[\s\S]*?<div class="section-content"[^>]*>)/,
  '$1' + muhurateSection
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Ram Navami muhurat data!');
