const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Remove the OLD second initTop10Page function (lines 7070-7087 approx)
// Find both and keep only one clean version
const newInitTop10 = `function initTop10Page() {
  const container = document.getElementById('top10-list-container');
  if(!container) return;
  
  container.style.display = 'flex';
  container.style.flexDirection = 'column';
  container.style.gap = '1.2rem';
  container.style.padding = '0';
  
  container.innerHTML = TOP10_FESTIVALS.map((f, i) => {
    // Determine click action - page property = navigate in-app, else go to first link
    let clickAction = '';
    if(f.page) {
      clickAction = \`showPage('\${f.page}')\`;
    } else if(f.links && f.links.length > 0 && f.links[0].url !== '#') {
      clickAction = \`window.open('\${f.links[0].url}')\`;
    }
    
    let linksHtml = '';
    if (f.links && f.links.length > 0) {
      const visibleLinks = f.links.filter(l => l.url !== '#');
      if(visibleLinks.length > 0) {
        linksHtml = '<div style="margin-top:0.8rem; padding-top:0.8rem; border-top:1px solid #e2e8f0; display:flex; flex-direction:column; gap:0.5rem;">' +
          visibleLinks.map(l => \`<a href="\${l.url}" onclick="event.stopPropagation();" style="color:var(--maroon); font-size:0.9rem; text-decoration:none; font-weight:600; display:flex; align-items:center; gap:0.5rem;">🔗 \${l.text}</a>\`).join('') +
          '</div>';
      }
    }
    
    return \`
      <div class="sk-date-card" style="display:flex; flex-direction:column; padding: 0.8rem; border-radius: 16px; cursor:pointer;" onclick="\${clickAction}">
         <img src="\${f.img}" style="width:100%; height:160px; border-radius:12px; object-fit:cover; border:2px solid var(--saffron);">
         <div style="display:flex; align-items:flex-start; gap: 0.8rem; margin-top:0.8rem;">
           <div style="background:var(--saffron); color:#fff; width:30px; height:30px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold; flex-shrink:0;">\${i+1}</div>
           <div style="flex:1;">
             <div class="sk-name" style="font-size:1.2rem; font-weight:800; color:var(--maroon);">\${f.name}</div>
             <div class="sk-tithi" style="font-size:0.9rem; color:#475569; margin-bottom:0.5rem;">\${f.desc || ''}</div>
             \${linksHtml}
           </div>
         </div>
      </div>
    \`;
  }).join('');
}`;

// Remove ALL initTop10Page functions
code = code.replace(/function initTop10Page\(\) \{[\s\S]*?\n\}/g, '');

// Add ONE clean version just before the SANKASHTI_RELATED
code = code.replace('const SANKASHTI_RELATED = [', newInitTop10 + '\n\nconst SANKASHTI_RELATED = [');

fs.writeFileSync('app.js', code, 'utf8');
console.log('Rebuilt initTop10Page cleanly!');
