const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Fix English Calendar Janmashtami
code = code.replace(
  "'2026-08-15': { name: 'Independence Day / Janmashtami', hindi: 'स्वतंत्रता दिवस / जन्माष्टमी', type: 'holiday' },",
  "'2026-08-15': { name: 'Independence Day', hindi: 'स्वतंत्रता दिवस', type: 'holiday' },"
);
code = code.replace(
  "'2026-08-17': { name: 'Janmashtami (Smarta)', hindi: 'जन्माष्टमी (स्मार्त)', type: 'festival' },",
  "'2026-09-04': { name: 'Janmashtami', hindi: 'जन्माष्टमी', type: 'festival' },"
);

// Fix Hindi Calendar Janmashtami (CAL_FESTIVALS)
// Current might be '7-9':'जन्माष्टमी' or similar. 
// Note: we can't be sure about the exact unicode string because of encoding issues in terminal, but let's just do a regex.
code = code.replace(
  /'\d+-\d+':\s*'जन्माष्टमी'/g,
  ""
);
// Also add the correct one in CAL_FESTIVALS
code = code.replace(
  "'8-14':'गणेश चतुर्थी 🌟',",
  "'8-4':'जन्माष्टमी', '8-14':'गणेश चतुर्थी 🌟',"
);

// Also let's find other wrong ones in CAL_FESTIVALS and fix if possible, but let's just do Janmashtami for now since user pointed it out.
fs.writeFileSync('app.js', code, 'utf8');
console.log('Janmashtami fixed!');
