const http = require('http');

const urls = [
  'http://localhost:8000/',
  'http://localhost:8000/gita_engine.js',
  'http://localhost:8000/bhagavad_gita_chapters.json',
  'http://localhost:8000/assets/gallery/gita_upadesh_card.jpg'
];

let completed = 0;
urls.forEach(u => {
  http.get(u, (res) => {
    let size = 0;
    res.on('data', chunk => size += chunk.length);
    res.on('end', () => {
      console.log(`URL: ${u} => Status: ${res.statusCode}, Size: ${size} bytes`);
      if (res.statusCode !== 200) {
        console.error(`ERROR: Non-200 status for ${u}`);
        process.exit(1);
      }
      completed++;
      if (completed === urls.length) {
        console.log('ALL HTTP 200 CHECKS PASSED SUCCESSFULLY! ✨');
      }
    });
  }).on('error', err => {
    console.error(`ERROR fetching ${u}:`, err);
    process.exit(1);
  });
});
