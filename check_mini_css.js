const fs = require('fs');
const css = fs.readFileSync('styles.css', 'utf8');

const checkClasses = ['.glass-mini-controls', '.glass-mini-btn', '.glass-mini-player', '.glass-mini-play-btn'];
for (let c of checkClasses) {
  const s = css.indexOf(c);
  if (s !== -1) {
    console.log(`=== ${c} in styles.css ===`);
    console.log(css.substring(s, s + 500));
  }
}
