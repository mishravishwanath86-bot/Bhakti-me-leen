# 📖🎬 Phase 2M-D — Final Apply Safety Verification / Dry Run Report

**Mode**: `STRICT READ-ONLY — FINAL DRY RUN ONLY` (Zero Database Writes)  
**Database File**: `db/bhakti.db` (Unchanged, 0 Writes)  
**Date**: `2026-08-31 12:58:39`  
**Safety Gate**: **`PASS`**  

---

## 1. 🛡️ Current Database Baseline vs. Projected Post-Apply State

| Metric | Current Real Baseline | Projected Post-Apply | Status |
| :--- | :--- | :--- | :--- |
| **Total Database Records** | **`10,010`** | `10,010` | ✅ Unchanged |
| **FTS5 Search Documents** | **`10,010`** | `10,010` | ✅ Unchanged |
| **Playable Audio Total** | **`240`** | **`284`** (+44) | 🎯 Audio Expansion |
| **Local MP3 Audio** | **`38`** | `38` | ✅ Untouched |
| **YouTube HD Audio** | **`202`** | **`246`** (+44) | 🎧 +44 Verified Spoken Kathas |
| **YouTube Video URLs** | **`109`** | **`148`** (+39) | 🎬 +39 Verified Video Discourses |
| **PRAGMA integrity_check** | **`ok`** | `ok` | ✅ 0 Corruption |
| **Foreign-Key Violations** | **`0`** | `0` | ✅ 100% Valid |
| **Real Database Writes** | **`0`** | `0` | ✅ Zero Writes (Dry Run Only) |

---

## 2. 📖 Projected Katha Coverage Evolution Across All 505 Records

| Katha Category Metric | Current State | Projected Post-Apply | Change |
| :--- | :---: | :---: | :---: |
| **Katha With Audio** | `179` | **`223`** | +44 |
| **Katha With Video** | `107` | **`146`** | +39 |
| **Katha With Both Media** | `98` | **`135`** | +37 |
| **Katha With Neither Media (Gaps)** | `317` | **`271`** | -46 |

---

## 3. 📋 83 Candidate Safety Revalidation Matrix

