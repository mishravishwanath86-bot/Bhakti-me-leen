const fs = require('fs');
let code = fs.readFileSync('index.html', 'utf8');

const top10PageHTML = `
    <!-- 🌺 TOP 10 FESTIVALS PAGE 🌺 -->
    <section id="page-top10" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-home">❮</button>
        <h2>प्रमुख 10 हिन्दू त्यौहार</h2>
        <span style="width:36px"></span>
      </div>
      
      <div class="sankashti-hero">
        <img src="assets/top10_1.jpg" alt="Top 10 Hero" id="top10-hero-img">
        <div class="sh-overlay">
          <h1 id="top10-hero-title">प्रमुख 10 हिन्दू त्यौहार</h1>
          <p id="top10-hero-subtitle">वर्ष के सबसे बड़े त्यौहार</p>
        </div>
      </div>

      <div class="section-content" style="background:#fffcf7; margin-top:-1rem; border-top-left-radius:20px; border-top-right-radius:20px; position:relative; padding-top:2rem;">
        <div id="top10-list-container" style="display:flex; flex-direction:column; gap:1.2rem; padding-bottom:3rem;">
        </div>
      </div>
    </section>
`;

code = code.replace(/<\/body>/, `${top10PageHTML}\n  </body>`);

fs.writeFileSync('index.html', code, 'utf8');
console.log('Added page-top10 to HTML');
