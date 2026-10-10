/**
 * ═════════════════════════════════════════════════════════════════════
 * 🌸 ROYAL VEDIC DIVINE GALLERY ENGINE (गैलरी एवं तीर्थ दर्शन) 🌸
 * Features:
 *  - 100% Mobile Phone Responsive UI/UX
 *  - Intelligent Deity Search (supports "load shiva", "shiva", "krishna", etc.)
 *  - Daily 1-Image Download Quota with warning popup
 *  - AndroidBridge Native Save to Phone Gallery
 *  - Full Screen Divine Lightbox with sacred mantra & details
 * ═════════════════════════════════════════════════════════════════════
 */

(function() {
  window.galleryActiveTab = 'bal';
  window.galleryActiveCategory = 'all';
  window.currentGallerySearch = '';
  window.currentLightboxItem = null;

  // Synonyms dictionary for smart search
  const DEITY_SYNONYMS = {
    shiva: ['shiva', 'shiv', 'load shiva', 'lord shiva', 'mahadev', 'shankar', 'bholenath', 'bhole', 'rudra', 'neelkanth', 'शिव', 'महादेव', 'शंकर', 'भोलेनाथ', 'रुद्र'],
    krishna: ['krishna', 'load krishna', 'lord krishna', 'krishn', 'kanha', 'gopal', 'gopala', 'kanhaiya', 'shyam', 'govind', 'radhe', 'कृष्ण', 'कान्हा', 'गोपाल', 'माखनचोर', 'श्याम'],
    ram: ['ram', 'rama', 'load ram', 'lord ram', 'shri ram', 'sitaram', 'raghav', 'raghupati', 'ayodhya', 'राम', 'श्रीराम', 'सीताराम', 'राघव', 'रघुपति'],
    hanuman: ['hanuman', 'load hanuman', 'lord hanuman', 'bajrang', 'bajrangbali', 'maruti', 'anjaneya', 'sankatmochan', 'हनुमान', 'बजरंगबली', 'मारुति', 'संकटमोचन'],
    ganesh: ['ganesh', 'ganesha', 'load ganesh', 'lord ganesh', 'vinayak', 'ganpati', 'gajanan', 'गणेश', 'विनायक', 'गणपति', 'गजानन'],
    durga: ['durga', 'load durga', 'mata', 'ambe', 'sherawali', 'shakti', 'bhavani', 'kali', 'दुर्गा', 'अम्बे', 'माता', 'शेरावाली', 'भवानी'],
    lakshmi: ['lakshmi', 'laxmi', 'load lakshmi', 'mahalakshmi', 'लक्ष्मी', 'महालक्ष्मी'],
    saraswati: ['saraswati', 'sharada', 'veena', 'सरस्वती', 'शारदा'],
    surya: ['surya', 'sun', 'aditya', 'bhaskar', 'सूर्य', 'आदित्य'],
    vishnu: ['vishnu', 'narayana', 'hari', 'विष्णु', 'नारायण', 'हरि']
  };

  // Quota Management (1 Download Per Day)
  function getDailyQuota() {
    const today = new Date().toISOString().split('T')[0];
    const lastDate = localStorage.getItem('bhakti_last_image_dl_date');
    if (lastDate !== today) {
      localStorage.setItem('bhakti_last_image_dl_date', today);
      localStorage.setItem('bhakti_daily_image_dl_count', '0');
      return { count: 0, max: 1, remaining: 1, today: today };
    }
    const count = parseInt(localStorage.getItem('bhakti_daily_image_dl_count') || '0', 10);
    return { count: count, max: 1, remaining: Math.max(0, 1 - count), today: today };
  }

  window.updateGalleryQuotaBadge = function() {
    const badge = document.getElementById('gallery-quota-pill');
    if (!badge) return;
    const q = getDailyQuota();
    if (q.count >= 1) {
      badge.innerHTML = '🔒 दैनिक कोटा: 0/1 शेष (आज का कोटा पूर्ण • कल पुनः उपलब्ध)';
      badge.style.background = 'rgba(239, 68, 68, 0.2)';
      badge.style.borderColor = '#EF4444';
      badge.style.color = '#FCA5A5';
    } else {
      badge.innerHTML = '📥 दैनिक कोटा: 1/1 शेष • प्रतिदिन 1 दिव्य छवि निःशुल्क डाउनलोड';
      badge.style.background = 'rgba(248, 200, 59, 0.15)';
      badge.style.borderColor = '#F8C83B';
      badge.style.color = '#FDE68A';
    }
  };

  window.downloadDivineImage = function(imgUrl, imgName) {
    const q = getDailyQuota();
    if (q.count >= 1) {
      window.showDownloadQuotaAlert();
      return;
    }

    try {
      const cleanName = (imgName || 'divine_darshan').replace(/[^a-zA-Z0-9_\u0900-\u097F]/g, '_');

      // Native AndroidBridge save to device photo gallery
      if (window.AndroidBridge && typeof window.AndroidBridge.saveImageToGallery === 'function') {
        window.AndroidBridge.saveImageToGallery(imgUrl, cleanName);
      } else {
        // Web / HTML5 download fallback
        const a = document.createElement('a');
        a.href = imgUrl;
        a.download = cleanName + '.jpg';
        a.target = '_blank';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      }

      // Record daily count
      localStorage.setItem('bhakti_daily_image_dl_count', '1');
      window.updateGalleryQuotaBadge();

      if (typeof showToast === 'function') {
        showToast('✅ दिव्य छवि सफलतापूर्वक डाउनलोड हो गई! (आज का कोटा: 1/1 पूर्ण)');
      }
    } catch (e) {
      console.error('Download error:', e);
      window.open(imgUrl, '_blank');
    }
  };

  window.showDownloadQuotaAlert = function() {
    const modal = document.getElementById('gallery-quota-modal');
    if (modal) {
      modal.style.display = 'flex';
      modal.style.opacity = '1';
    } else {
      alert('⚠️ आज का कोटा पूरा हुआ!\nएक दिन में केवल 1 दिव्य छवि डाउनलोड कर सकते हैं। अगले दिन पुनः प्रयास करें।');
    }
    if (navigator.vibrate) navigator.vibrate([50, 70, 50]);
  };

  window.closeDownloadQuotaAlert = function() {
    const modal = document.getElementById('gallery-quota-modal');
    if (modal) {
      modal.style.display = 'none';
    }
  };

  // Smart Query Matcher
  function matchesQuery(item, query) {
    if (!query) return true;
    const q = query.trim().toLowerCase();

    const nameHi = (item.nameHi || '').toLowerCase();
    const nameEn = (item.nameEn || '').toLowerCase();
    const desc = (item.desc || item.famous || item.location || '').toLowerCase();

    // Direct string match
    if (nameHi.includes(q) || nameEn.includes(q) || desc.includes(q)) return true;

    // Clean prefix match (e.g. "load shiva" -> "shiva")
    const cleanQ = q.replace(/^(load|lord|shree|shri|bhagwan|jai|mata|maa)\s+/i, '').trim();
    if (cleanQ && (nameHi.includes(cleanQ) || nameEn.includes(cleanQ) || desc.includes(cleanQ))) return true;

    // Check synonym dictionary
    for (const [key, aliases] of Object.entries(DEITY_SYNONYMS)) {
      const qMatchesKey = aliases.some(alias => q.includes(alias) || alias.includes(q) || cleanQ.includes(alias));
      if (qMatchesKey) {
        const itemBelongsToDeity = aliases.some(alias => 
          nameHi.includes(alias) || 
          nameEn.includes(alias) || 
          desc.includes(alias) ||
          (item.category && item.category.toLowerCase().includes(key)) ||
          (item.id && item.id.toLowerCase().includes(key))
        );
        if (itemBelongsToDeity) return true;
      }
    }

    return false;
  }

  // Get active dataset
  function getActiveDataset() {
    if (window.galleryActiveTab === 'bal') {
      return (window.BAL_ROOP_GALLERY && window.BAL_ROOP_GALLERY.length) ? window.BAL_ROOP_GALLERY : [];
    } else if (window.galleryActiveTab === 'divya') {
      return (window.DIVYA_ROOP_GALLERY && window.DIVYA_ROOP_GALLERY.length) ? window.DIVYA_ROOP_GALLERY : [];
    } else if (window.galleryActiveTab === 'india') {
      return (window.INDIA_TEMPLES_GALLERY && window.INDIA_TEMPLES_GALLERY.length) ? window.INDIA_TEMPLES_GALLERY : [];
    } else if (window.galleryActiveTab === 'world') {
      return (window.WORLD_TEMPLES_GALLERY && window.WORLD_TEMPLES_GALLERY.length) ? window.WORLD_TEMPLES_GALLERY : [];
    }
    return (window.BAL_ROOP_GALLERY || []);
  }

  // Render Divine Gallery Grid
  window.renderDivineGallery = function() {
    const container = document.getElementById('gallery-grid-container') || document.getElementById('gallery-grid');
    if (!container) return;

    window.updateGalleryQuotaBadge();

    const dataset = getActiveDataset();
    const searchInput = document.getElementById('gallery-search-input');
    const query = (searchInput ? searchInput.value : (window.currentGallerySearch || '')).trim();

    // Filter by category and search
    let filtered = dataset.filter(item => {
      // Category filter
      let matchesCat = true;
      if (window.galleryActiveCategory && window.galleryActiveCategory !== 'all') {
        const cat = window.galleryActiveCategory.toLowerCase();
        const itemCat = (item.category || '').toLowerCase();
        const itemName = ((item.nameHi || '') + ' ' + (item.nameEn || '')).toLowerCase();
        
        if (DEITY_SYNONYMS[cat]) {
          matchesCat = DEITY_SYNONYMS[cat].some(alias => itemName.includes(alias) || itemCat.includes(alias));
        } else {
          matchesCat = itemCat.includes(cat) || itemName.includes(cat);
        }
      }

      // Search query filter
      const matchesSearch = matchesQuery(item, query);
      return matchesCat && matchesSearch;
    });

    // Update Counter Badge
    const countBadge = document.getElementById('gallery-count-badge');
    if (countBadge) {
      countBadge.textContent = `${filtered.length} स्वरूप उपलब्ध`;
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div style="grid-column:1/-1; text-align:center; padding:3.5rem 1rem; color:#FDE68A;">
          <div style="font-size:3.5rem; margin-bottom:0.8rem; filter:drop-shadow(0 0 10px rgba(248,200,59,0.5));">🌸</div>
          <div style="font-size:1.15rem; font-weight:900; color:#FFFDF8;">कोई स्वरूप नहीं मिला</div>
          <p style="font-size:0.85rem; color:#CBD5E1; margin:6px auto 0; max-width:280px; line-height:1.5;">
            "${query}" के लिए कोई छवि नहीं मिली। कृपया दूसरा नाम (जैसे: Shiva, Krishna, Ram, Hanuman) खोजें।
          </p>
        </div>
      `;
      return;
    }

    // Render Cards in Mobile Grid
    const isTemple = (window.galleryActiveTab === 'india' || window.galleryActiveTab === 'world');
    container.innerHTML = filtered.map((item, idx) => {
      const imgSrc = item.img || 'assets/app_logo_circle.png';
      const fallback = item.fallbackImg || 'assets/app_logo.jpg';
      const title = item.nameHi || 'दिव्य स्वरूप';
      const sub = item.nameEn || (item.location || 'पावन धाम');
      const badgeText = isTemple ? (item.location ? `📍 ${item.location}` : '🏛️ तीर्थ') : (window.galleryActiveTab === 'bal' ? '👶 बाल स्वरूप' : '🕉️ दिव्य स्वरूप');

      return `
        <div class="gallery-card-royal" onclick="openGalleryLightboxItem('${item.id}', '${window.galleryActiveTab}')" style="cursor:pointer;">
          <div class="gallery-img-container" style="position:relative; width:100%; aspect-ratio:1/1; overflow:hidden; background:#120526; border-radius:18px 18px 0 0;">
            <img 
              src="${imgSrc}" 
              alt="${title}" 
              loading="lazy"
              style="width:100%; height:100%; object-fit:cover; transition:transform 0.3s ease;"
              onerror="this.src='${fallback}'" 
            />
            <div style="position:absolute; top:8px; left:8px; background:rgba(18,4,34,0.85); border:1px solid rgba(248,200,59,0.45); color:#FDE68A; font-size:0.68rem; font-weight:800; padding:2px 8px; border-radius:10px; backdrop-filter:blur(6px); max-width:85%; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">
              ${badgeText}
            </div>
          </div>
          
          <div class="gallery-info-box" style="padding:10px 10px 12px; display:flex; flex-direction:column; justify-content:space-between; flex:1; background:linear-gradient(180deg, rgba(30,10,54,0.95) 0%, rgba(15,4,28,0.98) 100%); border-radius:0 0 18px 18px;">
            <div>
              <div style="font-size:0.92rem; font-weight:900; color:#FFFDF8; line-height:1.25; margin-bottom:2px; overflow:hidden; text-overflow:ellipsis; display:-webkit-box; -webkit-line-clamp:1; -webkit-box-orient:vertical;">
                ${title}
              </div>
              <div style="font-size:0.72rem; color:#CBD5E1; margin-bottom:8px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">
                ${sub}
              </div>
            </div>

            <div style="display:flex; align-items:center; justify-content:space-between; gap:6px; margin-top:4px;">
              <button onclick="event.stopPropagation(); downloadDivineImage('${imgSrc}', '${title}')" style="flex:1; background:linear-gradient(135deg, #F8C83B, #D97706); color:#1A0B2E; border:none; padding:6px 0; border-radius:12px; font-weight:900; font-size:0.75rem; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:4px; box-shadow:0 2px 8px rgba(248,200,59,0.35);">
                <span>📥</span> डाउनलोड
              </button>

              <button onclick="event.stopPropagation(); triggerFlowerShower(); if(typeof showToast==='function') showToast('🌸 ${title} को पुष्प अर्पित!');" style="width:30px; height:30px; border-radius:10px; background:rgba(255,255,255,0.08); border:1px solid rgba(248,200,59,0.3); font-size:0.9rem; cursor:pointer; display:flex; align-items:center; justify-content:center;">
                🌸
              </button>
            </div>
          </div>
        </div>
      `;
    }).join('');
  };

  // Switch Gallery Tab (Bal / Divya / India / World)
  window.switchGalleryTab = function(tab) {
    window.galleryActiveTab = tab;
    document.querySelectorAll('.gal-tab-pill').forEach(b => {
      b.classList.toggle('active', b.getAttribute('data-tab') === tab);
    });
    window.renderDivineGallery();
  };

  // Filter Category
  window.filterGalleryCategory = function(cat, btn) {
    window.galleryActiveCategory = cat;
    document.querySelectorAll('.gal-cat-chip').forEach(b => b.classList.remove('active'));
    if (btn) {
      btn.classList.add('active');
    } else {
      const targetBtn = document.querySelector(`.gal-cat-chip[data-cat="${cat}"]`);
      if (targetBtn) targetBtn.classList.add('active');
    }
    window.renderDivineGallery();
  };

  // Open Lightbox
  window.openGalleryLightboxItem = function(itemId, tab) {
    const dataset = getActiveDataset();
    const item = dataset.find(x => x.id === itemId);
    if (!item) return;

    window.currentLightboxItem = item;
    const modal = document.getElementById('gallery-lightbox-modal');
    if (!modal) return;

    const imgEl = document.getElementById('lightbox-img');
    if (imgEl) {
      imgEl.src = item.img || 'assets/app_logo_circle.png';
      imgEl.onerror = function() { this.src = item.fallbackImg || 'assets/app_logo.jpg'; };
    }

    const titleEl = document.getElementById('lightbox-title');
    if (titleEl) titleEl.textContent = item.nameHi || 'दिव्य स्वरूप';

    const subEl = document.getElementById('lightbox-sub');
    if (subEl) subEl.textContent = item.nameEn || item.location || '';

    const mantraEl = document.getElementById('lightbox-mantra');
    if (mantraEl) {
      if (item.mantra) {
        mantraEl.textContent = item.mantra;
        mantraEl.style.display = 'block';
      } else {
        mantraEl.style.display = 'none';
      }
    }

    const descEl = document.getElementById('lightbox-desc');
    if (descEl) descEl.textContent = item.desc || item.famous || 'पावन अलौकिक दिव्य दर्शन।';

    modal.style.display = 'flex';
    modal.style.opacity = '1';

    if (navigator.vibrate) navigator.vibrate(25);
  };

  window.closeGalleryLightbox = function() {
    const modal = document.getElementById('gallery-lightbox-modal');
    if (modal) modal.style.display = 'none';
  };

  // Clear search field
  window.clearGallerySearch = function() {
    const inp = document.getElementById('gallery-search-input');
    if (inp) {
      inp.value = '';
      window.currentGallerySearch = '';
    }
    window.renderDivineGallery();
  };

  // Hook into showPage navigation
  const origShowPage = window.showPage;
  window.showPage = function(pageId) {
    if (typeof origShowPage === 'function') origShowPage(pageId);
    if (pageId === 'page-gallery') {
      setTimeout(window.renderDivineGallery, 50);
    }
  };

  // Initial update
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      window.updateGalleryQuotaBadge();
    });
  } else {
    window.updateGalleryQuotaBadge();
  }
})();
