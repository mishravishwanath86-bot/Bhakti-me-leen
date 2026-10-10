const fs = require('fs');

let addEng = fs.readFileSync('add_eng_cal.js', 'utf8');
const codeStart = addEng.indexOf("const engCalCode = `") + 20;
const codeEnd = addEng.lastIndexOf("`;\n\n// Add to end of app.js");
if(codeStart > 19 && codeEnd > -1) {
    const engCalCode = addEng.substring(codeStart, codeEnd);
    
    let app = fs.readFileSync('app.js', 'utf8');
    if(!app.includes('function initEngCalendar()')) {
        // insert before window.addEventListener('load'
        const loadStart = app.lastIndexOf("window.addEventListener('load'");
        if(loadStart > -1) {
            app = app.substring(0, loadStart) + engCalCode + '\n\n' + app.substring(loadStart);
            
            // Add initEngCalendar to the array of init functions to call
            app = app.replace("'initKatha'", "'initKatha', 'initEngCalendar'");
            
            fs.writeFileSync('app.js', app, 'utf8');
            console.log('Restored initEngCalendar');
        }
    } else {
        console.log('initEngCalendar already in app.js');
    }
}
