const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const engCalHTML = `

    <!-- ════════════════════════════════════
         🗓️ ENGLISH CALENDAR PAGE
         ════════════════════════════════════ -->
    <section id="page-english-calendar" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-home">←</button>
        <h2>English Calendar</h2>
        <span style="width:36px"></span>
      </div>

      <!-- Header -->
      <div style="background:#fff; padding:0.8rem 1rem 0; border-bottom:1px solid #e2e8f0;">
        <div class="cal-month-nav" style="padding:0; border:none;">
          <button class="cal-nav-btn" id="eng-cal-prev">‹</button>
          <div style="text-align:center;">
            <div style="font-size:0.7rem; font-weight:600; color:#1a73e8; letter-spacing:0.05em; text-transform:uppercase; margin-bottom:2px;">🗓️ English Calendar 2026</div>
            <div style="font-size:1.1rem; font-weight:700; color:#202124;" id="eng-cal-title">August 2026</div>
          </div>
          <button class="cal-nav-btn" id="eng-cal-next">›</button>
        </div>

        <!-- Day headers Google Calendar style -->
        <div class="cal-day-headers" style="margin:0; border-radius:0; border:none; background:transparent; padding:0.3rem 0 0.4rem;">
          <div class="cal-day-hdr sun">S</div>
          <div class="cal-day-hdr">M</div>
          <div class="cal-day-hdr">T</div>
          <div class="cal-day-hdr">W</div>
          <div class="cal-day-hdr">T</div>
          <div class="cal-day-hdr">F</div>
          <div class="cal-day-hdr">S</div>
        </div>
      </div>

      <!-- English Calendar Grid -->
      <div id="eng-cal-grid" style="display:grid; grid-template-columns:repeat(7,1fr); background:#fff; gap:0;">
        <!-- filled by JS -->
      </div>

      <!-- Selected day info card -->
      <div id="eng-cal-event" class="hidden" style="margin:0.8rem; background:#fff; border:1px solid #e2e8f0; border-left:4px solid #1a73e8; border-radius:10px; padding:0.9rem 1rem; box-shadow:0 1px 4px rgba(0,0,0,0.06);">
        <div style="display:flex; align-items:center; gap:0.8rem;">
          <div style="text-align:center; min-width:40px;">
            <div style="font-size:1.8rem; font-weight:900; color:#1a73e8; line-height:1;" id="eng-event-day"></div>
            <div style="font-size:0.6rem; font-weight:600; text-transform:uppercase; color:#70757a; letter-spacing:0.04em;" id="eng-event-dow"></div>
          </div>
          <div style="width:1px; height:36px; background:#e2e8f0;"></div>
          <div>
            <div style="font-size:0.95rem; font-weight:700; color:#202124;" id="eng-event-name"></div>
            <div style="font-size:0.75rem; color:#70757a; margin-top:2px;" id="eng-event-hindi"></div>
          </div>
        </div>
      </div>

      <!-- Legend -->
      <div style="margin:0.5rem 0.8rem; display:flex; gap:0.6rem; flex-wrap:wrap; font-size:0.72rem; color:#70757a;">
        <div style="display:flex; align-items:center; gap:4px;"><span style="width:10px;height:10px;border-radius:50%;background:#1a73e8;display:inline-block;"></span>Today</div>
        <div style="display:flex; align-items:center; gap:4px;"><span style="width:10px;height:10px;border-radius:3px;background:hsl(33,100%,90%);border:1px solid hsl(33,80%,70%);display:inline-block;"></span>Festival</div>
        <div style="display:flex; align-items:center; gap:4px;"><span style="width:10px;height:10px;border-radius:3px;background:#f0fdf4;border:1px solid #86efac;display:inline-block;"></span>Public Holiday</div>
        <div style="display:flex; align-items:center; gap:4px;"><span style="width:10px;height:10px;border-radius:3px;background:#fef2f2;display:inline-block;"></span>Sunday</div>
      </div>

      <!-- Upcoming this month -->
      <div style="margin:0 0.8rem 5rem;" id="eng-upcoming">
        <!-- filled by JS -->
      </div>
    </section>
`;

if (!html.includes('id="page-english-calendar"')) {
  // Insert it after page-calendar section
  const calEndIndex = html.indexOf('</section>', html.indexOf('id="page-calendar"')) + 10;
  html = html.substring(0, calEndIndex) + engCalHTML + html.substring(calEndIndex);
  fs.writeFileSync('index.html', html, 'utf8');
  console.log('English Calendar HTML inserted!');
} else {
  console.log('English Calendar HTML already exists.');
}
