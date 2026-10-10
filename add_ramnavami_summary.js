const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const extraData = `
        <!-- Key Info -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">✨ मुख्य जानकारी</div>
          <div style="font-size:0.88rem; color:#475569; display:flex; flex-direction:column; gap:0.5rem;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Rama Naumi</div>
            <div><strong style="color:var(--maroon);">Key Rituals:</strong> Rama Navami Puja</div>
            <div><strong style="color:var(--maroon);">Mythological Figures:</strong> Lord Rama, Mata Kaushalya, King Dasharatha, Devi Sita, Bharata, Lakshmana, Shatrughna, Hanuman</div>
          </div>
        </div>

        <!-- Year-wise Dates -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 राम नवमी तिथियाँ</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.92rem;">
            <div style="color:#475569;">2025: <strong>April 06 (Sunday)</strong></div>
            <div style="color:#475569;">2026: <strong>March 26 (Thursday)</strong></div>
            <div style="color:#a50000; font-weight:700;">2027: April 15 (Thursday) ← Next</div>
            <div style="color:#475569;">2028: <strong>April 03 (Monday)</strong></div>
          </div>
        </div>

        <!-- 12-City Muhurat -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🏙️ 2027 शहर-वार पूजा मुहूर्त</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.78rem;">
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">New Delhi</div><div>11:04–01:38 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Noida</div><div>11:04–01:38 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Pune</div><div>11:19–01:50 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Jaipur</div><div>11:10–01:44 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Chennai</div><div>10:55–01:24 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Mumbai</div><div>11:23–01:54 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Kolkata</div><div>10:21–12:53 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Gurgaon</div><div>11:05–01:39 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Hyderabad</div><div>11:01–01:32 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Bengaluru</div><div>11:05–01:34 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Ahmedabad</div><div>11:24–01:56 PM</div></div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:#2d4a1e;">Chandigarh</div><div>11:06–01:41 PM</div></div>
          </div>
        </div>

        <!-- Devotional Songs -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎵 भक्ति गीत</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.5rem;">
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">आरती:</strong> Shree Rama Chandra Kripalu Bhajman</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">चालीसा:</strong> Shree Raghubir Bhakta Hitakari</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">नामावली:</strong> 108 Rama Names</div>
          </div>
        </div>

        <!-- Recipes -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🍱 प्रसाद एवं व्यंजन</div>
          <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.5rem; font-size:0.85rem; text-align:center;">
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍹 Panakam</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🥛 Neer Mor</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🥄 Panchamrit</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍮 Halwa</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍚 Kheer</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🥗 Kosambari</div>
          </div>
        </div>`;

// Inject before the closing section tag of Ram Navami page
html = html.replace(
  /(id="page-ramnavami"[\s\S]*?)(      <\/div>\s*<\/section>)(\s*\n\s*<\/body>)/,
  '$1' + extraData + '\n      </div>\n    </section>$3'
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Ram Navami summary data!');
