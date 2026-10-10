import re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Update MediaRouter in app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_media_router = """window.isPlayerVideoModeActive = false;

window.togglePlayerVideoMode = function() {
  window.isPlayerVideoModeActive = !window.isPlayerVideoModeActive;
  window.updatePlayerVideoVisibility();
  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof playSoundEffect === 'function') playSoundEffect('correct');
};

window.updatePlayerVideoVisibility = function() {
  const ytContainer = document.getElementById('glass-youtube-container');
  const artRing = document.querySelector('.classic-artwork-ring');
  const toggleBtn = document.getElementById('glass-video-toggle-btn');
  const toggleText = document.getElementById('glass-video-toggle-text');
  const toggleIcon = document.getElementById('glass-video-toggle-icon');
  const toggleContainer = document.getElementById('glass-video-toggle-container');

  if (!window.MediaRouter || window.MediaRouter.activeMode !== 'youtube') {
    if (toggleContainer) toggleContainer.style.display = 'none';
    if (artRing) artRing.style.display = '';
    if (ytContainer) {
      ytContainer.style.display = 'none';
      ytContainer.style.position = 'relative';
      ytContainer.style.top = '0';
      ytContainer.style.left = '0';
    }
    return;
  }

  // Active mode is YouTube stream
  if (toggleContainer) toggleContainer.style.display = 'flex';

  if (window.isPlayerVideoModeActive) {
    // Show Full Video View
    if (artRing) artRing.style.display = 'none';
    if (ytContainer) {
      ytContainer.style.display = 'block';
      ytContainer.style.position = 'relative';
      ytContainer.style.top = '0';
      ytContainer.style.left = '0';
      ytContainer.style.width = '100%';
      ytContainer.style.maxWidth = '320px';
      ytContainer.style.height = 'auto';
      ytContainer.style.aspectRatio = '16/9';
      ytContainer.style.opacity = '1';
      ytContainer.style.pointerEvents = 'auto';
    }
    if (toggleBtn) {
      toggleBtn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      toggleBtn.style.color = '#1A0B2E';
    }
    if (toggleText) toggleText.textContent = '🎵 केवल ऑडियो सुनें (Audio Only)';
    if (toggleIcon) toggleIcon.textContent = '🎵';
  } else {
    // Pure Audio Mode (Default) - Show Artwork & hide video visually while audio plays
    if (artRing) artRing.style.display = '';
    if (ytContainer) {
      // Keep iframe alive so sound plays, but hide visually
      ytContainer.style.display = 'block';
      ytContainer.style.position = 'absolute';
      ytContainer.style.top = '-9999px';
      ytContainer.style.left = '-9999px';
      ytContainer.style.width = '1px';
      ytContainer.style.height = '1px';
      ytContainer.style.opacity = '0.01';
      ytContainer.style.pointerEvents = 'none';
    }
    if (toggleBtn) {
      toggleBtn.style.background = 'rgba(248,200,59,0.15)';
      toggleBtn.style.color = '#FDE68A';
    }
    if (toggleText) toggleText.textContent = '🎬 वीडियो देखें (Watch Video)';
    if (toggleIcon) toggleIcon.textContent = '🎬';
  }
};

window.MediaRouter = {
  activeMode: null, // 'local' | 'youtube' | null
  currentYouTubeId: null,
  isYouTubePaused: false,
  playbackCurrentTime: 0,
  playbackDuration: 300,
  timelineInterval: null,

  isYouTubeUrl(url) {
    if (!url || typeof url !== 'string') return false;
    const u = url.trim();
    return /(?:youtube\\.com\\/(?:[^\\/]+\\/.+\\/|(?:v|e(?:mbed)?)\\/|.*[?&]v=)|youtu\\.be\\/)/i.test(u);
  },

  getYouTubeVideoId(url) {
    if (!url || typeof url !== 'string') return null;
    const match = url.trim().match(/(?:youtu\\.be\\/|youtube\\.com\\/(?:embed\\/|v\\/|watch\\?v=|watch\\?.+&v=))([\\w-]{11})/i);
    return match ? match[1] : null;
  },

  getMediaType(url) {
    if (!url || typeof url !== 'string' || url.trim() === '') return 'none';
    if (this.isYouTubeUrl(url)) return 'youtube';
    return 'local';
  },

  destroyYouTubePlayer() {
    const containers = [
      document.getElementById('glass-youtube-container'),
      document.getElementById('reader-youtube-container')
    ];
    containers.forEach(c => {
      if (c) {
        c.innerHTML = '';
        c.style.display = 'none';
        c.style.position = 'relative';
        c.style.top = '0';
        c.style.left = '0';
      }
    });

    const artRing = document.querySelector('.classic-artwork-ring');
    if (artRing) artRing.style.display = '';

    const toggleContainer = document.getElementById('glass-video-toggle-container');
    if (toggleContainer) toggleContainer.style.display = 'none';

    this.currentYouTubeId = null;
    this.isYouTubePaused = false;
    window.isPlayerVideoModeActive = false;

    if (this.timelineInterval) {
      clearInterval(this.timelineInterval);
      this.timelineInterval = null;
    }
    if (this.activeMode === 'youtube') {
      this.activeMode = null;
    }
  },

  stopLocalAudio() {
    if (window.coreAudioElement) {
      window.coreAudioElement.pause();
    }
    if (typeof readerAudio !== 'undefined' && readerAudio) {
      readerAudio.pause();
    }
    if (typeof audioPlayerObj !== 'undefined' && audioPlayerObj) {
      audioPlayerObj.pause();
    }
    if (typeof updateAllPlayButtons === 'function') {
      updateAllPlayButtons(false);
    }
  },

  loadYouTubePlayer(url, containerId, meta) {
    meta = meta || {};
    const videoId = this.getYouTubeVideoId(url);
    if (!videoId) {
      console.warn("Invalid YouTube video URL:", url);
      if (typeof showToast === 'function') showToast("⚠️ अमान्य यूट्यूब वीडियो लिंक");
      return false;
    }

    // 1. Stop local audio
    this.stopLocalAudio();

    // 2. Clear previous YouTube embed
    this.destroyYouTubePlayer();

    this.activeMode = 'youtube';
    this.currentYouTubeId = videoId;
    this.isYouTubePaused = false;
    window.isPlayerVideoModeActive = false; // Pure Audio by default!

    const container = document.getElementById(containerId);
    if (container) {
      container.innerHTML = `
        <div class="youtube-player-wrapper" style="width:100%; height:100%; position:relative;">
          <iframe 
            id="${containerId}-iframe"
            src="https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&enablejsapi=1&rel=0&playsinline=1" 
            title="${meta.title || 'YouTube Devotional Stream'}"
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen
            style="width:100%; height:100%; border-radius:18px; border:none; display:block;">
          </iframe>
        </div>
      `;

      // Apply initial Pure Audio visibility
      window.updatePlayerVideoVisibility();
    } else {
      console.error(`MediaRouter error: Target container #${containerId} not found in DOM`);
      if (typeof showToast === 'function') showToast("⚠️ प्लेयर कंटेनर उपलब्ध नहीं है");
      return false;
    }

    // Update Mini player text if available
    const miniTitle = document.getElementById('glass-mini-title');
    if (miniTitle && meta.title) miniTitle.textContent = meta.title;
    const miniDeity = document.getElementById('glass-mini-deity');
    if (miniDeity && meta.deity) miniDeity.textContent = meta.deity;
    const miniTime = document.getElementById('glass-mini-time');
    if (miniTime) miniTime.textContent = '▶ भक्ति ऑडियो';

    if (typeof updateAllPlayButtons === 'function') {
      updateAllPlayButtons(true);
    }

    if (typeof showToast === 'function') {
      showToast(`🎧 प्रारंभ: ${meta.title || 'भक्ति रस'}`);
    }

    return true;
  },

  playRecord(record, containerType) {
    containerType = containerType || 'glass';
    if (!record) return;
    const url = record.audio_url || record.audio || record.video_url || record.src;
    const mType = this.getMediaType(url);

    // Update modal metadata
    const modalTitle = document.getElementById('glass-modal-title');
    if (modalTitle) modalTitle.textContent = record.title || record.name;
    const modalSub = document.getElementById('glass-modal-sub');
    if (modalSub) modalSub.textContent = `${record.deity_name_hi || record.deity_id || record.deity || 'भक्ति रस'} • ${mType === 'youtube' ? 'पावन ऑडियो (YouTube)' : 'पावन ऑडियो'}`;

    const lyricsBody = document.getElementById('glass-lyrics-body') || document.getElementById('glass-lyrics-content');
    if (lyricsBody) {
      const text = record.content || record.text || record.short_description || 'पावन पंक्तियाँ एवं भावार्थ...';
      lyricsBody.innerHTML = `<div style="white-space:pre-line;">${text}</div>`;
    }

    if (mType === 'youtube') {
      const containerId = containerType === 'reader' ? 'reader-youtube-container' : 'glass-youtube-container';
      
      const success = this.loadYouTubePlayer(url, containerId, {
        title: record.title || record.name,
        deity: record.deity_id || record.deity
      });

      if (success && containerType === 'glass') {
        openGlassPlayer();
      }

      if (typeof updateMiniPlayerDock === 'function') {
        updateMiniPlayerDock(record, true);
      }
    } else if (mType === 'local') {
      this.destroyYouTubePlayer();
      this.activeMode = 'local';

      const artRing = document.querySelector('.classic-artwork-ring');
      if (artRing) artRing.style.display = '';

      const toggleContainer = document.getElementById('glass-video-toggle-container');
      if (toggleContainer) toggleContainer.style.display = 'none';

      if (window.coreAudioElement && url) {
        window.coreAudioElement.src = url;
        window.coreAudioElement.load();
        window.coreAudioElement.play().then(() => {
          if (typeof updateAllPlayButtons === 'function') updateAllPlayButtons(true);
          window.activeAudioRecord = record;
          if (typeof updateMiniPlayerDock === 'function') updateMiniPlayerDock(record, true);
        }).catch(e => {
          console.warn("Autoplay notice:", e);
        });

        if (containerType === 'glass') {
          openGlassPlayer();
        }
      }
    } else {
      if (typeof showToast === 'function') showToast("ℹ️ कोई ऑडियो उपलब्ध नहीं है");
    }
  },

  updatePlayIcons(isPlaying) {
    if (typeof updateAllPlayButtons === 'function') {
      updateAllPlayButtons(isPlaying);
    }
  }
};"""

mr_pattern = r'window\.MediaRouter\s*=\s*\{[\s\S]*?\n\};'
if re.search(mr_pattern, js):
    js = re.sub(mr_pattern, lambda m: new_media_router, js, count=1)
    print("✓ Successfully replaced MediaRouter with Audio-Only default & Video Switcher!")
else:
    print("⚠️ Pattern match failed!")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ app.js updated successfully!")
