const fs = require('fs');
const css = fs.readFileSync('styles.css', 'utf8');

const s = css.indexOf('.cat-card');
if (s !== -1) {
  console.log("=== Found .cat-card in styles.css ===");
  console.log(css.substring(s, s + 600));
}

const s2 = css.indexOf('.today-panchang');
if (s2 !== -1) {
  console.log("=== Found .today-panchang in styles.css ===");
  console.log(css.substring(s2, s2 + 600));
}
