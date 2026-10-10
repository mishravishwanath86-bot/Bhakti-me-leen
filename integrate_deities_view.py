import re

file_path = r'd:\FabricQ_OSHub\NewsHub\NewsGraphic02\bhakti-platform\apps\web\src\views\VratUpvasView.tsx'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update imports
old_import = """import {
  Moon,
  Sun,
  Calendar,
  ChevronDown,
  ChevronUp,
  Clock,
  MapPin,
  Star,
  Flame,
  Droplets,
  Eye,
  ExternalLink,
  BookOpen
} from 'lucide-react';"""

new_import = """import {
  Moon,
  Sun,
  Calendar,
  ChevronDown,
  ChevronUp,
  Clock,
  MapPin,
  Star,
  Flame,
  Droplets,
  Eye,
  ExternalLink,
  BookOpen,
  X,
  Check,
  Copy,
  Utensils,
  Sparkles,
  Shield
} from 'lucide-react';
import {
  DEITIES_SAPTAVARA_VRATS,
  DEITIES_SAPTAVARA_INTRO,
  DeitySaptavaraVrat
} from '../data/deitiesSaptavaraData';"""

if old_import in content:
    content = content.replace(old_import, new_import)
    print("Imports updated successfully!")
else:
    print("Could not find old_import, checking alternative...")

# 2. Update activeSection state & add deity states
old_state = """export const VratUpvasView: React.FC = () => {
  const [activeSection, setActiveSection] = useState<'shivaratri' | 'sawan' | 'satyanarayana' | 'purnima' | 'navagraha'>('shivaratri');
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [selectedNavagrahaId, setSelectedNavagrahaId] = useState<string | null>(null);
  const [showAllShivaratri, setShowAllShivaratri] = useState(false);"""

new_state = """export const VratUpvasView: React.FC = () => {
  const [activeSection, setActiveSection] = useState<'deities-saptavara' | 'shivaratri' | 'sawan' | 'satyanarayana' | 'purnima' | 'navagraha'>('deities-saptavara');
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [selectedNavagrahaId, setSelectedNavagrahaId] = useState<string | null>(null);
  const [selectedDeityId, setSelectedDeityId] = useState<string | null>(null);
  const [deityDetailTab, setDeityDetailTab] = useState<'overview' | 'food' | 'vidhi' | 'udyapan'>('overview');
  const [deityLang, setDeityLang] = useState<'hi' | 'en'>('hi');
  const [introLang, setIntroLang] = useState<'en' | 'hi'>('en');
  const [copiedMantra, setCopiedMantra] = useState<boolean>(false);
  const [showAllShivaratri, setShowAllShivaratri] = useState(false);"""

if old_state in content:
    content = content.replace(old_state, new_state)
    print("State updated successfully!")
else:
    print("Could not find old_state!")

# 3. Add todayDeityVrats and selectedDeity helper
old_today = """  const todayDayNumber = new Date().getDay();
  const todayNavagraha = NAVAGRAHA_VRATS.find(v => v.dayNumber === todayDayNumber);"""

new_today = """  const todayDayNumber = new Date().getDay();
  const todayNavagraha = NAVAGRAHA_VRATS.find(v => v.dayNumber === todayDayNumber);
  const todayDeityVrats = useMemo(
    () => DEITIES_SAPTAVARA_VRATS.filter(v => v.dayNum === todayDayNumber),
    [todayDayNumber]
  );
  const selectedDeity = useMemo(
    () => DEITIES_SAPTAVARA_VRATS.find(v => v.id === selectedDeityId) || null,
    [selectedDeityId]
  );"""

if old_today in content:
    content = content.replace(old_today, new_today)
    print("todayDeityVrats added successfully!")

# 4. Add Today's Deity Weekday Vrat banner to next occurrence banners
old_banner = """          {todayNavagraha && (
            <div style={{
              padding: '14px 18px', borderRadius: '14px',
              background: 'linear-gradient(135deg,rgba(234,179,8,0.1),rgba(249,115,22,0.07))',
              border: '1px solid rgba(234,179,8,0.35)', display: 'flex', alignItems: 'center', gap: '12px'
            }}>
              <span style={{ fontSize: '28px' }}>🪐</span>
              <div>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.5px' }}>Today's Weekday Vrat</div>
                <div style={{ fontSize: '15px', fontWeight: 700, color: 'var(--text-primary)' }}>{todayNavagraha.vratNameHi}</div>
                <div style={{ fontSize: '11px', color: '#eab308', fontWeight: 600 }}>
                  🔴 Today ({todayNavagraha.dayNameEn}) • {todayNavagraha.deity}
                </div>
              </div>
            </div>
          )}"""

