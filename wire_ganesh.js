const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');
code = code.replace(
  "name: 'गणेश चतुर्थी (Ganesha Chaturthi)',",
  "name: 'गणेश चतुर्थी (Ganesha Chaturthi)', page: 'page-ganeshchaturthi',"
);
fs.writeFileSync('app.js', code, 'utf8');
console.log('Wired Ganesha Chaturthi nav!');
