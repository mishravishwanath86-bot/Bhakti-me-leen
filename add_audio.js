const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Replace KATHA_LIST with URLs
const kathaListRegex = /const KATHA_LIST = \[([\s\S]*?)\];/;
const newKathaList = `const KATHA_LIST = [
  { id:'bhagwat',    title:'श्रीमद् भागवत कथा', emoji:'🕉️', plays:'59.3K', ep:12, url:'https://upload.wikimedia.org/wikipedia/commons/4/4b/Gayatri_Mantra.ogg' },
  { id:'mahabharat', title:'महाभारत : गुप्त द्वार', emoji:'⚔️', plays:'1.8L',  ep:8, url:'https://upload.wikimedia.org/wikipedia/commons/d/dd/Bhagavad_Gita_Sloka_1.ogg'  },
  { id:'ramkatha',   title:'रामकथा - वाल्मीकि', emoji:'🏹', plays:'42.1K', ep:18, url:'https://upload.wikimedia.org/wikipedia/commons/4/4b/Gayatri_Mantra.ogg' },
  { id:'shiv',       title:'शिव तांडव कथा', emoji:'🔱', plays:'28.3K', ep:9, url:'https://upload.wikimedia.org/wikipedia/commons/d/dd/Bhagavad_Gita_Sloka_1.ogg'  },
  { id:'krishna',    title:'कृष्ण लीला कथा', emoji:'🦚', plays:'18.6K', ep:15, url:'https://upload.wikimedia.org/wikipedia/commons/4/4b/Gayatri_Mantra.ogg' },
  { id:'sai',        title:'साईं कथा: सबका मालिक एक', emoji:'📿', plays:'8.7K',  ep:6, url:'https://upload.wikimedia.org/wikipedia/commons/d/dd/Bhagavad_Gita_Sloka_1.ogg'  },
  { id:'somnath',    title:'ज्योतिर्लिंग: सोमनाथ', emoji:'🛕', plays:'18.6K', ep:4, url:'https://upload.wikimedia.org/wikipedia/commons/4/4b/Gayatri_Mantra.ogg'  },
  { id:'durga',      title:'नवदुर्गा उत्पत्ति कथा', emoji:'🦁', plays:'12.4K', ep:7, url:'https://upload.wikimedia.org/wikipedia/commons/d/dd/Bhagavad_Gita_Sloka_1.ogg'  }
];`;

code = code.replace(kathaListRegex, newKathaList);

// Find initKatha and update the audio logic
let initKathaFunc = code.substring(code.indexOf('function initKatha(){'));
const initEnd = initKathaFunc.indexOf('initAchievements()'); // Next function
if(initEnd > -1) {
  let oldInit = initKathaFunc.substring(0, initEnd);
  
  let newInit = oldInit.replace(
    'let currentKatha = null, playing = false;',
    'let currentKatha = null, playing = false;\n  let audioPlayer = new Audio();\n  audioPlayer.onended = () => { playing = false; updateMiniPlayerUI(); };'
  );
  
  // Replace the mini play button event listener
  newInit = newInit.replace(
    /miniPlayBtn\.addEventListener\('click',\s*\(\)\s*=>\s*\{[\s\S]*?\}\);/,
    `miniPlayBtn.addEventListener('click', () => {
    if(!currentKatha) return;
    if(playing){
      audioPlayer.pause();
      playing = false;
    }else{
      audioPlayer.play();
      playing = true;
    }
    updateMiniPlayerUI();
  });
  
  function updateMiniPlayerUI() {
    miniPlayBtn.textContent = playing ? '⏸' : '▶';
    miniPlayBtn.classList.toggle('playing', playing);
  }`
  );
  
  // Replace playKatha function
  newInit = newInit.replace(
    /function playKatha\(k\)[\s\S]*?miniPlayer\?\.classList\.remove\('hidden'\);\n\s*\}/,
    `function playKatha(k){
    if (currentKatha && currentKatha.id === k.id) {
       if(playing) { audioPlayer.pause(); playing = false; }
       else { audioPlayer.play(); playing = true; }
       updateMiniPlayerUI();
       return;
    }
    currentKatha = k;
    playing = true;
    audioPlayer.src = k.url;
    audioPlayer.play();
    document.getElementById('mini-thumb').textContent = k.emoji;
    document.getElementById('mini-title').textContent = k.title;
    document.getElementById('mini-sub').textContent = \`Episode 1 • \${k.ep} एपिसोड\`;
    miniPlayer?.classList.remove('hidden');
    updateMiniPlayerUI();
  }`
  );
  
  code = code.replace(oldInit, newInit);
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('Audio logic injected!');
