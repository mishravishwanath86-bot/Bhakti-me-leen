const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

if(!html.includes('id="page-ganeshchaturthi"')) {
  const ganeshPage = `
    <!-- 🌺 GANESHA CHATURTHI PAGE 🌺 -->
    <section id="page-ganeshchaturthi" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-top10">❮</button>
        <h2>गणेश चतुर्थी</h2>
        <span style="width:36px"></span>
      </div>
      <div class="sankashti-hero">
        <img src="assets/top10_7.jpg" alt="Ganesha Chaturthi" style="width:100%; height:220px; object-fit:cover;">
        <div class="sh-overlay">
          <h1>गणेश चतुर्थी</h1>
          <p>गणपति बप्पा मोरया! 10 दिनों का महोत्सव</p>
        </div>
      </div>

      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding: 1.5rem 1rem 4rem;">

        <!-- Description -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <p style="font-size:0.92rem; color:#334155; line-height:1.75; margin:0 0 0.8rem;">
            <strong>Ganesha Chaturthi</strong> is a famous Hindu festival celebrated throughout India, dedicated to <strong>Lord Ganesha</strong>. It is observed as the birth anniversary of Lord Ganesha. Celebrations are most elaborate in <strong>Maharashtra, Telangana and Karnataka</strong>. Mumbai, Pune and Hyderabad are most significant cities.
          </p>
          <div style="font-size:0.88rem; color:#475569; display:flex; flex-direction:column; gap:0.4rem;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Siddhi Vinayaka Chaturthi, Ganesha Chauth</div>
            <div><strong style="color:var(--maroon);">Significance:</strong> Birth anniversary of Lord Ganesha — God of wisdom and remover of all obstacles, worshipped first among all Gods</div>
          </div>
        </div>

        <!-- Origin & Significance -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📜 उत्पत्ति एवं महत्व</div>
          <div style="font-size:0.88rem; color:#334155; line-height:1.75; display:flex; flex-direction:column; gap:0.7rem;">
            <p style="margin:0;">As per <strong>Ganesha Purana</strong> and <strong>Skanda Purana</strong>, Lord Ganesha was born on <strong>Shukla Chaturthi during Bhadrapada month</strong>.</p>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;">
              <strong style="color:var(--maroon);">Deity:</strong> Lord Ganesha<br>
              <strong style="color:var(--maroon);">Hindu Calendar Date:</strong> Shukla Paksha Chaturthi (4th day) of Bhadrapada (6th month)
            </div>
            <p style="margin:0; font-size:0.85rem; color:#475569;">As per Shiva Dharma, Lord Ganesha was born on Krishna Chaturthi during Magha month. In Maharashtra, Shukla Chaturthi during Magha is observed as <strong>Ganesha Jayanti</strong>.</p>
          </div>
        </div>

        <!-- Festivals List (10 Days) -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🗓️ 10 दिन का महोत्सव</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.88rem;">
            <div style="background:#f97316; color:white; padding:0.6rem 1rem; border-radius:8px; font-weight:700;">🐘 Day 1 — Ganesha Chaturthi (Ganesh Sthapana)</div>
            <div style="background:#fef3c7; padding:0.5rem 1rem; border-radius:8px; color:#475569;">Days 2–9 — Daily worship of Lord Ganesha</div>
            <div style="background:#fef3c7; padding:0.6rem 1rem; border-radius:8px; font-weight:700; color:var(--maroon);">🌊 Day 10 — Ganesha Visarjan (Anant Chaturdashi) — Grand Immersion</div>
          </div>
          <div style="margin-top:0.8rem; font-size:0.85rem; color:#475569; line-height:1.6; border-top:1px solid #e2e8f0; padding-top:0.8rem;">
            <strong>⚠️ Avoid Moonsighting</strong> on the day of Ganesha Chaturthi — it is considered inauspicious.
          </div>
        </div>

        <!-- Observances -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎉 अनुष्ठान (Observances)</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.45rem;">
            <div>🐘 Buying beautiful Ganesha Idol</div>
            <div>🍽️ A day long fast</div>
            <div>🏺 Ritualistically installing Ganesha idol on Ganesha Chaturthi</div>
            <div>🙏 Shodashopachara Ganesha Puja during Madhyahna</div>
            <div>🌙 Avoid moonsighting</div>
            <div>📿 Daily worshipping Lord Ganesha for next 10 days</div>
            <div>🌊 Bidding farewell to Lord Ganesha on Anant Chaturdashi day</div>
          </div>
        </div>

        <!-- Dishes / Prasad -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🍬 प्रसाद एवं व्यंजन</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.88rem; text-align:center;">
            <div style="background:#fef9ec; padding:0.7rem; border-radius:8px;">🍮 Modak</div>
            <div style="background:#fef9ec; padding:0.7rem; border-radius:8px;">🌾 Til & Jaggery Laddu</div>
            <div style="background:#fef9ec; padding:0.7rem; border-radius:8px;">🟡 Besan Laddu</div>
            <div style="background:#fef9ec; padding:0.7rem; border-radius:8px;">🟠 Motichoor Laddu</div>
          </div>
        </div>

        <!-- Visarjan Info -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🌊 गणेश विसर्जन (Anant Chaturdashi)</div>
          <p style="font-size:0.88rem; color:#334155; line-height:1.75; margin:0;">
            <strong>Anant Chaturdashi</strong> falls 10 days after Ganesha Chaturthi — it is the culmination day when idols of Lord Ganesha are offered to water body through <strong>Visarjan and immersion</strong>. Grand street processions are taken out with much fun and frolic. In some states it is declared as <strong>dry day</strong>.
          </p>
        </div>

        <!-- Similar Festivals -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🌏 समान त्यौहार</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.9rem;">
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🐘 Ganesha Jayanti</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🌊 Ganesha Visarjan</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🙏 Sakat Chauth</div>
          </div>
        </div>

      </div>
    </section>`;
  html = html.replace('</body>', ganeshPage + '\n  </body>');
}

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Ganesha Chaturthi page!');
