const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const regex = /<div class="sk-date-card" style="(display:flex; flex-direction:column; padding: 0\.8rem; border-radius: 16px;)">/g;

code = code.replace(regex, (match, p1) => {
    return `<div class="sk-date-card" style="${p1}" \${(f.links && f.links.length > 0) ? \`onclick="window.location.href='\${f.links[0].url}'"\` : ''}>`;
});

fs.writeFileSync('app.js', code, 'utf8');
console.log('Added onclick to the whole card!');
