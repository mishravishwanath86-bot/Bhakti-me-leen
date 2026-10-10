const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// The file currently ends with:
// let audioPlayer = new Audio();
// We will append the rest of initKatha, plus a splash screen hider, and call initKatha!

const appendCode = `
  const miniPlayBtn = document.getElementById('mini-play');
  const timeDisp = document.getElementById('mini-time');
  const progFill = document.getElementById('mini-progress-fill');
  const miniPlayer = document.getElementById('mini-player');

  function formatTime(s){ if(isNaN(s))return '00:00'; let m=Math.floor(s/60); let sec=Math.floor(s%60); return m.toString().padStart(2,'0')+':'+sec.toString().padStart(2,'0'); }

  audioPlayer.addEventListener('timeupdate', () => {
    if(!audioPlayer.duration) return;
    if(timeDisp) timeDisp.innerText = formatTime(audioPlayer.currentTime) + ' / ' + formatTime(audioPlayer.duration);
    if(progFill) progFill.style.width = ((audioPlayer.currentTime / audioPlayer.duration)*100) + '%';
  });

  audioPlayer.addEventListener('ended', () => { playing = false; updateMiniPlayerUI(); });

  miniPlayBtn?.addEventListener('click', () => {
    if(!currentKatha) return;
    if(playing) {
       audioPlayer.pause();
       playing = false;
    } else {
       audioPlayer.play();
       playing = true;
    }
    updateMiniPlayerUI();
  });

  function updateMiniPlayerUI() {
    if(miniPlayBtn) {
       miniPlayBtn.innerHTML = playing ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>' : '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>';
       miniPlayBtn.classList.toggle('playing', playing);
    }
  }

  window.playKatha = function(k){
    if (currentKatha && currentKatha.id === k.id) {
       if(playing) { audioPlayer.pause(); playing = false; }
       else { audioPlayer.play(); playing = true; }
       updateMiniPlayerUI();
       return;
    }
    currentKatha = k;
    playing = true;
    audioPlayer.src = k.url || 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Gayatri_Mantra.ogg';
    audioPlayer.play();
    document.getElementById('mini-thumb').innerHTML = k.emoji;
    document.getElementById('mini-title').textContent = k.title;
    document.getElementById('mini-sub').textContent = 'Episode 1';
    miniPlayer?.classList.remove('hidden');
    updateMiniPlayerUI();
  }
}

window.addEventListener('load', () => {
    const splash = document.getElementById('splash-screen');
    if (splash) {
        splash.style.opacity = 0;
        setTimeout(() => splash.style.display = 'none', 300);
    }
    // Call init functions that survive
    initKatha();
    if(typeof initPWA === 'function') initPWA();
});
`;

fs.writeFileSync('app.js', code + appendCode, 'utf8');
console.log('Appended audio logic and splash screen hider.');
