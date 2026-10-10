const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const newPlayerHTML = `
    <!-- 🎵 MUSIC PLAYER SYSTEM 🎵 -->
    
    <!-- 1. FLOATING MINI PLAYER -->
    <div class="glass-mini-player hidden" id="mini-player">
      <div class="glass-mini-content" id="mini-player-expand">
        <div class="glass-mini-thumb" id="mini-thumb">🕉️</div>
        <div class="glass-mini-info">
          <div class="glass-mini-title" id="mini-title">Title</div>
          <div class="glass-mini-sub" id="mini-sub">Subtitle</div>
        </div>
      </div>
      <div class="glass-mini-controls">
        <button class="glass-btn-icon" id="mini-like">🤍</button>
        <button class="glass-btn-play" id="mini-play">▶</button>
      </div>
      <div class="glass-mini-progress">
        <div class="glass-mini-progress-fill" id="mini-progress-fill"></div>
      </div>
    </div>

    <!-- 2. FULL SCREEN PLAYER -->
    <div class="glass-full-player hidden" id="full-player">
      <!-- Top Bar -->
      <div class="glass-fp-top">
        <button class="glass-fp-icon-btn" id="full-close">🔽</button>
        <div class="glass-fp-now-playing">अब बज रहा है</div>
        <button class="glass-fp-icon-btn">⋮</button>
      </div>
      
      <!-- Artwork -->
      <div class="glass-fp-artwork-container">
        <div class="glass-fp-artwork-ring">
          <div class="glass-fp-artwork" id="full-thumb">🕉️</div>
        </div>
      </div>
      
      <!-- Info -->
      <div class="glass-fp-info">
        <div class="glass-fp-title" id="full-title">Title</div>
        <div class="glass-fp-sub" id="full-sub">Subtitle</div>
      </div>
      
      <!-- Progress Bar -->
      <div class="glass-fp-progress-container">
        <span class="glass-fp-time" id="full-time-cur">0:00</span>
        <input type="range" class="glass-fp-slider" id="full-slider" value="0" min="0" max="100">
        <span class="glass-fp-time" id="full-time-tot">0:00</span>
      </div>
      
      <!-- Controls -->
      <div class="glass-fp-controls">
        <button class="glass-fp-ctrl-sm">🔀</button>
        <button class="glass-fp-ctrl-md" id="full-prev">⏮</button>
        <button class="glass-fp-ctrl-lg" id="full-play">▶</button>
        <button class="glass-fp-ctrl-md" id="full-next">⏭</button>
        <button class="glass-fp-ctrl-sm">🔁</button>
      </div>
      
      <!-- Lyrics Pull Up -->
      <div class="glass-fp-lyrics-tab">
        <div class="glass-fp-lyrics-handle"></div>
        कथा पाठ / Lyrics
      </div>
    </div>
`;

// Replace old mini-player block with the new system
const startIdx = html.indexOf('<!-- MINI PLAYER');
const endIdx = html.indexOf('</section>', startIdx); // wait, it's outside sections.
// Let's use regex to find the old mini player
const regex = /<!-- MINI PLAYER[\s\S]*?<\/div>(\s*<!-- 📥 DOWNLOADS -->|\s*<!-- 📥)/;
const match = html.match(regex);

if (match) {
    html = html.replace(match[0], newPlayerHTML + '\n' + match[1]);
    fs.writeFileSync('index.html', html, 'utf8');
    console.log("Replaced mini-player HTML with new Glassmorphism UI.");
} else {
    // If exact regex fails, try a broader one or manual replacement
    const r2 = /<div class="mini-player hidden" id="mini-player">[\s\S]*?id="mini-play">.*?<\/button>\s*<\/div>/;
    if(r2.test(html)) {
        html = html.replace(r2, newPlayerHTML);
        fs.writeFileSync('index.html', html, 'utf8');
        console.log("Replaced mini-player HTML using fallback regex.");
    } else {
        console.log("Could not find the old mini player to replace.");
    }
}
