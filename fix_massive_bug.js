const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const correctCode = `function initVratGrids() {
  const vgrid = document.getElementById('vrat-home-grid');
  if (vgrid) {
    vgrid.innerHTML = HINDU_VRATS.map(v => 
      \`<button class="vrat-card" onclick="if('\${v.isDynamic}' === 'true') openVratPage('\${v.page}'); else if('\${v.page}' !== 'undefined') showPage('\${v.page}');">
         <div style="padding:4px;">
           \${v.img ? \`<img class="vrat-icon-img" src="\${v.img}">\` : \`<div class="vrat-icon">\${v.emoji}</div>\`}
         </div>
         <div class="vrat-name">\${v.name}</div>
       </button>\`
    ).join('');
  }
  
  const fgrid = document.getElementById('fest-home-grid');
  if(fgrid) {
    fgrid.innerHTML = HINDU_FESTIVALS.map(f => {
      let pageAttr = '';
      if(f.name === 'प्रमुख 10 पर्व') pageAttr = 'onclick="initTop10Page(); showPage(\\'page-top10\\');"';
      return \`<button class="vrat-card" \${pageAttr}>
          <div style="padding:4px;">
            <img src="\${f.img}" class="vrat-icon-img" alt="\${f.name}">
          </div>
          <div class="vrat-name">\${f.name}</div>
        </button>\`;
    }).join('');
  }
}
`;

// Find start and end exactly!
const startIdx = code.indexOf('function initVratGrids() {');
const nextFuncIdx = code.indexOf('function initTop10Page() {'); // Top 10 comes right after!

if(startIdx > -1 && nextFuncIdx > -1) {
  code = code.substring(0, startIdx) + correctCode + '\n' + code.substring(nextFuncIdx);
  fs.writeFileSync('app.js', code, 'utf8');
  console.log("Successfully rebuilt initVratGrids!");
} else {
  console.log("Indices not found!", startIdx, nextFuncIdx);
}
