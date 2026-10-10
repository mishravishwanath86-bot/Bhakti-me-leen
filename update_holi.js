const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// The block for Holi currently looks like:
// { text: 'About Holi', url: 'https://www.Sanatan Panchang.com/festivals/holi/holi-info.html' }
// Let's replace the links for Holi to match what they want. They said "ye होली (Holi) Dhulandi h"
// I will just add { text: 'होली (Holi) Dhulandi', url: 'https://www.Sanatan Panchang.com/festivals/holi/info/holi.html' } 
// to the Holi links.

code = code.replace(
  /name: 'होली \(Holi\)',[\s\S]*?links: \[([\s\S]*?)\]/,
  (match, p1) => {
    // If it already has it, don't duplicate
    if(p1.includes('Dhulandi')) return match;
    
    // Replace the inner links array with a newly constructed one
    return `name: 'होली (Holi)', 
    img: 'assets/top10_2.jpg', 
    desc: 'रंगों और उल्लास का त्यौहार', 
    links: [
      { text: 'होली (Holi) Dhulandi', url: 'https://www.Sanatan Panchang.com/festivals/holi/info/holi.html' },
      { text: 'About Holi', url: 'https://www.Sanatan Panchang.com/festivals/holi/holi-info.html' },
      { text: 'Holika Muhurat', url: 'https://www.Sanatan Panchang.com/festivals/holika/holika-dahan-timings.html' }
    ]`;
  }
);

fs.writeFileSync('app.js', code, 'utf8');
console.log('Updated Holi links!');
