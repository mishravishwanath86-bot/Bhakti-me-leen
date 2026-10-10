const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('id="page-profile"');
const e = html.indexOf('</section>', s);
console.log(html.substring(s, e));
