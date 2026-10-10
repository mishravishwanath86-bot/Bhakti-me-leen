const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const extraData = `
        <!-- Key Info & Dates -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">✨ मुख्य जानकारी</div>
          <div style="font-size:0.88rem; color:#475569; display:flex; flex-direction:column; gap:0.5rem;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Bhagwati Puja, Akal Bodhon</div>
            <div><strong style="color:var(--maroon);">Key Rituals:</strong> Durga Puja, Pushpanjali, Sandhi Puja, Chandi Homa, Sindoor Khela, Durga Visarjan</div>
            <div><strong style="color:var(--maroon);">Mythological Figures:</strong> Lord Shiva, Goddess Lakshmi, Goddess Saraswati, Lord Ganesha, Lord Kartikeya, Goddess Kali, Demon Mahishasura</div>
            <div style="margin-top:0.5rem;"><strong style="color:var(--maroon);">Hindu Calendar:</strong><br>
            Durga Puja begins - Shashthi of Ashwin month (Shukla Paksha)<br>
            Durga Puja ends - Dashami of Ashwin month (Shukla Paksha)</div>
          </div>
        </div>

        <!-- Year-wise Dates -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 दुर्गा पूजा तिथियाँ (वर्ष-वार)</div>
          
          <div style="font-size:0.88rem; margin-bottom:0.8rem;">
            <div style="font-weight:800; color:#475569; margin-bottom:0.4rem;">2025 Durga Puja Dates</div>
            <div style="background:#f8fafc; padding:0.6rem; border-radius:8px; display:flex; flex-direction:column; gap:0.3rem; font-size:0.83rem; color:#334155;">
              <div>• Navpatrika Puja: September 29 (Monday)</div>
              <div>• Durga Ashtami: September 30 (Tuesday)</div>
              <div>• Maha Navami: October 01 (Wednesday)</div>
            </div>
          </div>

          <div style="font-size:0.88rem; margin-bottom:0.8rem;">
            <div style="font-weight:800; color:#a50000; margin-bottom:0.4rem;">2026 Durga Puja Dates ← Current</div>
            <div style="background:#fff3f3; padding:0.6rem; border-radius:8px; display:flex; flex-direction:column; gap:0.3rem; font-size:0.83rem; color:#334155; border:1px solid #fecaca;">
              <div>• Navpatrika Puja: <strong>October 17 (Saturday)</strong></div>
              <div>• Durga Ashtami: <strong>October 19 (Monday)</strong></div>
              <div>• Maha Navami: <strong>October 19 (Monday)</strong></div>
              <div>• Bengal Maha Navami: <strong>October 20 (Tuesday)</strong></div>
            </div>
          </div>

          <div style="font-size:0.88rem; margin-bottom:0.8rem;">
            <div style="font-weight:800; color:#475569; margin-bottom:0.4rem;">2027 Durga Puja Dates</div>
            <div style="background:#f8fafc; padding:0.6rem; border-radius:8px; display:flex; flex-direction:column; gap:0.3rem; font-size:0.83rem; color:#334155;">
              <div>• Navpatrika Puja: October 06 (Wednesday)</div>
              <div>• Durga Ashtami: October 07 (Thursday)</div>
              <div>• Maha Navami: October 08 (Friday)</div>
              <div>• Bengal Maha Navami: October 09 (Saturday)</div>
            </div>
          </div>

          <div style="font-size:0.88rem;">
            <div style="font-weight:800; color:#475569; margin-bottom:0.4rem;">2028 Durga Puja Dates</div>
            <div style="background:#f8fafc; padding:0.6rem; border-radius:8px; display:flex; flex-direction:column; gap:0.3rem; font-size:0.83rem; color:#334155;">
              <div>• Navpatrika Puja: September 24 (Sunday)</div>
              <div>• Durga Ashtami: September 26 (Tuesday)</div>
              <div>• Maha Navami: September 26 (Tuesday)</div>
              <div>• Bengal Maha Navami: September 27 (Wednesday)</div>
            </div>
          </div>
        </div>

        <!-- Devotional Songs -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎵 भक्ति गीत (Devotional Songs)</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.5rem;">
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">आरती:</strong> Ambe Tu Hai Jagdambe Kali, Jai Ambe Gauri, Jag Janani Jai Jai</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">चालीसा:</strong> Namo Namo Durge Sukh Karni</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">स्तोत्रम्:</strong> Durga Saptashati</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">नामावली:</strong> 108 Names, 1000 Names, 32 Names</div>
          </div>
        </div>`;

// Inject before the closing of Durga Puja page
html = html.replace(
  /(id="page-durgapuja"[\s\S]*?)(      <\/div>\s*<\/section>)(\s*\n\s*<\/body>)/,
  '$1' + extraData + '\n      </div>\n    </section>$3'
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added year-wise dates and devotional songs to Durga Puja page!');
