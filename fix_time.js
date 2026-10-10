const fs = require('fs');
let css = fs.readFileSync('styles.css', 'utf8');

css = css.replace(
  '#mini-time {\n  font-size: 0.7rem !important;\n  color: #6b7280 !important;\n  font-weight: 600 !important;\n  margin-right: 5px !important;\n  display: none !important; /* Hide time to exactly match reference UI, we can add a circular progress ring later if needed */\n}',
  `#mini-time {
  font-size: 0.65rem !important;
  color: #6b7280 !important;
  font-weight: 700 !important;
  margin-right: 8px !important;
  display: block !important;
  background: rgba(255,255,255,0.4) !important;
  padding: 4px 8px !important;
  border-radius: 12px !important;
}`
);

fs.writeFileSync('styles.css', css);
console.log('Restored time display with pill style');
