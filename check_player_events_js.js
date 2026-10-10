const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

const matches = [];
const lines = code.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('audioPlayerObj') || line.includes('ontimeupdate') || line.includes('updatePlayerUI')) {
    matches.push(`${idx+1}: ${line}`);
  }
});
console.log(matches.slice(0, 30).join('\n'));
