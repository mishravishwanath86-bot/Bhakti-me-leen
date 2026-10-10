const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');
const lines = code.split('\n');

console.log("Lines 6670 to 6700:");
for (let i = 6669; i < 6700; i++) {
  console.log(`${i+1}: ${lines[i]}`);
}
