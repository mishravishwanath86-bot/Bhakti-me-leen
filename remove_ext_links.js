const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Remove the external links section from Diwali page
// Replace the entire "अधिक जानकारी" section in Diwali with nothing
html = html.replace(
  /<div style="display:flex; flex-direction:column; gap:0.8rem;">\s*<div style="font-size:1rem; font-weight:800; color:var\(--maroon\); margin-bottom:0.4rem;">🔗 अधिक जानकारी<\/div>[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/section>\s*<!-- 🌺 HOLI PAGE 🌺 -->/g,
  (match) => {
    // Keep only the closing tags and the HOLI PAGE comment
    return match.split('<!-- 🌺 HOLI PAGE 🌺 -->')[0].replace(/<div style="display:flex; flex-direction:column; gap:0.8rem;">[\s\S]*$/, '</div>\n    </section>\n\n    <!-- 🌺 HOLI PAGE 🌺 -->');
  }
);

// Also remove all <a href="http... external links from Holi and Rakhi pages
// Replace external link sections with a note saying data is shown above
html = html.replace(/<a href="https:\/\/www\.Sanatan Panchang\.com[^"]*"[^>]*>[\s\S]*?<\/a>/g, '');

// Remove leftover empty link sections
html = html.replace(/<div style="display:flex; flex-direction:column; gap:0.8rem;">\s*<div style="font-size:1rem; font-weight:800[^"]*">🔗 अधिक जानकारी<\/div>\s*<\/div>/g, '');

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Removed all external links from index.html!');
