const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

// Check what reader data exists in app.js
const s = code.indexOf('const CONTENT');
if (s !== -1) {
  console.log(code.substring(s, s + 1000));
} else {
  console.log("const CONTENT not found, checking chalisa_hanuman");
  const s2 = code.indexOf('chalisa_hanuman');
  if (s2 !== -1) {
    console.log(code.substring(s2 - 100, s2 + 600));
  } else {
    console.log("chalisa_hanuman not found");
  }
}
