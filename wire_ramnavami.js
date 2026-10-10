const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');
code = code.replace(
  "name: 'राम नवमी (Rama Navami)',",
  "name: 'राम नवमी (Rama Navami)', page: 'page-ramnavami',"
);
code = code.replace(/^\/\/ v\d+\n/, '');
code = '// v' + Date.now() + '\n' + code;
fs.writeFileSync('app.js', code, 'utf8');
console.log('Wired Ram Navami nav!');
