const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const matches = [];
const lines = code.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('http') && line.includes('.mp3')) {
    matches.push(`${idx+1}: ${line}`);
  }
});
console.log(matches.slice(0, 20).join('\n'));
