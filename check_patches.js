const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.js') && (f.startsWith('add_') || f.startsWith('patch_') || f.startsWith('wire_') || f.startsWith('update_') || f.startsWith('rebuild_') || f.startsWith('insert_')));

console.log("Found patch files:", files);
files.forEach(f => {
  const content = fs.readFileSync(f, 'utf8');
  console.log(`=== ${f} (${content.length} bytes) ===`);
  const lines = content.split('\n');
  console.log(lines.slice(0, 10).join('\n'));
});
