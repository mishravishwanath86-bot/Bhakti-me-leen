const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');

const newData = `
const SANKASHTI_DATES_2026 = [
  { img: 'assets/sk_img_0.jpg', month: 'Jan', day: 6, weekday: 'Tue', name: 'सकट चौथ / लंबोदर संकष्टी', moonrise: '08:59 PM', tithi: 'माघ, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_1.jpg', month: 'Feb', day: 5, weekday: 'Thu', name: 'द्विजप्रिय संकष्टी', moonrise: '09:39 PM', tithi: 'फाल्गुन, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_2.jpg', month: 'Mar', day: 6, weekday: 'Fri', name: 'भालचंद्र संकष्टी', moonrise: '09:18 PM', tithi: 'चैत्र, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_3.jpg', month: 'Apr', day: 5, weekday: 'Sun', name: 'विकट संकष्टी', moonrise: '09:58 PM', tithi: 'वैशाख, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_4.jpg', month: 'May', day: 5, weekday: 'Tue', name: 'एकदन्त संकष्टी', moonrise: '10:35 PM', tithi: 'ज्येष्ठ, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_5.jpg', month: 'Jun', day: 3, weekday: 'Wed', name: 'विभुवन संकष्टी', moonrise: '10:04 PM', tithi: 'ज्येष्ठ (अधिक), कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_6.jpg', month: 'Jul', day: 3, weekday: 'Fri', name: 'कृष्णपिंगल संकष्टी', moonrise: '09:53 PM', tithi: 'आषाढ़, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_7.jpg', month: 'Aug', day: 2, weekday: 'Sun', name: 'गजानन संकष्टी', moonrise: '09:24 PM', tithi: 'श्रावण, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_8.jpg', month: 'Aug', day: 31, weekday: 'Mon', name: 'बहुला चतुर्थी / हेरम्ब संकष्टी', moonrise: '08:29 PM', tithi: 'भाद्रपद, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_9.jpg', month: 'Sep', day: 29, weekday: 'Tue', name: 'विघ्नराज संकष्टी', moonrise: '07:44 PM', tithi: 'आश्विन, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_10.jpg', month: 'Oct', day: 29, weekday: 'Thu', name: 'करवा चौथ / वक्रतुण्ड संकष्टी', moonrise: '08:17 PM', tithi: 'कार्तिक, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_11.jpg', month: 'Nov', day: 27, weekday: 'Fri', name: 'गणाधिप संकष्टी', moonrise: '08:18 PM', tithi: 'मार्गशीर्ष, कृष्ण चतुर्थी' },
  { img: 'assets/sk_img_12.jpg', month: 'Dec', day: 26, weekday: 'Sat', name: 'अखुरथ संकष्टी', moonrise: '08:19 PM', tithi: 'पौष, कृष्ण चतुर्थी' }
];
`;

const renderBlock = `
    datesWrap.innerHTML = SANKASHTI_DATES_2026.map(d => 
      \`<div class="sk-date-card" style="display:flex; align-items:center; gap:0.8rem;">
         <img src="\${d.img}" style="width:60px; height:60px; border-radius:8px; object-fit:cover; border:2px solid var(--saffron);">
         <div class="sk-date-left" style="min-width:60px;">
           <div class="sk-month">\${d.month}</div>
           <div class="sk-day">\${d.day}</div>
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

let rxArray = /const SANKASHTI_DATES_2026 = \[[^\]]+\];/;
code = code.replace(rxArray, newData.trim());

let rxRender = /datesWrap\.innerHTML = SANKASHTI_DATES_2026\.map\([\s\S]*?}\)/;
code = code.replace(rxRender, renderBlock.trim());

fs.writeFileSync('app.js', code, 'utf8');
console.log('Sankashti detailed UI updated!');
