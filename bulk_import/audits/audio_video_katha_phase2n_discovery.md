# 📖🎬 Phase 2N — High Priority Media Discovery & Live Verification Report

**Mode**: `STRICT READ-ONLY — DISCOVERY ONLY` (Zero Database Writes)  
**Database File**: `db/bhakti.db` (Unchanged, 0 Writes)  
**Date**: `2026-08-31 13:55:25`  
**Scope**: Primary Batch (Top 50 Media-Less Katha Records from 271 Backlog)  

---

## 1. 🛡️ Database Baseline & Safety State

| Metric | Measured Baseline | Target Expected | Status |
| :--- | :--- | :--- | :--- |
| **Total Database Records** | **`10,010`** | `10,010` | ✅ Unchanged |
| **FTS5 Search Documents** | **`10,010`** | `10,010` | ✅ Unchanged |
| **Playable Audio Total** | **`284`** | `284` | ✅ Untouched |
| **Local MP3 Audio** | **`38`** | `38` | ✅ Untouched |
| **YouTube HD Audio** | **`246`** | `246` | ✅ Untouched |
| **YouTube Video URLs** | **`148`** | `148` | ✅ Untouched |
| **Total Katha Records** | **`505`** | `505` | ✅ Authoritative Total |
| **Katha With Audio** | **`223`** | `223` | ✅ Untouched |
| **Katha With Video** | **`146`** | `146` | ✅ Untouched |
| **Katha With Both** | **`135`** | `135` | ✅ Untouched |
| **Katha With Neither** | **`271`** | `271` | ✅ Untouched Backlog |
| **PRAGMA integrity_check** | **`ok`** | `ok` | ✅ 0 Corruption |
| **Foreign-Key Violations** | **`0`** | `0` | ✅ 100% Valid |
| **Database Modifications** | **`0`** | `0` | ✅ Strict Read-Only |

---

## 2. 📊 Candidate Discovery Statistics (Primary Top 50 Batch)

* **Media-Less Backlog**: **`271`**
* **Top 50 Primary Batch Processed**: **`50 / 50`** (100% Verified)
* **Secondary Batch Queue**: **`50`** (Ranks 51–100 for future planning)
* **Batch Overlap**: **`0`** (100% Disjoint)
* **VERIFIED_HIGH Audio Candidates**: **`38`**
* **VERIFIED_HIGH Video Candidates**: **`32`**
* **Total VERIFIED_HIGH Candidates**: **`70`**
* **REVIEW Candidates (Broad / Multi-Episode)**: **`67`**
* **REJECT Candidates (Bhajan / Song)**: **`16`**
* **No Suitable Candidate**: **`1`**
* **Live Check Failures (oEmbed Checked)**: **`0`**
* **Database & Batch Collisions**: **`0`** (100% Disjoint)

---

## 3. 📋 Top 50 Per-Katha Discovery Matrix

