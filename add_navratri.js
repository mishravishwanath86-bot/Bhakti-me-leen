const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

if(!html.includes('id="page-navratri"')) {
  const navratriPage = `
    <!-- 🌺 NAVRATRI PAGE 🌺 -->
    <section id="page-navratri" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-top10">❮</button>
        <h2>नवरात्रि (Navratri)</h2>
        <span style="width:36px"></span>
      </div>
      <div class="sankashti-hero">
        <img src="assets/top10_6.jpg" alt="Navratri" style="width:100%; height:220px; object-fit:cover;">
        <div class="sh-overlay">
          <h1>नवरात्रि (Navratri)</h1>
          <p>9 रातें, 9 देवियाँ, अपार शक्ति</p>
        </div>
      </div>

      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding: 1.5rem 1rem 4rem;">

        <!-- Description -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <p style="font-size:0.92rem; color:#334155; line-height:1.75; margin:0 0 0.8rem;">
            <strong>Navratri</strong> is a significant Hindu festival observed for <strong>9 nights and 10 days</strong>. During Navratri, nine forms of <strong>Goddess Durga</strong> are worshipped.
          </p>
          <div style="font-size:0.88rem; color:#475569; line-height:1.7;">
            As per <strong>Mahakala Samhita</strong>, there are <strong>four Navratri</strong> in Hindu calendar:<br>
            1. Sharad Navratri &nbsp; 2. Chaitra Navratri<br>
            3. Magha Gupta Navratri &nbsp; 4. Ashadha Gupta Navratri
          </div>
          <div style="margin-top:0.8rem; background:#fef9ec; padding:0.8rem; border-radius:8px; font-size:0.85rem; color:#475569; line-height:1.6;">
            In <strong>Kali Yuga</strong> — Sharad Navratri during Ashwin lunar month is the most significant among all four Navratri.
          </div>
        </div>

        <!-- Origin & Significance -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📜 उत्पत्ति एवं महत्व</div>
          <div style="font-size:0.88rem; color:#334155; line-height:1.75; display:flex; flex-direction:column; gap:0.7rem;">
            <p style="margin:0;">During Sharadiya Navratri, <strong>Goddess Durga killed mighty demon Mahishasura</strong>. As per Rambha Kalpa, Goddess Durga in the form of 18-handed <strong>Ugrachandi</strong> killed Mahishasura.</p>
            <p style="margin:0;"><strong>Lord Rama</strong> also worshipped Goddess Durga during Sharad Navratri. On the advice of <strong>Lord Brahma</strong>, Lord Rama invoked Goddess Durga before waging war against Ravana. This untimely invocation is also known as <strong>Akal Bodhan</strong> of Goddess Durga.</p>
          </div>
        </div>

        <!-- Deity -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🙏 देवी-देवता (Deity/s)</div>
          <div style="font-size:0.88rem; color:#334155; margin-bottom:0.8rem;">Main Goddess: <strong>Goddess Durga</strong> (also known as Goddess Bhavani and Goddess Amba — all attributed to Goddess Parvati)</div>
          
          <div style="font-size:0.88rem; font-weight:700; color:var(--maroon); margin-bottom:0.5rem;">नव दुर्गा (North India - Shaiva Sampradaya):</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.4rem; font-size:0.82rem; margin-bottom:0.8rem;">
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;">1. Shailaputri</div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;">2. Brahmacharini</div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;">3. Chandraghanta</div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;">4. Kushmanda</div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;">5. Skandamata</div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;">6. Katyayani</div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;">7. Kalaratri</div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;">8. Mahagauri</div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px; grid-column:span 2;">9. Siddhidatri</div>
          </div>

          <div style="font-size:0.88rem; font-weight:700; color:var(--maroon); margin-bottom:0.5rem;">दक्षिण भारत (South India):</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.4rem; font-size:0.82rem;">
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;">1. Vanadurga</div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;">2. Shoolini</div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;">3. Jataveda</div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;">4. Shanti</div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;">5. Shabari</div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;">6. Jwaladurga</div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;">7. Lavanadurga</div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px;">8. Asuridurga</div>
            <div style="background:#f0f9e8; padding:0.5rem; border-radius:8px; grid-column:span 2;">9. Deepdurga</div>
          </div>
        </div>

        <!-- Date & 9 Days -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 तिथि एवं 9 दिन का उत्सव</div>
          <div style="font-size:0.85rem; color:#a50000; font-weight:600; margin-bottom:0.8rem;">
            Navratri begins - Pratipada (1st day) of Ashwin (7th lunar month) Shukla Paksha<br>
            Navratri ends - Navami (9th day) of Ashwin Shukla Paksha
          </div>
          <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.82rem;">
            <div style="background:#fef3c7; padding:0.5rem 0.8rem; border-radius:8px; display:flex; gap:0.5rem;"><span style="font-weight:700; color:var(--maroon); min-width:40px;">Day 1</span> Ghatasthapana, Shailaputri Puja</div>
            <div style="background:#fef3c7; padding:0.5rem 0.8rem; border-radius:8px; display:flex; gap:0.5rem;"><span style="font-weight:700; color:var(--maroon); min-width:40px;">Day 2</span> Brahmacharini Puja</div>
            <div style="background:#fef3c7; padding:0.5rem 0.8rem; border-radius:8px; display:flex; gap:0.5rem;"><span style="font-weight:700; color:var(--maroon); min-width:40px;">Day 3</span> Chandraghanta Puja</div>
            <div style="background:#fef3c7; padding:0.5rem 0.8rem; border-radius:8px; display:flex; gap:0.5rem;"><span style="font-weight:700; color:var(--maroon); min-width:40px;">Day 4</span> Kushmanda Puja</div>
            <div style="background:#fef3c7; padding:0.5rem 0.8rem; border-radius:8px; display:flex; gap:0.5rem;"><span style="font-weight:700; color:var(--maroon); min-width:40px;">Day 5</span> Upang Lalita Vrat, Skandamata Puja</div>
            <div style="background:#fef3c7; padding:0.5rem 0.8rem; border-radius:8px; display:flex; gap:0.5rem;"><span style="font-weight:700; color:var(--maroon); min-width:40px;">Day 6</span> Katyayani Puja</div>
            <div style="background:#fef3c7; padding:0.5rem 0.8rem; border-radius:8px; display:flex; gap:0.5rem;"><span style="font-weight:700; color:var(--maroon); min-width:40px;">Day 7</span> Maha Saptami, Kalaratri Puja</div>
            <div style="background:#c0392b; color:white; padding:0.5rem 0.8rem; border-radius:8px; display:flex; gap:0.5rem; font-weight:700;"><span style="min-width:40px;">Day 8</span> Mahashtami, Durgashtami, Kumari Puja, Mahagauri Puja ⭐</div>
            <div style="background:#fef3c7; padding:0.5rem 0.8rem; border-radius:8px; display:flex; gap:0.5rem;"><span style="font-weight:700; color:var(--maroon); min-width:40px;">Day 9</span> Maha Navami, Navami Homa, Siddhidatri Puja</div>
          </div>
        </div>

        <!-- Observances -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎉 अनुष्ठान (Observances)</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.45rem;">
            <div>🏺 Ghatasthapana on first day</div>
            <div>🙏 Worshipping 9 forms of Goddess Durga</div>
            <div>🍽️ 9 days long Navratri fast</div>
            <div>🌾 Sowing Sapta-Dhanya (seven grains)</div>
            <div>🪔 Installing Jyoti Kalash for 9 days</div>
            <div>📖 Recitation of Durga Saptashati</div>
            <div>💃 Performing Dandiya and Garba in honor of the Goddess</div>
            <div>🎨 Adorning as per 9 Navratri colors</div>
            <div>👧 Kanya Puja (Kumari Puja)</div>
            <div>🔥 Chandi Homa</div>
          </div>
        </div>

        <!-- Regional Variance -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🗺️ क्षेत्रीय विविधता</div>
          <div style="display:flex; flex-direction:column; gap:0.8rem; font-size:0.87rem; color:#334155;">
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;"><strong style="color:var(--maroon);">🏮 West Bengal & Assam:</strong> Navratri observed as Durga Puja (Katyayani Kalpa). 3 main days — Maha Saptami, Durga Ashtami, Durga Navami.</div>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;"><strong style="color:var(--maroon);">💃 Gujarat & North India:</strong> Bhadrakali Kalpa — each day dedicated to one of nine forms of Durga. Kanya Puja and Jyoti Kalash are key rituals. Famous for <strong>Garba</strong> and <strong>Dandiya</strong>.</div>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;"><strong style="color:var(--maroon);">🪆 South India (Bommala Koluvu):</strong> Also known as Golu/Kolu/Bombe Habba — dolls displayed publicly. Days 1-3: Goddess Kali, Days 4-6: Goddess Lakshmi, Days 7-9: Goddess Saraswati.</div>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;"><strong style="color:var(--maroon);">⚔️ Karnataka:</strong> Day 9 = Ayudha Puja. Weapons and vehicles are worshipped ritualistically.</div>
          </div>
        </div>

        <!-- Similar Festivals -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🌏 समान त्यौहार</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.9rem;">
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🏮 Durga Puja - West Bengal</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🏹 Vijayadashami</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🐘 Mysore Dasara - Karnataka</div>
          </div>
        </div>

      </div>
    </section>`;
  html = html.replace('</body>', navratriPage + '\n  </body>');
}

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Navratri page!');
