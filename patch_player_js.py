import re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

app_js_path = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app\app.js")

with open(app_js_path, 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# Replace MediaRouter implementation in app.js with the advanced player controller
new_media_router_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🎬 NEXT-GEN ADVANCED DUAL-MODE MEDIA ROUTER & TIMELINE CONTROLLER
// ══════════════════════════════════════════════════════════════════════════════

window.MediaRouter = {
  activeMode: null, // 'local' | 'youtube' | null
  currentYouTubeId: null,
  activeRecord: null,
  isUserVideoView: false, // false = Audio Mode (Default), true = Video Mode
  playbackDuration: 300,
  playbackCurrentTime: 0,
  timelineInterval: null,
  isDraggingSeekbar: false,

  isYouTubeUrl(url) {
    if (!url || typeof url !== 'string') return false;
    const u = url.trim();
    return /(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)/i.test(u);
  },

  getYouTubeVideoId(url) {
    if (!url || typeof url !== 'string') return null;
    const match = url.trim().match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([\w-]{11})/i);
    return match ? match[1] : null;
  },

  getMediaType(url) {
    if (!url || typeof url !== 'string' || url.trim() === '') return 'none';
    if (this.isYouTubeUrl(url)) return 'youtube';
    return 'local';
  },

  getDeityArtwork(deityId) {
    const d = (deityId || '').toLowerCase();
    if (d.includes('hanuman')) return 'assets/deity_hanuman.jpg';
    if (d.includes('shiv')) return 'assets/deity_shiv.jpg';
    if (d.includes('durga') || d.includes('kali') || d.includes('ambe')) return 'assets/deity_durga.jpg';
    if (d.includes('krishna') || d.includes('radha')) return 'assets/deity_krishna.jpg';
    if (d.includes('ram')) return 'assets/deity_ramayana.jpg';
    if (d.includes('vishnu') || d.includes('narayan')) return 'assets/deity_vishnu.jpg';
    if (d.includes('lakshmi')) return 'assets/deity_lakshmi.jpg';
    if (d.includes('ganesh')) return 'assets/deity_ganesh.jpg';
    if (d.includes('saraswati') || d.includes('sharda')) return 'assets/deity_saraswati.jpg';
    if (d.includes('khatu') || d.includes('shyam')) return 'assets/speaker_khatushyam.jpg';
    if (d.includes('sai')) return 'assets/speaker_indresh.jpg';
    return 'assets/app_logo_circle.png';
  },

  destroyYouTubePlayer() {
    const c = document.getElementById('glass-youtube-container');
    if (c) {
      c.innerHTML = '';
      c.style.display = 'none';
    }
    this.currentYouTubeId = null;
    if (this.activeMode === 'youtube') this.activeMode = null;
  },

  stopLocalAudio() {
    if (window.coreAudioElement) {
      window.coreAudioElement.pause();
    }
  },

  formatTime(secs) {
    if (isNaN(secs) || secs < 0) return '00:00';
    const m = Math.floor(secs / 60);
    const s = Math.floor(secs % 60);
    return `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
  },

  startTimelineTicker() {
    if (this.timelineInterval) clearInterval(this.timelineInterval);
    this.timelineInterval = setInterval(() => {
      this.updateTimelineTick();
    }, 500);
  },

  updateTimelineTick() {
    if (this.isDraggingSeekbar) return;

    if (this.activeMode === 'local' && window.coreAudioElement) {
      const audio = window.coreAudioElement;
      if (!isNaN(audio.duration) && audio.duration > 0) {
        this.playbackDuration = audio.duration;
      }
      this.playbackCurrentTime = audio.currentTime || 0;
      this.syncUI();
    } else if (this.activeMode === 'youtube') {
      // Simulate/approximate elapsed time for smooth scrubber
      if (this.playbackCurrentTime < this.playbackDuration) {
        this.playbackCurrentTime += 0.5;
        this.syncUI();
      }
    }
  },

  syncUI() {
    const curEl = document.getElementById('glass-modal-cur-time');
    const totEl = document.getElementById('glass-modal-tot-time');
    const seekbar = document.getElementById('glass-modal-seekbar');

    if (curEl) curEl.textContent = this.formatTime(this.playbackCurrentTime);
    if (totEl) totEl.textContent = this.formatTime(this.playbackDuration);

    if (seekbar && this.playbackDuration > 0) {
      const pct = (this.playbackCurrentTime / this.playbackDuration) * 100;
      seekbar.value = Math.min(100, Math.max(0, pct));
    }
  },

  seekTo(targetSeconds) {
    this.playbackCurrentTime = Math.max(0, Math.min(targetSeconds, this.playbackDuration));
    if (this.activeMode === 'local' && window.coreAudioElement) {
      window.coreAudioElement.currentTime = this.playbackCurrentTime;
    } else if (this.activeMode === 'youtube') {
      const iframe = document.querySelector('#glass-youtube-container iframe');
      if (iframe && iframe.contentWindow) {
        iframe.contentWindow.postMessage(JSON.stringify({
          event: 'command',
          func: 'seekTo',
          args: [this.playbackCurrentTime, true]
        }), '*');
      }
    }
    this.syncUI();
  },

  skipSeconds(delta) {
    this.seekTo(this.playbackCurrentTime + delta);
    if (typeof showToast === 'function') {
      showToast(`${delta > 0 ? '⏩ +10s आगे' : '⏪ -10s पीछे'}`);
    }
  },

  playRecord(record) {
    if (!record) return;
    this.activeRecord = record;
    window.activeAudioRecord = record;

    const url = record.audio_url || record.audio || record.video_url || record.src;
    const mType = this.getMediaType(url);

    // Setup Track Metadata
    const modalTitle = document.getElementById('glass-modal-title');
    if (modalTitle) modalTitle.textContent = record.title || 'पावन संकीर्तन';

    const deityBadge = document.getElementById('glass-modal-deity-badge');
    if (deityBadge) {
      const dName = record.deity_name_hi || record.deity_id || 'भक्ति रस';
      const cType = record.content_type === 'aarti' ? 'नित्य आरती' : (record.content_type === 'chalisa' ? 'चालीसा' : 'पावन भजन');
      deityBadge.textContent = `✨ ${dName} • ${cType}`;
    }

    // Set Centerpiece Artwork
    const modalImg = document.getElementById('glass-modal-img');
    const artworkSrc = this.getDeityArtwork(record.deity_id);
    if (modalImg) modalImg.src = artworkSrc;

    // Load Lyrics Body
    const lyricsBody = document.getElementById('glass-lyrics-body');
    if (lyricsBody) {
      const text = record.content || record.text || record.short_description || 'पावन पंक्तियाँ एवं भावार्थ लोड हो रहे हैं...';
      lyricsBody.innerHTML = `<div style="white-space:pre-line;">${text}</div>`;
    }

    // Reset scrubber & duration
    this.playbackCurrentTime = 0;
    this.playbackDuration = (record.duration_seconds && record.duration_seconds > 0) ? record.duration_seconds : 300;
    this.syncUI();

    // Default to Audio Mode (Clean Artwork)
    this.isUserVideoView = false;
    this.updateMediaViewMode();

    if (mType === 'youtube') {
      this.stopLocalAudio();
      this.destroyYouTubePlayer();
      this.activeMode = 'youtube';

      const videoId = this.getYouTubeVideoId(url);
      this.currentYouTubeId = videoId;

      const container = document.getElementById('glass-youtube-container');
      if (container && videoId) {
        container.innerHTML = `
          <iframe 
            src="https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&enablejsapi=1&rel=0" 
            title="${record.title || 'Devotional Media'}"
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen>
          </iframe>
        `;
      }

      this.startTimelineTicker();
      this.updatePlayIcons(true);
      openGlassPlayer();

      if (typeof updateMiniPlayerDock === 'function') {
        updateMiniPlayerDock(record, true);
      }
    } else if (mType === 'local') {
      this.destroyYouTubePlayer();
      this.activeMode = 'local';

      if (window.coreAudioElement && url) {
        window.coreAudioElement.src = url;
        window.coreAudioElement.load();
        window.coreAudioElement.play().then(() => {
          this.updatePlayIcons(true);
        }).catch(e => console.warn(e));

        this.startTimelineTicker();
        openGlassPlayer();

        if (typeof updateMiniPlayerDock === 'function') {
          updateMiniPlayerDock(record, true);
        }
      }
    }

    if (typeof showToast === 'function') {
      showToast(`▶ प्रारंभ: ${record.title || 'भक्ति संगीत'}`);
    }
  },

  updateMediaViewMode() {
    const videoBox = document.getElementById('glass-youtube-container');
    const artworkBox = document.getElementById('glass-artwork-container');
    const toggleBtnText = document.getElementById('glass-mode-toggle-text');

    if (this.isUserVideoView && this.activeMode === 'youtube') {
      if (videoBox) videoBox.style.display = 'block';
      if (artworkBox) artworkBox.style.display = 'none';
      if (toggleBtnText) toggleBtnText.textContent = '🎵 ऑडियो मोड';
    } else {
      if (videoBox) videoBox.style.display = 'none';
      if (artworkBox) artworkBox.style.display = 'flex';
      if (toggleBtnText) toggleBtnText.textContent = '🎬 वीडियो देखें';
    }
  },

  toggleMediaView() {
    if (this.activeMode !== 'youtube') {
      if (typeof showToast === 'function') showToast("ℹ️ यह रचना केवल ऑडियो प्रारूप में उपलब्ध है");
      return;
    }
    this.isUserVideoView = !this.isUserVideoView;
    this.updateMediaViewMode();
    if (typeof showToast === 'function') {
      showToast(this.isUserVideoView ? "🎬 वीडियो दृश्य सक्रिय" : "🎵 ऑडियो दृश्य सक्रिय");
    }
  },

  updatePlayIcons(isPlaying) {
    const playIcon = document.getElementById('glass-modal-play-icon');
    if (playIcon) playIcon.textContent = isPlaying ? '⏸' : '▶';

    const miniPlayBtn = document.getElementById('mini-player-play-btn');
    if (miniPlayBtn) miniPlayBtn.textContent = isPlaying ? '⏸' : '▶';

    if (typeof updateAllPlayButtons === 'function') {
      updateAllPlayButtons(isPlaying);
    }
  }
};

// Global Handlers
function togglePlayerMediaView() {
  window.MediaRouter.toggleMediaView();
}

function onSeekbarInput(val) {
  window.MediaRouter.isDraggingSeekbar = true;
  const dur = window.MediaRouter.playbackDuration || 300;
  const targetTime = (parseFloat(val) / 100) * dur;
  const curEl = document.getElementById('glass-modal-cur-time');
  if (curEl) curEl.textContent = window.MediaRouter.formatTime(targetTime);
}

function onSeekbarChange(val) {
  window.MediaRouter.isDraggingSeekbar = false;
  const dur = window.MediaRouter.playbackDuration || 300;
  const targetTime = (parseFloat(val) / 100) * dur;
  window.MediaRouter.seekTo(targetTime);
}

function skipAudioSeconds(delta) {
  window.MediaRouter.skipSeconds(delta);
}

function openGlassPlayer() {
  const modal = document.getElementById('glass-full-player-modal');
  if (modal) {
    modal.style.display = 'flex';
    modal.style.opacity = '1';
    modal.style.pointerEvents = 'auto';
  }
}

function closeGlassPlayer() {
  const modal = document.getElementById('glass-full-player-modal');
  if (modal) {
    modal.style.display = 'none';
  }
}

function toggleLyricsDrawer() {
  const content = document.getElementById('glass-lyrics-content');
  const txt = document.getElementById('glass-lyrics-tab-text');
  if (content) {
    const isOpen = content.style.display === 'block';
    content.style.display = isOpen ? 'none' : 'block';
    if (txt) {
      txt.textContent = isOpen ? 'पाठ एवं भावार्थ देखें (Lyrics) ⌃' : 'पाठ एवं भावार्थ छिपाएं (Lyrics) ⌄';
    }
  }
}

function togglePlayKatha() {
  if (window.MediaRouter.activeMode === 'local' && window.coreAudioElement) {
    if (window.coreAudioElement.paused) {
      window.coreAudioElement.play();
      window.MediaRouter.updatePlayIcons(true);
    } else {
      window.coreAudioElement.pause();
      window.MediaRouter.updatePlayIcons(false);
    }
  } else if (window.MediaRouter.activeMode === 'youtube') {
    const iframe = document.querySelector('#glass-youtube-container iframe');
    if (iframe && iframe.contentWindow) {
      // Toggle play/pause via postMessage
      iframe.contentWindow.postMessage(JSON.stringify({
        event: 'command',
        func: 'pauseVideo',
        args: []
      }), '*');
    }
  }
}
"""

# Append to app.js
with open(app_js_path, 'a', encoding='utf-8') as f:
    f.write("\n" + new_media_router_js)

print("✓ Injected advanced MediaRouter and Timeline Controller into app.js")
