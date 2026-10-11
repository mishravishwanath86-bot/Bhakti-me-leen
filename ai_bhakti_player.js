// ====================================================================
// BHAKTI APP: AI BHAKTI SINGING & DEVOTIONAL AUDIO PLAYER (एआई भक्ति स्वर)
// 100% On-Demand, Zero Cost Free Mode, Smart Caching & Temple Ambiance
// ====================================================================

(function() {
  'use strict';

  window.AiBhaktiPlayer = {
    // Current Active Content
    currentContent: null,    // { id, title, text, type, deity }
    currentVoice: 'male',    // 'male' (Madhur) or 'female' (Swara)
    currentSpeed: 1.0,       // 0.75, 1.0, 1.25, 1.5
    isLooping: false,
    jaapCount: 0,
    targetJaapCount: 108,
    isTempleAmbianceOn: true,
    
    // Playback States
    isPlaying: false,
    isGenerating: false,
    audioInstance: null,
    
    // Web Audio Tanpura / Temple Drone Synthesizer
    audioCtx: null,
    tanpuraGain: null,
    oscillators: [],

    // Supported Speed Steps
    SPEEDS: [0.75, 1.0, 1.25, 1.5],

    init: function() {
      console.log('[AiBhaktiPlayer] Initializing AI Devotional Player Engine...');
      this.attachGlobalHooks();
    },

    // ─────────────────────────────────────────────────────────────────
    // 🪕 SACRED TEMPLE TANPURA AMBIANCE (सुर व संगीत संगत - शून्य डेटा खर्च)
    // ─────────────────────────────────────────────────────────────────
    initTempleDrone: function() {
      if (this.audioCtx) return;
      try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        this.audioCtx = new AudioContext();
        
        // Master Tanpura Gain Node
        this.tanpuraGain = this.audioCtx.createGain();
        this.tanpuraGain.gain.setValueAtTime(0.001, this.audioCtx.currentTime);

        // Low-pass warm filter (gives wooden temple tanpura tone)
        const filter = this.audioCtx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(450, this.audioCtx.currentTime);

        this.tanpuraGain.connect(filter);
        filter.connect(this.audioCtx.destination);

        // Indian classical devotional root: C# (138.59 Hz) and Pa (207.65 Hz)
        const freqs = [138.59, 207.65, 277.18];
        this.oscillators = [];

        freqs.forEach((freq, idx) => {
          const osc = this.audioCtx.createOscillator();
          osc.type = idx === 1 ? 'triangle' : 'sine';
          osc.frequency.setValueAtTime(freq, this.audioCtx.currentTime);

          // Gentle LFO for realistic tanpura pluck wave
          const lfo = this.audioCtx.createOscillator();
          lfo.frequency.setValueAtTime(0.2 + idx * 0.15, this.audioCtx.currentTime);
          const lfoGain = this.audioCtx.createGain();
          lfoGain.gain.setValueAtTime(0.04, this.audioCtx.currentTime);
          lfo.connect(lfoGain);

          const subGain = this.audioCtx.createGain();
          subGain.gain.setValueAtTime(0.035, this.audioCtx.currentTime);
          lfoGain.connect(subGain.gain);

          osc.connect(subGain);
          subGain.connect(this.tanpuraGain);

          osc.start();
          lfo.start();
          this.oscillators.push(osc);
        });
      } catch (e) {
        console.warn('[AiBhaktiPlayer] WebAudio drone unavailable:', e);
      }
    },

    startTempleDrone: function() {
      if (!this.isTempleAmbianceOn) return;
      this.initTempleDrone();
      if (!this.audioCtx || !this.tanpuraGain) return;
      if (this.audioCtx.state === 'suspended') {
        this.audioCtx.resume();
      }
      // Fade in smoothly over 1.2s
      const now = this.audioCtx.currentTime;
      this.tanpuraGain.gain.cancelScheduledValues(now);
      this.tanpuraGain.gain.setValueAtTime(this.tanpuraGain.gain.value, now);
      this.tanpuraGain.gain.linearRampToValueAtTime(0.12, now + 1.2);
    },

    stopTempleDrone: function() {
      if (!this.audioCtx || !this.tanpuraGain) return;
      // Fade out smoothly over 0.8s
      const now = this.audioCtx.currentTime;
      this.tanpuraGain.gain.cancelScheduledValues(now);
      this.tanpuraGain.gain.setValueAtTime(this.tanpuraGain.gain.value, now);
      this.tanpuraGain.gain.linearRampToValueAtTime(0.0001, now + 0.8);
    },

    toggleTempleDrone: function() {
      this.isTempleAmbianceOn = !this.isTempleAmbianceOn;
      const btn = document.getElementById('ai-drone-toggle-btn');
      if (btn) {
        btn.classList.toggle('active', this.isTempleAmbianceOn);
        btn.innerHTML = this.isTempleAmbianceOn
          ? '<span>🪕</span> तानपुरा संगत: चालू'
          : '<span>🪕</span> तानपुरा संगत: बंद';
      }
      if (this.isPlaying) {
        if (this.isTempleAmbianceOn) this.startTempleDrone();
        else this.stopTempleDrone();
      }
      this.showToast(this.isTempleAmbianceOn ? '🪕 मंदिर तानपुरा व सुर संगत सक्रिय' : '🪕 तानपुरा संगत शांत की गई');
    },

    // ─────────────────────────────────────────────────────────────────
    // 🎧 ON-DEMAND AUDIO GENERATION & PLAYBACK (जब Play दबे, तभी बने)
    // ─────────────────────────────────────────────────────────────────
    togglePlay: async function() {
      if (!this.currentContent) {
        this.showToast('⚠️ कोई सामग्री लोड नहीं है');
        return;
      }

      // 1. If currently playing -> PAUSE
      if (this.isPlaying && this.audioInstance) {
        this.audioInstance.pause();
        this.stopTempleDrone();
        this.isPlaying = false;
        this.updateUI();
        return;
      }

      // 2. If paused with existing audio instance -> RESUME
      if (!this.isPlaying && this.audioInstance && !this.audioInstance.ended) {
        try {
          await this.audioInstance.play();
          this.startTempleDrone();
          this.isPlaying = true;
          this.updateUI();
          if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
          return;
        } catch (e) {
          console.warn('[AiBhaktiPlayer] Resume failed, re-fetching:', e);
        }
      }

      // 3. Otherwise -> Fresh or Cached Fetch from Backend
      await this.requestAndPlayAudio();
    },

    requestAndPlayAudio: async function() {
      if (this.isGenerating) return;

      this.isGenerating = true;
      this.updateUI();

      const payload = {
        content_id: this.currentContent.id || 'current',
        text: this.currentContent.text || '',
        title: this.currentContent.title || 'दिव्य पाठ',
        content_type: this.currentContent.type || 'aarti',
        voice: this.currentVoice,
        speed: this.currentSpeed
      };

      try {
        const resp = await fetch('/api/ai-audio/generate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        const data = await resp.json();
        if (!data.success || !data.audio_url) {
          throw new Error(data.error || 'ऑडियो प्राप्त नहीं हो सका');
        }

        // Clean up previous audio instance
        if (this.audioInstance) {
          this.audioInstance.pause();
          this.audioInstance.src = '';
          this.audioInstance = null;
        }

        // Create new Audio element
        const audio = new Audio(data.audio_url);
        audio.playbackRate = this.currentSpeed;
        this.audioInstance = audio;

        // Wire event listeners
        audio.addEventListener('timeupdate', () => this.handleTimeUpdate());
        audio.addEventListener('ended', () => this.handleTrackEnded());
        audio.addEventListener('error', (e) => {
          console.error('[AiBhaktiPlayer] Audio error:', e);
          this.isGenerating = false;
          this.isPlaying = false;
          this.stopTempleDrone();
          this.updateUI();
          this.showToast('⚠️ ऑडियो प्लेबैक में त्रुटि आई');
        });

        // Start playback
        await audio.play();
        this.isPlaying = true;
        this.isGenerating = false;
        this.startTempleDrone();
        this.updateUI();

        if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
        if (data.cached) {
          this.showToast('⚡ पावन ऑडियो लोड हुआ (कैश से तुरंत)');
        } else {
          this.showToast('✨ AI दिव्य स्वर व संगीत सृजन पूर्ण हुआ!');
        }

      } catch (err) {
        console.error('[AiBhaktiPlayer] Request failed:', err);
        this.isGenerating = false;
        this.isPlaying = false;
        this.stopTempleDrone();
        this.updateUI();
        this.showToast('⚠️ ' + (err.message || 'ऑडियो सृजन असफल'));
      }
    },

    // ─────────────────────────────────────────────────────────────────
    // 🎛️ CONTROLS: SPEED, REPEAT, VOICE & SEEKING
    // ─────────────────────────────────────────────────────────────────
    cycleSpeed: function() {
      const idx = this.SPEEDS.indexOf(this.currentSpeed);
      const nextIdx = (idx + 1) % this.SPEEDS.length;
      this.currentSpeed = this.SPEEDS[nextIdx];

      if (this.audioInstance) {
        this.audioInstance.playbackRate = this.currentSpeed;
      }
      this.updateUI();
      this.showToast(`⚡ गायन गति: ${this.currentSpeed}x`);
    },

    toggleLoop: function() {
      this.isLooping = !this.isLooping;
      this.jaapCount = 0;
      if (this.audioInstance) {
        this.audioInstance.loop = this.isLooping;
      }
      this.updateUI();
      this.showToast(this.isLooping ? '🔁 १०८ बार निरंतर दिव्य जाप लूप सक्रिय' : '🔁 लूपिंग बंद की गई');
    },

    toggleVoice: function() {
      this.currentVoice = this.currentVoice === 'male' ? 'female' : 'male';
      const voiceLabel = this.currentVoice === 'male' ? 'ऋषि/पुजारी स्वर (मधुर)' : 'देवी/भक्ति स्वर (स्वरा)';
      this.showToast(`🪔 स्वर बदला गया: ${voiceLabel}`);

      // If already playing, re-generate in new voice
      if (this.isPlaying || this.audioInstance) {
        if (this.audioInstance) {
          this.audioInstance.pause();
          this.audioInstance = null;
        }
        this.isPlaying = false;
        this.stopTempleDrone();
        this.requestAndPlayAudio();
      } else {
        this.updateUI();
      }
    },

    seek: function(pct) {
      if (this.audioInstance && this.audioInstance.duration) {
        this.audioInstance.currentTime = (pct / 100) * this.audioInstance.duration;
      }
    },

    handleTimeUpdate: function() {
      if (!this.audioInstance || !this.audioInstance.duration) return;
      const cur = this.audioInstance.currentTime;
      const dur = this.audioInstance.duration;
      const pct = (cur / dur) * 100;

      const progressEl = document.getElementById('ai-audio-progress-bar');
      if (progressEl) progressEl.value = pct;

      const timeEl = document.getElementById('ai-audio-time-label');
      if (timeEl) {
        timeEl.textContent = `${this.formatTime(cur)} / ${this.formatTime(dur)}`;
      }
    },

    handleTrackEnded: function() {
      if (this.isLooping) {
        this.jaapCount++;
        const badge = document.getElementById('ai-jaap-count-badge');
        if (badge) badge.textContent = `${this.jaapCount}/108`;
        
        if (typeof incrementJaapCounter === 'function') incrementJaapCounter();
        if (typeof triggerFlowerShower === 'function') triggerFlowerShower();

        if (this.jaapCount < this.targetJaapCount) {
          if (this.audioInstance) this.audioInstance.play();
          return;
        }
      }

      this.isPlaying = false;
      this.stopTempleDrone();
      this.updateUI();
      this.showToast('🙏 दिव्य पाठ एवं श्रवण संपन्न हुआ');
    },

    formatTime: function(sec) {
      if (isNaN(sec) || !isFinite(sec)) return '00:00';
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
    },

    showToast: function(msg) {
      if (typeof window.showToast === 'function') {
        window.showToast(msg);
      } else {
        console.log('[AiBhaktiPlayer]', msg);
      }
    },

    // ─────────────────────────────────────────────────────────────────
    // 🎨 UI RENDERING & SYNCHRONIZATION
    // ─────────────────────────────────────────────────────────────────
    loadContent: function(contentObj) {
      if (!contentObj) return;

      // Stop previous playback if switching content
      if (this.audioInstance) {
        this.audioInstance.pause();
        this.audioInstance = null;
      }
      this.isPlaying = false;
      this.isGenerating = false;
      this.stopTempleDrone();

      let text = contentObj.text || '';
      if (!text && Array.isArray(contentObj.lines)) {
        text = contentObj.lines.map(l => (typeof l === 'object' ? (l.hindi || l.text || '') : l)).join('\n');
      }
      if (!text && contentObj.content) {
        text = contentObj.content;
      }
      if (!text || text.trim().length < 5) {
        const domEl = document.getElementById('reader-cosmic-content');
        if (domEl) {
          text = domEl.innerText.trim();
        }
      }

      this.currentContent = {
        id: contentObj.id || contentObj.key || contentObj.title,
        title: contentObj.title || contentObj.name || 'दिव्य पाठ',
        text: text,
        type: contentObj.type || contentObj.content_type || 'aarti',
        deity: contentObj.deity || 'सनातन'
      };

      this.updateUI();
    },

    updateUI: function() {
      const container = document.getElementById('ai-bhakti-audio-bar');
      if (!container) return;

      const playBtn = document.getElementById('ai-audio-play-btn');
      const voiceBtn = document.getElementById('ai-voice-toggle-btn');
      const speedBtn = document.getElementById('ai-speed-btn');
      const loopBtn = document.getElementById('ai-loop-btn');
      const statusPill = document.getElementById('ai-audio-status-pill');

      // Update Play Button State
      if (playBtn) {
        if (this.isGenerating) {
          playBtn.innerHTML = '<span>⏳</span> <span class="ai-btn-text">दिव्य स्वर सृजन हो रहा है...</span>';
          playBtn.classList.add('generating');
        } else if (this.isPlaying) {
          playBtn.innerHTML = '<span>⏸</span> <span class="ai-btn-text">विराम (Pause)</span>';
          playBtn.classList.remove('generating');
        } else {
          playBtn.innerHTML = '<span>▶</span> <span class="ai-btn-text">AI दिव्य पाठ / गायन सुनें</span>';
          playBtn.classList.remove('generating');
        }
      }

      // Update Voice Button
      if (voiceBtn) {
        voiceBtn.innerHTML = this.currentVoice === 'male'
          ? '<span>🪔</span> ऋषि/पुजारी स्वर (मधुर)'
          : '<span>🌸</span> देवी स्वर (स्वरा)';
      }

      // Update Speed Button
      if (speedBtn) {
        speedBtn.innerHTML = `<span>⚡</span> ${this.currentSpeed.toFixed(2)}x`;
      }

      // Update Loop Button
      if (loopBtn) {
        loopBtn.classList.toggle('active', this.isLooping);
        loopBtn.innerHTML = `<span>🔁</span> ${this.isLooping ? '१०८x जाप चालू' : 'लूप'}`;
      }

      // Update Status Pill
      if (statusPill) {
        if (this.isGenerating) {
          statusPill.innerHTML = '<span class="pulse-dot"></span> AI दिव्य सुर सृजन...';
          statusPill.style.color = '#F59E0B';
        } else if (this.isPlaying) {
          statusPill.innerHTML = '<span class="live-dot"></span> लाइव भक्ति श्रवण';
          statusPill.style.color = '#10B981';
        } else {
          statusPill.innerHTML = '<span>✨</span> प्ले करने पर AI गायन प्रारंभ होगा';
          statusPill.style.color = '#FDE68A';
        }
      }
    },

    // ─────────────────────────────────────────────────────────────────
    // 🔗 GLOBAL HOOKS INTO APP.JS (Automatic Content Binding)
    // ─────────────────────────────────────────────────────────────────
    attachGlobalHooks: function() {
      const self = this;

      // Wrap window.openReader if exists
      const origOpenReader = window.openReader;
      if (typeof origOpenReader === 'function') {
        window.openReader = function(key, fromPage) {
          const res = origOpenReader.apply(this, arguments);
          try {
            let item = (typeof key === 'object') ? key : (window.CONTENT && window.CONTENT[key]);
            if (!item && typeof key === 'string') {
              item = { title: key, text: key };
            }
            if (item) self.loadContent(item);
          } catch (e) {
            console.warn('[AiBhaktiPlayer] Hook error:', e);
          }
          return res;
        };
      }

      // Export convenient helper for Bhagavad Gita verses
      window.playAiGitaVerse = function(shlokaText, title, verseNum, btnEl) {
        self.loadContent({
          id: `gita_shloka_${verseNum || 'verse'}`,
          title: title || 'श्रीमद्भगवद्गीता श्लोक',
          text: shlokaText,
          type: 'shloka'
        });
        self.togglePlay();
      };
    }
  };

  // Auto-init on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => window.AiBhaktiPlayer.init());
  } else {
    window.AiBhaktiPlayer.init();
  }
})();
