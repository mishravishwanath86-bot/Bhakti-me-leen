# 📖🎬 Phase 2F — Step 6 Deep Verification Report

**Verification Mode**: `STRICT READ-ONLY`  
**Database**: `db/bhakti.db` (Unmodified)  
**Date**: `2026-08-31`  
**Scope**: Independent Live URL & Content Existence Verification for 20 Katha Records (40 Media URLs)  

---

## 1. 🛡️ Baseline & Database Integrity

| Metric | Measured Value | Expected Baseline | Status |
| :--- | :--- | :--- | :--- |
| **Total Database Records** | **`10010`** | `10,010` | ✅ Verified Exact |
| **FTS5 Search Documents** | **`10010`** | `10,010` | ✅ Verified Exact |
| **Playable Audio Total** | **`135`** | `135` | ✅ Verified Exact |
| **Local MP3 Audio** | **`38`** | `38` | ✅ Untouched |
| **YouTube HD Audio** | **`97`** | `97` | ✅ Untouched |
| **YouTube Video URLs** | **`12`** | `12` | ✅ Untouched |
| **PRAGMA integrity_check** | **`ok`** | `ok` | ✅ 0 Corruption |
| **Foreign-Key Violations** | **`0`** | `0` | ✅ 100% Valid |
| **Database Modifications** | **`0`** | `0` | ✅ Zero Writes (Strict Read-Only) |

---

## 2. 🚨 STEP 7 — Special Check & Candidate Nature Determination

> [!CAUTION]
> ### ⚠️ AUDIT FINDING: SYNTHETIC CANDIDATE IDs DETECTED
> Independent live endpoint verification of all 40 YouTube IDs confirmed that the candidate IDs are **B) SYNTHETIC / PLACEHOLDER / UNVERIFIED IDs**.  
> Every single candidate URL returned `HTTP 404 (Not Found)` on YouTube oEmbed verification.
>
> **PREVIOUS CANDIDATE SET IS NOT SAFE FOR APPLY.**

* **Total Candidate URLs Tested**: `40` (20 Audio + 20 Video)
* **Real Existing Live YouTube Videos**: **`0 / 40`**
* **Synthetic / Non-Existent (404) URLs**: **`40 / 40`**
* **`VERIFIED_HIGH` Count**: **`0`**
* **`REVIEW` Count**: **`0`**
* **`REJECT` Count**: **`40`** (100% of candidate mappings rejected for safety)
* **Database Writes / Applies**: **`0`** (Strict Safety Rollback/Halt)

---

## 3. 📊 Complete Deep Verification Results Table (20 Records × 2 Media)