new_banner = """          {todayDeityVrats.length > 0 && (
            <div style={{
              padding: '14px 18px', borderRadius: '14px',
              background: 'linear-gradient(135deg,rgba(226,176,74,0.15),rgba(245,158,11,0.09))',
              border: '1px solid rgba(226,176,74,0.4)', display: 'flex', alignItems: 'center', gap: '12px'
            }}>
              <span style={{ fontSize: '28px' }}>🕉️</span>
              <div>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.5px' }}>Today's Deity Weekday Vrat</div>
                <div style={{ fontSize: '15px', fontWeight: 700, color: 'var(--text-primary)' }}>
                  {todayDeityVrats.map(v => v.nameHi).join(' व ')}
                </div>
                <div style={{ fontSize: '11px', color: 'var(--gold-accent)', fontWeight: 600 }}>
                  🔴 Today ({todayDeityVrats[0].dayHi} • {todayDeityVrats[0].dayEn}) — {todayDeityVrats.map(v => v.deityHi).join(' एवं ')}
                </div>
              </div>
            </div>
          )}
          {todayNavagraha && (
            <div style={{
              padding: '14px 18px', borderRadius: '14px',
              background: 'linear-gradient(135deg,rgba(234,179,8,0.1),rgba(249,115,22,0.07))',
              border: '1px solid rgba(234,179,8,0.35)', display: 'flex', alignItems: 'center', gap: '12px'
            }}>
              <span style={{ fontSize: '28px' }}>🪐</span>
              <div>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.5px' }}>Today's Navagraha Vrat</div>
                <div style={{ fontSize: '15px', fontWeight: 700, color: 'var(--text-primary)' }}>{todayNavagraha.vratNameHi}</div>
                <div style={{ fontSize: '11px', color: '#eab308', fontWeight: 600 }}>
                  🔴 Today ({todayNavagraha.dayNameEn}) • {todayNavagraha.deity}
                </div>
              </div>
            </div>
          )}"""

if old_banner in content:
    content = content.replace(old_banner, new_banner)
    print("Banner updated successfully!")

# 5. Update tabs
old_tabs = """      {/* SECTION TABS */}
      <div style={{ display: 'flex', gap: '4px', padding: '4px', background: 'var(--bg-primary)', borderRadius: '12px', marginBottom: '28px', width: 'fit-content', flexWrap: 'wrap' }}>
        {([
          { key: 'shivaratri' as const, emoji: '🌙', label: 'मासिक शिवरात्रि', sub: 'Masik Shivaratri 2026' },
          { key: 'sawan' as const, emoji: '💧', label: 'सावन सोमवार', sub: 'Sawan Somwar 2026' },
          { key: 'satyanarayana' as const, emoji: '📖', label: 'सत्यनारायण पूजा', sub: 'Satyanarayana Puja 2026' },
          { key: 'purnima' as const, emoji: '🌕', label: 'पूर्णिमा व्रत', sub: 'Purnima Dates 2026' },
          { key: 'navagraha' as const, emoji: '🪐', label: 'नवग्रह सप्तवार व्रत', sub: 'Navagraha Weekdays 2026' }
        ]).map(tab => ("""

new_tabs = """      {/* SECTION TABS */}
      <div style={{ display: 'flex', gap: '4px', padding: '4px', background: 'var(--bg-primary)', borderRadius: '12px', marginBottom: '28px', width: 'fit-content', flexWrap: 'wrap' }}>
        {([
          { key: 'deities-saptavara' as const, emoji: '🕉️', label: 'देवी-देवता सप्तवार व्रत', sub: 'Deities Weekdays Fasting' },
          { key: 'shivaratri' as const, emoji: '🌙', label: 'मासिक शिवरात्रि', sub: 'Masik Shivaratri 2026' },
          { key: 'sawan' as const, emoji: '💧', label: 'सावन सोमवार', sub: 'Sawan Somwar 2026' },
          { key: 'satyanarayana' as const, emoji: '📖', label: 'सत्यनारायण पूजा', sub: 'Satyanarayana Puja 2026' },
          { key: 'purnima' as const, emoji: '🌕', label: 'पूर्णिमा व्रत', sub: 'Purnima Dates 2026' },
          { key: 'navagraha' as const, emoji: '🪐', label: 'नवग्रह सप्तवार व्रत', sub: 'Navagraha Weekdays 2026' }
        ]).map(tab => ("""

if old_tabs in content:
    content = content.replace(old_tabs, new_tabs)
    print("Tabs updated successfully!")

# 6. Insert DEITIES SAPTAVARA SECTION before MASIK SHIVARATRI SECTION
masik_marker = """      {/* ═══ MASIK SHIVARATRI SECTION ═══ */}"""

