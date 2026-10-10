const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Insert time display before mini-seek-btn
if (!html.includes('id="mini-time"')) {
    html = html.replace(
        '<button class="mini-seek-btn"',
        '<div id="mini-time" style="font-size:0.7rem; color:rgba(255,255,255,0.7); min-width: 70px; text-align: center;">00:00</div>\n      <button class="mini-seek-btn"'
    );
    fs.writeFileSync('index.html', html);
    console.log("Added #mini-time to HTML");
} else {
    console.log("Already has #mini-time");
}
