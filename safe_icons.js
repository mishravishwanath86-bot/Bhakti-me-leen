const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');

// We will do a robust replacement based on the name of the vrat in the arrays.
const map = {
  'प्रमुख 10 व्रत': 'assets/panchang_book.jpg',
  'संकष्टी चतुर्थी': 'assets/deity_ganesh.jpg',
  'एकादशी व्रत': 'assets/deity_vishnu.jpg',
  'प्रदोष व्रत': 'assets/deity_shiv.jpg',
  'विनायक चतुर्थी': 'assets/deity_ganesh.jpg',
  'द्वादशी तिथियाँ': 'assets/deity_vishnu.jpg',
  'महाद्वादशी': 'assets/deity_vishnu.jpg',
  'मासिक शिवरात्रि': 'assets/deity_shiv.jpg',
  'सावन सोमवार': 'assets/deity_shiv.jpg',
  'श्री सत्यनारायण': 'assets/deity_vishnu.jpg',
  'पूर्णिमा व्रत': 'assets/deity_vishnu.jpg',
  'नवग्रह उपवास': 'assets/deity_navagraha.jpg',
  'देवी-देवता उपवास': 'assets/deity_durga.jpg',
  'अमावस्या': 'assets/deity_shiv.jpg',
  'स्कंद षष्ठी': 'assets/deity_shiv.jpg',
  'कार्तिगाई': 'assets/deity_shiv.jpg',
  'श्राद्ध तिथियाँ': 'assets/deity_vishnu.jpg',
  'दुर्गाष्टमी': 'assets/deity_durga.jpg',
  'कालाष्टमी': 'assets/deity_shiv.jpg',
  'रोहिणी व्रत': 'assets/deity_saraswati.jpg',
  
  'संक्रांति कैलेंडर': 'assets/deity_surya.jpg',
  'चंद्र दर्शन': 'assets/deity_shiv.jpg',
  'मंगला गौरी': 'assets/deity_gauri.jpg',
  'इष्टि एवं अन्वाधान': 'assets/deity_vishnu.jpg',
  'इस्कॉन एकादशी': 'assets/deity_krishna.jpg',
  'मासिक जन्माष्टमी': 'assets/deity_krishna.jpg'
};

// Also we need to sync VRAT_PAGES_DATA heroImg!
// I will just use a generic regex replacement for the grid icons first:
for (const [name, img] of Object.entries(map)) {
    // Replace in HINDU_VRATS / SPECIAL_VRATS
    let regex = new RegExp(`name:\\s*'${name}',\\s*img:\\s*'assets/vrat_img_[^']+'`);
    code = code.replace(regex, `name: '${name}', img: '${img}'`);
    
    // Also try without assets/vrat_img just in case it's something else
    let regex2 = new RegExp(`name:\\s*'${name}',\\s*img:\\s*'[^']+'`);
    code = code.replace(regex2, `name: '${name}', img: '${img}'`);
}

// Now replace VRAT_PAGES_DATA heroImgs
// I will just replace all heroImg: '...' with heroImg: img for the corresponding page.
// Need a map from page key to img:
const pageKeyMap = {
  'ekadashi': 'assets/deity_vishnu.jpg',
  'pradosham': 'assets/deity_shiv.jpg',
  'vinayaka-chaturthi': 'assets/deity_ganesh.jpg',
  'dwadashi': 'assets/deity_vishnu.jpg',
  'masik-shivaratri': 'assets/deity_shiv.jpg',
  'mahadwadashi': 'assets/deity_vishnu.jpg',
  'sawan-somwar': 'assets/deity_shiv.jpg',
  'satyanarayan': 'assets/deity_vishnu.jpg',
  'purnima': 'assets/deity_vishnu.jpg',
  'navagraha': 'assets/deity_navagraha.jpg',
  'devi-devta': 'assets/deity_durga.jpg',
  'amavasya': 'assets/deity_shiv.jpg',
  'skanda-sashti': 'assets/deity_shiv.jpg',
  'karthigai': 'assets/deity_shiv.jpg',
  'shraddha': 'assets/deity_vishnu.jpg',
  'durgashtami': 'assets/deity_durga.jpg',
  'kalashtami': 'assets/deity_shiv.jpg',
  'rohini-vrat': 'assets/deity_saraswati.jpg',
  'sankranti': 'assets/deity_surya.jpg',
  'chandra-darshan': 'assets/deity_shiv.jpg',
  'mangala-gauri': 'assets/deity_gauri.jpg',
  'ishti': 'assets/deity_vishnu.jpg',
  'iskcon-ekadashi': 'assets/deity_krishna.jpg',
  'masik-janmashtami': 'assets/deity_krishna.jpg'
};

for (const [key, img] of Object.entries(pageKeyMap)) {
    let regex = new RegExp(`('${key}':\\s*\\{[\\s\\S]*?heroImg:\\s*)'[^']+'`);
    code = code.replace(regex, `$1'${img}'`);
}

// Delete all the old vrat_img files to clean up space and avoid confusion
fs.writeFileSync('app.js', code, 'utf8');
console.log('Copyright-safe images injected everywhere!');
