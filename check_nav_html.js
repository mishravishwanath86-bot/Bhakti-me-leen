const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('<nav class="bottom-nav"');
if (s !== -1) {
  const e = html.indexOf('</nav>', s) + '</nav>'.length;
  console.log(html.substring(s, e));
}