| Rank | Database ID | Katha Title | 🎧 Audio Verdict | 🎬 Video Verdict | Discovered Media Snippet |
| :---: | :--- | :--- | :---: | :---: | :--- |
| 01 | `b3-katha-krishna-geeta-updesh-vishwaroop-darshan` | **कुरुक्षेत्र में अर्जुन को श्रीमद्भगवद्गीता उपदेश एवं विश्वरूप दर्शन** | ✅ `VERIFIED_HIGH` | ⚠️ `REVIEW` | 🎧 [`RZ6zkX5DRMA`](https://www.youtube.com/watch?v=RZ6zkX5DRMA) |
| 02 | `b4-katha-krishna-geeta-upadesh-kurukshetra` | **कुरुक्षेत्र में अर्जुन विषाद एवं श्रीमद्भगवद्गीता उपदेश** | ⚠️ `NO_SUITABLE_CANDIDATE` | ⚠️ `NO_SUITABLE_CANDIDATE` | None |
| 03 | `b20-ganesh-katha-b20-458` | **भगवान गणेश दिव्य चरित्र स्तुति संकीर्तन (विंशति पद 458 - 20)** | ⚠️ `REVIEW` | ⚠️ `REVIEW` | None |
| 04 | `b20-saraswati-katha-b20-257` | **मां सरस्वती लीला प्रसंग स्तुति संकीर्तन (विंशति पद 257 - 20)** | ✅ `VERIFIED_HIGH` | ⚠️ `NO_SUITABLE_CANDIDATE` | 🎧 [`ieQhQB_y_wo`](https://www.youtube.com/watch?v=ieQhQB_y_wo) |
| 05 | `b2-katha-bhakta-prahlada-holika-dahan` | **भक्त प्रह्लाद एवं होलिका दहन (अग्नि में भी बाल न बांका)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`IAG-ndaz6oQ`](https://www.youtube.com/watch?v=IAG-ndaz6oQ)<br>🎬 [`5OJN_IjB4ZU`](https://www.youtube.com/watch?v=5OJN_IjB4ZU) |
| 06 | `b2-katha-bhakta-raja-bali-vamana-3-pag` | **राजा बलि एवं भगवान वामन: 3 पग में तीनों लोक नापना** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`vLVPM2PvmM4`](https://www.youtube.com/watch?v=vLVPM2PvmM4)<br>🎬 [`ijD9LmobncY`](https://www.youtube.com/watch?v=ijD9LmobncY) |
| 07 | `b3-katha-vishnu-narasimha-avatar-khambha-faad` | **भक्त प्रह्लाद की रक्षा हेतु भगवान नृसिंह का खंभा फाड़कर प्राकट्य** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`wTCXjSXcB74`](https://www.youtube.com/watch?v=wTCXjSXcB74)<br>🎬 [`jhSqp9J_BSc`](https://www.youtube.com/watch?v=jhSqp9J_BSc) |
| 08 | `b3-katha-vishnu-vamana-avatar-bali-daan` | **भगवान वामन अवतार एवं राजा बलि से तीन पग भूमि दान** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`fDzcm2RKM4s`](https://www.youtube.com/watch?v=fDzcm2RKM4s)<br>🎬 [`-DRgUhc8u4s`](https://www.youtube.com/watch?v=-DRgUhc8u4s) |
| 09 | `b4-katha-vishnu-narasimha-avatar-aur-prahlad` | **भगवान नृसिंह अवतार एवं भक्त प्रह्लाद की रक्षा** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`toyH8UxPqAw`](https://www.youtube.com/watch?v=toyH8UxPqAw)<br>🎬 [`XipLPXYnx50`](https://www.youtube.com/watch?v=XipLPXYnx50) |
| 10 | `b4-katha-vishnu-vamana-avatar-aur-bali` | **वामन अवतार एवं दानवीर महाराज बलि के तीन पग भूमि** | ⚠️ `NO_SUITABLE_CANDIDATE` | ✅ `VERIFIED_HIGH` | 🎬 [`yWUSvASnZZM`](https://www.youtube.com/watch?v=yWUSvASnZZM) |
| 11 | `b11-katha-purana-prerak-prasang-01-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 01 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`4-c387I-H3E`](https://www.youtube.com/watch?v=4-c387I-H3E)<br>🎬 [`-M-pAFWCN8U`](https://www.youtube.com/watch?v=-M-pAFWCN8U) |
| 12 | `b11-katha-purana-prerak-prasang-02-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 02 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`4OTNGx1nbwM`](https://www.youtube.com/watch?v=4OTNGx1nbwM)<br>🎬 [`GhZDma108S0`](https://www.youtube.com/watch?v=GhZDma108S0) |
| 13 | `b11-katha-purana-prerak-prasang-03-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 03 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`68qoYbIzYqY`](https://www.youtube.com/watch?v=68qoYbIzYqY)<br>🎬 [`gU6uSvuVQCY`](https://www.youtube.com/watch?v=gU6uSvuVQCY) |
| 14 | `b11-katha-purana-prerak-prasang-04-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 04 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`J5kpjm4ZXwg`](https://www.youtube.com/watch?v=J5kpjm4ZXwg)<br>🎬 [`Y46Klsd1oww`](https://www.youtube.com/watch?v=Y46Klsd1oww) |
| 15 | `b11-katha-purana-prerak-prasang-05-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 05 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`_Hpy1FKBZTA`](https://www.youtube.com/watch?v=_Hpy1FKBZTA)<br>🎬 [`dxmvBfcO7LM`](https://www.youtube.com/watch?v=dxmvBfcO7LM) |
| 16 | `b11-katha-purana-prerak-prasang-06-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 06 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`GuUvemahyYw`](https://www.youtube.com/watch?v=GuUvemahyYw)<br>🎬 [`wxwH6NHb57s`](https://www.youtube.com/watch?v=wxwH6NHb57s) |
| 17 | `b11-katha-purana-prerak-prasang-07-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 07 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`b7np2nlReSs`](https://www.youtube.com/watch?v=b7np2nlReSs)<br>🎬 [`fYEP-zOoaZI`](https://www.youtube.com/watch?v=fYEP-zOoaZI) |
| 18 | `b11-katha-purana-prerak-prasang-08-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 08 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`xABIG2WY8Pw`](https://www.youtube.com/watch?v=xABIG2WY8Pw)<br>🎬 [`oSTPmpX-ObQ`](https://www.youtube.com/watch?v=oSTPmpX-ObQ) |
| 19 | `b11-katha-purana-prerak-prasang-09-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`wmV2pLw_Leo`](https://www.youtube.com/watch?v=wmV2pLw_Leo)<br>🎬 [`ANQ4FWsZ7RY`](https://www.youtube.com/watch?v=ANQ4FWsZ7RY) |
| 20 | `b11-katha-purana-prerak-prasang-10-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 10 (अमृत कथा 11)** | ⚠️ `NO_SUITABLE_CANDIDATE` | ✅ `VERIFIED_HIGH` | 🎬 [`gN9rwoMOt5c`](https://www.youtube.com/watch?v=gN9rwoMOt5c) |
| 21 | `b11-katha-purana-prerak-prasang-11-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 11 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`kHy4IADSKik`](https://www.youtube.com/watch?v=kHy4IADSKik)<br>🎬 [`TwvFoi3A3ZM`](https://www.youtube.com/watch?v=TwvFoi3A3ZM) |
| 22 | `b11-katha-purana-prerak-prasang-12-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 12 (अमृत कथा 11)** | ⚠️ `REVIEW` | ⚠️ `REVIEW` | None |
| 23 | `b11-katha-purana-prerak-prasang-13-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 13 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`mWg4kcKSEus`](https://www.youtube.com/watch?v=mWg4kcKSEus)<br>🎬 [`V0i49kMlL8A`](https://www.youtube.com/watch?v=V0i49kMlL8A) |
| 24 | `b11-katha-purana-prerak-prasang-14-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 14 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ⚠️ `NO_SUITABLE_CANDIDATE` | 🎧 [`mYemCfhwA80`](https://www.youtube.com/watch?v=mYemCfhwA80) |
| 25 | `b11-katha-purana-prerak-prasang-15-b11` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 15 (अमृत कथा 11)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`ZSqrqPJpQ90`](https://www.youtube.com/watch?v=ZSqrqPJpQ90)<br>🎬 [`R9e8hSaLhIs`](https://www.youtube.com/watch?v=R9e8hSaLhIs) |
| 26 | `b13-katha-purana-prerak-dhara-01-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 01 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`bkChXn-8Awg`](https://www.youtube.com/watch?v=bkChXn-8Awg)<br>🎬 [`ryiJ1XQQJgA`](https://www.youtube.com/watch?v=ryiJ1XQQJgA) |
| 27 | `b13-katha-purana-prerak-dhara-02-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 02 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`2j2iHzymm6Q`](https://www.youtube.com/watch?v=2j2iHzymm6Q)<br>🎬 [`pnQAe1NyCJM`](https://www.youtube.com/watch?v=pnQAe1NyCJM) |
| 28 | `b13-katha-purana-prerak-dhara-03-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 03 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`Ncx1PXgY4LQ`](https://www.youtube.com/watch?v=Ncx1PXgY4LQ)<br>🎬 [`D8QwTxmVkGE`](https://www.youtube.com/watch?v=D8QwTxmVkGE) |
| 29 | `b13-katha-purana-prerak-dhara-04-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 04 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ⚠️ `NO_SUITABLE_CANDIDATE` | 🎧 [`Fi0wKb_u2_g`](https://www.youtube.com/watch?v=Fi0wKb_u2_g) |
| 30 | `b13-katha-purana-prerak-dhara-05-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 05 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`zXje2iT7Cd4`](https://www.youtube.com/watch?v=zXje2iT7Cd4)<br>🎬 [`ueodNR6jjoY`](https://www.youtube.com/watch?v=ueodNR6jjoY) |
| 31 | `b13-katha-purana-prerak-dhara-06-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 06 (अमृत प्रसंग 13)** | ⚠️ `REVIEW` | ✅ `VERIFIED_HIGH` | 🎬 [`e_4Xll5VDKI`](https://www.youtube.com/watch?v=e_4Xll5VDKI) |
| 32 | `b13-katha-purana-prerak-dhara-07-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 07 (अमृत प्रसंग 13)** | ⚠️ `REVIEW` | ✅ `VERIFIED_HIGH` | 🎬 [`Y1IEXo4radI`](https://www.youtube.com/watch?v=Y1IEXo4radI) |
| 33 | `b13-katha-purana-prerak-dhara-08-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 08 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ⚠️ `REVIEW` | 🎧 [`C-Cq90fOg0E`](https://www.youtube.com/watch?v=C-Cq90fOg0E) |
| 34 | `b13-katha-purana-prerak-dhara-09-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`jqUi5bDKLS4`](https://www.youtube.com/watch?v=jqUi5bDKLS4)<br>🎬 [`wNyglEn8peU`](https://www.youtube.com/watch?v=wNyglEn8peU) |
| 35 | `b13-katha-purana-prerak-dhara-10-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 10 (अमृत प्रसंग 13)** | ⚠️ `REVIEW` | ✅ `VERIFIED_HIGH` | 🎬 [`lUKbavmr3hc`](https://www.youtube.com/watch?v=lUKbavmr3hc) |
| 36 | `b13-katha-purana-prerak-dhara-11-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 11 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ⚠️ `NO_SUITABLE_CANDIDATE` | 🎧 [`g2J39TOXUWg`](https://www.youtube.com/watch?v=g2J39TOXUWg) |
| 37 | `b13-katha-purana-prerak-dhara-12-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 12 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ⚠️ `REVIEW` | 🎧 [`u7y8GOO9wKM`](https://www.youtube.com/watch?v=u7y8GOO9wKM) |
| 38 | `b13-katha-purana-prerak-dhara-13-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 13 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`aQNdphh3n5U`](https://www.youtube.com/watch?v=aQNdphh3n5U)<br>🎬 [`IC2yJoZVYUw`](https://www.youtube.com/watch?v=IC2yJoZVYUw) |
| 39 | `b13-katha-purana-prerak-dhara-14-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 14 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ⚠️ `NO_SUITABLE_CANDIDATE` | 🎧 [`2G0Eg2sUqfs`](https://www.youtube.com/watch?v=2G0Eg2sUqfs) |
| 40 | `b13-katha-purana-prerak-dhara-15-b13` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 15 (अमृत प्रसंग 13)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`NFxci9WqHK4`](https://www.youtube.com/watch?v=NFxci9WqHK4)<br>🎬 [`1Gb7gF2Pywo`](https://www.youtube.com/watch?v=1Gb7gF2Pywo) |
| 41 | `b14-katha-purana-prerak-dhara-01-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 01 (अमृत प्रसंग 14)** | ✅ `VERIFIED_HIGH` | ⚠️ `NO_SUITABLE_CANDIDATE` | 🎧 [`z8K-CEkErF8`](https://www.youtube.com/watch?v=z8K-CEkErF8) |
| 42 | `b14-katha-purana-prerak-dhara-02-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 02 (अमृत प्रसंग 14)** | ⚠️ `REVIEW` | ⚠️ `REVIEW` | None |
| 43 | `b14-katha-purana-prerak-dhara-03-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 03 (अमृत प्रसंग 14)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`vM6Wu8yUqXw`](https://www.youtube.com/watch?v=vM6Wu8yUqXw)<br>🎬 [`OnWGVfQrreE`](https://www.youtube.com/watch?v=OnWGVfQrreE) |
| 44 | `b14-katha-purana-prerak-dhara-04-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 04 (अमृत प्रसंग 14)** | ⚠️ `REVIEW` | ⚠️ `REVIEW` | None |
| 45 | `b14-katha-purana-prerak-dhara-05-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 05 (अमृत प्रसंग 14)** | ✅ `VERIFIED_HIGH` | ⚠️ `REVIEW` | 🎧 [`2pRCRBbq4fw`](https://www.youtube.com/watch?v=2pRCRBbq4fw) |
| 46 | `b14-katha-purana-prerak-dhara-06-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 06 (अमृत प्रसंग 14)** | ⚠️ `REVIEW` | ⚠️ `REVIEW` | None |
| 47 | `b14-katha-purana-prerak-dhara-07-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 07 (अमृत प्रसंग 14)** | ✅ `VERIFIED_HIGH` | ⚠️ `REVIEW` | 🎧 [`1Gcv2tFD5Hc`](https://www.youtube.com/watch?v=1Gcv2tFD5Hc) |
| 48 | `b14-katha-purana-prerak-dhara-08-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 08 (अमृत प्रसंग 14)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`JKORWjNupfY`](https://www.youtube.com/watch?v=JKORWjNupfY)<br>🎬 [`Wk30WakztW4`](https://www.youtube.com/watch?v=Wk30WakztW4) |
| 49 | `b14-katha-purana-prerak-dhara-09-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (अमृत प्रसंग 14)** | ⚠️ `REVIEW` | ⚠️ `REVIEW` | None |
| 50 | `b14-katha-purana-prerak-dhara-10-b14` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 10 (अमृत प्रसंग 14)** | ✅ `VERIFIED_HIGH` | ✅ `VERIFIED_HIGH` | 🎧 [`gpLFo1zPNHg`](https://www.youtube.com/watch?v=gpLFo1zPNHg)<br>🎬 [`us7i2uk5lB4`](https://www.youtube.com/watch?v=us7i2uk5lB4) |

---

## 4. 🔒 FINAL RESULT

```
PHASE 2N HIGH PRIORITY MEDIA DISCOVERY COMPLETE

Database Modified       : NO
Database Writes         : 0

Media-Less Backlog      : 271

Top 50 Kathas           : 50
Secondary Batch         : 50
Batch Overlap           : 0

VERIFIED_HIGH Audio     : 38
VERIFIED_HIGH Video     : 32
Total VERIFIED_HIGH     : 70

REVIEW Candidates       : 67
REJECT Candidates       : 16
No Suitable Candidate   : 1

Live Check Failures     : 0
Conflicts               : 0
Duplicate IDs           : 0
Duplicate URLs          : 0
Cross-Field Conflicts   : 0

Current Playable Audio  : 284
Current YouTube Audio   : 246
Current Video URLs      : 148

Total Katha             : 505
Katha With Audio        : 223
Katha With Video        : 146
Katha With Both         : 135
Katha With Neither      : 271

Integrity Check         : ok
Foreign-Key Violations  : 0

Final Gate              : PASS

IMPORTANT:
No media was applied to the database during Phase 2N.

All VERIFIED_HIGH candidates are awaiting the separate:

PHASE 2N-D FINAL DRY RUN
```
