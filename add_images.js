const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Replace the render logic in initVratGrids
const renderOld = `<div class="vrat-icon">\${v.emoji}</div>`;
const renderNew = `\${v.img ? \`<img class="vrat-icon-img" src="\${v.img}">\` : \`<div class="vrat-icon">\${v.emoji}</div>\`}`;
code = code.replace(renderOld, renderNew);
code = code.replace(renderOld, renderNew); // Twice for both grids

// Update the arrays with the image paths
const vratsImages = [
  'vrat_img_0_0.jpg', 'vrat_img_0_1.jpg', 'vrat_img_0_2.jpg', 'vrat_img_0_3.jpg',
  'vrat_img_1_0.jpg', 'vrat_img_1_1.jpg', 'vrat_img_1_2.jpg', 'vrat_img_1_3.jpg',
  'vrat_img_2_0.jpg', 'vrat_img_2_1.jpg', 'vrat_img_2_2.jpg', 'vrat_img_2_3.jpg',
  'vrat_img_3_0.jpg', 'vrat_img_3_1.jpg', 'vrat_img_3_2.jpg', 'vrat_img_3_3.jpg',
  'vrat_img_4_0.jpg', 'vrat_img_4_1.jpg', 'vrat_img_4_2.jpg', 'vrat_img_4_3.jpg',
  'vrat_img_5_0.jpg', 'vrat_img_5_1.jpg', 'vrat_img_5_2.jpg', 'vrat_img_5_3.jpg',
  'vrat_img_6_1.jpg', 'vrat_img_6_2.jpg' // ISKCON & Masik
];

const specVratImages = [
  'vrat_img_7_0.jpg', 'vrat_img_7_1.jpg', 'vrat_img_7_2.jpg', 'vrat_img_7_3.jpg',
  'vrat_img_8_0.jpg', 'vrat_img_8_1.jpg', 'vrat_img_8_2.jpg', 'vrat_img_8_3.jpg'
];

let hinduMatch = code.match(/const HINDU_VRATS = \[([\s\S]*?)\];/);
if(hinduMatch) {
  let lines = hinduMatch[1].trim().split('\n');
  let newLines = lines.map((l, i) => {
    if(vratsImages[i]) {
      return l.replace(/emoji:\s*'[^']+'/, `img: 'assets/${vratsImages[i]}'`);
    }
    return l;
  });
  code = code.replace(hinduMatch[0], `const HINDU_VRATS = [\n${newLines.join('\n')}\n];`);
}

let specMatch = code.match(/const SPECIAL_VRATS = \[([\s\S]*?)\];/);
if(specMatch) {
  let lines = specMatch[1].trim().split('\n');
  let newLines = lines.map((l, i) => {
    if(specVratImages[i]) {
      return l.replace(/emoji:\s*'[^']+'/, `img: 'assets/${specVratImages[i]}'`);
    }
    return l;
  });
  code = code.replace(specMatch[0], `const SPECIAL_VRATS = [\n${newLines.join('\n')}\n];`);
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Images added to Vrats!');