deities_section_code = """      {/* ═══ DEITIES SAPTAVARA VRAT SECTION (MATCHING IMAGE 1) ═══ */}
      {activeSection === 'deities-saptavara' && (
        <div>
          {/* Authentic Intro Text Box as shown in User Screenshot Image 1 */}
          <div style={{
            background: 'linear-gradient(135deg, rgba(238, 216, 161, 0.28) 0%, rgba(245, 202, 140, 0.16) 100%)',
            border: '1px solid rgba(216, 188, 126, 0.5)',
            borderRadius: '14px',
            padding: '22px 26px',
            marginBottom: '26px',
            boxShadow: '0 4px 16px rgba(0,0,0,0.06)'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', flexWrap: 'wrap', gap: '8px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '18px' }}>📜</span>
                <span style={{ fontSize: '13px', fontWeight: 800, color: 'var(--gold-accent)', textTransform: 'uppercase', letterSpacing: '0.6px' }}>
                  सप्तवार व्रत माहात्म्य एवं विधान (Vrat Ratnakara)
                </span>
              </div>
              <div style={{ display: 'flex', gap: '6px', background: 'var(--bg-primary)', padding: '3px', borderRadius: '8px', border: '1px solid var(--border-subtle)' }}>
                <button
                  type="button"
                  onClick={() => setIntroLang('en')}
                  style={{
                    padding: '4px 12px', borderRadius: '6px', fontSize: '11px', fontWeight: 700, cursor: 'pointer', border: 'none',
                    background: introLang === 'en' ? 'var(--gold-accent)' : 'transparent',
                    color: introLang === 'en' ? '#000' : 'var(--text-muted)'
                  }}
                >
                  English
                </button>
                <button
                  type="button"
                  onClick={() => setIntroLang('hi')}
                  style={{
                    padding: '4px 12px', borderRadius: '6px', fontSize: '11px', fontWeight: 700, cursor: 'pointer', border: 'none',
                    background: introLang === 'hi' ? 'var(--gold-accent)' : 'transparent',
                    color: introLang === 'hi' ? '#000' : 'var(--text-muted)'
                  }}
                >
                  हिन्दी
                </button>
              </div>
            </div>

            <p style={{ margin: 0, fontSize: '14.5px', color: 'var(--text-primary)', lineHeight: '1.85' }}>
              {introLang === 'en' ? (
                <>
                  Different types of <strong style={{ color: 'var(--gold-accent)' }}>Vrat and Upavasa</strong> are prevalent in Hinduism. Devotees observe these fasts for the fulfillment of their specific wishes. <strong style={{ color: 'var(--gold-accent)' }}>Saptavara Vrat</strong> dedicated to various <strong style={{ color: 'var(--gold-accent)' }}>Gods and Goddesses</strong>, are very popular among the people. Saptavara Vrat means fasts observed according to the weekdays such as Ravivara Vrat, Somavara Vrat, Mangalavara Vrat etc. According to the <strong style={{ color: 'var(--gold-accent)' }}>Vrat Ratnakara</strong>, these weekday fasts should ideally be started in the months of <strong style={{ color: 'var(--gold-accent)' }}>Vaishakha</strong>, <strong style={{ color: 'var(--gold-accent)' }}>Margashirsha</strong> and <strong style={{ color: 'var(--gold-accent)' }}>Magha</strong>. By observing these fasts, one not only attains spiritual benefits but also experiences physical and mental well-being. Here, the weekday fasts dedicated to the Gods and Goddesses are described, including their fasting food, Puja Vidhi, and the ritual of conclusion, i.e. Udyapana Vidhi.
                </>
              ) : (
                <>
                  हिन्दु धर्म में विभिन्न प्रकार के <strong style={{ color: 'var(--gold-accent)' }}>व्रत एवं उपवास</strong> प्रचलित हैं। भक्तगण अपने विशेष मनोरथों की सिद्धि हेतु इन व्रतों का पालन करते हैं। जन साधारण में विभिन्न <strong style={{ color: 'var(--gold-accent)' }}>देवी-देवताओं</strong> को समर्पित सप्तवार व्रत अत्यन्त लोकप्रिय हैं। सप्तवार व्रत अर्थात् सप्ताह के दिनों के अनुसार किये जाने वाले व्रत जैसे रविवार व्रत, सोमवार व्रत, मङ्गलवार व्रत आदि। <strong style={{ color: 'var(--gold-accent)' }}>व्रत रत्नाकर</strong> के अनुसार, वार के व्रत का आरम्भ मुख्यतः <strong style={{ color: 'var(--gold-accent)' }}>वैशाख</strong>, <strong style={{ color: 'var(--gold-accent)' }}>मार्गशीर्ष</strong> तथा <strong style={{ color: 'var(--gold-accent)' }}>माघ</strong> माह में किया जाना चाहिये। इन व्रतों को करने से व्यक्ति को आध्यात्मिक लाभ तो होता ही है साथ ही शारीरिक एवं मानसिक लाभ की अनुभूति भी होती है। यहाँ देवी-देवताओं को समर्पित सप्ताह के सभी दिनों के व्रत, उनका आहार-विचार, पूजन विधि एवं उद्यापन विधि का वर्णन किया गया है।
                </>
              )}
            </p>
          </div>

          {/* Drik Panchang Signature Centered Title as shown in Screenshot */}
          <div style={{ textAlign: 'center', marginBottom: '24px' }}>
            <h2 style={{
              margin: '0 0 6px',
              fontSize: '24px',
              fontWeight: 800,
              color: '#9F2800',
              fontFamily: 'serif',
              letterSpacing: '0.2px'
            }}>
              Deities Weekdays Fasting List
            </h2>
            <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>
              देवी-देवता सप्तवार व्रत संग्रह — Click on any card below to view full Vidhi, Diet &amp; Udyapana
            </div>
          </div>

          {/* 3x3 Cards Grid - Exactly Matching Screenshot 1 */}
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(290px, 1fr))',
            gap: '18px',
            marginBottom: '36px'
          }}>
            {DEITIES_SAPTAVARA_VRATS.map((vrat) => {
              const isToday = vrat.dayNum === todayDayNumber;
              return (
                <div
                  key={vrat.id}
                  onClick={() => {
                    setSelectedDeityId(vrat.id);
                    setDeityDetailTab('overview');
                  }}
                  style={{
                    borderRadius: '10px',
                    overflow: 'hidden',
                    background: '#EED8A1',
                    border: isToday ? '2px solid #b91c1c' : '1px solid #D8BC7E',
                    boxShadow: isToday ? '0 6px 20px rgba(185,28,28,0.25)' : '0 3px 12px rgba(0,0,0,0.08)',
                    cursor: 'pointer',
                    transition: 'all 0.25s cubic-bezier(0.4, 0, 0.2, 1)',
                    display: 'flex',
                    flexDirection: 'column'
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.transform = 'translateY(-4px)';
                    e.currentTarget.style.boxShadow = '0 10px 24px rgba(216, 188, 126, 0.55)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.transform = 'translateY(0)';
                    e.currentTarget.style.boxShadow = isToday ? '0 6px 20px rgba(185,28,28,0.25)' : '0 3px 12px rgba(0,0,0,0.08)';
                  }}
                >
                  {/* 3:2 Ratio Image Container */}
                  <div style={{
                    position: 'relative',
                    width: '100%',
                    paddingTop: '66.66%',
                    overflow: 'hidden',
                    background: '#2d1b0e'
                  }}>
                    <img
                      src={vrat.image}
                      alt={vrat.nameEn}
                      onError={(e) => {
                        (e.target as HTMLImageElement).src = vrat.fallbackImage;
                      }}
                      style={{
                        position: 'absolute',
                        inset: 0,
                        width: '100%',
                        height: '100%',
                        objectFit: 'cover',
                        transition: 'transform 0.4s ease'
                      }}
                    />

                    {/* Day Pill on top-left */}
                    <div style={{
                      position: 'absolute',
                      top: '8px',
                      left: '8px',
                      padding: '3px 8px',
                      borderRadius: '12px',
                      background: 'rgba(0,0,0,0.65)',
                      backdropFilter: 'blur(4px)',
                      color: '#fff',
                      fontSize: '10.5px',
                      fontWeight: 700,
                      border: '1px solid rgba(255,255,255,0.25)',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '4px'
                    }}>
                      <span>📅</span> {vrat.dayHi} • {vrat.dayEn}
                    </div>

                    {/* Today Badge on top-right */}
                    {isToday && (
                      <div style={{
                        position: 'absolute',
                        top: '8px',
                        right: '8px',
                        padding: '3px 9px',
                        borderRadius: '12px',
                        background: 'linear-gradient(135deg, #b91c1c, #dc2626)',
                        color: '#fff',
                        fontSize: '10.5px',
                        fontWeight: 800,
                        boxShadow: '0 2px 8px rgba(185,28,28,0.45)',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '3px'
                      }}>
                        <span>🔴</span> TODAY
                      </div>
                    )}
                  </div>

                  {/* Title Bar Styled Exactly Like Screenshot */}
                  <div style={{
                    padding: '13px 10px',
                    textAlign: 'center',
                    background: '#EED8A1',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    gap: '2px'
                  }}>
                    <div style={{
                      fontFamily: 'serif',
                      fontSize: '15.5px',
                      fontWeight: 700,
                      color: '#3B1E08',
                      letterSpacing: '0.2px',
                      lineHeight: '1.25'
                    }}>
                      {vrat.nameEn}
                    </div>
                    <div style={{
                      fontSize: '11.5px',
                      fontWeight: 600,
                      color: '#6e4018',
                      opacity: 0.88
                    }}>
                      {vrat.nameHi}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Full Interactive Modal / Drawer for Selected Deity Vrat */}
          {selectedDeity && (
            <div
              style={{
                position: 'fixed',
                inset: 0,
                background: 'rgba(0,0,0,0.75)',
                backdropFilter: 'blur(6px)',
                zIndex: 9999,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                padding: '20px'
              }}
              onClick={(e) => {
                if (e.target === e.currentTarget) setSelectedDeityId(null);
              }}
            >
              <div
                style={{
                  background: 'var(--bg-surface)',
                  border: '2px solid rgba(226,176,74,0.4)',
                  borderRadius: '20px',
                  maxWidth: '860px',
                  width: '100%',
                  maxHeight: '90vh',
                  overflowY: 'auto',
                  boxShadow: '0 20px 60px rgba(0,0,0,0.4)',
                  position: 'relative',
                  display: 'flex',
                  flexDirection: 'column'
                }}
              >
                {/* Modal Header Banner */}
                <div style={{
                  position: 'relative',
                  height: '210px',
                  overflow: 'hidden',
                  background: '#22150a',
                  flexShrink: 0
                }}>
                  <img
                    src={selectedDeity.image}
                    alt={selectedDeity.nameEn}
                    onError={(e) => {
                      (e.target as HTMLImageElement).src = selectedDeity.fallbackImage;
                    }}
                    style={{
                      width: '100%',
                      height: '100%',
                      objectFit: 'cover',
                      filter: 'brightness(0.55)'
                    }}
                  />
                  <div style={{
                    position: 'absolute',
                    inset: 0,
                    background: 'linear-gradient(to top, rgba(0,0,0,0.92) 0%, rgba(0,0,0,0.4) 60%, rgba(0,0,0,0.2) 100%)'
                  }} />

                  {/* Close button */}
                  <button
                    type="button"
                    onClick={() => setSelectedDeityId(null)}
                    style={{
                      position: 'absolute',
                      top: '16px',
                      right: '16px',
                      width: '36px',
                      height: '36px',
                      borderRadius: '50%',
                      background: 'rgba(0,0,0,0.6)',
                      border: '1px solid rgba(255,255,255,0.2)',
                      color: '#fff',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      zIndex: 10
                    }}
                  >
                    <X size={18} />
                  </button>

                  {/* Title & info in header */}
                  <div style={{
                    position: 'absolute',
                    bottom: '16px',
                    left: '20px',
                    right: '20px',
                    display: 'flex',
                    alignItems: 'flex-end',
                    justifyContent: 'space-between',
                    flexWrap: 'wrap',
                    gap: '12px'
                  }}>
                    <div>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
                        <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'var(--gold-accent)', color: '#000', fontSize: '11px', fontWeight: 800 }}>
                          {selectedDeity.dayHi} • {selectedDeity.dayEn}
                        </span>
                        <span style={{ fontSize: '12px', color: 'rgba(255,255,255,0.85)', fontWeight: 600 }}>
                          शासक ग्रह: {selectedDeity.planetHi} ({selectedDeity.planetEn})
                        </span>
                      </div>
                      <h3 style={{ margin: '0 0 2px', fontSize: '24px', fontWeight: 800, color: '#fff', fontFamily: 'serif' }}>
                        {selectedDeity.nameHi} ({selectedDeity.nameEn})
                      </h3>
                      <div style={{ fontSize: '13px', color: 'var(--gold-accent)', fontWeight: 600 }}>
                        इष्ट देवता: {selectedDeity.deityHi} ({selectedDeity.deityEn})
                      </div>
                    </div>

                    {/* Language Switcher */}
                    <div style={{ display: 'flex', gap: '4px', background: 'rgba(0,0,0,0.7)', padding: '3px', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.2)' }}>
                      <button
                        type="button"
                        onClick={() => setDeityLang('hi')}
                        style={{
                          padding: '4px 12px', borderRadius: '6px', fontSize: '11px', fontWeight: 700, cursor: 'pointer', border: 'none',
                          background: deityLang === 'hi' ? 'var(--gold-accent)' : 'transparent',
                          color: deityLang === 'hi' ? '#000' : '#fff'
                        }}
                      >
                        हिन्दी
                      </button>
                      <button
                        type="button"
                        onClick={() => setDeityLang('en')}
                        style={{
                          padding: '4px 12px', borderRadius: '6px', fontSize: '11px', fontWeight: 700, cursor: 'pointer', border: 'none',
                          background: deityLang === 'en' ? 'var(--gold-accent)' : 'transparent',
                          color: deityLang === 'en' ? '#000' : '#fff'
                        }}
                      >
                        English
                      </button>
                    </div>
                  </div>
                </div>

                {/* Quick Info Grid */}
                <div style={{
                  padding: '14px 20px',
                  background: 'var(--bg-primary)',
                  borderBottom: '1px solid var(--border-subtle)',
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
                  gap: '10px'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <Calendar size={15} color="var(--gold-accent)" />
                    <div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 600 }}>आरम्भ मुहूर्त (Best Months)</div>
                      <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-primary)' }}>वैशाख, मार्गशीर्ष, माघ</div>
                    </div>
                  </div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <Clock size={15} color="#38bdf8" />
                    <div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 600 }}>व्रत अवधि (Duration)</div>
                      <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-primary)' }}>
                        {deityLang === 'hi' ? selectedDeity.durationHi : selectedDeity.durationEn}
                      </div>
                    </div>
                  </div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <Sparkles size={15} color="#ec4899" />
                    <div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 600 }}>शुभ रंग (Sacred Color)</div>
                      <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-primary)' }}>{selectedDeity.color}</div>
                    </div>
                  </div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <Shield size={15} color="#22c55e" />
                    <div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)', fontWeight: 600 }}>प्रमाणित ग्रन्थ (Scripture)</div>
                      <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-primary)' }}>व्रत रत्नाकर, पुराण</div>
                    </div>
                  </div>
                </div>

                {/* 4 Detail Tabs */}
                <div style={{
                  display: 'flex',
                  borderBottom: '1px solid var(--border-subtle)',
                  background: 'var(--bg-surface)',
                  overflowX: 'auto'
                }}>
                  {[
                    { key: 'overview' as const, labelEn: 'Overview & Significance', labelHi: 'परिचय एवं माहात्म्य', icon: '📖' },
                    { key: 'food' as const, labelEn: 'Fasting Food & Diet', labelHi: 'आहार-विचार व नियम', icon: '🍎' },
                    { key: 'vidhi' as const, labelEn: 'Puja Vidhi & Mantras', labelHi: 'सङ्क्षिप्त विधि व मन्त्र', icon: '🪔' },
                    { key: 'udyapan' as const, labelEn: 'Udyapana & Katha', labelHi: 'उद्यापन विधि व कथा', icon: '🕉️' }
                  ].map(tab => {
                    const isActive = deityDetailTab === tab.key;
                    return (
                      <button
                        key={tab.key}
                        type="button"
                        onClick={() => setDeityDetailTab(tab.key)}
                        style={{
                          flex: 1,
                          minWidth: '150px',
                          padding: '12px 14px',
                          border: 'none',
                          borderBottom: isActive ? '3px solid var(--gold-accent)' : '3px solid transparent',
                          background: isActive ? 'rgba(226,176,74,0.08)' : 'transparent',
                          color: isActive ? 'var(--gold-accent)' : 'var(--text-muted)',
                          fontSize: '13px',
                          fontWeight: isActive ? 800 : 500,
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          gap: '6px',
                          transition: 'all 0.2s ease'
                        }}
                      >
                        <span>{tab.icon}</span>
                        <span>{deityLang === 'hi' ? tab.labelHi : tab.labelEn}</span>
                      </button>
                    );
                  })}
                </div>

                {/* Tab Content Body */}
                <div style={{ padding: '22px 24px', flex: 1, overflowY: 'auto' }}>
                  {/* TAB 1: OVERVIEW */}
                  {deityDetailTab === 'overview' && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                      <div style={{
                        padding: '16px 18px',
                        borderRadius: '12px',
                        background: 'rgba(226,176,74,0.07)',
                        border: '1px solid rgba(226,176,74,0.25)',
                        lineHeight: '1.8',
                        fontSize: '14px',
                        color: 'var(--text-primary)'
                      }}>
                        <p style={{ margin: '0 0 12px', fontWeight: 600 }}>
                          {deityLang === 'hi' ? selectedDeity.overviewHi : selectedDeity.overviewEn}
                        </p>
                      </div>

                      {/* Benefits box */}
                      <div style={{
                        padding: '16px 18px',
                        borderRadius: '12px',
                        background: 'rgba(34,197,94,0.08)',
                        border: '1px solid rgba(34,197,94,0.3)'
                      }}>
                        <div style={{ fontSize: '13px', fontWeight: 800, color: '#22c55e', marginBottom: '6px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                          <Sparkles size={16} /> {deityLang === 'hi' ? 'विशेष फल एवं आध्यात्मिक लाभ' : 'Special Fruits & Spiritual Benefits'}
                        </div>
                        <p style={{ margin: 0, fontSize: '13.5px', color: 'var(--text-primary)', lineHeight: '1.7' }}>
                          {deityLang === 'hi' ? selectedDeity.benefitsHi : selectedDeity.benefitsEn}
                        </p>
                      </div>

                      {/* Canonical Source Note */}
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)', lineHeight: '1.6' }}>
                        📌 <strong>सन्दर्भ ग्रन्थ:</strong> व्रत रत्नाकर, स्कन्द पुराण, भविष्य पुराण तथा शिवरहस्य पुराण।
                      </div>
                    </div>
                  )}

                  {/* TAB 2: FASTING FOOD */}
                  {deityDetailTab === 'food' && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                      <div style={{
                        padding: '16px 18px',
                        borderRadius: '12px',
                        background: 'rgba(234,179,8,0.08)',
                        border: '1px solid rgba(234,179,8,0.28)'
                      }}>
                        <div style={{ fontSize: '14px', fontWeight: 800, color: 'var(--gold-accent)', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                          <Utensils size={16} /> {deityLang === 'hi' ? 'आहार-विचार एवं फलाहार नियम' : 'Dietary Guidelines & Phalahara'}
                        </div>
                        <p style={{ margin: 0, fontSize: '14px', color: 'var(--text-primary)', lineHeight: '1.8' }}>
                          {deityLang === 'hi' ? selectedDeity.fastingFoodHi : selectedDeity.fastingFoodEn}
                        </p>
                      </div>

                      {/* Do's and Don'ts checklist */}
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '12px' }}>
                        <div style={{ padding: '14px', borderRadius: '10px', background: 'rgba(34,197,94,0.08)', border: '1px solid rgba(34,197,94,0.25)' }}>
                          <div style={{ fontSize: '12px', fontWeight: 800, color: '#22c55e', marginBottom: '6px' }}>
                            ✓ अनुमन्य आहार (Allowed Food)
                          </div>
                          <ul style={{ margin: 0, paddingLeft: '18px', fontSize: '12.5px', color: 'var(--text-primary)', lineHeight: '1.6' }}>
                            <li>ताजे मौसमी फल, गाय का शुद्ध दूध व जल</li>
                            <li>मखाना, मूंगफली, सिंघाड़े का आटा, साबूदाना</li>
                            <li>संध्या आरती के बाद एकभुक्त सात्विक भोजन</li>
                          </ul>
                        </div>
                        <div style={{ padding: '14px', borderRadius: '10px', background: 'rgba(239,68,68,0.08)', border: '1px solid rgba(239,68,68,0.25)' }}>
                          <div style={{ fontSize: '12px', fontWeight: 800, color: '#ef4444', marginBottom: '6px' }}>
                            ✕ वर्जित एवं निषिद्ध (Prohibited)
                          </div>
                          <ul style={{ margin: 0, paddingLeft: '18px', fontSize: '12.5px', color: 'var(--text-primary)', lineHeight: '1.6' }}>
                            <li>मांसाहार, मद्यपान, धूम्रपान व तामसिक भोजन</li>
                            <li>प्याज, लहसुन तथा अत्यधिक व मिथ्या भाषण</li>
                            {selectedDeity.id.includes('santoshi') && (
                              <li style={{ color: '#ef4444', fontWeight: 700 }}>खटाई, नींबू, इमली व खट्टे फल (पूर्ण वर्जित!)</li>
                            )}
                          </ul>
                        </div>
                      </div>
                    </div>
                  )}

                  {/* TAB 3: PUJA VIDHI & MANTRAS */}
                  {deityDetailTab === 'vidhi' && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                      {/* Sacred Mantra Highlight Card */}
                      <div style={{
                        padding: '16px 20px',
                        borderRadius: '12px',
                        background: 'linear-gradient(135deg, rgba(226,176,74,0.15) 0%, rgba(245,158,11,0.08) 100%)',
                        border: '1px solid rgba(226,176,74,0.4)',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '8px'
                      }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                          <div style={{ fontSize: '11px', fontWeight: 800, color: 'var(--gold-accent)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                            🕉️ मुख्य जप मन्त्र (Sacred Mantra)
                          </div>
                          <button
                            type="button"
                            onClick={() => {
                              navigator.clipboard.writeText(selectedDeity.mantra);
                              setCopiedMantra(true);
                              setTimeout(() => setCopiedMantra(false), 2000);
                            }}
                            style={{
                              display: 'flex',
                              alignItems: 'center',
                              gap: '5px',
                              padding: '4px 10px',
                              borderRadius: '6px',
                              background: 'var(--bg-primary)',
                              border: '1px solid var(--border-subtle)',
                              color: copiedMantra ? '#22c55e' : 'var(--text-muted)',
                              fontSize: '11px',
                              cursor: 'pointer',
                              fontWeight: 600
                            }}
                          >
                            {copiedMantra ? <Check size={12} /> : <Copy size={12} />}
                            {copiedMantra ? 'Copied!' : 'Copy'}
                          </button>
                        </div>
                        <div style={{
                          fontSize: '17px',
                          fontWeight: 800,
                          color: 'var(--gold-accent)',
                          fontFamily: 'serif',
                          lineHeight: '1.6',
                          letterSpacing: '0.3px'
                        }}>
                          {selectedDeity.mantra}
                        </div>
                        <div style={{ fontSize: '11.5px', color: 'var(--text-muted)' }}>
                          प्रतिदिन अथवा व्रत दिवस पर 108 बार (1 माला) श्रद्धापूर्वक जप करें।
                        </div>
                      </div>

                      {/* Step-by-Step Vidhi */}
                      <div style={{
                        padding: '16px 18px',
                        borderRadius: '12px',
                        background: 'var(--bg-primary)',
                        border: '1px solid var(--border-subtle)'
                      }}>
                        <div style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text-primary)', marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                          <span>🪔</span> {deityLang === 'hi' ? 'सङ्क्षिप्त पूजन विधि' : 'Step-by-Step Puja Procedure'}
                        </div>
                        <p style={{ margin: 0, fontSize: '14px', color: 'var(--text-primary)', lineHeight: '1.85' }}>
                          {deityLang === 'hi' ? selectedDeity.vidhiHi : selectedDeity.vidhiEn}
                        </p>
                      </div>
                    </div>
                  )}

                  {/* TAB 4: UDYAPANA & KATHA */}
                  {deityDetailTab === 'udyapan' && (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                      {/* Udyapana Card */}
                      <div style={{
                        padding: '16px 18px',
                        borderRadius: '12px',
                        background: 'rgba(251,191,36,0.08)',
                        border: '1px solid rgba(251,191,36,0.28)'
                      }}>
                        <div style={{ fontSize: '14px', fontWeight: 800, color: '#fbbf24', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                          <span>📜</span> {deityLang === 'hi' ? 'उद्यापन विधि एवं हवन विधान' : 'Udyapana Vidhi & Havan Ritual'}
                        </div>
                        <p style={{ margin: 0, fontSize: '14px', color: 'var(--text-primary)', lineHeight: '1.85' }}>
                          {deityLang === 'hi' ? selectedDeity.udyapanHi : selectedDeity.udyapanEn}
                        </p>
                      </div>

                      {/* Vrat Katha Summary */}
                      {selectedDeity.kathaHi && (
                        <div style={{
                          padding: '16px 18px',
                          borderRadius: '12px',
                          background: 'var(--bg-primary)',
                          border: '1px solid var(--border-subtle)'
                        }}>
                          <div style={{ fontSize: '13px', fontWeight: 800, color: 'var(--text-primary)', marginBottom: '6px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                            <span>📖</span> {deityLang === 'hi' ? 'व्रत कथा सार' : 'Vrat Katha Summary'}
                          </div>
                          <p style={{ margin: 0, fontSize: '13.5px', color: 'var(--text-muted)', lineHeight: '1.75' }}>
                            {deityLang === 'hi' ? selectedDeity.kathaHi : selectedDeity.kathaEn}
                          </p>
                        </div>
                      )}
                    </div>
                  )}
                </div>

                {/* Modal Footer with External Link */}
                <div style={{
                  padding: '14px 20px',
                  background: 'var(--bg-primary)',
                  borderTop: '1px solid var(--border-subtle)',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  flexWrap: 'wrap',
                  gap: '8px'
                }}>
                  <a
                    href={selectedDeity.url}
                    target="_blank"
                    rel="noreferrer"
                    style={{
                      display: 'inline-flex',
                      alignItems: 'center',
                      gap: '6px',
                      fontSize: '12px',
                      color: 'var(--gold-accent)',
                      textDecoration: 'none',
                      fontWeight: 600
                    }}
                  >
                    <ExternalLink size={13} /> View full details on DrikPanchang.com
                  </a>
                  <button
                    type="button"
                    onClick={() => setSelectedDeityId(null)}
                    style={{
                      padding: '6px 16px',
                      borderRadius: '8px',
                      background: 'var(--gold-accent)',
                      color: '#000',
                      fontWeight: 700,
                      border: 'none',
                      cursor: 'pointer',
                      fontSize: '12px'
                    }}
                  >
                    Close
                  </button>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

"""

if masik_marker in content:
    content = content.replace(masik_marker, deities_section_code + "\n" + masik_marker)
    print("Deities section inserted successfully!")
else:
    print("Could not find masik_marker!")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("VratUpvasView.tsx successfully updated!")
