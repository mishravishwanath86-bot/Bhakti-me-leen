import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Unified MediaRouter implementation
unified_media_router = """window.MediaRouter = {
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
      }
    });

    const artRing = document.querySelector('.classic-artwork-ring');
    if (artRing) artRing.style.display = '';

    this.currentYouTubeId = null;
    this.isYouTubePaused = false;
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

    // 1. Stop local audio (never allow both to play simultaneously)
    this.stopLocalAudio();

    // 2. Clear previous YouTube embed
    this.destroyYouTubePlayer();

    this.activeMode = 'youtube';
    this.currentYouTubeId = videoId;
    this.isYouTubePaused = false;

    const container = document.getElementById(containerId);
    if (container) {
      container.style.display = 'block';
      container.innerHTML = `
        <div class="youtube-player-wrapper" style="width:100%; height:100%; position:relative;">
          <iframe 
            id="${containerId}-iframe"
            src="https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&enablejsapi=1&rel=0&playsinline=1" 
            title="${meta.title || 'YouTube Devotional Video'}"
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen
            style="width:100%; height:100%; border-radius:18px; border:none; display:block;">
          </iframe>
        </div>
      `;

      // Hide static deity artwork ring when YouTube stream is mounted
      if (containerId === 'glass-youtube-container') {
        const artRing = document.querySelector('.classic-artwork-ring');
        if (artRing) artRing.style.display = 'none';
      }
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
    if (miniTime) miniTime.textContent = '▶ YouTube वीडियो';

    if (typeof updateAllPlayButtons === 'function') {
      updateAllPlayButtons(true);
    }

    if (typeof showToast === 'function') {
      showToast(`🎬 प्रारंभ: ${meta.title || 'भक्ति रस'}`);
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
    if (modalSub) modalSub.textContent = `${record.deity_name_hi || record.deity_id || record.deity || 'भक्ति रस'} • ${mType === 'youtube' ? 'YouTube HD Stream' : 'पावन ऑडियो'}`;

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
      if (typeof showToast === 'function') showToast("ℹ️ कोई ऑडियो/वीडियो उपलब्ध नहीं है");
    }
  },

  updatePlayIcons(isPlaying) {
    if (typeof updateAllPlayButtons === 'function') {
      updateAllPlayButtons(isPlaying);
    }
  }
};"""

# 1. Replace first MediaRouter block at top
mr1_pattern = r'window\.MediaRouter\s*=\s*\{[\s\S]*?\n\};'
js = re.sub(mr1_pattern, lambda m: unified_media_router, js, count=1)

# 2. Replace second MediaRouter block (around line 12600)
# Look for the second occurrence
s_idx = js.find('window.MediaRouter = {', len(unified_media_router) + 50)
if s_idx != -1:
    e_idx = js.find('// Global Handlers', s_idx)
    if e_idx != -1:
        js = js[:s_idx] + "// (Consolidated with main window.MediaRouter)\n\n" + js[e_idx:]
        print("✓ Removed duplicate second MediaRouter block and consolidated into primary MediaRouter")

# 3. Ensure togglePlayKatha and open/closeGlassPlayer are clean
toggle_func = """function togglePlayKatha() {
  if (window.MediaRouter && window.MediaRouter.activeMode === 'youtube') {
    const iframe = document.querySelector('#glass-youtube-container iframe, #reader-youtube-container iframe');
    if (iframe && iframe.contentWindow) {
      if (window.MediaRouter.isYouTubePaused) {
        iframe.contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
        window.MediaRouter.isYouTubePaused = false;
        updateAllPlayButtons(true);
      } else {
        iframe.contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
        window.MediaRouter.isYouTubePaused = true;
        updateAllPlayButtons(false);
      }
    }
    return;
  }

  const audio = window.coreAudioElement;
  if (!audio) return;
  if (!audio.paused) {
    audio.pause();
    updateAllPlayButtons(false);
  } else {
    audio.play().then(() => {
      updateAllPlayButtons(true);
    }).catch(e => {
      console.warn("Play error:", e);
    });
  }
}"""

open_close_funcs = """function openGlassPlayer() {
  const modal = document.getElementById('glass-full-player-modal');
  if (modal) {
    modal.classList.add('open');
    modal.style.display = 'flex';
    modal.style.opacity = '1';
    modal.style.pointerEvents = 'auto';
    modal.style.transform = 'translateY(0)';
  }
}

function closeGlassPlayer() {
  const modal = document.getElementById('glass-full-player-modal');
  if (modal) {
    modal.classList.remove('open');
    modal.style.display = 'none';
    modal.style.opacity = '0';
    modal.style.pointerEvents = 'none';
    modal.style.transform = 'translateY(100%)';
  }
  if (window.MediaRouter && window.MediaRouter.activeMode === 'youtube') {
    window.MediaRouter.destroyYouTubePlayer();
  }
}"""

# Update open/closeGlassPlayer at the end of app.js
if 'function openGlassPlayer()' in js:
    js = re.sub(r'function openGlassPlayer\(\)\s*\{[\s\S]*?function closeGlassPlayer\(\)\s*\{[\s\S]*?\n\}', lambda m: open_close_funcs, js)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Successfully unified MediaRouter and player handlers in app.js!")
