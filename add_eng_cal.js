const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Add English Calendar init function and bottom nav entry
const engCalCode = `

// ══════════════════════════════════════════
//   ENGLISH CALENDAR  (Google Calendar style)
// ══════════════════════════════════════════

// 2026 Indian public holidays + Hindu festivals (English names)
const ENG_CAL_EVENTS = {
  '2026-01-14': { name: 'Makar Sankranti', hindi: 'मकर संक्रांति', type: 'festival' },
  '2026-01-26': { name: 'Republic Day', hindi: 'गणतंत्र दिवस', type: 'holiday' },
  '2026-02-26': { name: 'Maha Shivaratri', hindi: 'महा शिवरात्रि', type: 'festival' },
  '2026-03-02': { name: 'Holika Dahan', hindi: 'होलिका दहन', type: 'festival' },
  '2026-03-03': { name: 'Holi', hindi: 'होली', type: 'holiday' },
  '2026-03-26': { name: 'Rama Navami', hindi: 'राम नवमी', type: 'festival' },
  '2026-04-14': { name: 'Baisakhi / Dr. Ambedkar Jayanti', hindi: 'बैसाखी / अम्बेडकर जयंती', type: 'holiday' },
  '2026-04-18': { name: 'Good Friday', hindi: 'गुड फ्राइडे', type: 'holiday' },
  '2026-05-07': { name: 'Buddha Purnima', hindi: 'बुद्ध पूर्णिमा', type: 'holiday' },
  '2026-06-29': { name: 'Rath Yatra', hindi: 'रथ यात्रा', type: 'festival' },
  '2026-07-29': { name: 'Guru Purnima', hindi: 'गुरु पूर्णिमा', type: 'festival' },
  '2026-08-15': { name: 'Independence Day / Janmashtami', hindi: 'स्वतंत्रता दिवस / जन्माष्टमी', type: 'holiday' },
  '2026-08-17': { name: 'Janmashtami (Smarta)', hindi: 'जन्माष्टमी (स्मार्त)', type: 'festival' },
  '2026-08-26': { name: 'Onam', hindi: 'ओणम', type: 'festival' },
  '2026-08-28': { name: 'Raksha Bandhan', hindi: 'रक्षा बंधन', type: 'holiday' },
  '2026-09-14': { name: 'Ganesha Chaturthi', hindi: 'गणेश चतुर्थी', type: 'holiday' },
  '2026-10-02': { name: 'Gandhi Jayanti / Navratri begins', hindi: 'गांधी जयंती / नवरात्रि', type: 'holiday' },
  '2026-10-20': { name: 'Dussehra (Vijayadashami)', hindi: 'दशहरा', type: 'holiday' },
  '2026-10-28': { name: 'Maharishi Valmiki Jayanti', hindi: 'वाल्मीकि जयंती', type: 'holiday' },
  '2026-11-01': { name: 'Ahoi Ashtami', hindi: 'अहोई अष्टमी', type: 'festival' },
  '2026-11-06': { name: 'Dhanteras', hindi: 'धनतेरस', type: 'festival' },
  '2026-11-07': { name: 'Choti Diwali / Narak Chaturdashi', hindi: 'छोटी दीपावली', type: 'festival' },
  '2026-11-08': { name: 'Diwali (Deepavali)', hindi: 'दीपावली', type: 'holiday' },
  '2026-11-09': { name: 'Govardhan Puja', hindi: 'गोवर्धन पूजा', type: 'festival' },
  '2026-11-10': { name: 'Bhai Dooj', hindi: 'भाई दूज', type: 'festival' },
  '2026-11-15': { name: 'Guru Nanak Jayanti', hindi: 'गुरु नानक जयंती', type: 'holiday' },
  '2026-12-25': { name: 'Christmas', hindi: 'क्रिसमस', type: 'holiday' },
};

function initEngCalendar() {
  const today = new Date();
  let engYear = 2026;
  let engMonth = today.getMonth();
  const MONTHS_EN = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  const DAYS_EN = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];

  function renderEngCal(year, month) {
    const grid = document.getElementById('eng-cal-grid');
    const title = document.getElementById('eng-cal-title');
    if(!grid) return;
    title.textContent = MONTHS_EN[month] + ' ' + year;
    grid.innerHTML = '';

    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    // Empty cells
    for(let i = 0; i < firstDay; i++) {
      const e = document.createElement('div');
      e.style.cssText = 'min-height:56px; border-right:1px solid #f1f5f9; border-bottom:1px solid #f1f5f9; background:#fafafa;';
      grid.appendChild(e);
    }

    for(let d = 1; d <= daysInMonth; d++) {
      const dateKey = year + '-' + String(month+1).padStart(2,'0') + '-' + String(d).padStart(2,'0');
      const ev = ENG_CAL_EVENTS[dateKey];
      const dow = new Date(year, month, d).getDay();
      const isToday = (d === today.getDate() && month === today.getMonth() && year === today.getFullYear());
      const isSun = dow === 0;
      const isHoliday = ev && ev.type === 'holiday';
      const isFestival = ev && ev.type === 'festival';

      const cell = document.createElement('div');
      let bg = '#fff';
      if(isSun) bg = '#fef2f2';
      if(isFestival) bg = 'hsl(44,80%,98%)';
      if(isHoliday) bg = '#f0fdf4';
      cell.style.cssText = \`min-height:56px; border-right:1px solid #f1f5f9; border-bottom:1px solid #f1f5f9; background:\${bg}; cursor:pointer; padding:4px 3px; display:flex; flex-direction:column; align-items:center; position:relative; transition:background 0.12s;\`;
      cell.addEventListener('click', () => showEngEvent(d, dow, ev));

      // Date number
      const num = document.createElement('div');
      num.style.cssText = \`width:26px; height:26px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:0.78rem; font-weight:\${isToday ? 500 : 400}; color:\${isSun ? '#d93025' : '#202124'}; background:\${isToday ? '#1a73e8' : 'transparent'}; color:\${isToday ? '#fff' : isSun ? '#d93025' : '#202124'}; margin:0 auto;\`;
      num.textContent = d;
      cell.appendChild(num);

      if(ev) {
        const chip = document.createElement('div');
        chip.style.cssText = \`font-size:0.5rem; font-weight:600; width:100%; text-align:center; border-radius:2px; padding:1px 2px; line-height:1.4; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; margin-top:2px; background:\${isHoliday ? '#bbf7d0' : 'hsl(33,100%,88%)'}; color:\${isHoliday ? '#14532d' : 'hsl(22,80%,28%)'};\`;
        chip.textContent = ev.name.split(' ')[0];
        chip.title = ev.name;
        cell.appendChild(chip);
      }
      grid.appendChild(cell);
    }
    // Render upcoming
    renderEngUpcoming(year, month);
  }

  function showEngEvent(d, dow, ev) {
    const card = document.getElementById('eng-cal-event');
    const dayEl = document.getElementById('eng-event-day');
    const dowEl = document.getElementById('eng-event-dow');
    const nameEl = document.getElementById('eng-event-name');
    const hindiEl = document.getElementById('eng-event-hindi');
    dayEl.textContent = d;
    dowEl.textContent = ['SUN','MON','TUE','WED','THU','FRI','SAT'][dow];
    if(ev) {
      nameEl.textContent = ev.name;
      hindiEl.textContent = ev.hindi;
      card.classList.remove('hidden');
    } else {
      nameEl.textContent = 'No events this day';
      hindiEl.textContent = 'इस दिन कोई त्योहार नहीं';
      card.classList.remove('hidden');
    }
  }

  function renderEngUpcoming(year, month) {
    const container = document.getElementById('eng-upcoming');
    if(!container) return;
    const MONTHS_EN2 = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    const monthKey = String(month+1).padStart(2,'0');
    const events = Object.entries(ENG_CAL_EVENTS)
      .filter(([k]) => k.startsWith(year + '-' + monthKey))
      .sort(([a],[b]) => a.localeCompare(b));

    if(!events.length) { container.innerHTML = '<div style="text-align:center; color:#70757a; padding:1.5rem 0; font-size:0.85rem;">No events this month</div>'; return; }

    const heading = \`<div style="font-size:0.8rem; font-weight:700; color:#202124; margin:0.8rem 0 0.5rem; text-transform:uppercase; letter-spacing:0.05em;">Events this month</div>\`;
    const items = events.map(([dateKey, ev]) => {
      const d = parseInt(dateKey.split('-')[2]);
      const dt = new Date(year, month, d);
      const dow = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'][dt.getDay()];
      const isHol = ev.type === 'holiday';
      return \`<div style="display:flex; align-items:center; gap:0.7rem; padding:0.6rem 0.8rem; background:#fff; border-radius:8px; border:1px solid #e2e8f0; margin-bottom:0.4rem; border-left:3px solid \${isHol ? '#22c55e' : '#f97316'};">
        <div style="min-width:36px; text-align:center;">
          <div style="font-size:1rem; font-weight:800; color:\${isHol ? '#15803d' : '#c2410c'}; line-height:1;">\${d}</div>
          <div style="font-size:0.6rem; font-weight:600; color:#70757a; text-transform:uppercase;">\${dow}</div>
        </div>
        <div>
          <div style="font-size:0.85rem; font-weight:700; color:#202124;">\${ev.name}</div>
          <div style="font-size:0.72rem; color:#70757a;">\${ev.hindi} · \${isHol ? '🟢 Public Holiday' : '🔶 Festival'}</div>
        </div>
      </div>\`;
    }).join('');
    container.innerHTML = heading + items;
  }

  // Nav buttons
  document.getElementById('eng-cal-prev')?.addEventListener('click', () => {
    engMonth = (engMonth - 1 + 12) % 12;
    if(engMonth === 11) engYear--;
    renderEngCal(engYear, engMonth);
  });
  document.getElementById('eng-cal-next')?.addEventListener('click', () => {
    engMonth = (engMonth + 1) % 12;
    if(engMonth === 0) engYear++;
    renderEngCal(engYear, engMonth);
  });

  renderEngCal(engYear, engMonth);
}
`;

// Add to end of app.js before last line or add call in DOMContentLoaded
code = code.replace(/^\/\/ v\d+\n/, '');
code = '// v' + Date.now() + '\n' + code;

// Add the function before the closing of the file
code += engCalCode;

// Also wire the English Calendar button in the bottom nav
// Find the bottom nav calendar button and add English calendar nav option
code = code.replace(
  "case 'page-english-calendar':",
  "case 'page-english-calendar-old':"
);

// Add initEngCalendar() call after initCalendar
if(code.includes('initCalendar()')) {
  code = code.replace('initCalendar()', 'initCalendar(); initEngCalendar()');
}

fs.writeFileSync('app.js', code, 'utf8');
console.log('English Calendar JS added!');

// Check if initCalendar call exists
const hasInit = code.includes('initEngCalendar()');
console.log('initEngCalendar wired:', hasInit);
