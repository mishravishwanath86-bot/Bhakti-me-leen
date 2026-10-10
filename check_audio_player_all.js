const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const matches = [];
const lines = code.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('Audio(') || line.includes('.play(') || line.includes('function play')) {
    matches.push(`${idx+1}: ${line}`);
  }
});
console.log(matches.slice(0, 30).join('\n'));
