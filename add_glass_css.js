const fs = require('fs');
let css = fs.readFileSync('styles.css', 'utf8');

const glassCSS = `
/* =========================================
   GLASSMORPHISM MINI PLAYER (User Request)
   ========================================= */
.mini-player {
  position: fixed !important;
  bottom: calc(var(--bottom-nav-h, 60px) + 15px) !important; 
  left: 12px !important; 
  right: 12px !important;
  background: rgba(45, 10, 45, 0.65) !important; /* Deep glass tint */
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-radius: 22px !important;
  display: flex !important;
  align-items: center !important;
  gap: 0.6rem !important;
  padding: 0.6rem 0.8rem 0.6rem 0.6rem !important;
  z-index: 900 !important;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.2) !important;
  overflow: hidden !important; /* Keep progress bar inside borders */
}

/* Progress bar inside the glass container at the absolute bottom */
.mini-progress-bar {
  top: auto !important;
  bottom: 0 !important;
  height: 3px !important;
  background: rgba(255,255,255,0.1) !important;
}
.mini-progress-fill {
  background: linear-gradient(90deg, #a855f7, #ec4899) !important;
  box-shadow: 0 0 8px rgba(236, 72, 153, 0.8) !important;
}

.mini-player-thumb {
  width: 44px !important; 
  height: 44px !important;
  background: rgba(255,255,255,0.1) !important;
  border-radius: 50% !important;
  border: 1px solid rgba(255,255,255,0.15) !important;
  box-shadow: inset 0 2px 4px rgba(255,255,255,0.1) !important;
}

.mini-player-title {
  font-size: 0.9rem !important;
  color: #fff !important;
  font-weight: 600 !important;
  text-shadow: 0 1px 2px rgba(0,0,0,0.5) !important;
}

.mini-player-sub {
  color: rgba(255,255,255,0.6) !important;
  font-weight: 400 !important;
}

#mini-time {
  font-size: 0.65rem !important;
  color: rgba(255,255,255,0.7) !important;
  min-width: 60px !important;
  text-align: right !important;
  font-variant-numeric: tabular-nums !important;
}

.mini-seek-btn {
  background: transparent !important;
  color: rgba(255,255,255,0.8) !important;
}
.mini-seek-btn:active {
  background: rgba(255,255,255,0.1) !important;
}

.mini-play-btn {
  background: linear-gradient(135deg, #a855f7 0%, #7e22ce 100%) !important;
  width: 44px !important; 
  height: 44px !important;
  box-shadow: 0 4px 12px rgba(168, 85, 247, 0.4), inset 0 1px 0 rgba(255,255,255,0.3) !important;
  border: 1px solid rgba(255,255,255,0.1) !important;
}
.mini-play-btn.playing {
  background: linear-gradient(135deg, #ec4899 0%, #be185d 100%) !important;
  box-shadow: 0 4px 12px rgba(236, 72, 153, 0.4), inset 0 1px 0 rgba(255,255,255,0.3) !important;
}
`;

fs.appendFileSync('styles.css', '\n' + glassCSS);
console.log('Appended glassmorphism CSS');
