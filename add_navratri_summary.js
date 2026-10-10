const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const extraData = `
        <!-- Key Info -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">✨ मुख्य जानकारी</div>
          <div style="font-size:0.88rem; color:#475569; display:flex; flex-direction:column; gap:0.5rem;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Shardiya Navratri, Maha Navaratri</div>
            <div><strong style="color:var(--maroon);">Significance:</strong> Victory of Goddess Durga over demon Mahishasura</div>
            <div><strong style="color:var(--maroon);">Deity(s):</strong> Goddess Durga, Navdurga</div>
            <div><strong style="color:var(--maroon);">Key Rituals:</strong> Ghatasthapana Puja, Durga Puja, Chandi Homa, Kanya Puja, Jyoti Kalash, Navratri 9 Colors</div>
            <div><strong style="color:var(--maroon);">Mythological Figures:</strong> Goddess Durga, Navdurga, Ugrachandi, Bhadrakali, Mahishasura, Lord Rama</div>
          </div>
        </div>

        <!-- Year-wise Dates -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 नवरात्रि तिथियाँ (वर्ष-वार)</div>

          <div style="font-size:0.85rem; margin-bottom:0.8rem;">
            <div style="font-weight:800; color:#475569; margin-bottom:0.4rem;">2025 Navratri Dates</div>
            <div style="background:#f8fafc; padding:0.6rem; border-radius:8px; font-size:0.82rem; color:#334155; display:flex; flex-direction:column; gap:0.25rem;">
              <div>• Ghatasthapana: September 22 (Monday)</div>
              <div>• Durga Ashtami: September 30 (Tuesday)</div>
              <div>• Maha Navami: October 01 (Wednesday)</div>
              <div>• Navami Homa: October 01 (Wednesday)</div>
            </div>
          </div>

          <div style="font-size:0.85rem; margin-bottom:0.8rem;">
            <div style="font-weight:800; color:#a50000; margin-bottom:0.4rem;">2026 Navratri Dates ← Current</div>
            <div style="background:#fff3f3; padding:0.6rem; border-radius:8px; font-size:0.82rem; color:#334155; display:flex; flex-direction:column; gap:0.25rem; border:1px solid #fecaca;">
              <div>• Ghatasthapana: <strong>October 11 (Sunday)</strong></div>
              <div>• Durga Ashtami: <strong>October 19 (Monday)</strong></div>
              <div>• Maha Navami: <strong>October 19 (Monday)</strong></div>
              <div>• Navami Homa: <strong>October 20 (Tuesday)</strong></div>
            </div>
          </div>

          <div style="font-size:0.85rem; margin-bottom:0.8rem;">
            <div style="font-weight:800; color:#475569; margin-bottom:0.4rem;">2027 Navratri Dates</div>
            <div style="background:#f8fafc; padding:0.6rem; border-radius:8px; font-size:0.82rem; color:#334155; display:flex; flex-direction:column; gap:0.25rem;">
              <div>• Ghatasthapana: September 30 (Thursday)</div>
              <div>• Durga Ashtami: October 07 (Thursday)</div>
              <div>• Maha Navami: October 08 (Friday)</div>
              <div>• Navami Homa: October 09 (Saturday)</div>
            </div>
          </div>

          <div style="font-size:0.85rem;">
            <div style="font-weight:800; color:#475569; margin-bottom:0.4rem;">2028 Navratri Dates</div>
            <div style="background:#f8fafc; padding:0.6rem; border-radius:8px; font-size:0.82rem; color:#334155; display:flex; flex-direction:column; gap:0.25rem;">
              <div>• Ghatasthapana: September 19 (Tuesday)</div>
              <div>• Durga Ashtami: September 26 (Tuesday)</div>
              <div>• Maha Navami: September 26 (Tuesday)</div>
              <div>• Navami Homa: September 27 (Wednesday)</div>
            </div>
          </div>
        </div>

        <!-- Devotional Songs -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎵 भक्ति गीत (Devotional Songs)</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.5rem;">
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">आरती:</strong> Ambe Tu Hai Jagdambe Kali, Jai Ambe Gauri, Jag Janani Jai Jai</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">चालीसा:</strong> Namo Namo Durge Sukh Karni</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">स्तोत्रम्:</strong> Navadurga Stotram, Durga Saptashati</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">नामावली:</strong> 108 Names, 1000 Names, 32 Names</div>
          </div>
        </div>`;

// Inject before closing of Navratri page
html = html.replace(
  /(id="page-navratri"[\s\S]*?)(      <\/div>\s*<\/section>)(\s*\n\s*<\/body>)/,
  '$1' + extraData + '\n      </div>\n    </section>$3'
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added year-wise Navratri dates and songs!');
