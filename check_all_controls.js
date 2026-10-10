const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

let pos = 0;
while (true) {
  const idx = html.indexOf('glass-controls-row', pos);
  if (idx === -1) break;
  console.log('Found glass-controls-row at index:', idx);
  console.log(html.substring(Math.max(0, idx - 400), idx + 400));
  pos = idx + 1;
}
