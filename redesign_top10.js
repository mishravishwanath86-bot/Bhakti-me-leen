const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const newTop10DataAndRender = `
const TOP10_FESTIVALS = [
  { 
    nameEng: 'Diwali', nameHi: 'दीपावली', img: 'assets/top10_1.jpg',
    links: [{ text: 'About Diwali', url: 'https://www.Sanatan Panchang.com/diwali/info/diwali.html' }, { text: 'Deepavali Muhurat', url: 'https://www.Sanatan Panchang.com/festivals/lakshmipuja/festivals-lakshmipuja-timings.html' }, { text: 'Deepavali Summary', url: 'https://www.Sanatan Panchang.com/hindu-festivals/diwali/diwali.html' }]
  },
  { 
    nameEng: 'Holi', nameHi: 'होली', img: 'assets/top10_2.jpg',
    links: [{ text: 'About Holi', url: '#' }, { text: 'Holika Muhurat', url: '#' }, { text: 'Holi Summary', url: '#' }, { text: 'Holika Dahan Summary', url: '#' }]
  },
  { 
    nameEng: 'Rakhi', nameHi: 'रक्षा बंधन', img: 'assets/top10_3.jpg',
    links: [{ text: 'About Rakhi', url: '#' }, { text: 'Rakhi Muhurat', url: '#' }, { text: 'Raksha Bandhan Summary', url: '#' }]
  },
  { 
    nameEng: 'Dussehra', nameHi: 'दशहरा', img: 'assets/top10_4.jpg',
    links: [{ text: 'About Dussehra', url: '#' }, { text: 'Dussehra Muhurat', url: '#' }, { text: 'Vijayadashmi Summary', url: '#' }]
  },
  { 
    nameEng: 'Durga Puja', nameHi: 'दुर्गा पूजा', img: 'assets/top10_5.jpg',
    links: [{ text: 'About Durga Puja', url: '#' }, { text: 'Sandhi Puja Muhurat', url: '#' }, { text: 'Durga Puja Summary', url: '#' }]
  },
  { 
    nameEng: 'Navratri', nameHi: 'नवरात्रि', img: 'assets/top10_6.jpg',
    links: [{ text: 'About Navratri', url: '#' }, { text: 'Navami Homa Muhurat', url: '#' }, { text: 'Navratri Summary', url: '#' }]
  },
  { 
    nameEng: 'Ganesha Chaturthi', nameHi: 'गणेश चतुर्थी', img: 'assets/top10_7.jpg',
    links: [{ text: 'About Ganesha Chaturthi', url: '#' }, { text: 'Chaturthi Muhurat', url: '#' }, { text: 'Ganesha Chaturthi Summary', url: '#' }]
  },
  { 
    nameEng: 'Rama Navami', nameHi: 'राम नवमी', img: 'assets/top10_8.jpg',
    links: [{ text: 'About Rama Navami', url: '#' }, { text: 'Rama Navami Muhurat', url: '#' }, { text: 'Rama Navami Summary', url: '#' }]
  },
  { 
    nameEng: 'Janmashtami', nameHi: 'जन्माष्टमी', img: 'assets/top10_9.jpg',
    links: [{ text: 'About Janmashtami', url: '#' }, { text: 'Janmashtami Muhurat', url: '#' }, { text: 'Janmashtami Summary', url: '#' }]
  },
  { 
    nameEng: 'Maha Shivaratri', nameHi: 'महा शिवरात्रि', img: 'assets/top10_10.jpg',
    links: [{ text: 'About Maha Shivaratri', url: '#' }, { text: 'Maha Shivaratri Muhurat', url: '#' }, { text: 'Maha Shivaratri Summary', url: '#' }]
  },
  { 
    nameEng: 'Makar Sankranti', nameHi: 'मकर संक्रांति', img: 'assets/top10_11.jpg',
    links: [{ text: 'About Makar Sankranti', url: '#' }, { text: 'Makar Sankranti Muhurat', url: '#' }, { text: 'Makar Sankranti Summary', url: '#' }]
  }
];

function initTop10Page() {
  const container = document.getElementById('top10-list-container');
  if(!container) return;
  
  // Make it a grid for nice layout
  container.style.display = 'grid';
  container.style.gridTemplateColumns = 'repeat(auto-fill, minmax(280px, 1fr))';
  container.style.gap = '1.2rem';
  container.style.padding = '1rem';
  
  container.innerHTML = TOP10_FESTIVALS.map((f, i) => {
    let linksHtml = '';
    if (f.links && f.links.length > 0) {
      linksHtml = '<div style="padding: 12px 16px; display:flex; flex-direction:column; gap:10px;">' +
        f.links.map(l => \`<a href="\${l.url}" target="_blank" style="color:#780000; font-size:15px; text-decoration:underline; font-family:sans-serif; cursor:pointer;">\${l.text}</a>\`).join('') +
        '</div>';
    }
    
    // Facebook icon (CSS square) to perfectly match Sanatan Panchang
    const fbIcon = \`<div style="width: 22px; height: 22px; background-color: #3b5998; color: white; border-radius: 2px; display:flex; align-items:flex-end; justify-content:center; font-weight:bold; font-size:18px; font-family:serif; line-height:1.2;">f</div>\`;
    
    return \`
      <div style="background-color: #f7ce95; border-radius: 4px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.15); display:flex; flex-direction:column; position:relative; border: 1px solid #dcb57e;">
         
         <div style="position:relative;">
           <img src="\${f.img}" style="width:100%; height:180px; object-fit:cover; display:block;">
           <div style="position:absolute; top:12px; left:12px; background-color:#a50000; color:white; width:40px; height:40px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:18px; box-shadow: 0 2px 4px rgba(0,0,0,0.3);">
             \${f.nameEng === 'Navratri' ? '5.2' : (f.nameEng === 'Durga Puja' ? '5.1' : (i > 5 ? i : i+1))}
           </div>
         </div>
         
         <div style="background-color: #f3c27e; padding: 10px 16px; display:flex; align-items:center; justify-content:space-between; border-bottom: 1px solid rgba(0,0,0,0.05);">
           <div style="font-size:18px; font-family:sans-serif; color:#a50000;">\${f.nameEng}</div>
           <div>\${fbIcon}</div>
         </div>
         
         \${linksHtml}
         
      </div>
    \`;
  }).join('');
}
`;

// Replace everything from const TOP10_FESTIVALS = [ to the end of initTop10Page()
const rx = /const TOP10_FESTIVALS = \[\s*\{[\s\S]*?\}\s*\];[\s\S]*?function initTop10Page\(\) \{[\s\S]*?\n\}/;
code = code.replace(rx, newTop10DataAndRender.trim());

fs.writeFileSync('app.js', code, 'utf8');
console.log('Completely redesigned Top 10 to match Sanatan Panchang perfectly!');
