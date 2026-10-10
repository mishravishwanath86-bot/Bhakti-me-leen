# 📖🎬 Phase 2Q-D — Final Dry Run & Apply Safety Verification Report

**Mode**: `STRICT READ-ONLY — FINAL DRY RUN ONLY` (Zero Database Writes)  
**Database File**: `db/bhakti.db` (Unchanged, 0 Writes)  
**Date**: `2026-08-31 16:18:16`  
**Safety Gate**: **`PASS`**  

---

## 1. 🛡️ Current Database Baseline vs. Projected Post-Apply State

| Metric | Current Real Baseline | Projected Post-Apply | Status |
| :--- | :--- | :--- | :--- |
| **Total Database Records** | **`10,010`** | `10,010` | ✅ Unchanged |
| **FTS5 Search Documents** | **`10,010`** | `10,010` | ✅ Unchanged |
| **Playable Audio Total** | **`370`** | **`394`** (+24) | 🎯 Audio Expansion |
| **Local MP3 Audio** | **`38`** | `38` | ✅ Untouched |
| **YouTube HD Audio** | **`332`** | **`356`** (+24) | 🎧 +24 Verified Spoken Kathas |
| **YouTube Video URLs** | **`203`** | **`226`** (+23) | 🎬 +23 Verified Video Discourses |
| **PRAGMA integrity_check** | **`ok`** | `ok` | ✅ 0 Corruption |
| **Foreign-Key Violations** | **`0`** | `0` | ✅ 100% Valid |
| **Real Database Writes** | **`0`** | `0` | ✅ Zero Writes (Dry Run Only) |

---

## 2. 📖 Projected Katha Coverage Evolution Across All 505 Records

| Katha Category Metric | Current State | Projected Post-Apply | Change |
| :--- | :---: | :---: | :---: |
| **Katha With Audio** | `309` | **`333`** | +24 |
| **Katha With Video** | `201` | **`224`** | +23 |
| **Katha With Both Media** | `180` | **`200`** | +20 |
| **Katha With Neither Media (Gaps)** | `175` | **`148`** | -27 |

* **Projected Disjoint Partition**: Both (`200`) + Audio Only (`133`) + Video Only (`24`) + Neither (`148`) = **`505`**

---

## 3. 📋 47 Candidate Safety Revalidation Matrix

