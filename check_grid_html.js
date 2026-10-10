const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('हिन्दू त्यौहार (पर्व)');
if (s !== -1) {
  console.log(html.substring(s - 100, s + 2500));
}
