const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const s = code.indexOf('const DEITIES');
if (s !== -1) {
  console.log(code.substring(s, s + 800));
} else {
  console.log("const DEITIES not found");
}
