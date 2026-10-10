const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const pages = ['page-diwali', 'page-holi', 'page-rakhi', 'page-dussehra', 'page-durgapuja', 'page-navratri', 'page-ganeshchaturthi', 'page-ramnavami'];

pages.forEach(p => {
  const s = html.indexOf(`id="${p}"`);
  if (s !== -1) {
    const e = html.indexOf('</section>', s);
    const content = html.substring(s, e);
    // Find headings or section titles
    const headings = content.match(/<h[2345][^>]*>[\s\S]*?<\/h[2345]>/g);
    console.log(`=== ${p} ===`);
    console.log(headings ? headings.map(h => h.replace(/<[^>]+>/g, '').trim()).join(' | ') : 'No headings');
  }
});
