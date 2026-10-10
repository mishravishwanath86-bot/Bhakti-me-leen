const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Replace assets/sk_img_\d+.jpg with assets/deity_ganesh.jpg
code = code.replace(/assets\/sk_img_\d+\.jpg/g, 'assets/deity_ganesh.jpg');

fs.writeFileSync('app.js', code, 'utf8');
console.log('Fixed Sankashti images');
