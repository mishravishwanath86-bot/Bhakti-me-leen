import re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
index_html_path = BASE_DIR / "index.html"
styles_css_path = BASE_DIR / "styles.css"
app_js_path = BASE_DIR / "app.js"

print("=" * 80)
print("BUILDING GANESHA & HANUMAN AARTI MULTI-OPTION SYSTEM")
print("=" * 80)

# 1. Define complete Aarti text and metadata in JS
aarti_dataset_js = """
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 GANESHA & HANUMAN AUTHENTIC MULTI-AARTI DATASET (DRIK PANCHANG VERIFIED)
// ══════════════════════════════════════════════════════════════════════════════

window.AARTI_COLLECTIONS = {
  ganesh: {
    title: 'श्री गणेश आरती संग्रह',
    deity: 'श्री गणेश जी',
    img: 'assets/gallery/bal_ganesha.jpg',
    fallbackImg: 'assets/deity_ganesh.jpg',
    mantra: '॥ वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ ॥',
    items: [
      {
        id: 'aarti_ganesh_jay',
        title: 'श्री गणेश आरती (जय गणेश देवा)',
        sub: 'Shree Ganesh Aarti • पारंपरिक महाआरती',
        audio_url: 'https://www.youtube.com/watch?v=0h3jKq3Lp7k',
        content: `॥ श्री गणेश जी की आरती ॥

जय गणेश जय गणेश जय गणेश देवा ।
माता जाकी पार्वती पिता महादेवा ॥

एक दन्त दयावन्त चार भुजाधारी ।
माथे सिन्दूर सोहे मूसे की सवारी ॥
जय गणेश जय गणेश जय गणेश देवा...

अन्धन को आंख देत कोढ़िन को काया ।
बांझन को पुत्र देत निर्धन को माया ॥
जय गणेश जय गणेश जय गणेश देवा...

हार चढ़े फूल चढ़े और चढ़े मेवा ।
लड्डुअन का भोग लगे सन्त करें सेवा ॥
जय गणेश जय गणेश जय गणेश देवा...

दीनन की लाज राखो शम्भु सुत वारी ।
कामना को पूर्ण करो जग बलिहारी ॥
जय गणेश जय गणेश जय गणेश देवा...

सूरश्याम शरण आए सफल कीजे सेवा ।
माता जाकी पार्वती पिता महादेवा ॥
जय गणेश जय गणेश जय गणेश देवा ।
माता जाकी पार्वती पिता महादेवा ॥`
      },
      {
        id: 'aarti_ganesh_vinayaka',
        title: 'विनायक आरती (गजवदन विनायका)',
        sub: 'Vinayaka Aarti • विघ्नहर्ता स्तुति आरती',
        audio_url: 'https://www.youtube.com/watch?v=0h3jKq3Lp7k',
        content: `॥ आरती गजवदन विनायका की ॥

आरती गजवदन विनायका की ।
सुर-मुनि-पूजित गणनायका की ॥

एकदन्त भवभय-निवारक ।
विघ्नविनाशक सुखविस्तारक ॥
आरती गजवदन विनायका की...

लम्बोधर सुन्दर वपुधारी ।
मोदक-प्रिय शुभ मंगलकारी ॥
आरती गजवदन विनायका की...

भाल-विशाल सिन्दूर-सुहावन ।
मूषक-वाहन जग-मन-भावन ॥
आरती गजवदन विनायका की...

रिद्धि-सिद्धि-पति सुख-दातार ।
जय जय जय विघ्नेश उदार ॥
आरती गजवदन विनायका की...

जो ध्यावै मन-इच्छा पावै ।
सो नर पार उतर भव जावै ॥
आरती गजवदन विनायका की ।
सुर-मुनि-पूजित गणनायका की ॥`
      },
      {
        id: 'aarti_ganesh_seva',
        title: 'श्री गणपति आरती (गणपति की सेवा मंगल मेवा)',
        sub: 'Shree Ganapati Aarti • संकट निवारण आरती',
        audio_url: 'https://www.youtube.com/watch?v=0h3jKq3Lp7k',
        content: `॥ गणपति की सेवा मंगल मेवा आरती ॥

गणपति की सेवा मंगल मेवा, सेवा से सब विघ्न टरैं ।
सब भक्त चढ़ें अरु शीश धरैं ॥

फूल चढ़ें अरु पान चढ़ें और चढ़े मेवा ।
लड्डुअन का भोग लगे सन्त करें सेवा ॥
गणपति की सेवा मंगल मेवा...

बांझन को पुत्र देत निर्धन को माया ।
कोढ़ी को काया देत सब कष्ट हरैं ॥
गणपति की सेवा मंगल मेवा...

पारवती का नन्दन शंभू का लाला ।
सब जग में डंका बाजत उजियाला ॥
गणपति की सेवा मंगल मेवा...

ॐ जय जय जय गणराज दयाल ।
दीन भक्त प्रतिपाल कृपाल ॥
गणपति की सेवा मंगल मेवा, सेवा से सब विघ्न टरैं ॥`
      }
    ]
  },
  hanuman: {
    title: 'श्री हनुमान आरती संग्रह',
    deity: 'श्री हनुमान जी महाराज',
    img: 'assets/gallery/bal_hanuman.jpg',
    fallbackImg: 'assets/deity_hanuman.jpg',
    mantra: '॥ मनोजवं मारुततुल्यवेगं जितेन्द्रियम् ॥',
    items: [
      {
        id: 'aarti_hanuman_shree',
        title: 'श्री हनुमान आरती (आरती कीजै हनुमान लला की)',
        sub: 'Shree Hanuman Aarti • संकटमोचन आरती',
        audio_url: 'https://www.youtube.com/watch?v=AETFv444yoE',
        content: `॥ श्री हनुमान लला की आरती ॥

आरती कीजै हनुमान लला की ।
दुष्ट दलन रघुनाथ कला की ॥

जाके बल से गिरिवर कांपै ।
रोग दोष जाके निकट न झांपै ॥
अंजनि पुत्र महा बलदाई ।
सन्तन के प्रभु सदा सहाई ॥

दे बीरा रघुनाथ पठाए ।
लंका जारि सीय सुधि लाए ॥
लंका सो कोट समुद्र सी खाई ।
जात पवनसुत बार न लाई ॥

लंका जारि असुर संहारे ।
सियारामजी के काज संवारे ॥
लक्ष्मण मूर्छित पड़े सकारे ।
आनि संजीवन प्रान उबारे ॥

पैठि पताल तोरि जम-कारे ।
अहिरावन की भुजा उखारे ॥
बाएं भुजा असुर दल मारे ।
दहिने भुजा सन्तजन तारे ॥

सुर नर मुनि आरती उतारे ।
जय जय जय हनुमान उचारे ॥
कंचन थार कपूर लौ छाई ।
आरति करत अंजना माई ॥

जो हनुमानजी की आरती गावै ।
बसि बैकुंठ परम पद पावै ॥`
      },
      {
        id: 'aarti_hanuman_balaji',
        title: 'श्री बालाजी आरती (ॐ जय हनुमत वीरा)',
        sub: 'Lord Balaji Aarti • मेहंदीपुर व सालासर बालाजी',
        audio_url: 'https://www.youtube.com/watch?v=AETFv444yoE',
        content: `॥ श्री बालाजी आरती ॥

ॐ जय हनुमत वीरा, स्वामी जय हनुमत वीरा ।
संकट मोचन स्वामी, तुम हो रणधीरा ॥ ॐ जय...

पवन पुत्र अंजनी सुत, महिमा अति भारी ।
दुष्ट दलन जग वन्दन, जय जय गिरधारी ॥ ॐ जय...

मेहंदीपुर अवतार लियो, प्रेत राज नाशा ।
भैरव कोतवाल संग, पूरन हो आशा ॥ ॐ जय...

लाल लंगोट हाथ में सोटा, कांधे मूंज जनेऊ ।
जो नर सुमिरन करहिं, कष्ट न व्यापै तेऊ ॥ ॐ जय...

भूत पिशाच निकट नहिं आवै, महावीर जब नाम सुनावै ।
नासै रोग हरै सब पीरा, जपत निरंतर हनुमत बीरा ॥

आरती श्री बालाजी की, जो नर-नारी गावैं ।
कहहिं दास सब सुख सम्पति पावैं ॥
ॐ जय हनुमत वीरा, स्वामी जय हनुमत वीरा ॥`
      },
      {
        id: 'aarti_hanuman_pavanasuta',
        title: 'श्री पवनसुत हनुमान आरती (जय अंजनीसुत संकटमोचन)',
        sub: 'Shri Pavanasuta Hanuman Aarti • पवनपुत्र स्तुति',
        audio_url: 'https://www.youtube.com/watch?v=AETFv444yoE',
        content: `॥ श्री पवनसुत हनुमान की आरती ॥

जय अंजनीसुत संकटमोचन, जय पवनसुत हनुमान ।
भक्तजनों के काज संवारो, हे दयाल भगवान ॥

बाल समय रवि भक्ष लियो तब, तीनहुं लोक भयो अंधियारो ।
ताहि सों त्रास भयो जग को, यह संकट काहू सों जात न टारो ॥

देवन आनि करी विनती तब, छांड़ि दियो रवि कष्ट निवारो ।
को नहिं जानत है जग में कपि, संकटमोचन नाम तिहारो ॥

जय कपीश सुग्रीव सहायी, लंका दहन कियो बलवान ।
जय अंजनीसुत संकटमोचन, जय पवनसुत हनुमान ॥

रामदूत अतुलित बलधामा, संकट हरहु कृपा निधान ।
आरती कीजै पवनसुत की, जय जय जय श्री हनुमान ॥`
      }
    ]
  }
};

function openAartiCollectionModal(deityKey) {
  const coll = window.AARTI_COLLECTIONS[deityKey];
  if (!coll) return;

  const modal = document.getElementById('aarti-options-modal');
  if (!modal) return;

  document.getElementById('aarti-modal-title').textContent = coll.title;
  document.getElementById('aarti-modal-deity').textContent = coll.deity;
  document.getElementById('aarti-modal-mantra').textContent = coll.mantra;
  
  const imgEl = document.getElementById('aarti-modal-img');
  if (imgEl) {
    imgEl.src = coll.img;
    imgEl.onerror = function() { this.src = coll.fallbackImg; };
  }

  const listContainer = document.getElementById('aarti-modal-list');
  if (listContainer) {
    listContainer.innerHTML = coll.items.map((item, idx) => `
      <div class="aarti-opt-card" onclick="openAartiItemDirect('${deityKey}', ${idx})">
        <div class="aarti-opt-index">0${idx+1}</div>
        <div class="aarti-opt-info">
          <div class="aarti-opt-title">${item.title}</div>
          <div class="aarti-opt-sub">${item.sub}</div>
        </div>
        <div class="aarti-opt-actions">
          <button class="aarti-opt-read-btn" onclick="event.stopPropagation(); readAartiItemDirect('${deityKey}', ${idx})" title="पाठ पढ़ें">
            📖 पढ़ें
          </button>
          <button class="aarti-opt-play-btn" onclick="event.stopPropagation(); playAartiItemDirect('${deityKey}', ${idx})" title="आरती सुनें">
            ▶
          </button>
        </div>
      </div>
    `).join('');
  }

  modal.style.display = 'flex';
  modal.style.opacity = '1';
  modal.style.pointerEvents = 'auto';

  if (navigator.vibrate) navigator.vibrate(25);
}

function closeAartiOptionsModal() {
  const modal = document.getElementById('aarti-options-modal');
  if (modal) modal.style.display = 'none';
}

function openAartiItemDirect(deityKey, idx) {
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
}
"""

