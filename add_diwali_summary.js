const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Add new sections before the closing </div></section> of Diwali page (before HOLI PAGE comment)
const extraSection = `
        <!-- Diwali Dates 2025-2028 -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 दीपावली तिथियाँ</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.92rem;">
            <div style="color:#475569;">2025: <strong>October 20 (Monday)</strong></div>
            <div style="color:#a50000; font-weight:700;">2026: November 08 (Sunday) ← Current</div>
            <div style="color:#475569;">2027: <strong>October 29 (Friday)</strong></div>
            <div style="color:#475569;">2028: <strong>October 17 (Tuesday)</strong></div>
          </div>
          <div style="margin-top:1rem; border-top:1px solid #e2e8f0; padding-top:0.8rem; font-size:0.88rem; color:#475569;">
            <div><strong>Purnimanta:</strong> Amavasya of Kartik month (Krishna Paksha)</div>
            <div><strong>Amanta:</strong> Amavasya of Ashwin month (Krishna Paksha)</div>
          </div>
        </div>

        <!-- Mythological Figures -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📜 पौराणिक कथाएँ (Legends)</div>
          <div style="font-size:0.9rem; color:#475569; margin-bottom:0.8rem;"><strong style="color:var(--maroon);">Mythological Figures:</strong> Lord Rama, Goddess Sita, Lakshmana, Ravana</div>
          <div style="font-size:0.88rem; color:#334155; line-height:1.7; background:#fef9ec; padding:0.8rem; border-radius:8px;">
            Lord Rama - One of the famous legends of Diwali is associated with Lord Rama. It is believed that Lord Rama, his wife Goddess Sita and Lakshmana returned to Ayodhya after 14 years of exile on the day of Diwali. The people of Ayodhya celebrated their return by lighting diyas all over the city.
          </div>
        </div>

        <!-- Devotional Songs -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎵 भक्ति गीत (Devotional Songs)</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.5rem;">
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">आरती:</strong> Om Jai Lakshmi Mata</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">चालीसा:</strong> Maatu Lakshmi Kari Kripa</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">स्तोत्रम्:</strong> Shree Suktam, Ashtalakshmi, Dhanalakshmi, Kanakadhara</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">नामावली:</strong> 108 Names, 1000 Names</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;"><strong style="color:var(--maroon);">मंत्र:</strong> Lakshmi Mantra, Lakshmi-Ganesha Mantra, Diwali Mantra</div>
          </div>
        </div>

        <!-- Recipes -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🍬 पारंपरिक व्यंजन (Recipes)</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.85rem; text-align:center;">
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🧆 Gujiya, Karanji</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🌙 Chandrakala</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍮 Gulab Jamun</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍬 Shakkarpara</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🌾 Namakpara</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🍚 Anarsa</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🥮 Mathari</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px;">🪙 Kaju Katli</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px; grid-column: span 2;">🍇 Dry Fruits</div>
          </div>
        </div>

        <!-- Attire -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">👗 परिधान (Attire)</div>
          <div style="display:flex; gap:0.8rem; font-size:0.9rem; color:#334155;">
            <div style="background:#fef3c7; padding:0.7rem 1rem; border-radius:8px; flex:1; text-align:center;">👘 Traditional Indian clothes</div>
            <div style="background:#fef3c7; padding:0.7rem 1rem; border-radius:8px; flex:1; text-align:center;">👗 Indo-western</div>
          </div>
        </div>`;

// Insert before the closing of Diwali section (just before HOLI PAGE comment)
html = html.replace(
  /(\s*<\/div>\s*<\/section>\s*\n\s*<!-- 🌺 HOLI PAGE 🌺 -->)/,
  extraSection + '\n\n      </div>\n    </section>\n\n    <!-- 🌺 HOLI PAGE 🌺 -->'
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Diwali Summary, Recipes, Devotional Songs to Diwali page!');
