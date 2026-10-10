const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const muhurateSection = `
        <!-- Ganesh Chaturthi 2026 Date Card -->
        <div class="sk-date-card" style="background:linear-gradient(135deg,#4a5e2a,#6b8c3a); color:white; padding:1.2rem; border-radius:16px; margin-bottom:1.2rem; text-align:center;">
          <div style="font-size:1rem; font-weight:600; opacity:0.9;">गणेश चतुर्थी (Ganesh Chaturthi) 2026</div>
          <div style="font-size:3rem; font-weight:900; line-height:1.1; margin: 0.3rem 0;">14</div>
          <div style="font-size:1.2rem; font-weight:700;">सितम्बर 2026</div>
          <div style="font-size:0.95rem; opacity:0.85; margin-top:0.3rem;">सोमवार / Monday</div>
          <div style="margin-top:0.6rem; font-size:0.88rem; opacity:0.9; background:rgba(255,255,255,0.15); padding:0.4rem 0.8rem; border-radius:8px; display:inline-block;">🌊 Ganesha Visarjan: September 25, 2026 (Friday)</div>
        </div>

        <!-- Muhurat Box -->
        <div class="sk-date-card" style="border-left:4px solid var(--saffron); padding:1.2rem; border-radius:12px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">⏰ मध्याह्न गणेश पूजा मुहूर्त</div>
          <div style="font-size:1.05rem; color:#a50000; font-weight:700;">11:02 AM से 01:31 PM</div>
          <div style="font-size:0.85rem; color:#475569; margin-top:0.3rem; margin-bottom:1rem;">अवधि - 2 घंटे 28 मिनट</div>
          
          <div style="background:#fff3cd; padding:0.8rem; border-radius:8px; margin-bottom:0.8rem;">
            <div style="font-size:0.88rem; font-weight:700; color:#a50000;">🌙 चन्द्र दर्शन निषेध (Avoid Moon Sighting)</div>
            <div style="font-size:0.9rem; font-weight:700; color:#a50000; margin-top:0.3rem;">09:06 AM से 08:04 PM</div>
            <div style="font-size:0.8rem; color:#475569;">Duration - 10 Hours 58 Mins</div>
          </div>

          <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.83rem; color:#475569; border-top:1px solid #e2e8f0; padding-top:0.8rem;">
            <div>📍 Chaturthi Tithi Begins - 07:06 AM on Sep 14, 2026</div>
            <div>📍 Chaturthi Tithi Ends - 07:44 AM on Sep 15, 2026</div>
            <div>📖 Vrat Katha: Story of Lord Krishna being accused of stealing the Syamantaka Mani</div>
          </div>
        </div>

        <!-- City-wise Muhurat -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🏙️ 2026 शहर-वार पूजा मुहूर्त</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.78rem;">
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">New Delhi</div><div>11:02–01:31 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Noida</div><div>11:02–01:30 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Pune</div><div>11:16–01:44 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Chandigarh</div><div>11:04–01:33 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Chennai</div><div>10:51–01:18 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Kolkata</div><div>10:18–12:46 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Jaipur</div><div>11:08–01:36 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Mumbai</div><div>11:20–01:48 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Hyderabad</div><div>10:58–01:25 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Bengaluru</div><div>11:02–01:28 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Gurgaon</div><div>11:03–01:31 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Ahmedabad</div><div>11:21–01:49 PM</div></div>
          </div>
        </div>

        <!-- Recent Years -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 गणेश चतुर्थी - वर्ष-वार</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.35rem; font-size:0.82rem; color:#475569;">
            <div>2023 - Tue, Sep 19</div><div>2029 - Tue, Sep 11</div>
            <div>2024 - Sat, Sep 7</div><div>2030 - Sun, Sep 1</div>
            <div>2025 - Wed, Aug 27</div><div>2031 - Sat, Sep 20</div>
            <div style="color:#a50000; font-weight:700;">2026 - Mon, Sep 14 ←</div><div>2032 - Wed, Sep 8</div>
            <div>2027 - Sat, Sep 4</div><div>2033 - Sun, Aug 28</div>
            <div>2028 - Wed, Aug 23</div><div></div>
          </div>
        </div>

        <!-- Moon Sighting Warning -->
        <div class="sk-date-card" style="border-left:4px solid #ef4444; padding:1.2rem; border-radius:12px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:#b91c1c; margin-bottom:0.8rem;">🌙 चन्द्र दर्शन निषेध - क्यों?</div>
          <div style="font-size:0.88rem; color:#334155; line-height:1.75; display:flex; flex-direction:column; gap:0.7rem;">
            <p style="margin:0;">Sighting moon on Ganesha Chaturthi creates <strong>Mithya Dosham</strong> or <strong>Mithya Kalank (कलंक)</strong> — means false accusation of stealing something.</p>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; font-size:0.85rem; line-height:1.65;">As per Puranic legends, <strong>Lord Krishna</strong> was falsely accused of stealing jewel <strong>Syamantaka</strong> because he had sighted moon on this day. <strong>Sage Narada</strong> informed that God Chandra has been cursed by Lord Ganesha — anyone sighting moon on Shukla Chaturthi of Bhadrapada would be cursed with Mithya Dosha.</div>
            <div style="background:#fef3f3; padding:0.8rem; border-radius:8px;">
              <div style="font-size:0.88rem; font-weight:700; color:#b91c1c; margin-bottom:0.5rem;">🕉️ Mithya Dosha Nivaran Mantra:</div>
              <div style="font-size:0.95rem; color:#7B1C1C; line-height:1.8; text-align:center;">सिंहः प्रसेनमवधीत्सिंहो जाम्बवता हतः।<br>सुकुमारक मारोदीस्तव ह्येष स्यन्तकः॥</div>
              <div style="font-size:0.8rem; color:#475569; margin-top:0.4rem; text-align:center; font-style:italic;">Simhah Prasenamavadhitsimho Jambavata Hatah। Sukumaraka Marodistava Hyesha Syamantakah॥</div>
            </div>
          </div>
        </div>`;

// Inject at top of Ganesha Chaturthi page content
html = html.replace(
  /(<section id="page-ganeshchaturthi"[\s\S]*?<div class="section-content"[^>]*>)/,
  '$1' + muhurateSection
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Ganesh Chaturthi muhurat and moon warning to page!');
