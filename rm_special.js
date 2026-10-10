const fs = require('fs');

let code = fs.readFileSync('index.html', 'utf8');

// Find the block corresponding to Special Vrats
// It looks like:
// <div class="home-section-row" style="margin-top:1.5rem">
//   <span class="home-section-title" style="color:var(--saffron); text-align:center; width:100%;">विशेष व्रत</span>
// </div>
// <div class="vrat-home-grid" id="special-vrat-grid"></div>

// Instead of matching unicode exactly, we match the id
let rx = /<div class="home-section-row"[^>]*>[\s\S]*?<span class="home-section-title"[^>]*>[^<]*<\/span>[\s\S]*?<\/div>[\s\S]*?<div class="vrat-home-grid" id="special-vrat-grid"><\/div>/;

code = code.replace(rx, '');

fs.writeFileSync('index.html', code, 'utf8');
console.log('Removed Special Vrats grid from HTML!');
