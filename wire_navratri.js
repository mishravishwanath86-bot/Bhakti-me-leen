const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');
code = code.replace(
  "name: 'नवरात्रि (Navratri)',",
  "name: 'नवरात्रि (Navratri)', page: 'page-navratri',"
);
fs.writeFileSync('app.js', code, 'utf8');
console.log('Wired Navratri nav!');
