import re
import json

# Define the full Drik Panchang data for Jai Ganesh Deva
ganesh_drik_item = {
    "id": "drik_ganesh_1",
    "title": "जय गणेश जय गणेश देवा",
    "title_en": "Jai Ganesh Deva (Shree Ganesh Aarti)",
    "en_line": "Jai Ganesh Jai Ganesh Deva",
    "hi_line": "जय गणेश जय गणेश देवा",
    "sub": "माता जाकी पार्वती पिता महादेवा • Drik Panchang Verified",
    "thumb": "assets/gallery/bal_ganesha_little.jpg",
    "audio_url": "https://www.youtube.com/watch?v=ty_BRH3b9lY",
    "video_id": "ty_BRH3b9lY",
    "drik_url": "https://www.drikpanchang.com/lyrics/aarti/shree-ganesh/jay-ganesh-aarti.html?lang=hi&ck=1",
    "source": "Drik Panchang Verified (द्रिक पञ्चाङ्ग प्रमाणिक)",
    "content": """॥ श्री गणेशजी की आरती ॥

जय गणेश, जय गणेश, जय गणेश देवा।
माता जाकी पार्वती, पिता महादेवा॥ (x2)

एकदन्त दयावन्त, चार भुजाधारी।
माथे पर तिलक सोहे, मूसे की सवारी॥ (x2)
(माथे पर सिन्दूर सोहे, मूसे की सवारी॥)

पान चढ़े फूल चढ़े, और चढ़े मेवा।
(हार चढ़े, फूल चढ़े, और चढ़े मेवा।)
लड्डुअन का भोग लगे, सन्त करें सेवा॥ (x2)

जय गणेश, जय गणेश, जय गणेश देवा।
माता जाकी पार्वती, पिता महादेवा॥ (x2)

अँधे को आँख देत, कोढ़िन को काया।
बाँझन को पुत्र देत, निर्धन को माया॥ (x2)

'सूर' श्याम शरण आए, सफल कीजे सेवा।
माता जाकी पार्वती, पिता महादेवा॥ (x2)

(दीनन की लाज राखो, शम्भु सुतवारी।
कामना को पूर्ण करो, जग बलिहारी॥ x2)

जय गणेश, जय गणेश, जय गणेश देवा।
माता जाकी पार्वती, पिता महादेवा॥ (x2)""",
    "meaning": """🌺 श्लोकवार सम्पूर्ण भावार्थ (Drik Panchang Meaning) 🌺

• जय गणेश, जय गणेश, जय गणेश देवा। माता जाकी पार्वती, पिता महादेवा॥
भावार्थ: हे विघ्नहर्ता प्रथम पूज्य भगवान श्री गणेश! आपकी सदा ही जय हो, जय हो, जय हो देवा! आपकी माता सम्पूर्ण जगत की जननी माँ पार्वती हैं और आपके पिता देवाधिदेव महादेव भगवान शिव शंकर हैं।

• एकदन्त दयावन्त, चार भुजाधारी। माथे पर तिलक (सिन्दूर) सोहे, मूसे की सवारी॥
भावार्थ: आप एक दन्त (एकदन्त) से सुशोभित हैं, परम दयालु (दयावन्त) हैं और चार भुजाओं वाले हैं। आपके पावन मस्तक पर चन्दन एवं सिन्दूर का भव्य तिलक सुशोभित है और आपका प्रिय वाहन मूषकराज (मूसा) है।

• पान चढ़े फूल चढ़े, और चढ़े मेवा (हार चढ़े...)। लड्डुअन का भोग लगे, सन्त करें सेवा॥
भावार्थ: भक्तजन आपकी सेवा में तांबूल (पान), पुष्प, सुगंधित पुष्पहार और उत्तम मेवे अर्पित करते हैं। आपको मोदक एवं लड्डुओं का भोग अति प्रिय है और सभी संत, मुनि व भक्तजन निष्काम प्रेमभाव से आपकी सेवा करते हैं।

• अँधे को आँख देत, कोढ़िन को काया। बाँझन को पुत्र देत, निर्धन को माया॥
भावार्थ: आप शरणागत वत्सल व दयानिधान हैं; दृष्टिहीनों को दिव्य दृष्टि (आँख) प्रदान करते हैं, व्याधिग्रस्त (कोढ़ आदि से पीड़ित) जनों को स्वस्थ व सुन्दर काया देते हैं, निःसन्तान को सुयोग्य संतान का वरदान देते हैं और निर्धनों को धन-सम्पदा व वैभव (माया) से परिपूर्ण करते हैं।

• 'सूर' श्याम शरण आए, सफल कीजे सेवा। दीनन की लाज राखो, शम्भु सुतवारी। कामना को पूर्ण करो, जग बलिहारी॥
भावार्थ: भक्त सूरदास एवं प्रभु श्याम की शरण में आए समस्त भक्तजन करबद्ध प्रार्थना करते हैं कि हे दयानिधान, हमारी सेवा व आराधना को सफल कीजिए। हे भगवान शिव के पुत्र (शम्भु सुतवारी)! हम दीन-दुखियों की लाज रखिए, हमारी सभी शुभ व सात्विक मनोकामनाओं को पूर्ण कीजिए, संपूर्ण संसार आपके चरणों में नतमस्तक व बलिहारी जाता है।""",
    "vidhi": """🪔 श्री गणेश आरती विधि एवं नियम (Drik Panchang Verified) 🪔

1. आरती का समय: भगवान गणेश जी की आरती प्रातः एवं सायं कालीन दैनिक पूजा के अंत में तथा बुधवार, विनायक चतुर्थी, संकष्टी चतुर्थी और गणेशोत्सव पर विशेष रूप से की जाती है।
2. आवश्यक सामग्री: पीतल या तांबे की थाली, शुद्ध देसी घी का दीपक (पंचमुखी या एकमुखी) अथवा शुद्ध भीमसेनी कपूर, रोली-चन्दन, अक्षत, 21 दूर्वा दल, लाल पुष्प (गुड़हल/गेंदा), मोदक अथवा बेसन के लड्डू।
3. थाली घुमाने की शास्त्रीय विधि:
   - 4 बार भगवान श्री गणेश जी के पावन चरणों में घुमाएं।
   - 2 बार नाभि प्रदेश के सम्मुख घुमाएं।
   - 1 बार मुखारविन्द के सम्मुख घुमाएं।
   - 7 बार सम्पूर्ण विग्रह के चारों ओर घड़ी की सुई की दिशा (Clockwise) में 'ॐ' आकार में घुमाएं।
4. वाद्य एवं स्वर: आरती के समय शुद्ध भाव से शंख, घंटी और मंजीरे की मंगल ध्वनि के साथ सस्वर आरती गान करें।
5. पुष्पांजलि व आचमन: आरती के उपरांत थाली के चारों ओर तीन बार जल का आचमन कराएं, हाथ जोड़कर पुष्पांजलि अर्पित करें और दोनों हाथों से आरती की पवित्र ज्योति ग्रहण करें।""",
    "significance": """✨ श्री गणेश आरती का धार्मिक महत्त्व एवं फलश्रुति ✨

• विघ्न निवारण: भगवान गणेश प्रथम पूज्य देव हैं। किसी भी नए कार्य, व्यापार, गृह प्रवेश या शुभ अनुष्ठान से पूर्व इनकी आरती करने से समस्त विघ्न-बाधाएं स्वतः समाप्त हो जाती हैं।
• ऋद्धि-सिद्धि व सुख-शांति: नित्य श्रद्धापूर्वक श्री गणेश आरती करने से घर में ज्ञान, बुद्धि, विवेक, ऋद्धि-सिद्धि और अष्ट-सिद्धियों का वास होता है।
• वास्तु दोष व नकारात्मकता शमन: नित्य प्रातः-सायं इस आरती के श्रवण व गायन से घर का वातावरण पवित्र एवं सकारात्मक ऊर्जा से भर जाता है।""",
    "english_lyrics": """॥ Shree Ganeshji Ki Aarti ॥

Jai Ganesh, Jai Ganesh, Jai Ganesh Deva।
Mata Jaki Parvati, Pita Mahadeva॥ (x2)

Ekadanta Dayavanta, Char Bhujadhari।
Mathe Par Tilak Sohe, Muse Ki Sawari॥ (x2)
(Mathe Par Sindoor Sohe, Muse Ki Sawari॥)

Paan Chadhe Phool Chadhe, Aur Chadhe Mewa।
(Haar Chadhe, Phool Chadhe, Aur Chadhe Mewa।)
Ladduan Ka Bhog Lage, Sant Karein Sewa॥ (x2)

Jai Ganesh, Jai Ganesh, Jai Ganesh Deva।
Mata Jaki Parvati, Pita Mahadeva॥ (x2)

Andhe Ko Aankh Det, Kodhin Ko Kaya।
Banjhan Ko Putra Det, Nirdhan Ko Maya॥ (x2)

'Soor' Shyam Sharan Aaye, Safal Kije Sewa।
Mata Jaki Parvati, Pita Mahadeva॥ (x2)

(Deenan Ki Laaj Rakho, Shambhu Sutwari।
Kamna Ko Purna Karo, Jag Balihari॥ x2)

Jai Ganesh, Jai Ganesh, Jai Ganesh Deva।
Mata Jaki Parvati, Pita Mahadeva॥ (x2)"""
}

