const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');
code = code.replace(
  "name: 'दशहरा (Dussehra)',",
  "name: 'दशहरा (Dussehra)', page: 'page-dussehra',"
);
fs.writeFileSync('app.js', code, 'utf8');
console.log('Wired Dussehra nav!');
