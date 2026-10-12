import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Patch legacy declarations around 18942-18978
old_18942 = """function openAartiItemDirect(deityKey, idx) {
  readAartiItemDirect(deityKey, idx);
}

function readAartiItemDirect(deityKey, idx) {
  const item = window.AARTI_COLLECTIONS[deityKey].items[idx];
  if (!item) return;
  closeAartiOptionsModal();

  // Load into Reader
  const readerTitle = document.getElementById('reader-title');
  const readerContent = document.getElementById('reader-content');
  if (readerTitle) readerTitle.textContent = item.title;
  if (readerContent) {
    readerContent.innerHTML = `<div style="white-space:pre-line; text-align:center; line-height:2.0; font-size:1.1rem; color:#1A0B2E; font-weight:700;">${item.content}</div>`;
  }
  showPage('page-reader');
}

function playAartiItemDirect(deityKey, idx) {
  const item = window.AARTI_COLLECTIONS[deityKey].items[idx];
  if (!item) return;
  closeAartiOptionsModal();

  const record = {
    title: item.title,
    deity_id: deityKey,
    deity_name_hi: window.AARTI_COLLECTIONS[deityKey].deity,
    content_type: 'aarti',
    audio_url: item.audio_url,
    content: item.content
  };

  if (window.MediaRouter) {
    window.MediaRouter.playRecord(record);
  }
}"""

new_18942 = """function openAartiItemDirect(deityKey, idx) {
  if (typeof window.readAartiItemDirect === 'function') {
    window.readAartiItemDirect(deityKey, idx);
  }
}

function readAartiItemDirect(deityKey, idx) {
  if (typeof window.readAartiItemDirect === 'function' && window.readAartiItemDirect !== readAartiItemDirect) {
    return window.readAartiItemDirect(deityKey, idx);
  }
}

function playAartiItemDirect(deityKey, idx) {
  if (typeof window.playAartiItemDirect === 'function' && window.playAartiItemDirect !== playAartiItemDirect) {
    return window.playAartiItemDirect(deityKey, idx);
  }
}"""

if old_18942 in code:
    code = code.replace(old_18942, new_18942, 1)
    print("SUCCESS: Replaced legacy 18942 handlers in app.js")
else:
    print("WARNING: old_18942 not found")

# 2. Patch legacy 19918 handlers
old_19918 = """window.readAartiItemDirect = function(deityKey, idx) {
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items[idx]) return;
  const item = coll.items[idx];
  
  window.closeAartiOptionsModal();

  // Load into Reader
  const readerTitle = document.getElementById('reader-title');
  const readerContent = document.getElementById('reader-content');
  if (readerTitle) readerTitle.textContent = item.title;
  if (readerContent) {
    readerContent.innerHTML = `
      <div style="text-align:center; padding:1rem 0;">
        <div style="font-size:1.15rem; color:#D97706; font-weight:800; margin-bottom:0.5rem;">${coll.deity}</div>
        <div style="font-size:0.9rem; color:#78350F; font-weight:600; margin-bottom:1.5rem;">${coll.mantra}</div>
        <div style="white-space:pre-line; text-align:center; line-height:2.2; font-size:1.15rem; color:#1A0B2E; font-weight:700; font-family:'Tiro Devanagari Hindi', serif;">${item.content}</div>
      </div>
    `;
  }
  window.showPage('page-reader');
};

window.playAartiItemDirect = function(deityKey, idx) {
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items[idx]) return;
  const item = coll.items[idx];
  
  window.closeAartiOptionsModal();

  const record = {
    title: item.title,
    deity_id: deityKey,
    deity_name_hi: coll.deity,
    content_type: 'aarti',
    audio_url: item.audio_url,
    content: item.content
  };

  if (window.MediaRouter) {
    window.MediaRouter.playRecord(record);
  }
};"""

new_19918 = """// Legacy 19918 Aarti handlers removed in favor of canonical reader"""

if old_19918 in code:
    code = code.replace(old_19918, new_19918, 1)
    print("SUCCESS: Replaced legacy 19918 handlers in app.js")
else:
    print("WARNING: old_19918 not found")

# 3. Patch legacy 21603 handler
# Let's find line 21603 window.readAartiItemDirect = function(deityKey, idx) {
pos21603 = code.find("window.readAartiItemDirect = function(deityKey, idx) {\n  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;")
if pos21603 != -1:
    end_pos = code.find("// 5. Open Reader Page", pos21603)
    if end_pos != -1:
        end_pos = code.find("window.showPage('page-reader');\n};", end_pos) + len("window.showPage('page-reader');\n};")
        code = code[:pos21603] + "// Legacy 21603 Aarti handler removed in favor of canonical reader" + code[end_pos:]
        print("SUCCESS: Replaced legacy 21603 handler in app.js")
    else:
        print("WARNING: end_pos for 21603 not found")
else:
    print("WARNING: pos21603 not found")

# 4. Patch openReader to ALWAYS loadContent into AiBhaktiPlayer
old_open_reader_audio = """    // Bind to AI Bhakti Singing & Chanting Player
    if (window.AiBhaktiPlayer) {
      window.AiBhaktiPlayer.loadContent(item);
    }
  }

  showPage('page-reader');"""

new_open_reader_audio = """    // Bind to AI Bhakti Singing & Chanting Player
    if (window.AiBhaktiPlayer) {
      window.AiBhaktiPlayer.loadContent(item);
    }
  }

  // Guaranteed synchronization with AI Bhakti Player
  if (window.AiBhaktiPlayer && typeof window.AiBhaktiPlayer.loadContent === 'function') {
    window.AiBhaktiPlayer.loadContent(item);
  }

  showPage('page-reader');"""

if old_open_reader_audio in code:
    code = code.replace(old_open_reader_audio, new_open_reader_audio, 1)
    print("SUCCESS: Patched openReader guaranteed AiBhaktiPlayer sync")
else:
    print("WARNING: old_open_reader_audio not found")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Finished patching app.js")
