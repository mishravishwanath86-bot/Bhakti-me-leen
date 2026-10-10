const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Find initKatha body
let initStart = code.indexOf('function initKatha(){');
let initEnd = code.indexOf('function initAchievements(){');

if (initStart !== -1 && initEnd !== -1) {
  let oldInit = code.substring(initStart, initEnd);
  
  // We need to carefully inject audioPlayer logic.
  let newInit = oldInit;
  
  // 1. Add audioPlayer declaration
  if (!newInit.includes('let audioPlayer = new Audio();')) {
     newInit = newInit.replace(
       'let currentKatha = null, playing = false;',
       'let currentKatha = null, playing = false;\n  let audioPlayer = new Audio();'
     );
  }
  
  // 2. Add timeDisp
  if(!newInit.includes("const timeDisp = document.getElementById('mini-time');")) {
      newInit = newInit.replace(
        "const miniPlayBtn = document.getElementById('mini-play');",
        "const miniPlayBtn = document.getElementById('mini-play');\n  const timeDisp = document.getElementById('mini-time');\n  const progFill = document.getElementById('mini-progress-fill');\n\n  function formatTime(s){ if(isNaN(s))return '00:00'; let m=Math.floor(s/60); let sec=Math.floor(s%60); return m.toString().padStart(2,'0')+':'+sec.toString().padStart(2,'0'); }\n\n  audioPlayer.addEventListener('timeupdate', () => {\n    if(!audioPlayer.duration) return;\n    if(timeDisp) timeDisp.innerText = formatTime(audioPlayer.currentTime) + ' / ' + formatTime(audioPlayer.duration);\n    if(progFill) progFill.style.width = ((audioPlayer.currentTime / audioPlayer.duration)*100) + '%';\n  });\n\n  audioPlayer.addEventListener('ended', () => { playing = false; updateMiniPlayerUI(); });"
      );
  }
  
  // 3. Update play button toggle
  newInit = newInit.replace(
    /miniPlayBtn\?\.addEventListener\('click',\s*\(\)\s*=>\s*\{[\s\S]*?showToast[^\n]*\n\s*\}\);/,
    `miniPlayBtn?.addEventListener('click', () => {
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
  }`
  );
  
  // 4. Update playKatha function
  newInit = newInit.replace(
    /function playKatha\(k\)[\s\S]*?showToast[^\n]*\n\s*\}/,
    `function playKatha(k){
    if (currentKatha && currentKatha.id === k.id) {
       // toggle
       if(playing) { audioPlayer.pause(); playing = false; }
       else { audioPlayer.play(); playing = true; }
       updateMiniPlayerUI();
       return;
    }
    currentKatha = k;
    playing = true;
    audioPlayer.src = k.url || 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3';
    audioPlayer.play();
    document.getElementById('mini-thumb').innerHTML = k.emoji;
    document.getElementById('mini-title').textContent = k.title;
    document.getElementById('mini-sub').textContent = 'Episode 1';
    miniPlayer?.classList.remove('hidden');
    updateMiniPlayerUI();
  }`
  );
  
  code = code.replace(oldInit, newInit);
  fs.writeFileSync('app.js', code);
  console.log("Audio injected successfully!");
} else {
  console.log("Could not find init boundaries.");
}
