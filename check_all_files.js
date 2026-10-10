const fs = require('fs');
['service-worker.js', 'index.html', 'styles.css'].forEach(fn => {
  const c = fs.readFileSync(fn, 'utf8');
  if (c.includes('.wav') || c.includes('.webm')) {
    console.log(`Found in ${fn}`);
  } else {
    console.log(`Clean: ${fn}`);
  }
});