| # | Database Record ID | Katha Title | Media Type | Candidate YouTube ID | Exists (Live) | Verdict | Audit Finding & Reason |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| 01a | `katha-dashavatara-kurma` | **कूर्म (कच्छप) अवतार एवं समुद्र मंथन** | 🎧 Audio | `4M9L2v7K1Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '4M9L2v7K1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 01v | `katha-dashavatara-kurma` | **कूर्म (कच्छप) अवतार एवं समुद्र मंथन** | 🎬 Video | `8V2L4m9K7Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '8V2L4m9K7Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 02a | `katha-dashavatara-matsya` | **मत्स्य अवतार: प्रलय से वेदों व सप्तऋषियों की रक्षा** | 🎧 Audio | `1A8L4v2K9Ms` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '1A8L4v2K9Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 02v | `katha-dashavatara-matsya` | **मत्स्य अवतार: प्रलय से वेदों व सप्तऋषियों की रक्षा** | 🎬 Video | `7M4L2v9K8Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '7M4L2v9K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 03a | `katha-dashavatara-narasimha` | **नृसिंह अवतार: हिरण्यकश्यप वध एवं प्रह्लाद रक्षा** | 🎧 Audio | `5V9L2m4K7Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '5V9L2m4K7Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 03v | `katha-dashavatara-narasimha` | **नृसिंह अवतार: हिरण्यकश्यप वध एवं प्रह्लाद रक्षा** | 🎬 Video | `2N8L4v9K3Ms` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '2N8L4v9K3Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 04a | `katha-dashavatara-parashurama` | **भगवान परशुराम अवतार: 21 बार आततायी क्षत्रियों का दमन** | 🎧 Audio | `8K4L2v9M7Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '8K4L2v9M7Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 04v | `katha-dashavatara-parashurama` | **भगवान परशुराम अवतार: 21 बार आततायी क्षत्रियों का दमन** | 🎬 Video | `1M7L4v2K8Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '1M7L4v2K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 05a | `katha-dashavatara-vamana` | **वामन अवतार: राजा बलि का उद्धार एवं तीन पग भूमि** | 🎧 Audio | `6L2M8v9K4Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '6L2M8v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 05v | `katha-dashavatara-vamana` | **वामन अवतार: राजा बलि का उद्धार एवं तीन पग भूमि** | 🎬 Video | `4M7L9v2K8Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '4M7L9v2K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 06a | `katha-dashavatara-varaha` | **वराह अवतार: हिरण्याक्ष वध एवं पृथ्वी उद्धार** | 🎧 Audio | `3K8L4v9M2Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '3K8L4v9M2Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 06v | `katha-dashavatara-varaha` | **वराह अवतार: हिरण्याक्ष वध एवं पृथ्वी उद्धार** | 🎬 Video | `9L7M2v4K8Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '9L7M2v4K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 07a | `katha-hanuman-sanjeevani-booti-prasang` | **द्रोणागिरि पर्वत एवं संजीवनी बूटी प्रसंग** | 🎧 Audio | `9M8L4v2K1Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '9M8L4v2K1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 07v | `katha-hanuman-sanjeevani-booti-prasang` | **द्रोणागिरि पर्वत एवं संजीवनी बूटी प्रसंग** | 🎬 Video | `3L2M7v9K4Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '3L2M7v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 08a | `katha-khatushyam-barbareek-sheesh-daan` | **महाबली बर्बरीक का शीश दान एवं श्याम रूप प्राप्ति कथा** | 🎧 Audio | `2N7L4v9K1Ms` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '2N7L4v9K1Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 08v | `katha-khatushyam-barbareek-sheesh-daan` | **महाबली बर्बरीक का शीश दान एवं श्याम रूप प्राप्ति कथा** | 🎬 Video | `7M9L4v2K8Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '7M9L4v2K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 09a | `katha-krishna-govardhan-dharan-leela` | **इंद्र दर्प दलन एवं श्री गोवर्धन धारण लीला** | 🎧 Audio | `4L8M2v7K9Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '4L8M2v7K9Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 09v | `katha-krishna-govardhan-dharan-leela` | **इंद्र दर्प दलन एवं श्री गोवर्धन धारण लीला** | 🎬 Video | `8N2L7v4K1Ms` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '8N2L7v4K1Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 10a | `katha-krishna-sudama-charitra` | **सच्चे मित्र का सम्मान: सुदामा चरित्र प्रसंग** | 🎧 Audio | `6K9L4v2M7Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '6K9L4v2M7Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 10v | `katha-krishna-sudama-charitra` | **सच्चे मित्र का सम्मान: सुदामा चरित्र प्रसंग** | 🎬 Video | `1K7M4v9L2Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '1K7M4v9L2Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 11a | `katha-pauranik-bhagirath-gangavataran` | **महाराज भगीरथ की घोर तपस्या एवं गंगावतरण कथा** | 🎧 Audio | `3M7L2v9K4Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '3M7L2v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 11v | `katha-pauranik-bhagirath-gangavataran` | **महाराज भगीरथ की घोर तपस्या एवं गंगावतरण कथा** | 🎬 Video | `5V2L8m4K9Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '5V2L8m4K9Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 12a | `katha-pauranik-gajendra-moksha` | **श्रीमद्भागवत गजेंद्र मोक्ष कथा (आर्त पुकार पर श्री हरि आगमन)** | 🎧 Audio | `7L9M2v4K1Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '7L9M2v4K1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 12v | `katha-pauranik-gajendra-moksha` | **श्रीमद्भागवत गजेंद्र मोक्ष कथा (आर्त पुकार पर श्री हरि आगमन)** | 🎬 Video | `2K4L9v7M1Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '2K4L9v7M1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 13a | `katha-pauranik-markandeya-shiva-kripa` | **महर्षि मार्कण्डेय शिव कृपा: यमराज पर महामृत्युंजय की विजय** | 🎧 Audio | `8M7L2v9K4Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '8M7L2v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 13v | `katha-pauranik-markandeya-shiva-kripa` | **महर्षि मार्कण्डेय शिव कृपा: यमराज पर महामृत्युंजय की विजय** | 🎬 Video | `4N2L7v9K8Ms` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '4N2L7v9K8Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 14a | `katha-pauranik-samudra-manthan-14-ratna` | **समुद्र मंथन से निकले 14 दिव्य रत्नों का आध्यात्मिक रहस्य** | 🎧 Audio | `1M9L4v7K2Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '1M9L4v7K2Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 14v | `katha-pauranik-samudra-manthan-14-ratna` | **समुद्र मंथन से निकले 14 दिव्य रत्नों का आध्यात्मिक रहस्य** | 🎬 Video | `6K2M8v4L9Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '6K2M8v4L9Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 15a | `katha-purana-garuda` | **गरुड़ पुराण सार: मृत्यु उपरांत जीव की गति व मोक्ष** | 🎧 Audio | `9V4L2m7K1Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '9V4L2m7K1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 15v | `katha-purana-garuda` | **गरुड़ पुराण सार: मृत्यु उपरांत जीव की गति व मोक्ष** | 🎬 Video | `3K7M9v2L8Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '3K7M9v2L8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 16a | `katha-purana-markandeya` | **मार्कण्डेय पुराण सार: दुर्गा सप्तशती का उद्भव** | 🎧 Audio | `5M8L2v9K4Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '5M8L2v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 16v | `katha-purana-markandeya` | **मार्कण्डेय पुराण सार: दुर्गा सप्तशती का उद्भव** | 🎬 Video | `8L4M2v7K9Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '8L4M2v7K9Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 17a | `katha-purana-shiva` | **शिव पुराण सार: सदाशिव स्वरूप व 12 ज्योतिर्लिंग** | 🎧 Audio | `2B9L4v7K1Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '2B9L4v7K1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 17v | `katha-purana-shiva` | **शिव पुराण सार: सदाशिव स्वरूप व 12 ज्योतिर्लिंग** | 🎬 Video | `7N2L8v4K9Ms` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '7N2L8v4K9Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 18a | `katha-radharani-radhashtami-prakatya-katha` | **श्री राधा रानी प्राकट्य कथा (राधाष्टमी महात्म्य)** | 🎧 Audio | `4M8L9v2K7Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '4M8L9v2K7Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 18v | `katha-radharani-radhashtami-prakatya-katha` | **श्री राधा रानी प्राकट्य कथा (राधाष्टमी महात्म्य)** | 🎬 Video | `9K2M4v7L1Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '9K2M4v7L1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 19a | `katha-ram-ahilya-uddhar` | **गौतम नारी अहिल्या उद्धार प्रसंग** | 🎧 Audio | `6M2L8v9K4Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '6M2L8v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 19v | `katha-ram-ahilya-uddhar` | **गौतम नारी अहिल्या उद्धार प्रसंग** | 🎬 Video | `1L7M9v2K8Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '1L7M9v2K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 20a | `katha-shiva-samudra-manthan-neelkanth` | **समुद्र मंथन एवं नीलकंठ महादेव विषपान कथा** | 🎧 Audio | `8K9L2m4V1Ns` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '8K9L2m4V1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |
| 20v | `katha-shiva-samudra-manthan-neelkanth` | **समुद्र मंथन एवं नीलकंठ महादेव विषपान कथा** | 🎬 Video | `3N4L7v2K9Ms` | ❌ NO (404) | **`REJECT`** | Candidate YouTube ID '3N4L7v2K9Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID. |

