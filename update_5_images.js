const fs = require('fs');

// Update app.js - TOP10 list thumbnails
let code = fs.readFileSync('app.js', 'utf8');
code = code.replace("img: 'assets/top10_6.jpg'", "img: 'assets/festival_navratri.jpg'");
code = code.replace("img: 'assets/top10_7.jpg'", "img: 'assets/festival_ganesh.jpg'");
// Find Ram Navami, Janmashtami, Shivaratri entries
code = code.replace("img: 'assets/top10_8.jpg'", "img: 'assets/festival_ramnavami.jpg'");
code = code.replace("img: 'assets/top10_9.jpg'", "img: 'assets/festival_janmashtami.jpg'");
code = code.replace("img: 'assets/top10_10.jpg'", "img: 'assets/festival_shivaratri.jpg'");
fs.writeFileSync('app.js', code, 'utf8');

// Update index.html - hero images inside detail pages
let html = fs.readFileSync('index.html', 'utf8');
html = html.replace(
  /<img src="[^"]*" alt="Navratri"[^>]*>/,
  '<img src="assets/festival_navratri.jpg" alt="Navratri" style="width:100%; height:220px; object-fit:cover;">'
);
html = html.replace(
  /<img src="[^"]*" alt="Ganesha Chaturthi"[^>]*>/,
  '<img src="assets/festival_ganesh.jpg" alt="Ganesha Chaturthi" style="width:100%; height:220px; object-fit:cover;">'
);
html = html.replace(
  /<img src="[^"]*" alt="Ram Navami"[^>]*>/,
  '<img src="assets/festival_ramnavami.jpg" alt="Ram Navami" style="width:100%; height:220px; object-fit:cover;">'
);
html = html.replace(
  /<img src="[^"]*" alt="Janmashtami"[^>]*>/,
  '<img src="assets/festival_janmashtami.jpg" alt="Janmashtami" style="width:100%; height:220px; object-fit:cover;">'
);
html = html.replace(
  /<img src="[^"]*" alt="Maha Shivaratri"[^>]*>/,
  '<img src="assets/festival_shivaratri.jpg" alt="Maha Shivaratri" style="width:100%; height:220px; object-fit:cover;">'
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Updated all 5 festival images in TOP10 list + detail pages!');
