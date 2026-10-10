const fs = require('fs');
let code = fs.readFileSync('index.html', 'utf8');

const htmlBlock = `
      <!-- 🌺 HINDU FESTIVALS 🌺 -->
      <div class="home-section-row" style="margin-top:1.5rem">
        <span class="home-section-title" style="color:var(--saffron); text-align:center; width:100%;">हिन्दू त्यौहार (पर्व)</span>
      </div>
      <div class="vrat-home-grid" id="fest-home-grid"></div>
`;

// Insert it after vrat-home-grid
code = code.replace(/<div class="vrat-home-grid" id="vrat-home-grid"><\/div>/, `<div class="vrat-home-grid" id="vrat-home-grid"></div>\n${htmlBlock}`);

fs.writeFileSync('index.html', code, 'utf8');
console.log('Added fest-home-grid to index.html');
