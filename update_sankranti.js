const fs = require('fs');

// Update app.js - TOP10 list thumbnail
let code = fs.readFileSync('app.js', 'utf8');
code = code.replace("img: 'assets/top10_11.jpg'", "img: 'assets/festival_sankranti.jpg'");
fs.writeFileSync('app.js', code, 'utf8');

// Update index.html - hero image in Makar Sankranti detail page
let html = fs.readFileSync('index.html', 'utf8');
html = html.replace(
  /<img src="[^"]*" alt="Makar Sankranti"[^>]*>/,
  '<img src="assets/festival_sankranti.jpg" alt="Makar Sankranti" style="width:100%; height:220px; object-fit:cover;">'
);

// Cache bust
const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');

// Also bust app.js cache
code = code.replace(/^\/\/ v\d+\n/, '');
code = '// v' + Date.now() + '\n' + code;
fs.writeFileSync('app.js', code, 'utf8');

console.log('Makar Sankranti image updated on both sides!');
