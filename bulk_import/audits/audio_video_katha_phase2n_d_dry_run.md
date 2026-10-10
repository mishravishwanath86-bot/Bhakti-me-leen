# 📖🎬 Phase 2N-D — Final Dry Run & Apply Safety Verification Report

**Mode**: `STRICT READ-ONLY — FINAL DRY RUN ONLY` (Zero Database Writes)  
**Database File**: `db/bhakti.db` (Unchanged, 0 Writes)  
**Date**: `2026-08-31 13:57:31`  
**Safety Gate**: **`PASS`**  

---

## 1. 🛡️ Current Database Baseline vs. Projected Post-Apply State

| Metric | Current Real Baseline | Projected Post-Apply | Status |
| :--- | :--- | :--- | :--- |
| **Total Database Records** | **`10,010`** | `10,010` | ✅ Unchanged |
| **FTS5 Search Documents** | **`10,010`** | `10,010` | ✅ Unchanged |
| **Playable Audio Total** | **`284`** | **`322`** (+38) | 🎯 Audio Expansion |
| **Local MP3 Audio** | **`38`** | `38` | ✅ Untouched |
| **YouTube HD Audio** | **`246`** | **`284`** (+38) | 🎧 +38 Verified Spoken Kathas |
| **YouTube Video URLs** | **`148`** | **`180`** (+32) | 🎬 +32 Verified Video Discourses |
| **PRAGMA integrity_check** | **`ok`** | `ok` | ✅ 0 Corruption |
| **Foreign-Key Violations** | **`0`** | `0` | ✅ 100% Valid |
| **Real Database Writes** | **`0`** | `0` | ✅ Zero Writes (Dry Run Only) |

---

## 2. 📖 Projected Katha Coverage Evolution Across All 505 Records

| Katha Category Metric | Current State | Projected Post-Apply | Change |
| :--- | :---: | :---: | :---: |
| **Katha With Audio** | `223` | **`261`** | +38 |
| **Katha With Video** | `146` | **`178`** | +32 |
| **Katha With Both Media** | `135` | **`162`** | +27 |
| **Katha With Neither Media (Gaps)** | `271` | **`228`** | -43 |

* **Projected Disjoint Partition**: Both (`162`) + Audio Only (`99`) + Video Only (`16`) + Neither (`228`) = **`505`**

---

## 3. 📋 70 Candidate Safety Revalidation Matrix

