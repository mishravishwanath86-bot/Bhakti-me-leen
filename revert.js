const fs = require('fs');

// Restore app.js
let appCode = fs.readFileSync('app.js', 'utf8');
let oldKatha = fs.readFileSync('katha_old.txt', 'utf8');
const s = appCode.indexOf('function initKatha(){');
const e = appCode.indexOf('//   ENGLISH CALENDAR');
if(s > -1 && e > -1) {
    // We need to back up before the comment block above ENGLISH CALENDAR
    const realEnd = appCode.lastIndexOf('// ═', e);
    
    appCode = appCode.substring(0, s) + oldKatha + '\n\n' + appCode.substring(realEnd);
    fs.writeFileSync('app.js', appCode, 'utf8');
    console.log("Restored app.js");
}

// Restore index.html
let html = fs.readFileSync('index.html', 'utf8');
const newPlayerRegex = /<!-- 1\. FLOATING MINI PLAYER -->[\s\S]*?<\/div>\s*<\/div>/;
if (newPlayerRegex.test(html)) {
    const oldHtml = `
    <!-- MINI PLAYER (shown when katha playing) -->
    <div class="mini-player hidden" id="mini-player">
      <div class="mini-progress-bar" id="mini-progress-bar">
        <div class="mini-progress-fill" id="mini-progress-fill"></div>
      </div>
      <div class="mini-player-thumb" id="mini-thumb">???</div>
      <div class="mini-player-info">
        <div class="mini-player-title" id="mini-title">???</div>
        <div class="mini-player-sub" id="mini-sub">Episode 1</div>
      </div>
      <div id="mini-time" style="font-size:0.7rem; color:rgba(255,255,255,0.7); min-width: 70px; text-align: center;">00:00</div>
      <button class="mini-seek-btn" id="mini-seek">?<span style="font-size:0.55rem;display:block;margin-top:-3px">10</span></button>
      <button class="mini-play-btn" id="mini-play">?</button>
    </div>`;
    html = html.replace(newPlayerRegex, oldHtml);
    fs.writeFileSync('index.html', html, 'utf8');
    console.log("Restored index.html");
}

// Cache bust SW
let sw = fs.readFileSync('service-worker.js', 'utf8');
let v = parseInt(sw.match(/bhakti-cache-v(\d+)/)[1]);
sw = sw.replace(`bhakti-cache-v${v}`, `bhakti-cache-v${v+1}`);
fs.writeFileSync('service-worker.js', sw, 'utf8');

// Cache bust index.html timestamps
html = fs.readFileSync('index.html', 'utf8');
const time = new Date().getTime();
html = html.replace(/styles\.css(\?v=\d+)?/, `styles.css?v=${time}`);
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
