# 📖🎬 Phase 2P-F — Global Post-Apply Audit Report

**Mode**: `STRICT READ-ONLY — POST-APPLY AUDIT ONLY` (Zero Database Writes)  
**Database File**: `db/bhakti.db` (Unchanged, 0 Writes)  
**Date**: `2026-08-31 16:12:10`  
**Final Gate Verdict**: **`PASS`**  

---

## 1. 🛡️ Global Database Baseline & Invariants

| Metric | Measured Baseline | Target Expected | Status |
| :--- | :--- | :--- | :--- |
| **Total Database Records** | **`10,010`** | `10,010` | ✅ Exact Match |
| **FTS5 Search Documents** | **`10,010`** | `10,010` | ✅ Exact Match |
| **Playable Audio Total** | **`370`** | `370` | ✅ Reconciled |
| **Local MP3 Audio** | **`38`** | `38` | ✅ Untouched |
| **YouTube HD Audio** | **`332`** | `332` | ✅ Reconciled |
| **YouTube Video URLs** | **`203`** | `203` | ✅ Reconciled |
| **Total Katha Records** | **`505`** | `505` | ✅ Authoritative Total |
| **PRAGMA integrity_check** | **`ok`** | `ok` | ✅ 0 Corruption |
| **Foreign-Key Violations** | **`0`** | `0` | ✅ 100% Valid |
| **Database Writes in Phase** | **`0`** | `0` | ✅ Strict Read-Only |

---

## 2. 📖 Katha Media Coverage & Exact Disjoint Reconciliation

Across all **505 authoritative Katha records**:

| Category Classification | Record Count | Description | Coverage % |
| :--- | :---: | :--- | :---: |
| **BOTH** | **`180`** | Records with Both Playable Audio & Video URLs | `35.64%` |
| **AUDIO_ONLY** | **`129`** | Records with Audio only (No Video) | `25.54%` |
| **VIDEO_ONLY** | **`21`** | Records with Video only (No Audio) | `4.16%` |
| **NEITHER** | **`175`** | Media-Less Backlog (Neither Audio nor Video) | `34.65%` |
| **Total Katha Population** | **`505`** | $\mathbf{180 + 129 + 21 + 175 = 505}$ | `100.00%` |

* **Katha With Audio**: **`309`** ($180 + 129 = 309$)
* **Katha With Video**: **`201`** ($180 + 21 = 201$)

---

## 3. 📋 Phase 2P Applied Mappings & Integrity Audit

* **27/27 Mappings Verified**: **`27 / 27 MATCH`** (21 Audio + 6 Video)
* **Mismatches / Missing**: **`0`**
* **Live Status (oEmbed Checked)**: **`27 / 27 LIVE_PASS`**
* **Authorized Changes**: **`27`** (Only approved 27 media fields updated)
* **Unauthorized Changes**: **`0`**
* **Duplicate YouTube Audio IDs**: **`0`** (332 unique IDs across 332 records)
* **Duplicate YouTube Video IDs**: **`0`** (203 unique IDs across 203 records)
* **Cross-Field Collisions**: **`0`** (Audio and Video IDs are 100% disjoint)
* **URL-ID Consistency & Format**: **`100% VALID`** (0 malformed URLs)
* **FTS5 Global Synchronization**: **`PASS`** (Search functional for all major deities)

---

## 4. 🔒 FINAL RESULT

```
PHASE 2P-F GLOBAL POST-APPLY AUDIT COMPLETE

Database Modified       : NO
Database Writes         : 0

Total Katha             : 505

Katha With Audio        : 309
Katha With Video        : 201
Katha With Both         : 180
Katha With Neither      : 175

Audio Only              : 129
Video Only              : 21

Current Playable Audio  : 370
Current YouTube Audio   : 332
Current Video URLs      : 203

Phase 2P Audio Added    : 21
Phase 2P Video Added    : 6
Phase 2P Total Added    : 27

27/27 Mapping Verification : PASS

Authorized Changes      : 27
Unauthorized Changes    : 0

Duplicate YouTube IDs   : 0
Duplicate YouTube URLs  : 0
Cross-Field Conflicts   : 0
URL-ID Mismatches       : 0
Malformed URLs          : 0

VERIFIED_HIGH Evidence  : 27/27
Live Verification       : PASS

Review Applied          : 0
Reject Applied          : 0
No-Suitable Applied     : 0

FTS5 Verification       : PASS
Integrity Check         : ok
Foreign-Key Violations  : 0
Schema Audit            : PASS
Backup Verification     : PASS

Katha Reconciliation    : PASS
Media Reconciliation    : PASS
Delta Reconciliation    : PASS
Apply Scope Reconciliation : PASS

Final Gate              : PASS

IMPORTANT:
Phase 2P-F performed no database modifications.

Phase 2P-E Apply:
Audio = 21
Video = 6
Total = 27

Phase 2P Discovery      : PASS
Phase 2P-D Dry Run      : PASS
Phase 2P-E Apply        : PASS
Phase 2P-F Global Audit : PASS

No corrective changes were made during Phase 2P-F.

STOP AFTER AUDIT.
```
