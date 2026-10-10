with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. In renderAudioLibrary, ensure window.AUDIO_LIBRARY_ITEMS is set
old_assign = 'AUDIO_LIBRARY_ITEMS = data.items || [];'
new_assign = '''AUDIO_LIBRARY_ITEMS = data.items || [];
    window.AUDIO_LIBRARY_ITEMS = AUDIO_LIBRARY_ITEMS;'''

if old_assign in js:
    js = js.replace(old_assign, new_assign, 1)
    print("1. Added window.AUDIO_LIBRARY_ITEMS assignment in renderAudioLibrary")
else:
    print("1. old_assign not found or already modified")

# 2. Fix playAudioLibraryIndex definition and window.playAudioLibraryIndex
old_play_fn = '''function playAudioLibraryIndex(idx) {
  if (idx < 0 || idx >= AUDIO_LIBRARY_ITEMS.length) return;
  currentAudioIndex = idx;
  const item = AUDIO_LIBRARY_ITEMS[idx];'''

new_play_fn = '''function playAudioLibraryIndex(idx) {
  const items = (window.AUDIO_LIBRARY_ITEMS && window.AUDIO_LIBRARY_ITEMS.length) ? window.AUDIO_LIBRARY_ITEMS : AUDIO_LIBRARY_ITEMS;
  if (!items || idx < 0 || idx >= items.length) return;
  currentAudioIndex = idx;
  window.currentAudioIndex = idx;
  const item = items[idx];'''

if old_play_fn in js:
    js = js.replace(old_play_fn, new_play_fn, 1)
    print("2. Updated playAudioLibraryIndex")

# 3. Fix openReaderFromAudioLib definition
old_open_fn = '''function openReaderFromAudioLib(idx) {
  const item = AUDIO_LIBRARY_ITEMS[idx];
  if (!item) return;
  openReader(item, 'page-katha');
}'''

new_open_fn = '''function openReaderFromAudioLib(idx) {
  const items = (window.AUDIO_LIBRARY_ITEMS && window.AUDIO_LIBRARY_ITEMS.length) ? window.AUDIO_LIBRARY_ITEMS : AUDIO_LIBRARY_ITEMS;
  if (!items || idx < 0 || idx >= items.length) return;
  const item = items[idx];
  if (typeof window.openReaderFromAudioLib === 'function') {
    window.openReaderFromAudioLib(idx);
  } else {
    openReader(item, 'page-katha');
  }
}'''

if old_open_fn in js:
    js = js.replace(old_open_fn, new_open_fn, 1)
    print("3. Updated openReaderFromAudioLib")

