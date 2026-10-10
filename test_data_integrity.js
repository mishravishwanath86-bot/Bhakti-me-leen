const fs = require('fs');
const code = fs.readFileSync('app.js', 'utf8');

// Test that VRAT_PAGES_DATA is valid JSON
const m = code.match(/const VRAT_PAGES_DATA = (\{[\s\S]*?\n\});/);
if (m) {
  const data = eval('(' + m[1] + ')');
  console.log("VRAT_PAGES_DATA valid! Keys count:", Object.keys(data).length);
  for (let k of Object.keys(data)) {
    console.log(` - ${k}: title="${data[k].title}", dates=${data[k].dates.length}, heroImg="${data[k].heroImg}"`);
  }
} else {
  console.log("❌ VRAT_PAGES_DATA not found");
}

const m2 = code.match(/const TOP10_FESTIVALS = (\[[\s\S]*?\n\]);/);
if (m2) {
  const data = eval(m2[1]);
  console.log("\nTOP10_FESTIVALS valid! Count:", data.length);
  data.forEach((f, i) => {
    console.log(` - #${i+1} ${f.name}: page=${f.page || 'none'}, links=${f.links ? f.links.length : 0}`);
  });
}
