const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');
const lines = code.split('\n');

for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes('const SANKASHTI_DATES_2026 =') || lines[i].includes('const HINDU_VRATS =')) {
    console.log(`Line ${i+1}: ${lines[i]}`);
  }
}
