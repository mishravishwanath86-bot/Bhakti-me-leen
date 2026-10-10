const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');
let data = JSON.parse(fs.readFileSync('vrat_data_7.json', 'utf8'));

// Hardcode some fallbacks for 0 dates
if (data['navagraha'].length === 0) {
  data['navagraha'] = [
    {month: 'रवि', day: '☀️', weekday: 'Sun', name: 'सूर्य देव व्रत', tithi: 'रविवार'},
    {month: 'सोम', day: '🌙', weekday: 'Mon', name: 'चंद्र देव व्रत', tithi: 'सोमवार'},
    {month: 'मंगल', day: '🔥', weekday: 'Tue', name: 'मंगल देव व्रत', tithi: 'मंगलवार'},
    {month: 'बुध', day: '🌿', weekday: 'Wed', name: 'बुध देव व्रत', tithi: 'बुधवार'},
    {month: 'गुरु', day: '⭐', weekday: 'Thu', name: 'बृहस्पति देव व्रत', tithi: 'गुरुवार'},
    {month: 'शुक्र', day: '✨', weekday: 'Fri', name: 'शुक्र देव व्रत', tithi: 'शुक्रवार'},
    {month: 'शनि', day: '🪐', weekday: 'Sat', name: 'शनि देव व्रत', tithi: 'शनिवार'}
  ];
}
if (data['devi-devta'].length === 0) {
  data['devi-devta'] = [
    {month: 'रवि', day: '☀️', weekday: 'Sun', name: 'सूर्य देव / भैरव', tithi: 'रविवार'},
    {month: 'सोम', day: '🔱', weekday: 'Mon', name: 'भगवान शिव', tithi: 'सोमवार'},
    {month: 'मंगल', day: '🐒', weekday: 'Tue', name: 'हनुमान जी / कार्तिकेय', tithi: 'मंगलवार'},
    {month: 'बुध', day: '🐘', weekday: 'Wed', name: 'भगवान गणेश', tithi: 'बुधवार'},
    {month: 'गुरु', day: '📖', weekday: 'Thu', name: 'भगवान विष्णु / साईं बाबा', tithi: 'गुरुवार'},
    {month: 'शुक्र', day: '🌺', weekday: 'Fri', name: 'माता संतोषी / लक्ष्मी', tithi: 'शुक्रवार'},
    {month: 'शनि', day: '🪐', weekday: 'Sat', name: 'शनि देव / हनुमान जी', tithi: 'शनिवार'}
  ];
}
if (data['shraddha'].length === 0) {
  data['shraddha'] = [
    {month: 'Sep', day: '25', weekday: 'Fri', name: 'प्रतिपदा श्राद्ध', tithi: 'पितृ पक्ष प्रारंभ'},
    {month: 'Sep', day: '26', weekday: 'Sat', name: 'द्वितीया श्राद्ध', tithi: ''},
    {month: 'Sep', day: '27', weekday: 'Sun', name: 'तृतीया श्राद्ध', tithi: ''},
    {month: 'Oct', day: '10', weekday: 'Sat', name: 'सर्वपितृ अमावस्या', tithi: 'पितृ पक्ष समाप्त'}
  ];
}

for(let key of Object.keys(data)) {
    if(data[key].length > 0) {
        let datesArrayStr = JSON.stringify(data[key]);
        let regex = new RegExp(`('${key}':\\s*\\{[\\s\\S]*?dates:\\s*)\\[\\]`);
        code = code.replace(regex, `$1${datesArrayStr}`);
    } else {
        let placeholder = JSON.stringify([
           {month: 'N/A', day: '--', weekday: '', name: 'तिथियाँ उपलब्ध नहीं', tithi: ''}
        ]);
        let regex = new RegExp(`('${key}':\\s*\\{[\\s\\S]*?dates:\\s*)\\[\\]`);
        code = code.replace(regex, `$1${placeholder}`);
    }
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Injected dates for the 7 new vrats!');
