const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');
const lines = code.split('\n');

for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes('const HINDU_VRATS =') || lines[i].includes('const HINDU_FESTIVALS =') || lines[i].includes('const TOP10_FESTIVALS =')) {
    console.log(`Line ${i+1}: ${lines[i]}`);
  }
}
