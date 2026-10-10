const fs = require('fs');
let css = fs.readFileSync('styles.css', 'utf8');

css = css.replace(
  'padding: 2px !important; /* Tiny gap inside the ring */',
  'padding: 3px !important; box-sizing: border-box !important;'
);

fs.writeFileSync('styles.css', css, 'utf8');
