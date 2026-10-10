# 📖🎬 Phase 2K-F — Global Post-Apply Reconciliation & Coverage Audit Report

**Audit Mode**: `STRICT READ-ONLY` (Zero Database Writes)  
**Database File**: `db/bhakti.db`  
**Date**: `2026-08-31 11:53:57`  
**Final Status**: **`PASS`**  

---

## 1. 🔍 Root Cause Resolution of Katha Count Numbers (505 vs. 551 vs. 637)

The **authoritative distinct Katha record count in SQLite is exactly 505 records**.

### Mathematical Breakdown
Across all phases, the underlying records in `content_items` (`content_type = 'katha' OR category_id = 'katha'`) have never changed from **505**. The apparent numbers 551 and 637 arose from naive non-disjoint additions:

1. **Current Disjoint Mutually Exclusive Partition**:
   * **Audio Only**: **`71`**
   * **Video Only**: **`4`**
   * **Both Audio & Video**: **`66`**
   * **Neither (Media-Less)**: **`364`**
   * **Exact Total**: $71 + 4 + 66 + 364 =$ **`505`**

2. **Why 551 Appeared in Phase 2I**:
   * Naive sum: $90 \text{ (Audio)} + 27 \text{ (Video)} + 23 \text{ (Both)} + 411 \text{ (Neither)} = 551$.
   * The 23 dual-media records were counted 3 times (+2 excess each): $505 + (2 \times 23) = 551$.

3. **Why 637 Appeared in Phase 2K-E**:
   * Naive sum: $137 \text{ (Audio)} + 70 \text{ (Video)} + 66 \text{ (Both)} + 364 \text{ (Neither)} = 637$.
   * The 66 dual-media records were counted 3 times (+2 excess each): $505 + (2 \times 66) = 637$.

✅ **The mathematical identity $\text{AUDIO\_ONLY} + \text{VIDEO\_ONLY} + \text{BOTH} + \text{NEITHER} = 505$ holds 100% perfectly.**

---

## 2. 🛡️ Global Database Baseline & Phase 2K-E Before/After Comparison

| Metric | Before Phase 2K-E | Target Expected | Final Post-Apply State | Delta |
| :--- | :--- | :--- | :--- | :---: |
| **Total Database Records** | `10,010` | `10,010` | **`10,010`** | 0 |
| **FTS5 Search Documents** | `10,010` | `10,010` | **`10,010`** | 0 |
| **Playable Audio Total** | `151` | `198` (+47) | **`198`** | +47 |
| **Local MP3 Audio** | `38` | `38` | **`38`** | 0 |
| **YouTube HD Audio** | `113` | `160` (+47) | **`160`** | +47 |
| **YouTube Video URLs** | `29` | `72` (+43) | **`72`** | +43 |
| **Total Katha Records** | `505` | `505` | **`505`** | 0 |
| **Katha With Audio** | `90` | `137` (+47) | **`137`** | +47 |
| **Katha With Video** | `27` | `70` (+43) | **`70`** | +43 |
| **Katha With Both Media** | `23` | `66` (+43) | **`66`** | +43 |
| **Katha With Neither (Gaps)** | `411` | `364` (-47) | **`364`** | -47 |
| **PRAGMA integrity_check** | `ok` | `ok` | **`ok`** | ✅ ok |
| **Foreign-Key Violations** | `0` | `0` | **`0`** | ✅ 0 |

---

## 3. 📋 Phase 2K-E Applied Mappings & Duplicate Verification

* **Phase 2K-E Mappings Verified in DB**: **`90 / 90 PASS`** (47 Audio + 43 Video)
* **Duplicate YouTube Audio IDs**: **`0`** (160 unique IDs across 160 records)
* **Duplicate YouTube Video IDs**: **`0`** (72 unique IDs across 72 records)
* **Cross-Field Collisions**: **`0`** (Audio and Video IDs are 100% disjoint)
* **Excluded Candidates Preserved (Review/Reject)**: **`0 Applied`**

---

## 4. 📊 Katha Category Media Coverage Summary

* **Total Authoritative Katha Records**: **`505`**
* **Audio Coverage**: **`137 / 505`** (`27.13%`)
* **Video Coverage**: **`70 / 505`** (`13.86%`)
* **Dual Media Coverage (Audio + Video)**: **`66 / 505`** (`13.07%`)
* **Any Media Coverage (Audio or Video)**: **`141 / 505`** (`27.92%`)
* **Remaining Media-Less Backlog**: **`364 / 505`** (`72.08%`)

---

## 5. 🔮 Prioritized Next Discovery Queue (from 364 Backlog)

The remaining **364 media-less Katha records** are prioritized into:
* **Tier A (High Priority)**: **`10`** records
* **Tier B (Medium Priority)**: **`354`** records
* **Tier C (Low Priority)**: **`0`** records

### Discovery Queues for Next Phase:
* 🎯 **Next Batch (Top 50)**: Ranks 01–50
* 🎯 **Secondary Batch (Next 50)**: Ranks 51–100
* 🎯 **Remaining Backlog**: 264 records
* **Top 50 ∩ Secondary 50 Overlap**: **`0`**

---

## 6. 🔒 FINAL RESULT

```
PHASE 2K-F GLOBAL POST-APPLY RECONCILIATION COMPLETE

Database Modified       : NO
Database Writes         : 0

Phase 2K-E Mappings     : 90 / 90

Integrity Check         : ok
Foreign-Key Violations  : 0

Total Database Records  : 10,010
FTS5 Documents          : 10,010

Playable Audio          : 198
Local MP3               : 38
YouTube Audio           : 160
Video URLs              : 72

Total Katha             : 505
Katha With Audio        : 137
Katha With Video        : 70
Katha With Both         : 66
Katha With Neither      : 364

Audio Only              : 71
Video Only              : 4

Duplicate YouTube IDs   : 0
Duplicate URLs          : 0
Cross-Field Collisions  : 0

Media-Less Backlog      : 364

Next Batch              : 50
Secondary Batch         : 50
Priority Overlap        : 0

Final Gate              : PASS
```
