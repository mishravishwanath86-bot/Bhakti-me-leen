const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Replace entire Holi page with rich data
const oldHoliPage = html.match(/<!-- 🌺 HOLI PAGE 🌺 -->[\s\S]*?<\/section>/)[0];

const newHoliPage = `<!-- 🌺 HOLI PAGE 🌺 -->
    <section id="page-holi" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-top10">❮</button>
        <h2>होली (Holi)</h2>
        <span style="width:36px"></span>
      </div>
      
      <div class="sankashti-hero">
        <img src="assets/top10_2.jpg" alt="Holi" style="width:100%; height:220px; object-fit:cover;">
        <div class="sh-overlay">
          <h1>होली (Holi)</h1>
          <p>रंगों का महापर्व - रंगवाली होली / धुलंडी</p>
        </div>
      </div>

      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding: 1.5rem 1rem 4rem;">

        <!-- Description -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <p style="font-size:0.95rem; color:#334155; line-height:1.7; margin:0;">
            Holi is one of the most significant festivals among Hindus. Holi, which is also known as <strong>Rangawali Holi</strong> or <strong>Dhulandi</strong>, is the festival of colors. Holi celebrations start a night before Holi with <strong>Holika bonfire</strong>, when people worship Holika and burn her in huge bonfire.
          </p>
          <div style="margin-top:1rem; display:flex; flex-direction:column; gap:0.5rem; font-size:0.9rem; color:#475569;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Dhulandi, Festival of Colors</div>
            <div><strong style="color:var(--maroon);">Significance:</strong> Celebrating victory of good over evil</div>
            <div><strong style="color:var(--maroon);">Key Rituals:</strong> Holi Puja, Playing Holi with Colors</div>
          </div>
        </div>

        <!-- Holi Dates -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 होली तिथियाँ</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.92rem;">
            <div style="color:#475569;">2025 Holi date: <strong style="color:#334155;">March 14 (Friday)</strong></div>
            <div style="color:#475569;">2026 Holi date: <strong style="color:#334155;">March 04 (Wednesday)</strong></div>
            <div style="color:#a50000; font-weight:700;">2027 Holi date: March 22 (Monday) ← Current</div>
            <div style="color:#475569;">2028 Holi date: <strong style="color:#334155;">March 11 (Saturday)</strong></div>
          </div>
          <div style="margin-top:1rem; border-top:1px solid #e2e8f0; padding-top:0.8rem; font-size:0.88rem; color:#475569;">
            <div><strong>Hindu Calendar Date:</strong></div>
            <div>Purnimanta - Pratipada of Chaitra month (Krishna Paksha)</div>
            <div>Amanta - Pratipada of Phalguna month (Krishna Paksha)</div>
          </div>
        </div>

        <!-- Holika Dahan Section -->
        <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🔥 होलिका दहन (Holika Dahan)</div>

        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1rem; font-size:0.9rem; color:#334155;">
          <p style="margin:0 0 0.8rem; line-height:1.7;">Holika Dahan is also known as <strong>Chhoti Holi</strong>, Jalanewali Holi. The bonfire is reminder of the symbolic victory of good over evil.</p>
          <div style="display:flex; flex-direction:column; gap:0.4rem;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Chhoti Holi, Jalanewali Holi</div>
            <div><strong style="color:var(--maroon);">Deity(s):</strong> Holika, Prahlada</div>
            <div><strong style="color:var(--maroon);">Mythological Figures:</strong> Lord Narasimha, Lord Vishnu, Prahlada, Hiranyakashipu, Holika</div>
          </div>
        </div>

        <!-- Holika Dahan Dates -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 होलिका दहन तिथियाँ</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.92rem;">
            <div style="color:#475569;">2025: <strong>March 13 (Thursday)</strong></div>
            <div style="color:#475569;">2026: <strong>March 03 (Tuesday)</strong></div>
            <div style="color:#a50000; font-weight:700;">2027: March 21 (Sunday) ← Current</div>
            <div style="color:#475569;">2028: <strong>March 10 (Friday)</strong></div>
          </div>
        </div>

        <!-- 2027 Muhurat Table -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">⏰ 2027 होलिका दहन मुहूर्त</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.82rem;">
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">New Delhi</div><div style="color:#334155;">06:33 PM – 08:55 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Noida</div><div style="color:#334155;">06:32 PM – 08:54 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Pune</div><div style="color:#334155;">06:46 PM – 09:08 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Jaipur</div><div style="color:#334155;">06:38 PM – 09:00 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Mumbai</div><div style="color:#334155;">06:50 PM – 09:12 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Gurgaon</div><div style="color:#334155;">06:33 PM – 08:56 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Chennai</div><div style="color:#334155;">06:21 PM – 08:42 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Bengaluru</div><div style="color:#334155;">06:30 PM – 08:53 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Kolkata</div><div style="color:#334155;">06:21 PM – 08:10 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Hyderabad</div><div style="color:#334155;">06:27 PM – 08:50 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Ahmedabad</div><div style="color:#334155;">06:51 PM – 09:13 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Chandigarh</div><div style="color:#334155;">06:35 PM – 08:57 PM</div></div>
          </div>
        </div>

        <!-- Observances -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🙏 अनुष्ठान (Observances)</div>
          <div style="font-size:0.9rem; color:#334155; display:flex; flex-direction:column; gap:0.5rem;">
            <div style="display:flex; align-items:center; gap:0.5rem;"><span>🎨</span> Playing Holi with colors</div>
            <div style="display:flex; align-items:center; gap:0.5rem;"><span>🥛</span> Preparing Thandai</div>
            <div style="display:flex; align-items:center; gap:0.5rem;"><span>🔥</span> Holika Puja</div>
            <div style="display:flex; align-items:center; gap:0.5rem;"><span>🌾</span> Roasting green cereals in Holika bonfire</div>
          </div>
        </div>

        <!-- Recipes -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🍬 पारंपरिक व्यंजन (Recipes)</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.9rem;">
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px; text-align:center;">🧆 Gujiya</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px; text-align:center;">🍮 Gulab Jamun</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px; text-align:center;">🥛 Thandai</div>
            <div style="background:#fef9ec; padding:0.6rem; border-radius:8px; text-align:center;">🌿 Bhang</div>
          </div>
        </div>

        <!-- Links -->
        <div style="display:flex; flex-direction:column; gap:0.8rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.4rem;">🔗 अधिक जानकारी</div>
          <a href="https://www.Sanatan Panchang.com/hindu-festivals/holi/holi.html" style="display:flex; align-items:center; gap:0.8rem; background:#fff; padding:1rem; border-radius:12px; text-decoration:none; border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.07);">
            <span style="font-size:1.4rem;">🎨</span>
            <div><div style="font-size:0.95rem; font-weight:700; color:var(--maroon);">Holi Summary</div><div style="font-size:0.8rem; color:#64748b;">Sanatan Panchang.com</div></div>
          </a>
          <a href="https://www.Sanatan Panchang.com/hindu-festivals/holi/holika-dahan.html" style="display:flex; align-items:center; gap:0.8rem; background:#fff; padding:1rem; border-radius:12px; text-decoration:none; border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.07);">
            <span style="font-size:1.4rem;">🔥</span>
            <div><div style="font-size:0.95rem; font-weight:700; color:var(--maroon);">Holika Dahan Summary</div><div style="font-size:0.8rem; color:#64748b;">Sanatan Panchang.com</div></div>
          </a>
          <a href="https://www.Sanatan Panchang.com/festivals/holi/festivals-holika-dahan-timings.html" style="display:flex; align-items:center; gap:0.8rem; background:#fff; padding:1rem; border-radius:12px; text-decoration:none; border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.07);">
            <span style="font-size:1.4rem;">⏰</span>
            <div><div style="font-size:0.95rem; font-weight:700; color:var(--maroon);">Holika Dahan Muhurat</div><div style="font-size:0.8rem; color:#64748b;">Sanatan Panchang.com</div></div>
          </a>
          <a href="https://www.Sanatan Panchang.com/festivals/holi/info/holi.html" style="display:flex; align-items:center; gap:0.8rem; background:#fff; padding:1rem; border-radius:12px; text-decoration:none; border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.07);">
            <span style="font-size:1.4rem;">ℹ️</span>
            <div><div style="font-size:0.95rem; font-weight:700; color:var(--maroon);">About Holi (Dhulandi)</div><div style="font-size:0.8rem; color:#64748b;">Sanatan Panchang.com</div></div>
          </a>
        </div>

      </div>
    </section>`;

