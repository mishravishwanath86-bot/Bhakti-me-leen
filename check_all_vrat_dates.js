const fs = require('fs');

const f1 = JSON.parse(fs.readFileSync('vrat_data.json', 'utf8'));
const f2 = JSON.parse(fs.readFileSync('vrat_data_4.json', 'utf8'));
const f3 = JSON.parse(fs.readFileSync('vrat_data_7.json', 'utf8'));
const f4 = JSON.parse(fs.readFileSync('vrat_data_8.json', 'utf8'));

const allData = Object.assign({}, f1, f2, f3, f4);
console.log("Total vrat categories:", Object.keys(allData).length);
for (let k of Object.keys(allData)) {
  console.log(`${k}: ${allData[k].length} dates (e.g. ${JSON.stringify(allData[k][0])})`);
}
