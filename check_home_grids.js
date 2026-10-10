const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('id="vrat-home-grid"');
if (s !== -1) {
  console.log(html.substring(s - 250, s + 400));
}
