const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Add page: 'page-diwali' to Diwali entry
code = code.replace(
  "name: 'दीपावली (Diwali)',",
  "name: 'दीपावली (Diwali)', page: 'page-diwali',"
);

fs.writeFileSync('app.js', code, 'utf8');

// Also ensure index.html has a page-diwali section
let html = fs.readFileSync('index.html', 'utf8');

// Check if page-diwali already exists
if(!html.includes('id="page-diwali"')) {
  const diwaliPage = `
    <!-- 🌺 DIWALI PAGE 🌺 -->
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
        
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <p style="font-size:0.95rem; color:#334155; line-height:1.7; margin:0;">
            Diwali or Deepawali is the Hindu festival of lights celebrated with great enthusiasm all over India and across the world. It is one of the biggest festivals of Hinduism symbolizing the spiritual victory of light over darkness.
          </p>
          <div style="margin-top:1rem; display:flex; flex-direction:column; gap:0.5rem; font-size:0.9rem; color:#475569;">
            <div><strong style="color:var(--maroon);">Also Called:</strong> Deepawali, Festival of Lights</div>
            <div><strong style="color:var(--maroon);">Significance:</strong> Victory of light over darkness, good over evil</div>
            <div><strong style="color:var(--maroon);">Key Deity:</strong> Goddess Lakshmi & Lord Ganesha</div>
          </div>
        </div>

        <div style="display:flex; flex-direction:column; gap:0.8rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.4rem;">🔗 अधिक जानकारी</div>
          <a href="https://www.Sanatan Panchang.com/diwali/info/diwali.html" style="display:flex; align-items:center; gap:0.8rem; background:#fff; padding:1rem; border-radius:12px; text-decoration:none; border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.07);">
            <span style="font-size:1.4rem;">🪔</span>
            <div><div style="font-size:0.95rem; font-weight:700; color:var(--maroon);">About Diwali</div><div style="font-size:0.8rem; color:#64748b;">Sanatan Panchang.com</div></div>
          </a>
          <a href="https://www.Sanatan Panchang.com/festivals/lakshmipuja/festivals-lakshmipuja-timings.html" style="display:flex; align-items:center; gap:0.8rem; background:#fff; padding:1rem; border-radius:12px; text-decoration:none; border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.07);">
            <span style="font-size:1.4rem;">⏰</span>
            <div><div style="font-size:0.95rem; font-weight:700; color:var(--maroon);">Deepavali Muhurat</div><div style="font-size:0.8rem; color:#64748b;">Sanatan Panchang.com</div></div>
          </a>
          <a href="https://www.Sanatan Panchang.com/hindu-festivals/diwali/diwali.html" style="display:flex; align-items:center; gap:0.8rem; background:#fff; padding:1rem; border-radius:12px; text-decoration:none; border:1px solid #e2e8f0; box-shadow:0 1px 4px rgba(0,0,0,0.07);">
            <span style="font-size:1.4rem;">📖</span>
            <div><div style="font-size:0.95rem; font-weight:700; color:var(--maroon);">Deepavali Summary</div><div style="font-size:0.8rem; color:#64748b;">Sanatan Panchang.com</div></div>
          </a>
        </div>

      </div>
    </section>`;
  html = html.replace(/<\/body>/, diwaliPage + '\n  </body>');
}

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Diwali page and cache busted!');
