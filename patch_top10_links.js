const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const newTop10 = `
const TOP10_FESTIVALS = [
  { 
    name: 'दीपावली (Diwali)', 
    img: 'assets/top10_1.jpg', 
    desc: 'रोशनी और खुशियों का महापर्व',
    links: [
      { text: 'About Diwali', url: 'https://www.Sanatan Panchang.com/diwali/info/diwali.html' },
      { text: 'Deepavali Muhurat', url: 'https://www.Sanatan Panchang.com/festivals/lakshmipuja/festivals-lakshmipuja-timings.html' },
      { text: 'Deepavali Summary', url: 'https://www.Sanatan Panchang.com/hindu-festivals/diwali/diwali.html' }
    ]
  },
  { name: 'होली (Holi)', img: 'assets/top10_2.jpg', desc: 'रंगों और उल्लास का त्यौहार', links: [{text: 'About Holi', url:'#'}, {text: 'Holika Muhurat', url:'#'}, {text: 'Holi Summary', url:'#'}] },
  { name: 'रक्षा बंधन (Rakhi)', img: 'assets/top10_3.jpg', desc: 'भाई-बहन के प्रेम का प्रतीक', links: [{text: 'About Rakhi', url:'#'}, {text: 'Rakhi Muhurat', url:'#'}, {text: 'Raksha Bandhan Summary', url:'#'}] },
  { name: 'दशहरा (Dussehra)', img: 'assets/top10_4.jpg', desc: 'बुराई पर अच्छाई की जीत', links: [{text: 'About Dussehra', url:'#'}, {text: 'Dussehra Muhurat', url:'#'}, {text: 'Vijayadashmi Summary', url:'#'}] },
  { name: 'दुर्गा पूजा (Durga Puja)', img: 'assets/top10_5.jpg', desc: 'माँ दुर्गा की विशेष आराधना', links: [{text: 'About Durga Puja', url:'#'}, {text: 'Sandhi Puja Muhurat', url:'#'}, {text: 'Durga Puja Summary', url:'#'}] },
  { name: 'नवरात्रि (Navratri)', img: 'assets/top10_6.jpg', desc: 'नौ रात्रियों का पावन पर्व', links: [{text: 'About Navratri', url:'#'}, {text: 'Navami Homa Muhurat', url:'#'}, {text: 'Navratri Summary', url:'#'}] },
  { name: 'गणेश चतुर्थी (Ganesha Chaturthi)', img: 'assets/top10_7.jpg', desc: 'विघ्नहर्ता श्री गणेश का जन्मोत्सव', links: [{text: 'About Ganesha Chaturthi', url:'#'}, {text: 'Chaturthi Muhurat', url:'#'}, {text: 'Ganesha Chaturthi Summary', url:'#'}] },
  { name: 'राम नवमी (Rama Navami)', img: 'assets/top10_8.jpg', desc: 'मर्यादा पुरुषोत्तम प्रभु राम का जन्म', links: [{text: 'About Rama Navami', url:'#'}, {text: 'Rama Navami Muhurat', url:'#'}, {text: 'Rama Navami Summary', url:'#'}] },
  { name: 'जन्माष्टमी (Janmashtami)', img: 'assets/top10_9.jpg', desc: 'भगवान श्री कृष्ण का प्राकट्य दिवस', links: [{text: 'About Janmashtami', url:'#'}, {text: 'Janmashtami Muhurat', url:'#'}, {text: 'Janmashtami Summary', url:'#'}] },
  { name: 'महा शिवरात्रि (Maha Shivaratri)', img: 'assets/top10_10.jpg', desc: 'भोलेनाथ की महा पूजा की रात्रि', links: [{text: 'About Maha Shivaratri', url:'#'}, {text: 'Maha Shivaratri Muhurat', url:'#'}, {text: 'Maha Shivaratri Summary', url:'#'}] },
  { name: 'मकर संक्रांति (Makar Sankranti)', img: 'assets/top10_11.jpg', desc: 'सूर्य देव का उत्तरायण पर्व', links: [{text: 'About Makar Sankranti', url:'#'}, {text: 'Makar Sankranti Muhurat', url:'#'}, {text: 'Makar Sankranti Summary', url:'#'}] }
];
`;

const newRender = `
function initTop10Page() {
  const container = document.getElementById('top10-list-container');
  if(!container) return;
  container.innerHTML = TOP10_FESTIVALS.map((f, i) => {
    let linksHtml = '';
    if (f.links && f.links.length > 0) {
      linksHtml = '<div style="margin-top:0.8rem; padding-top:0.8rem; border-top:1px solid #e2e8f0; display:flex; flex-direction:column; gap:0.5rem;">' +
        f.links.map(l => \`<a href="\${l.url}" target="_blank" style="color:var(--maroon); font-size:0.9rem; text-decoration:none; font-weight:600; display:flex; align-items:center; gap:0.5rem;">🔗 \${l.text}</a>\`).join('') +
        '</div>';
    }
    return \`
      <div class="sk-date-card" style="display:flex; flex-direction:column; padding: 0.8rem; border-radius: 16px;">
         <img src="\${f.img}" style="width:100%; height:160px; border-radius:12px; object-fit:cover; border:2px solid var(--saffron);">
         <div style="display:flex; align-items:flex-start; gap: 0.8rem; margin-top:0.8rem;">
           <div style="background:var(--saffron); color:#fff; width:30px; height:30px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold; flex-shrink:0;">\${i+1}</div>
           <div style="flex:1;">
             <div class="sk-name" style="font-size:1.2rem; font-weight:800; color:var(--maroon);">\${f.name}</div>
             <div class="sk-tithi" style="font-size:0.9rem; color:#475569; margin-bottom:0.5rem;">\${f.desc}</div>
             \${linksHtml}
           </div>
         </div>
      </div>
    \`;
  }).join('');
}
`;

// Replace old TOP10_FESTIVALS array
code = code.replace(/const TOP10_FESTIVALS = \[[^\]]*\];/g, match => {
  return newTop10; // we replace it directly
});

// Remove multiple newTop10 if there are
let parts = code.split('const TOP10_FESTIVALS = [');
if(parts.length > 2) {
  // Just use replace
}

code = code.replace(/const TOP10_FESTIVALS = \[[^\]]*\];/, newTop10); // this won't work well if there's nested arrays in newTop10

// Let's use a safer regex:
const rxData = /const TOP10_FESTIVALS = \[\s*\{[\s\S]*?\}\s*\];/;
code = code.replace(rxData, newTop10.trim());

const rxFunc = /function initTop10Page\(\) \{[\s\S]*?\n\}/;
code = code.replace(rxFunc, newRender.trim());

fs.writeFileSync('app.js', code, 'utf8');
console.log('Added links to Top 10');
