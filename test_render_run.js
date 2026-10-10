const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// evaluate the initTop10Page function by writing it and calling it
const testCode = `
  const document = { getElementById: () => ({ style: {}, innerHTML: '' }) };
` + code.match(/const TOP10_FESTIVALS = [\s\S]*?];/)[0] + '\n' +
code.match(/function initTop10Page\(\) \{[\s\S]*?\n\}/)[0] + `
  const fakeContainer = document.getElementById();
  initTop10Page();
  console.log(fakeContainer.innerHTML.substring(0, 1000));
`;

fs.writeFileSync('test_render.js', testCode, 'utf8');
