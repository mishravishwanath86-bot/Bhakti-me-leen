# 📖🎬 Phase 2Q-F — Global Post-Apply Audit Report

**Mode**: `STRICT READ-ONLY — POST-APPLY AUDIT ONLY` (Zero Database Writes)  
**Database File**: `db/bhakti.db` (Unchanged, 0 Writes)  
**Date**: `2026-08-31 16:23:14`  
**Final Gate Verdict**: **`PASS`**  

---

## 1. 🛡️ Global Database Baseline & Invariants

| Metric | Measured Baseline | Target Expected | Status |
| :--- | :--- | :--- | :--- |
| **Total Database Records** | **`10,010`** | `10,010` | ✅ Exact Match |
| **FTS5 Search Documents** | **`10,010`** | `10,010` | ✅ Exact Match |
| **Playable Audio Total** | **`394`** | `394` | ✅ Reconciled |
| **Local MP3 Audio** | **`38`** | `38` | ✅ Untouched |
| **YouTube HD Audio** | **`356`** | `356` | ✅ Reconciled |
| **YouTube Video URLs** | **`226`** | `226` | ✅ Reconciled |
| **Total Katha Records** | **`505`** | `505` | ✅ Authoritative Total |
| **PRAGMA integrity_check** | **`ok`** | `ok` | ✅ 0 Corruption |
| **Foreign-Key Violations** | **`0`** | `0` | ✅ 100% Valid |
| **Database Writes in Phase** | **`0`** | `0` | ✅ Strict Read-Only |

---

## 2. 📖 Katha Media Coverage & Exact Disjoint Reconciliation

Across all **505 authoritative Katha records**:

| Category Classification | Record Count | Description | Coverage % |
| :--- | :---: | :--- | :---: |
| **BOTH** | **`200`** | Records with Both Playable Audio & Video URLs | `39.60%` |
| **AUDIO_ONLY** | **`133`** | Records with Audio only (No Video) | `26.34%` |
| **VIDEO_ONLY** | **`24`** | Records with Video only (No Audio) | `4.75%` |
| **NEITHER** | **`148`** | Media-Less Backlog (Neither Audio nor Video) | `29.31%` |
| **Total Katha Population** | **`505`** | $\mathbf{200 + 133 + 24 + 148 = 505}$ | `100.00%` |

* **Katha With Audio**: **`333`** ($200 + 133 = 333$)
* **Katha With Video**: **`224`** ($200 + 24 = 224$)

---

## 3. 📋 Phase 2Q Applied Mappings & Integrity Audit

* **47/47 Mappings Verified**: **`47 / 47 MATCH`** (24 Audio + 23 Video)
* **Mismatches / Missing**: **`0`**
* **Live Status (oEmbed Checked)**: **`47 / 47 LIVE_PASS`**
* **Authorized Changes**: **`47`** (Only approved 47 media fields updated)
* **Unauthorized Changes**: **`0`**
* **Duplicate YouTube Audio IDs**: **`0`** (356 unique IDs across 356 records)
* **Duplicate YouTube Video IDs**: **`0`** (226 unique IDs across 226 records)
* **Cross-Field Collisions**: **`0`** (Audio and Video IDs are 100% disjoint)
* **URL-ID Consistency & Format**: **`100% VALID`** (0 malformed URLs)
* **FTS5 Global Synchronization**: **`PASS`** (Search functional for all major deities)

---

## 4. 🔒 FINAL RESULT

```
PHASE 2Q-F GLOBAL POST-APPLY AUDIT COMPLETE

Database Modified       : NO
Database Writes         : 0

Total Katha             : 505

Katha With Audio        : 333
Katha With Video        : 224
Katha With Both         : 200
Katha With Neither      : 148

Audio Only              : 133
Video Only              : 24

Current Playable Audio  : 394
Current YouTube Audio   : 356
Current Video URLs      : 226

Phase 2Q Audio Added    : 24
Phase 2Q Video Added    : 23
Phase 2Q Total Added    : 47

47/47 Mapping Verification : PASS

Authorized Changes      : 47
Unauthorized Changes    : 0

Duplicate YouTube IDs   : 0
Duplicate YouTube URLs  : 0
Cross-Field Conflicts   : 0
URL-ID Mismatches       : 0
Malformed URLs          : 0

Overwrite Attempts      : 0

VERIFIED_HIGH Evidence  : 47/47
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
Phase 2Q-F performed no database modifications.

Phase 2Q-E Apply:
Audio = 24
Video = 23
Total = 47

Phase 2Q Discovery      : PASS
Phase 2Q-D Dry Run      : PASS
Phase 2Q-E Apply        : PASS
Phase 2Q-F Global Audit : PASS

No corrective changes were made during Phase 2Q-F.

STOP AFTER AUDIT.
```
