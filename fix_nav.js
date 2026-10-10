const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Fix the onclick handler for "Top 10 Hindu Festivals"
let festRender = `
  const fgrid = document.getElementById('fest-home-grid');
  if(fgrid) {
    fgrid.innerHTML = HINDU_FESTIVALS.map(f => {
      let pageAttr = '';
      if(f.name === 'प्रमुख 10 पर्व') pageAttr = 'onclick="initTop10Page(); showPage(\\'page-top10\\');"';
      return \`<div class="vrat-card" \${pageAttr}>
          <div style="padding:4px;">
            <img src="\${f.img}" class="vrat-icon-img" alt="\${f.name}">
          </div>
          <div class="vrat-name">\${f.name}</div>
        </div>\`;
    }).join('');
  }
`;

// Replace the buggy fgrid render block
// Since we used <button class="vrat-card"...> earlier, let's find that block.
code = code.replace(/const fgrid = document\.getElementById\('fest-home-grid'\);[\s\S]*?\}\n/, festRender + '\n');

fs.writeFileSync('app.js', code, 'utf8');
console.log('Fixed navigation in app.js');
