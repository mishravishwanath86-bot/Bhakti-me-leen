const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const oldDiwaliPage = html.match(/<!-- 🌺 DIWALI PAGE 🌺 -->[\s\S]*?<\/section>/)[0];

const newDiwaliPage = `<!-- 🌺 DIWALI PAGE 🌺 -->
    <section id="page-diwali" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-top10">❮</button>
        <h2>दीपावली (Diwali)</h2>
        <span style="width:36px"></span>
      </div>
      <div class="sankashti-hero">
        <img src="assets/top10_1.jpg" alt="Diwali" style="width:100%; height:220px; object-fit:cover;">
        <div class="sh-overlay">
          <h1>दीपावली (Diwali)</h1>
          <p>रोशनी और खुशियों का महापर्व</p>
        </div>
      </div>

      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding: 1.5rem 1rem 4rem;">

        <!-- Description -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <p style="font-size:0.95rem; color:#334155; line-height:1.75; margin:0;">
            <strong>Diwali</strong>, also known as <strong>Deepavali</strong>, is the most significant religious festival among Hindus — the <strong>festival of lights</strong>. It spiritually signifies the victory of <em>light over darkness</em>, <em>knowledge over ignorance</em>, <em>good over evil</em> and <em>hope over despair</em>. At most places Diwali is celebrated for <strong>five days</strong>.
          </p>
        </div>

        <!-- Origin -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📜 उत्पत्ति एवं महत्व</div>
          <p style="font-size:0.9rem; color:#334155; line-height:1.7; margin:0 0 0.8rem;">Diwali has its origin in the <strong>Era of Lord Rama</strong>, or probably even before that at the time of churning of milky ocean when Goddess Lakshmi came out as the boon to the Gods and whole humanity.</p>
          <p style="font-size:0.9rem; color:#334155; line-height:1.7; margin:0;">All legends signify the victory of light over darkness, knowledge over ignorance, good over evil and hope over despair.</p>
        </div>

        <!-- Deities -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🙏 देवी-देवता (Deity/s)</div>
          <div style="font-size:0.9rem; color:#334155; line-height:1.7;">
            <div style="margin-bottom:0.5rem;"><strong>प्रमुख:</strong> Goddess Lakshmi, Lord Ganesha, Lord Kuber</div>
            <div><strong>अन्य:</strong> Lord Yamraj, God Dhanvantari, God Hanuman, Goddess Kali, Goddess Saraswati, Lord Krishna, Demon King Bali</div>
          </div>
        </div>

        <!-- 5 Days -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🪔 पाँच दिन के त्यौहार (5 Days)</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem;">
            <div style="background:#fef3c7; padding:0.6rem 1rem; border-radius:8px; font-size:0.9rem; display:flex; gap:0.8rem;"><span style="font-weight:800; color:var(--maroon); min-width:40px;">Day 1</span><span>Dhantrayodashi (Dhanteras)</span></div>
            <div style="background:#fef3c7; padding:0.6rem 1rem; border-radius:8px; font-size:0.9rem; display:flex; gap:0.8rem;"><span style="font-weight:800; color:var(--maroon); min-width:40px;">Day 2</span><span>Narak Chaturdashi (Chhoti Diwali)</span></div>
            <div style="background:#f97316; color:white; padding:0.6rem 1rem; border-radius:8px; font-size:0.9rem; display:flex; gap:0.8rem; font-weight:700;"><span style="min-width:40px;">Day 3</span><span>Lakshmi Puja ⭐ (Main Diwali)</span></div>
            <div style="background:#fef3c7; padding:0.6rem 1rem; border-radius:8px; font-size:0.9rem; display:flex; gap:0.8rem;"><span style="font-weight:800; color:var(--maroon); min-width:40px;">Day 4</span><span>Govardhan Puja (Annakut)</span></div>
            <div style="background:#fef3c7; padding:0.6rem 1rem; border-radius:8px; font-size:0.9rem; display:flex; gap:0.8rem;"><span style="font-weight:800; color:var(--maroon); min-width:40px;">Day 5</span><span>Bhaiya Dooj</span></div>
          </div>
        </div>

        <!-- Date and Time -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 दीपावली तिथि</div>
          <div style="font-size:0.88rem; color:#475569; line-height:1.8;">
            <div style="margin-bottom:0.8rem;"><strong style="color:#334155;">Amanta Calendar:</strong><br>
            • Begins: Krishna Paksha Trayodashi (28th day) of Ashwin (7th month)<br>
            • Ends: Shukla Paksha Dwitiya (2nd day) of Kartik (8th month)</div>
            <div><strong style="color:#334155;">Purnimanta Calendar:</strong><br>
            • Begins: Krishna Paksha Trayodashi (13th day) of Kartik (8th month)<br>
            • Ends: Shukla Paksha Dwitiya (17th day) of Kartik (8th month)</div>
          </div>
        </div>

        <!-- Observances -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🎉 अनुष्ठान (Observances)</div>
          <div style="font-size:0.88rem; color:#334155; display:flex; flex-direction:column; gap:0.45rem; line-height:1.6;">
            <div>🏠 Cleaning and decorating homes</div>
            <div>👗 Buying new clothes and jewelry</div>
            <div>🛍️ Buying new household items</div>
            <div>🍬 Preparing traditional home-made sweets</div>
            <div>🙏 Worshipping numerous deities</div>
            <div>🪔 Lighting Diyas and decorating with electric lamps</div>
            <div>🎆 Bursting firecrackers</div>
            <div>💰 Trying Diwali remedies to gain wealth</div>
            <div>👨‍👩‍👧‍👦 Visiting relatives and family friends</div>
            <div>🎁 Distributing sweets, dry-fruits and gifts</div>
          </div>
        </div>

        <!-- Regional Variance -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🗺️ क्षेत्रीय विविधता (Regional Variance)</div>
          <p style="font-size:0.88rem; color:#334155; line-height:1.7; margin:0 0 0.8rem;">Diwali celebrations are more extravagant in north Indian states. <strong>Delhi, Hyderabad and Mumbai</strong> are the most suitable metros for spectacular fireworks.</p>
          <p style="font-size:0.88rem; color:#334155; line-height:1.7; margin:0;">In <strong>Chennai (Tamil Nadu)</strong>, Narak Chaturdashi is more significant than Lakshmi Puja. In <strong>Kolkata (West Bengal)</strong>, devotees worship <strong>Goddess Kali</strong> rather than Goddess Lakshmi on the third day.</p>
        </div>

        <!-- Other Religions -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🌐 अन्य धर्मों में दीपावली</div>
          <div style="font-size:0.88rem; color:#334155; line-height:1.7; display:flex; flex-direction:column; gap:0.5rem;">
            <div>⚔️ <strong>Sikhism:</strong> Bandi Chhor Divas</div>
            <div>🕉️ <strong>Jainism:</strong> Day to commemorate Mahavir</div>
            <div style="margin-top:0.5rem; border-top:1px solid #e2e8f0; padding-top:0.5rem;"><strong>Similar Festivals:</strong><br>Dev Diwali - Varanasi<br>Kartigai Deepam - Tamil Nadu</div>
          </div>
        </div>

      </div>
    </section>`;

html = html.replace(oldDiwaliPage, newDiwaliPage);
const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Updated Diwali page with complete data from 3 screenshots!');
