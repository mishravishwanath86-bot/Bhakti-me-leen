const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// 1. Find the calendar page section and add tabs
// Find page-calendar section
const calStart = html.indexOf('id="page-calendar"');
if(calStart < 0) {
  console.log('page-calendar NOT FOUND - searching...');
  const alt = html.indexOf('page-calendar');
  console.log('Found at:', alt);
} else {
  console.log('page-calendar found at:', calStart);
  // Check existing page header
  const pageEnd = html.indexOf('</section>', calStart);
  console.log('Section ends at:', pageEnd);
  const snippet = html.substring(calStart, calStart + 500);
  console.log('Snippet:', snippet.replace(/</g,'[').replace(/>/g,']'));
}