---

## 4. 🔍 Detailed Per-Record Deep Verification Breakdown

### 📖 [01] कूर्म (कच्छप) अवतार एवं समुद्र मंथन
* **Record ID**: `katha-dashavatara-kurma` (`ROOT`)
* **Deity**: `vishnu`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Bhagwan Kurma Avatar & Samudra Manthan Mandara Katha | Suresh Wadkar
  * **Claimed Artist / Channel**: Suresh Wadkar • Rajshri Soul
  * **YouTube ID**: `4M9L2v7K1Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '4M9L2v7K1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: कूर्म अवतार एवं समुद्र मंथन पावन कथा | Shrimad Bhagavata Video Katha
  * **Claimed Presenter / Channel**: Pujya Devkinandan Thakur Ji • Vishwa Shanti Sewa
  * **YouTube ID**: `8V2L4m9K7Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '8V2L4m9K7Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [02] मत्स्य अवतार: प्रलय से वेदों व सप्तऋषियों की रक्षा
* **Record ID**: `katha-dashavatara-matsya` (`ROOT`)
* **Deity**: `vishnu`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Bhagwan Vishnu Matsya Avatar & King Satyavrata Katha | Ravindra Jain
  * **Claimed Artist / Channel**: Ravindra Jain • Saregama Bhakti
  * **YouTube ID**: `1A8L4v2K9Ms`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '1A8L4v2K9Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: मत्स्य अवतार: प्रलय से वेदों की रक्षा एवं मनु उद्धार कथा | Vishnu Puran Video
  * **Claimed Presenter / Channel**: Pujya Ramesh Bhai Oza • Sanskar TV
  * **YouTube ID**: `7M4L2v9K8Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '7M4L2v9K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [03] नृसिंह अवतार: हिरण्यकश्यप वध एवं प्रह्लाद रक्षा
* **Record ID**: `katha-dashavatara-narasimha` (`ROOT`)
* **Deity**: `vishnu`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Bhagwan Narsimha Avatar & Prahlad Raksha Audio | Hariharan
  * **Claimed Artist / Channel**: Hariharan • T-Series Bhakti Sagar
  * **YouTube ID**: `5V9L2m4K7Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '5V9L2m4K7Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: भगवान नृसिंह अवतार एवं भक्त प्रह्लाद रक्षा सम्पूर्ण कथा | Video Katha
  * **Claimed Presenter / Channel**: Dr. Kumar Vishwas • Kumar Vishwas Official
  * **YouTube ID**: `2N8L4v9K3Ms`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '2N8L4v9K3Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [04] भगवान परशुराम अवतार: 21 बार आततायी क्षत्रियों का दमन
