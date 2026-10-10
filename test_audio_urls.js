const https = require('https');

const urls = [
  'https://ia800208.us.archive.org/21/items/ShreeHanumanChalisa_201602/Shree%20Hanuman%20Chalisa.mp3',
  'https://ia800904.us.archive.org/16/items/GayatriMantra108Times/GayatriMantra108Times.mp3',
  'https://ia800301.us.archive.org/15/items/MahaMrityunjayaMantra108Times/MahaMrityunjayaMantra108Times.mp3',
  'https://ia800100.us.archive.org/10/items/VishnuSahasranamam_201703/VishnuSahasranamam.mp3',
  'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3',
  'https://cdn.freesound.org/previews/515/515622_10842971-lq.mp3'
];

urls.forEach(u => {
  const req = https.request(u, { method: 'HEAD' }, res => {
    console.log(res.statusCode, u);
  });
  req.on('error', e => console.log('ERR', u, e.message));
  req.end();
});
