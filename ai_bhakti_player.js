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
      if (window._activeDevotionalContent && window._activeDevotionalContent.text) {
        this.loadContent(window._activeDevotionalContent);
      } else {
        this.autoDetectCurrentContent();
      }
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
    // 🔍 RESILIENT AUTO-DETECTION (यदि सीधे Play बटन दबाया जाए)
    // ─────────────────────────────────────────────────────────────────
    autoDetectCurrentContent: function() {
      // Tier 1: Check global anchor window._activeDevotionalContent
      if (window._activeDevotionalContent) {
        const anc = window._activeDevotionalContent;
        const rawText = anc.text || anc.content || anc.sanskrit || (anc.chaupais ? anc.chaupais.join('\n') : '');
        if (rawText && rawText.trim().length >= 5) {
          this.loadContent(anc);
          return true;
        }
      }

      // Tier 2: Check if Sundarkand reader modal is open or doha is active
      const skModal = document.getElementById('sundarkand-reader-modal');
      const isSkOpen = skModal && (skModal.style.display === 'flex' || skModal.style.display === 'block' || skModal.classList.contains('active'));
      if ((isSkOpen || window._sundarkandCurrentDoha) && window.SUNDARKAND_DATA && window.SUNDARKAND_DATA.dohas) {
        const dohaNum = window._sundarkandCurrentDoha || 1;
        const doha = window.SUNDARKAND_DATA.dohas.find(d => d.doha_number === dohaNum) || window.SUNDARKAND_DATA.dohas[0];
        if (doha) {
          const parts = [];
          if (doha.shloka && doha.shloka.length > 0) parts.push(Array.isArray(doha.shloka) ? doha.shloka.join('\n') : doha.shloka);
          if (doha.chaupais && doha.chaupais.length > 0) parts.push(Array.isArray(doha.chaupais) ? doha.chaupais.join('\n') : doha.chaupais);
          if (doha.chhand && doha.chhand.length > 0) parts.push(Array.isArray(doha.chhand) ? doha.chhand.join('\n') : doha.chhand);
          if (doha.doha && doha.doha.length > 0) parts.push(Array.isArray(doha.doha) ? doha.doha.join('\n') : doha.doha);
          const recText = parts.join('\n\n');
          this.loadContent({
            id: `sundarkand-doha-${doha.doha_number}`,
            title: `सुन्दरकाण्ड दोहा ${doha.doha_number}: ${doha.title}`,
            text: recText,
            type: 'sundarkand',
            deity: 'श्री हनुमान जी'
          });
          return true;
        }
      }

      // Tier 3: Dedicated Aarti Pane (#aarti-pane-lyrics)
      const aartiPane = document.getElementById('aarti-pane-lyrics');
      if (aartiPane) {
        const lyricsText = (aartiPane.innerText || aartiPane.textContent || '').trim();
        if (lyricsText.length > 10) {
          const titleEl = document.querySelector('.pure-reader-wrapper h1') || document.getElementById('reader-page-title');
          let title = titleEl ? titleEl.textContent.replace(/^[॥\s]+|[॥\s]+$/g, '').trim() : 'पावन आरती';
          this.loadContent({
            id: 'aarti_' + (window._aartiReaderOriginModalDeity || 'current') + '_' + Math.abs(lyricsText.length),
            title: title,
            text: lyricsText,
            type: 'aarti',
            deity: window._aartiReaderOriginModalDeity || 'सनातन'
          });
          return true;
        }
      }

      // Tier 4: Dedicated Chalisa Pane (#chalisa-pane-lyrics)
      const chalisaPane = document.getElementById('chalisa-pane-lyrics');
      if (chalisaPane) {
        const lyricsText = (chalisaPane.innerText || chalisaPane.textContent || '').trim();
        if (lyricsText.length > 10) {
          const titleEl = document.querySelector('.pure-reader-wrapper h1') || document.getElementById('reader-page-title');
          let title = titleEl ? titleEl.textContent.replace(/^[॥\s]+|[॥\s]+$/g, '').trim() : 'पावन चालीसा';
          this.loadContent({
            id: 'chalisa_' + (window._chalisaReaderOriginModalDeity || 'current') + '_' + Math.abs(lyricsText.length),
            title: title,
            text: lyricsText,
            type: 'chalisa',
            deity: window._chalisaReaderOriginModalDeity || 'संकटमोचन श्री हनुमान जी'
          });
          return true;
        }
      }

      // Tier 5: Sundarkand Reader Content (#sundarkand-reader-content)
      const skContent = document.getElementById('sundarkand-reader-content');
      if (skContent) {
        const text = (skContent.innerText || skContent.textContent || '').trim();
        if (text.length > 15) {
          const titleEl = document.getElementById('sundarkand-reader-doha-title');
          const title = titleEl ? titleEl.textContent.trim() : 'सुन्दरकाण्ड पावन पाठ';
          this.loadContent({
            id: `sundarkand-doha-${window._sundarkandCurrentDoha || 1}`,
            title: title,
            text: text,
            type: 'sundarkand',
            deity: 'श्री हनुमान जी'
          });
          return true;
        }
      }

      // Tier 6: Active Devanagari Reader Verses (#reader-cosmic-content, .pure-reader-wrapper, etc.)
      const cosmicEl = document.getElementById('reader-cosmic-content') || document.getElementById('reader-content');
      if (cosmicEl) {
        const verseEl = cosmicEl.querySelector('.pure-reader-text, .cosmic-verse-text, [style*="pre-line"], .cosmic-verse-card');
        const text = verseEl ? (verseEl.innerText || verseEl.textContent || '').trim() : (cosmicEl.innerText || cosmicEl.textContent || '').trim();
        if (text.length > 10) {
          const titleEl = cosmicEl.querySelector('h1') || document.getElementById('reader-page-title') || document.getElementById('reader-audio-title');
          const rawTitle = titleEl ? titleEl.textContent.replace(/^[॥\s]+|[॥\s]+$/g, '').trim() : 'दिव्य भक्ति पाठ';
          let type = 'aarti';
          if (rawTitle.includes('चालीसा')) type = 'chalisa';
          else if (rawTitle.includes('मन्त्र') || rawTitle.includes('मंत्र')) type = 'mantra';
          else if (rawTitle.includes('सुन्दरकाण्ड') || rawTitle.includes('दोहा')) type = 'sundarkand';

          this.loadContent({
            id: 'auto_' + type + '_' + Math.abs(text.length),
            title: rawTitle,
            text: text,
            type: type,
            deity: 'सनातन'
          });
          return true;
        }
      }

      // Tier 7: In-memory Collection Fallbacks
      if (window._aartiReaderOriginModalDeity && window.AARTI_COLLECTIONS && window.AARTI_COLLECTIONS[window._aartiReaderOriginModalDeity]) {
        const coll = window.AARTI_COLLECTIONS[window._aartiReaderOriginModalDeity];
        const item = (coll.items && coll.items[0]) ? coll.items[0] : null;
        if (item) {
          this.loadContent({
            id: item.id || `aarti_${window._aartiReaderOriginModalDeity}_0`,
            title: item.title || coll.title,
            text: item.content || item.text,
            type: 'aarti',
            deity: coll.deity
          });
          return true;
        }
      }
      if (window._chalisaReaderOriginModalDeity && window.CHALISA_COLLECTIONS && window.CHALISA_COLLECTIONS[window._chalisaReaderOriginModalDeity]) {
        const coll = window.CHALISA_COLLECTIONS[window._chalisaReaderOriginModalDeity];
        const item = (coll.items && coll.items[0]) ? coll.items[0] : null;
        if (item) {
          this.loadContent({
            id: item.id || `chalisa_${window._chalisaReaderOriginModalDeity}_0`,
            title: item.title || coll.title,
            text: item.content || item.text,
            type: 'chalisa',
            deity: coll.deity
          });
          return true;
        }
      }
      if (window._mantraReaderOriginModalDeity && window.MANTRA_COLLECTIONS && window.MANTRA_COLLECTIONS[window._mantraReaderOriginModalDeity]) {
        const coll = window.MANTRA_COLLECTIONS[window._mantraReaderOriginModalDeity];
        const item = (coll.items && coll.items[0]) ? coll.items[0] : null;
        if (item) {
          this.loadContent({
            id: item.id || `mantra_${window._mantraReaderOriginModalDeity}_0`,
            title: item.title || coll.title,
            text: item.sanskrit || item.content || item.text,
            type: 'mantra',
            deity: coll.deity
          });
          return true;
        }
      }

      // Tier 8: Current Page Context Fallback
      const curPage = window.currentPage || (typeof currentPage !== 'undefined' ? currentPage : '');
      if (curPage === 'page-sundarkand' && window.SUNDARKAND_DATA && window.SUNDARKAND_DATA.dohas && window.SUNDARKAND_DATA.dohas.length > 0) {
        const d = window.SUNDARKAND_DATA.dohas[0];
        const recText = (d.chaupais || []).concat(d.doha || []).join('\n');
        this.loadContent({ id: `sundarkand-doha-${d.doha_number}`, title: `सुन्दरकाण्ड दोहा ${d.doha_number}: ${d.title}`, text: recText, type: 'sundarkand', deity: 'श्री हनुमान जी' });
        return true;
      }
      if (curPage === 'page-mantra' && window.MANTRA_COLLECTIONS) {
        const firstK = Object.keys(window.MANTRA_COLLECTIONS)[0];
        const coll = window.MANTRA_COLLECTIONS[firstK];
        if (coll && coll.items && coll.items[0]) {
          const item = coll.items[0];
          this.loadContent({ id: item.id || 'mantra_default', title: `${coll.deity} • ${item.title}`, text: item.sanskrit || item.text, type: 'mantra', deity: coll.deity });
          return true;
        }
      }
      if (curPage === 'page-chalisa' && window.CHALISA_COLLECTIONS) {
        const firstK = Object.keys(window.CHALISA_COLLECTIONS)[0];
        const coll = window.CHALISA_COLLECTIONS[firstK];
        if (coll && coll.items && coll.items[0]) {
          const item = coll.items[0];
          this.loadContent({ id: item.id || 'chalisa_default', title: item.title, text: item.content || item.text, type: 'chalisa', deity: coll.deity });
          return true;
        }
      }
      if (curPage === 'page-aarti' && window.AARTI_COLLECTIONS) {
        const firstK = Object.keys(window.AARTI_COLLECTIONS)[0];
        const coll = window.AARTI_COLLECTIONS[firstK];
        if (coll && coll.items && coll.items[0]) {
          const item = coll.items[0];
          this.loadContent({ id: item.id || 'aarti_default', title: item.title, text: item.content || item.text, type: 'aarti', deity: coll.deity });
          return true;
        }
      }

      return false;
    },

    // ─────────────────────────────────────────────────────────────────
    // 🎧 ON-DEMAND AUDIO GENERATION & PLAYBACK (जब Play दबे, तभी बने)
    // ─────────────────────────────────────────────────────────────────
    togglePlay: async function() {
      if (!this.currentContent || !this.currentContent.text) {
        this.autoDetectCurrentContent();
      }

      if (!this.currentContent || !this.currentContent.text) {
        if (window._activeDevotionalContent) {
          this.loadContent(window._activeDevotionalContent);
        }
      }

      // Ultimate DOM Inspection Fallback before throwing any error
      if (!this.currentContent || !this.currentContent.text || this.currentContent.text.trim().length === 0) {
        const domCandidates = [
          document.getElementById('reader-cosmic-content'),
          document.getElementById('sundarkand-reader-content'),
          document.getElementById('aarti-pane-lyrics'),
          document.getElementById('chalisa-pane-lyrics'),
          document.querySelector('.pure-reader-text'),
          document.querySelector('.cosmic-verse-text')
        ];
        for (const el of domCandidates) {
          if (el && (el.innerText || el.textContent)) {
            const domText = (el.innerText || el.textContent).trim();
            if (domText.length >= 8) {
              this.loadContent({
                id: 'dom_direct_' + Math.abs(domText.length),
                title: 'दिव्य भक्ति पाठ',
                text: domText,
                type: 'aarti',
                deity: 'सनातन'
              });
              break;
            }
          }
        }
      }

      if (!this.currentContent || !this.currentContent.text || this.currentContent.text.trim().length === 0) {
        this.showToast('⚠️ कोई सामग्री लोड नहीं है');
        return;
      }

      // 1. If currently playing -> PAUSE
      if (this.isPlaying) {
        if (this.audioInstance) {
          try { this.audioInstance.pause(); } catch (_) {}
        }
        if (window.speechSynthesis && (window.speechSynthesis.speaking || window.speechSynthesis.pending)) {
          try { window.speechSynthesis.pause(); } catch (_) {}
        }
        this.stopSpeechProgressTimer();
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
          console.warn('[AiBhaktiPlayer] Audio resume failed, attempting on-device resume or fresh play:', e);
        }
      }

      // 2b. If paused with SpeechSynthesis -> RESUME
      if (!this.isPlaying && window.speechSynthesis && window.speechSynthesis.paused) {
        try {
          window.speechSynthesis.resume();
          this.startTempleDrone();
          this.startSpeechProgressTimer(this.speechEstDuration || 30);
          this.isPlaying = true;
          this.updateUI();
          if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
          return;
        } catch (e) {
          console.warn('[AiBhaktiPlayer] SpeechSynthesis resume failed:', e);
        }
      }

      // 3. Otherwise -> Fresh or Cached Playback via Direct URL / Backend / On-Device Synthesis
      await this.requestAndPlayAudio();
    },

    cleanDevotionalText: function(rawText) {
      if (!rawText) return '';
      let text = String(rawText).replace(/<[^>]+>/g, ' ');
      text = text.replace(/\[[^\]]*\]/g, '');
      text = text.replace(/\([^\)]*(?:chorus|verse|meaning|भावार्थ|उच्चारण|फलश्रुति)[^\)]*\)/gi, '');
      const lines = text.split(/\r?\n/).map(l => l.trim()).filter(Boolean);
      const cleanLines = [];
      for (const line of lines) {
        let devanagariCount = 0;
        let asciiAlphaCount = 0;
        for (let i = 0; i < line.length; i++) {
          const code = line.charCodeAt(i);
          if (code >= 0x0900 && code <= 0x097F) devanagariCount++;
          else if ((code >= 65 && code <= 90) || (code >= 97 && code <= 122)) asciiAlphaCount++;
        }
        if (asciiAlphaCount > 15 && devanagariCount === 0) continue;
        cleanLines.push(line.replace(/\s+/g, ' '));
      }
      return cleanLines.join('\n').trim();
    },

    getPreCachedAudioUrl: function() {
      if (!this.currentContent) return null;
      const id = String(this.currentContent.id || '').toLowerCase();
      const title = String(this.currentContent.title || '').toLowerCase();

      // 1. Sundarkand Doha 1
      if (id.includes('sundarkand-doha-1') || (title.includes('सुन्दरकाण्ड') && (title.includes(' 1') || title.includes('१')))) {
        return 'assets/ai_audio/bhakti_sundarkand-doha-1_male_0d83562022b5.mp3';
      }
      // 2. Ganesha Vakratunda Mantra
      if (id.includes('mantra_ganesha_1') || title.includes('वक्रतुण्ड')) {
        return 'assets/ai_audio/bhakti_mantra_ganesha_1_male_019e46dd67e0.mp3';
      }
      // 3. Hanuman Chalisa
      if (id.includes('drik_chalisa_1') || id.includes('chalisa-1') || id.includes('hanuman-chalisa') || (title.includes('हनुमान') && title.includes('चालीसा'))) {
        return 'assets/ai_audio/bhakti_drik_chalisa_1_male_126de0dc8e75.mp3';
      }
      // 4. Aarti Kunjbihari
      if (id.includes('krishna_3') || id.includes('kunjbihari') || title.includes('कुंजबिहारी') || title.includes('कृष्णमुरारी')) {
        return 'assets/ai_audio/bhakti_drik_krishna_3_male_4cb475bed36f.mp3';
      }
      return null;
    },

    requestAndPlayAudio: async function() {
      if (this.isGenerating) return;

      // Tier 1: Check for Direct Audio URL (Like Bhagavad Gita Architecture)
      const directUrl = this.currentContent ? this.currentContent.audio_url : null;
      if (directUrl && typeof directUrl === 'string' && directUrl.trim().length > 5 &&
          !directUrl.includes('youtube.com') && !directUrl.includes('youtu.be')) {
        try {
          this.playDirectAudioStream(directUrl, true);
          return;
        } catch (err) {
          console.warn('[AiBhaktiPlayer] Direct audio playback failed, falling back to AI synthesis:', err);
        }
      }

      // Tier 1b: Check Known Pre-Cached High-Fidelity Devotional Audio
      const preCachedAudio = this.getPreCachedAudioUrl();
      if (preCachedAudio) {
        try {
          this.playDirectAudioStream(preCachedAudio, true);
          return;
        } catch (err) {
          console.warn('[AiBhaktiPlayer] Pre-cached audio stream failed, falling back:', err);
        }
      }

      // Tier 2: AI Neural Speech Generation via Backend API (if reachable)
      const payload = {
        content_id: (this.currentContent && this.currentContent.id) ? this.currentContent.id : 'current',
        text: (this.currentContent && this.currentContent.text) ? this.currentContent.text : '',
        title: (this.currentContent && this.currentContent.title) ? this.currentContent.title : 'दिव्य पाठ',
        content_type: (this.currentContent && this.currentContent.type) ? this.currentContent.type : 'aarti',
        voice: this.currentVoice,
        speed: this.currentSpeed
      };

      const isMobileApp = (typeof window !== 'undefined' && window.location && (
        window.location.protocol === 'file:' ||
        (window.location.hostname && window.location.hostname.includes('androidplatform.net')) ||
        window.location.hostname === ''
      ));

      let apiUrl = null;
      if (typeof window !== 'undefined' && window.API_BASE_URL) {
        apiUrl = window.API_BASE_URL.replace(/\/+$/, '') + '/api/ai-audio/generate';
      } else if (!isMobileApp && typeof window !== 'undefined' && window.location && window.location.origin &&
                 window.location.origin.startsWith('http') && !window.location.origin.includes('appassets.androidplatform.net')) {
        apiUrl = '/api/ai-audio/generate';
      }

      if (apiUrl) {
        this.isGenerating = true;
        this.updateUI();

        try {
          const controller = (typeof AbortController !== 'undefined') ? new AbortController() : null;
          const timeoutId = controller ? setTimeout(() => controller.abort(), 4000) : null;

          const resp = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
            signal: controller ? controller.signal : undefined
          });
          if (timeoutId) clearTimeout(timeoutId);

          if (resp && resp.ok) {
            const data = await resp.json();
            if (data && data.success && data.audio_url) {
              this.playDirectAudioStream(data.audio_url, data.cached);
              return;
            }
          }
        } catch (netErr) {
          console.info('[AiBhaktiPlayer] Backend API unreachable, engaging on-device devotional speech engine:', netErr.message);
        } finally {
          this.isGenerating = false;
        }
      }

      // Tier 3: Resilient On-Device AI Devotional Synthesis (Offline / Mobile App Mode)
      // Never crash or pop up "Failed to fetch" toast. Always provide divine recitation!
      this.playOnDeviceAiSynthesis();
    },

    playDirectAudioStream: function(audioUrl, isCached) {
      if (window.speechSynthesis) {
        try { window.speechSynthesis.cancel(); } catch (_) {}
      }
      this.stopSpeechProgressTimer();

      if (this.audioInstance) {
        try {
          this.audioInstance.pause();
          this.audioInstance.src = '';
        } catch (_) {}
        this.audioInstance = null;
      }

      let finalUrl = audioUrl;
      if (finalUrl.startsWith('/') && window.API_BASE_URL) {
        finalUrl = window.API_BASE_URL.replace(/\/+$/, '') + finalUrl;
      }

      const audio = new Audio(finalUrl);
      audio.playbackRate = this.currentSpeed;
      audio.loop = this.isLooping;
      this.audioInstance = audio;

      audio.addEventListener('timeupdate', () => this.handleTimeUpdate());
      audio.addEventListener('ended', () => this.handleTrackEnded());
      audio.addEventListener('error', (e) => {
        console.warn('[AiBhaktiPlayer] Audio error, falling back to on-device synthesis:', e);
        this.playOnDeviceAiSynthesis();
      });

      audio.play().then(() => {
        this.isPlaying = true;
        this.isGenerating = false;
        this.startTempleDrone();
        this.updateUI();

        if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
        if (isCached) {
          this.showToast('⚡ पावन ऑडियो लोड हुआ (कैश से तुरंत)');
        } else {
          this.showToast('✨ AI दिव्य स्वर व संगीत श्रवण प्रारंभ!');
        }
      }).catch((playErr) => {
        console.warn('[AiBhaktiPlayer] Audio play rejected, falling back to on-device synthesis:', playErr);
        this.playOnDeviceAiSynthesis();
      });
    },

    playOnDeviceAiSynthesis: function() {
      if (!('speechSynthesis' in window)) {
        this.showToast('⚠️ ऑडियो प्लेबैक डिवाइस पर उपलब्ध नहीं है');
        this.isPlaying = false;
        this.isGenerating = false;
        this.updateUI();
        return;
      }

      const rawText = this.currentContent ? this.currentContent.text : '';
      const cleanText = this.cleanDevotionalText(rawText);
      if (!cleanText || cleanText.trim().length === 0) {
        this.showToast('⚠️ सामग्री का पाठ रिक्त है');
        this.isPlaying = false;
        this.isGenerating = false;
        this.updateUI();
        return;
      }

      try { window.speechSynthesis.cancel(); } catch (_) {}
      if (this.audioInstance) {
        try { this.audioInstance.pause(); } catch (_) {}
        this.audioInstance = null;
      }

      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.lang = 'hi-IN';
      utterance.rate = Math.max(0.7, Math.min(1.4, this.currentSpeed * 0.92));
      utterance.pitch = this.currentVoice === 'female' ? 1.15 : 0.95;

      try {
        const voices = window.speechSynthesis.getVoices ? window.speechSynthesis.getVoices() : [];
        if (voices && voices.length > 0) {
          const hVoice = voices.find(v => v.lang === 'hi-IN' || v.lang === 'hi_IN' || (v.lang && v.lang.startsWith('hi')));
          if (hVoice) utterance.voice = hVoice;
        }
      } catch (_) {}

      this.speechUtterance = utterance;
      this.isPlaying = true;
      this.isGenerating = false;
      this.startTempleDrone();
      this.updateUI();

      if (typeof triggerFlowerShower === 'function') triggerFlowerShower();
      this.showToast('✨ AI दिव्य पाठ व तानपुरा संगत प्रारंभ (पावन स्वर)');

      const estSec = Math.max(8, Math.round((cleanText.length / 13) / this.currentSpeed));
      this.speechEstDuration = estSec;
      this.startSpeechProgressTimer(estSec);

      utterance.onend = () => {
        this.stopSpeechProgressTimer();
        this.handleTrackEnded();
      };

      utterance.onerror = (e) => {
        console.warn('[AiBhaktiPlayer] SpeechSynthesis error:', e);
        this.stopSpeechProgressTimer();
        this.handleTrackEnded();
      };

      try {
        window.speechSynthesis.speak(utterance);
      } catch (synthErr) {
        console.error('[AiBhaktiPlayer] Speech speak() error:', synthErr);
        this.isPlaying = false;
        this.stopTempleDrone();
        this.updateUI();
      }
    },

    startSpeechProgressTimer: function(durationSeconds) {
      this.stopSpeechProgressTimer();
      this.speechDuration = durationSeconds;
      this.speechElapsed = 0;
      this.speechTimer = setInterval(() => {
        if (!this.isPlaying) return;
        this.speechElapsed += 0.25;
        const pct = Math.min(100, (this.speechElapsed / this.speechDuration) * 100);

        const progressEl = document.getElementById('ai-audio-progress-bar');
        if (progressEl) progressEl.value = pct;

        const timeEl = document.getElementById('ai-audio-time-label');
        if (timeEl) {
          timeEl.textContent = `${this.formatTime(this.speechElapsed)} / ${this.formatTime(this.speechDuration)}`;
        }

        const skProgress = document.getElementById('sundarkand-audio-progress');
        if (skProgress) skProgress.value = pct;

        const skTime = document.getElementById('sundarkand-audio-time');
        if (skTime) {
          skTime.textContent = `${this.formatTime(this.speechElapsed)} / ${this.formatTime(this.speechDuration)}`;
        }
      }, 250);
    },

    stopSpeechProgressTimer: function() {
      if (this.speechTimer) {
        clearInterval(this.speechTimer);
        this.speechTimer = null;
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
      if (this.isPlaying && window.speechSynthesis && window.speechSynthesis.speaking) {
        this.playOnDeviceAiSynthesis();
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

      if (this.isPlaying) {
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
      pct = parseFloat(pct) || 0;
      if (this.audioInstance && this.audioInstance.duration) {
        this.audioInstance.currentTime = (pct / 100) * this.audioInstance.duration;
      } else if (this.speechDuration) {
        this.speechElapsed = (pct / 100) * this.speechDuration;
        const progressEl = document.getElementById('ai-audio-progress-bar');
        if (progressEl) progressEl.value = pct;
        const timeEl = document.getElementById('ai-audio-time-label');
        if (timeEl) {
          timeEl.textContent = `${this.formatTime(this.speechElapsed)} / ${this.formatTime(this.speechDuration)}`;
        }
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

      const skProgress = document.getElementById('sundarkand-audio-progress');
      if (skProgress) skProgress.value = pct;

      const skTime = document.getElementById('sundarkand-audio-time');
      if (skTime) {
        skTime.textContent = `${this.formatTime(cur)} / ${this.formatTime(dur)}`;
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
          if (this.audioInstance) {
            this.audioInstance.play();
          } else {
            this.playOnDeviceAiSynthesis();
          }
          return;
        }
      }

      this.isPlaying = false;
      this.stopSpeechProgressTimer();
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
        try { this.audioInstance.pause(); } catch (_) {}
        this.audioInstance = null;
      }
      if (window.speechSynthesis) {
        try { window.speechSynthesis.cancel(); } catch (_) {}
      }
      this.stopSpeechProgressTimer();
      this.isPlaying = false;
      this.isGenerating = false;
      this.stopTempleDrone();

      let text = contentObj.text || '';
      if (!text && contentObj.sanskrit) {
        text = contentObj.sanskrit;
      }
      if (!text && contentObj.content) {
        text = contentObj.content;
      }
      if (!text && Array.isArray(contentObj.lines)) {
        text = contentObj.lines.map(l => (typeof l === 'object' ? (l.hindi || l.text || l.sanskrit || '') : l)).join('\n');
      }
      if (!text && (contentObj.chaupais || contentObj.doha || contentObj.shloka)) {
        const parts = [];
        if (contentObj.shloka && contentObj.shloka.length) parts.push(Array.isArray(contentObj.shloka) ? contentObj.shloka.join('\n') : contentObj.shloka);
        if (contentObj.chaupais && contentObj.chaupais.length) parts.push(Array.isArray(contentObj.chaupais) ? contentObj.chaupais.join('\n') : contentObj.chaupais);
        if (contentObj.chhand && contentObj.chhand.length) parts.push(Array.isArray(contentObj.chhand) ? contentObj.chhand.join('\n') : contentObj.chhand);
        if (contentObj.doha && contentObj.doha.length) parts.push(Array.isArray(contentObj.doha) ? contentObj.doha.join('\n') : contentObj.doha);
        text = parts.join('\n\n');
      }
      if (!text && contentObj.lyrics) {
        text = contentObj.lyrics;
      }
      if (!text && contentObj.body) {
        text = contentObj.body;
      }
      if (!text || text.trim().length < 5) {
        const domCandidates = [
          document.getElementById('reader-cosmic-content'),
          document.getElementById('sundarkand-reader-content'),
          document.getElementById('aarti-pane-lyrics'),
          document.getElementById('chalisa-pane-lyrics'),
          document.querySelector('.pure-reader-text'),
          document.querySelector('.cosmic-verse-text'),
          document.getElementById('reader-content')
        ];
        for (const el of domCandidates) {
          if (el && (el.innerText || el.textContent)) {
            const cText = (el.innerText || el.textContent).trim();
            if (cText.length >= 5) {
              text = cText;
              break;
            }
          }
        }
      }

      this.currentContent = {
        id: contentObj.id || contentObj.key || contentObj.title || 'current_devotional_item',
        title: contentObj.title || contentObj.name || contentObj.hi_line || 'दिव्य पाठ',
        text: text,
        type: contentObj.type || contentObj.content_type || 'aarti',
        deity: contentObj.deity || contentObj.deity_name_hi || 'सनातन',
        audio_url: contentObj.audio_url || contentObj.audio_source || contentObj.audio || null,
        video_id: contentObj.video_id || null,
        meaning: contentObj.meaning || ''
      };

      window._activeDevotionalContent = this.currentContent;

      this.updateUI();
    },

    updateUI: function() {
      const container = document.getElementById('ai-bhakti-audio-bar');

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

      // Also update Sundarkand modal controls if active
      const skPlayBtn = document.getElementById('sundarkand-play-btn');
      const skPlayText = document.getElementById('sundarkand-play-btn-text');
      const skStatus = document.getElementById('sundarkand-audio-status');
      if (skPlayBtn) {
        if (this.isGenerating) {
          if (skPlayText) skPlayText.textContent = 'दिव्य स्वर सृजन हो रहा है...';
        } else if (this.isPlaying) {
          if (skPlayText) skPlayText.textContent = 'विराम (Pause)';
        } else {
          if (skPlayText) skPlayText.textContent = 'AI दिव्य पाठ सुनें';
        }
      }
      if (skStatus) {
        if (this.isGenerating) {
          skStatus.textContent = '⏳ AI दिव्य सुर सृजन...';
          skStatus.style.color = '#F59E0B';
        } else if (this.isPlaying) {
          skStatus.textContent = '🎵 लाइव भक्ति श्रवण';
          skStatus.style.color = '#10B981';
        } else {
          skStatus.textContent = '✨ ऑन-डिमांड AI पाठ';
          skStatus.style.color = '#FDE68A';
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
      if (typeof origOpenReader === 'function' && !origOpenReader._aiHooked) {
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
        window.openReader._aiHooked = true;
      }

      // Wrap window.showPage to auto-detect content if page-reader opens
      const origShowPage = window.showPage;
      if (typeof origShowPage === 'function' && !origShowPage._aiHooked) {
        window.showPage = function(pageId) {
          const res = origShowPage.apply(this, arguments);
          if (pageId === 'page-reader') {
            setTimeout(function() {
              if (!self.currentContent || !self.currentContent.text) {
                self.autoDetectCurrentContent();
              }
            }, 60);
          }
          return res;
        };
        window.showPage._aiHooked = true;
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
