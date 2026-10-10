const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Rebuild initTop10Page WITHOUT linksHtml - just clean cards, click goes to in-app page
const newInitTop10 = `function initTop10Page() {
  const container = document.getElementById('top10-list-container');
  if(!container) return;
  
  container.style.display = 'flex';
  container.style.flexDirection = 'column';
  container.style.gap = '0';
  container.style.padding = '0';
  
  container.innerHTML = TOP10_FESTIVALS.map((f, i) => {
    let clickAction = '';
    if(f.page) {
      clickAction = \`showPage('\${f.page}')\`;
    }
    
    return \`
      <div style="cursor:pointer; border-bottom: 1px solid #f0e6d3;" onclick="\${clickAction}">
         <img src="\${f.img}" style="width:100%; height:180px; object-fit:cover; display:block;">
         <div style="display:flex; align-items:center; gap: 0.8rem; padding: 0.9rem 1rem;">
           <div style="background:var(--saffron); color:#fff; width:32px; height:32px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:0.9rem; flex-shrink:0;">\${i+1}</div>
           <div style="flex:1;">
             <div class="sk-name" style="font-size:1.05rem; font-weight:800; color:var(--maroon);">\${f.name}</div>
             \${f.desc ? \`<div style="font-size:0.85rem; color:#475569;">\${f.desc}</div>\` : ''}
           </div>
           \${f.page ? '<div style="color:var(--saffron); font-size:1.2rem; font-weight:bold;">›</div>' : ''}
         </div>
      </div>
    \`;
  }).join('');
}`;

code = code.replace(/function initTop10Page\(\) \{[\s\S]*?\n\}/, newInitTop10);

fs.writeFileSync('app.js', code, 'utf8');
console.log('Rebuilt initTop10Page - no external links!');
