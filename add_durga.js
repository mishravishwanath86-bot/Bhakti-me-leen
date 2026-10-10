const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

if(!html.includes('id="page-durgapuja"')) {
  const durgaPage = `
    <!-- 🌺 DURGA PUJA PAGE 🌺 -->
    <section id="page-durgapuja" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-top10">❮</button>
        <h2>दुर्गा पूजा (Durga Puja)</h2>
        <span style="width:36px"></span>
      </div>
      <div class="sankashti-hero">
        <img src="assets/top10_5.jpg" alt="Durga Puja" style="width:100%; height:220px; object-fit:cover;">
        <div class="sh-overlay">
          <h1>दुर्गा पूजा</h1>
          <p>माँ दुर्गा की विशेष आराधना</p>
        </div>
      </div>

      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding: 1.5rem 1rem 4rem;">

        <!-- Description -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <p style="font-size:0.92rem; color:#334155; line-height:1.75; margin:0 0 0.8rem;">
            <strong>Durga Puja</strong> is an annual Hindu festival dedicated to <strong>Goddess Durga</strong>. It is celebrated during <strong>Devi Paksha</strong> — a 15-day period of Ashwin lunar month. Devi Paksha literally translates to <em>"Fortnight of the Goddess"</em>.
          </p>
          <p style="font-size:0.9rem; color:#334155; line-height:1.75; margin:0;">
            Widely celebrated in <strong>West Bengal, Odisha, Assam, Manipur and Tripura</strong>. In these states, Durga Puja is not only the biggest Hindu festival but also the most significant socio-cultural event. Also known as <strong>Durgotsava</strong> and <strong>Sharadotsava</strong>.
          </p>
        </div>

        <!-- Origin & Significance -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📜 उत्पत्ति एवं महत्व</div>
          <div style="font-size:0.9rem; color:#334155; line-height:1.75; display:flex; flex-direction:column; gap:0.8rem;">
            <p style="margin:0;">As per Puranic legends, <strong>Lord Rama</strong> worshipped Goddess Durga before going to war with <strong>Ravana</strong>. He performed <strong>Chandi Homa</strong> (Akal Bodhan) and sought her blessing. As Lord Rama was blessed with victory over Ravana, this time is considered most suitable to seek blessings of Goddess Durga.</p>
            <p style="margin:0;">As per <strong>Devi Mahatmya</strong>, Durga Puja marks the victory of Goddess Durga over <strong>Mahishasura</strong> — victory of good over evil.</p>
          </div>
        </div>

        <!-- Deities -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🙏 देवी-देवता (Deity/s)</div>
          <div style="font-size:0.9rem; color:#334155; line-height:1.7;">
            <div style="margin-bottom:0.6rem;"><strong style="color:var(--maroon);">प्रमुख:</strong> Goddess Durga (also an aspect of Goddess Parvati), Lord Shiva (as consort)</div>
            <div><strong style="color:var(--maroon);">4 सन्तान:</strong> Goddess Lakshmi, Goddess Saraswati, Lord Ganesha, Lord Kartikeya<br>
            <span style="font-size:0.85rem; color:#475569;">(In West Bengal, all four are considered children of Goddess Durga)</span></div>
          </div>
        </div>

        <!-- Date & Time -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 तिथि एवं काल</div>
          <div style="font-size:0.88rem; color:#a50000; font-weight:600; line-height:1.8; margin-bottom:0.8rem;">
            <div>Durga Puja begins - Sixth (6th day) of Ashwin (7th lunar month) Shukla Paksha</div>
            <div>Durga Puja ends - Tenth (10th day) of Ashwin Shukla Paksha</div>
          </div>
          <p style="font-size:0.85rem; color:#475569; margin:0;">The ritualistic Durga Puja begins on the <strong>sixth day of Devi Paksha</strong>. Chandi Patha narration in West Bengal begins from the day of Mahalaya.</p>
        </div>

        <!-- 5 Days -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🗓️ पाँच दिन (Durga Puja Festivals List)</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem;">
            <div style="background:#fef3c7; padding:0.6rem 1rem; border-radius:8px; font-size:0.88rem; display:flex; gap:0.8rem;"><span style="font-weight:800; color:var(--maroon); min-width:45px;">Day 1</span><span>Akal Bodhan, Kalparambha (6th day of Devi Paksha)</span></div>
            <div style="background:#fef3c7; padding:0.6rem 1rem; border-radius:8px; font-size:0.88rem; display:flex; gap:0.8rem;"><span style="font-weight:800; color:var(--maroon); min-width:45px;">Day 2</span><span>Navpatrika Puja, Kolabou Puja (7th day)</span></div>
            <div style="background:#c0392b; color:white; padding:0.6rem 1rem; border-radius:8px; font-size:0.88rem; display:flex; gap:0.8rem; font-weight:700;"><span style="min-width:45px;">Day 3</span><span>Durga Ashtami, Sandhi Puja ⭐ (8th day)</span></div>
            <div style="background:#fef3c7; padding:0.6rem 1rem; border-radius:8px; font-size:0.88rem; display:flex; gap:0.8rem;"><span style="font-weight:800; color:var(--maroon); min-width:45px;">Day 4</span><span>Maha Navami, Navami Homa (9th day)</span></div>
            <div style="background:#fef3c7; padding:0.6rem 1rem; border-radius:8px; font-size:0.88rem; display:flex; gap:0.8rem;"><span style="font-weight:800; color:var(--maroon); min-width:45px;">Day 5</span><span>Vijayadashami, Durga Visarjan, Sindoor Utsav (10th day)</span></div>
          </div>
        </div>

        <!-- In West Bengal -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🏮 West Bengal mein 6 Dine (Mahalaya se)</div>
          <div style="font-size:0.88rem; color:#475569; line-height:1.7;">
            Mahalaya → Shashthi → Saptami → Ashtami → Navami → <strong>Vijayadashami</strong>
          </div>
        </div>

        <!-- Observances -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎉 अनुष्ठान (Observances)</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.45rem;">
            <div>📖 Narrating or listening Chandi Patha</div>
            <div>🎪 Display of decorated Pandal with sculptures of Goddess Durga</div>
            <div>🌸 Morning Pushpanjali to Goddess Durga for first 4 days</div>
            <div>🙏 Shodashopachar Durga Puja from Saptami to Navami</div>
            <div>🔥 Dhunuchi Dance in front of Goddess Durga</div>
            <div>🕯️ Performing Chandi Homa on Maha Navami</div>
            <div>🏮 Lighting 108 earthen lamps during Sandhi Puja</div>
            <div>🌊 Durga Visarjan on Vijayadashami day</div>
            <div>🔴 Playing with Sindur during Sindur Utsav</div>
            <div>🙌 Exchange of Vijaya greetings</div>
          </div>
        </div>

        <!-- Similar Festivals -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🌏 समान त्यौहार (Similar Festivals)</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.9rem;">
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🙏 Shardiya Navratri - Gujarat</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🇳🇵 Dashain - Nepal</div>
            <div style="background:#fef3c7; padding:0.6rem 0.8rem; border-radius:8px;">🐘 Mysore Dasara - Karnataka</div>
          </div>
        </div>

      </div>
    </section>`;
  html = html.replace('</body>', durgaPage + '\n  </body>');
}

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Durga Puja page!');
