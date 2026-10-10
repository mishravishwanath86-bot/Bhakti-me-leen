const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');
if(html.includes('Other Languages')) {
  console.log('Successfully added other languages!');
} else {
  console.log('Failed. Printing snippet:');
  const idx = html.indexOf('setting-row');
  console.log(html.substring(idx + 300, idx + 600));
}
