const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const extraData = `
        <!-- Dussehra Dates 2025-2028 -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 दशहरा तिथियाँ</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.92rem;">
            <div style="color:#475569;">2025: <strong>October 02 (Thursday)</strong></div>
            <div style="color:#a50000; font-weight:700;">2026: October 20 (Tuesday) ← Current</div>
            <div style="color:#475569;">2027: <strong>October 09 (Saturday)</strong></div>
            <div style="color:#475569;">2028: <strong>September 27 (Wednesday)</strong></div>
          </div>
          <div style="margin-top:1rem; border-top:1px solid #e2e8f0; padding-top:0.8rem; font-size:0.88rem; color:#475569;">
            <div><strong>Also Called:</strong> Vijayadashami, Dasara</div>
            <div><strong>Key Rituals:</strong> Ravana Dahana (burning effigy of demon king Ravana)</div>
            <div><strong>Mythological Figures:</strong> Lord Rama, Goddess Sita, Lakshmana, Ravana</div>
            <div style="margin-top:0.5rem;"><strong>Purnimanta:</strong> Dashami of Ashwin month (Shukla Paksha)</div>
            <div><strong>Amanta:</strong> Dashami of Ashwin month (Shukla Paksha)</div>
          </div>
        </div>

        <!-- City-wise Puja Time -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🏙️ 2026 शहर-वार पूजा समय</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.78rem;">
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">New Delhi</div><div>01:59–02:45 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Noida</div><div>01:59–02:44 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Pune</div><div>02:16–03:02 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Jaipur</div><div>02:06–02:51 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Chennai</div><div>01:51–02:39 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Mumbai</div><div>02:19–03:06 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Kolkata</div><div>01:17–02:03 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Gurgaon</div><div>02:00–02:46 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Hyderabad</div><div>01:57–02:44 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Bengaluru</div><div>02:02–02:49 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Ahmedabad</div><div>02:20–03:06 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#4a5e2a;">Chandigarh</div><div>02:00–02:46 PM</div></div>
          </div>
        </div>

        <!-- Recipes & Attire -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🍬 व्यंजन एवं परिधान</div>
          <div style="display:flex; gap:0.8rem; margin-bottom:0.8rem;">
            <div style="background:#fef9ec; padding:0.7rem 1rem; border-radius:8px; flex:1; text-align:center; font-size:0.9rem;">🍮 Jalebi</div>
            <div style="background:#fef9ec; padding:0.7rem 1rem; border-radius:8px; flex:1; text-align:center; font-size:0.9rem;">🥘 Aloo Kachori</div>
          </div>
          <div style="background:#fef3c7; padding:0.7rem 1rem; border-radius:8px; font-size:0.9rem; text-align:center;">👗 Attire: Traditional clothes</div>
        </div>`;

// Inject before the closing of Dussehra page
html = html.replace(
  /(<\/div>\s*<\/section>\s*<!-- 🌺 DUSSEHRA PAGE 🌺 -->[\s\S]*?)(<!--)/,
  (match, p1, p2) => match
);

// Better approach - find the last </div></section> before HOLI or any next page
html = html.replace(
  /(id="page-dussehra"[\s\S]*?)(      <\/div>\s*<\/section>)(\s*\n\s*<\/body>)/,
  '$1' + extraData + '\n      </div>\n    </section>$3'
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Dussehra dates, city muhurat, recipes to Dussehra page!');
