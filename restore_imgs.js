const fs = require('fs');

let code = fs.readFileSync('app.js', 'utf8');

// I will manually map the names back to the original vrats_img.
const map = {
  'प्रमुख 10 व्रत': 'assets/vrat_img_0_0.jpg',
  'संकष्टी चतुर्थी': 'assets/vrat_img_0_1.jpg',
  'एकादशी व्रत': 'assets/vrat_img_0_2.jpg',
  'प्रदोष व्रत': 'assets/vrat_img_0_3.jpg',
  'विनायक चतुर्थी': 'assets/vrat_img_1_0.jpg',
  'द्वादशी तिथियाँ': 'assets/vrat_img_1_1.jpg',
  'महाद्वादशी': 'assets/vrat_img_1_2.jpg',
  'मासिक शिवरात्रि': 'assets/vrat_img_1_3.jpg',
  'सावन सोमवार': 'assets/vrat_img_2_0.jpg',
  'श्री सत्यनारायण': 'assets/vrat_img_2_1.jpg',
  'पूर्णिमा व्रत': 'assets/vrat_img_2_2.jpg',
  'नवग्रह उपवास': 'assets/vrat_img_2_3.jpg',
  'देवी-देवता उपवास': 'assets/vrat_img_3_0.jpg',
  'अमावस्या': 'assets/vrat_img_3_1.jpg',
  'स्कंद षष्ठी': 'assets/vrat_img_3_2.jpg',
  'कार्तिगाई': 'assets/vrat_img_3_3.jpg',
  'श्राद्ध तिथियाँ': 'assets/vrat_img_4_0.jpg',
  'दुर्गाष्टमी': 'assets/vrat_img_4_1.jpg',
  'कालाष्टमी': 'assets/vrat_img_4_2.jpg',
  'रोहिणी व्रत': 'assets/vrat_img_4_3.jpg',
  
  'संक्रांति कैलेंडर': 'assets/vrat_img_5_0.jpg',
  'चंद्र दर्शन': 'assets/vrat_img_5_1.jpg',
  'मंगला गौरी': 'assets/vrat_img_5_2.jpg',
  'इष्टि एवं अन्वाधान': 'assets/vrat_img_5_3.jpg',
  'इस्कॉन एकादशी': 'assets/vrat_img_6_1.jpg',
  'मासिक जन्माष्टमी': 'assets/vrat_img_6_2.jpg'
};

for (const [name, img] of Object.entries(map)) {
    // Replace in HINDU_VRATS / SPECIAL_VRATS
    // Find name: '...', img: 'assets/deity_...'
    let regex = new RegExp(`name:\\s*'${name}',\\s*img:\\s*'[^']+'`);
    code = code.replace(regex, `name: '${name}', img: '${img}'`);
}

// VRAT_PAGES_DATA heroImgs
const pageKeyMap = {
  'ekadashi': 'assets/vrat_img_0_2.jpg',
  'pradosham': 'assets/vrat_img_0_3.jpg',
  'vinayaka-chaturthi': 'assets/vrat_img_1_0.jpg',
  'dwadashi': 'assets/vrat_img_1_1.jpg',
  'masik-shivaratri': 'assets/vrat_img_1_3.jpg',
  'mahadwadashi': 'assets/vrat_img_1_2.jpg',
  'sawan-somwar': 'assets/vrat_img_2_0.jpg',
  'satyanarayan': 'assets/vrat_img_2_1.jpg',
  'purnima': 'assets/vrat_img_2_2.jpg',
  'navagraha': 'assets/vrat_img_2_3.jpg',
  'devi-devta': 'assets/vrat_img_3_0.jpg',
  'amavasya': 'assets/vrat_img_3_1.jpg',
  'skanda-sashti': 'assets/vrat_img_3_2.jpg',
  'karthigai': 'assets/vrat_img_3_3.jpg',
  'shraddha': 'assets/vrat_img_4_0.jpg',
  'durgashtami': 'assets/vrat_img_4_1.jpg',
  'kalashtami': 'assets/vrat_img_4_2.jpg',
  'rohini-vrat': 'assets/vrat_img_4_3.jpg',
  'sankranti': 'assets/vrat_img_5_0.jpg',
  'chandra-darshan': 'assets/vrat_img_5_1.jpg',
  'mangala-gauri': 'assets/vrat_img_5_2.jpg',
  'ishti': 'assets/vrat_img_5_3.jpg',
  'iskcon-ekadashi': 'assets/vrat_img_6_1.jpg',
  'masik-janmashtami': 'assets/vrat_img_6_2.jpg'
};

for (const [key, img] of Object.entries(pageKeyMap)) {
    let regex = new RegExp(`('${key}':\\s*\\{[\\s\\S]*?heroImg:\\s*)'[^']+'`);
    code = code.replace(regex, `$1'${img}'`);
}

// Restore Sankashti images!
// In SANKASHTI_DATES_2026, it currently says `img: 'assets/deity_ganesh.jpg'`
// We need to put back `assets/sk_img_${i}.jpg`
let sk_match = code.match(/const SANKASHTI_DATES_2026 = \[([\s\S]*?)\];/);
if (sk_match) {
    let lines = sk_match[1].trim().split('\n');
    let newLines = lines.map((l, i) => {
        return l.replace(/img:\s*'assets\/deity_ganesh\.jpg'/, `img: 'assets/sk_img_${i}.jpg'`);
    });
    code = code.replace(sk_match[0], `const SANKASHTI_DATES_2026 = [\n${newLines.join('\n')}\n];`);
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Restored original images to JS!');
