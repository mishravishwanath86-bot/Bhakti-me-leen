const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('id="glass-mini-player"');
if (s !== -1) {
  console.log(html.substring(s, s + 1000));
}
