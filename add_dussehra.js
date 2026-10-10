const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Add Dussehra page before </body>
if(!html.includes('id="page-dussehra"')) {
  const dussehraPage = `
    <!-- 🌺 DUSSEHRA PAGE 🌺 -->
    <section id="page-dussehra" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-top10">❮</button>
        <h2>दशहरा (Dussehra)</h2>
        <span style="width:36px"></span>
      </div>
      <div class="sankashti-hero">
        <img src="assets/top10_4.jpg" alt="Dussehra" style="width:100%; height:220px; object-fit:cover;">
        <div class="sh-overlay">
          <h1>दशहरा (Dussehra)</h1>
          <p>बुराई पर अच्छाई की विजय</p>
        </div>
      </div>

      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding: 1.5rem 1rem 4rem;">

        <!-- Description -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <p style="font-size:0.92rem; color:#334155; line-height:1.75; margin:0 0 0.8rem;">
            In India, <strong>Dussehra</strong> and <strong>Vijayadashami</strong> are used interchangeably. Both terms represent the same festival observed on <strong>Shukla Paksha Dashami</strong> during Ashwin month. It is celebrated on the <strong>tenth day of Devi Paksha</strong> — after 9 days of Navratri.
          </p>
          <div style="font-size:0.88rem; color:#475569; line-height:1.6;">
            Also spelled as: <strong>Dasara</strong>, <strong>Dashahara (दशहरा)</strong>
          </div>
        </div>

        <!-- Origin & Significance -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📜 उत्पत्ति एवं महत्व</div>
          <p style="font-size:0.9rem; color:#334155; line-height:1.75; margin:0 0 0.8rem;">The term <strong>Dussehra</strong> refers to killing of 10-headed demon <strong>Ravana</strong>. It literally means removal of 10 sins — the 10 bad qualities represented by Ravana's 10 heads:</p>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.4rem; font-size:0.82rem;">
            <div style="background:#fef3c7; padding:0.5rem 0.7rem; border-radius:8px;">1. Kama Vasana - काम वासना</div>
            <div style="background:#fef3c7; padding:0.5rem 0.7rem; border-radius:8px;">2. Krodha - क्रोध (anger)</div>
            <div style="background:#fef3c7; padding:0.5rem 0.7rem; border-radius:8px;">3. Moha - मोह (attraction)</div>
            <div style="background:#fef3c7; padding:0.5rem 0.7rem; border-radius:8px;">4. Lobha - लोभ (greed)</div>
            <div style="background:#fef3c7; padding:0.5rem 0.7rem; border-radius:8px;">5. Mada - मद (over pride)</div>
            <div style="background:#fef3c7; padding:0.5rem 0.7rem; border-radius:8px;">6. Matsara - मत्सर (jealousy)</div>
            <div style="background:#fef3c7; padding:0.5rem 0.7rem; border-radius:8px;">7. Swartha - स्वार्थ (selfishness)</div>
            <div style="background:#fef3c7; padding:0.5rem 0.7rem; border-radius:8px;">8. Anyaya - अन्याय (injustice)</div>
            <div style="background:#fef3c7; padding:0.5rem 0.7rem; border-radius:8px;">9. Amanavata - अमानवता</div>
            <div style="background:#fef3c7; padding:0.5rem 0.7rem; border-radius:8px;">10. Ahankara - अहंकार (ego)</div>
          </div>
        </div>

        <!-- Deity -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🙏 देवी-देवता (Deity/s)</div>
          <div style="display:flex; flex-direction:column; gap:0.8rem; font-size:0.9rem; color:#334155;">
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;">
              <strong style="color:var(--maroon);">Lord Rama</strong> - The most popular deity. The day is observed as the victory of Lord Rama over demon Ravana. Lord Rama took 20 lunar days to return to Ayodhya after killing Ravana — it was Diwali day when he reached Ayodhya.
            </div>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;">
              <strong style="color:var(--maroon);">Goddess Aparajita</strong> - Worshipped in many regions. Lord Rama sought blessings of Goddess Aparajita before waging war against Ravana.
            </div>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;">
              <strong style="color:var(--maroon);">Shami Tree</strong> - Worshipping Shami tree is very significant. Arjun hid his weapons inside Shami tree during his exile. Also known as <em>Banni Puja</em> and <em>Jammi Puja</em> in southern states.
            </div>
          </div>
        </div>

        <!-- Observances -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎉 अनुष्ठान (Observances)</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.5rem;">
            <div>🎭 Mocking killing of demon Ravana through Ramlila</div>
            <div>🔥 Effigy of Ravana getting burned in public event</div>
            <div>🎆 Display of firework</div>
            <div>💛 Sisters putting Tika on the forehead of brothers</div>
            <div>🔴 Sindur Utsav in West Bengal</div>
            <div>🌿 Seema Avalanghan</div>
            <div>🙏 Worshipping Goddess Aparajita</div>
            <div>🌳 Worshipping Shami tree</div>
            <div>🐘 Grand elephant procession (Jumbo Savari) in Mysore</div>
          </div>
        </div>

        <!-- Public Life -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🏛️ सार्वजनिक जीवन (Public Life)</div>
          <p style="font-size:0.88rem; color:#334155; line-height:1.7; margin:0;">
            Dussehra and Vijayadashami are <strong>compulsory gazetted holidays</strong> in India. All government offices, banks, schools and colleges are closed. Public transport runs as usual.
          </p>
        </div>

        <!-- Similar Festivals -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🌏 समान त्यौहार (Similar Festivals)</div>
          <div style="font-size:0.9rem; color:#334155; display:flex; flex-direction:column; gap:0.5rem;">
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🇳🇵 Dashain - Nepal</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🐘 Mysore Dasara - Karnataka</div>
          </div>
        </div>

      </div>
    </section>`;
  html = html.replace('</body>', dussehraPage + '\n  </body>');
}

// Update Dussehra in TOP10 data (will be handled in app.js)
const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Dussehra page!');
