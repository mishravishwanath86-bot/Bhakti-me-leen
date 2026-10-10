const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const s = html.indexOf('id="page-home"');
const e = html.indexOf('</section>', s);
const homeContent = html.substring(s, e);

// Find all headings and grids on home page
const matches = homeContent.match(/<div[^>]*>[\s\S]*?<\/div>/g) || [];
console.log("Searching for vrat and festival sections on home page...");
const lines = homeContent.split('\n');
lines.forEach((l, i) => {
  if (l.includes('vrat') || l.includes('fest') || l.includes('व्रत') || l.includes('त्यौहार')) {
    console.log(`Line ${i+1}: ${l.trim()}`);
  }
});
