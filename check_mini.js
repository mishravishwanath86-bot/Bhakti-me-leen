const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('glass-mini-player');
if (s !== -1) {
  console.log(html.substring(s - 200, s + 1000));
}
