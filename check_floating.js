const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const matches = [];
const lines = html.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('class="floating') || line.includes('mini-player') || line.includes('bottom-player') || line.includes('audio-bar')) {
    matches.push(`${idx+1}: ${line.trim()}`);
  }
});
console.log(matches.join('\n'));
