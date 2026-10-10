const fs = require('fs');
const lines = fs.readFileSync('app.js', 'utf8').split('\n');

const results = [];
for(let i=0; i<lines.length; i++){
    if(lines[i].includes('function initCalendar(){')) {
        results.push(i);
    }
}
console.log(results);
