const fs = require('fs');
console.log(fs.readFileSync('service-worker.js', 'utf8').substring(0, 800));