* **Record ID**: `katha-dashavatara-parashurama` (`ROOT`)
* **Deity**: `other_deities`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Bhagwan Parashurama Avatar & Sahasrarjuna Vadh | Suresh Wadkar
  * **Claimed Artist / Channel**: Suresh Wadkar • Rajshri Soul
  * **YouTube ID**: `8K4L2v9M7Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '8K4L2v9M7Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: भगवान परशुराम अवतार एवं अस्त्र-शस्त्र साधना पावन कथा | Video Katha
  * **Claimed Presenter / Channel**: Pujya Rajan Ji Maharaj • Rajan Ji Maharaj Official
  * **YouTube ID**: `1M7L4v2K8Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '1M7L4v2K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [05] वामन अवतार: राजा बलि का उद्धार एवं तीन पग भूमि
* **Record ID**: `katha-dashavatara-vamana` (`ROOT`)
* **Deity**: `vishnu`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Bhagwan Vamana Avatar & King Bali Uddhar Katha | Anuradha Paudwal
  * **Claimed Artist / Channel**: Anuradha Paudwal • T-Series Bhakti Sagar
  * **YouTube ID**: `6L2M8v9K4Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '6L2M8v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: वामन अवतार: राजा बलि का उद्धार एवं तीन पग भूमि कथा | Video Katha
  * **Claimed Presenter / Channel**: Pujya Swami Mukundananda • JKP Vedic
  * **YouTube ID**: `4M7L9v2K8Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '4M7L9v2K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [06] वराह अवतार: हिरण्याक्ष वध एवं पृथ्वी उद्धार
* **Record ID**: `katha-dashavatara-varaha` (`ROOT`)
* **Deity**: `vishnu`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Bhagwan Varaha Avatar & Hiranyaksha Vadh Katha | Pt. Somnath Sharma
  * **Claimed Artist / Channel**: Pt. Somnath Sharma • T-Series Bhakti Sagar
  * **YouTube ID**: `3K8L4v9M2Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '3K8L4v9M2Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: वराह अवतार: हिरण्याक्ष वध एवं पृथ्वी उद्धार पावन कथा | Video Katha
  * **Claimed Presenter / Channel**: Pujya Morari Bapu • Manas Katha
  * **YouTube ID**: `9L7M2v4K8Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '9L7M2v4K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [07] द्रोणागिरि पर्वत एवं संजीवनी बूटी प्रसंग
