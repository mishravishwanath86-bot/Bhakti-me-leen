const fs = require('fs');
const css = fs.readFileSync('styles.css', 'utf8');

const matches = [];
const lines = css.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('glass-full-player-modal')) {
    matches.push(`${idx+1}: ${line}`);
  }
});
console.log(matches.join('\n'));
