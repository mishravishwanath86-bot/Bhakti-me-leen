const fs = require('fs');
const css = fs.readFileSync('styles.css', 'utf8');
const lines = css.split('\n');

console.log('--- 5110 to 5140 ---');
console.log(lines.slice(5110, 5140).join('\n'));

console.log('--- 13095 to 13330 ---');
console.log(lines.slice(13095, 13330).join('\n'));
