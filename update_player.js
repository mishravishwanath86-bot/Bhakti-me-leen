const fs = require('fs');

// 1. Update index.html
let html = fs.readFileSync('index.html', 'utf8');
if(!html.includes('mini-progress-bar')) {
  html = html.replace(
    '<div class="mini-player hidden" id="mini-player">',
    `<div class="mini-player hidden" id="mini-player">
      <div class="mini-progress-bar" id="mini-progress-bar">
        <div class="mini-progress-fill" id="mini-progress-fill"></div>
      </div>`
  );
  fs.writeFileSync('index.html', html, 'utf8');
}

// 2. Update styles.css
let css = fs.readFileSync('styles.css', 'utf8');
if(!css.includes('.mini-progress-bar')) {
  css += `
.mini-progress-bar {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: rgba(255,255,255,0.2);
  cursor: pointer;
}
.mini-progress-fill {
  height: 100%;
  width: 0%;
  background: #fde047;
}
.mini-player-time {
  font-size: 0.65rem;
  color: #fbbf24;
  margin-top: 2px;
}
`;
  fs.writeFileSync('styles.css', css, 'utf8');
}

// 3. Update app.js
let js = fs.readFileSync('app.js', 'utf8');
// Replace the URL with soundhelix
js = js.replace(/https:\/\/upload.wikimedia.org\/wikipedia\/commons\/[^'"]+/g, 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3');

// Add audio event listeners
if(!js.includes('audioPlayer.addEventListener("timeupdate"')) {
  const insertIndex = js.indexOf('function updateMiniPlayerUI()');
  const addEvents = `
  const progFill = document.getElementById('mini-progress-fill');
  const progBar = document.getElementById('mini-progress-bar');
  const timeDisp = document.getElementById('mini-sub'); // We will reuse the subtitle for time

  function formatTime(s) {
    if(isNaN(s)) return "0:00";
    let m = Math.floor(s / 60);
    let sec = Math.floor(s % 60);
    return m + ":" + (sec < 10 ? "0"+sec : sec);
  }

  audioPlayer.addEventListener('timeupdate', () => {
    if(!audioPlayer.duration) return;
    let pct = (audioPlayer.currentTime / audioPlayer.duration) * 100;
    progFill.style.width = pct + '%';
    timeDisp.innerHTML = formatTime(audioPlayer.currentTime) + ' / ' + formatTime(audioPlayer.duration);
  });

  progBar.addEventListener('click', (e) => {
    let rect = progBar.getBoundingClientRect();
    let x = e.clientX - rect.left;
    let pct = x / rect.width;
    audioPlayer.currentTime = pct * audioPlayer.duration;
  });
  
  document.getElementById('mini-seek').addEventListener('click', () => {
     audioPlayer.currentTime -= 10;
     if(audioPlayer.currentTime < 0) audioPlayer.currentTime = 0;
  });

  `;
  js = js.substring(0, insertIndex) + addEvents + js.substring(insertIndex);
  fs.writeFileSync('app.js', js, 'utf8');
}
console.log('Player UI updated');
