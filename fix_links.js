const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Replace target="_blank" with target="_self" or just remove it.
// Also add some padding and background to make them look like buttons!
const oldStr = 'f.links.map(l => `<a href="${l.url}" target="_blank" style="color:var(--maroon); font-size:0.9rem; text-decoration:none; font-weight:600; display:flex; align-items:center; gap:0.5rem;">🔗 ${l.text}</a>`).join(\'\') +';
const newStr = 'f.links.map(l => `<a href="${l.url}" style="color:#fff; background-color:var(--maroon); padding:0.6rem 1rem; border-radius:8px; font-size:0.95rem; text-decoration:none; font-weight:bold; display:flex; align-items:center; justify-content:center; gap:0.5rem; text-align:center;">🔗 ${l.text}</a>`).join(\'\') +';

code = code.replace(oldStr, newStr);

fs.writeFileSync('app.js', code, 'utf8');
console.log('Updated links to be large buttons and removed target_blank!');
