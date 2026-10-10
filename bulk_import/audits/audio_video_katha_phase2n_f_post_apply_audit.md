# 📖🎬 Phase 2N-F — Global Post-Apply Audit Report

**Mode**: `STRICT READ-ONLY — POST-APPLY AUDIT ONLY` (Zero Database Writes)  
**Database File**: `db/bhakti.db` (Unchanged, 0 Writes)  
**Date**: `2026-08-31 15:45:06`  
**Final Gate Verdict**: **`PASS`**  

---

## 1. 🛡️ Global Database Baseline & Invariants

| Metric | Measured Baseline | Target Expected | Status |
| :--- | :--- | :--- | :--- |
| **Total Database Records** | **`10,010`** | `10,010` | ✅ Exact Match |
| **FTS5 Search Documents** | **`10,010`** | `10,010` | ✅ Exact Match |
| **Playable Audio Total** | **`322`** | `322` | ✅ Reconciled |
| **Local MP3 Audio** | **`38`** | `38` | ✅ Untouched |
| **YouTube HD Audio** | **`284`** | `284` | ✅ Reconciled |
| **YouTube Video URLs** | **`180`** | `180` | ✅ Reconciled |
| **Total Katha Records** | **`505`** | `505` | ✅ Authoritative Total |
| **PRAGMA integrity_check** | **`ok`** | `ok` | ✅ 0 Corruption |
| **Foreign-Key Violations** | **`0`** | `0` | ✅ 100% Valid |
| **Database Writes in Phase** | **`0`** | `0` | ✅ Strict Read-Only |

---

## 2. 📖 Katha Media Coverage & Exact Disjoint Reconciliation

Across all **505 authoritative Katha records**:

| Category Classification | Record Count | Description | Coverage % |
| :--- | :---: | :--- | :---: |
| **BOTH** | **`162`** | Records with Both Playable Audio & Video URLs | `32.08%` |
| **AUDIO_ONLY** | **`99`** | Records with Audio only (No Video) | `19.6%` |
| **VIDEO_ONLY** | **`16`** | Records with Video only (No Audio) | `3.17%` |
| **NEITHER** | **`228`** | Media-Less Backlog (Neither Audio nor Video) | `45.15%` |
| **Total Katha Population** | **`505`** | $\mathbf{162 + 99 + 16 + 228 = 505}$ | `100.00%` |

* **Katha With Audio**: **`261`** ($162 + 99 = 261$)
* **Katha With Video**: **`178`** ($162 + 16 = 178$)

---

## 3. 📋 Phase 2N Applied Mappings & Integrity Audit

* **70/70 Mappings Verified**: **`70 / 70 MATCH`** (38 Audio + 32 Video)
* **Mismatches / Missing**: **`0`**
* **Live Status (oEmbed Checked)**: **`70 / 70 LIVE_PASS`**
* **Unauthorized Changes**: **`0`** (Only approved 70 media fields updated)
* **Duplicate YouTube Audio IDs**: **`0`** (284 unique IDs across 284 records)
* **Duplicate YouTube Video IDs**: **`0`** (180 unique IDs across 180 records)
* **Cross-Field Collisions**: **`0`** (Audio and Video IDs are 100% disjoint)
* **URL-ID Consistency & Format**: **`100% VALID`** (0 malformed URLs)
* **FTS5 Global Synchronization**: **`PASS`** (Search functional for all major deities)

---

## 4. 🔒 FINAL RESULT

```
PHASE 2N-F GLOBAL POST-APPLY AUDIT COMPLETE

Database Modified       : NO
Database Writes         : 0

Total Katha             : 505

Katha With Audio        : 261
Katha With Video        : 178
Katha With Both         : 162
Katha With Neither      : 228

Audio Only              : 99
Video Only              : 16

Current Playable Audio  : 322
Current YouTube Audio   : 284
Current Video URLs      : 180

Phase 2N Audio Added    : 38
Phase 2N Video Added    : 32
Phase 2N Total Added    : 70

70/70 Mapping Verification : PASS

Unauthorized Changes    : 0
Duplicate YouTube IDs   : 0
Duplicate YouTube URLs  : 0
Cross-Field Conflicts   : 0
URL-ID Mismatches       : 0
Malformed URLs          : 0

VERIFIED_HIGH Evidence  : 70/70
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

Final Gate              : PASS

IMPORTANT:
Phase 2N-F performed no database modifications.

Phase 2N Discovery      : PASS
Phase 2N-D Dry Run      : PASS
Phase 2N-E Apply        : PASS
Phase 2N-F Global Audit  : PASS

No corrective changes were made during Phase 2N-F.
```
