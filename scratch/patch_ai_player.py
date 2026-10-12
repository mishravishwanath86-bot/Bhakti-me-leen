import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ai_bhakti_player.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update autoDetectCurrentContent and togglePlay
old_autodetect = '''    // ─────────────────────────────────────────────────────────────────
    // 🔍 RESILIENT AUTO-DETECTION (यदि सीधे Play बटन दबाया जाए)
    // ─────────────────────────────────────────────────────────────────
    autoDetectCurrentContent: function() {
      // Tier 1: Check global anchor window._activeDevotionalContent
      if (window._activeDevotionalContent && window._activeDevotionalContent.text && window._activeDevotionalContent.text.trim().length > 10) {
        this.loadContent(window._activeDevotionalContent);
        return true;
      }

      // Tier 2: Check if Sundarkand modal is open or doha is active
      const skModal = document.getElementById('sundarkand-reader-modal');
      const isSkOpen = skModal && (skModal.style.display === 'flex' || skModal.style.display === 'block' || skModal.classList.contains('active'));
      if ((isSkOpen || window._sundarkandCurrentDoha) && window.SUNDARKAND_DATA && window.SUNDARKAND_DATA.dohas) {
        const dohaNum = window._sundarkandCurrentDoha || 1;
        const doha = window.SUNDARKAND_DATA.dohas.find(d => d.doha_number === dohaNum);
        if (doha) {
          const parts = [];
          if (doha.shloka && doha.shloka.length > 0) parts.push(doha.shloka.join('\\n'));
          if (doha.chaupais && doha.chaupais.length > 0) parts.push(doha.chaupais.join('\\n'));
          if (doha.chhand && doha.chhand.length > 0) parts.push(doha.chhand.join('\\n'));
          if (doha.doha && doha.doha.length > 0) parts.push(doha.doha.join('\\n'));
          const recText = parts.join('\\n\\n');
          this.loadContent({
            id: `sundarkand-doha-${dohaNum}`,
            title: `सुन्दरकाण्ड दोहा ${dohaNum}: ${doha.title}`,
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
        if (lyricsText.length > 15) {
          const titleEl = document.querySelector('.pure-reader-wrapper h1') || document.getElementById('reader-page-title');
          let title = titleEl ? titleEl.textContent.replace(/^[॥\\s]+|[॥\\s]+$/g, '').trim() : 'पावन आरती';
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
        if (lyricsText.length > 15) {
          const titleEl = document.querySelector('.pure-reader-wrapper h1') || document.getElementById('reader-page-title');
          let title = titleEl ? titleEl.textContent.replace(/^[॥\\s]+|[॥\\s]+$/g, '').trim() : 'पावन चालीसा';
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
        if (text.length > 30) {
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

      // Tier 6: Active Devanagari Reader Verses (#reader-cosmic-content or .pure-reader-wrapper)
      const cosmicEl = document.getElementById('reader-cosmic-content') || document.getElementById('reader-content');
      if (cosmicEl) {
        const verseEl = cosmicEl.querySelector('.pure-reader-text, .cosmic-verse-text, [style*="pre-line"]');
        const text = verseEl ? (verseEl.innerText || verseEl.textContent || '').trim() : (cosmicEl.innerText || cosmicEl.textContent || '').trim();
        if (text.length > 15) {
          const titleEl = cosmicEl.querySelector('h1') || document.getElementById('reader-page-title') || document.getElementById('reader-audio-title');
          const rawTitle = titleEl ? titleEl.textContent.replace(/^[॥\\s]+|[॥\\s]+$/g, '').trim() : 'दिव्य भक्ति पाठ';
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
        if (window._activeDevotionalContent && window._activeDevotionalContent.text) {
          this.loadContent(window._activeDevotionalContent);
        }
      }

      if (!this.currentContent || !this.currentContent.text || this.currentContent.text.trim().length === 0) {
        this.showToast('⚠️ कोई सामग्री लोड नहीं है');
        return;
      }'''

