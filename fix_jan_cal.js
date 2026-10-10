const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// The entry is likely '7-9':'जन्माष्टमी'
code = code.replace("'7-9':'जन्माष्टमी',", "");
// Just in case it has different spacing
code = code.replace(/'7-9':\s*'जन्माष्टमी',?/, "");

// We added '8-4':'जन्माष्टमी' earlier, let's verify if it's there
if (!code.includes("'8-4':'जन्माष्टमी'")) {
    code = code.replace("'8-14':'गणेश चतुर्थी 🌟',", "'8-4':'जन्माष्टमी', '8-14':'गणेश चतुर्थी 🌟',");
}

fs.writeFileSync('app.js', code, 'utf8');
