const fs = require('fs');
let code = fs.readFileSync('index.html', 'utf8');

// Replace the static sankashti hero image with the grid icon
code = code.replace(/<img src="assets\/sankashti_hero\.jpg" alt="Sankashti Hero">/, '<img src="assets/vrat_img_0_1.jpg" alt="Sankashti Hero" id="sankashti-hero-img">');

fs.writeFileSync('index.html', code, 'utf8');
console.log('Fixed sankashti hero in html');
