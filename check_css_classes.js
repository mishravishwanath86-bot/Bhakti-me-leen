const fs = require('fs');
const css = fs.readFileSync('styles.css', 'utf8');

const checkClasses = [
  '.today-panchang-card',
  '.tpc-header',
  '.tpc-badge',
  '.category-grid',
  '.cat-card',
  '.sadhana-hub-container',
  '.sadhana-header',
  '.weekly-day-strip',
  '.day-dot'
];

for (let c of checkClasses) {
  console.log(`${c} in styles.css:`, css.includes(c));
}
