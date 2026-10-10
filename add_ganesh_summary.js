const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const extraData = `
        <!-- Key Info & Dates -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">✨ मुख्य जानकारी</div>
          <div style="font-size:0.88rem; color:#475569; display:flex; flex-direction:column; gap:0.5rem;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Siddhi Vinayaka Chaturthi, Ganesha Chauth</div>
            <div><strong style="color:var(--maroon);">Key Rituals:</strong> Ganesha Puja</div>
            <div><strong style="color:var(--maroon);">Mythological Figures:</strong> Lord Ganesha</div>
            <div style="margin-top:0.4rem;"><strong style="color:var(--maroon);">Hindu Calendar Date:</strong><br>
            Purnimanta - Chaturthi of Bhadrapada month (Shukla Paksha)<br>
            Amanta - Chaturthi of Bhadrapada month (Shukla Paksha)</div>
          </div>
        </div>

        <!-- Year-wise Dates -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 गणेश चतुर्थी तिथियाँ</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.92rem;">
            <div style="color:#475569;">2025: <strong>August 27 (Wednesday)</strong></div>
            <div style="color:#a50000; font-weight:700;">2026: September 14 (Monday) ← Current</div>
            <div style="color:#475569;">2027: <strong>September 04 (Saturday)</strong></div>
            <div style="color:#475569;">2028: <strong>August 23 (Wednesday)</strong></div>
          </div>
        </div>

        <!-- Devotional Songs -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎵 भक्ति गीत (Devotional Songs)</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.5rem;">
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">आरती:</strong> Jay Ganesh Deva, Aarti Gajavadan Vinayaka Ki</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">चालीसा:</strong> Jaya Jaya Jaya Ganapati Gan Raaju</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">स्तोत्रम्:</strong> Rinharta Ganesha Stotram, Rinmukti Ganesha Stotram</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">अष्टकम्:</strong> Ganesha Ashtakam</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">नामावली:</strong> 108 Names, 108 Siddhivinayaka, 1000 Names, 32 Names</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">मंत्र:</strong> Ganesha Mantras</div>
          </div>
        </div>`;

// Inject before the closing of Ganesha Chaturthi page
html = html.replace(
  /(id="page-ganeshchaturthi"[\s\S]*?)(      <\/div>\s*<\/section>)(\s*\n\s*<\/body>)/,
  '$1' + extraData + '\n      </div>\n    </section>$3'
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added key info, dates and songs to Ganesha Chaturthi page!');
