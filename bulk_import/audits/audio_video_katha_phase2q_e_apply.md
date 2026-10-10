# 📖🎬 Phase 2Q-E — Verified Media Apply Report

**Apply Mode**: `STRICT VERIFIED APPLY — ONLY PHASE 2Q-D APPROVED MAPPINGS`  
**Database**: `db/bhakti.db`  
**Verified Pre-Apply Backup**: [`db/backups/bhakti_pre_phase2q_e_apply_backup.db`](file:///C:/Users/vishw/.gemini/antigravity-ide/scratch/bhakti-app/db/backups/bhakti_pre_phase2q_e_apply_backup.db)  
**Manifest Source**: [`bulk_import/audits/audio_video_katha_phase2q_d_dry_run.json`](file:///C:/Users/vishw/.gemini/antigravity-ide/scratch/bhakti-app/bulk_import/audits/audio_video_katha_phase2q_d_dry_run.json)  
**Date**: `2026-08-31 16:20:42`  
**Status**: `SUCCESS`  

---

## 1. 🛡️ Database Baseline & Final Verified State

| Metric | Pre-Apply Baseline | Target Expected | Final Verified State | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Total Database Records** | `10,010` | `10,010` | **`10,010`** | ✅ Exact Match |
| **FTS5 Search Documents** | `10,010` | `10,010` | **`10,010`** | ✅ Exact Match |
| **Playable Audio Total** | `370` | `394` (+24) | **`394`** | 🎯 Audio Expansion |
| **Local MP3 Audio** | `38` | `38` | **`38`** | ✅ Untouched |
| **YouTube HD Audio** | `332` | `356` (+24) | **`356`** | 🎧 +24 Verified Spoken Kathas |
| **YouTube Video URLs** | `203` | `226` (+23) | **`226`** | 🎬 +23 Verified Video Discourses |
| **Duplicate YouTube IDs** | `0` | `0` | **`0`** (356/356 Audio, 226/226 Video) | ✅ 100% Collision-Free |
| **PRAGMA integrity_check** | `ok` | `ok` | **`ok`** | ✅ 0 Corruption |
| **Foreign-Key Violations** | `0` | `0` | **`0`** | ✅ 100% Valid |

---

## 2. 📖 Katha Media Coverage State Evolution Across All 505 Records

| Katha Category Metric | Before Phase 2Q-E | After Phase 2Q-E Apply | Change |
| :--- | :---: | :---: | :---: |
| **Katha With Audio** | `309` | **`333`** | +24 |
| **Katha With Video** | `201` | **`224`** | +23 |
| **Katha With Both Media** | `180` | **`200`** | +20 |
| **Katha With Neither Media (Gaps)** | `175` | **`148`** | -27 |

* **Exact Disjoint Partition**: Both (`200`) + Audio Only (`133`) + Video Only (`24`) + Neither (`148`) = **`505`**

---

## 3. 📋 Applied Mappings Sample (47 / 47 PASS)

| # | Database Record ID | Katha Title | Media Type | YouTube Video ID | Applied YouTube URL | Status |
| :---: | :--- | :--- | :---: | :---: | :--- | :---: |
| 01 | `b17-katha-purana-prerak-dhara-12-b17` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 12 (सप्तदश प्रसंग 17)** | 🎧 Audio | [`A2Tj6-kWtow`](https://www.youtube.com/watch?v=A2Tj6-kWtow) | [https://www.youtube.com/watch?v=A2Tj6-kWtow](https://www.youtube.com/watch?v=A2Tj6-kWtow) | ✅ **PASS** |
| 02 | `b18-katha-purana-prerak-dhara-10-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 10 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`SpT0XiC5t_s`](https://www.youtube.com/watch?v=SpT0XiC5t_s) | [https://www.youtube.com/watch?v=SpT0XiC5t_s](https://www.youtube.com/watch?v=SpT0XiC5t_s) | ✅ **PASS** |
| 03 | `b18-katha-purana-prerak-dhara-14-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 14 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`wPVvx_7jk6A`](https://www.youtube.com/watch?v=wPVvx_7jk6A) | [https://www.youtube.com/watch?v=wPVvx_7jk6A](https://www.youtube.com/watch?v=wPVvx_7jk6A) | ✅ **PASS** |
| 04 | `b18-katha-purana-prerak-dhara-15-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 15 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`dZGNnjLF2WE`](https://www.youtube.com/watch?v=dZGNnjLF2WE) | [https://www.youtube.com/watch?v=dZGNnjLF2WE](https://www.youtube.com/watch?v=dZGNnjLF2WE) | ✅ **PASS** |
| 05 | `b2-katha-hanuman-dronagiri-parvat-udaran` | **द्रोणागिरि पर्वत उखाड़ना एवं कालनेमि संहार** | 🎧 Audio | [`WofLPYMZ9lA`](https://www.youtube.com/watch?v=WofLPYMZ9lA) | [https://www.youtube.com/watch?v=WofLPYMZ9lA](https://www.youtube.com/watch?v=WofLPYMZ9lA) | ✅ **PASS** |
| 06 | `b2-katha-krishna-kalia-naag-daman` | **कालिया नाग दमन लीला (यमुना जल विष मुक्ति)** | 🎧 Audio | [`N2gp8hjFrUw`](https://www.youtube.com/watch?v=N2gp8hjFrUw) | [https://www.youtube.com/watch?v=N2gp8hjFrUw](https://www.youtube.com/watch?v=N2gp8hjFrUw) | ✅ **PASS** |
| 07 | `b2-katha-krishna-kansa-vadh-ugrasen-raj` | **कंस वध एवं महाराज उग्रसेन का राज्याभिषेक** | 🎧 Audio | [`_xCW3j2yw2U`](https://www.youtube.com/watch?v=_xCW3j2yw2U) | [https://www.youtube.com/watch?v=_xCW3j2yw2U](https://www.youtube.com/watch?v=_xCW3j2yw2U) | ✅ **PASS** |
| 08 | `b2-katha-krishna-makhan-chori-ukhal-bandhan` | **माखन चोरी एवं यमलार्जुन मोक्ष (ऊखल बंधन लीला)** | 🎧 Audio | [`GT4TiqTUgyg`](https://www.youtube.com/watch?v=GT4TiqTUgyg) | [https://www.youtube.com/watch?v=GT4TiqTUgyg](https://www.youtube.com/watch?v=GT4TiqTUgyg) | ✅ **PASS** |
| 09 | `b2-katha-krishna-putana-moksha-leela` | **पूतना मोक्ष लीला: विषपान कराने वाली राक्षसी को मातृगति** | 🎧 Audio | [`gnc4KAveHzU`](https://www.youtube.com/watch?v=gnc4KAveHzU) | [https://www.youtube.com/watch?v=gnc4KAveHzU](https://www.youtube.com/watch?v=gnc4KAveHzU) | ✅ **PASS** |
| 10 | `b2-katha-pauranik-chandra-shapa-somnath` | **चंद्रमा का क्षय रोग एवं सोमनाथ ज्योतिर्लिंग प्राकट्य** | 🎧 Audio | [`CnM0YeJr7hc`](https://www.youtube.com/watch?v=CnM0YeJr7hc) | [https://www.youtube.com/watch?v=CnM0YeJr7hc](https://www.youtube.com/watch?v=CnM0YeJr7hc) | ✅ **PASS** |
| 11 | `b2-katha-shiva-andhakasur-vadh` | **अंधकासुर वध एवं मातृकाओं का प्राकट्य** | 🎧 Audio | [`U4G4Ec5D9BY`](https://www.youtube.com/watch?v=U4G4Ec5D9BY) | [https://www.youtube.com/watch?v=U4G4Ec5D9BY](https://www.youtube.com/watch?v=U4G4Ec5D9BY) | ✅ **PASS** |
| 12 | `b2-katha-shiva-bhasmasur-mohini-lila` | **भस्मासुर मोहिनी प्रसंग: अहंकार का स्वतः विनाश** | 🎧 Audio | [`jBspv5RiB8I`](https://www.youtube.com/watch?v=jBspv5RiB8I) | [https://www.youtube.com/watch?v=jBspv5RiB8I](https://www.youtube.com/watch?v=jBspv5RiB8I) | ✅ **PASS** |
| 13 | `b3-katha-hanuman-ahiravan-vadh-patal-vijay-b3` | **पाताल लोक में अहिरावण वध एवं मकरध्वज से पावन मिलन** | 🎧 Audio | [`evUvGGHz0rU`](https://www.youtube.com/watch?v=evUvGGHz0rU) | [https://www.youtube.com/watch?v=evUvGGHz0rU](https://www.youtube.com/watch?v=evUvGGHz0rU) | ✅ **PASS** |
| 14 | `b3-katha-hanuman-sanjivani-parvat-drona-uthana` | **लक्ष्मण शक्ति बाण मूर्छा एवं द्रोणागिरि पर्वत संजीवनी लाना** | 🎧 Audio | [`_-MWuyxXp70`](https://www.youtube.com/watch?v=_-MWuyxXp70) | [https://www.youtube.com/watch?v=_-MWuyxXp70](https://www.youtube.com/watch?v=_-MWuyxXp70) | ✅ **PASS** |
| 15 | `b3-katha-krishna-dwarka-nagari-samudra-nirman` | **विश्वकर्मा द्वारा समुद्र मध्य स्वर्णमयी द्वारका निर्माण** | 🎧 Audio | [`vMLYv2hHMkI`](https://www.youtube.com/watch?v=vMLYv2hHMkI) | [https://www.youtube.com/watch?v=vMLYv2hHMkI](https://www.youtube.com/watch?v=vMLYv2hHMkI) | ✅ **PASS** |
| 16 | `b3-katha-krishna-kansa-vadh-mathura-vijay` | **धनुष यज्ञ, कुवलयापीड-चाणूर वध एवं कंस वध कथा** | 🎧 Audio | [`GWFRV1I2OZ8`](https://www.youtube.com/watch?v=GWFRV1I2OZ8) | [https://www.youtube.com/watch?v=GWFRV1I2OZ8](https://www.youtube.com/watch?v=GWFRV1I2OZ8) | ✅ **PASS** |
| 17 | `b3-katha-krishna-maha-raas-leela-sharad-purnima` | **शरद पूर्णिमा महारास लीला एवं जीवात्मा-परमात्मा मिलन** | 🎧 Audio | [`F-oTu5dyWVU`](https://www.youtube.com/watch?v=F-oTu5dyWVU) | [https://www.youtube.com/watch?v=F-oTu5dyWVU](https://www.youtube.com/watch?v=F-oTu5dyWVU) | ✅ **PASS** |
| 18 | `b3-katha-krishna-shishupal-vadh-sudarshana-chakra` | **राजसूय यज्ञ में शिशुपाल के 100 अपराध क्षमा व सुदर्शन चक्र वध** | 🎧 Audio | [`QmYsSkTmPPM`](https://www.youtube.com/watch?v=QmYsSkTmPPM) | [https://www.youtube.com/watch?v=QmYsSkTmPPM](https://www.youtube.com/watch?v=QmYsSkTmPPM) | ✅ **PASS** |
| 19 | `b3-katha-krishna-yamalarjuna-bhanjan-damodar` | **ऊखल बंधन एवं यमलार्जुन वृक्षों का दिव्य उद्धार** | 🎧 Audio | [`02hdezOLbq8`](https://www.youtube.com/watch?v=02hdezOLbq8) | [https://www.youtube.com/watch?v=02hdezOLbq8](https://www.youtube.com/watch?v=02hdezOLbq8) | ✅ **PASS** |
| 20 | `b3-katha-shiva-samudra-manthan-neelkanth-mahadev` | **समुद्र मंथन में हलाहल विष पान एवं नीलकंठ महादेव** | 🎧 Audio | [`KMhclpkgEbI`](https://www.youtube.com/watch?v=KMhclpkgEbI) | [https://www.youtube.com/watch?v=KMhclpkgEbI](https://www.youtube.com/watch?v=KMhclpkgEbI) | ✅ **PASS** |
| 21 | `b4-katha-krishna-kalia-mardan-yamuna-tat` | **कालिया नाग दमन एवं यमुना जी का पावन विष-मुक्ति प्रसंग** | 🎧 Audio | [`yndLpHTYW8g`](https://www.youtube.com/watch?v=yndLpHTYW8g) | [https://www.youtube.com/watch?v=yndLpHTYW8g](https://www.youtube.com/watch?v=yndLpHTYW8g) | ✅ **PASS** |
| 22 | `b4-katha-krishna-kansa-vadh-mathura-leela` | **मथुरा आगमन, कुब्जा उद्धार, धनुषभंग एवं कंस वध** | 🎧 Audio | [`bgp6JV8Popc`](https://www.youtube.com/watch?v=bgp6JV8Popc) | [https://www.youtube.com/watch?v=bgp6JV8Popc](https://www.youtube.com/watch?v=bgp6JV8Popc) | ✅ **PASS** |
| 23 | `b4-katha-krishna-rasa-lila-sharad-purnima` | **शरद पूर्णिमा महारास लीला एवं वंशीवट का दिव्य नृत्य** | 🎧 Audio | [`u_kJeqVGI9U`](https://www.youtube.com/watch?v=u_kJeqVGI9U) | [https://www.youtube.com/watch?v=u_kJeqVGI9U](https://www.youtube.com/watch?v=u_kJeqVGI9U) | ✅ **PASS** |
| 24 | `b4-katha-shiva-samudra-manthan-neelkanth-katha` | **समुद्र मंथन, कालकूट हलाहल विष एवं नीलकंठ महादेव** | 🎧 Audio | [`TDGTDJpY4AA`](https://www.youtube.com/watch?v=TDGTDJpY4AA) | [https://www.youtube.com/watch?v=TDGTDJpY4AA](https://www.youtube.com/watch?v=TDGTDJpY4AA) | ✅ **PASS** |
| 25 | `b14-katha-purana-prerak-dhara-04-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 04 (अमृत प्रसंग 14)** | 🎬 Video | [`8csU19A_sYQ`](https://www.youtube.com/watch?v=8csU19A_sYQ) | [https://www.youtube.com/watch?v=8csU19A_sYQ](https://www.youtube.com/watch?v=8csU19A_sYQ) | ✅ **PASS** |
| 26 | `b15-katha-purana-prerak-dhara-09-b15` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (अमृत प्रसंग 15)** | 🎬 Video | [`q6MhIzOi600`](https://www.youtube.com/watch?v=q6MhIzOi600) | [https://www.youtube.com/watch?v=q6MhIzOi600](https://www.youtube.com/watch?v=q6MhIzOi600) | ✅ **PASS** |
| 27 | `b2-katha-hanuman-dronagiri-parvat-udaran` | **द्रोणागिरि पर्वत उखाड़ना एवं कालनेमि संहार** | 🎬 Video | [`MYAq8xAimfA`](https://www.youtube.com/watch?v=MYAq8xAimfA) | [https://www.youtube.com/watch?v=MYAq8xAimfA](https://www.youtube.com/watch?v=MYAq8xAimfA) | ✅ **PASS** |
| 28 | `b2-katha-krishna-kalia-naag-daman` | **कालिया नाग दमन लीला (यमुना जल विष मुक्ति)** | 🎬 Video | [`g2QPLSqKkU4`](https://www.youtube.com/watch?v=g2QPLSqKkU4) | [https://www.youtube.com/watch?v=g2QPLSqKkU4](https://www.youtube.com/watch?v=g2QPLSqKkU4) | ✅ **PASS** |
| 29 | `b2-katha-krishna-kansa-vadh-ugrasen-raj` | **कंस वध एवं महाराज उग्रसेन का राज्याभिषेक** | 🎬 Video | [`AsFCiuB_flE`](https://www.youtube.com/watch?v=AsFCiuB_flE) | [https://www.youtube.com/watch?v=AsFCiuB_flE](https://www.youtube.com/watch?v=AsFCiuB_flE) | ✅ **PASS** |
| 30 | `b2-katha-krishna-makhan-chori-ukhal-bandhan` | **माखन चोरी एवं यमलार्जुन मोक्ष (ऊखल बंधन लीला)** | 🎬 Video | [`O4D0By8ykgk`](https://www.youtube.com/watch?v=O4D0By8ykgk) | [https://www.youtube.com/watch?v=O4D0By8ykgk](https://www.youtube.com/watch?v=O4D0By8ykgk) | ✅ **PASS** |
| 31 | `b2-katha-krishna-putana-moksha-leela` | **पूतना मोक्ष लीला: विषपान कराने वाली राक्षसी को मातृगति** | 🎬 Video | [`Xp3LoRFMAoI`](https://www.youtube.com/watch?v=Xp3LoRFMAoI) | [https://www.youtube.com/watch?v=Xp3LoRFMAoI](https://www.youtube.com/watch?v=Xp3LoRFMAoI) | ✅ **PASS** |
| 32 | `b2-katha-pauranik-chandra-shapa-somnath` | **चंद्रमा का क्षय रोग एवं सोमनाथ ज्योतिर्लिंग प्राकट्य** | 🎬 Video | [`bjUGeCA_4tM`](https://www.youtube.com/watch?v=bjUGeCA_4tM) | [https://www.youtube.com/watch?v=bjUGeCA_4tM](https://www.youtube.com/watch?v=bjUGeCA_4tM) | ✅ **PASS** |
| 33 | `b2-katha-shiva-andhakasur-vadh` | **अंधकासुर वध एवं मातृकाओं का प्राकट्य** | 🎬 Video | [`Y12c1RQZ36Y`](https://www.youtube.com/watch?v=Y12c1RQZ36Y) | [https://www.youtube.com/watch?v=Y12c1RQZ36Y](https://www.youtube.com/watch?v=Y12c1RQZ36Y) | ✅ **PASS** |
| 34 | `b2-katha-shiva-bhasmasur-mohini-lila` | **भस्मासुर मोहिनी प्रसंग: अहंकार का स्वतः विनाश** | 🎬 Video | [`NYfFlghyz_M`](https://www.youtube.com/watch?v=NYfFlghyz_M) | [https://www.youtube.com/watch?v=NYfFlghyz_M](https://www.youtube.com/watch?v=NYfFlghyz_M) | ✅ **PASS** |
| 35 | `b3-katha-hanuman-ahiravan-vadh-patal-vijay-b3` | **पाताल लोक में अहिरावण वध एवं मकरध्वज से पावन मिलन** | 🎬 Video | [`a77mC7WnWBw`](https://www.youtube.com/watch?v=a77mC7WnWBw) | [https://www.youtube.com/watch?v=a77mC7WnWBw](https://www.youtube.com/watch?v=a77mC7WnWBw) | ✅ **PASS** |
| 36 | `b3-katha-hanuman-sanjivani-parvat-drona-uthana` | **लक्ष्मण शक्ति बाण मूर्छा एवं द्रोणागिरि पर्वत संजीवनी लाना** | 🎬 Video | [`bYsnpcq8MZc`](https://www.youtube.com/watch?v=bYsnpcq8MZc) | [https://www.youtube.com/watch?v=bYsnpcq8MZc](https://www.youtube.com/watch?v=bYsnpcq8MZc) | ✅ **PASS** |
| 37 | `b3-katha-hanuman-surya-gras-balpan-leela` | **बाल्यकाल में सूर्य को फल समझकर मुख में रखना एवं देव वरदान** | 🎬 Video | [`KdXBxre5K4Q`](https://www.youtube.com/watch?v=KdXBxre5K4Q) | [https://www.youtube.com/watch?v=KdXBxre5K4Q](https://www.youtube.com/watch?v=KdXBxre5K4Q) | ✅ **PASS** |
| 38 | `b3-katha-krishna-dwarka-nagari-samudra-nirman` | **विश्वकर्मा द्वारा समुद्र मध्य स्वर्णमयी द्वारका निर्माण** | 🎬 Video | [`uxVHt6YcLzM`](https://www.youtube.com/watch?v=uxVHt6YcLzM) | [https://www.youtube.com/watch?v=uxVHt6YcLzM](https://www.youtube.com/watch?v=uxVHt6YcLzM) | ✅ **PASS** |
| 39 | `b3-katha-krishna-kansa-vadh-mathura-vijay` | **धनुष यज्ञ, कुवलयापीड-चाणूर वध एवं कंस वध कथा** | 🎬 Video | [`VQ6uwmjotA0`](https://www.youtube.com/watch?v=VQ6uwmjotA0) | [https://www.youtube.com/watch?v=VQ6uwmjotA0](https://www.youtube.com/watch?v=VQ6uwmjotA0) | ✅ **PASS** |
| 40 | `b3-katha-krishna-maha-raas-leela-sharad-purnima` | **शरद पूर्णिमा महारास लीला एवं जीवात्मा-परमात्मा मिलन** | 🎬 Video | [`IROCnRKIc3E`](https://www.youtube.com/watch?v=IROCnRKIc3E) | [https://www.youtube.com/watch?v=IROCnRKIc3E](https://www.youtube.com/watch?v=IROCnRKIc3E) | ✅ **PASS** |
| 41 | `b3-katha-krishna-shishupal-vadh-sudarshana-chakra` | **राजसूय यज्ञ में शिशुपाल के 100 अपराध क्षमा व सुदर्शन चक्र वध** | 🎬 Video | [`1nc43PdrxdQ`](https://www.youtube.com/watch?v=1nc43PdrxdQ) | [https://www.youtube.com/watch?v=1nc43PdrxdQ](https://www.youtube.com/watch?v=1nc43PdrxdQ) | ✅ **PASS** |
| 42 | `b3-katha-krishna-yamalarjuna-bhanjan-damodar` | **ऊखल बंधन एवं यमलार्जुन वृक्षों का दिव्य उद्धार** | 🎬 Video | [`dC-J2EtzlJM`](https://www.youtube.com/watch?v=dC-J2EtzlJM) | [https://www.youtube.com/watch?v=dC-J2EtzlJM](https://www.youtube.com/watch?v=dC-J2EtzlJM) | ✅ **PASS** |
| 43 | `b3-katha-shiva-samudra-manthan-neelkanth-mahadev` | **समुद्र मंथन में हलाहल विष पान एवं नीलकंठ महादेव** | 🎬 Video | [`Ws4BKCsh-Q4`](https://www.youtube.com/watch?v=Ws4BKCsh-Q4) | [https://www.youtube.com/watch?v=Ws4BKCsh-Q4](https://www.youtube.com/watch?v=Ws4BKCsh-Q4) | ✅ **PASS** |
| 44 | `b4-katha-krishna-kalia-mardan-yamuna-tat` | **कालिया नाग दमन एवं यमुना जी का पावन विष-मुक्ति प्रसंग** | 🎬 Video | [`AB2sbXuL9kQ`](https://www.youtube.com/watch?v=AB2sbXuL9kQ) | [https://www.youtube.com/watch?v=AB2sbXuL9kQ](https://www.youtube.com/watch?v=AB2sbXuL9kQ) | ✅ **PASS** |
| 45 | `b4-katha-krishna-kansa-vadh-mathura-leela` | **मथुरा आगमन, कुब्जा उद्धार, धनुषभंग एवं कंस वध** | 🎬 Video | [`7AoCZv9yCD0`](https://www.youtube.com/watch?v=7AoCZv9yCD0) | [https://www.youtube.com/watch?v=7AoCZv9yCD0](https://www.youtube.com/watch?v=7AoCZv9yCD0) | ✅ **PASS** |
| 46 | `b4-katha-krishna-rasa-lila-sharad-purnima` | **शरद पूर्णिमा महारास लीला एवं वंशीवट का दिव्य नृत्य** | 🎬 Video | [`ts-MZ-QGmYs`](https://www.youtube.com/watch?v=ts-MZ-QGmYs) | [https://www.youtube.com/watch?v=ts-MZ-QGmYs](https://www.youtube.com/watch?v=ts-MZ-QGmYs) | ✅ **PASS** |
| 47 | `b4-katha-shiva-samudra-manthan-neelkanth-katha` | **समुद्र मंथन, कालकूट हलाहल विष एवं नीलकंठ महादेव** | 🎬 Video | [`yPunxn4BUlM`](https://www.youtube.com/watch?v=yPunxn4BUlM) | [https://www.youtube.com/watch?v=yPunxn4BUlM](https://www.youtube.com/watch?v=yPunxn4BUlM) | ✅ **PASS** |

---

## 4. 🔒 FINAL RESULT

```
PHASE 2Q-E VERIFIED MEDIA APPLY COMPLETE

Database Modified       : YES
Database Writes         : 47

Approved Audio          : 24
Approved Video          : 23
Approved Total          : 47

Audio Applied           : 24
Video Applied           : 23
Total Applied           : 47

Audio Skipped           : 0
Video Skipped           : 0
Total Failed            : 0

Overwrite Attempts      : 0
Duplicate YouTube IDs   : 0
Duplicate YouTube URLs  : 0
Cross-Field Conflicts   : 0
URL-ID Mismatches       : 0
Malformed URLs          : 0
Unauthorized Changes    : 0

47/47 Mapping Verification : PASS

Live Verification       : PASS

Pre-Apply Playable Audio : 370
Post-Apply Playable Audio: 394
Playable Audio Delta     : +24

Pre-Apply YouTube Audio  : 332
Post-Apply YouTube Audio : 356
YouTube Audio Delta      : +24

Pre-Apply Video URLs     : 203
Post-Apply Video URLs    : 226
Video URL Delta          : +23

Katha With Audio        : 333
Katha With Video        : 224
Katha With Both         : 200
Katha With Neither      : 148

Audio Only              : 133
Video Only              : 24

FTS5 Verification       : PASS
Integrity Check         : ok
Foreign-Key Violations  : 0
Schema Audit            : PASS

Katha Reconciliation    : PASS
Delta Reconciliation    : PASS

Transaction             : COMMITTED

Final Gate              : PASS

IMPORTANT:
Phase 2Q-E applied ONLY the Phase 2Q-D approved mappings.

No REVIEW, REJECT, or NO_SUITABLE candidate was applied.

DO NOT automatically start Phase 2Q-F.
STOP AFTER APPLY AUDIT.
```
