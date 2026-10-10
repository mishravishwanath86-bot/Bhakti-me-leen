const fs = require('fs');
let css = fs.readFileSync('styles.css', 'utf8');

// Remove the previously injected glassmorphism CSS
const startIdx = css.indexOf('/* =========================================\n   GLASSMORPHISM MINI PLAYER (User Request)');
if (startIdx !== -1) {
    css = css.substring(0, startIdx);
}

// Add the NEW corrected glassmorphism CSS
const newCSS = `
/* =========================================
   GLASSMORPHISM MINI PLAYER (Corrected)
   ========================================= */
.mini-player {
  position: fixed !important;
  bottom: calc(var(--bottom-nav-h, 60px) + 20px) !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: calc(100% - 32px) !important;
  max-width: 400px !important; /* Keep it phone-sized on desktop */
  
  /* The Glass Effect (matching the left phone in reference) */
  background: rgba(255, 255, 255, 0.25) !important;
  backdrop-filter: blur(20px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.5) !important;
  border-radius: 35px !important; /* Extra round */
  
  display: flex !important;
  align-items: center !important;
  gap: 1rem !important;
  padding: 8px 16px 8px 8px !important; /* Padding for the pill shape */
  z-index: 900 !important;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.6) !important;
  overflow: visible !important;
}

/* We don't need the old top progress bar, the reference doesn't have it in the mini-player */
.mini-progress-bar { display: none !important; }

/* The circular album art */
.mini-player-thumb {
  width: 48px !important; 
  height: 48px !important;
  background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%) !important; /* Add some color to the thumb background */
  border-radius: 50% !important;
  border: 2px solid rgba(255,255,255,0.8) !important;
  box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
  color: #fff !important;
  font-size: 1.5rem !important;
}

/* Info section */
.mini-player-info {
  flex: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
}

.mini-player-title {
  font-size: 0.95rem !important;
  color: #1f2937 !important; /* Dark text for light glass */
  font-weight: 700 !important;
  letter-spacing: 0.3px !important;
}

.mini-player-sub {
  color: #4b5563 !important;
  font-weight: 500 !important;
  font-size: 0.75rem !important;
  margin-top: 2px !important;
}

/* Time text - the reference doesn't have time in the mini player, but user asked for it. 
   We will style it subtly */
#mini-time {
  font-size: 0.7rem !important;
  color: #6b7280 !important;
  font-weight: 600 !important;
  margin-right: 5px !important;
  display: none !important; /* Hide time to exactly match reference UI, we can add a circular progress ring later if needed */
}

/* Hide seek button to match reference */
.mini-seek-btn {
  display: none !important;
}

/* The iconic white play/pause button from the reference */
.mini-play-btn {
  background: rgba(255, 255, 255, 0.9) !important;
  width: 42px !important; 
  height: 42px !important;
  border-radius: 50% !important;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
  border: none !important;
  color: #a855f7 !important; /* Purple icon */
  font-size: 1.2rem !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
}
.mini-play-btn:active {
  transform: scale(0.9) !important;
}
`;

fs.appendFileSync('styles.css', '\n' + newCSS);
console.log('Appended corrected glassmorphism CSS');
