const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

if(!html.includes('id="page-ramnavami"')) {
  const page = `
    <!-- 🌺 RAM NAVAMI PAGE 🌺 -->
    <section id="page-ramnavami" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-top10">❮</button>
        <h2>राम नवमी (Rama Navami)</h2>
        <span style="width:36px"></span>
      </div>
      <div class="sankashti-hero">
        <img src="assets/festival_ramnavami.jpg" alt="Ram Navami" style="width:100%; height:220px; object-fit:cover;">
        <div class="sh-overlay">
          <h1>राम नवमी</h1>
          <p>प्रभु श्री राम का जन्मोत्सव</p>
        </div>
      </div>
      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding:1.5rem 1rem 4rem;">

        <!-- Description -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <p style="font-size:0.92rem; color:#334155; line-height:1.75; margin:0 0 0.8rem;">
            <strong>Rama Navami</strong> is observed as the birth anniversary of <strong>Lord Rama</strong> — the seventh incarnation of <strong>Lord Vishnu</strong>. Devotees keep a day long fast and worship Him with all rituals.
          </p>
          <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; font-size:0.88rem; color:#475569; line-height:1.6;">
            In North India, Rama Navami coincides with the last day of <strong>Chaitra Navratri</strong>. Hence Navratri Puja during Chaitra month is also known as <strong>Rama Navratri</strong>.
          </div>
        </div>

        <!-- Origin -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📜 उत्पत्ति एवं महत्व</div>
          <p style="font-size:0.9rem; color:#334155; line-height:1.75; margin:0;">
            Rama Navami is observed since the <strong>Era of Lord Rama</strong>. As per Vedic time keeping, <strong>Lord Rama was born about a million years ago during Treta Yuga</strong>. Hindus have been celebrating Rama Navami since ages and no historic records are kept to count the exact years.
          </p>
        </div>

        <!-- Deity -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🙏 देवी-देवता</div>
          <div style="font-size:0.88rem; color:#334155; margin-bottom:0.6rem;">Main deity: <strong>Lord Rama</strong></div>
          <div style="font-size:0.88rem; color:#334155; line-height:1.7; background:#fef9ec; padding:0.8rem; border-radius:8px;">
            Also worshipped: <strong>Mata Kaushalya</strong> (mother), <strong>King Dasharatha</strong> (father), <strong>Devi Sita</strong> (wife), <strong>Bharata</strong>, <strong>Lakshmana</strong>, <strong>Shatrughna</strong> (brothers), <strong>Bhakta Hanuman</strong> (devotee)
          </div>
          <div style="margin-top:0.8rem; font-size:0.88rem; color:#a50000; font-weight:600; background:#fff3f3; padding:0.7rem; border-radius:8px;">
            📅 Hindu Calendar: Shukla Paksha Navami (9th day) of Chaitra (1st month)
          </div>
        </div>

        <!-- Observances -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎉 अनुष्ठान (Observances)</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.45rem;">
            <div>🍽️ A day long fast</div>
            <div>🙏 Worshipping Lord Rama</div>
            <div>📖 Listen or narrating the epic Ramayana or Nama Ramayanam</div>
            <div>💒 Performing ceremonial wedding of Lord Rama and Goddess Sita</div>
            <div>🚩 Conducting Rama Navami procession</div>
            <div>🔥 Conducting Hawan (Homa) before breaking the fast on the next day</div>
          </div>
        </div>

        <!-- Regional Variance -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🗺️ क्षेत्रीय विविधता</div>
          <div style="display:flex; flex-direction:column; gap:0.8rem; font-size:0.87rem; color:#334155;">
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;">
              <strong style="color:var(--maroon);">🕌 Uttar Pradesh (Ayodhya):</strong> Most significant place for Rama Navami. Devotees take holy dip in sacred river <strong>Sarayu</strong> and visit <strong>Kanak Bhawan</strong> temple. Ayodhya during Rama Navami is similar to what Mathura is during Krishna Janmashtami.
            </div>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;">
              <strong style="color:var(--maroon);">🏔️ Andhra Pradesh (Tirumala):</strong> Celebrated with great fervor. TTD observes <em>Shri Rama Navami Asthanam</em>.
            </div>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;">
              <strong style="color:var(--maroon);">🌸 Telangana (Bhadrachalam):</strong> Wedding anniversary of Lord Rama and Sita celebrated with fanfare as <strong>Shri Ramanavami Kalyanam Utsava</strong>.
            </div>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;">
              <strong style="color:var(--maroon);">🌴 Tamil Nadu:</strong> Devotees perform <em>Kalyanotsavam</em> — symbolic marriage ceremony. Special drink <strong>Panakam</strong> (ginger, jaggery, cardamom) is served — natural body coolant, like Gangajal in North India.
            </div>
            <div style="background:#fef9ec; padding:0.8rem; border-radius:8px; line-height:1.65;">
              <strong style="color:var(--maroon);">🌍 ISKCON:</strong> Special events, procession of Lord Rama and Goddess Sita, Abhishekam, and Homa are performed. Lord Rama, being the incarnation of Lord Vishnu, is as important as Lord Krishna for ISKCON followers.
            </div>
          </div>
        </div>

        <!-- Public Life -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🏛️ सार्वजनिक जीवन</div>
          <p style="font-size:0.88rem; color:#334155; line-height:1.7; margin:0;">
            Rama Navami is an <strong>optional gazetted holiday</strong> in India. However, in <strong>North India</strong>, government offices, schools and colleges might keep one day off during Rama Navami.
          </p>
        </div>

      </div>
    </section>`;
  html = html.replace('</body>', page + '\n  </body>');
}

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Ram Navami page added!');
