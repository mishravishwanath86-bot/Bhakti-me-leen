const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const regex = /id="(page-[a-z0-9-]+)"/g;
let m;
while((m = regex.exec(html)) !== null) {
  console.log(m[1]);
}
