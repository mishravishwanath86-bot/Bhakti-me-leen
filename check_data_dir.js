const fs = require('fs');
if (fs.existsSync('data')) {
  console.log(fs.readdirSync('data'));
}
