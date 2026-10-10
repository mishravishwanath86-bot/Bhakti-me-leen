# 🎵 Phase 2R-A — Audio Failure Diagnosis Audit Report

**Mode**: `STRICT READ-ONLY — AUDIO FAILURE DIAGNOSIS ONLY` (Zero Database Writes)  
**Database File**: `db/bhakti.db` (Unchanged, 0 Writes)  
**Date**: `2026-08-31 16:49:05`  
**Final Gate Verdict**: **`PASS`**  

---

## 1. 🛡️ Executive Summary & Key Findings

* **Total Failed Audio Diagnosed**: **`31 / 31`**
* **Newly Applied Media Failures (Phases 2N, 2O, 2P, 2Q)**: **`0`** (100% of Phase 2N–2Q additions are healthy)
* **Pre-2N Legacy Failures**: **`31 / 31`** (Originated from early legacy imports Batch 001–020)
* **Primary Root Cause**: `VIDEO_DELETED_OR_NOT_FOUND` (404 on YouTube oEmbed endpoint for historical placeholder URLs)
* **Database Writes**: **`0`** (Strict Read-Only)

---

## 2. 📋 Phase Lineage Breakdown of 31 Failures

| Source Origin Phase | Failure Count | Status in Phase 2R-A |
| :--- | :---: | :--- |
| **Phase 2N Additions** | `0` | ✅ 38/38 Audio Healthy |
| **Phase 2O Additions** | `0` | ✅ 27/27 Audio Healthy |
| **Phase 2P Additions** | `0` | ✅ 21/21 Audio Healthy |
| **Phase 2Q Additions** | `0` | ✅ 24/24 Audio Healthy |
| **Pre-2N Legacy Records** | `31` | ⚠️ Historical Legacy Inactive Links |
| **Total Diagnosed** | **`31`** | **`100% Accounted For`** |

---

## 3. 🔍 Detailed Diagnosis of All 31 Failed Audio Records

