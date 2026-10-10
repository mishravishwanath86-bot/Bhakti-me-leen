# 📖🎬 Phase 2P-E — Verified Media Apply Report

**Apply Mode**: `CONTROLLED WRITE — APPLY ONLY 2P-D APPROVED MAPPINGS`  
**Database**: `db/bhakti.db`  
**Verified Pre-Apply Backup**: [`db/backups/bhakti_pre_phase2p_e_apply_backup.db`](file:///C:/Users/vishw/.gemini/antigravity-ide/scratch/bhakti-app/db/backups/bhakti_pre_phase2p_e_apply_backup.db)  
**Manifest Source**: [`bulk_import/audits/audio_video_katha_phase2p_d_dry_run.json`](file:///C:/Users/vishw/.gemini/antigravity-ide/scratch/bhakti-app/bulk_import/audits/audio_video_katha_phase2p_d_dry_run.json)  
**Date**: `2026-08-31 16:09:48`  
**Status**: `SUCCESS`  

---

## 1. 🛡️ Database Baseline & Final Verified State

| Metric | Pre-Apply Baseline | Target Expected | Final Verified State | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Total Database Records** | `10,010` | `10,010` | **`10,010`** | ✅ Exact Match |
| **FTS5 Search Documents** | `10,010` | `10,010` | **`10,010`** | ✅ Exact Match |
| **Playable Audio Total** | `349` | `370` (+21) | **`370`** | 🎯 Audio Expansion |
| **Local MP3 Audio** | `38` | `38` | **`38`** | ✅ Untouched |
| **YouTube HD Audio** | `311` | `332` (+21) | **`332`** | 🎧 +21 Verified Spoken Kathas |
| **YouTube Video URLs** | `197` | `203` (+6) | **`203`** | 🎬 +6 Verified Video Discourses |
| **Duplicate YouTube IDs** | `0` | `0` | **`0`** (332/332 Audio, 203/203 Video) | ✅ 100% Collision-Free |
| **PRAGMA integrity_check** | `ok` | `ok` | **`ok`** | ✅ 0 Corruption |
| **Foreign-Key Violations** | `0` | `0` | **`0`** | ✅ 100% Valid |

---

## 2. 📖 Katha Media Coverage State Evolution Across All 505 Records

| Katha Category Metric | Before Phase 2P-E | After Phase 2P-E Apply | Change |
| :--- | :---: | :---: | :---: |
| **Katha With Audio** | `288` | **`309`** | +21 |
| **Katha With Video** | `195` | **`201`** | +6 |
| **Katha With Both Media** | `174` | **`180`** | +6 |
| **Katha With Neither Media (Gaps)** | `196` | **`175`** | -21 |

* **Exact Disjoint Partition**: Both (`180`) + Audio Only (`129`) + Video Only (`21`) + Neither (`175`) = **`505`**

---

## 3. 📋 Applied Mappings Sample (27 / 27 PASS)

| # | Database Record ID | Katha Title | Media Type | YouTube Video ID | Applied YouTube URL | Status |
| :---: | :--- | :--- | :---: | :---: | :--- | :---: |
| 01 | `b15-katha-purana-prerak-dhara-06-b15` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 06 (अमृत प्रसंग 15)** | 🎧 Audio | [`fQse0WNm0hE`](https://www.youtube.com/watch?v=fQse0WNm0hE) | [https://www.youtube.com/watch?v=fQse0WNm0hE](https://www.youtube.com/watch?v=fQse0WNm0hE) | ✅ **PASS** |
| 02 | `b17-katha-purana-prerak-dhara-01-b17` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 01 (सप्तदश प्रसंग 17)** | 🎧 Audio | [`u8MhrVKyWcc`](https://www.youtube.com/watch?v=u8MhrVKyWcc) | [https://www.youtube.com/watch?v=u8MhrVKyWcc](https://www.youtube.com/watch?v=u8MhrVKyWcc) | ✅ **PASS** |
| 03 | `b17-katha-purana-prerak-dhara-09-b17` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (सप्तदश प्रसंग 17)** | 🎧 Audio | [`TWq8fp-i-Ec`](https://www.youtube.com/watch?v=TWq8fp-i-Ec) | [https://www.youtube.com/watch?v=TWq8fp-i-Ec](https://www.youtube.com/watch?v=TWq8fp-i-Ec) | ✅ **PASS** |
| 04 | `b17-katha-purana-prerak-dhara-11-b17` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 11 (सप्तदश प्रसंग 17)** | 🎧 Audio | [`txTwNo2XUJ4`](https://www.youtube.com/watch?v=txTwNo2XUJ4) | [https://www.youtube.com/watch?v=txTwNo2XUJ4](https://www.youtube.com/watch?v=txTwNo2XUJ4) | ✅ **PASS** |
| 05 | `b17-katha-purana-prerak-dhara-13-b17` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 13 (सप्तदश प्रसंग 17)** | 🎧 Audio | [`VjeMCAhYPSY`](https://www.youtube.com/watch?v=VjeMCAhYPSY) | [https://www.youtube.com/watch?v=VjeMCAhYPSY](https://www.youtube.com/watch?v=VjeMCAhYPSY) | ✅ **PASS** |
| 06 | `b17-katha-purana-prerak-dhara-14-b17` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 14 (सप्तदश प्रसंग 17)** | 🎧 Audio | [`IrG57AAvNsI`](https://www.youtube.com/watch?v=IrG57AAvNsI) | [https://www.youtube.com/watch?v=IrG57AAvNsI](https://www.youtube.com/watch?v=IrG57AAvNsI) | ✅ **PASS** |
| 07 | `b18-katha-purana-prerak-dhara-01-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 01 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`DtiQ70LJ-es`](https://www.youtube.com/watch?v=DtiQ70LJ-es) | [https://www.youtube.com/watch?v=DtiQ70LJ-es](https://www.youtube.com/watch?v=DtiQ70LJ-es) | ✅ **PASS** |
| 08 | `b18-katha-purana-prerak-dhara-02-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 02 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`LXxQS3wFPYY`](https://www.youtube.com/watch?v=LXxQS3wFPYY) | [https://www.youtube.com/watch?v=LXxQS3wFPYY](https://www.youtube.com/watch?v=LXxQS3wFPYY) | ✅ **PASS** |
| 09 | `b18-katha-purana-prerak-dhara-03-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 03 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`uk2hb0Up61g`](https://www.youtube.com/watch?v=uk2hb0Up61g) | [https://www.youtube.com/watch?v=uk2hb0Up61g](https://www.youtube.com/watch?v=uk2hb0Up61g) | ✅ **PASS** |
| 10 | `b18-katha-purana-prerak-dhara-04-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 04 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`pW8EC2cTng8`](https://www.youtube.com/watch?v=pW8EC2cTng8) | [https://www.youtube.com/watch?v=pW8EC2cTng8](https://www.youtube.com/watch?v=pW8EC2cTng8) | ✅ **PASS** |
| 11 | `b18-katha-purana-prerak-dhara-05-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 05 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`iSR-uJvVm80`](https://www.youtube.com/watch?v=iSR-uJvVm80) | [https://www.youtube.com/watch?v=iSR-uJvVm80](https://www.youtube.com/watch?v=iSR-uJvVm80) | ✅ **PASS** |
| 12 | `b18-katha-purana-prerak-dhara-07-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 07 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`OcvNpK9U6aw`](https://www.youtube.com/watch?v=OcvNpK9U6aw) | [https://www.youtube.com/watch?v=OcvNpK9U6aw](https://www.youtube.com/watch?v=OcvNpK9U6aw) | ✅ **PASS** |
| 13 | `b18-katha-purana-prerak-dhara-09-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`J6-vd4RJsSM`](https://www.youtube.com/watch?v=J6-vd4RJsSM) | [https://www.youtube.com/watch?v=J6-vd4RJsSM](https://www.youtube.com/watch?v=J6-vd4RJsSM) | ✅ **PASS** |
| 14 | `b18-katha-purana-prerak-dhara-11-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 11 (अष्टादश प्रसंग 18)** | 🎧 Audio | [`bD8h_ukZjsY`](https://www.youtube.com/watch?v=bD8h_ukZjsY) | [https://www.youtube.com/watch?v=bD8h_ukZjsY](https://www.youtube.com/watch?v=bD8h_ukZjsY) | ✅ **PASS** |
| 15 | `b19-corpus19-hanuman-katha-127` | **हनुमत लंका दहन पावन कथा (एकोनविंशति पद 127)** | 🎧 Audio | [`zLDnxsOpLCc`](https://www.youtube.com/watch?v=zLDnxsOpLCc) | [https://www.youtube.com/watch?v=zLDnxsOpLCc](https://www.youtube.com/watch?v=zLDnxsOpLCc) | ✅ **PASS** |
| 16 | `b19-corpus19-hanuman-katha-128` | **हनुमत लंका दहन पावन कथा (एकोनविंशति पद 128)** | 🎧 Audio | [`nmvD1v2x8hQ`](https://www.youtube.com/watch?v=nmvD1v2x8hQ) | [https://www.youtube.com/watch?v=nmvD1v2x8hQ](https://www.youtube.com/watch?v=nmvD1v2x8hQ) | ✅ **PASS** |
| 17 | `b19-corpus19-hanuman-katha-129` | **हनुमत लंका दहन पावन कथा (एकोनविंशति पद 129)** | 🎧 Audio | [`ZLggOigFaho`](https://www.youtube.com/watch?v=ZLggOigFaho) | [https://www.youtube.com/watch?v=ZLggOigFaho](https://www.youtube.com/watch?v=ZLggOigFaho) | ✅ **PASS** |
| 18 | `b19-corpus19-hanuman-katha-130` | **हनुमत लंका दहन पावन कथा (एकोनविंशति पद 130)** | 🎧 Audio | [`zLd9Ty_6W2I`](https://www.youtube.com/watch?v=zLd9Ty_6W2I) | [https://www.youtube.com/watch?v=zLd9Ty_6W2I](https://www.youtube.com/watch?v=zLd9Ty_6W2I) | ✅ **PASS** |
| 19 | `b19-corpus19-hanuman-katha-131` | **हनुमत लंका दहन पावन कथा (एकोनविंशति पद 131)** | 🎧 Audio | [`oTebKh1U9FA`](https://www.youtube.com/watch?v=oTebKh1U9FA) | [https://www.youtube.com/watch?v=oTebKh1U9FA](https://www.youtube.com/watch?v=oTebKh1U9FA) | ✅ **PASS** |
| 20 | `b19-corpus19-hanuman-katha-134` | **हनुमत लंका दहन पावन कथा (एकोनविंशति पद 134)** | 🎧 Audio | [`PZneGUNqto4`](https://www.youtube.com/watch?v=PZneGUNqto4) | [https://www.youtube.com/watch?v=PZneGUNqto4](https://www.youtube.com/watch?v=PZneGUNqto4) | ✅ **PASS** |
| 21 | `b2-katha-hanuman-ahravana-vadh-patala` | **अहिरावण वध एवं पाताल लोक विजय** | 🎧 Audio | [`TYkeixhzru8`](https://www.youtube.com/watch?v=TYkeixhzru8) | [https://www.youtube.com/watch?v=TYkeixhzru8](https://www.youtube.com/watch?v=TYkeixhzru8) | ✅ **PASS** |
| 22 | `b17-katha-purana-prerak-dhara-09-b17` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 09 (सप्तदश प्रसंग 17)** | 🎬 Video | [`PLjI0i2oyIY`](https://www.youtube.com/watch?v=PLjI0i2oyIY) | [https://www.youtube.com/watch?v=PLjI0i2oyIY](https://www.youtube.com/watch?v=PLjI0i2oyIY) | ✅ **PASS** |
| 23 | `b18-katha-purana-prerak-dhara-02-b18` | **सनातन धर्म पावन पुराण प्रेरक प्रसंग 02 (अष्टादश प्रसंग 18)** | 🎬 Video | [`0RfjTfz-x6Q`](https://www.youtube.com/watch?v=0RfjTfz-x6Q) | [https://www.youtube.com/watch?v=0RfjTfz-x6Q](https://www.youtube.com/watch?v=0RfjTfz-x6Q) | ✅ **PASS** |
| 24 | `b19-corpus19-hanuman-katha-127` | **हनुमत लंका दहन पावन कथा (एकोनविंशति पद 127)** | 🎬 Video | [`nMmxtk7j6CY`](https://www.youtube.com/watch?v=nMmxtk7j6CY) | [https://www.youtube.com/watch?v=nMmxtk7j6CY](https://www.youtube.com/watch?v=nMmxtk7j6CY) | ✅ **PASS** |
| 25 | `b19-corpus19-hanuman-katha-128` | **हनुमत लंका दहन पावन कथा (एकोनविंशति पद 128)** | 🎬 Video | [`hFSXmnwDgrw`](https://www.youtube.com/watch?v=hFSXmnwDgrw) | [https://www.youtube.com/watch?v=hFSXmnwDgrw](https://www.youtube.com/watch?v=hFSXmnwDgrw) | ✅ **PASS** |
| 26 | `b19-corpus19-hanuman-katha-129` | **हनुमत लंका दहन पावन कथा (एकोनविंशति पद 129)** | 🎬 Video | [`5Pj601jOA74`](https://www.youtube.com/watch?v=5Pj601jOA74) | [https://www.youtube.com/watch?v=5Pj601jOA74](https://www.youtube.com/watch?v=5Pj601jOA74) | ✅ **PASS** |
| 27 | `b2-katha-hanuman-ahravana-vadh-patala` | **अहिरावण वध एवं पाताल लोक विजय** | 🎬 Video | [`hygusqE4ZMY`](https://www.youtube.com/watch?v=hygusqE4ZMY) | [https://www.youtube.com/watch?v=hygusqE4ZMY](https://www.youtube.com/watch?v=hygusqE4ZMY) | ✅ **PASS** |

---

## 4. 🔒 FINAL RESULT

```
PHASE 2P-E VERIFIED MEDIA APPLY COMPLETE

Database Modified       : YES
Database Writes         : 27

Approved Audio          : 21
Approved Video          : 6
Approved Total          : 27

Audio Applied           : 21
Video Applied           : 6
Total Applied           : 27

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

27/27 Mapping Verification : PASS

Live Verification       : PASS

Pre-Apply Playable Audio : 349
Post-Apply Playable Audio: 370
Playable Audio Delta     : +21

Pre-Apply YouTube Audio  : 311
Post-Apply YouTube Audio : 332
YouTube Audio Delta      : +21

Pre-Apply Video URLs     : 197
Post-Apply Video URLs    : 203
Video URL Delta          : +6

Katha With Audio        : 309
Katha With Video        : 201
Katha With Both         : 180
Katha With Neither      : 175

Audio Only              : 129
Video Only              : 21

FTS5 Verification       : PASS
Integrity Check         : ok
Foreign-Key Violations  : 0
Schema Audit            : PASS

Katha Reconciliation    : PASS
Delta Reconciliation    : PASS

Transaction             : COMMITTED

Final Gate              : PASS

IMPORTANT:
Phase 2P-E applied ONLY the Phase 2P-D approved mappings.

No REVIEW, REJECT, or NO_SUITABLE candidate was applied.

DO NOT automatically start Phase 2P-F.
STOP AFTER APPLY AUDIT.
```
