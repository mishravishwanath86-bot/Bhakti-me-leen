const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

code = code.replace(/{ name: 'एकादशी व्रत', emoji: '🌿' }/, "{ name: 'एकादशी व्रत', emoji: '🌿', page: 'ekadashi', isDynamic: true }");
code = code.replace(/{ name: 'प्रदोष व्रत', emoji: '🌙' }/, "{ name: 'प्रदोष व्रत', emoji: '🌙', page: 'pradosham', isDynamic: true }");
code = code.replace(/{ name: 'विनायक चतुर्थी', emoji: '🐘' }/, "{ name: 'विनायक चतुर्थी', emoji: '🐘', page: 'vinayaka-chaturthi', isDynamic: true }");
code = code.replace(/{ name: 'द्वादशी तिथियाँ', emoji: '📿' }/, "{ name: 'द्वादशी तिथियाँ', emoji: '📿', page: 'dwadashi', isDynamic: true }");
code = code.replace(/{ name: 'मासिक शिवरात्रि', emoji: '🕉️' }/, "{ name: 'मासिक शिवरात्रि', emoji: '🕉️', page: 'masik-shivaratri', isDynamic: true }");

// Replace the onclick handler logic for dynamic pages
code = code.replace(
  /<div class="vrat-card" onclick="if\(typeof '\${v\.page}' !== 'undefined' && '\${v\.page}' !== 'undefined'\) showPage\('\${v\.page}'\)">/g,
  '<div class="vrat-card" onclick="if(\'${v.isDynamic}\' === \'true\') openVratPage(\'${v.page}\'); else if(\'${v.page}\' !== \'undefined\') showPage(\'${v.page}\');">'
);

fs.writeFileSync('app.js', code, 'utf8');
console.log('Linked dynamic vrats!');
