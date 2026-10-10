const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Replace hero images in each festival page
// Diwali
html = html.replace(
  /<img src="[^"]*" alt="Diwali"[^>]*>/,
  '<img src="assets/festival_diwali.jpg" alt="Diwali" style="width:100%; height:220px; object-fit:cover;">'
);

// Holi
html = html.replace(
  /<img src="[^"]*" alt="Holi"[^>]*>/,
  '<img src="assets/festival_holi.jpg" alt="Holi" style="width:100%; height:220px; object-fit:cover;">'
);

// Rakhi
html = html.replace(
  /<img src="[^"]*" alt="Raksha Bandhan"[^>]*>/,
  '<img src="assets/festival_rakhi.jpg" alt="Raksha Bandhan" style="width:100%; height:220px; object-fit:cover;">'
);

// Dussehra
html = html.replace(
  /<img src="[^"]*" alt="Dussehra"[^>]*>/,
  '<img src="assets/festival_dussehra.jpg" alt="Dussehra" style="width:100%; height:220px; object-fit:cover;">'
);

// Durga Puja
html = html.replace(
  /<img src="[^"]*" alt="Durga Puja"[^>]*>/,
  '<img src="assets/festival_durga.jpg" alt="Durga Puja" style="width:100%; height:220px; object-fit:cover;">'
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Updated all 5 festival hero images!');
