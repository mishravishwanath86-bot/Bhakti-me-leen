const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const newVrats = `
  'kalashtami': {
    title: 'कालाष्टमी 2026',
    heroImg: 'assets/deity_shiv.jpg',
    heroTitle: 'कालाष्टमी',
    heroSubtitle: 'भगवान कालभैरव की विशेष उपासना',
    relatedTitle: 'कालभैरव लिंक्स',
    dates: [],
    related: [
      { name: 'भैरव अष्टकम', emoji: '📜' },
      { name: 'कालभैरव आरती', emoji: '🪔' },
      { name: 'शिव स्तोत्र', emoji: '🕉️' }
    ]
  },
  'rohini-vrat': {
    title: 'रोहिणी व्रत 2026',
    heroImg: 'assets/deity_vishnu.jpg', // generic
    heroTitle: 'रोहिणी व्रत',
    heroSubtitle: 'जैन धर्म में विशेष व्रत',
    relatedTitle: 'जैन व्रत लिंक्स',
    dates: [],
    related: [
      { name: 'रोहिणी व्रत कथा', emoji: '📖' },
      { name: 'जैन तीर्थंकर', emoji: '🙏' }
    ]
  },
  'sankranti': {
    title: 'संक्रांति कैलेंडर 2026',
    heroImg: 'assets/deity_vishnu.jpg',
    heroTitle: 'संक्रांति',
    heroSubtitle: 'सूर्य देव का राशि परिवर्तन',
    relatedTitle: 'संक्रांति लिंक्स',
    dates: [],
    related: [
      { name: 'सूर्य मंत्र', emoji: '☀️' },
      { name: 'मकर संक्रांति', emoji: '🌾' },
      { name: 'दान का महत्व', emoji: '🤲' }
    ]
  },
  'chandra-darshan': {
    title: 'चंद्र दर्शन 2026',
    heroImg: 'assets/deity_shiv.jpg',
    heroTitle: 'चंद्र दर्शन',
    heroSubtitle: 'अमावस्या के बाद प्रथम चंद्र दर्शन',
    relatedTitle: 'चंद्र दर्शन लिंक्स',
    dates: [],
    related: [
      { name: 'चंद्र देव मंत्र', emoji: '🌙' },
      { name: 'शिव आरती', emoji: '🪔' },
      { name: 'मन की शांति', emoji: '🧘' }
    ]
  },
  'mangala-gauri': {
    title: 'मंगला गौरी 2026',
    heroImg: 'assets/deity_gauri.jpg',
    heroTitle: 'मंगला गौरी',
    heroSubtitle: 'श्रावण में देवी गौरी का व्रत',
    relatedTitle: 'देवी गौरी लिंक्स',
    dates: [],
    related: [
      { name: 'मंगला गौरी व्रत कथा', emoji: '📖' },
      { name: 'दुर्गा चालीसा', emoji: '📜' },
      { name: 'पार्वती स्तुति', emoji: '🌺' }
    ]
  },
  'ishti': {
    title: 'इष्टि एवं अन्वाधान 2026',
    heroImg: 'assets/deity_vishnu.jpg',
    heroTitle: 'इष्टि एवं अन्वाधान',
    heroSubtitle: 'वैष्णव संप्रदाय के विशेष उपवास',
    relatedTitle: 'वैष्णव लिंक्स',
    dates: [],
    related: [
      { name: 'विष्णु सहस्रनाम', emoji: '📜' },
      { name: 'वैष्णव नियम', emoji: '🙏' },
      { name: 'हरि नाम संकीर्तन', emoji: '🎶' }
    ]
  },
  'iskcon-ekadashi': {
    title: 'इस्कॉन एकादशी 2026',
    heroImg: 'assets/deity_vishnu.jpg',
    heroTitle: 'इस्कॉन एकादशी',
    heroSubtitle: 'इस्कॉन कैलेंडर के अनुसार एकादशी व्रत',
    relatedTitle: 'इस्कॉन लिंक्स',
    dates: [],
    related: [
      { name: 'हरे कृष्ण महामंत्र', emoji: '📿' },
      { name: 'इस्कॉन नियम', emoji: '📜' },
      { name: 'भगवद गीता', emoji: '📖' }
    ]
  },
  'masik-janmashtami': {
    title: 'मासिक जन्माष्टमी 2026',
    heroImg: 'assets/deity_vishnu.jpg',
    heroTitle: 'मासिक जन्माष्टमी',
    heroSubtitle: 'भगवान कृष्ण का मासिक जन्मोत्सव',
    relatedTitle: 'श्री कृष्ण लिंक्स',
    dates: [],
    related: [
      { name: 'कृष्ण भजन', emoji: '🎶' },
      { name: 'भगवद गीता', emoji: '📖' },
      { name: 'गोपाल सहस्रनाम', emoji: '📜' }
    ]
  },
`;

code = code.replace(/const VRAT_PAGES_DATA = \{/, `const VRAT_PAGES_DATA = {${newVrats}`);

// HINDU_VRATS remaining
code = code.replace(/{ name: 'कालाष्टमी', img: 'assets\/vrat_img_4_2.jpg' }/, "{ name: 'कालाष्टमी', img: 'assets/vrat_img_4_2.jpg', page: 'kalashtami', isDynamic: true }");
code = code.replace(/{ name: 'रोहिणी व्रत', img: 'assets\/vrat_img_4_3.jpg' }/, "{ name: 'रोहिणी व्रत', img: 'assets/vrat_img_4_3.jpg', page: 'rohini-vrat', isDynamic: true }");

// SPECIAL_VRATS
code = code.replace(/{ name: 'संक्रांति कैलेंडर', img: 'assets\/vrat_img_5_0.jpg' }/, "{ name: 'संक्रांति कैलेंडर', img: 'assets/vrat_img_5_0.jpg', page: 'sankranti', isDynamic: true }");
code = code.replace(/{ name: 'चंद्र दर्शन', img: 'assets\/vrat_img_5_1.jpg' }/, "{ name: 'चंद्र दर्शन', img: 'assets/vrat_img_5_1.jpg', page: 'chandra-darshan', isDynamic: true }");
code = code.replace(/{ name: 'मंगला गौरी', img: 'assets\/vrat_img_5_2.jpg' }/, "{ name: 'मंगला गौरी', img: 'assets/vrat_img_5_2.jpg', page: 'mangala-gauri', isDynamic: true }");
code = code.replace(/{ name: 'इष्टि एवं अन्वाधान', img: 'assets\/vrat_img_5_3.jpg' }/, "{ name: 'इष्टि एवं अन्वाधान', img: 'assets/vrat_img_5_3.jpg', page: 'ishti', isDynamic: true }");
code = code.replace(/{ name: 'इस्कॉन एकादशी', img: 'assets\/vrat_img_6_1.jpg' }/, "{ name: 'इस्कॉन एकादशी', img: 'assets/vrat_img_6_1.jpg', page: 'iskcon-ekadashi', isDynamic: true }");
code = code.replace(/{ name: 'मासिक जन्माष्टमी', img: 'assets\/vrat_img_6_2.jpg' }/, "{ name: 'मासिक जन्माष्टमी', img: 'assets/vrat_img_6_2.jpg', page: 'masik-janmashtami', isDynamic: true }");

fs.writeFileSync('app.js', code, 'utf8');
console.log('Added 8 new VRAT_PAGES_DATA keys');
