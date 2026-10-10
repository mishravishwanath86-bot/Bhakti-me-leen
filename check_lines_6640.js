const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');
const lines = code.split('\n');

console.log("Lines 6640 to 6670:");
for (let i = 6639; i < 6670; i++) {
  console.log(`${i+1}: ${lines[i]}`);
}
