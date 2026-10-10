const fs = require('fs');
const css = fs.readFileSync('styles.css', 'utf8');

const matches = [];
const lines = css.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('mini-player') || line.includes('glass-mini-player') || line.includes('floating')) {
    matches.push(`${idx+1}: ${line.trim()}`);
  }
});
console.log(matches.join('\n'));