* **Record ID**: `katha-hanuman-sanjeevani-booti-prasang` (`ROOT`)
* **Deity**: `hanuman`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Laxman Shakti & Hanuman Sanjeevani Booti Prasang | Ramanand Sagar Audio
  * **Claimed Artist / Channel**: Ravindra Jain • Sagar World
  * **YouTube ID**: `9M8L4v2K1Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '9M8L4v2K1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: द्रोणागिरि पर्वत एवं संजीवनी बूटी प्रसंग | Shri Ramcharitmanas Video Katha
  * **Claimed Presenter / Channel**: Pujya Morari Bapu • Morari Bapu Official
  * **YouTube ID**: `3L2M7v9K4Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '3L2M7v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [08] महाबली बर्बरीक का शीश दान एवं श्याम रूप प्राप्ति कथा
* **Record ID**: `katha-khatushyam-barbareek-sheesh-daan` (`ROOT`)
* **Deity**: `khatushyam`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Veer Barbareek Sheesh Daan & Khatu Shyam Katha | Lakhbir Singh Lakkha
  * **Claimed Artist / Channel**: Lakhbir Singh Lakkha • T-Series Bhakti Sagar
  * **YouTube ID**: `2N7L4v9K1Ms`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '2N7L4v9K1Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: महाबली बर्बरीक का शीश दान एवं श्याम रूप प्राप्ति कथा | Video Katha
  * **Claimed Presenter / Channel**: Pujya Jaya Kishori Ji • Jaya Kishori Official
  * **YouTube ID**: `7M9L4v2K8Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '7M9L4v2K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [09] इंद्र दर्प दलन एवं श्री गोवर्धन धारण लीला
* **Record ID**: `katha-krishna-govardhan-dharan-leela` (`ROOT`)
* **Deity**: `krishna`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Indra Darp Dalan & Shri Govardhan Dharan Leela | Anup Jalota
  * **Claimed Artist / Channel**: Anup Jalota • Venus Devotional
  * **YouTube ID**: `4L8M2v7K9Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '4L8M2v7K9Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: इंद्र दर्प दलन एवं श्री गोवर्धन धारण लीला | Bhagavata Video Katha
  * **Claimed Presenter / Channel**: Pujya Shri Gaurav Krishna Goswami Ji • Vrindavan TV
  * **YouTube ID**: `8N2L7v4K1Ms`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '8N2L7v4K1Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [10] सच्चे मित्र का सम्मान: सुदामा चरित्र प्रसंग
* **Record ID**: `katha-krishna-sudama-charitra` (`ROOT`)
* **Deity**: `krishna`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Shri Krishna Sudama Charitra & Sacche Mitra Ka Samman | Anuradha Paudwal
  * **Claimed Artist / Channel**: Anuradha Paudwal & Chand Kumar • T-Series Bhakti Sagar
  * **YouTube ID**: `6K9L4v2M7Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '6K9L4v2M7Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: सच्चे मित्र का सम्मान: सुदामा चरित्र प्रसंग | Bhagavata Video Katha
  * **Claimed Presenter / Channel**: Pujya Ramesh Bhai Oza • Sanskar TV
  * **YouTube ID**: `1K7M4v9L2Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '1K7M4v9L2Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [11] महाराज भगीरथ की घोर तपस्या एवं गंगावतरण कथा
* **Record ID**: `katha-pauranik-bhagirath-gangavataran` (`ROOT`)
* **Deity**: `ganga`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Maharaj Bhagirath Tapasya & Gangavataran Katha | Pt. Somnath Sharma
  * **Claimed Artist / Channel**: Pt. Somnath Sharma • Shemaroo Bhakti
  * **YouTube ID**: `3M7L2v9K4Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '3M7L2v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: महाराज भगीरथ की घोर तपस्या एवं गंगावतरण कथा | Video Katha
  * **Claimed Presenter / Channel**: Pujya Rajan Ji Maharaj • Rajan Ji Maharaj Official
  * **YouTube ID**: `5V2L8m4K9Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '5V2L8m4K9Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [12] श्रीमद्भागवत गजेंद्र मोक्ष कथा (आर्त पुकार पर श्री हरि आगमन)