# 1. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the drik_ganesh_1 definition in AARTI_COLLECTIONS
old_pattern = r'\{\s*"id":\s*"drik_ganesh_1"[\s\S]*?"content":\s*"॥ श्री गणेश जी की आरती[\s\S]*?\}\s*,'
new_item_json = json.dumps(ganesh_drik_item, ensure_ascii=False, indent=8) + ','

if re.search(old_pattern, js):
    js = re.sub(old_pattern, new_item_json, js, count=1)
    print("[OK] Replaced drik_ganesh_1 in app.js with full Drik Panchang data")
else:
    print("! Regex pattern didn't match, trying direct search")
    s_idx = js.find('"id": "drik_ganesh_1"')
    if s_idx != -1:
        # find the start of the object {
        obj_start = js.rfind('{', 0, s_idx)
        # find the end of the object },
        next_id = js.find('"id": "drik_ganesh_2"', s_idx)
        obj_end = js.rfind('}', 0, next_id) + 1
        # include trailing comma
        if js[obj_end] == ',':
            obj_end += 1
        js = js[:obj_start] + new_item_json + js[obj_end:]
        print("[OK] Directly replaced drik_ganesh_1 in app.js")

# 2. Add complete reader and player controllers if not already present
reader_controllers = """
// ══════════════════════════════════════════════════════════════════════════════
// 🪔 DRIK PANCHANG VERIFIED AARTI ITEM READER & PLAYER CONTROLLERS
// ══════════════════════════════════════════════════════════════════════════════

window.switchAartiReaderTab = function(tabName) {
  document.querySelectorAll('.aarti-tab-btn').forEach(btn => {
    if (btn.getAttribute('data-tab') === tabName) {
      btn.style.background = 'linear-gradient(135deg, #F8C83B, #D97706)';
      btn.style.color = '#1A0B2E';
      btn.style.fontWeight = '900';
      btn.style.border = 'none';
      btn.style.boxShadow = '0 2px 10px rgba(248,200,59,0.4)';
    } else {
      btn.style.background = 'rgba(255,255,255,0.08)';
      btn.style.color = '#FDE68A';
      btn.style.fontWeight = '700';
      btn.style.border = '1px solid rgba(248,200,59,0.3)';
      btn.style.boxShadow = 'none';
    }
  });

  document.querySelectorAll('.aarti-tab-pane').forEach(pane => {
    pane.style.display = (pane.id === 'aarti-pane-' + tabName) ? 'block' : 'none';
  });
};

window.readAartiItemDirect = function(deityKey, idx, initialMode) {
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items || !coll.items[idx]) {
    console.warn("Aarti item not found:", deityKey, idx);
    return;
  }
  const item = coll.items[idx];

  // Close modal if open
  const modal = document.getElementById('aarti-options-modal');
  if (modal) {
    modal.classList.remove('active');
    modal.style.display = 'none';
  }

  // 1. Set Header Title
  const titleEl = document.getElementById('reader-page-title');
  if (titleEl) titleEl.textContent = item.title || coll.title;

  // 2. Set Deity Image & Audio Titles
  const deityImg = document.getElementById('reader-deity-img');
  if (deityImg) {
    deityImg.src = item.thumb || coll.img || coll.fallbackImg || 'assets/deity_ganesh.jpg';
    deityImg.onerror = function() { this.src = coll.fallbackImg || 'assets/deity_ganesh.jpg'; };
  }

  const aTitleEl = document.getElementById('reader-audio-title');
  if (aTitleEl) aTitleEl.textContent = item.hi_line || item.title;

  const aSubEl = document.getElementById('reader-audio-sub');
  if (aSubEl) aSubEl.textContent = `${coll.deity || 'सनातन'} • ${item.sub || 'Drik Panchang Verified'}`;

  // 3. Set Back Button Target
  window.readerBackPage = (typeof currentPage !== 'undefined' && currentPage !== 'page-reader') ? currentPage : 'page-home';
  const backBtn = document.querySelector('#page-reader .back-btn');
  if (backBtn) {
    backBtn.onclick = () => window.showPage(window.readerBackPage || 'page-home');
  }

  // 4. Render Video Container if available
  const ytContainer = document.getElementById('reader-youtube-container');
  if (ytContainer) {
    if (item.video_id) {
      ytContainer.style.display = 'block';
      ytContainer.innerHTML = `
        <div style="max-width:680px; margin:0 auto 1.2rem; border-radius:18px; overflow:hidden; border:1.5px solid rgba(248,200,59,0.45); box-shadow:0 8px 25px rgba(0,0,0,0.6); position:relative; background:#000;">
          <iframe width="100%" height="220" src="https://www.youtube.com/embed/${item.video_id}?autoplay=0&rel=0" title="${item.title}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="display:block; width:100%; border:none;"></iframe>
          <div style="padding:6px 12px; background:rgba(26,11,46,0.95); font-size:0.75rem; color:#FDE68A; display:flex; align-items:center; justify-content:space-between;">
            <span>🎬 Drik Panchang Official Aarti Video</span>
            <span style="color:#FBCFE8; font-size:0.7rem;">अनुराधा पौडवाल • टी-सीरीज़</span>
          </div>
        </div>
      `;
    } else {
      ytContainer.style.display = 'none';
      ytContainer.innerHTML = '';
    }
  }

  // 5. Render Full Drik Panchang Scripture & Meaning Tabs
  const readerContent = document.getElementById('reader-cosmic-content') || document.getElementById('reader-content');
  if (readerContent) {
    const hasMeaning = !!item.meaning;
    const hasVidhi = !!item.vidhi;
    const hasSig = !!item.significance;
    const hasEn = !!item.english_lyrics;

    readerContent.innerHTML = `
      <div class="pure-reader-wrapper" style="padding:0.8rem 0 3rem; text-align:center;">
        
        <!-- Header Badge -->
        <div style="font-size:0.82rem; color:#FDE68A; font-weight:800; margin-bottom:0.5rem; background:rgba(248,200,59,0.18); display:inline-flex; align-items:center; gap:6px; padding:5px 16px; border-radius:16px; border:1.2px solid rgba(248,200,59,0.45); box-shadow:0 0 12px rgba(248,200,59,0.25);">
          <span>🪔</span> ${coll.deity} • ${item.source || 'द्रिक पञ्चाङ्ग प्रमाणिक'}
        </div>

        <h1 style="font-size:1.4rem; color:#FFFDF8; font-weight:900; margin:0.4rem 0 1rem; text-shadow:0 2px 8px rgba(0,0,0,0.8);">
          ॥ ${item.hi_line || item.title} ॥
        </h1>

        <!-- Navigation Tabs -->
        <div style="display:flex; gap:8px; overflow-x:auto; padding:0.4rem 0.6rem 1rem; margin-bottom:1rem; justify-content:center; flex-wrap:wrap; scrollbar-width:none;">
          <button class="aarti-tab-btn active" data-tab="lyrics" onclick="window.switchAartiReaderTab('lyrics')" style="padding:6px 14px; border-radius:16px; font-size:0.78rem; white-space:nowrap; cursor:pointer; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; font-weight:900; border:none; box-shadow:0 2px 10px rgba(248,200,59,0.4); transition:all 0.2s ease;">
            📜 आरती पाठ
          </button>
          ${hasMeaning ? `
          <button class="aarti-tab-btn" data-tab="meaning" onclick="window.switchAartiReaderTab('meaning')" style="padding:6px 14px; border-radius:16px; font-size:0.78rem; white-space:nowrap; cursor:pointer; background:rgba(255,255,255,0.08); color:#FDE68A; font-weight:700; border:1px solid rgba(248,200,59,0.3); transition:all 0.2s ease;">
            🌺 सम्पूर्ण भावार्थ
          </button>` : ''}
          ${hasVidhi ? `
          <button class="aarti-tab-btn" data-tab="vidhi" onclick="window.switchAartiReaderTab('vidhi')" style="padding:6px 14px; border-radius:16px; font-size:0.78rem; white-space:nowrap; cursor:pointer; background:rgba(255,255,255,0.08); color:#FDE68A; font-weight:700; border:1px solid rgba(248,200,59,0.3); transition:all 0.2s ease;">
            🪔 आरती विधि व नियम
          </button>` : ''}
          ${hasSig ? `
          <button class="aarti-tab-btn" data-tab="sig" onclick="window.switchAartiReaderTab('sig')" style="padding:6px 14px; border-radius:16px; font-size:0.78rem; white-space:nowrap; cursor:pointer; background:rgba(255,255,255,0.08); color:#FDE68A; font-weight:700; border:1px solid rgba(248,200,59,0.3); transition:all 0.2s ease;">
            ✨ महत्त्व व फलश्रुति
          </button>` : ''}
          ${hasEn ? `
          <button class="aarti-tab-btn" data-tab="en" onclick="window.switchAartiReaderTab('en')" style="padding:6px 14px; border-radius:16px; font-size:0.78rem; white-space:nowrap; cursor:pointer; background:rgba(255,255,255,0.08); color:#FDE68A; font-weight:700; border:1px solid rgba(248,200,59,0.3); transition:all 0.2s ease;">
            🔤 English
          </button>` : ''}
        </div>

        <!-- Tab 1: Lyrics Pane -->
        <div id="aarti-pane-lyrics" class="aarti-tab-pane" style="display:block;">
          <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:1.5rem 1rem; max-width:680px; margin:0 auto; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div style="font-family:'Tiro Devanagari Hindi', 'Georgia', serif; font-size:1.22rem; line-height:2.3; color:#FFFDF8; font-weight:700; white-space:pre-line; text-shadow:0 1px 4px rgba(0,0,0,0.8);">
${item.content}
            </div>
          </div>
        </div>

        <!-- Tab 2: Meaning Pane -->
        ${hasMeaning ? `
        <div id="aarti-pane-meaning" class="aarti-tab-pane" style="display:none;">
          <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:1.5rem 1.2rem; max-width:680px; margin:0 auto; text-align:left; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div style="font-family:'Inter', sans-serif; font-size:0.95rem; line-height:1.9; color:#FEF3C7; font-weight:500; white-space:pre-line;">
${item.meaning}
            </div>
          </div>
        </div>` : ''}

        <!-- Tab 3: Vidhi Pane -->
        ${hasVidhi ? `
        <div id="aarti-pane-vidhi" class="aarti-tab-pane" style="display:none;">
          <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:1.5rem 1.2rem; max-width:680px; margin:0 auto; text-align:left; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div style="font-family:'Inter', sans-serif; font-size:0.95rem; line-height:1.9; color:#FEF3C7; font-weight:500; white-space:pre-line;">
${item.vidhi}
            </div>
          </div>
        </div>` : ''}

        <!-- Tab 4: Significance Pane -->
        ${hasSig ? `
        <div id="aarti-pane-sig" class="aarti-tab-pane" style="display:none;">
          <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:1.5rem 1.2rem; max-width:680px; margin:0 auto; text-align:left; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div style="font-family:'Inter', sans-serif; font-size:0.95rem; line-height:1.9; color:#FEF3C7; font-weight:500; white-space:pre-line;">
${item.significance}
            </div>
          </div>
        </div>` : ''}

        <!-- Tab 5: English Lyrics Pane -->
        ${hasEn ? `
        <div id="aarti-pane-en" class="aarti-tab-pane" style="display:none;">
          <div style="background:rgba(255,255,255,0.04); border:1.5px solid rgba(248,200,59,0.3); border-radius:20px; padding:1.5rem 1rem; max-width:680px; margin:0 auto; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
            <div style="font-family:'Inter', sans-serif; font-size:1.05rem; line-height:2.1; color:#FFFDF8; font-weight:600; white-space:pre-line;">
${item.english_lyrics}
            </div>
          </div>
        </div>` : ''}

        <!-- Drik Panchang Verified Source Link Card -->
        ${item.drik_url ? `
        <div style="max-width:680px; margin:1.5rem auto 0; background:linear-gradient(135deg, rgba(217,119,6,0.18), rgba(120,53,15,0.22)); border:1.2px solid rgba(248,200,59,0.35); border-radius:16px; padding:1rem 1.2rem; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
          <div style="text-align:left;">
            <div style="color:#FDE68A; font-size:0.85rem; font-weight:800; display:flex; align-items:center; gap:6px;">
              <span>🌐</span> द्रिक पञ्चाङ्ग प्रमाणिक संदर्भ (Drik Panchang Verified)
            </div>
            <div style="color:#FBCFE8; font-size:0.75rem; margin-top:2px;">
              शास्त्रीय पाठ, गीतिकाव्य व वीडियो स्रोत
            </div>
          </div>
          <a href="${item.drik_url}" target="_blank" rel="noopener" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; text-decoration:none; font-weight:900; font-size:0.75rem; padding:6px 14px; border-radius:12px; display:inline-flex; align-items:center; gap:4px; box-shadow:0 2px 8px rgba(0,0,0,0.3);">
            द्रिक पञ्चाङ्ग पर देखें ↗
          </a>
        </div>` : ''}

        <!-- Interactive Action Buttons -->
        <div style="margin-top:1.8rem; display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
          <button onclick="triggerFlowerShower()" style="background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; font-weight:900; font-size:0.88rem; padding:10px 20px; border-radius:24px; cursor:pointer; box-shadow:0 4px 15px rgba(248,200,59,0.4); display:inline-flex; align-items:center; gap:6px;">
            🌸 पुष्प वर्षा करें
          </button>
          <button onclick="ringBell()" style="background:rgba(255,255,255,0.08); color:#FDE68A; border:1.5px solid rgba(248,200,59,0.35); font-weight:800; font-size:0.88rem; padding:10px 18px; border-radius:24px; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
            🔔 मन्दिर घंटी
          </button>
          <button onclick="shareDivineCard()" style="background:rgba(26,11,46,0.3); color:#FEF3C7; border:1.5px solid rgba(255,255,255,0.2); font-weight:800; font-size:0.88rem; padding:10px 18px; border-radius:24px; cursor:pointer; display:inline-flex; align-items:center; gap:6px;">
            📤 शेयर करें
          </button>
        </div>

      </div>
    `;
  }

  // 6. Open Reader Page
  window.showPage('page-reader');
  window.scrollTo(0, 0);
};

window.playAartiItemDirect = function(deityKey, idx) {
  // Directly launch reader in audio mode
  window.readAartiItemDirect(deityKey, idx, 'audio');
  
  // Also try playing audio via global play function if present
  const coll = window.AARTI_COLLECTIONS ? window.AARTI_COLLECTIONS[deityKey] : null;
  if (!coll || !coll.items || !coll.items[idx]) return;
  const item = coll.items[idx];
  
  if (typeof toggleReaderAudioPlay === 'function') {
    toggleReaderAudioPlay();
  }
};
"""

