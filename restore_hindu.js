const fs = require('fs');

let code = fs.readFileSync('index.html', 'utf8');

const hinduVratsHTML = `
      <!-- 🌺 HINDU VRATS 🌺 -->
      <div class="home-section-row" style="margin-top:1.5rem">
        <span class="home-section-title" style="color:var(--saffron); text-align:center; width:100%;">हिन्दू व्रत एवं उपवास</span>
      </div>
      <div class="vrat-home-grid" id="vrat-home-grid"></div>
`;

// Insert it before Muhurat
code = code.replace(/<!-- 🌺 HINDU MUHURAT 🌺 -->/, hinduVratsHTML + '\n      <!-- 🌺 HINDU MUHURAT 🌺 -->');

fs.writeFileSync('index.html', code, 'utf8');
console.log('Restored Hindu Vrats grid!');
