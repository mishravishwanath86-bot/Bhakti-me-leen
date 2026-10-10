const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Update Holi links to open the new in-app Holi page instead
// Replace onclick for Holi in TOP10_FESTIVALS
code = code.replace(
  "name: 'होली (Holi)',",
  "name: 'होली (Holi)', page: 'page-holi',"
);

// Also update the initTop10Page card click to use showPage if a page property exists
const oldCardHtml = `        return \`
      <div class="sk-date-card" style="display:flex; flex-direction:column; padding: 0.8rem; border-radius: 16px;" \${(f.links && f.links.length > 0) ? \`onclick="window.location.href='\${f.links[0].url}'"\` : ''}>`;
const newCardHtml = `        return \`
      <div class="sk-date-card" style="display:flex; flex-direction:column; padding: 0.8rem; border-radius: 16px; cursor:pointer;" onclick="\${f.page ? \`showPage('\${f.page}')\` : (f.links && f.links.length > 0 ? \`window.location.href='\${f.links[0].url}'\` : '')}">`;

code = code.replace(oldCardHtml, newCardHtml);

fs.writeFileSync('app.js', code, 'utf8');
console.log('Updated Holi card to navigate to in-app page!');
