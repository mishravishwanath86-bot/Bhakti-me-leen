const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('id="glass-full-player-modal"');
if (s !== -1) {
  const e = html.indexOf('</div>\n  </div>', s);
  console.log(html.substring(s, s + 2200));
}