| # | Database Record ID | Katha Title | Media Type | YouTube Video ID | Current Value | Proposed Value | Safety Verdict |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :---: |
| 01 | `b3-katha-durga-mahishasur-vadh-devi-mahatmya` | **मां दुर्गा द्वारा महिषासुर मर्दन एवं त्रिलोक रक्षा** | 🎧 Audio | [`rRXWclZJpHA`](https://www.youtube.com/watch?v=rRXWclZJpHA) | `NULL` | [`rRXWclZJpHA`](https://www.youtube.com/watch?v=rRXWclZJpHA) | ✅ **`SAFE_TO_APPLY`** |
| 02 | `b4-katha-lakshmi-samudra-manthan-prabhu-varan` | **महालक्ष्मी का प्राकट्य एवं भगवान विष्णु का वरण** | 🎧 Audio | [`B0D0mWGZwhk`](https://www.youtube.com/watch?v=B0D0mWGZwhk) | `NULL` | [`B0D0mWGZwhk`](https://www.youtube.com/watch?v=B0D0mWGZwhk) | ✅ **`SAFE_TO_APPLY`** |
| 03 | `b15-katha-ramayana-setubandha-rameshwaram-b15` | **श्री रामचरितमानस सेतुबंध एवं रामेश्वर प्रतिष्ठा (पंचदश सेतुबंध 15)** | 🎧 Audio | [`otVkR1lZ-KA`](https://www.youtube.com/watch?v=otVkR1lZ-KA) | `NULL` | [`otVkR1lZ-KA`](https://www.youtube.com/watch?v=otVkR1lZ-KA) | ✅ **`SAFE_TO_APPLY`** |
| 04 | `b19-katha-krishna-sudama-dwarka-bhent-b19` | **द्वारका में सुदामा मिलन एवं तंदुल प्रीति कथा (एकोनविंशति सुदामा कथा 19)** | 🎧 Audio | [`iAj14mp7I8E`](https://www.youtube.com/watch?v=iAj14mp7I8E) | `NULL` | [`iAj14mp7I8E`](https://www.youtube.com/watch?v=iAj14mp7I8E) | ✅ **`SAFE_TO_APPLY`** |
| 05 | `b19-katha-ram-rajyabhisheka-avadh-mahima-b19` | **प्रभु श्री राम राज्याभिषेक एवं रामराज्य स्थापना कथा (एकोनविंशति अवध कथा 19)** | 🎧 Audio | [`A9GxNSXiCXA`](https://www.youtube.com/watch?v=A9GxNSXiCXA) | `NULL` | [`A9GxNSXiCXA`](https://www.youtube.com/watch?v=A9GxNSXiCXA) | ✅ **`SAFE_TO_APPLY`** |
| 06 | `b2-katha-bhakta-raja-shivi-kapot-raksha` | **राजा शिवि की कपोत (कबूतर) रक्षा: अपने मांस का तराजू दान** | 🎧 Audio | [`Uxxbl9FaZ9E`](https://www.youtube.com/watch?v=Uxxbl9FaZ9E) | `NULL` | [`Uxxbl9FaZ9E`](https://www.youtube.com/watch?v=Uxxbl9FaZ9E) | ✅ **`SAFE_TO_APPLY`** |
| 07 | `b2-katha-krishna-sudama-charitra-tandul` | **सुदामा चरित्र: तीन मुट्ठी चावल पर तीनों लोक अर्पण** | 🎧 Audio | [`c5dW1ERwL0I`](https://www.youtube.com/watch?v=c5dW1ERwL0I) | `NULL` | [`c5dW1ERwL0I`](https://www.youtube.com/watch?v=c5dW1ERwL0I) | ✅ **`SAFE_TO_APPLY`** |
| 08 | `b2-katha-ram-dhanush-bhanga-parashuram` | **शिव धनुष भंग एवं श्री परशुराम-लक्ष्मण संवाद** | 🎧 Audio | [`MBHNw0hoUA0`](https://www.youtube.com/watch?v=MBHNw0hoUA0) | `NULL` | [`MBHNw0hoUA0`](https://www.youtube.com/watch?v=MBHNw0hoUA0) | ✅ **`SAFE_TO_APPLY`** |
| 09 | `b2-katha-ram-janakpur-pushpa-vatika` | **जनकपुर पुष्प वाटिका एवं श्री सीता-राम प्रथम मिलन** | 🎧 Audio | [`KPozhPim-a0`](https://www.youtube.com/watch?v=KPozhPim-a0) | `NULL` | [`KPozhPim-a0`](https://www.youtube.com/watch?v=KPozhPim-a0) | ✅ **`SAFE_TO_APPLY`** |
| 10 | `b2-katha-shiva-gangadhar-neelkantha` | **गंगाधर एवं नीलकंठ प्राकट्य: समुद्र मंथन हलाहल पान** | 🎧 Audio | [`FqACJaY8i5Q`](https://www.youtube.com/watch?v=FqACJaY8i5Q) | `NULL` | [`FqACJaY8i5Q`](https://www.youtube.com/watch?v=FqACJaY8i5Q) | ✅ **`SAFE_TO_APPLY`** |
| 11 | `b2-katha-shiva-tripurasur-vadh-devadhidev` | **त्रिपुरासुर वध एवं महादेव 'त्रिपुरारि' प्राकट्य** | 🎧 Audio | [`cZZEZvAfLD0`](https://www.youtube.com/watch?v=cZZEZvAfLD0) | `NULL` | [`cZZEZvAfLD0`](https://www.youtube.com/watch?v=cZZEZvAfLD0) | ✅ **`SAFE_TO_APPLY`** |
| 12 | `b20-ganesh-katha-b20-338` | **भगवान गणेश दिव्य चरित्र स्तुति संकीर्तन (विंशति पद 338 - 20)** | 🎧 Audio | [`42LQ73PLHz4`](https://www.youtube.com/watch?v=42LQ73PLHz4) | `NULL` | [`42LQ73PLHz4`](https://www.youtube.com/watch?v=42LQ73PLHz4) | ✅ **`SAFE_TO_APPLY`** |
| 13 | `b20-ganesh-katha-b20-398` | **भगवान गणेश दिव्य चरित्र स्तुति संकीर्तन (विंशति पद 398 - 20)** | 🎧 Audio | [`SBH9O2Cj2l0`](https://www.youtube.com/watch?v=SBH9O2Cj2l0) | `NULL` | [`SBH9O2Cj2l0`](https://www.youtube.com/watch?v=SBH9O2Cj2l0) | ✅ **`SAFE_TO_APPLY`** |
| 14 | `b20-saraswati-katha-b20-077` | **मां सरस्वती लीला प्रसंग स्तुति संकीर्तन (विंशति पद 077 - 20)** | 🎧 Audio | [`NQ-9h9dchDg`](https://www.youtube.com/watch?v=NQ-9h9dchDg) | `NULL` | [`NQ-9h9dchDg`](https://www.youtube.com/watch?v=NQ-9h9dchDg) | ✅ **`SAFE_TO_APPLY`** |
| 15 | `b3-katha-krishna-draupadi-cheer-haran-akshay-vastra` | **कुरु सभा में द्रौपदी चीर हरण एवं प्रभु का अक्षय वस्त्र दान** | 🎧 Audio | [`DT0VAcU5q80`](https://www.youtube.com/watch?v=DT0VAcU5q80) | `NULL` | [`DT0VAcU5q80`](https://www.youtube.com/watch?v=DT0VAcU5q80) | ✅ **`SAFE_TO_APPLY`** |
| 16 | `b3-katha-ram-dhanush-yajna-sita-swayamvar` | **जनकपुर में धनुष भंग एवं श्री सीता-राम विवाह महोत्सव** | 🎧 Audio | [`xUolyvePw2k`](https://www.youtube.com/watch?v=xUolyvePw2k) | `NULL` | [`xUolyvePw2k`](https://www.youtube.com/watch?v=xUolyvePw2k) | ✅ **`SAFE_TO_APPLY`** |
| 17 | `b3-katha-ram-kaikeyi-varadan-vanvaas-prasang` | **मंथरा कुटिलता, कैकेयी के दो वरदान एवं राम वनवास** | 🎧 Audio | [`4_KWTTzYYDQ`](https://www.youtube.com/watch?v=4_KWTTzYYDQ) | `NULL` | [`4_KWTTzYYDQ`](https://www.youtube.com/watch?v=4_KWTTzYYDQ) | ✅ **`SAFE_TO_APPLY`** |
| 18 | `b3-katha-ram-putreshti-yajna-ram-janma` | **राजा दशरथ का पुत्रेष्टि यज्ञ एवं श्री राम प्राकट्य कथा** | 🎧 Audio | [`rhNT6X4-ktE`](https://www.youtube.com/watch?v=rhNT6X4-ktE) | `NULL` | [`rhNT6X4-ktE`](https://www.youtube.com/watch?v=rhNT6X4-ktE) | ✅ **`SAFE_TO_APPLY`** |
| 19 | `b3-katha-shiva-sati-daha-daksha-yajna-destructive-tandav` | **दक्ष प्रजापति का यज्ञ, सती देह त्याग एवं वीरभद्र तांडव** | 🎧 Audio | [`KOZzhnghiNk`](https://www.youtube.com/watch?v=KOZzhnghiNk) | `NULL` | [`KOZzhnghiNk`](https://www.youtube.com/watch?v=KOZzhnghiNk) | ✅ **`SAFE_TO_APPLY`** |
| 20 | `b3-katha-shiva-tripurasur-vadh-meru-dhanush` | **त्रिपुरासुर वध हेतु पृथ्वी को रथ और मेरु को धनुष बनाना** | 🎧 Audio | [`AT2RVA-2dUI`](https://www.youtube.com/watch?v=AT2RVA-2dUI) | `NULL` | [`AT2RVA-2dUI`](https://www.youtube.com/watch?v=AT2RVA-2dUI) | ✅ **`SAFE_TO_APPLY`** |
| 21 | `b4-katha-ganesh-ekadanta-parashuram-katha` | **एकदंत स्वरूप की कथा (परशुराम जी के फरसे का सम्मान)** | 🎧 Audio | [`pwDPC-Wqbbw`](https://www.youtube.com/watch?v=pwDPC-Wqbbw) | `NULL` | [`pwDPC-Wqbbw`](https://www.youtube.com/watch?v=pwDPC-Wqbbw) | ✅ **`SAFE_TO_APPLY`** |
| 22 | `b4-katha-ganesh-parikrama-katha-pratham-poojya` | **माता-पिता की परिक्रमा एवं गणेश जी का प्रथम पूज्य बनना** | 🎧 Audio | [`S_xTuJrIQl8`](https://www.youtube.com/watch?v=S_xTuJrIQl8) | `NULL` | [`S_xTuJrIQl8`](https://www.youtube.com/watch?v=S_xTuJrIQl8) | ✅ **`SAFE_TO_APPLY`** |
| 23 | `b4-katha-guru_sant-kabir-aur-ram-naam-diksha` | **संत कबीर और स्वामी रामानंद से पंचगंगा घाट पर राम नाम दीक्षा** | 🎧 Audio | [`ESRFQriK2bE`](https://www.youtube.com/watch?v=ESRFQriK2bE) | `NULL` | [`ESRFQriK2bE`](https://www.youtube.com/watch?v=ESRFQriK2bE) | ✅ **`SAFE_TO_APPLY`** |
| 24 | `b4-katha-krishna-sudama-prem-bhent-leela` | **भक्त सुदामा की चावल पोटली एवं द्वारकाधीश का प्रेम** | 🎧 Audio | [`4rndFFXBVRM`](https://www.youtube.com/watch?v=4rndFFXBVRM) | `NULL` | [`4rndFFXBVRM`](https://www.youtube.com/watch?v=4rndFFXBVRM) | ✅ **`SAFE_TO_APPLY`** |
| 25 | `b4-katha-ram-dhanush-yagya-aur-parashuram-samvad` | **जनकपुर धनुष भंग एवं श्री परशुराम-लक्ष्मण संवाद** | 🎧 Audio | [`i-0u6ncctks`](https://www.youtube.com/watch?v=i-0u6ncctks) | `NULL` | [`i-0u6ncctks`](https://www.youtube.com/watch?v=i-0u6ncctks) | ✅ **`SAFE_TO_APPLY`** |
| 26 | `b4-katha-ram-jayant-katha-kripalu-shri-ram` | **जयंत का अपराध एवं कृपालु श्री राम द्वारा क्षमादान** | 🎧 Audio | [`dyoeUGF_IiI`](https://www.youtube.com/watch?v=dyoeUGF_IiI) | `NULL` | [`dyoeUGF_IiI`](https://www.youtube.com/watch?v=dyoeUGF_IiI) | ✅ **`SAFE_TO_APPLY`** |
| 27 | `b4-katha-ram-setu-bandhan-nal-neel-leela` | **नल-नील द्वारा सेतु बंधन एवं राम नाम पत्थरों का तैरना** | 🎧 Audio | [`TtP5g0rXrJc`](https://www.youtube.com/watch?v=TtP5g0rXrJc) | `NULL` | [`TtP5g0rXrJc`](https://www.youtube.com/watch?v=TtP5g0rXrJc) | ✅ **`SAFE_TO_APPLY`** |
| 28 | `b4-katha-ram-vibheeshana-sharanagati-katha` | **विभीषण शरणागति एवं प्रभु श्री राम का अभय वरदान** | 🎧 Audio | [`hj5-T8aHKuQ`](https://www.youtube.com/watch?v=hj5-T8aHKuQ) | `NULL` | [`hj5-T8aHKuQ`](https://www.youtube.com/watch?v=hj5-T8aHKuQ) | ✅ **`SAFE_TO_APPLY`** |
| 29 | `b4-katha-shiva-kashi-mahima-aur-manikarnika` | **काशी की उत्पत्ति, पंचक्रोशी परिक्रमा एवं मणिकर्णिका घाट** | 🎧 Audio | [`bINkwtTzV7U`](https://www.youtube.com/watch?v=bINkwtTzV7U) | `NULL` | [`bINkwtTzV7U`](https://www.youtube.com/watch?v=bINkwtTzV7U) | ✅ **`SAFE_TO_APPLY`** |
| 30 | `b4-katha-shiva-tripurasur-vadh-katha` | **त्रिपुरासुर वध एवं महादेव का त्रिपुरारी नामकरण** | 🎧 Audio | [`xw7L5yCrYtk`](https://www.youtube.com/watch?v=xw7L5yCrYtk) | `NULL` | [`xw7L5yCrYtk`](https://www.youtube.com/watch?v=xw7L5yCrYtk) | ✅ **`SAFE_TO_APPLY`** |
| 31 | `b5-katha-ganesh-pratham-pujya-parikrama-katha` | **गणेश जी की प्रथम पूजा: माता-पिता की परिक्रमा से ब्रह्मांड विजय** | 🎧 Audio | [`msKSippIeOE`](https://www.youtube.com/watch?v=msKSippIeOE) | `NULL` | [`msKSippIeOE`](https://www.youtube.com/watch?v=msKSippIeOE) | ✅ **`SAFE_TO_APPLY`** |
| 32 | `b5-katha-krishna-draupadi-cheer-haran-raksha` | **द्रौपदी चीर हरण: कौरव सभा में अक्षय वस्त्र अवतार** | 🎧 Audio | [`kiDFy-BcdMY`](https://www.youtube.com/watch?v=kiDFy-BcdMY) | `NULL` | [`kiDFy-BcdMY`](https://www.youtube.com/watch?v=kiDFy-BcdMY) | ✅ **`SAFE_TO_APPLY`** |
| 33 | `b5-katha-krishna-sudama-charitra-tundil-bhet` | **सुदामा चरित्र: दीन सुदामा की चावल भेंट और त्रैलोक्य दान** | 🎧 Audio | [`fFg12HXuQ0M`](https://www.youtube.com/watch?v=fFg12HXuQ0M) | `NULL` | [`fFg12HXuQ0M`](https://www.youtube.com/watch?v=fFg12HXuQ0M) | ✅ **`SAFE_TO_APPLY`** |
| 34 | `b5-katha-ram-setu-nirman-nal-neel-pathar-tarana` | **रामेश्वरम सेतु निर्माण: नल-नील द्वारा पत्थरों को तैराना** | 🎧 Audio | [`feZIIN_iqgU`](https://www.youtube.com/watch?v=feZIIN_iqgU) | `NULL` | [`feZIIN_iqgU`](https://www.youtube.com/watch?v=feZIIN_iqgU) | ✅ **`SAFE_TO_APPLY`** |
| 35 | `b5-katha-ram-vibhishan-sharanagati-abhay-dan` | **विभीषण शरणागति: रावण त्याग और श्री राम द्वारा लंकापति पद दान** | 🎧 Audio | [`kcC1J0rSBZQ`](https://www.youtube.com/watch?v=kcC1J0rSBZQ) | `NULL` | [`kcC1J0rSBZQ`](https://www.youtube.com/watch?v=kcC1J0rSBZQ) | ✅ **`SAFE_TO_APPLY`** |
| 36 | `b5-katha-shiva-sati-deha-tyaga-daksha-yagya` | **दक्ष प्रजापति यज्ञ विध्वंस एवं माता सती का देह त्याग** | 🎧 Audio | [`ehtD_ojSWys`](https://www.youtube.com/watch?v=ehtD_ojSWys) | `NULL` | [`ehtD_ojSWys`](https://www.youtube.com/watch?v=ehtD_ojSWys) | ✅ **`SAFE_TO_APPLY`** |
| 37 | `b5-katha-shiva-tripurasura-vadh-prithvi-ratha` | **त्रिपुरासुर वध: पृथ्वी का रथ और मेरु का धनुष बनाकर संहार** | 🎧 Audio | [`Sm7KL0-fUzY`](https://www.youtube.com/watch?v=Sm7KL0-fUzY) | `NULL` | [`Sm7KL0-fUzY`](https://www.youtube.com/watch?v=Sm7KL0-fUzY) | ✅ **`SAFE_TO_APPLY`** |
| 38 | `b6-katha-ram-agastya-muni-divyastra-dhanush-dan-b6` | **अगस्त्य मुनि मिलन: श्री राम को वैष्णव धनुष एवं अक्षय तरकश दान** | 🎧 Audio | [`96iw30PBSeY`](https://www.youtube.com/watch?v=96iw30PBSeY) | `NULL` | [`96iw30PBSeY`](https://www.youtube.com/watch?v=96iw30PBSeY) | ✅ **`SAFE_TO_APPLY`** |
| 39 | `b6-katha-ram-ahiravan-patal-prasang-hanuman-b6` | **अहिरावण पाताल प्रसंग: पाताल लोक में हनुमान जी द्वारा राम-लक्ष्मण मुक्ति** | 🎧 Audio | [`2MWF-UHsC64`](https://www.youtube.com/watch?v=2MWF-UHsC64) | `NULL` | [`2MWF-UHsC64`](https://www.youtube.com/watch?v=2MWF-UHsC64) | ✅ **`SAFE_TO_APPLY`** |
| 40 | `b6-katha-ram-bharat-charitra-chitrakoot-b6` | **श्री भरत चरित्र: चित्रकूट में पादुका ग्रहण एवं नन्दिग्राम तपस्या** | 🎧 Audio | [`B8rWe3XOSTk`](https://www.youtube.com/watch?v=B8rWe3XOSTk) | `NULL` | [`B8rWe3XOSTk`](https://www.youtube.com/watch?v=B8rWe3XOSTk) | ✅ **`SAFE_TO_APPLY`** |
| 41 | `b6-katha-ram-kakbhusundi-ram-charitra-katha-b6` | **काकभुशुण्डि जी द्वारा गरुड़ जी को सुनाई गई अमर रामकथा** | 🎧 Audio | [`_Fii7fqy2HQ`](https://www.youtube.com/watch?v=_Fii7fqy2HQ) | `NULL` | [`_Fii7fqy2HQ`](https://www.youtube.com/watch?v=_Fii7fqy2HQ) | ✅ **`SAFE_TO_APPLY`** |
| 42 | `b6-katha-ram-mandodari-ravan-hitopadesh-b6` | **महारानी मंदोदरी का रावण को हितोपदेश: 'कंत राम बिरोध परिहरहू'** | 🎧 Audio | [`_nGbYVEnce8`](https://www.youtube.com/watch?v=_nGbYVEnce8) | `NULL` | [`_nGbYVEnce8`](https://www.youtube.com/watch?v=_nGbYVEnce8) | ✅ **`SAFE_TO_APPLY`** |
| 43 | `b9-katha-krishna-draupadi-cheer-haran-raksha-b9` | **द्रौपदी चीर हरण: 'हे गोविंद राखो लाज हमारी' और चीर का अखंड विस्तार** | 🎧 Audio | [`5rCaKDaHZ4Q`](https://www.youtube.com/watch?v=5rCaKDaHZ4Q) | `NULL` | [`5rCaKDaHZ4Q`](https://www.youtube.com/watch?v=5rCaKDaHZ4Q) | ✅ **`SAFE_TO_APPLY`** |
| 44 | `b9-katha-krishna-sudama-charitra-prem-b9` | **सुदामा चरित्र: चार मुट्ठी तंदुल (चावल) और दो लोकों का ऐश्वर्य दान** | 🎧 Audio | [`ZV_z8e-szmw`](https://www.youtube.com/watch?v=ZV_z8e-szmw) | `NULL` | [`ZV_z8e-szmw`](https://www.youtube.com/watch?v=ZV_z8e-szmw) | ✅ **`SAFE_TO_APPLY`** |
| 45 | `b15-katha-ramayana-setubandha-rameshwaram-b15` | **श्री रामचरितमानस सेतुबंध एवं रामेश्वर प्रतिष्ठा (पंचदश सेतुबंध 15)** | 🎬 Video | [`yoKJVFMttoc`](https://www.youtube.com/watch?v=yoKJVFMttoc) | `NULL` | [`yoKJVFMttoc`](https://www.youtube.com/watch?v=yoKJVFMttoc) | ✅ **`SAFE_TO_APPLY`** |
| 46 | `b19-katha-krishna-sudama-dwarka-bhent-b19` | **द्वारका में सुदामा मिलन एवं तंदुल प्रीति कथा (एकोनविंशति सुदामा कथा 19)** | 🎬 Video | [`F5Q7rn13aPE`](https://www.youtube.com/watch?v=F5Q7rn13aPE) | `NULL` | [`F5Q7rn13aPE`](https://www.youtube.com/watch?v=F5Q7rn13aPE) | ✅ **`SAFE_TO_APPLY`** |
| 47 | `b19-katha-ram-rajyabhisheka-avadh-mahima-b19` | **प्रभु श्री राम राज्याभिषेक एवं रामराज्य स्थापना कथा (एकोनविंशति अवध कथा 19)** | 🎬 Video | [`jNc2IXcy_R4`](https://www.youtube.com/watch?v=jNc2IXcy_R4) | `NULL` | [`jNc2IXcy_R4`](https://www.youtube.com/watch?v=jNc2IXcy_R4) | ✅ **`SAFE_TO_APPLY`** |
| 48 | `b2-katha-bhakta-raja-shivi-kapot-raksha` | **राजा शिवि की कपोत (कबूतर) रक्षा: अपने मांस का तराजू दान** | 🎬 Video | [`8im9PWCxHKc`](https://www.youtube.com/watch?v=8im9PWCxHKc) | `NULL` | [`8im9PWCxHKc`](https://www.youtube.com/watch?v=8im9PWCxHKc) | ✅ **`SAFE_TO_APPLY`** |
| 49 | `b2-katha-krishna-sudama-charitra-tandul` | **सुदामा चरित्र: तीन मुट्ठी चावल पर तीनों लोक अर्पण** | 🎬 Video | [`VJDGX47hFsE`](https://www.youtube.com/watch?v=VJDGX47hFsE) | `NULL` | [`VJDGX47hFsE`](https://www.youtube.com/watch?v=VJDGX47hFsE) | ✅ **`SAFE_TO_APPLY`** |
| 50 | `b2-katha-ram-dhanush-bhanga-parashuram` | **शिव धनुष भंग एवं श्री परशुराम-लक्ष्मण संवाद** | 🎬 Video | [`DTS68H8OV9I`](https://www.youtube.com/watch?v=DTS68H8OV9I) | `NULL` | [`DTS68H8OV9I`](https://www.youtube.com/watch?v=DTS68H8OV9I) | ✅ **`SAFE_TO_APPLY`** |
| 51 | `b2-katha-ram-janakpur-pushpa-vatika` | **जनकपुर पुष्प वाटिका एवं श्री सीता-राम प्रथम मिलन** | 🎬 Video | [`fSCCYtaFu9c`](https://www.youtube.com/watch?v=fSCCYtaFu9c) | `NULL` | [`fSCCYtaFu9c`](https://www.youtube.com/watch?v=fSCCYtaFu9c) | ✅ **`SAFE_TO_APPLY`** |
| 52 | `b2-katha-shiva-gangadhar-neelkantha` | **गंगाधर एवं नीलकंठ प्राकट्य: समुद्र मंथन हलाहल पान** | 🎬 Video | [`BgQnxSBORXk`](https://www.youtube.com/watch?v=BgQnxSBORXk) | `NULL` | [`BgQnxSBORXk`](https://www.youtube.com/watch?v=BgQnxSBORXk) | ✅ **`SAFE_TO_APPLY`** |
| 53 | `b2-katha-shiva-tripurasur-vadh-devadhidev` | **त्रिपुरासुर वध एवं महादेव 'त्रिपुरारि' प्राकट्य** | 🎬 Video | [`MLjlK2bH3y8`](https://www.youtube.com/watch?v=MLjlK2bH3y8) | `NULL` | [`MLjlK2bH3y8`](https://www.youtube.com/watch?v=MLjlK2bH3y8) | ✅ **`SAFE_TO_APPLY`** |
| 54 | `b20-ganesh-katha-b20-338` | **भगवान गणेश दिव्य चरित्र स्तुति संकीर्तन (विंशति पद 338 - 20)** | 🎬 Video | [`8Uq-A__M3DA`](https://www.youtube.com/watch?v=8Uq-A__M3DA) | `NULL` | [`8Uq-A__M3DA`](https://www.youtube.com/watch?v=8Uq-A__M3DA) | ✅ **`SAFE_TO_APPLY`** |
| 55 | `b20-saraswati-katha-b20-077` | **मां सरस्वती लीला प्रसंग स्तुति संकीर्तन (विंशति पद 077 - 20)** | 🎬 Video | [`IERZqWu_BfQ`](https://www.youtube.com/watch?v=IERZqWu_BfQ) | `NULL` | [`IERZqWu_BfQ`](https://www.youtube.com/watch?v=IERZqWu_BfQ) | ✅ **`SAFE_TO_APPLY`** |
| 56 | `b20-saraswati-katha-b20-137` | **मां सरस्वती लीला प्रसंग स्तुति संकीर्तन (विंशति पद 137 - 20)** | 🎬 Video | [`yMjZfepQ84s`](https://www.youtube.com/watch?v=yMjZfepQ84s) | `NULL` | [`yMjZfepQ84s`](https://www.youtube.com/watch?v=yMjZfepQ84s) | ✅ **`SAFE_TO_APPLY`** |
| 57 | `b20-saraswati-katha-b20-197` | **मां सरस्वती लीला प्रसंग स्तुति संकीर्तन (विंशति पद 197 - 20)** | 🎬 Video | [`u3D7aEXsV3c`](https://www.youtube.com/watch?v=u3D7aEXsV3c) | `NULL` | [`u3D7aEXsV3c`](https://www.youtube.com/watch?v=u3D7aEXsV3c) | ✅ **`SAFE_TO_APPLY`** |
| 58 | `b3-katha-ram-dhanush-yajna-sita-swayamvar` | **जनकपुर में धनुष भंग एवं श्री सीता-राम विवाह महोत्सव** | 🎬 Video | [`POLUFVO0R8I`](https://www.youtube.com/watch?v=POLUFVO0R8I) | `NULL` | [`POLUFVO0R8I`](https://www.youtube.com/watch?v=POLUFVO0R8I) | ✅ **`SAFE_TO_APPLY`** |
| 59 | `b3-katha-ram-kaikeyi-varadan-vanvaas-prasang` | **मंथरा कुटिलता, कैकेयी के दो वरदान एवं राम वनवास** | 🎬 Video | [`5F0RDjJJOTo`](https://www.youtube.com/watch?v=5F0RDjJJOTo) | `NULL` | [`5F0RDjJJOTo`](https://www.youtube.com/watch?v=5F0RDjJJOTo) | ✅ **`SAFE_TO_APPLY`** |
| 60 | `b3-katha-ram-putreshti-yajna-ram-janma` | **राजा दशरथ का पुत्रेष्टि यज्ञ एवं श्री राम प्राकट्य कथा** | 🎬 Video | [`mz6Gx9f0wS0`](https://www.youtube.com/watch?v=mz6Gx9f0wS0) | `NULL` | [`mz6Gx9f0wS0`](https://www.youtube.com/watch?v=mz6Gx9f0wS0) | ✅ **`SAFE_TO_APPLY`** |
| 61 | `b3-katha-shiva-sati-daha-daksha-yajna-destructive-tandav` | **दक्ष प्रजापति का यज्ञ, सती देह त्याग एवं वीरभद्र तांडव** | 🎬 Video | [`nO-HmY0Qc1E`](https://www.youtube.com/watch?v=nO-HmY0Qc1E) | `NULL` | [`nO-HmY0Qc1E`](https://www.youtube.com/watch?v=nO-HmY0Qc1E) | ✅ **`SAFE_TO_APPLY`** |
| 62 | `b3-katha-shiva-tripurasur-vadh-meru-dhanush` | **त्रिपुरासुर वध हेतु पृथ्वी को रथ और मेरु को धनुष बनाना** | 🎬 Video | [`PRiJYSc2psM`](https://www.youtube.com/watch?v=PRiJYSc2psM) | `NULL` | [`PRiJYSc2psM`](https://www.youtube.com/watch?v=PRiJYSc2psM) | ✅ **`SAFE_TO_APPLY`** |
| 63 | `b4-katha-ganesh-ekadanta-parashuram-katha` | **एकदंत स्वरूप की कथा (परशुराम जी के फरसे का सम्मान)** | 🎬 Video | [`N-pvEtGyHFo`](https://www.youtube.com/watch?v=N-pvEtGyHFo) | `NULL` | [`N-pvEtGyHFo`](https://www.youtube.com/watch?v=N-pvEtGyHFo) | ✅ **`SAFE_TO_APPLY`** |
| 64 | `b4-katha-ganesh-parikrama-katha-pratham-poojya` | **माता-पिता की परिक्रमा एवं गणेश जी का प्रथम पूज्य बनना** | 🎬 Video | [`nAudWZ6a7aY`](https://www.youtube.com/watch?v=nAudWZ6a7aY) | `NULL` | [`nAudWZ6a7aY`](https://www.youtube.com/watch?v=nAudWZ6a7aY) | ✅ **`SAFE_TO_APPLY`** |
| 65 | `b4-katha-guru_sant-kabir-aur-ram-naam-diksha` | **संत कबीर और स्वामी रामानंद से पंचगंगा घाट पर राम नाम दीक्षा** | 🎬 Video | [`q0Zgp6XwTl4`](https://www.youtube.com/watch?v=q0Zgp6XwTl4) | `NULL` | [`q0Zgp6XwTl4`](https://www.youtube.com/watch?v=q0Zgp6XwTl4) | ✅ **`SAFE_TO_APPLY`** |
| 66 | `b4-katha-krishna-sudama-prem-bhent-leela` | **भक्त सुदामा की चावल पोटली एवं द्वारकाधीश का प्रेम** | 🎬 Video | [`mF65JqAJbRQ`](https://www.youtube.com/watch?v=mF65JqAJbRQ) | `NULL` | [`mF65JqAJbRQ`](https://www.youtube.com/watch?v=mF65JqAJbRQ) | ✅ **`SAFE_TO_APPLY`** |
| 67 | `b4-katha-ram-dhanush-yagya-aur-parashuram-samvad` | **जनकपुर धनुष भंग एवं श्री परशुराम-लक्ष्मण संवाद** | 🎬 Video | [`t1T8Wt6PjcI`](https://www.youtube.com/watch?v=t1T8Wt6PjcI) | `NULL` | [`t1T8Wt6PjcI`](https://www.youtube.com/watch?v=t1T8Wt6PjcI) | ✅ **`SAFE_TO_APPLY`** |
| 68 | `b4-katha-ram-jayant-katha-kripalu-shri-ram` | **जयंत का अपराध एवं कृपालु श्री राम द्वारा क्षमादान** | 🎬 Video | [`FIYtOLIr-b0`](https://www.youtube.com/watch?v=FIYtOLIr-b0) | `NULL` | [`FIYtOLIr-b0`](https://www.youtube.com/watch?v=FIYtOLIr-b0) | ✅ **`SAFE_TO_APPLY`** |
| 69 | `b4-katha-ram-setu-bandhan-nal-neel-leela` | **नल-नील द्वारा सेतु बंधन एवं राम नाम पत्थरों का तैरना** | 🎬 Video | [`q4Yknykqw_k`](https://www.youtube.com/watch?v=q4Yknykqw_k) | `NULL` | [`q4Yknykqw_k`](https://www.youtube.com/watch?v=q4Yknykqw_k) | ✅ **`SAFE_TO_APPLY`** |
| 70 | `b4-katha-shiva-kashi-mahima-aur-manikarnika` | **काशी की उत्पत्ति, पंचक्रोशी परिक्रमा एवं मणिकर्णिका घाट** | 🎬 Video | [`yPdoC8K8Dp4`](https://www.youtube.com/watch?v=yPdoC8K8Dp4) | `NULL` | [`yPdoC8K8Dp4`](https://www.youtube.com/watch?v=yPdoC8K8Dp4) | ✅ **`SAFE_TO_APPLY`** |
| 71 | `b4-katha-shiva-tripurasur-vadh-katha` | **त्रिपुरासुर वध एवं महादेव का त्रिपुरारी नामकरण** | 🎬 Video | [`hRqvxFbe2tE`](https://www.youtube.com/watch?v=hRqvxFbe2tE) | `NULL` | [`hRqvxFbe2tE`](https://www.youtube.com/watch?v=hRqvxFbe2tE) | ✅ **`SAFE_TO_APPLY`** |
| 72 | `b5-katha-ganesh-pratham-pujya-parikrama-katha` | **गणेश जी की प्रथम पूजा: माता-पिता की परिक्रमा से ब्रह्मांड विजय** | 🎬 Video | [`sFT-l8z76qs`](https://www.youtube.com/watch?v=sFT-l8z76qs) | `NULL` | [`sFT-l8z76qs`](https://www.youtube.com/watch?v=sFT-l8z76qs) | ✅ **`SAFE_TO_APPLY`** |
| 73 | `b5-katha-krishna-draupadi-cheer-haran-raksha` | **द्रौपदी चीर हरण: कौरव सभा में अक्षय वस्त्र अवतार** | 🎬 Video | [`rV274hcQAZI`](https://www.youtube.com/watch?v=rV274hcQAZI) | `NULL` | [`rV274hcQAZI`](https://www.youtube.com/watch?v=rV274hcQAZI) | ✅ **`SAFE_TO_APPLY`** |
| 74 | `b5-katha-ram-vibhishan-sharanagati-abhay-dan` | **विभीषण शरणागति: रावण त्याग और श्री राम द्वारा लंकापति पद दान** | 🎬 Video | [`QlrDpHf3cVY`](https://www.youtube.com/watch?v=QlrDpHf3cVY) | `NULL` | [`QlrDpHf3cVY`](https://www.youtube.com/watch?v=QlrDpHf3cVY) | ✅ **`SAFE_TO_APPLY`** |
| 75 | `b5-katha-shiva-sati-deha-tyaga-daksha-yagya` | **दक्ष प्रजापति यज्ञ विध्वंस एवं माता सती का देह त्याग** | 🎬 Video | [`Wjv9_8snplU`](https://www.youtube.com/watch?v=Wjv9_8snplU) | `NULL` | [`Wjv9_8snplU`](https://www.youtube.com/watch?v=Wjv9_8snplU) | ✅ **`SAFE_TO_APPLY`** |
| 76 | `b5-katha-shiva-tripurasura-vadh-prithvi-ratha` | **त्रिपुरासुर वध: पृथ्वी का रथ और मेरु का धनुष बनाकर संहार** | 🎬 Video | [`rm_i9CQfMiY`](https://www.youtube.com/watch?v=rm_i9CQfMiY) | `NULL` | [`rm_i9CQfMiY`](https://www.youtube.com/watch?v=rm_i9CQfMiY) | ✅ **`SAFE_TO_APPLY`** |
| 77 | `b6-katha-ram-agastya-muni-divyastra-dhanush-dan-b6` | **अगस्त्य मुनि मिलन: श्री राम को वैष्णव धनुष एवं अक्षय तरकश दान** | 🎬 Video | [`9NyGUcgjlIg`](https://www.youtube.com/watch?v=9NyGUcgjlIg) | `NULL` | [`9NyGUcgjlIg`](https://www.youtube.com/watch?v=9NyGUcgjlIg) | ✅ **`SAFE_TO_APPLY`** |
| 78 | `b6-katha-ram-ahiravan-patal-prasang-hanuman-b6` | **अहिरावण पाताल प्रसंग: पाताल लोक में हनुमान जी द्वारा राम-लक्ष्मण मुक्ति** | 🎬 Video | [`veuZOU2xPe4`](https://www.youtube.com/watch?v=veuZOU2xPe4) | `NULL` | [`veuZOU2xPe4`](https://www.youtube.com/watch?v=veuZOU2xPe4) | ✅ **`SAFE_TO_APPLY`** |
| 79 | `b6-katha-ram-bharat-charitra-chitrakoot-b6` | **श्री भरत चरित्र: चित्रकूट में पादुका ग्रहण एवं नन्दिग्राम तपस्या** | 🎬 Video | [`pF3hCLELuqI`](https://www.youtube.com/watch?v=pF3hCLELuqI) | `NULL` | [`pF3hCLELuqI`](https://www.youtube.com/watch?v=pF3hCLELuqI) | ✅ **`SAFE_TO_APPLY`** |
| 80 | `b6-katha-ram-kakbhusundi-ram-charitra-katha-b6` | **काकभुशुण्डि जी द्वारा गरुड़ जी को सुनाई गई अमर रामकथा** | 🎬 Video | [`RYlRRzmQ-P0`](https://www.youtube.com/watch?v=RYlRRzmQ-P0) | `NULL` | [`RYlRRzmQ-P0`](https://www.youtube.com/watch?v=RYlRRzmQ-P0) | ✅ **`SAFE_TO_APPLY`** |
| 81 | `b6-katha-ram-mandodari-ravan-hitopadesh-b6` | **महारानी मंदोदरी का रावण को हितोपदेश: 'कंत राम बिरोध परिहरहू'** | 🎬 Video | [`qV5dBSRZrSU`](https://www.youtube.com/watch?v=qV5dBSRZrSU) | `NULL` | [`qV5dBSRZrSU`](https://www.youtube.com/watch?v=qV5dBSRZrSU) | ✅ **`SAFE_TO_APPLY`** |
| 82 | `b9-katha-krishna-draupadi-cheer-haran-raksha-b9` | **द्रौपदी चीर हरण: 'हे गोविंद राखो लाज हमारी' और चीर का अखंड विस्तार** | 🎬 Video | [`Hj0BLyIVUfM`](https://www.youtube.com/watch?v=Hj0BLyIVUfM) | `NULL` | [`Hj0BLyIVUfM`](https://www.youtube.com/watch?v=Hj0BLyIVUfM) | ✅ **`SAFE_TO_APPLY`** |
| 83 | `b9-katha-krishna-sudama-charitra-prem-b9` | **सुदामा चरित्र: चार मुट्ठी तंदुल (चावल) और दो लोकों का ऐश्वर्य दान** | 🎬 Video | [`rAGHtr3VE8I`](https://www.youtube.com/watch?v=rAGHtr3VE8I) | `NULL` | [`rAGHtr3VE8I`](https://www.youtube.com/watch?v=rAGHtr3VE8I) | ✅ **`SAFE_TO_APPLY`** |

---

## 4. 🔒 FINAL RESULT & SAFETY GATE

```
PHASE 2M-D FINAL DRY RUN COMPLETE

Database Modified       : NO
Database Writes         : 0

Source VERIFIED_HIGH Audio : 44
Source VERIFIED_HIGH Video : 39
Source VERIFIED_HIGH Total : 83

Revalidated Audio       : 44
Revalidated Video       : 39

Still Eligible Audio    : 44
Still Eligible Video    : 39

Already Covered         : 0
Blocked / Revalidation  : 0

Duplicate IDs           : 0
Duplicate URLs          : 0
Conflicts               : 0
Cross-Field Conflicts   : 0
Overwrite Attempts      : 0

Proposed Audio Adds     : 44
Proposed Video Adds     : 39
Proposed Total Adds     : 83

Current Playable Audio  : 240
Current YouTube Audio   : 202
Current Video URLs      : 109

Projected Playable Audio : 284
Projected YouTube Audio   : 246
Projected Video URLs      : 148

Total Katha             : 505
Current Katha With Audio   : 179
Current Katha With Video   : 107
Current Katha With Both    : 98
Current Katha With Neither : 317

Projected Katha With Audio   : 223
Projected Katha With Video   : 146
Projected Katha With Both    : 135
Projected Katha Neither : 271

Integrity Check         : ok
Foreign-Key Violations  : 0

Final Gate              : PASS

IMPORTANT:
No media was applied to the database during Phase 2M-D.

The Proposed Apply Set is DRY-RUN ONLY.

PHASE 2M-E APPLY MUST NOT START
until explicit user approval is received.
```
