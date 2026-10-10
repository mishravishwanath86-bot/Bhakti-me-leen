const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('id="page-vrats"');
if (s !== -1) {
  console.log(html.substring(s, s + 1200));
}
