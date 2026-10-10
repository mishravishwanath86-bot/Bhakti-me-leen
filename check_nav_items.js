const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('<nav class="bottom-nav">');
if (s !== -1) {
  console.log(html.substring(s, s + 800));
}
