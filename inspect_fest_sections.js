const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

const pages = [
  'page-diwali', 'page-holi', 'page-rakhi', 'page-dussehra', 
  'page-durgapuja', 'page-navratri', 'page-ganeshchaturthi', 'page-ramnavami'
];

pages.forEach(p => {
  const s = html.indexOf(`id="${p}"`);
  if (s !== -1) {
    const e = html.indexOf('</section>', s);
    const content = html.substring(s, e);
    console.log(`\n=================== ${p} (${content.length} chars) ===================`);
    const divs = content.match(/<div class="sk-date-card"[^>]*>[\s\S]*?<\/div>/g) || [];
    divs.forEach(d => {
      const title = (d.match(/<div style="font-size:1\.1rem[^>]*>([\s\S]*?)<\/div>/) || 
                     d.match(/<strong[^>]*>([\s\S]*?)<\/strong>/) ||
                     d.match(/<h[34][^>]*>([\s\S]*?)<\/h[34]>/) || [])[1];
      if (title) {
        console.log(` - ${title.replace(/<[^>]+>/g, '').trim()}`);
      }
    });
  }
});