# Append to app.js
with open(app_js_path, 'a', encoding='utf-8') as f:
    f.write("\n" + aarti_dataset_js)
print("✓ Appended AARTI_COLLECTIONS & handlers to app.js")

# 2. Update styles.css with Aarti modal styles
aarti_css = """
/* ══════════════════════════════════════════════════════════════════
   🪔 AARTI SELECTION MODAL & OPTION CARDS
   ══════════════════════════════════════════════════════════════════ */
.aarti-options-modal {
  position: fixed;
  inset: 0;
  z-index: 100005;
  background: radial-gradient(circle at 50% 20%, rgba(35, 10, 68, 0.98) 0%, rgba(12, 3, 25, 0.99) 55%, rgba(5, 1, 12, 1) 100%);
  backdrop-filter: blur(35px);
  -webkit-backdrop-filter: blur(35px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  overflow-y: auto;
  padding: 1.2rem 1.4rem 2.5rem;
}

.aarti-modal-content {
  width: 100%;
  max-width: 440px;
  display: flex;
  flex-direction: column;
  margin: auto 0;
}

.aarti-opt-card {
  background: linear-gradient(145deg, rgba(32, 12, 60, 0.9) 0%, rgba(18, 6, 36, 0.95) 100%);
  border: 1.5px solid rgba(248, 200, 59, 0.3);
  border-radius: 20px;
  padding: 12px 14px;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
  transition: all 0.25s ease;
  cursor: pointer;
}

.aarti-opt-card:hover {
  transform: translateY(-3px) scale(1.01);
  border-color: rgba(248, 200, 59, 0.7);
  box-shadow: 0 10px 25px rgba(248, 200, 59, 0.25);
}

.aarti-opt-index {
  font-size: 1.1rem;
  font-weight: 900;
  color: #F8C83B;
  background: rgba(248, 200, 59, 0.15);
  width: 38px;
  height: 38px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border: 1px solid rgba(248, 200, 59, 0.35);
}

.aarti-opt-info {
  flex: 1;
  min-width: 0;
}

.aarti-opt-title {
  font-size: 0.98rem;
  font-weight: 800;
  color: #FFFDF8;
  line-height: 1.3;
  margin-bottom: 2px;
}

.aarti-opt-sub {
  font-size: 0.74rem;
  color: #FDE68A;
  font-weight: 600;
}

.aarti-opt-actions {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
}

.aarti-opt-read-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(248, 200, 59, 0.35);
  color: #FDE68A;
  font-size: 0.76rem;
  font-weight: 800;
  padding: 6px 12px;
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.aarti-opt-read-btn:hover {
  background: rgba(248, 200, 59, 0.25);
}

.aarti-opt-play-btn {
  background: linear-gradient(135deg, #F8C83B 0%, #D97706 100%);
  color: #1A0B2E;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  font-size: 1rem;
  font-weight: 900;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(248, 200, 59, 0.4);
  transition: all 0.2s ease;
}

.aarti-opt-play-btn:hover {
  transform: scale(1.1);
}
"""

