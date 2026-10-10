const fs = require('fs');

const f1 = JSON.parse(fs.readFileSync('vrat_data.json', 'utf8'));
const f2 = JSON.parse(fs.readFileSync('vrat_data_4.json', 'utf8'));
const f3 = JSON.parse(fs.readFileSync('vrat_data_7.json', 'utf8'));
const f4 = JSON.parse(fs.readFileSync('vrat_data_8.json', 'utf8'));

console.log("Keys in vrat_data.json:", Object.keys(f1));
console.log("Keys in vrat_data_4.json:", Object.keys(f2));
console.log("Keys in vrat_data_7.json:", Object.keys(f3));
console.log("Keys in vrat_data_8.json:", Object.keys(f4));