| # | Database Record ID | Katha Title | Media Type | YouTube Video ID | Current Value | Proposed Value | Safety Verdict |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :---: |
| 01 | `b17-katha-purana-prerak-dhara-12-b17` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 12 (सप्तदश प्रसंग 17)** | 🎧 Audio | [`A2Tj6-kWtow`](https://www.youtube.com/watch?v=A2Tj6-kWtow) | `NULL` | [`A2Tj6-kWtow`](https://www.youtube.com/watch?v=A2Tj6-kWtow) | ✅ **`APPLY_ELIGIBLE`** |
| 02 | `b18-katha-purana-prerak-dhara-10-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 10 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`SpT0XiC5t_s`](https://www.youtube.com/watch?v=SpT0XiC5t_s) | `NULL` | [`SpT0XiC5t_s`](https://www.youtube.com/watch?v=SpT0XiC5t_s) | ✅ **`APPLY_ELIGIBLE`** |
| 03 | `b18-katha-purana-prerak-dhara-14-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 14 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`wPVvx_7jk6A`](https://www.youtube.com/watch?v=wPVvx_7jk6A) | `NULL` | [`wPVvx_7jk6A`](https://www.youtube.com/watch?v=wPVvx_7jk6A) | ✅ **`APPLY_ELIGIBLE`** |
| 04 | `b18-katha-purana-prerak-dhara-15-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 15 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`dZGNnjLF2WE`](https://www.youtube.com/watch?v=dZGNnjLF2WE) | `NULL` | [`dZGNnjLF2WE`](https://www.youtube.com/watch?v=dZGNnjLF2WE) | ✅ **`APPLY_ELIGIBLE`** |
| 05 | `b2-katha-hanuman-dronagiri-parvat-udaran` | **द्रोणागिरि पर्वत उखाड़ना एवं कालनेमि संहार** | 🎧 Audio | [`WofLPYMZ9lA`](https://www.youtube.com/watch?v=WofLPYMZ9lA) | `NULL` | [`WofLPYMZ9lA`](https://www.youtube.com/watch?v=WofLPYMZ9lA) | ✅ **`APPLY_ELIGIBLE`** |
| 06 | `b2-katha-krishna-kalia-naag-daman` | **कालिया नाग दमन लीला (यमुना जल विष मुक्ति)** | 🎧 Audio | [`N2gp8hjFrUw`](https://www.youtube.com/watch?v=N2gp8hjFrUw) | `NULL` | [`N2gp8hjFrUw`](https://www.youtube.com/watch?v=N2gp8hjFrUw) | ✅ **`APPLY_ELIGIBLE`** |
| 07 | `b2-katha-krishna-kansa-vadh-ugrasen-raj` | **कंस वध एवं महाराज उग्रसेन का राज्याभिषेक** | 🎧 Audio | [`_xCW3j2yw2U`](https://www.youtube.com/watch?v=_xCW3j2yw2U) | `NULL` | [`_xCW3j2yw2U`](https://www.youtube.com/watch?v=_xCW3j2yw2U) | ✅ **`APPLY_ELIGIBLE`** |
| 08 | `b2-katha-krishna-makhan-chori-ukhal-bandhan` | **माखन चोरी एवं यमलार्जुन मोक्ष (ऊखल बंधन लीला)** | 🎧 Audio | [`GT4TiqTUgyg`](https://www.youtube.com/watch?v=GT4TiqTUgyg) | `NULL` | [`GT4TiqTUgyg`](https://www.youtube.com/watch?v=GT4TiqTUgyg) | ✅ **`APPLY_ELIGIBLE`** |
| 09 | `b2-katha-krishna-putana-moksha-leela` | **पूतना मोक्ष लीला: विषपान कराने वाली राक्षसी को मातृगति** | 🎧 Audio | [`gnc4KAveHzU`](https://www.youtube.com/watch?v=gnc4KAveHzU) | `NULL` | [`gnc4KAveHzU`](https://www.youtube.com/watch?v=gnc4KAveHzU) | ✅ **`APPLY_ELIGIBLE`** |
| 10 | `b2-katha-pauranik-chandra-shapa-somnath` | **चंद्रमा का क्षय रोग एवं सोमनाथ ज्योतिर्लिंग प्राकट्य** | 🎧 Audio | [`CnM0YeJr7hc`](https://www.youtube.com/watch?v=CnM0YeJr7hc) | `NULL` | [`CnM0YeJr7hc`](https://www.youtube.com/watch?v=CnM0YeJr7hc) | ✅ **`APPLY_ELIGIBLE`** |
| 11 | `b2-katha-shiva-andhakasur-vadh` | **अंधकासुर वध एवं मातृकाओं का प्राकट्य** | 🎧 Audio | [`U4G4Ec5D9BY`](https://www.youtube.com/watch?v=U4G4Ec5D9BY) | `NULL` | [`U4G4Ec5D9BY`](https://www.youtube.com/watch?v=U4G4Ec5D9BY) | ✅ **`APPLY_ELIGIBLE`** |
| 12 | `b2-katha-shiva-bhasmasur-mohini-lila` | **भस्मासुर मोहिनी प्रसंग: अहंकार का स्वतः विनाश** | 🎧 Audio | [`jBspv5RiB8I`](https://www.youtube.com/watch?v=jBspv5RiB8I) | `NULL` | [`jBspv5RiB8I`](https://www.youtube.com/watch?v=jBspv5RiB8I) | ✅ **`APPLY_ELIGIBLE`** |
| 13 | `b3-katha-hanuman-ahiravan-vadh-patal-vijay-b3` | **पाताल लोक में अहिरावण वध एवं मकरध्वज से पावन मिलन** | 🎧 Audio | [`evUvGGHz0rU`](https://www.youtube.com/watch?v=evUvGGHz0rU) | `NULL` | [`evUvGGHz0rU`](https://www.youtube.com/watch?v=evUvGGHz0rU) | ✅ **`APPLY_ELIGIBLE`** |
| 14 | `b3-katha-hanuman-sanjivani-parvat-drona-uthana` | **लक्ष्मण शक्ति बाण मूर्छा एवं द्रोणागिरि पर्वत संजीवनी लाना** | 🎧 Audio | [`_-MWuyxXp70`](https://www.youtube.com/watch?v=_-MWuyxXp70) | `NULL` | [`_-MWuyxXp70`](https://www.youtube.com/watch?v=_-MWuyxXp70) | ✅ **`APPLY_ELIGIBLE`** |
| 15 | `b3-katha-krishna-dwarka-nagari-samudra-nirman` | **विश्वकर्मा द्वारा समुद्र मध्य स्वर्णमयी द्वारका निर्माण** | 🎧 Audio | [`vMLYv2hHMkI`](https://www.youtube.com/watch?v=vMLYv2hHMkI) | `NULL` | [`vMLYv2hHMkI`](https://www.youtube.com/watch?v=vMLYv2hHMkI) | ✅ **`APPLY_ELIGIBLE`** |
| 16 | `b3-katha-krishna-kansa-vadh-mathura-vijay` | **धनुष यज्ञ, कुवलयापीड-चाणूर वध एवं कंस वध कथा** | 🎧 Audio | [`GWFRV1I2OZ8`](https://www.youtube.com/watch?v=GWFRV1I2OZ8) | `NULL` | [`GWFRV1I2OZ8`](https://www.youtube.com/watch?v=GWFRV1I2OZ8) | ✅ **`APPLY_ELIGIBLE`** |
| 17 | `b3-katha-krishna-maha-raas-leela-sharad-purnima` | **शरद पूर्णिमा महारास लीला एवं जीवात्मा-परमात्मा मिलन** | 🎧 Audio | [`F-oTu5dyWVU`](https://www.youtube.com/watch?v=F-oTu5dyWVU) | `NULL` | [`F-oTu5dyWVU`](https://www.youtube.com/watch?v=F-oTu5dyWVU) | ✅ **`APPLY_ELIGIBLE`** |
| 18 | `b3-katha-krishna-shishupal-vadh-sudarshana-chakra` | **राजसूय यज्ञ में शिशुपाल के 100 अपराध क्षमा व सुदर्शन चक्र वध** | 🎧 Audio | [`QmYsSkTmPPM`](https://www.youtube.com/watch?v=QmYsSkTmPPM) | `NULL` | [`QmYsSkTmPPM`](https://www.youtube.com/watch?v=QmYsSkTmPPM) | ✅ **`APPLY_ELIGIBLE`** |
| 19 | `b3-katha-krishna-yamalarjuna-bhanjan-damodar` | **ऊखल बंधन एवं यमलार्जुन वृक्षों का दिव्य उद्धार** | 🎧 Audio | [`02hdezOLbq8`](https://www.youtube.com/watch?v=02hdezOLbq8) | `NULL` | [`02hdezOLbq8`](https://www.youtube.com/watch?v=02hdezOLbq8) | ✅ **`APPLY_ELIGIBLE`** |
| 20 | `b3-katha-shiva-samudra-manthan-neelkanth-mahadev` | **समुद्र मंथन में हलाहल विष पान एवं नीलकंठ महादेव** | 🎧 Audio | [`KMhclpkgEbI`](https://www.youtube.com/watch?v=KMhclpkgEbI) | `NULL` | [`KMhclpkgEbI`](https://www.youtube.com/watch?v=KMhclpkgEbI) | ✅ **`APPLY_ELIGIBLE`** |
| 21 | `b4-katha-krishna-kalia-mardan-yamuna-tat` | **कालिया नाग दमन एवं यमुना जी का पावन विष-मुक्ति प्रसंग** | 🎧 Audio | [`yndLpHTYW8g`](https://www.youtube.com/watch?v=yndLpHTYW8g) | `NULL` | [`yndLpHTYW8g`](https://www.youtube.com/watch?v=yndLpHTYW8g) | ✅ **`APPLY_ELIGIBLE`** |
| 22 | `b4-katha-krishna-kansa-vadh-mathura-leela` | **मथुरा आगमन, कुब्जा उद्धार, धनुषभंग एवं कंस वध** | 🎧 Audio | [`bgp6JV8Popc`](https://www.youtube.com/watch?v=bgp6JV8Popc) | `NULL` | [`bgp6JV8Popc`](https://www.youtube.com/watch?v=bgp6JV8Popc) | ✅ **`APPLY_ELIGIBLE`** |
| 23 | `b4-katha-krishna-rasa-lila-sharad-purnima` | **शरद पूर्णिमा महारास लीला एवं वंशीवट का दिव्य नृत्य** | 🎧 Audio | [`u_kJeqVGI9U`](https://www.youtube.com/watch?v=u_kJeqVGI9U) | `NULL` | [`u_kJeqVGI9U`](https://www.youtube.com/watch?v=u_kJeqVGI9U) | ✅ **`APPLY_ELIGIBLE`** |
| 24 | `b4-katha-shiva-samudra-manthan-neelkanth-katha` | **समुद्र मंथन, कालकूट हलाहल विष एवं नीलकंठ महादेव** | 🎧 Audio | [`TDGTDJpY4AA`](https://www.youtube.com/watch?v=TDGTDJpY4AA) | `NULL` | [`TDGTDJpY4AA`](https://www.youtube.com/watch?v=TDGTDJpY4AA) | ✅ **`APPLY_ELIGIBLE`** |
| 25 | `b14-katha-purana-prerak-dhara-04-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 04 (अमृत प्रसंग 14)** | 🎬 Video | [`8csU19A_sYQ`](https://www.youtube.com/watch?v=8csU19A_sYQ) | `NULL` | [`8csU19A_sYQ`](https://www.youtube.com/watch?v=8csU19A_sYQ) | ✅ **`APPLY_ELIGIBLE`** |
| 26 | `b15-katha-purana-prerak-dhara-09-b15` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (अमृत प्रसंग 15)** | 🎬 Video | [`q6MhIzOi600`](https://www.youtube.com/watch?v=q6MhIzOi600) | `NULL` | [`q6MhIzOi600`](https://www.youtube.com/watch?v=q6MhIzOi600) | ✅ **`APPLY_ELIGIBLE`** |
| 27 | `b2-katha-hanuman-dronagiri-parvat-udaran` | **द्रोणागिरि पर्वत उखाड़ना एवं कालनेमि संहार** | 🎬 Video | [`MYAq8xAimfA`](https://www.youtube.com/watch?v=MYAq8xAimfA) | `NULL` | [`MYAq8xAimfA`](https://www.youtube.com/watch?v=MYAq8xAimfA) | ✅ **`APPLY_ELIGIBLE`** |
| 28 | `b2-katha-krishna-kalia-naag-daman` | **कालिया नाग दमन लीला (यमुना जल विष मुक्ति)** | 🎬 Video | [`g2QPLSqKkU4`](https://www.youtube.com/watch?v=g2QPLSqKkU4) | `NULL` | [`g2QPLSqKkU4`](https://www.youtube.com/watch?v=g2QPLSqKkU4) | ✅ **`APPLY_ELIGIBLE`** |
| 29 | `b2-katha-krishna-kansa-vadh-ugrasen-raj` | **कंस वध एवं महाराज उग्रसेन का राज्याभिषेक** | 🎬 Video | [`AsFCiuB_flE`](https://www.youtube.com/watch?v=AsFCiuB_flE) | `NULL` | [`AsFCiuB_flE`](https://www.youtube.com/watch?v=AsFCiuB_flE) | ✅ **`APPLY_ELIGIBLE`** |
| 30 | `b2-katha-krishna-makhan-chori-ukhal-bandhan` | **माखन चोरी एवं यमलार्जुन मोक्ष (ऊखल बंधन लीला)** | 🎬 Video | [`O4D0By8ykgk`](https://www.youtube.com/watch?v=O4D0By8ykgk) | `NULL` | [`O4D0By8ykgk`](https://www.youtube.com/watch?v=O4D0By8ykgk) | ✅ **`APPLY_ELIGIBLE`** |
| 31 | `b2-katha-krishna-putana-moksha-leela` | **पूतना मोक्ष लीला: विषपान कराने वाली राक्षसी को मातृगति** | 🎬 Video | [`Xp3LoRFMAoI`](https://www.youtube.com/watch?v=Xp3LoRFMAoI) | `NULL` | [`Xp3LoRFMAoI`](https://www.youtube.com/watch?v=Xp3LoRFMAoI) | ✅ **`APPLY_ELIGIBLE`** |
| 32 | `b2-katha-pauranik-chandra-shapa-somnath` | **चंद्रमा का क्षय रोग एवं सोमनाथ ज्योतिर्लिंग प्राकट्य** | 🎬 Video | [`bjUGeCA_4tM`](https://www.youtube.com/watch?v=bjUGeCA_4tM) | `NULL` | [`bjUGeCA_4tM`](https://www.youtube.com/watch?v=bjUGeCA_4tM) | ✅ **`APPLY_ELIGIBLE`** |
| 33 | `b2-katha-shiva-andhakasur-vadh` | **अंधकासुर वध एवं मातृकाओं का प्राकट्य** | 🎬 Video | [`Y12c1RQZ36Y`](https://www.youtube.com/watch?v=Y12c1RQZ36Y) | `NULL` | [`Y12c1RQZ36Y`](https://www.youtube.com/watch?v=Y12c1RQZ36Y) | ✅ **`APPLY_ELIGIBLE`** |
| 34 | `b2-katha-shiva-bhasmasur-mohini-lila` | **भस्मासुर मोहिनी प्रसंग: अहंकार का स्वतः विनाश** | 🎬 Video | [`NYfFlghyz_M`](https://www.youtube.com/watch?v=NYfFlghyz_M) | `NULL` | [`NYfFlghyz_M`](https://www.youtube.com/watch?v=NYfFlghyz_M) | ✅ **`APPLY_ELIGIBLE`** |
| 35 | `b3-katha-hanuman-ahiravan-vadh-patal-vijay-b3` | **पाताल लोक में अहिरावण वध एवं मकरध्वज से पावन मिलन** | 🎬 Video | [`a77mC7WnWBw`](https://www.youtube.com/watch?v=a77mC7WnWBw) | `NULL` | [`a77mC7WnWBw`](https://www.youtube.com/watch?v=a77mC7WnWBw) | ✅ **`APPLY_ELIGIBLE`** |
| 36 | `b3-katha-hanuman-sanjivani-parvat-drona-uthana` | **लक्ष्मण शक्ति बाण मूर्छा एवं द्रोणागिरि पर्वत संजीवनी लाना** | 🎬 Video | [`bYsnpcq8MZc`](https://www.youtube.com/watch?v=bYsnpcq8MZc) | `NULL` | [`bYsnpcq8MZc`](https://www.youtube.com/watch?v=bYsnpcq8MZc) | ✅ **`APPLY_ELIGIBLE`** |
| 37 | `b3-katha-hanuman-surya-gras-balpan-leela` | **बाल्यकाल में सूर्य को फल समझकर मुख में रखना एवं देव वरदान** | 🎬 Video | [`KdXBxre5K4Q`](https://www.youtube.com/watch?v=KdXBxre5K4Q) | `NULL` | [`KdXBxre5K4Q`](https://www.youtube.com/watch?v=KdXBxre5K4Q) | ✅ **`APPLY_ELIGIBLE`** |
| 38 | `b3-katha-krishna-dwarka-nagari-samudra-nirman` | **विश्वकर्मा द्वारा समुद्र मध्य स्वर्णमयी द्वारका निर्माण** | 🎬 Video | [`uxVHt6YcLzM`](https://www.youtube.com/watch?v=uxVHt6YcLzM) | `NULL` | [`uxVHt6YcLzM`](https://www.youtube.com/watch?v=uxVHt6YcLzM) | ✅ **`APPLY_ELIGIBLE`** |
| 39 | `b3-katha-krishna-kansa-vadh-mathura-vijay` | **धनुष यज्ञ, कुवलयापीड-चाणूर वध एवं कंस वध कथा** | 🎬 Video | [`VQ6uwmjotA0`](https://www.youtube.com/watch?v=VQ6uwmjotA0) | `NULL` | [`VQ6uwmjotA0`](https://www.youtube.com/watch?v=VQ6uwmjotA0) | ✅ **`APPLY_ELIGIBLE`** |
| 40 | `b3-katha-krishna-maha-raas-leela-sharad-purnima` | **शरद पूर्णिमा महारास लीला एवं जीवात्मा-परमात्मा मिलन** | 🎬 Video | [`IROCnRKIc3E`](https://www.youtube.com/watch?v=IROCnRKIc3E) | `NULL` | [`IROCnRKIc3E`](https://www.youtube.com/watch?v=IROCnRKIc3E) | ✅ **`APPLY_ELIGIBLE`** |
| 41 | `b3-katha-krishna-shishupal-vadh-sudarshana-chakra` | **राजसूय यज्ञ में शिशुपाल के 100 अपराध क्षमा व सुदर्शन चक्र वध** | 🎬 Video | [`1nc43PdrxdQ`](https://www.youtube.com/watch?v=1nc43PdrxdQ) | `NULL` | [`1nc43PdrxdQ`](https://www.youtube.com/watch?v=1nc43PdrxdQ) | ✅ **`APPLY_ELIGIBLE`** |
| 42 | `b3-katha-krishna-yamalarjuna-bhanjan-damodar` | **ऊखल बंधन एवं यमलार्जुन वृक्षों का दिव्य उद्धार** | 🎬 Video | [`dC-J2EtzlJM`](https://www.youtube.com/watch?v=dC-J2EtzlJM) | `NULL` | [`dC-J2EtzlJM`](https://www.youtube.com/watch?v=dC-J2EtzlJM) | ✅ **`APPLY_ELIGIBLE`** |
| 43 | `b3-katha-shiva-samudra-manthan-neelkanth-mahadev` | **समुद्र मंथन में हलाहल विष पान एवं नीलकंठ महादेव** | 🎬 Video | [`Ws4BKCsh-Q4`](https://www.youtube.com/watch?v=Ws4BKCsh-Q4) | `NULL` | [`Ws4BKCsh-Q4`](https://www.youtube.com/watch?v=Ws4BKCsh-Q4) | ✅ **`APPLY_ELIGIBLE`** |
| 44 | `b4-katha-krishna-kalia-mardan-yamuna-tat` | **कालिया नाग दमन एवं यमुना जी का पावन विष-मुक्ति प्रसंग** | 🎬 Video | [`AB2sbXuL9kQ`](https://www.youtube.com/watch?v=AB2sbXuL9kQ) | `NULL` | [`AB2sbXuL9kQ`](https://www.youtube.com/watch?v=AB2sbXuL9kQ) | ✅ **`APPLY_ELIGIBLE`** |
| 45 | `b4-katha-krishna-kansa-vadh-mathura-leela` | **मथुरा आगमन, कुब्जा उद्धार, धनुषभंग एवं कंस वध** | 🎬 Video | [`7AoCZv9yCD0`](https://www.youtube.com/watch?v=7AoCZv9yCD0) | `NULL` | [`7AoCZv9yCD0`](https://www.youtube.com/watch?v=7AoCZv9yCD0) | ✅ **`APPLY_ELIGIBLE`** |
| 46 | `b4-katha-krishna-rasa-lila-sharad-purnima` | **शरद पूर्णिमा महारास लीला एवं वंशीवट का दिव्य नृत्य** | 🎬 Video | [`ts-MZ-QGmYs`](https://www.youtube.com/watch?v=ts-MZ-QGmYs) | `NULL` | [`ts-MZ-QGmYs`](https://www.youtube.com/watch?v=ts-MZ-QGmYs) | ✅ **`APPLY_ELIGIBLE`** |
| 47 | `b4-katha-shiva-samudra-manthan-neelkanth-katha` | **समुद्र मंथन, कालकूट हलाहल विष एवं नीलकंठ महादेव** | 🎬 Video | [`yPunxn4BUlM`](https://www.youtube.com/watch?v=yPunxn4BUlM) | `NULL` | [`yPunxn4BUlM`](https://www.youtube.com/watch?v=yPunxn4BUlM) | ✅ **`APPLY_ELIGIBLE`** |

---

## 4. 🔒 FINAL RESULT & SAFETY GATE

```
PHASE 2Q-D FINAL DRY RUN COMPLETE

Database Modified       : NO
Database Writes         : 0

Total Katha             : 505
Media-Less Katha        : 175

Discovery VERIFIED_HIGH Audio : 24
Discovery VERIFIED_HIGH Video : 23
Discovery VERIFIED_HIGH Total : 47

Apply-Eligible Audio    : 24
Apply-Eligible Video    : 23
Apply-Eligible Total    : 47

Blocked Candidates      : 0

Duplicate YouTube IDs   : 0
Duplicate YouTube URLs  : 0
Cross-Field Conflicts   : 0
URL-ID Mismatches       : 0
Malformed URLs          : 0

Overwrite Attempts      : 0
Unauthorized Candidates : 0

Live Verification       : PASS
VERIFIED_HIGH Evidence  : 47/47

Review Candidates Excluded      : 70
Reject Candidates Excluded      : 12
No-Suitable Candidates Excluded : 19

Projected Audio Delta   : +24
Projected Video Delta   : +23
Projected Total Delta   : +47

Projected Katha Reconciliation : PASS

FTS5 Verification       : PASS
Integrity Check         : ok
Foreign-Key Violations  : 0
Schema Audit             : PASS

Final Gate              : PASS

IMPORTANT:
Phase 2Q-D performed no database modifications.

DO NOT automatically start Phase 2Q-E.

STOP AFTER DRY RUN.
```
