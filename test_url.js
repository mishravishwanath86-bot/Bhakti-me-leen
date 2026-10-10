const https = require('https');
const urls = [
  "https://upload.wikimedia.org/wikipedia/commons/d/dd/Bhagavad_Gita_Sloka_1.ogg",
  "https://upload.wikimedia.org/wikipedia/commons/4/4b/Gayatri_Mantra.ogg"
];
urls.forEach(u => {
  https.get(u, res => console.log(u + " => " + res.statusCode));
});