# 4. Fix window.playAudioLibraryIndex and window.openReaderFromAudioLib at the bottom of app.js
old_bottom_block = '''window.playAudioLibraryIndex = function(idx) {
  if (!window.AUDIO_LIBRARY_ITEMS || idx < 0 || idx >= window.AUDIO_LIBRARY_ITEMS.length) return;
  window.currentAudioIndex = idx;
  const item = window.AUDIO_LIBRARY_ITEMS[idx];
  if (!item) return;

  const thumb = (typeof getDeityArtwork === 'function') 
    ? getDeityArtwork(item.deity_id || item.deity_name_hi, item.title) 
    : 'assets/app_logo.jpg';

  // 1. Update Floating Mini Player
  const miniTitle = document.getElementById('glass-mini-title');
  if (miniTitle) miniTitle.textContent = item.title;
  const miniDeity = document.getElementById('glass-mini-deity');
  if (miniDeity) miniDeity.textContent = item.deity_name_hi || item.deity_id || 'भक्ति रस';
  const miniCover = document.getElementById('glass-mini-cover');
  if (miniCover) miniCover.src = thumb;

  // 2. Update Full Glass Timeline Player
  const modalTitle = document.getElementById('glass-modal-title');
  if (modalTitle) modalTitle.textContent = item.title;
  const modalSub = document.getElementById('glass-modal-sub');
  if (modalSub) modalSub.textContent = `${item.deity_name_hi || item.deity_id || 'सनातन'} • ${(typeof formatTypeBadge === 'function') ? formatTypeBadge(item.content_type) : 'भक्ति'}`;
  const modalImg = document.getElementById('glass-modal-img');
  if (modalImg) modalImg.src = thumb;

  const lyricsContent = document.getElementById('glass-lyrics-content');
  if (lyricsContent) {
    lyricsContent.innerHTML = `<div style="font-size:1rem; line-height:2; color:#FDE68A; white-space:pre-line; text-align:center;">${item.content || item.content_text || '॥ पावन भक्ति रस ॥'}\\n\\n<span style="color:#FFF; font-size:0.8rem;">📖 स्रोत: ${item.audio_url && item.audio_url.startsWith('assets/audio/') ? '💾 ऑफ़लाइन MP3' : '🎬 YouTube HD'}</span></div>`;
  }

  // 3. Play via unified MediaRouter
  if (window.MediaRouter) {
    window.MediaRouter.playRecord(item, 'glass');
  }

  // 4. Open Full Glassmorphic Timeline Scrubber Player Modal
  if (typeof window.openGlassPlayer === 'function') {
    window.openGlassPlayer();
  }
};

window.openReaderFromAudioLib = async function(idx) {
  if (!window.AUDIO_LIBRARY_ITEMS || idx < 0 || idx >= window.AUDIO_LIBRARY_ITEMS.length) return;
  const item = window.AUDIO_LIBRARY_ITEMS[idx];
  if (!item) return;

  // Fetch complete text if content is abbreviated
  let fullContent = item.content || item.content_text || '';
  if (!fullContent || fullContent.length < 50) {
    try {
      const resp = await fetch(`/api/content?id=${item.id}`);
      if (resp.ok) {
        const fullData = await resp.json();
        if (fullData && fullData.content) {
          fullContent = fullData.content;
        }
      }
    } catch(e) {
      console.warn("Could not fetch full content via API:", e);
    }
  }

  if (!fullContent) {
    fullContent = `॥ ${item.title} ॥\\n\\nपावन भक्ति रस एवं नित्य आराधना।`;
  }

  const thumb = (typeof getDeityArtwork === 'function') 
    ? getDeityArtwork(item.deity_id || item.deity_name_hi, item.title) 
    : 'assets/app_logo.jpg';

  // Set Back Button target
  window.readerBackPage = 'page-katha';
  const backBtn = document.querySelector('#page-reader .back-btn');
  if (backBtn) {
    backBtn.setAttribute('data-back', 'page-katha');
    backBtn.onclick = () => window.showPage('page-katha');
  }

  // 1. Set Header Title
  const titleEl = document.getElementById('reader-page-title') || document.querySelector('#page-reader .header-title');
  if (titleEl) titleEl.textContent = item.title;

  // 2. Set Deity Image & Subtitle
  const readerDeityImg = document.getElementById('reader-deity-img');
  if (readerDeityImg) readerDeityImg.src = thumb;

  const aTitleEl = document.getElementById('reader-audio-title');
  if (aTitleEl) aTitleEl.textContent = item.title;
  
  const aSubEl = document.getElementById('reader-audio-sub');
  if (aSubEl) aSubEl.textContent = `${item.deity_name_hi || item.deity_id || 'सनातन'} • पावन स्वाध्याय`;

  // 3. Render Pure, Complete, Beautiful Devanagari Text
  const readerContent = document.getElementById('reader-content');'''