| # | Database Record ID | Title | YouTube ID | Origin Phase | HTTP / Reason | Recommendation |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 01 | `bhajan-krishna-yashomati-maiya-se-bole` | **यशोमति मैया से बोले नंदलाला** | `yWTN6bsDWN4` | Pre-2N | `VIDEO_PRIVATE` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 02 | `chalisa-durga-shri-durga-chalisa` | **श्री दुर्गा चालीसा (नमो नमो दुर्गे सुख करनी)** | `kYIqj20eB54` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 03 | `aarti-lakshmi-om-jai-lakshmi-mata` | **महालक्ष्मी जी की आरती - ॐ जय लक्ष्मी माता** | `_4sTBRQQe9s` | Pre-2N | `VIDEO_PRIVATE` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 04 | `bhajan-surdas-nisidin-barsat-nain-hamare` | **निसिदिन बरसत नैन हमारे** | `AmXOoh3JPWU` | Pre-2N | `VIDEO_PRIVATE` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 05 | `aarti-krishna-shrinathji-ki` | **आरती श्रीनाथ जी की (आरती श्री नवनीतप्रिया की)** | `8Uj2tn5vSQE` | Pre-2N | `VIDEO_PRIVATE` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 06 | `b6-chalisa-hanuman-shri-hanuman-chalisa-tulsidas-b6` | **श्री हनुमान चालीसा (गोस्वामी तुलसीदास कृत 40 चौपाई)** | `AETFv444yoE` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 07 | `b10-chalisa-shri-ram-avadh-chalisa-sampurna-b10` | **श्री राम चालीसा (अवधपति रघुवीर दयाला करो कृपा दशरथ के लाला 10)** | `1F9L7v3K2Nm` | Pre-2N | `HTTP_400_UNAVAILABLE` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 08 | `b10-chalisa-shri-krishna-gopal-chalisa-sampurna-b10` | **श्री कृष्ण चालीसा (जय जय श्री गोकुल के वासी मुरलीधर त्रिभुवन सुखरासी 10)** | `7X5b9L3eN2Q` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 09 | `b10-katha-ram-kewat-samvad-charanamrit-b10` | **केवट संवाद कथा: प्रभु श्री राम के चरण पखारना और उतराई में भक्ति दान (10)** | `1M8L4v7K2Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 10 | `b10-katha-krishna-govardhan-dharana-indra-garva-b10` | **गोवर्धन लीला: कनिष्ठिका उंगली पर गिरिराज उठाना और इंद्र का मानमर्दन (10)** | `8M2K9v4L7Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 11 | `b11-chalisa-ram-chandra-kripa-chalisa-b11` | **श्री रामचंद्र कृपालु भक्ति चालीसा (राम चालीसा 11)** | `6K2M8v7L4Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 12 | `b11-chalisa-krishna-gopal-madhav-chalisa-b11` | **श्री कृष्ण गोपाल माधव भक्ति चालीसा (गोपाल चालीसा 11)** | `9B2L1v4k8Ms` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 13 | `b11-chalisa-durga-bhagavati-kripa-chalisa-b11` | **श्री दुर्गा भगवती नवदुर्गा चालीसा (दुर्गा चालीसा 11)** | `JmHj24NqE7w` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 14 | `b11-chalisa-shanidev-shanti-kripa-chalisa-b11` | **श्री शनिदेव महाराज शांति एवं न्याय चालीसा (शनि चालीसा 11)** | `8M3L2v7K9Ps` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 15 | `b11-katha-ramayana-kevat-samvad-prasang-b11` | **श्री रामचरितमानस केवट प्रेम एवं नौका प्रसंग कथा (केवट संवाद 11)** | `4L7M2v9K1Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 16 | `b11-katha-shrimad-bhagavata-sudama-charitra-b11` | **श्रीमद्भागवत सुदामा चरित्र एवं अनन्य मित्रता कथा (सुदामा मिलन 11)** | `5V2M8k4L9Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 17 | `b12-chalisa-ram-raghupati-kripa-chalisa-b12` | **श्री रघुपति राघव कृपालु भक्ति चालीसा (रघुपति चालीसा 12)** | `4N7L3v2K9Ms` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 18 | `b12-chalisa-krishna-nandanandana-kripa-chalisa-b12` | **श्री नंदनंदन कृष्ण कन्हैया अमृत चालीसा (नंदनंदन चालीसा 12)** | `3K8L2v9s1Nm` | Pre-2N | `HTTP_400_UNAVAILABLE` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 19 | `b12-chalisa-durga-singhavahini-kripa-chalisa-b12` | **श्री सिंहवाहिनी दुर्गा भवानी चालीसा (सिंहवाहिनी चालीसा 12)** | `482D1P8sH9A` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 20 | `b12-chalisa-hanuman-mahavir-kripa-chalisa-b12` | **श्री महावीर हनुमान संकटमोचन चालीसा (महावीर चालीसा 12)** | `Gk3K3u4k7Yg` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 21 | `b12-katha-ramayana-shabari-prasang-bhakti-b12` | **श्री रामचरितमानस शबरी नवधा भक्ति प्रसंग (शबरी भक्ति 12)** | `3N8L4v2K9Ms` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 22 | `b12-katha-shrimad-bhagavata-govardhan-dharan-b12` | **श्रीमद्भागवत गोवर्धन धारण एवं इंद्र मानभंग कथा (गोवर्धन कथा 12)** | `2K9M4v7L1Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 23 | `b13-chalisa-ram-avadh-pati-kripa-chalisa-b13` | **श्री अवधपति राघव कृपालु चालीसा (अवधपति चालीसा 13)** | `7M2L9v4K1Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 24 | `b13-chalisa-krishna-gokul-chandra-chalisa-b13` | **श्री गोकुल चंद्र कृष्ण कन्हैया अमृत चालीसा (गोकुल चंद्र चालीसा 13)** | `2L9M4k7V8Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 25 | `b13-chalisa-durga-ashtabhuja-bhavani-chalisa-b13` | **श्री अष्टभुजा दुर्गा भवानी अमृत चालीसा (अष्टभुजा चालीसा 13)** | `M99b2G5vG1Q` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 26 | `b13-chalisa-hanuman-anjaneya-kripa-chalisa-b13` | **श्री आंजनेय संकटमोचन महावीर चालीसा (आंजनेय चालीसा 13)** | `D6F6bK2L9sY` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 27 | `b13-katha-ramayana-kewat-samvad-bhakti-b13` | **श्री रामचरितमानस केवट संवाद एवं चरणामृत प्रसंग (केवट प्रसंग 13)** | `6L2M9v4K7Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 28 | `b13-katha-shrimad-bhagavata-sudama-charitra-b13` | **श्रीमद्भागवत सुदामा चरित्र अनन्य सखा भाव (सुदामा चरित्र 13)** | `1K7M9v2L4Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 29 | `b14-katha-ramayana-bharat-milap-chitrakoot-b14` | **श्री रामचरितमानस भरत मिलाप एवं पादुका प्रसंग (चतुर्दश भरत मिलाप 14)** | `2K8M4v9L1Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 30 | `b14-katha-shrimad-bhagavata-govardhan-leela-b14` | **श्रीमद्भागवत गोवर्धन धारण एवं इंद्र मानभंग कथा (चतुर्दश गोवर्धन 14)** | `8L3M7v2K9Ns` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |
| 31 | `b14-bhajan-guru-sant-kabir-chadariya-jhini-re-jhini-b14` | **झीनी झीनी बीनी चदरिया (संत कबीर पद 14)** | `Fj-E_U2x6fE` | Pre-2N | `VIDEO_DELETED_OR_NOT_FOUND` | `SOURCE_REPLACEMENT_MAY_BE_NEEDED` |

---

## 4. 🔒 FINAL RESULT

```
PHASE 2R-A AUDIO FAILURE DIAGNOSIS COMPLETE

Database Modified       : NO
Database Writes         : 0

Target Failed Audio     : 31
Records Diagnosed       : 31

Confirmed Failures      : 31
Recovered               : 0
User-Play Required      : 0
Player-Side Issues      : 0
Network Issues          : 0
Source-Side Issues      : 31
Unknown                 : 0

Phase 2N Failures       : 0
Phase 2O Failures       : 0
Phase 2P Failures       : 0
Phase 2Q Failures       : 0
Pre-2N Failures         : 31

Newly Applied Failures  : 0

Duplicate YouTube IDs   : 0
Duplicate YouTube URLs  : 0
Cross-Field Conflicts   : 0
URL-ID Mismatches       : 0
Malformed URLs          : 0

Integrity Check         : ok
Foreign-Key Violations  : 0

Final Gate              : PASS

IMPORTANT:
No database modifications were performed.
No audio was deleted.
No audio was replaced.
No replacement media was searched.

STOP AFTER DIAGNOSIS.
```
