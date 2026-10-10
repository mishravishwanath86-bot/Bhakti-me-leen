import sys, re, time

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_about_section = """    <!-- ══════════ ABOUT ══════════ -->
    <section id="page-about" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-home">←</button>
        <h2>हमारे बारे में</h2>
      </div>
      <div class="about-card">
        <img src="assets/app_logo.jpg?v=1787490651276" alt="भक्ति में लीन" class="about-logo" />
        <h3>भक्ति में लीन</h3>
        <p class="about-version">संस्करण 2.1.0</p>
        <p class="about-desc">भक्ति में लीन एक निःशुल्क भक्ति ऐप है जो आपको आरती, भजन, चालीसा, मंत्र, और रामायण के पाठ से जोड़ता है। हमारा उद्देश्य आपकी आध्यात्मिक यात्रा को सरल और सुंदर बनाना है।</p>
        <div class="about-divider"></div>
        <div class="about-links">
          <button class="about-link-btn">🌐 हमारी वेबसाइट</button>
          <button class="about-link-btn">📧 सम्पर्क करें</button>
          <button class="about-link-btn">🔒 गोपनीयता नीति</button>
        </div>
      </div>
    </section>"""

new_about_section = """    <!-- ══════════ ABOUT (हमारे बारे में) ══════════ -->
    <section id="page-about" class="page">
      <div class="page-header-bar">
        <button class="back-btn" data-back="page-home">←</button>
        <h2>हमारे बारे में</h2>
      </div>
      
      <div style="padding: 0 1.2rem 2rem;">
        
        <!-- Main Brand Hero Card -->
        <div class="about-card" style="margin: 0 0 1.2rem; background: linear-gradient(145deg, #2D1047 0%, #17042B 100%); border: 1.5px solid #F8C83B; border-radius: 26px; padding: 1.8rem 1.4rem; box-shadow: 0 12px 35px rgba(0,0,0,0.4), 0 0 20px rgba(248,200,59,0.15); text-align: center; position: relative; overflow: hidden;">
          
          <div style="width: 85px; height: 85px; border-radius: 50%; padding: 4px; background: linear-gradient(135deg, #F8C83B, #D97706); margin: 0 auto 12px; box-shadow: 0 0 25px rgba(248,200,59,0.5);">
            <img src="assets/app_logo.jpg?v=1787490651276" alt="भक्ति में लीन" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;" onerror="this.src='assets/gallery/bal_ganesha_little.jpg'" />
          </div>

          <h3 style="font-size: 1.45rem; font-weight: 900; color: #FFFDF8; margin: 0 0 4px 0; letter-spacing: 0.5px;">
            भक्ति में लीन
          </h3>
          <p style="font-size: 0.8rem; font-weight: 800; color: #FDE68A; margin: 0 0 12px 0;">
            Bhakti Mein Leen • संस्करण 2.2.0 (दिव्य 3D व AI एडिशन)
          </p>

          <p style="font-size: 0.84rem; color: #E2E8F0; line-height: 1.6; margin: 0 0 14px 0;">
            <strong>'भक्ति में लीन'</strong> एक पावन व निःशुल्क सनातन भक्ति मंच है, जो आधुनिक तकनीक के माध्यम से 3D मंदिर दर्शन, नित्य आरती, अमृत कथाएं, भजन, चालीसा और भगवद्गीता के दिव्य ज्ञान को हर भक्त की हथेली तक पहुँचाने के लिए समर्पित है।
          </p>

          <div style="display: inline-flex; align-items: center; gap: 6px; background: rgba(248,200,59,0.18); border: 1.2px solid #F8C83B; color: #FDE68A; padding: 5px 14px; border-radius: 14px; font-size: 0.78rem; font-weight: 800;">
            <span>🚩</span> ॐ सर्वे भवन्तु सुखिनः सर्वे सन्तु निरामयाः <span>🚩</span>
          </div>
        </div>

        <!-- 👨‍💻 DEVELOPER & CREATOR CARD -->
        <div style="background: radial-gradient(circle at 50% 20%, #3B1259 0%, #1C052E 100%); border: 1.5px solid rgba(248,200,59,0.45); border-radius: 24px; padding: 1.4rem 1.2rem; margin-bottom: 1.2rem; box-shadow: 0 8px 30px rgba(0,0,0,0.35);">
          
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
            <div style="width: 52px; height: 52px; border-radius: 16px; background: linear-gradient(135deg, #F8C83B, #D97706); display: flex; align-items: center; justify-content: center; font-size: 1.6rem; flex-shrink: 0; box-shadow: 0 4px 15px rgba(248,200,59,0.35);">
              👨‍💻
            </div>
            <div>
              <div style="font-size: 0.72rem; color: #FDE68A; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px;">
                मुख्य परिकल्पना व डेवलपर (Creator & Lead Developer)
              </div>
              <div style="font-size: 1.25rem; font-weight: 900; color: #FFFDF8; margin-top: 2px;">
                विश्वनाथ मिश्रा (Vishwanath Mishra)
              </div>
            </div>
          </div>

          <!-- Motivational Devotional Message -->
          <div style="background: rgba(255,255,255,0.06); border-left: 3.5px solid #F8C83B; border-radius: 0 14px 14px 0; padding: 10px 12px; margin-bottom: 12px;">
            <div style="font-size: 0.82rem; font-style: italic; color: #FFFDF8; line-height: 1.5;">
              "तकनीक और सनातन धर्म का यह पावन संगम, प्रत्येक हृदय में ईश्वर के प्रति अगाध प्रेम, आत्म-शांति और सकारात्मक ऊर्जा का संचार करने के लिए समर्पित है। निष्काम भाव से किया गया कर्म ही जीवन की सबसे बड़ी पूजा है।"
            </div>
            <div style="text-align: right; font-size: 0.72rem; font-weight: 800; color: #FDE68A; margin-top: 4px;">
              — विश्वनाथ मिश्रा
            </div>
          </div>

          <div style="display: flex; gap: 8px; justify-content: space-between;">
            <div style="flex: 1; background: rgba(0,0,0,0.25); border-radius: 12px; padding: 8px; text-align: center;">
              <div style="font-size: 1.1rem; color: #F8C83B; font-weight: 900;">100%</div>
              <div style="font-size: 0.65rem; color: #CBD5E1; margin-top: 2px;">निःशुल्क सनातन सेवा</div>
            </div>
            <div style="flex: 1; background: rgba(0,0,0,0.25); border-radius: 12px; padding: 8px; text-align: center;">
              <div style="font-size: 1.1rem; color: #F8C83B; font-weight: 900;">3D & AI</div>
              <div style="font-size: 0.65rem; color: #CBD5E1; margin-top: 2px;">स्मार्ट वैदिक टेक</div>
            </div>
            <div style="flex: 1; background: rgba(0,0,0,0.25); border-radius: 12px; padding: 8px; text-align: center;">
              <div style="font-size: 1.1rem; color: #F8C83B; font-weight: 900;">2000+</div>
              <div style="font-size: 0.65rem; color: #CBD5E1; margin-top: 2px;">भक्ति प्रश्नोत्तरी व पाठ</div>
            </div>
          </div>
        </div>

        <!-- Quick Contact & Links -->
        <div style="display: flex; flex-direction: column; gap: 10px;">
          <button class="about-link-btn" onclick="if(typeof showToast === 'function') showToast('🌐 आधिकारिक वेबसाइट जल्द उपलब्ध होगी!');" style="width: 100%; background: rgba(255,255,255,0.06); border: 1.2px solid rgba(248,200,59,0.3); border-radius: 16px; padding: 12px 16px; color: #FFFDF8; font-weight: 800; font-size: 0.88rem; display: flex; align-items: center; justify-content: space-between; cursor: pointer;">
            <span style="display:flex; align-items:center; gap:8px;"><span>🌐</span> हमारी वेबसाइट</span>
            <span>❯</span>
          </button>
          
          <button class="about-link-btn" onclick="window.open('mailto:vishwanath.mishra.dev@gmail.com', '_blank');" style="width: 100%; background: rgba(255,255,255,0.06); border: 1.2px solid rgba(248,200,59,0.3); border-radius: 16px; padding: 12px 16px; color: #FFFDF8; font-weight: 800; font-size: 0.88rem; display: flex; align-items: center; justify-content: space-between; cursor: pointer;">
            <span style="display:flex; align-items:center; gap:8px;"><span>📧</span> डेवलपर से सम्पर्क करें</span>
            <span>❯</span>
          </button>

          <button class="about-link-btn" onclick="if(typeof showToast === 'function') showToast('⭐ आपके आशीर्वाद व समर्थन हेतु आभार!');" style="width: 100%; background: rgba(255,255,255,0.06); border: 1.2px solid rgba(248,200,59,0.3); border-radius: 16px; padding: 12px 16px; color: #FFFDF8; font-weight: 800; font-size: 0.88rem; display: flex; align-items: center; justify-content: space-between; cursor: pointer;">
            <span style="display:flex; align-items:center; gap:8px;"><span>⭐</span> ऐप को 5-स्टार रेटिंग दें</span>
            <span>❯</span>
          </button>
        </div>

      </div>
    </section>"""

if old_about_section in html:
    html = html.replace(old_about_section, new_about_section)
    print("✓ Successfully replaced About section in index.html")
else:
    print("Direct match not found, replacing with regex")
    html = re.sub(r'<!-- ══════════ ABOUT ══════════ -->\s*<section id="page-about" class="page">[\s\S]*?<\/section>', new_about_section, html)
    print("✓ Replaced via Regex")

# Bump cache buster
ts = int(time.time())
html = re.sub(r'app\.js\?v=\d+', f'app.js?v={ts}', html)
html = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={ts}', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ Saved updated index.html with Vishwanath Mishra Developer Card and Devotional Motivation (v={ts})")