html = html.replace(oldHoliPage, newHoliPage);

// Now add Rakhi page
const rakhiPage = `
    <!-- 🌺 RAKHI PAGE 🌺 -->
    <section id="page-rakhi" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-top10">❮</button>
        <h2>रक्षा बंधन (Rakhi)</h2>
        <span style="width:36px"></span>
      </div>
      
      <div class="sankashti-hero">
        <img src="assets/top10_3.jpg" alt="Raksha Bandhan" style="width:100%; height:220px; object-fit:cover;">
        <div class="sh-overlay">
          <h1>रक्षा बंधन</h1>
          <p>भाई-बहन के प्रेम का पावन पर्व</p>
        </div>
      </div>

      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding: 1.5rem 1rem 4rem;">

        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:0.95rem; color:#334155; line-height:1.7;">
            Raksha Bandhan is the sacred festival of the bond between brother and sister. On this day, sisters tie a sacred thread (Rakhi) on the wrist of their brothers and pray for their well-being. Brothers in return promise to protect their sisters.
          </div>
          <div style="margin-top:1rem; display:flex; flex-direction:column; gap:0.5rem; font-size:0.9rem; color:#475569;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Rakhi, Rakhi Purnima</div>
            <div><strong style="color:var(--maroon);">Significance:</strong> Bond of love between brothers and sisters</div>
            <div><strong style="color:var(--maroon);">Hindu Calendar Date:</strong> Purnima of Shravana month</div>
          </div>
        </div>

        <!-- Links -->
        <div style="display:flex; flex-direction:column; gap:0.8rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.4rem;">🔗 अधिक जानकारी</div>
          <a href="https://www.Sanatan Panchang.com/festivals/rakhi/info/rakhi.html" style="display:flex; align-items:center; gap:0.8rem; background:#fff; padding:1rem; border-radius:12px; text-decoration:none; border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.07);">
            <span style="font-size:1.4rem;">💛</span>
            <div><div style="font-size:0.95rem; font-weight:700; color:var(--maroon);">About Rakhi</div><div style="font-size:0.8rem; color:#64748b;">Sanatan Panchang.com</div></div>
          </a>
        </div>

      </div>
    </section>`;

html = html.replace(/<\/body>/, rakhiPage + '\n  </body>');
fs.writeFileSync('index.html', html, 'utf8');
console.log('Updated Holi page with full data and added Rakhi page!');
