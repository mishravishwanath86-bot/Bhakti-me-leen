const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('id="onboarding-overlay"');
console.log(html.substring(s, s + 300));
