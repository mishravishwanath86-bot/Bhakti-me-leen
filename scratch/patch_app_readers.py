import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Patch modern readAartiItemDirect
old_aarti_player_call = """  // 7. Load into AI Bhakti Player Engine for on-demand playback
  if (window.AiBhaktiPlayer) {
    window.AiBhaktiPlayer.loadContent({
      id: item.id || `aarti_${deityKey}_${idx}`,
      title: item.hi_line || item.title || coll.title,
      text: item.content || item.text,
      type: 'aarti',
      deity: coll.deity || deityKey
    });
  }"""

new_aarti_player_call = """  // 7. Load into AI Bhakti Player Engine for on-demand playback
  const activeAartiObj = {
    id: item.id || `aarti_${deityKey}_${idx}`,
    title: item.hi_line || item.title || coll.title,
    text: item.content || item.text,
    type: 'aarti',
    deity: coll.deity || deityKey,
    source: 'aarti_collections',
    deityKey: deityKey,
    idx: idx
  };
  window._activeDevotionalContent = activeAartiObj;

  if (window.AiBhaktiPlayer && typeof window.AiBhaktiPlayer.loadContent === 'function') {
    window.AiBhaktiPlayer.loadContent(activeAartiObj);
  }"""

if old_aarti_player_call in content:
    content = content.replace(old_aarti_player_call, new_aarti_player_call, 1)
    print("SUCCESS: Patched modern readAartiItemDirect in app.js")
else:
    print("WARNING: old_aarti_player_call pattern not found in app.js")

# 2. Patch modern readChalisaItemDirect
old_chalisa_player_call = """  // 7. Connect to AI Bhakti Player Engine for On-Demand Audio
  if (window.AiBhaktiPlayer) {
    window.AiBhaktiPlayer.loadContent({
      id: item.id || `chalisa_${deityKey}_${idx}`,
      title: item.hi_line || item.title || coll.title,
      text: item.content || item.text,
      type: 'chalisa',
      deity: coll.deity || deityKey
    });
  }"""

new_chalisa_player_call = """  // 7. Connect to AI Bhakti Player Engine for On-Demand Audio
  const activeChalisaObj = {
    id: item.id || `chalisa_${deityKey}_${idx}`,
    title: item.hi_line || item.title || coll.title,
    text: item.content || item.text,
    type: 'chalisa',
    deity: coll.deity || deityKey,
    source: 'chalisa_collections',
    deityKey: deityKey,
    idx: idx
  };
  window._activeDevotionalContent = activeChalisaObj;

  if (window.AiBhaktiPlayer && typeof window.AiBhaktiPlayer.loadContent === 'function') {
    window.AiBhaktiPlayer.loadContent(activeChalisaObj);
  }"""

if old_chalisa_player_call in content:
    content = content.replace(old_chalisa_player_call, new_chalisa_player_call, 1)
    print("SUCCESS: Patched modern readChalisaItemDirect in app.js")
else:
    print("WARNING: old_chalisa_player_call pattern not found in app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Finished patching app.js")
