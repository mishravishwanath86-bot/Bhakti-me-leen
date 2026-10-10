const fs = require('fs');
const css = fs.readFileSync('styles.css', 'utf8');

const matches = [];
const lines = css.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('glass-full-player') || line.includes('glass-modal-img') || line.includes('rotate') || line.includes('spin')) {
    matches.push(`${idx+1}: ${line}`);
  }
});
console.log(matches.slice(0, 30).join('\n'));
