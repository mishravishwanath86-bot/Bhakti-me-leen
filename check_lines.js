const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');
const lines = code.split('\n');

console.log("Lines 5845 to 5870:");
for (let i = 5844; i < 5870; i++) {
  console.log(`${i+1}: ${lines[i]}`);
}
