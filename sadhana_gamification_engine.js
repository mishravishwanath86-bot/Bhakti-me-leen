
// ══════════════════════════════════════════════════════════════════════════════
// 🍞 UNIVERSAL TOAST NOTIFICATION ENGINE
// ══════════════════════════════════════════════════════════════════════════════

window.showToast = function(msg, duration = 3200) {
  let container = document.getElementById('universal-toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'universal-toast-container';
    container.style.cssText = 'position:fixed; top:24px; left:50%; transform:translateX(-50%); z-index:999999; display:flex; flex-direction:column; align-items:center; gap:8px; pointer-events:none; width:90%; max-width:380px;';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.style.cssText = 'background:radial-gradient(circle at 50% 30%, #3B1259 0%, #17042B 100%); border:1.8px solid #F8C83B; border-radius:20px; padding:11px 18px; color:#FFFDF8; font-size:0.86rem; font-weight:900; box-shadow:0 12px 35px rgba(0,0,0,0.9), 0 0 15px rgba(248,200,59,0.3) inset; text-align:center; animation:fadeInDown 0.3s ease; pointer-events:auto; backdrop-filter:blur(15px); -webkit-backdrop-filter:blur(15px); display:flex; align-items:center; justify-content:center; gap:8px; line-height:1.35;';
  toast.innerHTML = `<span>✨</span><span>${msg}</span>`;

  container.appendChild(toast);

  if (navigator.vibrate) navigator.vibrate(30);

  setTimeout(() => {
    toast.style.transition = 'opacity 0.35s ease, transform 0.35s ease';
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(-15px) scale(0.95)';
    setTimeout(() => {
      if (toast.parentNode) toast.parentNode.removeChild(toast);
    }, 360);
  }, duration);
};


// ══════════════════════════════════════════════════════════════════════════════
// 🛡️ SADHANA STREAK PROTECTION & COLLECTIVE SANGHA ENGINE
// Gamified Spiritual Growth, Shield Vault, Vedic Badges & Family Circle
// ══════════════════════════════════════════════════════════════════════════════

window.SadhanaProfile = {
  user_id: 'user_self',
  user_name: 'आप (You)',
  current_streak: 21,
  longest_streak: 21,
  punya_points: 1450,
  active_shields: 1,
  max_shields: 2,
  vedic_rank: 'TAPASWI',
  last_active_date: new Date().toISOString().split('T')[0]
};

window.ActiveSanghaCircle = {
  circle_id: 'circle_om1008',
  invite_code: 'OM1008',
  title: 'महामृत्युंजय 1 लाख महा-अनुष्ठान (मिश्रा परिवार)',
  target_count: 100000,
  current_count: 68400,
  mantra_type: 'महामृत्युंजय मंत्र',
  contributors: [
    { name: 'पिता जी', count: 24000, isSelf: false, avatar: '👑' },
    { name: 'आप (You)', count: 18200, isSelf: true, avatar: '🪷' },
    { name: 'माता जी', count: 15000, isSelf: false, avatar: '🌸' },
    { name: 'राहुल', count: 11200, isSelf: false, avatar: '🌿' }
  ],
  recent_feed: [
    { text: '🌸 माता जी ने 108 महामृत्युंजय जप समर्पित किए', time: '10 मिनट पहले' },
    { text: '👑 पिता जी ने 1,008 जप समर्पित किए', time: 'आज प्रातः' },
    { text: '🪷 आपने 540 जप समर्पित किए', time: 'कल संध्या' }
  ]
};

// 🏛️ VEDIC RANKS CONFIGURATION
window.VEDIC_RANKS = {
  'SADHAK': {
    rank_key: 'SADHAK',
    title: 'साधक (Sadhak)',
    level: 'Level 1',
    days_required: 7,
    icon: '🌿',
    perk_title: 'स्वर्ण ऐप आइकन अनलॉक',
    perk_desc: '7 दिन नित्य साधना पूर्ण होने पर दिव्य गोल्ड थीम!',
    multiplier: 1.0
  },
  'TAPASWI': {
    rank_key: 'TAPASWI',
    title: 'तपस्वी (Tapaswi)',
    level: 'Level 2',
    days_required: 21,
    icon: '🔱',
    perk_title: 'विशेष मंदिर घंटा नाद अनलॉक',
    perk_desc: '21 दिन की अटूट साधना पर दिव्य घंटा व शंख ध्वनि!',
    multiplier: 1.2
  },
  'SIDDHA_SADHAK': {
    rank_key: 'SIDDHA_SADHAK',
    title: 'सिद्ध साधक (Siddha Sadhak)',
    level: 'Level 3',
    days_required: 51,
    icon: '🪔',
    perk_title: '1.5x पुण्य अंक मल्टीप्लायर',
    perk_desc: 'हर साधना व परिक्रमा पर 50% अधिक पुण्य अंक!',
    multiplier: 1.5
  },
  'RISHI_KALP': {
    rank_key: 'RISHI_KALP',
    title: 'ऋषि कल्प (Rishi Kalp)',
    level: 'Level 4',
    days_required: 108,
    icon: '👑',
    perk_title: 'डिजिटल प्रमाणपत्र व शंखनाद',
    perk_desc: '108 दिन की सिद्धि पर व्यक्तिगत वैदिक साधना प्रमाणपत्र!',
    multiplier: 2.0
  }
};

// ══════════════════════════════════════════════════════════════════════════════
// 1. INITIALIZATION & LOCALSTORAGE SYNC
// ══════════════════════════════════════════════════════════════════════════════

window.initSadhanaGamificationEngine = function() {
  // Load Profile from LocalStorage
  const savedProfile = localStorage.getItem('user_sadhana_profile');
  if (savedProfile) {
    try {
      window.SadhanaProfile = Object.assign(window.SadhanaProfile, JSON.parse(savedProfile));
    } catch(e) { console.error(e); }
  }

  // Load Sangha Circle from LocalStorage
  const savedCircle = localStorage.getItem('active_sangha_circle');
  if (savedCircle) {
    try {
      window.ActiveSanghaCircle = Object.assign(window.ActiveSanghaCircle, JSON.parse(savedCircle));
    } catch(e) { console.error(e); }
  }

  // Check Vedic Rank according to current streak
  window.recalculateVedicRank();

  // Check Auto-Rescue Shield Condition
  window.checkAndExecuteStreakShieldRescue();

  // Render UI
  window.renderSadhanaShieldVaultUI();
  window.renderSanghaCircleUI();
  // Track Daily Visits
  window.trackDailyAppVisits();
  window.renderHomeCompactTriggerUI();
};

window.saveSadhanaProfileState = function() {
  localStorage.setItem('user_sadhana_profile', JSON.stringify(window.SadhanaProfile));
};

window.saveSanghaCircleState = function() {
  localStorage.setItem('active_sangha_circle', JSON.stringify(window.ActiveSanghaCircle));
};

window.recalculateVedicRank = function() {
  const streak = window.SadhanaProfile.current_streak;
  if (streak >= 108) {
    window.SadhanaProfile.vedic_rank = 'RISHI_KALP';
  } else if (streak >= 51) {
    window.SadhanaProfile.vedic_rank = 'SIDDHA_SADHAK';
  } else if (streak >= 21) {
    window.SadhanaProfile.vedic_rank = 'TAPASWI';
  } else if (streak >= 7) {
    window.SadhanaProfile.vedic_rank = 'SADHAK';
  } else {
    window.SadhanaProfile.vedic_rank = 'SADHAK';
  }
  window.saveSadhanaProfileState();
};

// ══════════════════════════════════════════════════════════════════════════════
// 2. STREAK SHIELD VAULT & VEDIC REWARDS
// ══════════════════════════════════════════════════════════════════════════════

window.renderSadhanaShieldVaultUI = function() {
  const pointsEl = document.getElementById('sadhana-punya-points-text');
  const shieldBadge = document.getElementById('sadhana-active-shield-badge');
  const rankEl = document.getElementById('sadhana-vedic-rank-text');
  const streakHeader = document.getElementById('sadhana-streak-count');

  if (pointsEl) {
    pointsEl.textContent = `${window.SadhanaProfile.punya_points.toLocaleString('en-IN')} अंक`;
  }
  if (shieldBadge) {
    const s = window.SadhanaProfile.active_shields;
    shieldBadge.innerHTML = `🛡️ ${s} सक्रिय कवच ${s >= window.SadhanaProfile.max_shields ? '(पूर्ण)' : ''}`;
    shieldBadge.style.background = s > 0 ? 'rgba(245,158,11,0.2)' : 'rgba(239,68,68,0.2)';
    shieldBadge.style.color = s > 0 ? '#FDE68A' : '#FCA5A5';
    shieldBadge.style.border = s > 0 ? '1px solid #F59E0B' : '1px solid #EF4444';
  }
  if (rankEl) {
    const rankInfo = window.VEDIC_RANKS[window.SadhanaProfile.vedic_rank] || window.VEDIC_RANKS['TAPASWI'];
    rankEl.innerHTML = `${rankInfo.icon} '${rankInfo.title}' (${rankInfo.level})`;
  }
  if (streakHeader) {
    streakHeader.textContent = `🔥 ${window.SadhanaProfile.current_streak} दिन स्ट्रीक`;
  }
};

window.buyStreakShield = function() {
  const cost = 500;
  if (window.SadhanaProfile.active_shields >= window.SadhanaProfile.max_shields) {
    if (typeof showToast === 'function') {
      showToast('🛡️ रक्षा कवच वॉल्ट पहले से पूर्ण है! (अधिकतम 2 कवच सुरक्षित हैं)');
    }
    return;
  }

  if (window.SadhanaProfile.punya_points < cost) {
    if (typeof showToast === 'function') {
      showToast(`🌟 पर्याप्त पुण्य अंक नहीं हैं! (नया कवच जोड़ने हेतु ${cost} अंक चाहिए)`);
    }
    return;
  }

  // Deduct points & add shield
  window.SadhanaProfile.punya_points -= cost;
  window.SadhanaProfile.active_shields += 1;
  window.saveSadhanaProfileState();
  window.renderSadhanaShieldVaultUI();

  if (navigator.vibrate) navigator.vibrate([50, 40, 90]);
  if (typeof playSoundEffect === 'function') playSoundEffect('victory');
  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();

  if (typeof showToast === 'function') {
    showToast('🛡️ दिव्य रक्षा कवच सक्रिय! आपकी स्ट्रीक अब पूरी तरह सुरक्षित है ✨');
  }
};

window.awardPunyaPoints = function(pts, reason) {
  const rankInfo = window.VEDIC_RANKS[window.SadhanaProfile.vedic_rank] || window.VEDIC_RANKS['TAPASWI'];
  const multiplier = rankInfo.multiplier || 1.0;
  const finalPts = Math.round(pts * multiplier);

  window.SadhanaProfile.punya_points += finalPts;
  window.saveSadhanaProfileState();
  window.renderSadhanaShieldVaultUI();

  if (typeof showToast === 'function') {
    showToast(`🌟 +${finalPts} पुण्य अंक अर्जित! (${reason})`);
  }
};

window.checkAndExecuteStreakShieldRescue = function() {
  const today = new Date().toISOString().split('T')[0];
  const lastDate = window.SadhanaProfile.last_active_date;
  if (!lastDate) {
    window.SadhanaProfile.last_active_date = today;
    window.saveSadhanaProfileState();
    return;
  }

  const d1 = new Date(lastDate);
  const d2 = new Date(today);
  const diffTime = Math.abs(d2 - d1);
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

  if (diffDays >= 2) {
    // User missed a day
    if (window.SadhanaProfile.active_shields > 0) {
      window.SadhanaProfile.active_shields -= 1;
      window.SadhanaProfile.last_active_date = today;
      window.saveSadhanaProfileState();

      setTimeout(() => {
        const modal = document.getElementById('streak-rescue-celebration-modal');
        const desc = document.getElementById('streak-rescue-desc');
        if (desc) {
          desc.innerHTML = `आपका नियम छूटा था, परंतु <strong>1 रक्षा कवच</strong> ने स्वतः सक्रिय होकर आपकी <strong>${window.SadhanaProfile.current_streak}-दिन की पावन स्ट्रीक</strong> को टूटने से बचा लिया! 🕉️`;
        }
        if (modal) modal.style.display = 'flex';
        if (typeof playSoundEffect === 'function') playSoundEffect('victory');
      }, 1200);
    } else {
      // No shield -> reset streak
      window.SadhanaProfile.current_streak = 1;
      window.SadhanaProfile.last_active_date = today;
      window.saveSadhanaProfileState();
    }
  } else {
    window.SadhanaProfile.last_active_date = today;
    window.saveSadhanaProfileState();
  }
};

window.closeStreakRescueModal = function() {
  const modal = document.getElementById('streak-rescue-celebration-modal');
  if (modal) modal.style.display = 'none';
};

// ══════════════════════════════════════════════════════════════════════════════
// 3. VEDIC RANKS & CERTIFICATE MODAL
// ══════════════════════════════════════════════════════════════════════════════

window.openVedicRanksModal = function() {
  const modal = document.getElementById('vedic-ranks-modal');
  if (modal) modal.style.display = 'flex';
};

window.closeVedicRanksModal = function() {
  const modal = document.getElementById('vedic-ranks-modal');
  if (modal) modal.style.display = 'none';
};

// ══════════════════════════════════════════════════════════════════════════════
// 4. COLLECTIVE SANGHA MANDAL (FAMILY & SANGHA CIRCLE)
// ══════════════════════════════════════════════════════════════════════════════

window.renderSanghaCircleUI = function() {
  const C = window.ActiveSanghaCircle;
  const titleEl = document.getElementById('sangha-circle-title');
  const progressTextEl = document.getElementById('sangha-progress-text');
  const progressPctEl = document.getElementById('sangha-progress-pct');
  const progressBarFill = document.getElementById('sangha-progress-bar-fill');
  const contributorsList = document.getElementById('sangha-contributors-list');
  const feedList = document.getElementById('sangha-feed-list');

  if (titleEl) titleEl.textContent = `🕉️ ${C.title}`;

  const pct = Math.min(100, ((C.current_count / C.target_count) * 100)).toFixed(1);
  if (progressTextEl) {
    progressTextEl.textContent = `${C.current_count.toLocaleString('en-IN')} / ${C.target_count.toLocaleString('en-IN')} जप`;
  }
  if (progressPctEl) {
    progressPctEl.textContent = `(${pct}%)`;
  }
  if (progressBarFill) {
    progressBarFill.style.width = `${pct}%`;
  }

  if (contributorsList) {
    contributorsList.innerHTML = '';
    // Sort contributors descending
    const sorted = [...C.contributors].sort((a, b) => b.count - a.count);
    sorted.forEach((member, idx) => {
      const isTop = idx === 0;
      const row = document.createElement('div');
      row.style.cssText = `display:flex; align-items:center; justify-content:space-between; padding:6px 10px; background:${member.isSelf ? 'rgba(248,200,59,0.15)' : 'rgba(255,255,255,0.05)'}; border:1px solid ${member.isSelf ? 'rgba(248,200,59,0.4)' : 'rgba(255,255,255,0.1)'}; border-radius:12px; font-size:0.78rem;`;
      row.innerHTML = `
        <div style="display:flex; align-items:center; gap:6px;">
          <span>${member.avatar || '🪷'}</span>
          <span style="font-weight:${member.isSelf ? '900' : '700'}; color:${member.isSelf ? '#FDE68A' : '#FFFDF8'};">${member.name}</span>
          ${isTop ? '<span style="font-size:0.68rem; background:#F59E0B; color:#1A0B2E; padding:1px 6px; border-radius:8px; font-weight:900;">शीर्ष साधक</span>' : ''}
        </div>
        <span style="font-weight:900; color:#F8C83B;">${member.count.toLocaleString('en-IN')} जप</span>
      `;
      contributorsList.appendChild(row);
    });
  }

  if (feedList && C.recent_feed) {
    feedList.innerHTML = '';
    C.recent_feed.slice(0, 2).forEach(f => {
      const item = document.createElement('div');
      item.style.cssText = 'font-size:0.72rem; color:#CBD5E1; display:flex; align-items:center; justify-content:space-between; padding:3px 0;';
      item.innerHTML = `<span>${f.text}</span><span style="color:#FDE68A; font-size:0.65rem;">${f.time}</span>`;
      feedList.appendChild(item);
    });
  }
};

window.openDedicateJapModal = function() {
  const modal = document.getElementById('dedicate-jap-modal');
  if (modal) modal.style.display = 'flex';
};

window.closeDedicateJapModal = function() {
  const modal = document.getElementById('dedicate-jap-modal');
  if (modal) modal.style.display = 'none';
};

window.submitDedicatedJap = function(count) {
  count = parseInt(count);
  if (!count || isNaN(count) || count <= 0) {
    const input = document.getElementById('custom-jap-dedicate-input');
    if (input) count = parseInt(input.value);
  }

  if (!count || isNaN(count) || count <= 0) {
    if (typeof showToast === 'function') showToast('कृपया वैध जप संख्या दर्ज करें!');
    return;
  }

  // Add to active circle current_count
  window.ActiveSanghaCircle.current_count += count;

  // Add to self contributor count
  const selfMember = window.ActiveSanghaCircle.contributors.find(m => m.isSelf);
  if (selfMember) {
    selfMember.count += count;
  } else {
    window.ActiveSanghaCircle.contributors.push({
      name: 'आप (You)',
      count: count,
      isSelf: true,
      avatar: '🪷'
    });
  }

  // Add to recent feed
  window.ActiveSanghaCircle.recent_feed.unshift({
    text: `🪷 आपने ${count.toLocaleString('en-IN')} जप समर्पित किए`,
    time: 'अभी-अभी'
  });

  // Award Punya Points (1 point per 10 jap)
  const pts = Math.max(10, Math.round(count / 10));
  window.SadhanaProfile.punya_points += pts;

  window.saveSanghaCircleState();
  window.saveSadhanaProfileState();
  window.renderSanghaCircleUI();
  // Track Daily Visits
  window.trackDailyAppVisits();
  window.renderHomeCompactTriggerUI();
  window.renderSadhanaShieldVaultUI();

  window.closeDedicateJapModal();

  if (navigator.vibrate) navigator.vibrate([60, 40, 100]);
  if (typeof playSoundEffect === 'function') playSoundEffect('victory');
  if (typeof triggerFlowerShower === 'function') triggerFlowerShower();

  if (typeof showToast === 'function') {
    showToast(`📿 ${count.toLocaleString('en-IN')} जप सामूहिक महा-अनुष्ठान में समर्पित! (+${pts} पुण्य अंक) ✨`);
  }
};

window.openAddMemberModal = function() {
  const modal = document.getElementById('add-sangha-member-modal');
  if (modal) modal.style.display = 'flex';
};

window.closeAddMemberModal = function() {
  const modal = document.getElementById('add-sangha-member-modal');
  if (modal) modal.style.display = 'none';
};

window.copySanghaInviteCode = function() {
  const code = window.ActiveSanghaCircle.invite_code || 'OM1008';
  if (navigator.clipboard) {
    navigator.clipboard.writeText(code).then(() => {
      if (typeof showToast === 'function') showToast(`📋 आमंत्रण कोड कॉपी हुआ: ${code}`);
    });
  } else {
    if (typeof showToast === 'function') showToast(`आमंत्रण कोड: ${code}`);
  }
};

window.shareSanghaProgressWhatsApp = function() {
  const C = window.ActiveSanghaCircle;
  const pct = Math.min(100, ((C.current_count / C.target_count) * 100)).toFixed(1);
  const msg = `🕉️ *सामूहिक साधना मंडल — महा-अनुष्ठान प्रगति* 🕉️\n\n` +
    `🚩 *संकल्प:* ${C.title}\n` +
    `📊 *कुल प्रगति:* ${C.current_count.toLocaleString('en-IN')} / ${C.target_count.toLocaleString('en-IN')} जप (${pct}% पूर्ण)\n\n` +
    `👑 *शीर्ष साधक योगदान:*\n` +
    C.contributors.map(c => `• ${c.name}: ${c.count.toLocaleString('en-IN')} जप`).join('\n') + `\n\n` +
    `✨ आप भी हमारे परिवार अनुष्ठान में जप समर्पित करें:\n` +
    `आमंत्रण कोड: *${C.invite_code}*\n` +
    `'भक्ति में लीन' ऐप डाउनलोड करें 📿`;

  const shareUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`;
  window.open(shareUrl, '_blank');
};

window.nudgeSanghaMember = function(name) {
  if (navigator.vibrate) navigator.vibrate(50);
  if (typeof showToast === 'function') {
    showToast(`🔔 ${name} जी को साधना स्मरण (Nudge) भेजा गया! 🕉️`);
  }
};

window.openCreateJoinSanghaModal = function() {
  const modal = document.getElementById('create-join-sangha-modal');
  if (modal) modal.style.display = 'flex';
};

window.closeCreateJoinSanghaModal = function() {
  const modal = document.getElementById('create-join-sangha-modal');
  if (modal) modal.style.display = 'none';
};

window.createNewSanghaCircle = function() {
  const titleInput = document.getElementById('new-sangha-title-input');
  const targetInput = document.getElementById('new-sangha-target-input');
  const mantraInput = document.getElementById('new-sangha-mantra-select');

  const title = titleInput ? titleInput.value.trim() : '';
  const target = targetInput ? parseInt(targetInput.value) : 10000;
  const mantra = mantraInput ? mantraInput.value : 'महामृत्युंजय मंत्र';

  if (!title) {
    if (typeof showToast === 'function') showToast('कृपया मंडल का पावन नाम दर्ज करें!');
    return;
  }

  const randomCode = 'OM' + Math.floor(1000 + Math.random() * 9000);
  window.ActiveSanghaCircle = {
    circle_id: 'circle_' + Date.now(),
    invite_code: randomCode,
    title: title,
    target_count: target || 10000,
    current_count: 0,
    mantra_type: mantra,
    contributors: [
      { name: 'आप (You)', count: 0, isSelf: true, avatar: '🪷' }
    ],
    recent_feed: [
      { text: `✨ नया मंडल '${title}' आरंभ हुआ`, time: 'अभी-अभी' }
    ]
  };

  window.saveSanghaCircleState();
  window.renderSanghaCircleUI();
  // Track Daily Visits
  window.trackDailyAppVisits();
  window.renderHomeCompactTriggerUI();
  window.closeCreateJoinSanghaModal();

  if (typeof showToast === 'function') {
    showToast(`🚩 नया साधना मंडल '${title}' सफलतापूर्वक बना! कोड: ${randomCode}`);
  }
};

window.joinSanghaCircle = function() {
  const codeInput = document.getElementById('join-sangha-code-input');
  const code = codeInput ? codeInput.value.trim().toUpperCase() : '';

  if (!code) {
    if (typeof showToast === 'function') showToast('कृपया आमंत्रण कोड दर्ज करें!');
    return;
  }

  window.ActiveSanghaCircle = {
    circle_id: 'circle_joined_' + code,
    invite_code: code,
    title: `सामूहिक अनुष्ठान (कोड: ${code})`,
    target_count: 50000,
    current_count: 12500,
    mantra_type: 'श्री राम जय राम जय जय राम',
    contributors: [
      { name: 'मंडल संचालक', count: 8500, isSelf: false, avatar: '👑' },
      { name: 'आप (You)', count: 0, isSelf: true, avatar: '🪷' },
      { name: 'साधक 1', count: 4000, isSelf: false, avatar: '🌸' }
    ],
    recent_feed: [
      { text: '🪷 आप साधना मंडल में शामिल हुए!', time: 'अभी-अभी' }
    ]
  };

  window.saveSanghaCircleState();
  window.renderSanghaCircleUI();
  // Track Daily Visits
  window.trackDailyAppVisits();
  window.renderHomeCompactTriggerUI();
  window.closeCreateJoinSanghaModal();

  if (typeof showToast === 'function') {
    showToast(`🤝 साधना मंडल (${code}) में सफलतापूर्वक जुड़े!`);
  }
};

// Auto-run on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    window.initSadhanaGamificationEngine();
  }, 400);
});


// ══════════════════════════════════════════════════════════════════════════════
// 👁️ DAILY APP VISIT TRACKING & TWO-STAGE ARCHITECTURE CONTROLLERS
// ══════════════════════════════════════════════════════════════════════════════

window.currentDailyVisits = 3;

window.trackDailyAppVisits = function() {
  const today = new Date().toISOString().split('T')[0];
  const lastDate = localStorage.getItem('sanatan_last_visit_date');
  const lastTs = parseInt(localStorage.getItem('sanatan_last_visit_timestamp') || '0');
  let visitCount = parseInt(localStorage.getItem('sanatan_daily_visit_count') || '3');

  const now = Date.now();

  if (lastDate !== today) {
    visitCount = 1;
    localStorage.setItem('sanatan_last_visit_date', today);
    localStorage.setItem('sanatan_daily_visit_count', '1');
    localStorage.setItem('sanatan_last_visit_timestamp', now.toString());
  } else {
    // Increment visit count if session gap > 15 minutes
    if (now - lastTs > 15 * 60 * 1000) {
      visitCount += 1;
      localStorage.setItem('sanatan_daily_visit_count', visitCount.toString());
      localStorage.setItem('sanatan_last_visit_timestamp', now.toString());
    }
  }

  if (visitCount < 1) visitCount = 1;
  window.currentDailyVisits = visitCount;
  window.updateVisitCountUI(visitCount);
};

window.updateVisitCountUI = function(count) {
  count = count || window.currentDailyVisits || 3;
  
  // Update Home Compact Card
  const homeVisitEl = document.getElementById('sadhana-home-visit-count');
  if (homeVisitEl) homeVisitEl.textContent = `${count} बार`;

  // Update Modal Banner
  const modalVisitText = document.getElementById('modal-visit-summary-text');
  if (modalVisitText) {
    modalVisitText.innerHTML = `आज आपने <strong style="color:#FDE68A;">${count} बार</strong> प्रभु दर्शन व साधना हेतु प्रवेश किया है`;
  }
};

window.renderHomeCompactTriggerUI = function() {
  const streakBadge = document.getElementById('sadhana-home-streak-badge');
  const shieldSummary = document.getElementById('sadhana-home-shield-summary');
  const punyaSummary = document.getElementById('sadhana-home-punya-summary');
  const modalStreakBadge = document.getElementById('modal-sadhana-streak-badge');

  const streak = window.SadhanaProfile.current_streak;
  const shields = window.SadhanaProfile.active_shields;
  const points = window.SadhanaProfile.punya_points;

  if (streakBadge) streakBadge.textContent = `🔥 ${streak} दिन स्ट्रीक`;
  if (modalStreakBadge) modalStreakBadge.textContent = `🔥 ${streak} दिन स्ट्रीक`;
  if (shieldSummary) shieldSummary.textContent = `${shields} सक्रिय`;
  if (punyaSummary) punyaSummary.textContent = `${points.toLocaleString('en-IN')}`;
};

window.openFullSadhanaControlModal = function() {
  const modal = document.getElementById('full-sadhana-control-modal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
  window.renderSadhanaShieldVaultUI();
  window.renderSanghaCircleUI();
  // Track Daily Visits
  window.trackDailyAppVisits();
  window.renderHomeCompactTriggerUI();
  window.updateVisitCountUI();

  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof playSoundEffect === 'function') playSoundEffect('correct');
};

window.closeFullSadhanaControlModal = function() {
  const modal = document.getElementById('full-sadhana-control-modal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
  window.renderHomeCompactTriggerUI();
};


// ══════════════════════════════════════════════════════════════════════════════
// 📅 DYNAMIC REAL-TIME WEEKLY SADHANA TRACKER (सोमवार से रविवार - 7 दिन नियम)
// ══════════════════════════════════════════════════════════════════════════════

window.DAY_NAMES_HI = ['सोम', 'मंगल', 'बुध', 'गुरु', 'शुक्र', 'शनि', 'रवि'];
window.DAY_NAMES_FULL_HI = ['सोमवार', 'मंगलवार', 'बुधवार', 'गुरुवार', 'शुक्रवार', 'शनिवार', 'रविवार'];

// 0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun
window.getTodayMondayIndex = function() {
  const jsDay = new Date().getDay(); // 0 is Sun, 1 is Mon...
  return (jsDay + 6) % 7;
};

// Current ISO Week identifier (e.g. "sanatan_weekly_sadhana_2026_w36")
window.getCurrentWeekKey = function() {
  const d = new Date();
  const year = d.getFullYear();
  const oneJan = new Date(year, 0, 1);
  const numberOfDays = Math.floor((d - oneJan) / (24 * 60 * 60 * 1000));
  const weekNum = Math.ceil((numberOfDays + oneJan.getDay() + 1) / 7);
  return `sanatan_weekly_sadhana_${year}_w${weekNum}`;
};

window.loadWeeklySadhanaDays = function() {
  const key = window.getCurrentWeekKey();
  const raw = localStorage.getItem(key);
  const todayIdx = window.getTodayMondayIndex();

  let days = [false, false, false, false, false, false, false];
  if (raw) {
    try {
      days = JSON.parse(raw);
    } catch(e) {}
  } else {
    // Default: Mark days up to today as done for active sadhak
    for (let i = 0; i <= todayIdx; i++) {
      days[i] = true;
    }
    localStorage.setItem(key, JSON.stringify(days));
  }

  // Ensure today is always marked active/done when user enters app
  days[todayIdx] = true;
  localStorage.setItem(key, JSON.stringify(days));

  return days;
};

window.toggleDayDone = function(dayIdx) {
  const key = window.getCurrentWeekKey();
  const days = window.loadWeeklySadhanaDays();

  // Toggle day done state
  days[dayIdx] = !days[dayIdx];
  localStorage.setItem(key, JSON.stringify(days));

  // Render updated UI
  window.renderWeeklySadhanaStrip();

  const dayName = window.DAY_NAMES_FULL_HI[dayIdx];
  const isDone = days[dayIdx];

  if (navigator.vibrate) navigator.vibrate(30);
  if (typeof playSoundEffect === 'function') playSoundEffect(isDone ? 'correct' : 'click');
  
  if (typeof showToast === 'function') {
    showToast(isDone ? `✓ ${dayName} की साधना पूर्ण चिह्नित की गई! 🕉️` : `○ ${dayName} की साधना रीसेट हुई`);
  }
};

window.renderWeeklySadhanaStrip = function() {
  const days = window.loadWeeklySadhanaDays();
  const todayIdx = window.getTodayMondayIndex();
  const stripEl = document.getElementById('modal-weekly-day-strip');
  const badgeEl = document.getElementById('modal-weekly-progress-badge');

  let completedCount = 0;
  days.forEach(d => { if (d) completedCount++; });

  if (badgeEl) {
    badgeEl.textContent = `आज ${completedCount}/7 पूर्ण ✓`;
  }

  if (stripEl) {
    stripEl.innerHTML = window.DAY_NAMES_HI.map((name, idx) => {
      const isDone = days[idx];
      const isToday = idx === todayIdx;
      let cls = 'day-dot';
      let icon = '○';

      if (isDone) {
        cls += ' done';
        icon = '✓';
      }
      if (isToday) {
        cls += ' active-today';
        if (!isDone) icon = '●';
      }

      return `
        <div class="${cls}" onclick="toggleDayDone(${idx})" title="${window.DAY_NAMES_FULL_HI[idx]} नियम (क्लिक कर बदलें)">
          <span>${name}</span>
          <span class="dot-check">${icon}</span>
        </div>
      `;
    }).join('');
  }
};



window.submitAddSanghaMember = function() {
  const input = document.getElementById('add-sangha-member-name-input');
  const name = input ? input.value.trim() : '';

  if (!name) {
    if (typeof showToast === 'function') showToast('कृपया सदस्य का नाम दर्ज करें!');
    return;
  }

  // Add new member to contributors list
  const avatars = ['🌸', '🌿', '🪷', '🌻', '🌺', '🕉️', '🚩'];
  const randomAvatar = avatars[Math.floor(Math.random() * avatars.length)];

  window.ActiveSanghaCircle.contributors.push({
    name: name,
    count: 0,
    isSelf: false,
    avatar: randomAvatar
  });

  window.ActiveSanghaCircle.recent_feed.unshift({
    text: `${randomAvatar} ${name} जी महा-अनुष्ठान में शामिल हुए`,
    time: 'अभी-अभी'
  });

  window.saveSanghaCircleState();
  window.renderSanghaCircleUI();

  if (input) input.value = '';
  window.closeAddMemberModal();

  if (navigator.vibrate) navigator.vibrate([40, 30, 70]);
  if (typeof playSoundEffect === 'function') playSoundEffect('click');

  if (typeof showToast === 'function') {
    showToast(`👥 ${name} जी सामूहिक महा-अनुष्ठान में जुड़ गए! 🚩`);
  }
};
