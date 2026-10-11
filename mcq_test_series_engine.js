/**
 * ═════════════════════════════════════════════════════════════════════════════
 * 🎯 SANATAN TEST SERIES ENGINE (4-STEP MCQ EXAMINATION SYSTEM)
 * Designed exactly as per User Reference Flow (Images 1 ➔ 2 ➔ 3 ➔ 4):
 *   Step 1: Topics / Category Listing (Image 1 - Mock Tests)
 *   Step 2: Tests under Selected Topic (Image 2 - Revision & Test Sets)
 *   Step 3: Test Instructions Screen (Image 3 - Duration, Marks & Language)
 *   Step 4: Active MCQ Examination Interface (Image 4 - Live Timer, Marks, Options, Palette)
 *   Step 5: Scorecard & Performance Review (Summary & Explanations)
 * ═════════════════════════════════════════════════════════════════════════════
 */

(function() {
  'use strict';

  // 1. Topic Definitions
  window.SANATAN_TEST_TOPICS = [
    {
      id: 'ramayan',
      title: 'रामायण महाकाव्य टेस्ट श्रृंखला',
      shortTitle: 'रामायण महाकाव्य श्रृंखला',
      icon: '🏹',
      countText: '139',
      freeTestsText: '14 Free Tests',
      category: 'ramayan',
      desc: 'बालकाण्ड, अयोध्याकाण्ड, किष्किन्धा, सुन्दरकाण्ड एवं लंकाकाण्ड',
      setTitles: [
        'बालकाण्ड एवं श्री राम जन्म',
        'ताड़का वध एवं विश्वामित्र यज्ञ रक्षा',
        'धनुष यज्ञ एवं श्री राम-जानकी विवाह',
        'अयोध्याकाण्ड: राजतिलक एवं कैकेयी वरदान',
        'वनवास प्रस्थान एवं केवट संवाद',
        'चित्रकूट वास एवं भरत मिलाप',
        'अरण्यकाण्ड: पंचवटी एवं शूर्पणखा प्रसंग',
        'सीता हरण एवं जटायु मोक्ष',
        'किष्किन्धाकाण्ड: सुग्रीव मित्रता व बालि वध',
        'सुन्दरकाण्ड: श्री हनुमान लंका दहन',
        'सेतु निर्माण एवं विभीषण शरणागति',
        'लंकाकाण्ड: कुंभकर्ण व मेघनाद युद्ध',
        'रावण वध एवं विभीषण राज्याभिषेक',
        'अयोध्या वापसी, राज्याभिषेक एवं उत्तरकाण्ड'
      ]
    },
    {
      id: 'mahabharat',
      title: 'महाभारत एवं श्रीमद्भगवद्गीता टेस्ट श्रृंखला',
      shortTitle: 'महाभारत एवं भगवद्गीता',
      icon: '⚔️',
      countText: '386',
      freeTestsText: '38 Free Tests',
      category: 'mahabharat',
      desc: 'आदिपर्व, सभापर्व, वनपर्व, विराटपर्व, उद्योगपर्व एवं भीष्मपर्व (गीता)',
      setTitles: [
        'कुरु वंश उद्भव एवं भीष्म प्रतिज्ञा',
        'पांडव-कौरव जन्म एवं द्रोणाचार्य शिक्षा',
        'लाक्षागृह षड्यंत्र एवं हिडिम्बा विवाह',
        'द्रौपदी स्वयंवर एवं इंद्रप्रस्थ निर्माण',
        'राजसूय यज्ञ एवं शिशुपाल वध',
        'द्यूत क्रीड़ा एवं द्रौपदी चीरहरण',
        'पांडवों का 12 वर्ष का वनवास लीला',
        'विराट नगर अज्ञातवास एवं कीचक वध',
        'गो-हरण युद्ध एवं अर्जुन पराक्रम',
        'श्री कृष्ण शांति दूत प्रसंग',
        'श्रीमद्भगवद्गीता ज्ञान: अध्याय 1 व 2 (सांख्य योग)',
        'श्रीमद्भगवद्गीता ज्ञान: अध्याय 3 व 4 (कर्म व ज्ञान योग)',
        'श्रीमद्भगवद्गीता ज्ञान: अध्याय 9 व 11 (विश्वरूप दर्शन)',
        'कुरुक्षेत्र महायुद्ध: भीष्म पितामह शरशय्या',
        'चक्रव्यूह रचना एवं वीर अभिमन्यु शौर्य',
        'द्रोण वध एवं जयद्रथ वध',
        'कर्ण-अर्जुन महायुद्ध',
        'दुर्योधन वध एवं अश्वत्थामा प्रसंग',
        'शांतिपर्व: भीष्म उपदेश एवं मोक्ष धर्म'
      ]
    },
    {
      id: 'god',
      title: 'प्रमुख देवी-देवता एवं अवतार दर्शन टेस्ट',
      shortTitle: 'प्रमुख देवी-देवता एवं अवतार',
      icon: '🪔',
      countText: '61',
      freeTestsText: '6 Free Tests',
      category: 'god',
      desc: 'शिव, विष्णु, ब्रह्मा, गणेश, कार्तिकेय, हनुमान एवं नवदुर्गा',
      setTitles: [
        'भगवान शिव महिमा एवं ज्योतिर्लिंग दर्शन',
        'भगवान विष्णु दशावतार एवं चतुर्भुज स्वरूप',
        'प्रथम पूज्य श्री गणेश एवं कार्तिकेय',
        'संकटमोचन श्री हनुमान जी दिव्य चरित्र',
        'नवदुर्गा एवं प्रमुख शक्तिपीठ',
        'भगवान सूर्यदेव एवं नवग्रह महिमा'
      ]
    },
    {
      id: 'ved',
      title: 'चारों वेद, उपनिषद एवं दर्शन शास्त्र',
      shortTitle: 'चारों वेद एवं उपनिषद',
      icon: '📜',
      countText: '72',
      freeTestsText: '7 Free Tests',
      category: 'ved',
      desc: 'ऋग्वेद, यजुर्वेद, सामवेद, अथर्ववेद, उपनिषद व षड्दर्शन',
      setTitles: [
        'ऋग्वेद: सूक्त, देवता एवं वैदिक सभ्यता',
        'यजुर्वेद एवं सामवेद: यज्ञ विधि व संगीत',
        'अथर्ववेद: आयुर्वेद एवं व्यावहारिक ज्ञान',
        'ईश, केन, कठ उपनिषद एवं नचिकेता संवाद',
        'मुण्डक, मांडूक्य एवं सत्यमेव जयते',
        'सांख्य, योग एवं वेदान्त दर्शन',
        'वैदिक ऋषि, आश्रम व्यवस्था व संस्कार'
      ]
    },
    {
      id: 'mantra',
      title: 'वैदिक मंत्र, स्तोत्र एवं स्तुति टेस्ट',
      shortTitle: 'वैदिक मंत्र, स्तोत्र एवं स्तुति',
      icon: '🕉️',
      countText: '106',
      freeTestsText: '10 Free Tests',
      category: 'mantra',
      desc: 'गायत्री मंत्र, महामृत्युंजय, शिव तांडव, विष्णु सहस्रनाम आदि',
      setTitles: [
        'महामंत्र गायत्री एवं सूर्य उपासना',
        'महामृत्युंजय मंत्र एवं संजीवनी साधना',
        'शिव तांडव स्तोत्र एवं रुद्राष्टकम',
        'विष्णु सहस्रनाम एवं नारायण कवच',
        'कनकधारा स्तोत्र एवं लक्ष्मी साधना',
        'बजरंग बाण एवं हनुमानाष्टक स्तुति',
        'वैदिक शांति पाठ एवं मंगलाचरण',
        'नवग्रह स्तोत्र एवं ग्रह शांति मंत्र',
        'आदित्य हृदय स्तोत्र एवं रावण पराजय',
        'दुर्गा सप्तशती एवं अर्गला स्तोत्र'
      ]
    },
    {
      id: 'bhakti_sahitya',
      title: 'भक्ति साहित्य, संत परम्परा एवं काव्य',
      shortTitle: 'भक्ति साहित्य एवं संत परम्परा',
      icon: '🌸',
      countText: '24',
      freeTestsText: '2 Free Tests',
      category: 'bhakti_sahitya',
      desc: 'तुलसीदास, सूरदास, कबीरदास, मीराबाई, रसखान व रविदास',
      setTitles: [
        'गोस्वामी तुलसीदास एवं रामचरितमानस',
        'सूरदास, मीराबाई एवं कृष्ण भक्ति काव्य',
        'कबीरदास एवं निर्गुण संत परम्परा'
      ]
    },
    {
      id: 'aarti_chalisa',
      title: 'आरती संग्रह एवं चालीसा पाठ महात्म्य',
      shortTitle: 'आरती संग्रह एवं चालीसा पाठ',
      icon: '🔔',
      countText: '23',
      freeTestsText: '2 Free Tests',
      category: 'aarti_chalisa',
      desc: 'हनुमान चालीसा, शिव चालीसा, आरती कुंजबिहारी की, ॐ जय जगदीश',
      setTitles: [
        'हनुमान चालीसा एवं शिव चालीसा महात्म्य',
        'प्रमुख देवी-देवताओं की आरती एवं विधि'
      ]
    },
    {
      id: 'all',
      title: 'ऑल इंडिया सनातन महा-मॉक टेस्ट (Mega Test)',
      shortTitle: 'ऑल इंडिया सनातन महा-मॉक टेस्ट',
      icon: '🎯',
      countText: '811',
      freeTestsText: '81 Free Tests',
      category: 'all',
      desc: 'समस्त वेदों, पुराणों, रामायण, महाभारत एवं गीता का व्यापक टेस्ट',
      setTitles: [
        'ऑल इंडिया सनातन ग्रैंड मॉक टेस्ट #1',
        'ऑल इंडिया सनातन ग्रैंड मॉक टेस्ट #2',
        'ऑल इंडिया सनातन ग्रैंड मॉक टेस्ट #3',
        'ऑल इंडिया सनातन ग्रैंड मॉक टेस्ट #4',
        'ऑल इंडिया सनातन ग्रैंड मॉक टेस्ट #5'
      ]
    },
    {
      id: 'bookmarks',
      title: 'सहेजे गए प्रश्न (Bookmarks Revision)',
      shortTitle: 'सहेजे गए प्रश्न (Bookmarks Revision)',
      icon: '⭐',
      countText: 'सहेजे',
      freeTestsText: 'रिवीजन टेस्ट',
      category: 'bookmarks',
      desc: 'आपके द्वारा अभ्यास के दौरान सहेजे गए कठिन प्रश्नों का दोहराव',
      setTitles: [
        'सहेजे गए प्रश्नों का रिवीजन टेस्ट'
      ]
    }
  ];

  // 2. Global State for Test Series Engine
  window.tsState = {
    currentStep: 1,           // 1: Topics, 2: Test Sets, 3: Instructions, 4: Active Exam, 5: Result
    selectedTopic: null,      // Topic object
    selectedTestSet: null,    // Test set object
    selectedLanguage: 'hi',   // 'hi' or 'en'
    currentSubTab: 'all',     // Sub-tab in Step 2: 'all', 'part1', 'part2', 'special'
    examQuestions: [],        // 10 questions for current test
    currentQIdx: 0,           // 0 to 9
    userAnswers: {},          // { qIdx: selectedOptionIdx }
    markedForReview: {},      // { qIdx: boolean }
    qTimeSpent: {},           // { qIdx: seconds }
    examTotalTime: 600,       // 10 minutes (600 seconds)
    examTimeLeft: 600,        // live countdown
    examTimerInterval: null,  // setInterval for exam countdown
    qTimerInterval: null,     // setInterval for per-question timer
    isPaletteOpen: false,     // drawer state
    examStartTime: 0,
    examSubmitted: false
  };

  // Helper: In-app smooth Toast
  function showEngineToast(msg) {
    if (typeof window.showToast === 'function') {
      window.showToast(msg);
      return;
    }
    let t = document.getElementById('ts-quick-toast');
    if (!t) {
      t = document.createElement('div');
      t.id = 'ts-quick-toast';
      t.style.cssText = 'position:fixed; bottom:75px; left:50%; transform:translateX(-50%); background:#27272A; color:#FFF; padding:8px 18px; border-radius:20px; font-size:0.82rem; font-weight:700; z-index:100060; border:1px solid #3F3F46; box-shadow:0 8px 24px rgba(0,0,0,0.6); pointer-events:none; transition:opacity 0.2s ease;';
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.style.display = 'block';
    t.style.opacity = '1';
    clearTimeout(window._tsToastTimer);
    window._tsToastTimer = setTimeout(() => {
      t.style.opacity = '0';
      setTimeout(() => { t.style.display = 'none'; }, 200);
    }, 2200);
  }

  // Inject Custom Styles for Test Series UI
  function injectTestSeriesStyles() {
    if (document.getElementById('ts-custom-css')) return;
    const style = document.createElement('style');
    style.id = 'ts-custom-css';
    style.textContent = `
      #quiz-hub-card {
        scrollbar-width: thin;
        scrollbar-color: #3F3F46 #18181B;
      }
      #quiz-hub-card::-webkit-scrollbar {
        width: 4px;
      }
      #quiz-hub-card::-webkit-scrollbar-thumb {
        background: #3F3F46;
        border-radius: 4px;
      }
      .ts-topic-row:active {
        background: rgba(255, 255, 255, 0.06) !important;
      }
      .ts-test-card:active {
        transform: scale(0.99);
      }
      .ts-opt-card:active {
        transform: scale(0.99);
      }
      @media (max-width: 500px) {
        #quiz-hub-modal {
          padding: 0 !important;
        }
        #quiz-hub-card {
          width: 100% !important;
          max-width: 100% !important;
          height: 100vh !important;
          max-height: 100vh !important;
          border-radius: 0 !important;
          border: none !important;
        }
        #ts-step-topics, #ts-step-tests, #ts-step-instructions, #ts-step-exam, #ts-step-result, #ts-step-wall-of-fame {
          height: 100vh !important;
          max-height: 100vh !important;
        }
        .wof-card {
          transition: transform 0.18s ease, box-shadow 0.18s ease;
        }
        .wof-card:active {
          transform: scale(0.98);
        }
        .wof-card-user {
          animation: userCardGlow 2.5s infinite ease-in-out;
        }
        @keyframes userCardGlow {
          0%, 100% { box-shadow: 0 4px 18px rgba(245, 158, 11, 0.28); }
          50% { box-shadow: 0 8px 28px rgba(245, 158, 11, 0.55); border-color: #F59E0B; }
        }
        #wof-cards-container::-webkit-scrollbar {
          width: 4px;
        }
        #wof-cards-container::-webkit-scrollbar-thumb {
          background: #CBD5E1;
          border-radius: 4px;
        }
      }
    `;
    document.head.appendChild(style);
  }

  // 3. Helper: Load all MCQs
  window.ensureMCQsLoaded = async function() {
    if (window.ALL_MCQS_DATA && window.ALL_MCQS_DATA.length > 0) return;
    try {
      const resp = await fetch('all_sanatan_mcqs.json');
      window.ALL_MCQS_DATA = await resp.json();
      console.log(`✓ [TestSeriesEngine] Loaded ${window.ALL_MCQS_DATA.length} MCQs`);
    } catch (e) {
      console.warn('[TestSeriesEngine] Could not load all_sanatan_mcqs.json:', e);
    }
  };

  // 4. Step 1: Render Topics List (Image 1 Style)
  window.renderTopicsListStep = function() {
    injectTestSeriesStyles();
    const listEl = document.getElementById('ts-topics-list');
    if (!listEl) return;

    listEl.innerHTML = window.SANATAN_TEST_TOPICS.map(topic => {
      let countDisplay = topic.countText;
      if (topic.id === 'bookmarks') {
        const bmCount = (window.quizBookmarks && window.quizBookmarks.length) || 0;
        countDisplay = `${bmCount}`;
      }

      return `
        <div onclick="openTopicTestSets('${topic.id}')" class="ts-topic-row" style="display:flex; align-items:center; justify-content:space-between; padding:16px 18px; border-bottom:1px solid #27272A; cursor:pointer; background:#121214; transition:background 0.15s ease;">
          <div style="display:flex; align-items:center; gap:12px; flex:1; min-width:0; padding-right:10px;">
            <span style="font-size:1.15rem; font-weight:800; color:#E4E4E7; flex-shrink:0; min-width:32px;">${countDisplay}</span>
            <span style="font-size:0.92rem; font-weight:700; color:#F4F4F5; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${topic.shortTitle}</span>
          </div>
          <div style="display:flex; align-items:center; gap:8px; flex-shrink:0;">
            <span style="font-size:0.82rem; font-weight:700; color:#10B981;">${topic.freeTestsText}</span>
            <span style="font-size:0.92rem; color:#71717A; font-weight:900;">❯</span>
          </div>
        </div>
      `;
    }).join('');
  };

  // 5. Step 2: Open Test Sets for Selected Topic (Image 2 Style)
  window.openTopicTestSets = async function(topicId) {
    injectTestSeriesStyles();
    await window.ensureMCQsLoaded();
    const topic = window.SANATAN_TEST_TOPICS.find(t => t.id === topicId) || window.SANATAN_TEST_TOPICS[0];
    window.tsState.selectedTopic = topic;
    window.tsState.currentSubTab = 'all';

    // Header Title & Subtitle
    const headerTitle = document.getElementById('ts-sets-header-title');
    if (headerTitle) {
      headerTitle.textContent = topic.title;
    }

    // Reset Subtab Visual State
    filterTestSetsByTab('all');
    goToQuizStep(2);
  };

  // Step 2 Sub-Tabs Filter
  window.filterTestSetsByTab = function(tabName) {
    window.tsState.currentSubTab = tabName;
    const tabs = ['all', 'part1', 'part2', 'special'];
    tabs.forEach(t => {
      const el = document.getElementById('ts-subtab-' + t);
      if (el) {
        if (t === tabName) {
          el.style.color = '#FFFFFF';
          el.style.fontWeight = '800';
          el.style.borderBottom = '3px solid #FFFFFF';
        } else {
          el.style.color = '#71717A';
          el.style.fontWeight = '600';
          el.style.borderBottom = 'none';
        }
      }
    });

    renderCurrentTopicSets();
  };

  function renderCurrentTopicSets() {
    const topic = window.tsState.selectedTopic;
    if (!topic) return;

    // Filter questions for this topic
    let pool = [];
    if (topic.id === 'all') {
      pool = [...(window.ALL_MCQS_DATA || [])];
    } else if (topic.id === 'bookmarks') {
      pool = [...(window.quizBookmarks || [])];
    } else if (topic.id === 'aarti_chalisa') {
      pool = (window.ALL_MCQS_DATA || []).filter(q => q.category === 'aarti' || q.category === 'chalisa');
    } else {
      pool = (window.ALL_MCQS_DATA || []).filter(q => q.category === topic.category);
    }

    if (pool.length === 0 && topic.id !== 'bookmarks') {
      pool = [...(window.ALL_MCQS_DATA || [])];
    }

    const setsListEl = document.getElementById('ts-sets-list');
    if (!setsListEl) return;

    const setTitles = topic.setTitles || ['मॉक टेस्ट #1'];
    const totalPossibleSets = Math.max(1, Math.min(setTitles.length, Math.ceil(pool.length / 10) || 1));

    let startIndex = 0;
    let endIndex = totalPossibleSets;

    if (window.tsState.currentSubTab === 'part1') {
      startIndex = 0;
      endIndex = Math.min(5, totalPossibleSets);
    } else if (window.tsState.currentSubTab === 'part2') {
      startIndex = Math.min(5, totalPossibleSets);
      endIndex = Math.min(10, totalPossibleSets);
    } else if (window.tsState.currentSubTab === 'special') {
      startIndex = Math.min(10, totalPossibleSets);
      endIndex = totalPossibleSets;
      if (startIndex >= endIndex) {
        startIndex = 0; // fallback if fewer sets
      }
    }

    let itemsHtml = '';
    for (let i = startIndex; i < endIndex; i++) {
      const setName = setTitles[i] || `मॉक टेस्ट #${i + 1}`;
      const qCount = Math.min(10, Math.max(1, pool.length - (i * 10)) || 10);
      const marks = (qCount * 2.0).toFixed(1);

      itemsHtml += `
        <div onclick="selectTestSetAndShowInstructions(${i})" class="ts-test-card" style="background:#18181B; border:1px solid #27272A; border-radius:14px; padding:15px; margin-bottom:12px; cursor:pointer; transition:transform 0.15s ease, border-color 0.15s ease;">
          <!-- Top Badges (Image 2 Exact Badges) -->
          <div style="display:flex; align-items:center; gap:8px; margin-bottom:10px;">
            <span style="background:#10B981; color:#FFFFFF; font-size:0.68rem; font-weight:900; padding:2px 7px; border-radius:4px; text-transform:uppercase; letter-spacing:0.4px;">FREE</span>
            <span style="background:#6366F1; color:#FFFFFF; font-size:0.68rem; font-weight:900; padding:2px 7px; border-radius:4px; letter-spacing:0.3px;">Must Attempt</span>
          </div>

          <!-- Test Title -->
          <h4 style="font-size:0.98rem; font-weight:800; color:#F4F4F5; margin:0 0 10px 0; line-height:1.45;">
            ${topic.shortTitle}: ${setName}
          </h4>

          <!-- Meta Row: Qs, Mins, Marks and Start Test Link -->
          <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
            <div style="font-size:0.8rem; color:#A1A1AA; font-weight:600;">
              ${qCount} Qs . 10 mins . ${marks} Marks
            </div>
            <div style="font-size:0.88rem; font-weight:800; color:#3B82F6; display:flex; align-items:center; gap:4px;">
              Start Test
            </div>
          </div>

          <!-- Divider -->
          <div style="height:1px; background:#27272A; margin-bottom:10px;"></div>

          <!-- Footer: Syllabus & Share -->
          <div style="display:flex; align-items:center; justify-content:space-between; font-size:0.75rem;">
            <div style="color:#60A5FA; font-weight:700;">
              Syllabus <span style="color:#A1A1AA; font-weight:500;">English, Hindi</span>
            </div>
            <div onclick="event.stopPropagation(); shareTestInfo('${topic.shortTitle} - ${setName}')" style="color:#34D399; font-weight:700; display:flex; align-items:center; gap:4px; cursor:pointer;">
              <span>🔗</span> Share
            </div>
          </div>
        </div>
      `;
    }

    if (!itemsHtml) {
      itemsHtml = `
        <div style="text-align:center; padding:30px 16px; color:#A1A1AA;">
          <div style="font-size:1.8rem; margin-bottom:8px;">📚</div>
          <p style="font-size:0.88rem; font-weight:600; margin:0;">इस टैब में टेस्ट उपलब्ध नहीं हैं। कृपया 'सभी टेस्ट' देखें।</p>
        </div>
      `;
    }

    setsListEl.innerHTML = itemsHtml;
  }

  // 6. Step 3: Instructions Screen (Image 3 Style)
  window.selectTestSetAndShowInstructions = function(setIndex) {
    const topic = window.tsState.selectedTopic;
    if (!topic) return;

    let pool = [];
    if (topic.id === 'all') {
      pool = [...(window.ALL_MCQS_DATA || [])];
    } else if (topic.id === 'bookmarks') {
      pool = [...(window.quizBookmarks || [])];
    } else if (topic.id === 'aarti_chalisa') {
      pool = (window.ALL_MCQS_DATA || []).filter(q => q.category === 'aarti' || q.category === 'chalisa');
    } else {
      pool = (window.ALL_MCQS_DATA || []).filter(q => q.category === topic.category);
    }
    if (pool.length === 0) pool = [...(window.ALL_MCQS_DATA || [])];

    // Pick 10 questions for this set
    const startIdx = (setIndex * 10) % Math.max(1, pool.length);
    let selectedQs = pool.slice(startIdx, startIdx + 10);
    if (selectedQs.length < 10) {
      selectedQs = selectedQs.concat(pool.slice(0, 10 - selectedQs.length));
    }
    if (selectedQs.length === 0) {
      selectedQs = (window.ALL_MCQS_DATA || []).slice(0, 10);
    }

    const setName = (topic.setTitles && topic.setTitles[setIndex]) || `मॉक टेस्ट #${setIndex + 1}`;
    const testTitle = `${topic.shortTitle}: ${setName}`;

    window.tsState.selectedTestSet = {
      index: setIndex,
      title: testTitle,
      setName: setName,
      questions: selectedQs,
      totalQuestions: selectedQs.length,
      durationMins: 10,
      maxMarks: (selectedQs.length * 2.0).toFixed(1)
    };

    // Populate Step 3 Elements
    const titleEl = document.getElementById('ts-instr-test-title');
    const metaEl = document.getElementById('ts-instr-meta');
    const countSpan = document.getElementById('ts-instr-total-q');
    const marksSpan = document.getElementById('ts-instr-marks-each');

    if (titleEl) titleEl.textContent = testTitle;
    if (metaEl) metaEl.textContent = `Duration: 10 Mins.    Maximum Marks: ${(selectedQs.length * 2.0).toFixed(1)}`;
    if (countSpan) countSpan.textContent = selectedQs.length;
    if (marksSpan) marksSpan.textContent = `2`;

    goToQuizStep(3);
  };

  // 7. Step 4: Start Actual Exam (Image 4 Style)
  window.startActualExam = function() {
    const testSet = window.tsState.selectedTestSet;
    if (!testSet || !testSet.questions || testSet.questions.length === 0) {
      showEngineToast('प्रश्नों की सूची उपलब्ध नहीं है। कृपया पुनः प्रयास करें।');
      return;
    }

    // Set Language from Step 3 dropdown
    const langSelect = document.getElementById('ts-lang-select');
    window.tsState.selectedLanguage = langSelect ? langSelect.value : 'hi';

    // Format examination questions
    window.tsState.examQuestions = testSet.questions.map((q, idx) => ({
      id: q.id || idx + 1,
      q: q.question || q.q || 'सनातन ज्ञान प्रश्न',
      opts: q.options || q.opts || ['विकल्प 1', 'विकल्प 2', 'विकल्प 3', 'विकल्प 4'],
      correct: (typeof q.correct_answer === 'number') ? q.correct_answer : (q.correct || 0),
      desc: q.explanation || q.desc || 'पावन सनातन ज्ञान का दिव्य उत्तर।',
      category: q.category || 'all',
      map: q.map || null
    }));

    window.tsState.currentQIdx = 0;
    window.tsState.userAnswers = {};
    window.tsState.markedForReview = {};
    window.tsState.qTimeSpent = {};
    window.tsState.examTotalTime = 600; // 10 minutes
    window.tsState.examTimeLeft = 600;
    window.tsState.examSubmitted = false;
    window.tsState.examStartTime = Date.now();

    // Start Live Examination Timer
    startExamCountdownTimer();

    // Render Question #1
    renderExamQuestion(0);

    goToQuizStep(4);
    if (navigator.vibrate) navigator.vibrate(30);
  };

  // Exam Countdown Timer (00:09:59)
  function startExamCountdownTimer() {
    clearInterval(window.tsState.examTimerInterval);
    clearInterval(window.tsState.qTimerInterval);

    window.tsState.examTimerInterval = setInterval(() => {
      if (window.tsState.examTimeLeft > 0) {
        window.tsState.examTimeLeft--;
        updateExamTimerUI();
      } else {
        clearInterval(window.tsState.examTimerInterval);
        showEngineToast('⏱️ समय समाप्त हो गया है! परीक्षा सबमिट की जा रही है...');
        submitExam();
      }
    }, 1000);

    // Per-question timer
    window.tsState.qTimerInterval = setInterval(() => {
      const idx = window.tsState.currentQIdx;
      window.tsState.qTimeSpent[idx] = (window.tsState.qTimeSpent[idx] || 0) + 1;
      const qTimerEl = document.getElementById('ts-exam-q-timer');
      if (qTimerEl) {
        const spent = window.tsState.qTimeSpent[idx];
        const m = String(Math.floor(spent / 60)).padStart(2, '0');
        const s = String(spent % 60).padStart(2, '0');
        qTimerEl.textContent = `${m}:${s}`;
      }
    }, 1000);
  }

  function updateExamTimerUI() {
    const el = document.getElementById('ts-exam-countdown-text');
    if (!el) return;
    const totalSecs = window.tsState.examTimeLeft;
    const hrs = String(Math.floor(totalSecs / 3600)).padStart(2, '0');
    const mins = String(Math.floor((totalSecs % 3600) / 60)).padStart(2, '0');
    const secs = String(totalSecs % 60).padStart(2, '0');
    el.textContent = `${hrs}:${mins}:${secs}`;
  }

  // Render Current Question in Step 4
  window.renderExamQuestion = function(idx) {
    if (idx < 0 || idx >= window.tsState.examQuestions.length) return;
    window.tsState.currentQIdx = idx;

    const q = window.tsState.examQuestions[idx];
    const total = window.tsState.examQuestions.length;

    // Header Title
    const headerTitle = document.getElementById('ts-exam-header-title');
    if (headerTitle && window.tsState.selectedTestSet) {
      headerTitle.textContent = window.tsState.selectedTestSet.setName || window.tsState.selectedTestSet.title;
    }

    // Question Number badge (Circle)
    const numBadge = document.getElementById('ts-exam-q-num');
    if (numBadge) numBadge.textContent = `${idx + 1}`;

    // Question Timer
    const qTimerEl = document.getElementById('ts-exam-q-timer');
    if (qTimerEl) {
      const spent = window.tsState.qTimeSpent[idx] || 0;
      const m = String(Math.floor(spent / 60)).padStart(2, '0');
      const s = String(spent % 60).padStart(2, '0');
      qTimerEl.textContent = `${m}:${s}`;
    }

    // Question Text
    const qTextEl = document.getElementById('ts-exam-q-text');
    if (qTextEl) qTextEl.textContent = q.q;

    // Bookmark icon state
    updateBookmarkIconState(q);

    // Options List (1. 2. 3. 4.)
    const optionsContainer = document.getElementById('ts-exam-options-list');
    if (optionsContainer) {
      const selectedOpt = window.tsState.userAnswers[idx];

      optionsContainer.innerHTML = q.opts.map((opt, optIdx) => {
        const isSelected = (selectedOpt === optIdx);
        const bg = isSelected ? 'rgba(59, 130, 246, 0.16)' : '#18181B';
        const border = isSelected ? '1.5px solid #3B82F6' : '1px solid #27272A';
        const numColor = isSelected ? '#60A5FA' : '#A1A1AA';

        return `
          <div onclick="selectExamOption(${optIdx})" class="ts-opt-card" style="display:flex; align-items:flex-start; gap:12px; padding:14px 16px; background:${bg}; border:${border}; border-radius:12px; cursor:pointer; transition:all 0.15s ease; box-shadow:${isSelected ? '0 0 14px rgba(59,130,246,0.3)' : 'none'};">
            <span style="font-size:0.92rem; font-weight:800; color:${numColor}; min-width:20px;">${optIdx + 1}.</span>
            <span style="font-size:0.94rem; font-weight:600; color:#F4F4F5; line-height:1.45; flex:1;">${opt}</span>
            <div style="width:18px; height:18px; border-radius:50%; border:1.5px solid ${isSelected ? '#3B82F6' : '#52525B'}; background:${isSelected ? '#3B82F6' : 'transparent'}; display:flex; align-items:center; justify-content:center; flex-shrink:0; margin-top:2px;">
              ${isSelected ? '<div style="width:6px; height:6px; border-radius:50%; background:#FFF;"></div>' : ''}
            </div>
          </div>
        `;
      }).join('');
    }

    // Save & Next Button Text (if last question: "Submit Test")
    const saveNextBtn = document.getElementById('ts-btn-save-next');
    if (saveNextBtn) {
      if (idx === total - 1) {
        saveNextBtn.textContent = 'Submit Test';
        saveNextBtn.style.background = '#10B981';
      } else {
        saveNextBtn.textContent = 'Save & Next';
        saveNextBtn.style.background = '#3B82F6';
      }
    }

    // Update Question Palette if open
    updatePaletteView();
  };

  // Option Selection
  window.selectExamOption = function(optIdx) {
    const idx = window.tsState.currentQIdx;
    window.tsState.userAnswers[idx] = optIdx;
    renderExamQuestion(idx);
    if (navigator.vibrate) navigator.vibrate(20);
  };

  // Clear Option
  window.clearCurrentExamOption = function() {
    const idx = window.tsState.currentQIdx;
    delete window.tsState.userAnswers[idx];
    delete window.tsState.markedForReview[idx];
    renderExamQuestion(idx);
  };

  // Mark & Next (Mark for Review & Move to next)
  window.markAndNextQuestion = function() {
    const idx = window.tsState.currentQIdx;
    window.tsState.markedForReview[idx] = true;
    const nextIdx = idx + 1;
    if (nextIdx < window.tsState.examQuestions.length) {
      renderExamQuestion(nextIdx);
    } else {
      updatePaletteView();
    }
  };

  // Save & Next (Save response & Move to next)
  window.saveAndNextQuestion = function() {
    const idx = window.tsState.currentQIdx;
    delete window.tsState.markedForReview[idx];

    const nextIdx = idx + 1;
    if (nextIdx < window.tsState.examQuestions.length) {
      renderExamQuestion(nextIdx);
    } else {
      // Last Question -> Confirm & Submit
      confirmAndSubmitExam();
    }
  };

  // Toggle Language between Hindi and English
  window.toggleExamLanguage = function() {
    window.tsState.selectedLanguage = (window.tsState.selectedLanguage === 'hi') ? 'en' : 'hi';
    const btn = document.getElementById('ts-exam-lang-btn');
    if (btn) btn.textContent = (window.tsState.selectedLanguage === 'hi') ? 'अ' : 'E';
    showEngineToast(window.tsState.selectedLanguage === 'hi' ? 'भाषा: हिंदी (Hindi)' : 'Language: English');
  };

  // Bookmark Toggle
  window.toggleExamBookmark = function() {
    const idx = window.tsState.currentQIdx;
    const q = window.tsState.examQuestions[idx];
    if (!q) return;

    window.quizBookmarks = window.quizBookmarks || [];
    const existingIdx = window.quizBookmarks.findIndex(b => (b.question || b.q) === q.q);
    if (existingIdx >= 0) {
      window.quizBookmarks.splice(existingIdx, 1);
      showEngineToast('🔖 प्रश्न बुकमार्क से हटा दिया गया');
    } else {
      window.quizBookmarks.push(q);
      showEngineToast('⭐ प्रश्न सफलतापूर्वक बुकमार्क कर लिया गया!');
    }
    localStorage.setItem('sanatan_quiz_bookmarks', JSON.stringify(window.quizBookmarks));
    updateBookmarkIconState(q);
  };

  function updateBookmarkIconState(q) {
    const btn = document.getElementById('ts-exam-bookmark-btn');
    if (!btn || !q) return;
    const isBookmarked = (window.quizBookmarks || []).some(b => (b.question || b.q) === q.q);
    btn.style.color = isBookmarked ? '#F59E0B' : '#A1A1AA';
  }

  // Report Question
  window.reportCurrentExamQuestion = function() {
    showEngineToast('🚩 आपका संदेह/रिपोर्ट दर्ज हो गया है। हमारी टीम इसे सत्यापित करेगी।');
  };

  // Question Palette Drawer (Slide-out Grid of 1 to 10)
  window.toggleQuestionPalette = function(show) {
    const paletteEl = document.getElementById('ts-palette-drawer');
    if (!paletteEl) return;
    window.tsState.isPaletteOpen = (typeof show === 'boolean') ? show : !window.tsState.isPaletteOpen;
    paletteEl.style.display = window.tsState.isPaletteOpen ? 'block' : 'none';
    if (window.tsState.isPaletteOpen) updatePaletteView();
  };

  function updatePaletteView() {
    const gridEl = document.getElementById('ts-palette-grid');
    if (!gridEl) return;

    gridEl.innerHTML = window.tsState.examQuestions.map((q, idx) => {
      const isCurrent = (idx === window.tsState.currentQIdx);
      const isAnswered = (typeof window.tsState.userAnswers[idx] === 'number');
      const isMarked = !!window.tsState.markedForReview[idx];

      let bg = '#27272A';
      let color = '#E4E4E7';
      let border = '1px solid transparent';

      if (isMarked) {
        bg = '#7C3AED'; // Purple
        color = '#FFFFFF';
      } else if (isAnswered) {
        bg = '#10B981'; // Green
        color = '#FFFFFF';
      }

      if (isCurrent) {
        border = '2px solid #F59E0B';
      }

      return `
        <button onclick="jumpToExamQuestion(${idx})" style="width:40px; height:40px; border-radius:10px; background:${bg}; color:${color}; border:${border}; font-size:0.9rem; font-weight:800; cursor:pointer; display:flex; align-items:center; justify-content:center; transition:all 0.15s ease;">
          ${idx + 1}
        </button>
      `;
    }).join('');
  }

  window.jumpToExamQuestion = function(idx) {
    toggleQuestionPalette(false);
    renderExamQuestion(idx);
  };

  // Confirm and Submit Exam
  window.confirmAndSubmitExam = function() {
    const answeredCount = Object.keys(window.tsState.userAnswers).length;
    const total = window.tsState.examQuestions.length;
    const unattempted = total - answeredCount;

    if (confirm(`क्या आप टेस्ट सबमिट करना चाहते हैं?\n\n• कुल प्रश्न: ${total}\n• उत्तर दिए गए: ${answeredCount}\n• अनुत्तरित: ${unattempted}`)) {
      submitExam();
    }
  };

  // 8. Step 5: Submit Exam & Show Scorecard (Image Review & Score)
  window.submitExam = function() {
    clearInterval(window.tsState.examTimerInterval);
    clearInterval(window.tsState.qTimerInterval);
    window.tsState.examSubmitted = true;

    const total = window.tsState.examQuestions.length;
    let correct = 0;
    let wrong = 0;
    let skipped = 0;

    window.tsState.examQuestions.forEach((q, idx) => {
      const userAns = window.tsState.userAnswers[idx];
      if (typeof userAns === 'number') {
        if (userAns === q.correct) {
          correct++;
        } else {
          wrong++;
        }
      } else {
        skipped++;
      }
    });

    // Record user's correct answers to cumulative Wall of Fame score
    if (correct > 0 && typeof window.recordMcqCorrectAnswers === 'function') {
      window.recordMcqCorrectAnswers(correct);
    }

    // Score calculated with +2.0 and -0.5 negative marking
    const rawScore = (correct * 2.0) - (wrong * 0.5);
    const marksObtained = Math.max(0, rawScore).toFixed(1);
    const maxMarks = (total * 2.0).toFixed(1);
    const accuracy = (correct + wrong > 0) ? Math.round((correct / (correct + wrong)) * 100) : 0;
    const timeSpentSecs = Math.max(1, 600 - window.tsState.examTimeLeft);
    const timeMins = Math.floor(timeSpentSecs / 60);
    const timeSecs = timeSpentSecs % 60;

    // Fill Scorecard UI
    const titleEl = document.getElementById('ts-result-test-title');
    const marksEl = document.getElementById('ts-result-score');
    const accEl = document.getElementById('ts-result-accuracy');
    const timeEl = document.getElementById('ts-result-time');
    const correctEl = document.getElementById('ts-result-correct');
    const wrongEl = document.getElementById('ts-result-wrong');
    const skipEl = document.getElementById('ts-result-skipped');

    if (titleEl && window.tsState.selectedTestSet) titleEl.textContent = window.tsState.selectedTestSet.title;
    if (marksEl) marksEl.textContent = `${marksObtained} / ${maxMarks}`;
    if (accEl) accEl.textContent = `${accuracy}%`;
    if (timeEl) timeEl.textContent = `${timeMins}m ${timeSecs}s`;
    if (correctEl) correctEl.textContent = `${correct}`;
    if (wrongEl) wrongEl.textContent = `${wrong}`;
    if (skipEl) skipEl.textContent = `${skipped}`;

    // Render Solutions & Explanations List
    const reviewList = document.getElementById('ts-result-review-list');
    if (reviewList) {
      reviewList.innerHTML = window.tsState.examQuestions.map((q, idx) => {
        const userAns = window.tsState.userAnswers[idx];
        const isRight = (userAns === q.correct);
        const isSkipped = (typeof userAns !== 'number');

        let statusBadge = '<span style="color:#10B981; font-weight:800;">✓ सही उत्तर</span>';
        let cardBorder = '#10B981';
        if (isSkipped) {
          statusBadge = '<span style="color:#94A3B8; font-weight:800;">⚪ अनुत्तरित</span>';
          cardBorder = '#3F3F46';
        } else if (!isRight) {
          statusBadge = '<span style="color:#EF4444; font-weight:800;">✕ गलत उत्तर</span>';
          cardBorder = '#EF4444';
        }

        return `
          <div style="background:#18181B; border:1px solid ${cardBorder}; border-radius:14px; padding:14px; margin-bottom:12px; text-align:left;">
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
              <span style="font-size:0.8rem; font-weight:900; color:#F59E0B;">प्रश्न ${idx + 1}</span>
              <span style="font-size:0.75rem;">${statusBadge}</span>
            </div>
            <p style="font-size:0.92rem; font-weight:700; color:#F4F4F5; margin:0 0 10px 0; line-height:1.45;">
              ${q.q}
            </p>
            <div style="font-size:0.82rem; margin-bottom:6px;">
              <span style="color:#A1A1AA;">आपका उत्तर:</span> 
              <strong style="color:${isRight ? '#10B981' : '#EF4444'};">${isSkipped ? 'कोई नहीं' : q.opts[userAns]}</strong>
            </div>
            <div style="font-size:0.82rem; margin-bottom:8px;">
              <span style="color:#A1A1AA;">सही उत्तर:</span> 
              <strong style="color:#10B981;">${q.opts[q.correct]}</strong>
            </div>
            <div style="background:rgba(255,255,255,0.05); border-radius:8px; padding:8px 10px; font-size:0.8rem; color:#CBD5E1; line-height:1.4;">
              💡 <strong>स्पष्टीकरण:</strong> ${q.desc}
            </div>
          </div>
        `;
      }).join('');
    }

    goToQuizStep(5);
    if (typeof triggerFlowerShower === 'function' && correct >= 7) triggerFlowerShower();
  };

  // 9. Generic Step Switcher (Step 1 ➔ 2 ➔ 3 ➔ 4 ➔ 5)
  window.goToQuizStep = function(stepNum) {
    window.tsState.currentStep = stepNum;

    const step1 = document.getElementById('ts-step-topics');       // Step 1
    const step2 = document.getElementById('ts-step-tests');        // Step 2
    const step3 = document.getElementById('ts-step-instructions'); // Step 3
    const step4 = document.getElementById('ts-step-exam');         // Step 4
    const step5 = document.getElementById('ts-step-result');       // Step 5
    const stepWall = document.getElementById('ts-step-wall-of-fame'); // Step Wall of Fame

    if (step1) step1.style.display = (stepNum === 1) ? 'flex' : 'none';
    if (step2) step2.style.display = (stepNum === 2) ? 'flex' : 'none';
    if (step3) step3.style.display = (stepNum === 3) ? 'flex' : 'none';
    if (step4) step4.style.display = (stepNum === 4) ? 'flex' : 'none';
    if (step5) step5.style.display = (stepNum === 5) ? 'flex' : 'none';
    if (stepWall) stepWall.style.display = (stepNum === 'wall' || stepNum === 6) ? 'flex' : 'none';

    // Auto-scroll modal container to top on view change
    const cardEl = document.getElementById('quiz-hub-card');
    if (cardEl) cardEl.scrollTop = 0;
  };

  // 10. Main Modal Open / Close Controllers
  window.openQuizHubModal = async function() {
    const modal = document.getElementById('quiz-hub-modal');
    if (!modal) return;

    modal.style.display = 'flex';
    injectTestSeriesStyles();
    await window.ensureMCQsLoaded();

    // Default ALWAYS to Step 1 (Topics list - Image 1)
    renderTopicsListStep();
    goToQuizStep(1);

    if (navigator.vibrate) navigator.vibrate(25);
  };
  window.openSanatanTestSeriesModal = window.openQuizHubModal;

  window.closeQuizHubModal = function() {
    const modal = document.getElementById('quiz-hub-modal');
    if (modal) modal.style.display = 'none';
    clearInterval(window.tsState.examTimerInterval);
    clearInterval(window.tsState.qTimerInterval);
  };

  // WhatsApp Share
  window.shareTestInfo = function(title) {
    const text = `🚩 सनातन ज्ञान परीक्षा: ${title}\n\nआज ही भक्ति ऐप में अपना ज्ञान परखें!`;
    window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, '_blank');
  };

  window.shareScoreWhatsApp = function() {
    const testSet = window.tsState.selectedTestSet;
    const title = testSet ? testSet.title : 'सनातन मॉक टेस्ट';
    const score = document.getElementById('ts-result-score')?.textContent || '';
    const text = `🚩 मैंने सनातन मॉक टेस्ट में उत्कृष्ट प्रदर्शन किया!\n\n📚 टेस्ट: ${title}\n🏆 स्कोर: ${score}\n\nआप भी भक्ति ऐप में अपना स्कोर आजमाएं!`;
    window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, '_blank');
  };

  // Auto-init on script load
  window.addEventListener('DOMContentLoaded', () => {
    window.ensureMCQsLoaded();
  });

  // ═════════════════════════════════════════════════════════════════════════════
  // 🏆 SANATAN WALL OF FAME (TESTBOOK STYLE LIVE ALL INDIA LEADERBOARD)
  // ═════════════════════════════════════════════════════════════════════════════

  window.DEFAULT_WOF_TOPPERS = [
    { id: 'samridhi', name: 'Samridhi Talwar', avatar: 'assets/wall_of_fame/rank_1_samridhi.jpg', correctAnswers: 98, exam: 'रामायण महाकाव्य 2024' },
    { id: 'ashish', name: 'Ashish Tiwari', avatar: 'assets/wall_of_fame/rank_2_ashish.jpg', correctAnswers: 94, exam: 'महाभारत एवं गीता 2024' },
    { id: 'debesh', name: 'Debesh Bairagi', avatar: 'assets/wall_of_fame/rank_3_debesh.jpg', correctAnswers: 90, exam: 'चारों वेद एवं उपनिषद' },
    { id: 'ishant', name: 'Ishant Shukla', avatar: 'assets/wall_of_fame/rank_4_ishant.jpg', correctAnswers: 86, exam: 'श्रीमद्भगवद्गीता ज्ञान' },
    { id: 'rohit', name: 'Rohit Chadhar', avatar: 'assets/wall_of_fame/rank_5_rohit.jpg', correctAnswers: 82, exam: 'वैदिक मंत्र एवं स्तोत्र' },
    { id: 'sagardip', name: 'Sagardip Ghosh', avatar: 'assets/wall_of_fame/rank_6_sagardip.jpg', correctAnswers: 78, exam: 'देवी-देवता दर्शन टेस्ट' },
    { id: 'mohan', name: 'Mohan Kumar', avatar: 'assets/wall_of_fame/rank_7_mohan.jpg', correctAnswers: 74, exam: 'भक्ति साहित्य एवं संत' },
    { id: 'sanket', name: 'Sanket Paul', avatar: 'assets/wall_of_fame/rank_8_sanket.jpg', correctAnswers: 70, exam: 'आरती व चालीसा पाठ' },
    { id: 'shaurya', name: 'Shaurya Kumar', avatar: 'assets/wall_of_fame/rank_9_shaurya.jpg', correctAnswers: 66, exam: 'सनातन इतिहास टेस्ट' },
    { id: 'prachi', name: 'Prachi Purohit', avatar: 'assets/wall_of_fame/rank_10_prachi.jpg', correctAnswers: 62, exam: 'उपनिषद दर्शन 2024' },
    { id: 'anam', name: 'Anam Zafar', avatar: 'assets/wall_of_fame/rank_11_anam.jpg', correctAnswers: 58, exam: 'सनातन ज्ञान प्रवाह' },
    { id: 'diksha', name: 'Diksha Dawar', avatar: 'assets/wall_of_fame/rank_12_diksha.jpg', correctAnswers: 54, exam: 'दिव्य तीर्थ महाकुंभ' }
  ];

  window.getWallOfFameUserRecord = function() {
    let raw = localStorage.getItem('bhakti_user');
    let u = {};
    if (raw) {
      try { u = JSON.parse(raw); } catch(e) {}
    }
    const savedName = localStorage.getItem('bhakti_user_name') || u.name || (u.isLoggedIn ? 'सनातन साधक' : 'आप (साधक)');
    const savedAvatar = localStorage.getItem('bhakti_user_avatar') || u.avatar || u.photoURL || 'assets/gallery/bal_ganesha_little.jpg';
    const isLoggedIn = !!(u && (u.isLoggedIn || u.name || u.email));
    const correctCount = parseInt(localStorage.getItem('sanatan_mcq_user_correct_count') || '0', 10);

    return {
      id: 'current_user',
      name: savedName,
      avatar: savedAvatar,
      correctAnswers: correctCount,
      exam: isLoggedIn ? 'सत्यापित सनातन साधक' : 'अतिथि साधक',
      isUser: true,
      isLoggedIn: isLoggedIn
    };
  };

  window.getSortedWallOfFameList = function() {
    const userRec = window.getWallOfFameUserRecord();
    const list = window.DEFAULT_WOF_TOPPERS.map(t => ({ ...t, isUser: false }));

    list.push(userRec);

    // Sort strictly descending by correct answers: whoever answers most correct answers is at top!
    list.sort((a, b) => {
      if (b.correctAnswers !== a.correctAnswers) {
        return b.correctAnswers - a.correctAnswers;
      }
      return a.isUser ? -1 : 1;
    });

    list.forEach((item, idx) => {
      item.rank = idx + 1;
      item.rankBadge = `AIR ${item.rank} | ${item.correctAnswers} प्रश्न सही`;
    });

    return { list, userRec };
  };

  window.recordMcqCorrectAnswers = function(newCorrect) {
    if (!newCorrect || newCorrect <= 0) return;
    const prev = parseInt(localStorage.getItem('sanatan_mcq_user_correct_count') || '0', 10);
    const updated = prev + newCorrect;
    localStorage.setItem('sanatan_mcq_user_correct_count', updated.toString());
    console.log(`✓ [WallOfFame] +${newCorrect} correct answers recorded. Total: ${updated}`);
    if (document.getElementById('ts-step-wall-of-fame')?.style.display === 'flex') {
      window.renderWallOfFame();
    }
  };

  window.boostMcqDemoScore = function(points = 10) {
    const prev = parseInt(localStorage.getItem('sanatan_mcq_user_correct_count') || '0', 10);
    const updated = prev + points;
    localStorage.setItem('sanatan_mcq_user_correct_count', updated.toString());
    if (typeof showEngineToast === 'function') {
      showEngineToast(`🎉 +${points} सही उत्तर जुड़े! कुल: ${updated}`);
    }
    window.renderWallOfFame();
    if (updated > 98 && typeof triggerFlowerShower === 'function') {
      triggerFlowerShower();
      if (typeof playSoundEffect === 'function') playSoundEffect('victory');
    }
  };

  window.resetMcqUserScore = function() {
    localStorage.setItem('sanatan_mcq_user_correct_count', '0');
    if (typeof showEngineToast === 'function') {
      showEngineToast('🔄 आपका स्कोर रीसेट हुआ!');
    }
    window.renderWallOfFame();
  };

  window.renderWallOfFame = function() {
    const { list, userRec } = window.getSortedWallOfFameList();
    const userRank = list.find(x => x.isUser)?.rank || list.length;
    const isRank1 = (userRank === 1);

    // 1. Render User Strip Ribbon
    const stripEl = document.getElementById('wof-user-strip');
    if (stripEl) {
      const topScore = list[0].correctAnswers;
      const neededForRank1 = Math.max(0, topScore - userRec.correctAnswers + 1);

      let statusMsg = '';
      if (isRank1) {
        statusMsg = `<span style="color:#059669; font-weight:900;">👑 अद्भुत! आप ऑल इंडिया रैंक #1 पर हैं! 🚩</span>`;
      } else {
        statusMsg = `<span style="color:#D97706; font-weight:700;">रैंक #1 के लिए और <strong>${neededForRank1}</strong> प्रश्न सही करें</span>`;
      }

      stripEl.innerHTML = `
        <div style="display:flex; align-items:center; gap:10px; flex:1; min-width:0;">
          <div style="position:relative; width:44px; height:44px; flex-shrink:0;">
            <img src="${userRec.avatar}" alt="${userRec.name}" onerror="this.src='assets/gallery/bal_ganesha_little.jpg'" style="width:44px; height:44px; border-radius:50%; object-fit:cover; border:2px solid #F59E0B; box-shadow:0 2px 8px rgba(0,0,0,0.15);" onclick="if(typeof openAvatarPickerModal==='function')openAvatarPickerModal();"/>
            <div style="position:absolute; bottom:-2px; right:-2px; background:#F59E0B; color:#1A0B2E; font-size:9px; font-weight:900; width:16px; height:16px; border-radius:50%; display:flex; align-items:center; justify-content:center; border:1.5px solid #FFF;">
              ${userRank}
            </div>
          </div>
          <div style="min-width:0;">
            <div style="display:flex; align-items:center; gap:6px;">
              <span style="font-size:0.88rem; font-weight:900; color:#1E293B; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${userRec.name}</span>
              ${userRec.isLoggedIn ? '<span style="background:#10B981; color:#FFF; font-size:0.58rem; font-weight:900; padding:1px 5px; border-radius:6px;">✓ Logged In</span>' : ''}
            </div>
            <div style="font-size:0.72rem; color:#059669; font-weight:800;">
              AIR ${userRank} • ${userRec.correctAnswers} प्रश्न सही
            </div>
            <div style="font-size:0.65rem; margin-top:1px;">
              ${statusMsg}
            </div>
          </div>
        </div>
        <div style="display:flex; flex-direction:column; gap:4px; align-items:flex-end; flex-shrink:0;">
          ${!userRec.isLoggedIn ? `
            <button onclick="if(typeof openGoogleAccountPickerModal==='function'){openGoogleAccountPickerModal();}else{document.getElementById('auth-modal').style.display='flex';}" style="background:#FFFFFF; border:1px solid #CBD5E1; color:#0F172A; font-size:0.7rem; font-weight:800; padding:5px 9px; border-radius:10px; cursor:pointer; display:flex; align-items:center; gap:4px; box-shadow:0 1px 3px rgba(0,0,0,0.08);">
              <span>🔑</span> लॉगिन करें
            </button>
          ` : `
            <button onclick="if(typeof openAvatarPickerModal==='function')openAvatarPickerModal();" style="background:#FFFFFF; border:1px solid #CBD5E1; color:#3B82F6; font-size:0.68rem; font-weight:800; padding:4px 8px; border-radius:8px; cursor:pointer;">
              अवतार बदलें
            </button>
          `}
        </div>
      `;
    }

    // 2. Render 12+ Cards Grid in exact Testbook style
    const gridEl = document.getElementById('wof-cards-grid');
    if (!gridEl) return;

    gridEl.innerHTML = list.map(item => {
      const isUser = item.isUser;
      const cardBorder = isUser ? '2px solid #F59E0B' : '1px solid #E2E8F0';
      const cardBg = isUser ? 'linear-gradient(180deg, #FEFCE8 0%, #FFFFFF 100%)' : '#FFFFFF';
      const cardShadow = isUser ? '0 8px 24px rgba(245,158,11,0.28)' : '0 4px 16px rgba(0,0,0,0.04)';

      return `
        <div class="wof-card ${isUser ? 'wof-card-user' : ''}" onclick="${isUser ? (item.isLoggedIn ? "if(typeof openAvatarPickerModal==='function')openAvatarPickerModal();" : "if(typeof openGoogleAccountPickerModal==='function'){openGoogleAccountPickerModal();}else{document.getElementById('auth-modal').style.display='flex';}") : `showEngineToast('🏆 ${item.name} (${item.rankBadge})')`}" style="background:${cardBg}; border:${cardBorder}; border-radius:18px; padding:14px 8px 12px; text-align:center; box-shadow:${cardShadow}; position:relative; display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:165px; cursor:pointer;">
          
          ${isUser ? `<div style="position:absolute; top:6px; left:50%; transform:translateX(-50%); background:#F59E0B; color:#1A0B2E; font-size:0.62rem; font-weight:900; padding:2px 8px; border-radius:8px; white-space:nowrap; box-shadow:0 2px 6px rgba(245,158,11,0.4);">⭐ आप (YOU)</div>` : ''}

          <!-- Circular Avatar with Decorative Festive Accents -->
          <div style="position:relative; width:88px; height:88px; display:flex; align-items:center; justify-content:center; margin-top:${isUser ? '10px' : '4px'};">
            
            <!-- SVG Festive Accents: Golden Whiskers & Multi-colored Sparkle Dots -->
            <svg viewBox="0 0 100 100" style="position:absolute; inset:0; width:100%; height:100%; pointer-events:none;">
              <!-- Left Golden Whiskers -->
              <line x1="8" y1="42" x2="19" y2="42" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>
              <line x1="4" y1="50" x2="16" y2="50" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>
              <line x1="8" y1="58" x2="19" y2="58" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>

              <!-- Right Golden Whiskers -->
              <line x1="81" y1="42" x2="92" y2="42" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>
              <line x1="84" y1="50" x2="96" y2="50" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>
              <line x1="81" y1="58" x2="92" y2="58" stroke="#FBBF24" stroke-width="2.5" stroke-linecap="round"/>

              <!-- Top Whisker -->
              <line x1="50" y1="4" x2="50" y2="14" stroke="#FBBF24" stroke-width="2" stroke-linecap="round"/>

              <!-- Colorful Festive Confetti Dots -->
              <circle cx="20" cy="24" r="2.2" fill="#38BDF8"/>
              <circle cx="80" cy="24" r="2.2" fill="#EC4899"/>
              <circle cx="16" cy="74" r="2.2" fill="#8B5CF6"/>
              <circle cx="82" cy="76" r="2.2" fill="#10B981"/>
              <circle cx="30" cy="14" r="1.8" fill="#F59E0B"/>
              <circle cx="70" cy="14" r="1.8" fill="#F59E0B"/>
            </svg>

            <!-- Devotee Avatar Image -->
            <img src="${item.avatar}" alt="${item.name}" onerror="this.src='assets/gallery/bal_ganesha_little.jpg'" style="width:68px; height:68px; border-radius:50%; object-fit:cover; border:2.5px solid #F59E0B; background:#F1F5F9; box-shadow:0 4px 10px rgba(0,0,0,0.1); display:block;"/>

            <!-- Pinned Gold Star Badge -->
            <div style="position:absolute; top:6px; right:6px; width:20px; height:20px; border-radius:50%; background:#FBBF24; border:1.8px solid #FFFFFF; color:#FFFFFF; display:flex; align-items:center; justify-content:center; font-size:10px; font-weight:900; box-shadow:0 2px 6px rgba(0,0,0,0.25);">
              ★
            </div>
          </div>

          <!-- Devotee Name -->
          <div style="font-size:0.86rem; font-weight:800; color:#1E293B; margin-top:6px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:100%; width:100%; text-align:center;">
            ${item.name}
          </div>

          <!-- Rank & Score Badge -->
          <div style="font-size:0.72rem; font-weight:800; color:#059669; margin-top:3px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:100%;">
            ${item.rankBadge}
          </div>

          <!-- Subtitle / Exam / Accuracy -->
          <div style="font-size:0.64rem; font-weight:600; color:#64748B; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:100%;">
            ${item.exam}
          </div>

        </div>
      `;
    }).join('');
  };

  window.switchQuizViewTab = function(tabName) {
    const tabMock = document.getElementById('ts-tab-btn-mock');
    const tabWall = document.getElementById('ts-tab-btn-wall');
    const stepTopics = document.getElementById('ts-step-topics');
    const stepWall = document.getElementById('ts-step-wall-of-fame');

    if (tabName === 'wall_of_fame' || tabName === 'wall') {
      if (tabMock) {
        tabMock.style.color = '#71717A';
        tabMock.style.fontWeight = '600';
        tabMock.style.borderBottom = '3px solid transparent';
      }
      if (tabWall) {
        tabWall.style.color = '#F59E0B';
        tabWall.style.fontWeight = '900';
        tabWall.style.borderBottom = '3px solid #F59E0B';
      }
      if (stepTopics) stepTopics.style.display = 'none';
      if (stepWall) {
        stepWall.style.display = 'flex';
        window.renderWallOfFame();
      }
    } else {
      if (tabMock) {
        tabMock.style.color = '#FFFFFF';
        tabMock.style.fontWeight = '800';
        tabMock.style.borderBottom = '3px solid #3B82F6';
      }
      if (tabWall) {
        tabWall.style.color = '#71717A';
        tabWall.style.fontWeight = '600';
        tabWall.style.borderBottom = '3px solid transparent';
      }
      if (stepWall) stepWall.style.display = 'none';
      if (stepTopics) {
        stepTopics.style.display = 'flex';
        if (typeof renderTopicsListStep === 'function') renderTopicsListStep();
      }
    }
  };

  window.openWallOfFameModal = async function() {
    await window.openQuizHubModal();
    window.switchQuizViewTab('wall_of_fame');
  };

  // Re-render Wall of Fame if profile or user avatar changes
  window.addEventListener('storage', (e) => {
    if (e.key === 'bhakti_user' || e.key === 'bhakti_user_avatar' || e.key === 'bhakti_user_name') {
      if (document.getElementById('ts-step-wall-of-fame')?.style.display === 'flex') {
        window.renderWallOfFame();
      }
    }
  });

})();
