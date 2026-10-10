const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

const newVrats = `
  'navagraha': {
    title: 'नवग्रह उपवास 2026',
    heroImg: 'assets/deity_vishnu.jpg',
    heroTitle: 'नवग्रह उपवास',
    heroSubtitle: 'नवग्रहों की शांति के लिए साप्ताहिक व्रत',
    relatedTitle: 'नवग्रह संबंधित लिंक्स',
    dates: [],
    related: [
      { name: 'नवग्रह स्तोत्र', emoji: '📜' },
      { name: 'सूर्य मंत्र', emoji: '☀️' },
      { name: 'शनि देव आरती', emoji: '🪔' }
    ]
  },
  'devi-devta': {
    title: 'देवी-देवता उपवास 2026',
    heroImg: 'assets/deity_gauri.jpg',
    heroTitle: 'देवी-देवता उपवास',
    heroSubtitle: 'इष्ट देव की विशेष उपासना',
    relatedTitle: 'देवी-देवता लिंक्स',
    dates: [],
    related: [
      { name: 'दुर्गा चालीसा', emoji: '📜' },
      { name: 'हनुमान चालीसा', emoji: '🐒' },
      { name: 'आरती संग्रह', emoji: '🪔' }
    ]
  },
  'amavasya': {
    title: 'अमावस्या 2026',
    heroImg: 'assets/deity_shiv.jpg',
    heroTitle: 'अमावस्या',
    heroSubtitle: 'पितृ तर्पण और स्नान दान',
    relatedTitle: 'अमावस्या लिंक्स',
    dates: [],
    related: [
      { name: 'पितृ दोष शांति', emoji: '🙏' },
      { name: 'गंगा स्नान', emoji: '🌊' },
      { name: 'विष्णु स्तोत्र', emoji: '📜' }
    ]
  },
  'skanda-sashti': {
    title: 'स्कंद षष्ठी 2026',
    heroImg: 'assets/deity_narsingh.jpg',
    heroTitle: 'स्कंद षष्ठी',
    heroSubtitle: 'भगवान कार्तिकेय का पावन दिन',
    relatedTitle: 'भगवान कार्तिकेय लिंक्स',
    dates: [],
    related: [
      { name: 'सुब्रमण्यम अष्टकम', emoji: '📜' },
      { name: 'कार्तिकेय स्तोत्र', emoji: '🙏' },
      { name: 'शिव आरती', emoji: '🪔' }
    ]
  },
  'karthigai': {
    title: 'मासिक कार्तिगाई 2026',
    heroImg: 'assets/deity_shiv.jpg',
    heroTitle: 'कार्तिगाई',
    heroSubtitle: 'शिव-पार्वती उपासना का दिन',
    relatedTitle: 'शिव लिंक्स',
    dates: [],
    related: [
      { name: 'शिव चालीसा', emoji: '📜' },
      { name: 'रुद्राष्टकम', emoji: '🙏' },
      { name: 'महामृत्युंजय मंत्र', emoji: '🕉️' }
    ]
  },
  'shraddha': {
    title: 'श्राद्ध तिथियाँ 2026',
    heroImg: 'assets/deity_vishnu.jpg',
    heroTitle: 'श्राद्ध / पितृ पक्ष',
    heroSubtitle: 'पितरों का तर्पण एवं श्राद्ध',
    relatedTitle: 'श्राद्ध लिंक्स',
    dates: [],
    related: [
      { name: 'पितृ सूक्त', emoji: '📜' },
      { name: 'तर्पण विधि', emoji: '💧' },
      { name: 'भगवद गीता', emoji: '📖' }
    ]
  },
  'durgashtami': {
    title: 'मासिक दुर्गाष्टमी 2026',
    heroImg: 'assets/deity_gauri.jpg',
    heroTitle: 'दुर्गाष्टमी',
    heroSubtitle: 'माँ दुर्गा की विशेष पूजा',
    relatedTitle: 'माँ दुर्गा लिंक्स',
    dates: [],
    related: [
      { name: 'दुर्गा चालीसा', emoji: '📜' },
      { name: 'दुर्गा आरती', emoji: '🪔' },
      { name: 'नवदुर्गा', emoji: '🌺' }
    ]
  },
`;

code = code.replace(/const VRAT_PAGES_DATA = \{/, `const VRAT_PAGES_DATA = {${newVrats}`);

code = code.replace(/{ name: 'नवग्रह उपवास', img: 'assets\/vrat_img_2_3.jpg' }/, "{ name: 'नवग्रह उपवास', img: 'assets/vrat_img_2_3.jpg', page: 'navagraha', isDynamic: true }");
code = code.replace(/{ name: 'देवी-देवता उपवास', img: 'assets\/vrat_img_3_0.jpg' }/, "{ name: 'देवी-देवता उपवास', img: 'assets/vrat_img_3_0.jpg', page: 'devi-devta', isDynamic: true }");
code = code.replace(/{ name: 'अमावस्या', img: 'assets\/vrat_img_3_1.jpg' }/, "{ name: 'अमावस्या', img: 'assets/vrat_img_3_1.jpg', page: 'amavasya', isDynamic: true }");
code = code.replace(/{ name: 'स्कंद षष्ठी', img: 'assets\/vrat_img_3_2.jpg' }/, "{ name: 'स्कंद षष्ठी', img: 'assets/vrat_img_3_2.jpg', page: 'skanda-sashti', isDynamic: true }");
code = code.replace(/{ name: 'कार्तिगाई', img: 'assets\/vrat_img_3_3.jpg' }/, "{ name: 'कार्तिगाई', img: 'assets/vrat_img_3_3.jpg', page: 'karthigai', isDynamic: true }");
code = code.replace(/{ name: 'श्राद्ध तिथियाँ', img: 'assets\/vrat_img_4_0.jpg' }/, "{ name: 'श्राद्ध तिथियाँ', img: 'assets/vrat_img_4_0.jpg', page: 'shraddha', isDynamic: true }");
code = code.replace(/{ name: 'दुर्गाष्टमी', img: 'assets\/vrat_img_4_1.jpg' }/, "{ name: 'दुर्गाष्टमी', img: 'assets/vrat_img_4_1.jpg', page: 'durgashtami', isDynamic: true }");

fs.writeFileSync('app.js', code, 'utf8');
console.log('Added 7 new VRAT_PAGES_DATA keys');
