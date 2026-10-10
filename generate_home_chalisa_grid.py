import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('drik_chalisa_collections.json', encoding='utf-8') as f:
    chalisa_data = json.load(f)

# Order of deities on home page
order = [
    'hanuman', 'ganesh', 'shiva', 'krishna', 'rama', 'durga',
    'lakshmi', 'saraswati', 'surya', 'shani', 'khatushyam', 'ganga',
    'bhairav', 'gayatri', 'radha', 'vishnu', 'devi', 'sants'
]

cards_html = []
for k in order:
    coll = chalisa_data[k]
    count = len(coll['items'])
    count_str = f"{count} चालीसा" if count > 1 else "१ चालीसा"
    card = f'''          <!-- {k.capitalize()} -->
          <div class="aarti-preview-card home-chalisa-card" data-cat="{k}" onclick="window.openChalisaCollectionModal('{k}')">
            <div class="aarti-preview-img-wrap">
              <img src="{coll['img']}" onerror="this.src='{coll['fallbackImg']}';" alt="{coll['title']}" class="aarti-preview-img" />
            </div>
            <div class="aarti-preview-name">{coll['title'].replace(' संग्रह', '')}</div>
            <div class="aarti-preview-badge">{count_str}</div>
          </div>'''
    cards_html.append(card)

full_grid_html = "\n".join(cards_html)
print("Generated grid with", len(cards_html), "cards!")
print(full_grid_html[:600])
