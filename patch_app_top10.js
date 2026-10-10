const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const top10Data = `
const TOP10_FESTIVALS = [
  { name: 'दीपावली (Diwali)', img: 'assets/top10_1.jpg', desc: 'रोशनी और खुशियों का महापर्व' },
  { name: 'होली (Holi)', img: 'assets/top10_2.jpg', desc: 'रंगों और उल्लास का त्यौहार' },
  { name: 'रक्षा बंधन (Rakhi)', img: 'assets/top10_3.jpg', desc: 'भाई-बहन के प्रेम का प्रतीक' },
  { name: 'दशहरा (Dussehra)', img: 'assets/top10_4.jpg', desc: 'बुराई पर अच्छाई की जीत' },
  { name: 'दुर्गा पूजा (Durga Puja)', img: 'assets/top10_5.jpg', desc: 'माँ दुर्गा की विशेष आराधना' },
  { name: 'नवरात्रि (Navratri)', img: 'assets/top10_6.jpg', desc: 'नौ रात्रियों का पावन पर्व' },
  { name: 'गणेश चतुर्थी (Ganesha Chaturthi)', img: 'assets/top10_7.jpg', desc: 'विघ्नहर्ता श्री गणेश का जन्मोत्सव' },
  { name: 'राम नवमी (Rama Navami)', img: 'assets/top10_8.jpg', desc: 'मर्यादा पुरुषोत्तम प्रभु राम का जन्म' },
  { name: 'जन्माष्टमी (Janmashtami)', img: 'assets/top10_9.jpg', desc: 'भगवान श्री कृष्ण का प्राकट्य दिवस' },
  { name: 'महा शिवरात्रि (Maha Shivaratri)', img: 'assets/top10_10.jpg', desc: 'भोलेनाथ की महा पूजा की रात्रि' },
  { name: 'मकर संक्रांति (Makar Sankranti)', img: 'assets/top10_11.jpg', desc: 'सूर्य देव का उत्तरायण पर्व' }
];

function initTop10Page() {
  const container = document.getElementById('top10-list-container');
  if(!container) return;
  container.innerHTML = TOP10_FESTIVALS.map((f, i) => {
    return \`
      <div class="sk-date-card" style="display:flex; flex-direction:column; gap:0.5rem; padding: 0.8rem; border-radius: 16px;">
         <img src="\${f.img}" style="width:100%; height:160px; border-radius:12px; object-fit:cover; border:2px solid var(--saffron);">
         <div style="display:flex; align-items:center; gap: 0.8rem; margin-top:0.5rem;">
           <div style="background:var(--saffron); color:#fff; width:30px; height:30px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">\${i+1}</div>
           <div style="flex:1;">
             <div class="sk-name" style="font-size:1.2rem; font-weight:800; color:var(--maroon);">\${f.name}</div>
             <div class="sk-tithi" style="font-size:0.9rem; color:#475569;">\${f.desc}</div>
           </div>
         </div>
      </div>
    \`;
  }).join('');
}
`;

// Insert after HINDU_FESTIVALS
code = code.replace(/const HINDU_FESTIVALS = \[[^\]]*\];/, match => match + '\n' + top10Data);

// Update initHomePage to route to top10
let festRender = `
  const fgrid = document.getElementById('fest-home-grid');
  if(fgrid) {
    fgrid.innerHTML = HINDU_FESTIVALS.map(f => {
      let pageAttr = '';
      if(f.name === 'प्रमुख 10 पर्व') pageAttr = 'data-page="page-top10" onclick="initTop10Page();"';
      return \`<button class="vrat-card" \${pageAttr}>
          <div style="padding:4px;">
            <img src="\${f.img}" class="vrat-icon-img" alt="\${f.name}">
          </div>
          <div class="vrat-name">\${f.name}</div>
        </button>\`;
    }).join('');
  }
`;

// Replace the previous fgrid render block
code = code.replace(/const fgrid = document\.getElementById\('fest-home-grid'\);[\s\S]*?\}\n/, festRender + '\n');

// Make sure clicks on fest-home-grid buttons also trigger navigation if they have data-page
// It's handled globally by data-page event listeners if they are buttons.
// The onclick="initTop10Page();" handles the rendering.
// Wait, global event listener for data-page checks closest('[data-page]'). It will work.

fs.writeFileSync('app.js', code, 'utf8');
console.log('Added Top10 logic to app.js');
