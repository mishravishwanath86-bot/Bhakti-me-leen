const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Find the closing div of Diwali page content and inject muhurat data before it
const muhurateSection = `
        <!-- Lakshmi Puja Muhurat 2026 -->
        <div class="sk-date-card" style="background:linear-gradient(135deg,#7B1C1C,#a50000); color:white; padding:1.2rem; border-radius:16px; margin-bottom:1.2rem; text-align:center;">
          <div style="font-size:1rem; font-weight:600; opacity:0.9;">लक्ष्मी पूजा (Lakshmi Puja) 2026</div>
          <div style="font-size:3rem; font-weight:900; line-height:1.1; margin: 0.3rem 0;">8</div>
          <div style="font-size:1.2rem; font-weight:700;">नवम्बर 2026</div>
          <div style="font-size:0.95rem; opacity:0.85; margin-top:0.3rem;">रविवार / Sunday</div>
        </div>

        <!-- Pradosh Kaal Muhurat -->
        <div class="sk-date-card" style="border-left:4px solid #f97316; padding:1.2rem; border-radius:12px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">⏰ लक्ष्मी पूजा मुहूर्त (Pradosh Kaal)</div>
          <div style="font-size:1.05rem; color:#a50000; font-weight:700;">05:54 PM से 07:50 PM</div>
          <div style="font-size:0.85rem; color:#475569; margin-top:0.3rem; margin-bottom:1rem;">अवधि - 1 घंटा 56 मिनट</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.85rem; color:#475569; border-top:1px solid #e2e8f0; padding-top:0.8rem;">
            <div>📍 Pradosh Kaal - 05:31 PM to 08:09 PM</div>
            <div>📍 Vrishabha Kaal - 05:54 PM to 07:50 PM</div>
            <div>📍 Amavasya Tithi Begins - 11:27 AM on Nov 08, 2026</div>
            <div>📍 Amavasya Tithi Ends - 12:31 PM on Nov 09, 2026</div>
          </div>
        </div>

        <!-- Mahanishita Kaal -->
        <div class="sk-date-card" style="border-left:4px solid #6366f1; padding:1.2rem; border-radius:12px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:#4338ca; margin-bottom:0.8rem;">🌙 महानिशिता काल मुहूर्त</div>
          <div style="font-size:1.05rem; color:#4338ca; font-weight:700;">11:39 PM से 12:31 AM, Nov 09</div>
          <div style="font-size:0.85rem; color:#475569; margin-top:0.3rem;">अवधि - 53 मिनट</div>
          <div style="margin-top:0.8rem; font-size:0.82rem; color:#475569; border-top:1px solid #e2e8f0; padding-top:0.6rem;">
            <div>Simha Kaal - 12:25 AM to 02:42 AM, Nov 09</div>
          </div>
        </div>

        <!-- Choghadiya Muhurat -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🌟 शुभ चौघड़िया मुहूर्त</div>
          <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.85rem; color:#334155;">
            <div style="background:#f0fdf4; padding:0.5rem 0.8rem; border-radius:8px;">🌅 Morning (Chara, Labha, Amrita) - 11:27 AM to 12:05 PM</div>
            <div style="background:#f0fdf4; padding:0.5rem 0.8rem; border-radius:8px;">☀️ Afternoon (Shubha) - 01:26 PM to 02:48 PM</div>
            <div style="background:#fef9ec; padding:0.5rem 0.8rem; border-radius:8px; font-weight:600;">🌆 Evening (Shubha, Amrita, Chara) - 05:31 PM to 10:27 PM ⭐</div>
            <div style="background:#f0fdf4; padding:0.5rem 0.8rem; border-radius:8px;">🌃 Night (Labha) - 01:43 AM to 03:22 AM, Nov 09</div>
            <div style="background:#f0fdf4; padding:0.5rem 0.8rem; border-radius:8px;">🌄 Early Morning (Shubha) - 05:00 AM to 06:39 AM, Nov 09</div>
          </div>
        </div>

        <!-- City-wise Muhurat -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:0.95rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">🏙️ शहर-वार मुहूर्त (Lakshmi Puja)</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.78rem;">
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">New Delhi</div><div>05:54–07:50 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Noida</div><div>05:54–07:49 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Pune</div><div>06:24–08:24 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Chandigarh</div><div>05:52–07:46 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Chennai</div><div>06:07–08:09 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Kolkata</div><div>05:20–07:18 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Jaipur</div><div>06:03–07:59 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Mumbai</div><div>06:27–08:27 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Hyderabad</div><div>06:07–08:08 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Bengaluru</div><div>06:17–08:20 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Gurgaon</div><div>05:55–07:51 PM</div></div>
            <div style="background:#fef3c7; padding:0.5rem; border-radius:8px;"><div style="font-weight:700; color:var(--maroon);">Ahmedabad</div><div>06:22–08:20 PM</div></div>
          </div>
        </div>

        <!-- Lakshmi Puja Recent Years -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📅 लक्ष्मी पूजा - वर्ष-वार तिथियाँ</div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.4rem; font-size:0.83rem;">
            <div style="color:#475569;">2023 - Sun, Nov 12</div>
            <div style="color:#475569;">2029 - Mon, Nov 5</div>
            <div style="color:#475569;">2024 - Fri, Nov 1</div>
            <div style="color:#475569;">2030 - Sat, Oct 26</div>
            <div style="color:#475569;">2025 - Mon, Oct 20</div>
            <div style="color:#475569;">2031 - Fri, Nov 14</div>
            <div style="color:#a50000; font-weight:700;">2026 - Sun, Nov 8 ←</div>
            <div style="color:#475569;">2032 - Tue, Nov 2</div>
            <div style="color:#475569;">2027 - Fri, Oct 29</div>
            <div style="color:#475569;">2033 - Sat, Oct 22</div>
            <div style="color:#475569;">2028 - Tue, Oct 17</div>
            <div></div>
          </div>
        </div>

        <!-- Lakshmi Puja Vrat Info -->
        <div class="sk-date-card" style="padding:1.2rem; border-radius:16px; margin-bottom:1.2rem;">
          <div style="font-size:1rem; font-weight:800; color:var(--maroon); margin-bottom:0.8rem;">📖 लक्ष्मी पूजा विधि</div>
          <div style="font-size:0.88rem; color:#334155; line-height:1.75; display:flex; flex-direction:column; gap:0.8rem;">
            <div><strong style="color:var(--maroon);">🌸 Puja Preparations:</strong> Decorate home with marigold flowers, Ashoka, mango and banana leaves. Keep Mangalik Kalash covered with unpeeled coconut at both sides of the main entrance.</div>
            <div><strong style="color:var(--maroon);">🕯️ Best Time:</strong> Lakshmi Puja should be done during <strong>Pradosh Kaal</strong> when <strong>Vrishabha Lagna</strong> (Sthir Lagna) prevails — as Lakshmiji will stay in your home!</div>
            <div><strong style="color:var(--maroon);">🍚 Chopda Pujan:</strong> Gujarati businessmen do Chopda Pujan during Diwali Puja — new account books are inaugurated in presence of Goddess Lakshmi.</div>
          </div>
        </div>`;

// Inject before the last </div></section> of Diwali page
html = html.replace(
  /(<\/div>\s*<\/section>\s*<!-- 🌺 HOLI PAGE 🌺 -->)/,
  muhurateSection + '\n      </div>\n    </section>\n\n    <!-- 🌺 HOLI PAGE 🌺 -->'
);

const time = new Date().getTime();
html = html.replace(/app\.js(\?v=\d+)?/, `app.js?v=${time}`);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Added Lakshmi Puja Muhurat data to Diwali page!');