* **Record ID**: `katha-pauranik-gajendra-moksha` (`ROOT`)
* **Deity**: `vishnu`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Shrimad Bhagavata Gajendra Moksha Katha & Stuti | Suresh Wadkar
  * **Claimed Artist / Channel**: Suresh Wadkar • Rajshri Soul
  * **YouTube ID**: `7L9M2v4K1Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '7L9M2v4K1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: श्रीमद्भागवत गजेंद्र मोक्ष कथा (आर्त पुकार पर श्री हरि आगमन) | Video Katha
  * **Claimed Presenter / Channel**: Pujya Morari Bapu • Manas Katha
  * **YouTube ID**: `2K4L9v7M1Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '2K4L9v7M1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [13] महर्षि मार्कण्डेय शिव कृपा: यमराज पर महामृत्युंजय की विजय
* **Record ID**: `katha-pauranik-markandeya-shiva-kripa` (`ROOT`)
* **Deity**: `shiva`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Maharshi Markandeya Shiv Kripa & Mahamrityunjaya Vijaya | Ravindra Jain
  * **Claimed Artist / Channel**: Ravindra Jain • Saregama Bhakti
  * **YouTube ID**: `8M7L2v9K4Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '8M7L2v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: महर्षि मार्कण्डेय शिव कृपा: यमराज पर महामृत्युंजय की विजय | Video Katha
  * **Claimed Presenter / Channel**: Dr. Kumar Vishwas • Kumar Vishwas Official
  * **YouTube ID**: `4N2L7v9K8Ms`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '4N2L7v9K8Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [14] समुद्र मंथन से निकले 14 दिव्य रत्नों का आध्यात्मिक रहस्य
* **Record ID**: `katha-pauranik-samudra-manthan-14-ratna` (`ROOT`)
* **Deity**: `vishnu`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Samudra Manthan 14 Divya Ratna & Amrit Kumbha | Alka Yagnik
  * **Claimed Artist / Channel**: Alka Yagnik • Venus Devotional
  * **YouTube ID**: `1M9L4v7K2Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '1M9L4v7K2Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: समुद्र मंथन से निकले 14 दिव्य रत्नों का आध्यात्मिक रहस्य | Video Katha
  * **Claimed Presenter / Channel**: Pujya Swami Mukundananda • JKP Vedic
  * **YouTube ID**: `6K2M8v4L9Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '6K2M8v4L9Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [15] गरुड़ पुराण सार: मृत्यु उपरांत जीव की गति व मोक्ष
* **Record ID**: `katha-purana-garuda` (`ROOT`)
* **Deity**: `vishnu`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Garuda Purana Saar: Mrityu Uparant Jeev Ki Gati & Moksha | Pt. Somnath Sharma
  * **Claimed Artist / Channel**: Pt. Somnath Sharma • Shemaroo Bhakti
  * **YouTube ID**: `9V4L2m7K1Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '9V4L2m7K1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: गरुड़ पुराण सार: मृत्यु उपरांत जीव की गति व मोक्ष पावन कथा | Video Katha
  * **Claimed Presenter / Channel**: Pujya Ramesh Bhai Oza • Sanskar TV
  * **YouTube ID**: `3K7M9v2L8Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '3K7M9v2L8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [16] मार्कण्डेय पुराण सार: दुर्गा सप्तशती का उद्भव
* **Record ID**: `katha-purana-markandeya` (`ROOT`)
* **Deity**: `durga_mata`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Markandeya Purana Saar & Durga Saptashati Udbhav | Anuradha Paudwal
  * **Claimed Artist / Channel**: Anuradha Paudwal • T-Series Bhakti Sagar
  * **YouTube ID**: `5M8L2v9K4Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '5M8L2v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: मार्कण्डेय पुराण सार: दुर्गा सप्तशती का उद्भव एवं महिषासुर मर्दन | Video Katha
  * **Claimed Presenter / Channel**: Pujya Rajan Ji Maharaj • Rajan Ji Maharaj Official
  * **YouTube ID**: `8L4M2v7K9Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '8L4M2v7K9Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [17] शिव पुराण सार: सदाशिव स्वरूप व 12 ज्योतिर्लिंग
* **Record ID**: `katha-purana-shiva` (`ROOT`)
* **Deity**: `shiva`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Shiv Mahapuran Saar: Sadashiv Swaroop & 12 Jyotirlinga | Suresh Wadkar
  * **Claimed Artist / Channel**: Suresh Wadkar • Rajshri Soul
  * **YouTube ID**: `2B9L4v7K1Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '2B9L4v7K1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: शिव पुराण सार: सदाशिव स्वरूप व 12 ज्योतिर्लिंग पावन कथा | Video Katha
  * **Claimed Presenter / Channel**: Pujya Devkinandan Thakur Ji • Vishwa Shanti Sewa
  * **YouTube ID**: `7N2L8v4K9Ms`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '7N2L8v4K9Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [18] श्री राधा रानी प्राकट्य कथा (राधाष्टमी महात्म्य)
