const fs = require('fs');
let css = fs.readFileSync('styles.css', 'utf8');

// Ensure justify-content: center is added to the wrapper
css = css.replace(
  'align-items: center;\n  transition: all 0.3s ease;',
  'align-items: center;\n  justify-content: center;\n  margin-bottom: 0.8rem;\n  transition: all 0.3s ease;'
);

// Also remove margin-bottom from .vrat-icon
css = css.replace(
  '.vrat-icon {\n  font-size: 2.2rem;\n  margin-bottom: 0.5rem;',
  '.vrat-icon {\n  font-size: 2.2rem;\n  margin-bottom: 0;'
);

// We should also look at app.js to ensure the HTML structure is matching our CSS.
let js = fs.readFileSync('app.js', 'utf8');
// In app.js:
// <div style="padding:4px;">
//   ${v.img ? `<img class="vrat-icon-img" src="${v.img}">` : `<div class="vrat-icon">${v.emoji}</div>`}
// </div>
// The wrapper is `<div style="padding:4px;">`. But the CSS targets `.vrat-card > div:first-child`.
// The inline style `padding:4px;` might conflict with the padding in CSS.
// Let's replace it with a class.
js = js.replace(/<div style="padding:4px;">/g, '<div class="vrat-icon-wrapper">');

fs.writeFileSync('app.js', js, 'utf8');
fs.writeFileSync('styles.css', css, 'utf8');
console.log("Replaced wrapper and updated CSS.");