new_autodetect = '''    // ─────────────────────────────────────────────────────────────────
    // 🔍 RESILIENT AUTO-DETECTION (यदि सीधे Play बटन दबाया जाए)
    // ─────────────────────────────────────────────────────────────────
    autoDetectCurrentContent: function() {
      // Tier 1: Check global anchor window._activeDevotionalContent
      if (window._activeDevotionalContent) {
        const anc = window._activeDevotionalContent;
        const rawText = anc.text || anc.content || anc.sanskrit || (anc.chaupais ? anc.chaupais.join('\\n') : '');
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
          if (doha.shloka && doha.shloka.length > 0) parts.push(Array.isArray(doha.shloka) ? doha.shloka.join('\\n') : doha.shloka);
          if (doha.chaupais && doha.chaupais.length > 0) parts.push(Array.isArray(doha.chaupais) ? doha.chaupais.join('\\n') : doha.chaupais);
          if (doha.chhand && doha.chhand.length > 0) parts.push(Array.isArray(doha.chhand) ? doha.chhand.join('\\n') : doha.chhand);
          if (doha.doha && doha.doha.length > 0) parts.push(Array.isArray(doha.doha) ? doha.doha.join('\\n') : doha.doha);
          const recText = parts.join('\\n\\n');
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
          let title = titleEl ? titleEl.textContent.replace(/^[॥\\s]+|[॥\\s]+$/g, '').trim() : 'पावन आरती';
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
          let title = titleEl ? titleEl.textContent.replace(/^[॥\\s]+|[॥\\s]+$/g, '').trim() : 'पावन चालीसा';
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
          const rawTitle = titleEl ? titleEl.textContent.replace(/^[॥\\s]+|[॥\\s]+$/g, '').trim() : 'दिव्य भक्ति पाठ';
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
        const recText = (d.chaupais || []).concat(d.doha || []).join('\\n');
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
      }'''

if old_autodetect in code:
    code = code.replace(old_autodetect, new_autodetect, 1)
    print("SUCCESS: Patched autoDetectCurrentContent & togglePlay in ai_bhakti_player.js")
else:
    print("WARNING: old_autodetect not found in ai_bhakti_player.js")

# 2. Update loadContent and updateUI
old_load_ui = '''    loadContent: function(contentObj) {
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
        text = contentObj.lines.map(l => (typeof l === 'object' ? (l.hindi || l.text || '') : l)).join('\\n');
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

      window._activeDevotionalContent = this.currentContent;

      this.updateUI();
    },

    updateUI: function() {
      const container = document.getElementById('ai-bhakti-audio-bar');
      if (!container) return;'''

new_load_ui = '''    loadContent: function(contentObj) {
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
      if (!text && contentObj.sanskrit) {
        text = contentObj.sanskrit;
      }
      if (!text && contentObj.content) {
        text = contentObj.content;
      }
      if (!text && Array.isArray(contentObj.lines)) {
        text = contentObj.lines.map(l => (typeof l === 'object' ? (l.hindi || l.text || l.sanskrit || '') : l)).join('\\n');
      }
      if (!text && (contentObj.chaupais || contentObj.doha || contentObj.shloka)) {
        const parts = [];
        if (contentObj.shloka && contentObj.shloka.length) parts.push(Array.isArray(contentObj.shloka) ? contentObj.shloka.join('\\n') : contentObj.shloka);
        if (contentObj.chaupais && contentObj.chaupais.length) parts.push(Array.isArray(contentObj.chaupais) ? contentObj.chaupais.join('\\n') : contentObj.chaupais);
        if (contentObj.chhand && contentObj.chhand.length) parts.push(Array.isArray(contentObj.chhand) ? contentObj.chhand.join('\\n') : contentObj.chhand);
        if (contentObj.doha && contentObj.doha.length) parts.push(Array.isArray(contentObj.doha) ? contentObj.doha.join('\\n') : contentObj.doha);
        text = parts.join('\\n\\n');
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
        deity: contentObj.deity || contentObj.deity_name_hi || 'सनातन'
      };

      window._activeDevotionalContent = this.currentContent;

      this.updateUI();
    },

    updateUI: function() {
      const container = document.getElementById('ai-bhakti-audio-bar');'''

if old_load_ui in code:
    code = code.replace(old_load_ui, new_load_ui, 1)
    print("SUCCESS: Patched loadContent & updateUI in ai_bhakti_player.js")
else:
    print("WARNING: old_load_ui not found in ai_bhakti_player.js")

with open('ai_bhakti_player.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Finished patching ai_bhakti_player.js")