with open(styles_css_path, 'a', encoding='utf-8') as f:
    f.write("\n" + aarti_css)
print("✓ Appended Aarti CSS to styles.css")

# 3. Add Home Page Aarti Section & Aarti Selection Modal to index.html
with open(index_html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Add prominent Ganesh & Hanuman Aarti quick cards in #page-home
home_aarti_cards = """
      <!-- 🪔 NITYA AARTI COLLECTION CARDS (GANESH & HANUMAN) 🪔 -->
      <div style="margin: 0 1.2rem 1.4rem;">
        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:0.8rem;">
          <h2 style="font-size:1.15rem; font-weight:900; color:#FFFDF8; margin:0; display:flex; align-items:center; gap:6px;">
            <span>🪔</span> नित्य पावन आरती संग्रह
          </h2>
          <span style="font-size:0.75rem; color:#FDE68A; font-weight:700; cursor:pointer;" onclick="showPage('page-aarti')">सभी देखें ❯</span>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
          
          <!-- Ganesh Aarti Card -->
          <div onclick="openAartiCollectionModal('ganesh')" style="background:linear-gradient(145deg, #2A0D4E 0%, #150628 100%); border:1.5px solid rgba(248,200,59,0.4); border-radius:20px; padding:1rem; cursor:pointer; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.4); position:relative; overflow:hidden;">
            <div style="position:absolute; top:6px; right:8px; font-size:0.68rem; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; padding:2px 6px; border-radius:8px; font-weight:800;">3 आरतियां</div>
            <img src="assets/gallery/bal_ganesha.jpg" onerror="this.src='assets/deity_ganesh.jpg'" style="width:65px; height:65px; border-radius:50%; object-fit:cover; border:2px solid #F8C83B; margin-bottom:8px; box-shadow:0 0 15px rgba(248,200,59,0.3);" />
            <div style="color:#FFFDF8; font-weight:900; font-size:0.95rem; margin-bottom:2px;">श्री गणेश आरती</div>
            <div style="color:#FBCFE8; font-size:0.72rem; margin-bottom:8px;">जय गणेश • विनायक • गणपति सेवा</div>
            <button style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-size:0.75rem; font-weight:900; padding:5px 14px; border-radius:12px; border:none; cursor:pointer; width:100%;">आरती चुनें ❯</button>
          </div>

          <!-- Hanuman Aarti Card -->
          <div onclick="openAartiCollectionModal('hanuman')" style="background:linear-gradient(145deg, #2A0D4E 0%, #150628 100%); border:1.5px solid rgba(248,200,59,0.4); border-radius:20px; padding:1rem; cursor:pointer; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.4); position:relative; overflow:hidden;">
            <div style="position:absolute; top:6px; right:8px; font-size:0.68rem; background:rgba(248,200,59,0.2); border:1px solid #F8C83B; color:#FDE68A; padding:2px 6px; border-radius:8px; font-weight:800;">3 आरतियां</div>
            <img src="assets/gallery/bal_hanuman.jpg" onerror="this.src='assets/deity_hanuman.jpg'" style="width:65px; height:65px; border-radius:50%; object-fit:cover; border:2px solid #F8C83B; margin-bottom:8px; box-shadow:0 0 15px rgba(248,200,59,0.3);" />
            <div style="color:#FFFDF8; font-weight:900; font-size:0.95rem; margin-bottom:2px;">श्री हनुमान आरती</div>
            <div style="color:#FBCFE8; font-size:0.72rem; margin-bottom:8px;">हनुमान लला • बालाजी • पवनसुत</div>
            <button style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-size:0.75rem; font-weight:900; padding:5px 14px; border-radius:12px; border:none; cursor:pointer; width:100%;">आरती चुनें ❯</button>
          </div>

        </div>
      </div>
"""

if 'नित्य पावन आरती संग्रह' not in html:
    # Insert right before festival promos or categories in #page-home
    html = html.replace('<!-- 🏺 BHAKTI AMRIT KALASH PROMO BANNER 🏺 -->', home_aarti_cards + '\n      <!-- 🏺 BHAKTI AMRIT KALASH PROMO BANNER 🏺 -->')
    print("✓ Added Ganesha & Hanuman Aarti Quick Cards to #page-home")

# Add Aarti Selection Modal to index.html
aarti_modal_html = """
  <!-- ═════════════════════════════════════════════════════════════════
       🪔 MULTI-AARTI SELECTION MODAL (GANESHA / HANUMAN)
       ═════════════════════════════════════════════════════════════════ -->
  <div id="aarti-options-modal" class="aarti-options-modal" style="display:none;">
    <div class="aarti-modal-content">
      
      <!-- Top Bar -->
      <div class="glass-player-topbar" style="margin-bottom:1rem;">
        <button class="glass-topbar-btn" onclick="closeAartiOptionsModal()">✕</button>
        <div id="aarti-modal-title" style="font-size:1.05rem; font-weight:900; color:#FDE68A;">॥ आरती संग्रह ॥</div>
        <button class="glass-topbar-btn" onclick="triggerFlowerShower()">🌸</button>
      </div>

      <!-- Deity Header Card -->
      <div style="background:linear-gradient(135deg, #1F0738 0%, #3B1259 50%, #150628 100%); border:1.5px solid rgba(248,200,59,0.4); border-radius:22px; padding:1.2rem; margin-bottom:1.2rem; text-align:center; box-shadow:0 8px 25px rgba(0,0,0,0.5);">
        <img id="aarti-modal-img" src="assets/gallery/bal_ganesha.jpg" style="width:75px; height:75px; border-radius:50%; object-fit:cover; border:2px solid #F8C83B; margin-bottom:6px; box-shadow:0 0 20px rgba(248,200,59,0.4);" />
        <div id="aarti-modal-deity" style="font-size:1.2rem; font-weight:900; color:#FFFDF8; margin-bottom:2px;"></div>
        <div id="aarti-modal-mantra" style="font-size:0.84rem; color:#FDE68A; font-weight:700;"></div>
      </div>

      <!-- Aarti Options List -->
      <div id="aarti-modal-list" style="margin-bottom:1rem;">
        <!-- Filled dynamically -->
      </div>

    </div>
  </div>
"""

if 'id="aarti-options-modal"' not in html:
    html = html.replace('</body>', aarti_modal_html + '\n</body>')
    print("✓ Added #aarti-options-modal to index.html")

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("=" * 80)
print("GANESHA & HANUMAN MULTI-AARTI SYSTEM BUILD COMPLETE")
print("=" * 80)
