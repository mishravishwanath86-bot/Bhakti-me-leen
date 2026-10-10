const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('<!-- 🎵 MUSIC PLAYER SYSTEM 🎵 -->');
if (s !== -1) {
  console.log(html.substring(s, s + 2500));
} else {
  const s2 = html.indexOf('glass-controls-row');
  console.log(html.substring(Math.max(0, s2 - 500), s2 + 1500));
}
