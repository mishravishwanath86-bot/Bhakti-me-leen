const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');

// 1. Add images to HINDU_VRATS
const vratImgs = [
  'vrat_img_0_0.jpg', 'vrat_img_0_1.jpg', 'vrat_img_0_2.jpg', 'vrat_img_0_3.jpg',
  'vrat_img_1_0.jpg', 'vrat_img_1_1.jpg', 'vrat_img_1_2.jpg', 'vrat_img_1_3.jpg',
  'vrat_img_2_0.jpg', 'vrat_img_2_1.jpg', 'vrat_img_2_2.jpg', 'vrat_img_2_3.jpg',
  'vrat_img_3_0.jpg', 'vrat_img_3_1.jpg', 'vrat_img_3_2.jpg', 'vrat_img_3_3.jpg',
  'vrat_img_4_0.jpg', 'vrat_img_4_1.jpg', 'vrat_img_4_2.jpg', 'vrat_img_4_3.jpg',
  'vrat_img_5_0.jpg', 'vrat_img_5_1.jpg', 'vrat_img_5_2.jpg', 'vrat_img_5_3.jpg',
  'vrat_img_6_1.jpg', 'vrat_img_6_2.jpg'
];

let match = code.match(/const HINDU_VRATS = \[([\s\S]*?)\];/);
if (match) {
  let lines = match[1].trim().split('\n');
  let newLines = lines.map((line, i) => {
     if (i < vratImgs.length) {
         // Insert img property before emoji or at the end
         if(line.includes('emoji:')) {
             return line.replace(/emoji:\s*'[^']+'/, `emoji: '', img: 'assets/${vratImgs[i]}?v=2'`);
         }
     }
     return line;
  });
  code = code.replace(match[0], `const HINDU_VRATS = [\n${newLines.join('\n')}\n];`);
}

// 2. Cache bust HINDU_FESTIVALS images
let fMatch = code.match(/const HINDU_FESTIVALS = \[([\s\S]*?)\];/);
if (fMatch) {
  let lines = fMatch[1].trim().split('\n');
  let newLines = lines.map(line => {
      return line.replace(/\.jpg'/, ".jpg?v=2'");
  });
  code = code.replace(fMatch[0], `const HINDU_FESTIVALS = [\n${newLines.join('\n')}\n];`);
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Fixed Vrat and Festival icons!');
