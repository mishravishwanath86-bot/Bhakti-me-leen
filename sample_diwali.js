const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('id="page-diwali"');
const e = html.indexOf('</section>', s);
console.log("=== page-diwali content sample ===");
console.log(html.substring(s, s + 1500));
