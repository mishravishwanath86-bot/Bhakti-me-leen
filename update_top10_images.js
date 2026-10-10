const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Replace thumbnail images for TOP10 list items 1-5
code = code.replace("img: 'assets/top10_1.jpg'", "img: 'assets/festival_diwali.jpg'");
code = code.replace("img: 'assets/top10_2.jpg'", "img: 'assets/festival_holi.jpg'");
code = code.replace("img: 'assets/top10_3.jpg'", "img: 'assets/festival_rakhi.jpg'");
code = code.replace("img: 'assets/top10_4.jpg'", "img: 'assets/festival_dussehra.jpg'");
code = code.replace("img: 'assets/top10_5.jpg'", "img: 'assets/festival_durga.jpg'");

fs.writeFileSync('app.js', code, 'utf8');
console.log('Updated TOP10 list thumbnail images for all 5 festivals!');
