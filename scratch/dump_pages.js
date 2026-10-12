const fs = require('fs');
const s = fs.readFileSync('index.html', 'utf8');
const m = s.match(/id=["']page-[a-z0-9_-]+["']/g);
console.log('Unique Pages:', [...new Set(m)]);
