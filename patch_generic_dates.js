const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const oldRender = '`<div class="sk-date-card">\n           <div class="sk-date-left">\n             <div class="sk-month">${d.month}</div>\n             <div class="sk-day">${d.day}</div>\n             <div class="sk-weekday">${d.weekday}</div>\n           </div>\n           <div class="sk-date-right">\n             <div class="sk-name">${d.name}</div>\n             <div class="sk-tithi"><span class="moon-icon">🌖</span> ${d.tithi}</div>\n           </div>\n         </div>`';

const newRender = '`<div class="sk-date-card" style="display:flex; align-items:center; gap:0.8rem;">\n           <img src="${data.heroImg}" style="width:65px; height:65px; border-radius:12px; object-fit:cover; border:2px solid var(--saffron);">\n           <div class="sk-date-left" style="min-width:60px;">\n             <div class="sk-month">${d.month}</div>\n             <div class="sk-day" style="font-size:1.8rem;">${d.day}</div>\n             <div class="sk-weekday">${d.weekday}</div>\n           </div>\n           <div class="sk-date-right" style="flex:1;">\n             <div class="sk-name" style="font-size:1.05rem; font-weight:800; color:var(--maroon); margin-bottom:0.2rem;">${d.name}</div>\n             <div class="sk-tithi" style="font-size:0.85rem; color:#475569;">${d.tithi}</div>\n           </div>\n         </div>`';

code = code.replace(oldRender, newRender);

// Let's also check if Sankashti page hero image needs updating.
// The user might be referring to the hero image of the Sankashti page not matching the icon.
// Let's update index.html's Sankashti section to have id="sankashti-hero-img" and then update it dynamically or just set it manually to assets/vrat_img_0_1.jpg
fs.writeFileSync('app.js', code, 'utf8');
console.log("Updated generic dates to render images!");