| # | Database Record ID | Katha Title | Media Type | YouTube Video ID | Current Value | Proposed Value | Safety Verdict |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :---: |
| 01 | `b3-katha-krishna-geeta-updesh-vishwaroop-darshan` | **कुरुक्षेत्र में अर्जुन को श्रीमद्भगवद्गीता उपदेश एवं विश्वरूप दर्शन** | 🎧 Audio | [`RZ6zkX5DRMA`](https://www.youtube.com/watch?v=RZ6zkX5DRMA) | `NULL` | [`RZ6zkX5DRMA`](https://www.youtube.com/watch?v=RZ6zkX5DRMA) | ✅ **`SAFE_TO_APPLY`** |
| 02 | `b20-saraswati-katha-b20-257` | **मां सरस्वती लीला प्रसंग स्तुति संकीर्तन (विंशति पद 257 - 20)** | 🎧 Audio | [`ieQhQB_y_wo`](https://www.youtube.com/watch?v=ieQhQB_y_wo) | `NULL` | [`ieQhQB_y_wo`](https://www.youtube.com/watch?v=ieQhQB_y_wo) | ✅ **`SAFE_TO_APPLY`** |
| 03 | `b2-katha-bhakta-prahlada-holika-dahan` | **भक्त प्रह्लाद एवं होलिका दहन (अग्नि में भी बाल न बांका)** | 🎧 Audio | [`IAG-ndaz6oQ`](https://www.youtube.com/watch?v=IAG-ndaz6oQ) | `NULL` | [`IAG-ndaz6oQ`](https://www.youtube.com/watch?v=IAG-ndaz6oQ) | ✅ **`SAFE_TO_APPLY`** |
| 04 | `b2-katha-bhakta-raja-bali-vamana-3-pag` | **राजा बलि एवं भगवान वामन: 3 पग में तीनों लोक नापना** | 🎧 Audio | [`vLVPM2PvmM4`](https://www.youtube.com/watch?v=vLVPM2PvmM4) | `NULL` | [`vLVPM2PvmM4`](https://www.youtube.com/watch?v=vLVPM2PvmM4) | ✅ **`SAFE_TO_APPLY`** |
| 05 | `b3-katha-vishnu-narasimha-avatar-khambha-faad` | **भक्त प्रह्लाद की रक्षा हेतु भगवान नृसिंह का खंभा फाड़कर प्राकट्य** | 🎧 Audio | [`wTCXjSXcB74`](https://www.youtube.com/watch?v=wTCXjSXcB74) | `NULL` | [`wTCXjSXcB74`](https://www.youtube.com/watch?v=wTCXjSXcB74) | ✅ **`SAFE_TO_APPLY`** |
| 06 | `b3-katha-vishnu-vamana-avatar-bali-daan` | **भगवान वामन अवतार एवं राजा बलि से तीन पग भूमि दान** | 🎧 Audio | [`fDzcm2RKM4s`](https://www.youtube.com/watch?v=fDzcm2RKM4s) | `NULL` | [`fDzcm2RKM4s`](https://www.youtube.com/watch?v=fDzcm2RKM4s) | ✅ **`SAFE_TO_APPLY`** |
| 07 | `b4-katha-vishnu-narasimha-avatar-aur-prahlad` | **भगवान नृसिंह अवतार एवं भक्त प्रह्लाद की रक्षा** | 🎧 Audio | [`toyH8UxPqAw`](https://www.youtube.com/watch?v=toyH8UxPqAw) | `NULL` | [`toyH8UxPqAw`](https://www.youtube.com/watch?v=toyH8UxPqAw) | ✅ **`SAFE_TO_APPLY`** |
| 08 | `b11-katha-purana-prerak-prasang-01-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 01 (अमृत कथा 11)** | 🎧 Audio | [`4-c387I-H3E`](https://www.youtube.com/watch?v=4-c387I-H3E) | `NULL` | [`4-c387I-H3E`](https://www.youtube.com/watch?v=4-c387I-H3E) | ✅ **`SAFE_TO_APPLY`** |
| 09 | `b11-katha-purana-prerak-prasang-02-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 02 (अमृत कथा 11)** | 🎧 Audio | [`4OTNGx1nbwM`](https://www.youtube.com/watch?v=4OTNGx1nbwM) | `NULL` | [`4OTNGx1nbwM`](https://www.youtube.com/watch?v=4OTNGx1nbwM) | ✅ **`SAFE_TO_APPLY`** |
| 10 | `b11-katha-purana-prerak-prasang-03-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 03 (अमृत कथा 11)** | 🎧 Audio | [`68qoYbIzYqY`](https://www.youtube.com/watch?v=68qoYbIzYqY) | `NULL` | [`68qoYbIzYqY`](https://www.youtube.com/watch?v=68qoYbIzYqY) | ✅ **`SAFE_TO_APPLY`** |
| 11 | `b11-katha-purana-prerak-prasang-04-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 04 (अमृत कथा 11)** | 🎧 Audio | [`J5kpjm4ZXwg`](https://www.youtube.com/watch?v=J5kpjm4ZXwg) | `NULL` | [`J5kpjm4ZXwg`](https://www.youtube.com/watch?v=J5kpjm4ZXwg) | ✅ **`SAFE_TO_APPLY`** |
| 12 | `b11-katha-purana-prerak-prasang-05-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 05 (अमृत कथा 11)** | 🎧 Audio | [`_Hpy1FKBZTA`](https://www.youtube.com/watch?v=_Hpy1FKBZTA) | `NULL` | [`_Hpy1FKBZTA`](https://www.youtube.com/watch?v=_Hpy1FKBZTA) | ✅ **`SAFE_TO_APPLY`** |
| 13 | `b11-katha-purana-prerak-prasang-06-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 06 (अमृत कथा 11)** | 🎧 Audio | [`GuUvemahyYw`](https://www.youtube.com/watch?v=GuUvemahyYw) | `NULL` | [`GuUvemahyYw`](https://www.youtube.com/watch?v=GuUvemahyYw) | ✅ **`SAFE_TO_APPLY`** |
| 14 | `b11-katha-purana-prerak-prasang-07-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 07 (अमृत कथा 11)** | 🎧 Audio | [`b7np2nlReSs`](https://www.youtube.com/watch?v=b7np2nlReSs) | `NULL` | [`b7np2nlReSs`](https://www.youtube.com/watch?v=b7np2nlReSs) | ✅ **`SAFE_TO_APPLY`** |
| 15 | `b11-katha-purana-prerak-prasang-08-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 08 (अमृत कथा 11)** | 🎧 Audio | [`xABIG2WY8Pw`](https://www.youtube.com/watch?v=xABIG2WY8Pw) | `NULL` | [`xABIG2WY8Pw`](https://www.youtube.com/watch?v=xABIG2WY8Pw) | ✅ **`SAFE_TO_APPLY`** |
| 16 | `b11-katha-purana-prerak-prasang-09-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (अमृत कथा 11)** | 🎧 Audio | [`wmV2pLw_Leo`](https://www.youtube.com/watch?v=wmV2pLw_Leo) | `NULL` | [`wmV2pLw_Leo`](https://www.youtube.com/watch?v=wmV2pLw_Leo) | ✅ **`SAFE_TO_APPLY`** |
| 17 | `b11-katha-purana-prerak-prasang-11-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 11 (अमृत कथा 11)** | 🎧 Audio | [`kHy4IADSKik`](https://www.youtube.com/watch?v=kHy4IADSKik) | `NULL` | [`kHy4IADSKik`](https://www.youtube.com/watch?v=kHy4IADSKik) | ✅ **`SAFE_TO_APPLY`** |
| 18 | `b11-katha-purana-prerak-prasang-13-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 13 (अमृत कथा 11)** | 🎧 Audio | [`mWg4kcKSEus`](https://www.youtube.com/watch?v=mWg4kcKSEus) | `NULL` | [`mWg4kcKSEus`](https://www.youtube.com/watch?v=mWg4kcKSEus) | ✅ **`SAFE_TO_APPLY`** |
| 19 | `b11-katha-purana-prerak-prasang-14-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 14 (अमृत कथा 11)** | 🎧 Audio | [`mYemCfhwA80`](https://www.youtube.com/watch?v=mYemCfhwA80) | `NULL` | [`mYemCfhwA80`](https://www.youtube.com/watch?v=mYemCfhwA80) | ✅ **`SAFE_TO_APPLY`** |
| 20 | `b11-katha-purana-prerak-prasang-15-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 15 (अमृत कथा 11)** | 🎧 Audio | [`ZSqrqPJpQ90`](https://www.youtube.com/watch?v=ZSqrqPJpQ90) | `NULL` | [`ZSqrqPJpQ90`](https://www.youtube.com/watch?v=ZSqrqPJpQ90) | ✅ **`SAFE_TO_APPLY`** |
| 21 | `b13-katha-purana-prerak-dhara-01-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 01 (अमृत प्रसंग 13)** | 🎧 Audio | [`bkChXn-8Awg`](https://www.youtube.com/watch?v=bkChXn-8Awg) | `NULL` | [`bkChXn-8Awg`](https://www.youtube.com/watch?v=bkChXn-8Awg) | ✅ **`SAFE_TO_APPLY`** |
| 22 | `b13-katha-purana-prerak-dhara-02-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 02 (अमृत प्रसंग 13)** | 🎧 Audio | [`2j2iHzymm6Q`](https://www.youtube.com/watch?v=2j2iHzymm6Q) | `NULL` | [`2j2iHzymm6Q`](https://www.youtube.com/watch?v=2j2iHzymm6Q) | ✅ **`SAFE_TO_APPLY`** |
| 23 | `b13-katha-purana-prerak-dhara-03-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 03 (अमृत प्रसंग 13)** | 🎧 Audio | [`Ncx1PXgY4LQ`](https://www.youtube.com/watch?v=Ncx1PXgY4LQ) | `NULL` | [`Ncx1PXgY4LQ`](https://www.youtube.com/watch?v=Ncx1PXgY4LQ) | ✅ **`SAFE_TO_APPLY`** |
| 24 | `b13-katha-purana-prerak-dhara-04-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 04 (अमृत प्रसंग 13)** | 🎧 Audio | [`Fi0wKb_u2_g`](https://www.youtube.com/watch?v=Fi0wKb_u2_g) | `NULL` | [`Fi0wKb_u2_g`](https://www.youtube.com/watch?v=Fi0wKb_u2_g) | ✅ **`SAFE_TO_APPLY`** |
| 25 | `b13-katha-purana-prerak-dhara-05-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 05 (अमृत प्रसंग 13)** | 🎧 Audio | [`zXje2iT7Cd4`](https://www.youtube.com/watch?v=zXje2iT7Cd4) | `NULL` | [`zXje2iT7Cd4`](https://www.youtube.com/watch?v=zXje2iT7Cd4) | ✅ **`SAFE_TO_APPLY`** |
| 26 | `b13-katha-purana-prerak-dhara-08-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 08 (अमृत प्रसंग 13)** | 🎧 Audio | [`C-Cq90fOg0E`](https://www.youtube.com/watch?v=C-Cq90fOg0E) | `NULL` | [`C-Cq90fOg0E`](https://www.youtube.com/watch?v=C-Cq90fOg0E) | ✅ **`SAFE_TO_APPLY`** |
| 27 | `b13-katha-purana-prerak-dhara-09-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (अमृत प्रसंग 13)** | 🎧 Audio | [`jqUi5bDKLS4`](https://www.youtube.com/watch?v=jqUi5bDKLS4) | `NULL` | [`jqUi5bDKLS4`](https://www.youtube.com/watch?v=jqUi5bDKLS4) | ✅ **`SAFE_TO_APPLY`** |
| 28 | `b13-katha-purana-prerak-dhara-11-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 11 (अमृत प्रसंग 13)** | 🎧 Audio | [`g2J39TOXUWg`](https://www.youtube.com/watch?v=g2J39TOXUWg) | `NULL` | [`g2J39TOXUWg`](https://www.youtube.com/watch?v=g2J39TOXUWg) | ✅ **`SAFE_TO_APPLY`** |
| 29 | `b13-katha-purana-prerak-dhara-12-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 12 (अमृत प्रसंग 13)** | 🎧 Audio | [`u7y8GOO9wKM`](https://www.youtube.com/watch?v=u7y8GOO9wKM) | `NULL` | [`u7y8GOO9wKM`](https://www.youtube.com/watch?v=u7y8GOO9wKM) | ✅ **`SAFE_TO_APPLY`** |
| 30 | `b13-katha-purana-prerak-dhara-13-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 13 (अमृत प्रसंग 13)** | 🎧 Audio | [`aQNdphh3n5U`](https://www.youtube.com/watch?v=aQNdphh3n5U) | `NULL` | [`aQNdphh3n5U`](https://www.youtube.com/watch?v=aQNdphh3n5U) | ✅ **`SAFE_TO_APPLY`** |
| 31 | `b13-katha-purana-prerak-dhara-14-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 14 (अमृत प्रसंग 13)** | 🎧 Audio | [`2G0Eg2sUqfs`](https://www.youtube.com/watch?v=2G0Eg2sUqfs) | `NULL` | [`2G0Eg2sUqfs`](https://www.youtube.com/watch?v=2G0Eg2sUqfs) | ✅ **`SAFE_TO_APPLY`** |
| 32 | `b13-katha-purana-prerak-dhara-15-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 15 (अमृत प्रसंग 13)** | 🎧 Audio | [`NFxci9WqHK4`](https://www.youtube.com/watch?v=NFxci9WqHK4) | `NULL` | [`NFxci9WqHK4`](https://www.youtube.com/watch?v=NFxci9WqHK4) | ✅ **`SAFE_TO_APPLY`** |
| 33 | `b14-katha-purana-prerak-dhara-01-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 01 (अमृत प्रसंग 14)** | 🎧 Audio | [`z8K-CEkErF8`](https://www.youtube.com/watch?v=z8K-CEkErF8) | `NULL` | [`z8K-CEkErF8`](https://www.youtube.com/watch?v=z8K-CEkErF8) | ✅ **`SAFE_TO_APPLY`** |
| 34 | `b14-katha-purana-prerak-dhara-03-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 03 (अमृत प्रसंग 14)** | 🎧 Audio | [`vM6Wu8yUqXw`](https://www.youtube.com/watch?v=vM6Wu8yUqXw) | `NULL` | [`vM6Wu8yUqXw`](https://www.youtube.com/watch?v=vM6Wu8yUqXw) | ✅ **`SAFE_TO_APPLY`** |
| 35 | `b14-katha-purana-prerak-dhara-05-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 05 (अमृत प्रसंग 14)** | 🎧 Audio | [`2pRCRBbq4fw`](https://www.youtube.com/watch?v=2pRCRBbq4fw) | `NULL` | [`2pRCRBbq4fw`](https://www.youtube.com/watch?v=2pRCRBbq4fw) | ✅ **`SAFE_TO_APPLY`** |
| 36 | `b14-katha-purana-prerak-dhara-07-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 07 (अमृत प्रसंग 14)** | 🎧 Audio | [`1Gcv2tFD5Hc`](https://www.youtube.com/watch?v=1Gcv2tFD5Hc) | `NULL` | [`1Gcv2tFD5Hc`](https://www.youtube.com/watch?v=1Gcv2tFD5Hc) | ✅ **`SAFE_TO_APPLY`** |
| 37 | `b14-katha-purana-prerak-dhara-08-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 08 (अमृत प्रसंग 14)** | 🎧 Audio | [`JKORWjNupfY`](https://www.youtube.com/watch?v=JKORWjNupfY) | `NULL` | [`JKORWjNupfY`](https://www.youtube.com/watch?v=JKORWjNupfY) | ✅ **`SAFE_TO_APPLY`** |
| 38 | `b14-katha-purana-prerak-dhara-10-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 10 (अमृत प्रसंग 14)** | 🎧 Audio | [`gpLFo1zPNHg`](https://www.youtube.com/watch?v=gpLFo1zPNHg) | `NULL` | [`gpLFo1zPNHg`](https://www.youtube.com/watch?v=gpLFo1zPNHg) | ✅ **`SAFE_TO_APPLY`** |
| 39 | `b2-katha-bhakta-prahlada-holika-dahan` | **भक्त प्रह्लाद एवं होलिका दहन (अग्नि में भी बाल न बांका)** | 🎬 Video | [`5OJN_IjB4ZU`](https://www.youtube.com/watch?v=5OJN_IjB4ZU) | `NULL` | [`5OJN_IjB4ZU`](https://www.youtube.com/watch?v=5OJN_IjB4ZU) | ✅ **`SAFE_TO_APPLY`** |
| 40 | `b2-katha-bhakta-raja-bali-vamana-3-pag` | **राजा बलि एवं भगवान वामन: 3 पग में तीनों लोक नापना** | 🎬 Video | [`ijD9LmobncY`](https://www.youtube.com/watch?v=ijD9LmobncY) | `NULL` | [`ijD9LmobncY`](https://www.youtube.com/watch?v=ijD9LmobncY) | ✅ **`SAFE_TO_APPLY`** |
| 41 | `b3-katha-vishnu-narasimha-avatar-khambha-faad` | **भक्त प्रह्लाद की रक्षा हेतु भगवान नृसिंह का खंभा फाड़कर प्राकट्य** | 🎬 Video | [`jhSqp9J_BSc`](https://www.youtube.com/watch?v=jhSqp9J_BSc) | `NULL` | [`jhSqp9J_BSc`](https://www.youtube.com/watch?v=jhSqp9J_BSc) | ✅ **`SAFE_TO_APPLY`** |
| 42 | `b3-katha-vishnu-vamana-avatar-bali-daan` | **भगवान वामन अवतार एवं राजा बलि से तीन पग भूमि दान** | 🎬 Video | [`-DRgUhc8u4s`](https://www.youtube.com/watch?v=-DRgUhc8u4s) | `NULL` | [`-DRgUhc8u4s`](https://www.youtube.com/watch?v=-DRgUhc8u4s) | ✅ **`SAFE_TO_APPLY`** |
| 43 | `b4-katha-vishnu-narasimha-avatar-aur-prahlad` | **भगवान नृसिंह अवतार एवं भक्त प्रह्लाद की रक्षा** | 🎬 Video | [`XipLPXYnx50`](https://www.youtube.com/watch?v=XipLPXYnx50) | `NULL` | [`XipLPXYnx50`](https://www.youtube.com/watch?v=XipLPXYnx50) | ✅ **`SAFE_TO_APPLY`** |
| 44 | `b4-katha-vishnu-vamana-avatar-aur-bali` | **वामन अवतार एवं दानवीर महाराज बलि के तीन पग भूमि** | 🎬 Video | [`yWUSvASnZZM`](https://www.youtube.com/watch?v=yWUSvASnZZM) | `NULL` | [`yWUSvASnZZM`](https://www.youtube.com/watch?v=yWUSvASnZZM) | ✅ **`SAFE_TO_APPLY`** |
| 45 | `b11-katha-purana-prerak-prasang-01-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 01 (अमृत कथा 11)** | 🎬 Video | [`-M-pAFWCN8U`](https://www.youtube.com/watch?v=-M-pAFWCN8U) | `NULL` | [`-M-pAFWCN8U`](https://www.youtube.com/watch?v=-M-pAFWCN8U) | ✅ **`SAFE_TO_APPLY`** |
| 46 | `b11-katha-purana-prerak-prasang-02-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 02 (अमृत कथा 11)** | 🎬 Video | [`GhZDma108S0`](https://www.youtube.com/watch?v=GhZDma108S0) | `NULL` | [`GhZDma108S0`](https://www.youtube.com/watch?v=GhZDma108S0) | ✅ **`SAFE_TO_APPLY`** |
| 47 | `b11-katha-purana-prerak-prasang-03-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 03 (अमृत कथा 11)** | 🎬 Video | [`gU6uSvuVQCY`](https://www.youtube.com/watch?v=gU6uSvuVQCY) | `NULL` | [`gU6uSvuVQCY`](https://www.youtube.com/watch?v=gU6uSvuVQCY) | ✅ **`SAFE_TO_APPLY`** |
| 48 | `b11-katha-purana-prerak-prasang-04-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 04 (अमृत कथा 11)** | 🎬 Video | [`Y46Klsd1oww`](https://www.youtube.com/watch?v=Y46Klsd1oww) | `NULL` | [`Y46Klsd1oww`](https://www.youtube.com/watch?v=Y46Klsd1oww) | ✅ **`SAFE_TO_APPLY`** |
| 49 | `b11-katha-purana-prerak-prasang-05-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 05 (अमृत कथा 11)** | 🎬 Video | [`dxmvBfcO7LM`](https://www.youtube.com/watch?v=dxmvBfcO7LM) | `NULL` | [`dxmvBfcO7LM`](https://www.youtube.com/watch?v=dxmvBfcO7LM) | ✅ **`SAFE_TO_APPLY`** |
| 50 | `b11-katha-purana-prerak-prasang-06-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 06 (अमृत कथा 11)** | 🎬 Video | [`wxwH6NHb57s`](https://www.youtube.com/watch?v=wxwH6NHb57s) | `NULL` | [`wxwH6NHb57s`](https://www.youtube.com/watch?v=wxwH6NHb57s) | ✅ **`SAFE_TO_APPLY`** |
| 51 | `b11-katha-purana-prerak-prasang-07-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 07 (अमृत कथा 11)** | 🎬 Video | [`fYEP-zOoaZI`](https://www.youtube.com/watch?v=fYEP-zOoaZI) | `NULL` | [`fYEP-zOoaZI`](https://www.youtube.com/watch?v=fYEP-zOoaZI) | ✅ **`SAFE_TO_APPLY`** |
| 52 | `b11-katha-purana-prerak-prasang-08-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 08 (अमृत कथा 11)** | 🎬 Video | [`oSTPmpX-ObQ`](https://www.youtube.com/watch?v=oSTPmpX-ObQ) | `NULL` | [`oSTPmpX-ObQ`](https://www.youtube.com/watch?v=oSTPmpX-ObQ) | ✅ **`SAFE_TO_APPLY`** |
| 53 | `b11-katha-purana-prerak-prasang-09-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (अमृत कथा 11)** | 🎬 Video | [`ANQ4FWsZ7RY`](https://www.youtube.com/watch?v=ANQ4FWsZ7RY) | `NULL` | [`ANQ4FWsZ7RY`](https://www.youtube.com/watch?v=ANQ4FWsZ7RY) | ✅ **`SAFE_TO_APPLY`** |
| 54 | `b11-katha-purana-prerak-prasang-10-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 10 (अमृत कथा 11)** | 🎬 Video | [`gN9rwoMOt5c`](https://www.youtube.com/watch?v=gN9rwoMOt5c) | `NULL` | [`gN9rwoMOt5c`](https://www.youtube.com/watch?v=gN9rwoMOt5c) | ✅ **`SAFE_TO_APPLY`** |
| 55 | `b11-katha-purana-prerak-prasang-11-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 11 (अमृत कथा 11)** | 🎬 Video | [`TwvFoi3A3ZM`](https://www.youtube.com/watch?v=TwvFoi3A3ZM) | `NULL` | [`TwvFoi3A3ZM`](https://www.youtube.com/watch?v=TwvFoi3A3ZM) | ✅ **`SAFE_TO_APPLY`** |
| 56 | `b11-katha-purana-prerak-prasang-13-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 13 (अमृत कथा 11)** | 🎬 Video | [`V0i49kMlL8A`](https://www.youtube.com/watch?v=V0i49kMlL8A) | `NULL` | [`V0i49kMlL8A`](https://www.youtube.com/watch?v=V0i49kMlL8A) | ✅ **`SAFE_TO_APPLY`** |
| 57 | `b11-katha-purana-prerak-prasang-15-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 15 (अमृत कथा 11)** | 🎬 Video | [`R9e8hSaLhIs`](https://www.youtube.com/watch?v=R9e8hSaLhIs) | `NULL` | [`R9e8hSaLhIs`](https://www.youtube.com/watch?v=R9e8hSaLhIs) | ✅ **`SAFE_TO_APPLY`** |
| 58 | `b13-katha-purana-prerak-dhara-01-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 01 (अमृत प्रसंग 13)** | 🎬 Video | [`ryiJ1XQQJgA`](https://www.youtube.com/watch?v=ryiJ1XQQJgA) | `NULL` | [`ryiJ1XQQJgA`](https://www.youtube.com/watch?v=ryiJ1XQQJgA) | ✅ **`SAFE_TO_APPLY`** |
| 59 | `b13-katha-purana-prerak-dhara-02-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 02 (अमृत प्रसंग 13)** | 🎬 Video | [`pnQAe1NyCJM`](https://www.youtube.com/watch?v=pnQAe1NyCJM) | `NULL` | [`pnQAe1NyCJM`](https://www.youtube.com/watch?v=pnQAe1NyCJM) | ✅ **`SAFE_TO_APPLY`** |
| 60 | `b13-katha-purana-prerak-dhara-03-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 03 (अमृत प्रसंग 13)** | 🎬 Video | [`D8QwTxmVkGE`](https://www.youtube.com/watch?v=D8QwTxmVkGE) | `NULL` | [`D8QwTxmVkGE`](https://www.youtube.com/watch?v=D8QwTxmVkGE) | ✅ **`SAFE_TO_APPLY`** |
| 61 | `b13-katha-purana-prerak-dhara-05-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 05 (अमृत प्रसंग 13)** | 🎬 Video | [`ueodNR6jjoY`](https://www.youtube.com/watch?v=ueodNR6jjoY) | `NULL` | [`ueodNR6jjoY`](https://www.youtube.com/watch?v=ueodNR6jjoY) | ✅ **`SAFE_TO_APPLY`** |
| 62 | `b13-katha-purana-prerak-dhara-06-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 06 (अमृत प्रसंग 13)** | 🎬 Video | [`e_4Xll5VDKI`](https://www.youtube.com/watch?v=e_4Xll5VDKI) | `NULL` | [`e_4Xll5VDKI`](https://www.youtube.com/watch?v=e_4Xll5VDKI) | ✅ **`SAFE_TO_APPLY`** |
| 63 | `b13-katha-purana-prerak-dhara-07-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 07 (अमृत प्रसंग 13)** | 🎬 Video | [`Y1IEXo4radI`](https://www.youtube.com/watch?v=Y1IEXo4radI) | `NULL` | [`Y1IEXo4radI`](https://www.youtube.com/watch?v=Y1IEXo4radI) | ✅ **`SAFE_TO_APPLY`** |
| 64 | `b13-katha-purana-prerak-dhara-09-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (अमृत प्रसंग 13)** | 🎬 Video | [`wNyglEn8peU`](https://www.youtube.com/watch?v=wNyglEn8peU) | `NULL` | [`wNyglEn8peU`](https://www.youtube.com/watch?v=wNyglEn8peU) | ✅ **`SAFE_TO_APPLY`** |
| 65 | `b13-katha-purana-prerak-dhara-10-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 10 (अमृत प्रसंग 13)** | 🎬 Video | [`lUKbavmr3hc`](https://www.youtube.com/watch?v=lUKbavmr3hc) | `NULL` | [`lUKbavmr3hc`](https://www.youtube.com/watch?v=lUKbavmr3hc) | ✅ **`SAFE_TO_APPLY`** |
| 66 | `b13-katha-purana-prerak-dhara-13-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 13 (अमृत प्रसंग 13)** | 🎬 Video | [`IC2yJoZVYUw`](https://www.youtube.com/watch?v=IC2yJoZVYUw) | `NULL` | [`IC2yJoZVYUw`](https://www.youtube.com/watch?v=IC2yJoZVYUw) | ✅ **`SAFE_TO_APPLY`** |
| 67 | `b13-katha-purana-prerak-dhara-15-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 15 (अमृत प्रसंग 13)** | 🎬 Video | [`1Gb7gF2Pywo`](https://www.youtube.com/watch?v=1Gb7gF2Pywo) | `NULL` | [`1Gb7gF2Pywo`](https://www.youtube.com/watch?v=1Gb7gF2Pywo) | ✅ **`SAFE_TO_APPLY`** |
| 68 | `b14-katha-purana-prerak-dhara-03-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 03 (अमृत प्रसंग 14)** | 🎬 Video | [`OnWGVfQrreE`](https://www.youtube.com/watch?v=OnWGVfQrreE) | `NULL` | [`OnWGVfQrreE`](https://www.youtube.com/watch?v=OnWGVfQrreE) | ✅ **`SAFE_TO_APPLY`** |
| 69 | `b14-katha-purana-prerak-dhara-08-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 08 (अमृत प्रसंग 14)** | 🎬 Video | [`Wk30WakztW4`](https://www.youtube.com/watch?v=Wk30WakztW4) | `NULL` | [`Wk30WakztW4`](https://www.youtube.com/watch?v=Wk30WakztW4) | ✅ **`SAFE_TO_APPLY`** |
| 70 | `b14-katha-purana-prerak-dhara-10-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 10 (अमृत प्रसंग 14)** | 🎬 Video | [`us7i2uk5lB4`](https://www.youtube.com/watch?v=us7i2uk5lB4) | `NULL` | [`us7i2uk5lB4`](https://www.youtube.com/watch?v=us7i2uk5lB4) | ✅ **`SAFE_TO_APPLY`** |

---

## 4. 🔒 FINAL RESULT & SAFETY GATE

```
PHASE 2N-D FINAL DRY RUN COMPLETE

Database Modified       : NO
Database Writes         : 0

Source VERIFIED_HIGH Audio : 38
Source VERIFIED_HIGH Video : 32
Source VERIFIED_HIGH Total : 70

Revalidated Audio       : 38
Revalidated Video       : 32

Still Eligible Audio    : 38
Still Eligible Video    : 32

Already Covered         : 0
Blocked / Revalidation  : 0

Duplicate IDs           : 0
Duplicate URLs          : 0
Conflicts               : 0
Cross-Field Conflicts   : 0
Overwrite Attempts      : 0
URL-ID Mismatches       : 0

Live Check Failures     : 0
Semantic Revalidation   : PASS

Proposed Audio Adds     : 38
Proposed Video Adds     : 32
Proposed Total Adds     : 70

Current Playable Audio  : 284
Current YouTube Audio   : 246
Current Video URLs      : 148

Projected Playable Audio : 322
Projected YouTube Audio   : 284
Projected Video URLs      : 180

Total Katha               : 505

Current Katha With Audio   : 223
Current Katha With Video   : 146
Current Katha With Both    : 135
Current Katha With Neither : 271

Projected Katha With Audio   : 261
Projected Katha With Video   : 178
Projected Katha With Both    : 162
Projected Katha With Neither : 228

Projected Audio Only       : 99
Projected Video Only       : 16

FTS5 Verification       : PASS
Integrity Check         : ok
Foreign-Key Violations  : 0

Katha Reconciliation    : PASS
Media Reconciliation    : PASS

Final Gate              : PASS

IMPORTANT:
No media was applied to the database during Phase 2N-D.

The Proposed Apply Set is DRY-RUN ONLY.

PHASE 2N-E APPLY MUST NOT START
until explicit user approval is received.
```
