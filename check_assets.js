const fs = require('fs');
const files = fs.readdirSync('assets');
console.log("Assets images:", files.filter(f => f.endsWith('.jpg') || f.endsWith('.png') || f.endsWith('.svg')));
