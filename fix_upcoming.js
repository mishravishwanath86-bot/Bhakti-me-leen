const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Fix 2026-08-15
code = code.replace(
  "{ date:'2026-08-15', name:'स्वतंत्रता दिवस / जन्माष्टमी व्रत', emoji:'🇮🇳', tithi:'श्रावण शु. एकादशी'},",
  "{ date:'2026-08-15', name:'स्वतंत्रता दिवस', emoji:'🇮🇳', tithi:'श्रावण शु. एकादशी'},"
);

// Add 2026-09-04
if(!code.includes("date:'2026-09-04'")) {
  code = code.replace(
    "{ date:'2026-09-14', name:'गणेश चतुर्थी',",
    "{ date:'2026-09-04', name:'जन्माष्टमी', emoji:'🦚', img:'assets/festival_janmashtami.jpg', tithi:'भाद्रपद कृ. अष्टमी'},\n  { date:'2026-09-14', name:'गणेश चतुर्थी',"
  );
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Upcoming events array fixed!');
