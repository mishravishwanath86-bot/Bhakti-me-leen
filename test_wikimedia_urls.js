const https = require('https');

const urls = [
  'https://upload.wikimedia.org/wikipedia/commons/4/4b/Gayatri_Mantra.ogg',
  'https://upload.wikimedia.org/wikipedia/commons/b/b5/Om_chanting_sound.ogg',
  'https://upload.wikimedia.org/wikipedia/commons/d/df/Tanpura_in_C_sharp.ogg',
  'https://archive.org/download/ShreeHanumanChalisa_201602/Shree%20Hanuman%20Chalisa.mp3',
  'https://archive.org/download/GayatriMantra_201703/GayatriMantra.mp3',
  'https://archive.org/download/MahamrityunjayMantra108Times/MahamrityunjayMantra108Times.mp3',
  'https://archive.org/download/BhagavadGitaInHindiAudio/01_Chapter_01.mp3'
];

urls.forEach(u => {
  const req = https.request(u, { method: 'HEAD', headers: { 'User-Agent': 'Mozilla/5.0' } }, res => {
    console.log(res.statusCode, u);
  });
  req.on('error', e => console.log('ERR', u, e.message));
  req.end();
});
