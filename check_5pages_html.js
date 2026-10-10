const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const pages = ['page-settings', 'page-panchang', 'page-jar', 'page-katha', 'page-profile'];
for (let p of pages) {
  const s = html.indexOf(`id="${p}"`);
  if (s !== -1) {
    console.log(`=== FOUND ${p} ===`);
    console.log(html.substring(s, s + 400));
  }
}
