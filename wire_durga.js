const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');
code = code.replace(
  "name: 'दुर्गा पूजा (Durga Puja)',",
  "name: 'दुर्गा पूजा (Durga Puja)', page: 'page-durgapuja',"
);
fs.writeFileSync('app.js', code, 'utf8');
console.log('Wired Durga Puja nav!');
