const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');
console.log('initTop10Page contains showPage:', code.includes("showPage('${f.page}')"));
console.log('initTop10Page contains target=_blank:', code.includes('target="_blank"'));
