const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const pages = ['page-chalisa', 'page-mantra', 'page-aarti', 'page-bhajan'];
pages.forEach(p => {
  const s = html.indexOf(`id="${p}"`);
  if (s !== -1) {
    const e = html.indexOf('</section>', s);
    console.log(`=== ${p} ===`);
    console.log(html.substring(s, Math.min(s + 500, e)));
  }
});