new_bottom_block = '''window.playAudioLibraryIndex = function(idx) {
  const items = (window.AUDIO_LIBRARY_ITEMS && window.AUDIO_LIBRARY_ITEMS.length) ? window.AUDIO_LIBRARY_ITEMS : (typeof AUDIO_LIBRARY_ITEMS !== 'undefined' ? AUDIO_LIBRARY_ITEMS : []);
  if (!items || idx < 0 || idx >= items.length) {
    console.warn("Invalid audio item index:", idx, items);
    return;
  }
  window.currentAudioIndex = idx;
  const item = items[idx];
  if (!item) return;

  const thumb = (typeof getDeityArtwork === 'function') 
    ? getDeityArtwork(item.deity_id || item.deity_name_hi, item.title) 
    : 'assets/app_logo.jpg';

  // 1. Update Floating Mini Player
  const miniTitle = document.getElementById('glass-mini-title');
  if (miniTitle) miniTitle.textContent = item.title;
  const miniDeity = document.getElementById('glass-mini-deity');
  if (miniDeity) miniDeity.textContent = item.deity_name_hi || item.deity_id || 'भक्ति रस';
  const miniCover = document.getElementById('glass-mini-cover');
  if (miniCover) miniCover.src = thumb;

  // 2. Update Full Glass Timeline Player
  const modalTitle = document.getElementById('glass-modal-title');
  if (modalTitle) modalTitle.textContent = item.title;
  const modalSub = document.getElementById('glass-modal-sub');
  if (modalSub) modalSub.textContent = `${item.deity_name_hi || item.deity_id || 'सनातन'} • ${(typeof formatTypeBadge === 'function') ? formatTypeBadge(item.content_type) : 'भक्ति'}`;
  const modalImg = document.getElementById('glass-modal-img');
  if (modalImg) modalImg.src = thumb;

  const lyricsContent = document.getElementById('glass-lyrics-content');
  if (lyricsContent) {
    lyricsContent.innerHTML = `<div style="font-size:1rem; line-height:2; color:#FDE68A; white-space:pre-line; text-align:center;">${item.content || item.content_text || '॥ पावन भक्ति रस ॥'}\\n\\n<span style="color:#FFF; font-size:0.8rem;">📖 स्रोत: ${item.audio_url && item.audio_url.startsWith('assets/audio/') ? '💾 ऑफ़लाइन MP3' : '🎬 YouTube HD'}</span></div>`;
  }

  // 3. Play via unified MediaRouter
  if (window.MediaRouter) {
    window.MediaRouter.playRecord(item, 'glass');
  }

  // 4. Open Full Glassmorphic Timeline Scrubber Player Modal
  if (typeof window.openGlassPlayer === 'function') {
    window.openGlassPlayer();
  }
};

window.openReaderFromAudioLib = async function(idx) {
  const items = (window.AUDIO_LIBRARY_ITEMS && window.AUDIO_LIBRARY_ITEMS.length) ? window.AUDIO_LIBRARY_ITEMS : (typeof AUDIO_LIBRARY_ITEMS !== 'undefined' ? AUDIO_LIBRARY_ITEMS : []);
  if (!items || idx < 0 || idx >= items.length) {
    console.warn("Invalid reader item index:", idx, items);
    return;
  }
  const item = items[idx];
  if (!item) return;

  // Fetch complete text if content is abbreviated
  let fullContent = item.content || item.content_text || item.lyrics || item.text || '';
  if (!fullContent || fullContent.length < 50) {
    try {
      const resp = await fetch(`/api/content?id=${item.id}`);
      if (resp.ok) {
        const fullData = await resp.json();
        if (fullData && (fullData.content || fullData.text)) {
          fullContent = fullData.content || fullData.text;
        }
      }
    } catch(e) {
      console.warn("Could not fetch full content via API:", e);
    }
  }

  if (!fullContent) {
    fullContent = `॥ ${item.title} ॥\\n\\n${item.short_desc || 'पावन भक्ति रस एवं नित्य आराधना।'}\\n\\n॥ ॐ नमो भगवते वासुदेवाय ॥`;
  }

  const thumb = (typeof getDeityArtwork === 'function') 
    ? getDeityArtwork(item.deity_id || item.deity_name_hi, item.title) 
    : 'assets/app_logo.jpg';

  // Set Back Button target
  window.readerBackPage = 'page-katha';
  const backBtn = document.querySelector('#page-reader .back-btn');
  if (backBtn) {
    backBtn.setAttribute('data-back', 'page-katha');
    backBtn.onclick = () => window.showPage('page-katha');
  }

  // 1. Set Header Title
  const titleEl = document.getElementById('reader-page-title') || document.querySelector('#page-reader .header-title');
  if (titleEl) titleEl.textContent = item.title;

  // 2. Set Deity Image & Subtitle
  const readerDeityImg = document.getElementById('reader-deity-img');
  if (readerDeityImg) readerDeityImg.src = thumb;

  const aTitleEl = document.getElementById('reader-audio-title');
  if (aTitleEl) aTitleEl.textContent = item.title;
  
  const aSubEl = document.getElementById('reader-audio-sub');
  if (aSubEl) aSubEl.textContent = `${item.deity_name_hi || item.deity_id || 'सनातन'} • पावन स्वाध्याय`;

  // 3. Render Pure, Complete, Beautiful Devanagari Text (Support both container IDs)
  const readerContent = document.getElementById('reader-cosmic-content') || document.getElementById('reader-content');'''

if old_bottom_block in js:
    js = js.replace(old_bottom_block, new_bottom_block, 1)
    print("4. Updated window.playAudioLibraryIndex and window.openReaderFromAudioLib successfully!")
else:
    print("4. old_bottom_block not matched exactly, checking partial...")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
