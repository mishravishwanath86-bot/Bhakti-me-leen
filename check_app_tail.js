const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');
const lines = code.split('\n');

console.log("Lines 10420 to end:");
for (let i = Math.max(0, lines.length - 25); i < lines.length; i++) {
  console.log(`${i+1}: ${lines[i]}`);
}
