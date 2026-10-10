const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');

const festArray = `
const HINDU_FESTIVALS = [
  { name: 'प्रमुख 10 पर्व', img: 'assets/fest_0_0.jpg' },
  { name: 'प्रमुख 20 पर्व', img: 'assets/fest_0_1.jpg' },
  { name: 'प्रमुख 25 पर्व', img: 'assets/fest_0_2.jpg' },
  { name: 'हिन्दू पर्व', img: 'assets/fest_0_3.jpg' },
  { name: 'तमिल पर्व', img: 'assets/fest_1_0.jpg' },
  { name: 'मलयालम पर्व', img: 'assets/fest_1_1.jpg' },
  { name: 'संक्रांति पर्व', img: 'assets/fest_1_2.jpg' },
  { name: 'गुरु एवं संत', img: 'assets/fest_1_3.jpg' },
  { name: 'चैत्र पर्व', img: 'assets/fest_2_0.jpg' },
  { name: 'वैशाख पर्व', img: 'assets/fest_2_1.jpg' },
  { name: 'ज्येष्ठ पर्व', img: 'assets/fest_2_2.jpg' },
  { name: 'आषाढ़ पर्व', img: 'assets/fest_2_3.jpg' },
  { name: 'श्रावण पर्व', img: 'assets/fest_3_0.jpg' },
  { name: 'भाद्रपद पर्व', img: 'assets/fest_3_1.jpg' },
  { name: 'आश्विन पर्व', img: 'assets/fest_3_2.jpg' },
  { name: 'कार्तिक पर्व', img: 'assets/fest_3_3.jpg' },
  { name: 'मार्गशीर्ष पर्व', img: 'assets/fest_4_0.jpg' },
  { name: 'पौष पर्व', img: 'assets/fest_4_1.jpg' },
  { name: 'माघ पर्व', img: 'assets/fest_4_2.jpg' },
  { name: 'फाल्गुन पर्व', img: 'assets/fest_4_3.jpg' }
];
`;

// Insert it after HINDU_VRATS
code = code.replace(/(const HINDU_VRATS = \[[\s\S]*?\];)/, `$1\n\n${festArray}`);

// Add rendering block in initHomePage
const renderBlock = `
  const fgrid = document.getElementById('fest-home-grid');
  if(fgrid) {
    fgrid.innerHTML = HINDU_FESTIVALS.map(f => {
      return \`<button class="vrat-card">
          <div style="padding:4px;">
            <img src="\${f.img}" class="vrat-icon-img" alt="\${f.name}">
          </div>
          <div class="vrat-name">\${f.name}</div>
        </button>\`;
    }).join('');
  }
`;

code = code.replace(/(const vgrid = document\.getElementById\('vrat-home-grid'\);[\s\S]*?\}\n)/, `$1\n${renderBlock}\n`);

fs.writeFileSync('app.js', code, 'utf8');
console.log('Added HINDU_FESTIVALS to app.js');
