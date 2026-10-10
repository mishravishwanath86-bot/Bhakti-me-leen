const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const prefix = code.split('\n').slice(0, 6836).join('\n');

const newData = `
const HINDU_VRATS = [
  { name: 'प्रमुख 10 व्रत', emoji: '🌟' },
  { name: 'संकष्टी चतुर्थी', emoji: '🐘', page: 'page-sankashti' },
  { name: 'एकादशी व्रत', emoji: '🌿' },
  { name: 'प्रदोष व्रत', emoji: '🌙' },
  { name: 'विनायक चतुर्थी', emoji: '🐘' },
  { name: 'द्वादशी तिथियाँ', emoji: '📿' },
  { name: 'महाद्वादशी', emoji: '🔱' },
  { name: 'मासिक शिवरात्रि', emoji: '🕉️' },
  { name: 'सावन सोमवार', emoji: '🌧️' },
  { name: 'श्री सत्यनारायण', emoji: '📖' },
  { name: 'पूर्णिमा व्रत', emoji: '🌕' },
  { name: 'नवग्रह उपवास', emoji: '🪐' },
  { name: 'देवी-देवता उपवास', emoji: '🙏' },
  { name: 'अमावस्या', emoji: '🌑' },
  { name: 'स्कंद षष्ठी', emoji: '🏹' },
  { name: 'कार्तिगाई', emoji: '🪔' },
  { name: 'श्राद्ध तिथियाँ', emoji: '🐦' },
  { name: 'दुर्गाष्टमी', emoji: '🦁' },
  { name: 'कालाष्टमी', emoji: '🐕' },
  { name: 'रोहिणी व्रत', emoji: '🌸' },
  { name: 'संक्रांति कैलेंडर', emoji: '🌞' },
  { name: 'चंद्र दर्शन', emoji: '🌛' },
  { name: 'मंगला गौरी', emoji: '🌺' },
  { name: 'इष्टि एवं अन्वाधान', emoji: '🔥' },
  { name: 'इस्कॉन एकादशी', emoji: '🦅' },
  { name: 'मासिक जन्माष्टमी', emoji: '🦚' }
];

const SPECIAL_VRATS = [
  { name: 'दशावतार व्रत', emoji: '🐍' },
  { name: 'पुरुषोत्तम मास', emoji: '🦅' },
  { name: 'चातुर्मास', emoji: '🌧️' },
  { name: 'अशोक अष्टमी', emoji: '🌳' },
  { name: 'आशा दशमी', emoji: '🕉️' },
  { name: 'दूर्वा अष्टमी', emoji: '🌿' },
  { name: 'जीवित्पुत्रिका व्रत', emoji: '👩‍👦' },
  { name: 'शीतला सप्तमी', emoji: '🫏' }
];

const SANKASHTI_DATES_2026 = [
  { month: 'Jan', day: 6, weekday: 'Tue', name: 'सकट चौथ / लंबोदर संकष्टी', tithi: 'माघ, कृष्ण चतुर्थी' },
  { month: 'Feb', day: 5, weekday: 'Thu', name: 'द्विजप्रिय संकष्टी', tithi: 'फाल्गुन, कृष्ण चतुर्थी' },
  { month: 'Mar', day: 6, weekday: 'Fri', name: 'भालचंद्र संकष्टी', tithi: 'चैत्र, कृष्ण चतुर्थी' },
  { month: 'Apr', day: 5, weekday: 'Sun', name: 'विकट संकष्टी', tithi: 'वैशाख, कृष्ण चतुर्थी' },
  { month: 'May', day: 5, weekday: 'Tue', name: 'एकदन्त संकष्टी', tithi: 'ज्येष्ठ, कृष्ण चतुर्थी' },
  { month: 'Jun', day: 3, weekday: 'Wed', name: 'विभुवन संकष्टी', tithi: 'आषाढ़ (अधिक), कृष्ण चतुर्थी' },
  { month: 'Jul', day: 3, weekday: 'Fri', name: 'गजानन संकष्टी', tithi: 'आषाढ़, कृष्ण चतुर्थी' },
  { month: 'Aug', day: 1, weekday: 'Sat', name: 'हेरम्ब संकष्टी', tithi: 'श्रावण, कृष्ण चतुर्थी' },
  { month: 'Aug', day: 31, weekday: 'Mon', name: 'विघ्नराज संकष्टी', tithi: 'भाद्रपद, कृष्ण चतुर्थी' },
  { month: 'Sep', day: 29, weekday: 'Tue', name: 'वक्रतुण्ड संकष्टी', tithi: 'आश्विन, कृष्ण चतुर्थी' },
  { month: 'Oct', day: 29, weekday: 'Thu', name: 'गणाधिप संकष्टी', tithi: 'कार्तिक, कृष्ण चतुर्थी' },
  { month: 'Nov', day: 27, weekday: 'Fri', name: 'अखुरथ संकष्टी', tithi: 'मार्गशीर्ष, कृष्ण चतुर्थी' },
  { month: 'Dec', day: 27, weekday: 'Sun', name: 'संकष्टी चतुर्थी', tithi: 'पौष, कृष्ण चतुर्थी' }
];

const SANKASHTI_RELATED = [
  { name: 'संकष्टी चतुर्थी व्रत कथा', emoji: '📖' },
  { name: 'श्री गणेश 108 नाम', emoji: '📿' },
  { name: 'गणेश आरती', emoji: '🪔' },
  { name: 'गणेश चालीसा', emoji: '📜' },
  { name: 'गणेश मंत्र', emoji: '🕉️' },
  { name: 'वक्रतुण्ड महाकाय', emoji: '🙏' },
  { name: '21 नाम पूजा', emoji: '🌸' },
  { name: '21 पत्र पूजा', emoji: '🍃' },
  { name: 'अंग पूजा विधि', emoji: '🧘' },
  { name: 'भगवान गणेश', emoji: '🐘' },
  { name: 'अष्टविनायक', emoji: '🏛️' },
  { name: 'गणेश चतुर्थी', emoji: '🎉' }
];

function initVratGrids() {
`;

let suffix = code.substring(code.indexOf("const vgrid = document.getElementById('vrat-home-grid');"));
let innerVrat = suffix.substring(0, suffix.indexOf('function initSankashtiPage() {'));

innerVrat = innerVrat.replace(/const SANKASHTI_DATES_2026[\s\S]*?\];/g, '');
innerVrat = innerVrat.replace(/const SANKASHTI_RELATED[\s\S]*?\];/g, '');

let initSankashti = suffix.substring(suffix.indexOf('function initSankashtiPage() {'));

fs.writeFileSync('app.js', prefix + '\n\n' + newData + innerVrat + '\n\n' + initSankashti, 'utf8');
console.log('Fixed Unicode arrays successfully!');
