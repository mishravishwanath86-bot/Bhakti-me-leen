const fs = require('fs');

const files = ['patch_app_top10.js', 'patch_top10_links.js', 'rebuild_top10.js', 'clean_top10.js', 'add_vrats.js', 'add_vrats_7.js', 'add_vrats_8.js'];

files.forEach(f => {
  if (fs.existsSync(f)) {
    console.log(`\n===================== ${f} =====================`);
    console.log(fs.readFileSync(f, 'utf8'));
  }
});
