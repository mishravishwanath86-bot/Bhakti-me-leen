const fs = require('fs');
let app = fs.readFileSync('app.js', 'utf8');

app = app.replace(
  "const timeDisp = document.getElementById('mini-sub'); // We will reuse the subtitle for time",
  "const timeDisp = document.getElementById('mini-time') || document.getElementById('mini-sub');"
);

fs.writeFileSync('app.js', app);
console.log("Updated timeDisp to use mini-time");