# Check if readAartiItemDirect is already in app.js
if "window.readAartiItemDirect =" in js:
    # Replace existing implementation
    p_start = js.find("window.readAartiItemDirect =")
    # find where next section or EOF is
    js = js[:p_start] + reader_controllers.strip() + "\n"
    print("[OK] Updated window.readAartiItemDirect in app.js")
else:
    js += "\n\n" + reader_controllers.strip() + "\n"
    print("[OK] Injected window.readAartiItemDirect into app.js")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Successfully written updated app.js")

# 3. Also update drik_app_addon.js if it exists
try:
    with open('drik_app_addon.js', 'r', encoding='utf-8') as f:
        addon_js = f.read()
    if re.search(old_pattern, addon_js):
        addon_js = re.sub(old_pattern, new_item_json, addon_js, count=1)
        with open('drik_app_addon.js', 'w', encoding='utf-8') as f:
            f.write(addon_js)
        print("[OK] Updated drik_ganesh_1 in drik_app_addon.js")
except Exception as e:
    print("drik_app_addon.js note:", e)

# 4. Also update json collections
for json_file in ['full_drik_aarti_collections.json', 'final_granular_aarti_collections.json']:
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if 'ganesh' in data and 'items' in data['ganesh'] and len(data['ganesh']['items']) > 0:
            data['ganesh']['items'][0] = ganesh_drik_item
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"[OK] Updated {json_file}")
    except Exception as e:
        print(f"Note for {json_file}:", e)
