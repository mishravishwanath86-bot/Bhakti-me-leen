const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const matches = [];
const lines = code.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('glass-mini-player') || line.includes('openGlassPlayer') || line.includes('mini-player')) {
    matches.push(`${idx+1}: ${line.trim()}`);
  }
});
console.log(matches.join('\n'));
