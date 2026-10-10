# 📖🎬 Phase 2L-F — Global Post-Apply Reconciliation Report

**Mode**: `STRICT READ-ONLY — POST-APPLY AUDIT ONLY` (Zero Database Writes)  
**Database File**: `db/bhakti.db`  
**Date**: `2026-08-31 12:39:02`  
**Final Gate Verdict**: **`PASS`**  

---

## 1. 🛡️ Global Database Baseline & Integrity

| Metric | Before Phase 2L-E | Target Expected | Final Post-Apply State | Delta |
| :--- | :--- | :--- | :--- | :---: |
| **Total Database Records** | `10,010` | `10,010` | **`10,010`** | 0 |
| **FTS5 Search Documents** | `10,010` | `10,010` | **`10,010`** | 0 |
| **Playable Audio Total** | `198` | `240` (+42) | **`240`** | +42 |
| **Local MP3 Audio** | `38` | `38` | **`38`** | 0 |
| **YouTube HD Audio** | `160` | `202` (+42) | **`202`** | +42 |
| **YouTube Video URLs** | `72` | `109` (+37) | **`109`** | +37 |
| **PRAGMA integrity_check** | `ok` | `ok` | **`ok`** | ✅ 0 Corruption |
| **Foreign-Key Violations** | `0` | `0` | **`0`** | ✅ 100% Valid |

---

## 2. 📋 Phase 2L-E 79 Mappings Post-Apply Verification

* **Mappings Verified in DB**: **`79 / 79 PASS`** (42 Audio + 37 Video)
* **Mismatches Detected**: **`0`**
* **Duplicate YouTube Audio IDs**: **`0`** (202 unique IDs across 202 records)
* **Duplicate YouTube Video IDs**: **`0`** (109 unique IDs across 109 records)
* **Cross-Field Collisions**: **`0`** (Audio and Video IDs are 100% disjoint)
* **Excluded Candidates Applied**: **`0`** (38 Review + 34 Reject preserved unapplied)

---

## 3. 📖 Katha Media Coverage & Disjoint Mutually Exclusive Classification

Across all **505 authoritative Katha records**:

| Category Classification | Record Count | Description | Coverage % |
| :--- | :---: | :--- | :---: |
| **BOTH** | **`98`** | Records with Both Playable Audio & Video URLs | `19.41%` |
| **AUDIO_ONLY** | **`81`** | Records with Audio only (No Video) | `16.04%` |
| **VIDEO_ONLY** | **`9`** | Records with Video only (No Audio) | `1.78%` |
| **NEITHER** | **`317`** | Media-Less Backlog (Neither Audio nor Video) | `62.77%` |
| **Total Katha Population** | **`505`** | $\mathbf{98 + 81 + 9 + 317 = 505}$ (100% Exact Partition) | `100.00%` |

* **Katha With Audio**: **`179`** ($98 + 81 = 179$)
* **Katha With Video**: **`107`** ($98 + 9 = 107$)

---

## 4. 🔮 Next Discovery Queues from the 317 Media-Less Backlog

* 🎯 **Next Discovery Batch (Top 50)**: Ranks 01–50
* 🎯 **Secondary Discovery Batch (Next 50)**: Ranks 51–100
* 🎯 **Remaining Backlog**: **`217`** records ($317 - 50 - 50 = 217$)
* **Top 50 ∩ Secondary 50 Priority Overlap**: **`0`**

---

## 5. 🔒 FINAL RESULT

```
PHASE 2L-F GLOBAL POST-APPLY RECONCILIATION COMPLETE

Database Modified       : NO
Database Writes         : 0

Phase 2L-E Mappings     : 79 / 79

Integrity Check         : ok
Foreign-Key Violations  : 0

Total Database Records  : 10,010
FTS5 Documents          : 10,010

Playable Audio          : 240
Local MP3               : 38
YouTube Audio           : 202
Video URLs              : 109

Total Katha             : 505
Katha With Audio        : 179
Katha With Video        : 107
Katha With Both         : 98
Katha With Neither      : 317

Audio Only              : 81
Video Only              : 9

Duplicate YouTube IDs   : 0
Duplicate URLs          : 0
Cross-Field Collisions  : 0

Media-Less Backlog      : 317

Next Batch              : 50
Secondary Batch         : 50
Remaining Backlog       : 217
Priority Overlap        : 0

Final Gate              : PASS
```
