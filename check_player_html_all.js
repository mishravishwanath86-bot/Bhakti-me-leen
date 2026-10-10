const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const matches = [];
const lines = html.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('player') || line.includes('audio') || line.includes('track')) {
    matches.push(`${idx+1}: ${line}`);
  }
});
console.log(matches.slice(0, 30).join('\n'));
