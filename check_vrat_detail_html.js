const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('id="page-vrat-detail"');
if (s !== -1) {
  console.log(html.substring(s - 100, s + 1000));
}
