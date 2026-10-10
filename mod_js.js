const fs = require('fs');
let app = fs.readFileSync('app.js', 'utf8');

// The player logic is inside initKatha
// Let's find where audioPlayer is declared and add the timeupdate event listener.

if (!app.includes('timeupdate')) {
    const audioPlayerDecl = 'let audioPlayer = new Audio();';
    const newDecl = `let audioPlayer = new Audio();
  const miniTime = document.getElementById('mini-time');
  const miniProgress = document.getElementById('mini-progress-fill');
  
  function formatTime(secs) {
    if(isNaN(secs)) return '00:00';
    const m = Math.floor(secs / 60);
    const s = Math.floor(secs % 60);
    return m.toString().padStart(2, '0') + ':' + s.toString().padStart(2, '0');
  }

  audioPlayer.addEventListener('timeupdate', () => {
    if(audioPlayer.duration) {
      const p = (audioPlayer.currentTime / audioPlayer.duration) * 100;
      if(miniProgress) miniProgress.style.width = p + '%';
      if(miniTime) miniTime.textContent = formatTime(audioPlayer.currentTime) + ' / ' + formatTime(audioPlayer.duration);
    }
  });
  
  audioPlayer.addEventListener('loadedmetadata', () => {
    if(miniTime) miniTime.textContent = '00:00 / ' + formatTime(audioPlayer.duration);
  });
`;
    app = app.replace(audioPlayerDecl, newDecl);
    fs.writeFileSync('app.js', app);
    console.log("Added timeupdate to app.js");
} else {
    console.log("Already has timeupdate");
}
