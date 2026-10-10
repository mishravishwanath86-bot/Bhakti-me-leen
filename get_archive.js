const https = require('https');
https.get('https://archive.org/advancedsearch.php?q=hanuman+chalisa&fl[]=identifier,title&rows=1&output=json', res => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => console.log(data));
});
