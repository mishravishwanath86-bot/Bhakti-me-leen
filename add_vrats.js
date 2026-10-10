const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Add new vrats to VRAT_PAGES_DATA
const newVrats = `
  'mahadwadashi': {
    title: 'महाद्वादशी 2026',
    heroImg: 'assets/deity_vishnu.jpg',
    heroTitle: 'महाद्वादशी',
    heroSubtitle: 'भगवान विष्णु का परम पावन व्रत',
    relatedTitle: 'भगवान विष्णु से संबंधित अन्य लिंक्स',
    dates: [],
    related: [
      { name: 'विष्णु सहस्रनाम', emoji: '📜' },
      { name: 'विष्णु आरती', emoji: '🪔' },
      { name: 'विष्णु मंत्र', emoji: '🕉️' }
    ]
  },
  'sawan-somwar': {
    title: 'सावन सोमवार 2026',
    heroImg: 'assets/deity_shiv.jpg',
    heroTitle: 'सावन सोमवार',
    heroSubtitle: 'श्रावण मास में महादेव की विशेष पूजा',
    relatedTitle: 'भगवान शिव से संबंधित अन्य लिंक्स',
    dates: [],
    related: [
      { name: 'शिव चालीसा', emoji: '📜' },
      { name: 'शिव आरती', emoji: '🪔' },
      { name: 'महामृत्युंजय मंत्र', emoji: '🕉️' },
      { name: 'रुद्राष्टकम', emoji: '🙏' }
    ]
  },
  'satyanarayan': {
    title: 'श्री सत्यनारायण 2026',
    heroImg: 'assets/deity_vishnu.jpg',
    heroTitle: 'श्री सत्यनारायण',
    heroSubtitle: 'सत्यनारायण भगवान की कथा और व्रत',
    relatedTitle: 'सत्यनारायण कथा लिंक्स',
    dates: [],
    related: [
      { name: 'सत्यनारायण कथा', emoji: '📖' },
      { name: 'सत्यनारायण आरती', emoji: '🪔' },
      { name: 'विष्णु सहस्रनाम', emoji: '📜' }
    ]
  },
  'purnima': {
    title: 'पूर्णिमा व्रत 2026',
    heroImg: 'assets/deity_satyanarayan.jpg', // or vishnu
    heroTitle: 'पूर्णिमा व्रत',
    heroSubtitle: 'हर माह की पूर्णिमा का उपवास',
    relatedTitle: 'पूर्णिमा व्रत लिंक्स',
    dates: [],
    related: [
      { name: 'सत्यनारायण कथा', emoji: '📖' },
      { name: 'चंद्र दर्शन', emoji: '🌛' },
      { name: 'विष्णु आरती', emoji: '🪔' }
    ]
  },
`;

// Insert into VRAT_PAGES_DATA
code = code.replace(/const VRAT_PAGES_DATA = \{/, `const VRAT_PAGES_DATA = {${newVrats}`);

// Link pages in HINDU_VRATS
code = code.replace(/{ name: 'महाद्वादशी', img: 'assets\/vrat_img_1_2.jpg' }/, "{ name: 'महाद्वादशी', img: 'assets/vrat_img_1_2.jpg', page: 'mahadwadashi', isDynamic: true }");
code = code.replace(/{ name: 'सावन सोमवार', img: 'assets\/vrat_img_2_0.jpg' }/, "{ name: 'सावन सोमवार', img: 'assets/vrat_img_2_0.jpg', page: 'sawan-somwar', isDynamic: true }");
code = code.replace(/{ name: 'श्री सत्यनारायण', img: 'assets\/vrat_img_2_1.jpg' }/, "{ name: 'श्री सत्यनारायण', img: 'assets/vrat_img_2_1.jpg', page: 'satyanarayan', isDynamic: true }");
code = code.replace(/{ name: 'पूर्णिमा व्रत', img: 'assets\/vrat_img_2_2.jpg' }/, "{ name: 'पूर्णिमा व्रत', img: 'assets/vrat_img_2_2.jpg', page: 'purnima', isDynamic: true }");

fs.writeFileSync('app.js', code, 'utf8');
console.log('Added 4 new VRAT_PAGES_DATA keys');