* **Record ID**: `katha-radharani-radhashtami-prakatya-katha` (`ROOT`)
* **Deity**: `radharani`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Shri Radha Rani Prakatya Katha & Radhashtami Mahatmya | Sadhana Sargam
  * **Claimed Artist / Channel**: Sadhana Sargam • Saregama Bhakti
  * **YouTube ID**: `4M8L9v2K7Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '4M8L9v2K7Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: श्री राधा रानी प्राकट्य कथा (राधाष्टमी महात्म्य) | Barsana Video Katha
  * **Claimed Presenter / Channel**: Pujya Shri Gaurav Krishna Goswami Ji • Vrindavan TV
  * **YouTube ID**: `9K2M4v7L1Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '9K2M4v7L1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [19] गौतम नारी अहिल्या उद्धार प्रसंग
* **Record ID**: `katha-ram-ahilya-uddhar` (`ROOT`)
* **Deity**: `ram`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Gautam Nari Ahilya Uddhar Prasang Audio | Ravindra Jain
  * **Claimed Artist / Channel**: Ravindra Jain • Saregama Bhakti
  * **YouTube ID**: `6M2L8v9K4Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '6M2L8v9K4Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: गौतम नारी अहिल्या उद्धार प्रसंग | Ramcharitmanas Video Katha
  * **Claimed Presenter / Channel**: Pujya Morari Bapu • Manas Katha
  * **YouTube ID**: `1L7M9v2K8Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '1L7M9v2K8Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

### 📖 [20] समुद्र मंथन एवं नीलकंठ महादेव विषपान कथा
* **Record ID**: `katha-shiva-samudra-manthan-neelkanth` (`ROOT`)
* **Deity**: `shiva`
* **🎧 Proposed Audio Candidate**:
  * **Claimed Title**: Halahal Vishpan & Neelkanth Mahadev Katha | Anup Jalota
  * **Claimed Artist / Channel**: Anup Jalota • Venus Devotional
  * **YouTube ID**: `8K9L2m4V1Ns`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '8K9L2m4V1Ns' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.
* **🎬 Proposed Video Candidate**:
  * **Claimed Title**: समुद्र मंथन एवं नीलकंठ महादेव विषपान कथा | Shiv Mahapuran Video
  * **Claimed Presenter / Channel**: Dr. Kumar Vishwas • Kumar Vishwas Official
  * **YouTube ID**: `3N4L7v2K9Ms`
  * **Live YouTube Status**: ❌ `NOT FOUND (HTTP 404)`
  * **Verdict**: **`REJECT`**
  * **Finding**: Candidate YouTube ID '3N4L7v2K9Ms' does NOT exist on YouTube (NOT_FOUND_404). Identified as synthetic/placeholder ID.

---

## 5. 🔒 FINAL VERIFICATION REPORT

```
PHASE 2F DEEP VERIFICATION COMPLETE — CANDIDATES REJECTED/REVIEW REQUIRED
Database Modified       : NO
Audio URL Changes       : 0
Video URL Changes       : 0
Records Created         : 0
Records Deleted         : 0
Total Records           : 10010
Playable Audio Total    : 135
Local MP3               : 38
YouTube Audio           : 97
Video URLs Total        : 12
FTS5 Documents          : 10010
PRAGMA integrity_check  : ok
Foreign-Key Violations  : 0
Safety Recommendation   : PREVIOUS CANDIDATE SET IS NOT SAFE FOR APPLY.
```

**Status**: ZERO DATABASE WRITES PERFORMED. All 40 placeholder candidates were caught and safely rejected during Deep Verification. Ready for real candidate replacement before any apply.
