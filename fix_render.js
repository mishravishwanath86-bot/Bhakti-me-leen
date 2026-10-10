const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const renderOld = "    datesWrap.innerHTML = SANKASHTI_DATES_2026.map(d => \n      `<div class=\"sk-date-card\">\n         <div class=\"sk-date-left\">\n           <div class=\"sk-month\">${d.month}</div>\n           <div class=\"sk-day\">${d.day}</div>\n           <div class=\"sk-weekday\">${d.weekday}</div>\n         </div>\n         <div class=\"sk-date-right\">\n           <div class=\"sk-name\">${d.name}</div>\n           <div class=\"sk-tithi\"><span class=\"moon-icon\">🌖</span> ${d.tithi}</div>\n         </div>\n       </div>`\n    ).join('');";

const renderBlock = `
    datesWrap.innerHTML = SANKASHTI_DATES_2026.map(d => 
      \`<div class="sk-date-card" style="display:flex; align-items:center; gap:0.8rem;">
         <img src="\${d.img}" style="width:70px; height:70px; border-radius:12px; object-fit:cover; border:2px solid var(--saffron);">
         <div class="sk-date-left" style="min-width:60px;">
           <div class="sk-month">\${d.month}</div>
           <div class="sk-day" style="font-size:1.8rem;">\${d.day}</div>
           <div class="sk-weekday">\${d.weekday}</div>
         </div>
         <div class="sk-date-right" style="flex:1;">
           <div class="sk-name" style="font-size:1.05rem; font-weight:800; color:var(--maroon); margin-bottom:0.2rem;">\${d.name}</div>
           <div class="sk-tithi" style="font-size:0.85rem; color:#475569; margin-bottom:0.15rem;">\${d.tithi}</div>
           <div style="font-size:0.85rem; color:var(--saffron); font-weight:bold;">🌙 चंद्रोदय: \${d.moonrise}</div>
         </div>
       </div>\`
    ).join('');
`;

code = code.replace(renderOld, renderBlock.trim());
fs.writeFileSync('app.js', code, 'utf8');
console.log('Fixed render!');
