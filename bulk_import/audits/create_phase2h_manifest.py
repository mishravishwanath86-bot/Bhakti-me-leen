import json, sqlite3, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app")
audits_dir = BASE_DIR / "bulk_import" / "audits"
audits_dir.mkdir(parents=True, exist_ok=True)
manifest_path = audits_dir / "audio_video_katha_phase2h_apply_manifest.json"

APPROVED_33_MANIFEST = [
    # 01. Matsya
    {"record_id": "katha-dashavatara-matsya", "katha_title": "मत्स्य अवतार: प्रलय से वेदों व सप्तऋषियों की रक्षा", "deity_id": "vishnu", "media_type": "Audio", "youtube_id": "jG4WPko_laM", "youtube_url": "https://www.youtube.com/watch?v=jG4WPko_laM", "video_title": "भगवान श्री विष्णु का मत्स्य अवतार | संपूर्ण कथा", "channel": "Hindi Tv Series", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-dashavatara-matsya", "katha_title": "मत्स्य अवतार: प्रलय से वेदों व सप्तऋषियों की रक्षा", "deity_id": "vishnu", "media_type": "Video", "youtube_id": "r633N12mJxQ", "youtube_url": "https://www.youtube.com/watch?v=r633N12mJxQ", "video_title": "भगवान विष्णु का पहला मत्स्य मछली अवतार", "channel": "Bhakti Sagar AR Entertainments", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 02. Kurma
    {"record_id": "katha-dashavatara-kurma", "katha_title": "कूर्म (कच्छप) अवतार एवं समुद्र मंथन", "deity_id": "vishnu", "media_type": "Audio", "youtube_id": "dJ2mzB3ADhI", "youtube_url": "https://www.youtube.com/watch?v=dJ2mzB3ADhI", "video_title": "Samudra Manthan – The Complete Story of Lord Vishnu's Kurma Avatar", "channel": "Amrit Dash Art", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-dashavatara-kurma", "katha_title": "कूर्म (कच्छप) अवतार एवं समुद्र मंथन", "deity_id": "vishnu", "media_type": "Video", "youtube_id": "hTVdwjK1YQw", "youtube_url": "https://www.youtube.com/watch?v=hTVdwjK1YQw", "video_title": "भगवान विष्णु का दूसरा अवतार कुर्मु कछुआ", "channel": "The Sources Behind", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 03. Varaha
    {"record_id": "katha-dashavatara-varaha", "katha_title": "वराह अवतार: हिरण्याक्ष वध एवं पृथ्वी उद्धार", "deity_id": "vishnu", "media_type": "Video", "youtube_id": "4LlkJsm66sA", "youtube_url": "https://www.youtube.com/watch?v=4LlkJsm66sA", "video_title": "\"वराह अवतार\" | भगवान विष्णु ने वराह अवतार क्यों लिया?", "channel": "श्री श्री प्रभु जी", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 04. Narasimha
    {"record_id": "katha-dashavatara-narasimha", "katha_title": "नृसिंह अवतार: हिरण्यकश्यप वध एवं प्रह्लाद रक्षा", "deity_id": "vishnu", "media_type": "Audio", "youtube_id": "P1dBpgjEnz4", "youtube_url": "https://www.youtube.com/watch?v=P1dBpgjEnz4", "video_title": "Narasimha Chaturdashi | Story of Lord Narasimha & Prahlad Maharaj", "channel": "Hare Krsna TV", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-dashavatara-narasimha", "katha_title": "नृसिंह अवतार: हिरण्यकश्यप वध एवं प्रह्लाद रक्षा", "deity_id": "vishnu", "media_type": "Video", "youtube_id": "GE_okUlJ2AA", "youtube_url": "https://www.youtube.com/watch?v=GE_okUlJ2AA", "video_title": "भक्त प्रह्लाद और नृसिंह अवतार की अद्भुत कथा", "channel": "Puran Sri Hari", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 05. Vamana
    {"record_id": "katha-dashavatara-vamana", "katha_title": "वामन अवतार: राजा बलि का उद्धार एवं तीन पग भूमि", "deity_id": "vishnu", "media_type": "Video", "youtube_id": "rdq9nocejP4", "youtube_url": "https://www.youtube.com/watch?v=rdq9nocejP4", "video_title": "वामन अवतार | राजा बली की संपूर्ण कथा", "channel": "Marudhar Films", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 06. Parashurama
    {"record_id": "katha-dashavatara-parashurama", "katha_title": "भगवान परशुराम अवतार: 21 बार आततायी क्षत्रियों का दमन", "deity_id": "vishnu", "media_type": "Audio", "youtube_id": "tYI80vkSBzo", "youtube_url": "https://www.youtube.com/watch?v=tYI80vkSBzo", "video_title": "Parashurama Avatar Full Story | 6th Avatar of Lord Vishnu", "channel": "Sanatani.Studio", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 07. Rama
    {"record_id": "katha-dashavatara-rama", "katha_title": "मर्यादा पुरुषोत्तम श्री राम अवतार: रावण संहार व धर्म स्थापना", "deity_id": "ram", "media_type": "Video", "youtube_id": "5Pqtq7i1ICE", "youtube_url": "https://www.youtube.com/watch?v=5Pqtq7i1ICE", "video_title": "राम जन्म कथा स्वर रजनेश शास्त्री", "channel": "Shivam Studio Barkhiriya", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 08. Krishna
    {"record_id": "katha-dashavatara-krishna", "katha_title": "लीला पुरुषोत्तम भगवान श्री कृष्ण अवतार: गीता ज्ञान", "deity_id": "krishna", "media_type": "Audio", "youtube_id": "FeZs62yREuk", "youtube_url": "https://www.youtube.com/watch?v=FeZs62yREuk", "video_title": "देखिए महाराज श्री कैसे छोटे से कृष्णा को लाड प्यार कर रहे हैं", "channel": "Shri Devkinandan Thakur Ji Maharaj", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 09. Buddha
    {"record_id": "katha-dashavatara-buddha", "katha_title": "भगवान बुद्ध अवतार: अहिंसा, करुणा व दया का संदेश", "deity_id": "vishnu", "media_type": "Video", "youtube_id": "aRtNO04vmLM", "youtube_url": "https://www.youtube.com/watch?v=aRtNO04vmLM", "video_title": "Gautam Buddha - The 9th Avatar of Lord Vishnu?", "channel": "Dr. Vineet Aggarwal", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 10. Kalki
    {"record_id": "katha-dashavatara-kalki", "katha_title": "कल्कि अवतार: कलयुग के अंत में अधर्म का नाश", "deity_id": "vishnu", "media_type": "Audio", "youtube_id": "n6oU7-PcwRQ", "youtube_url": "https://www.youtube.com/watch?v=n6oU7-PcwRQ", "video_title": "सम्पूर्ण श्री कल्कि पुराण | Kalki Puran Audiobook", "channel": "Spiritual Spirit", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-dashavatara-kalki", "katha_title": "कल्कि अवतार: कलयुग के अंत में अधर्म का नाश", "deity_id": "vishnu", "media_type": "Video", "youtube_id": "18HbayqQ84A", "youtube_url": "https://www.youtube.com/watch?v=18HbayqQ84A", "video_title": "Complete Sri kalki puran🔥 | भगवान कल्कि अवतार कथा", "channel": "Audiobook ki Ganga", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 11. Hanuman Sanjeevani
    {"record_id": "katha-hanuman-sanjeevani-booti-prasang", "katha_title": "द्रोणागिरि पर्वत एवं संजीवनी बूटी प्रसंग", "deity_id": "hanuman", "media_type": "Audio", "youtube_id": "RAGL8Yi0fgg", "youtube_url": "https://www.youtube.com/watch?v=RAGL8Yi0fgg", "video_title": "लक्ष्मण शक्ति Vol 6 | रामायण कथा", "channel": "KanhaiyaCassette", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-hanuman-sanjeevani-booti-prasang", "katha_title": "द्रोणागिरि पर्वत एवं संजीवनी बूटी प्रसंग", "deity_id": "hanuman", "media_type": "Video", "youtube_id": "j1LPAzOI4UU", "youtube_url": "https://www.youtube.com/watch?v=j1LPAzOI4UU", "video_title": "लक्ष्मण शक्ति 🔥भाग 2 | Lakshman Shakti Ramlila", "channel": "Dehati Ram Studio", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 12. Khatu Shyam Barbareek
    {"record_id": "katha-khatushyam-barbareek-sheesh-daan", "katha_title": "महाबली बर्बरीक का शीश दान एवं श्याम रूप प्राप्ति कथा", "deity_id": "khatushyam", "media_type": "Audio", "youtube_id": "uRRoe12Wf04", "youtube_url": "https://www.youtube.com/watch?v=uRRoe12Wf04", "video_title": "Jai Ho Tumhari Barbarik Balvaani", "channel": "T-Series Bhakti Sagar", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-khatushyam-barbareek-sheesh-daan", "katha_title": "महाबली बर्बरीक का शीश दान एवं श्याम रूप प्राप्ति कथा", "deity_id": "khatushyam", "media_type": "Video", "youtube_id": "POXXHjbMB10", "youtube_url": "https://www.youtube.com/watch?v=POXXHjbMB10", "video_title": "खाटू श्याम(बर्बरीक) जी की कथा/शीश के दानी बर्बरीक", "channel": "Vijender Singh Dhanda", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 13. Krishna Govardhan
    {"record_id": "katha-krishna-govardhan-dharan-leela", "katha_title": "इंद्र दर्प दलन एवं श्री गोवर्धन धारण लीला", "deity_id": "krishna", "media_type": "Audio", "youtube_id": "ZXhNB0jriT0", "youtube_url": "https://www.youtube.com/watch?v=ZXhNB0jriT0", "video_title": "गोवर्धन पूजा कथा | गोवर्धन पूजा | गिरिराज कथा", "channel": "Sonotek Bhakti", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-krishna-govardhan-dharan-leela", "katha_title": "इंद्र दर्प दलन एवं श्री गोवर्धन धारण लीला", "deity_id": "krishna", "media_type": "Video", "youtube_id": "jW86VFuSWsA", "youtube_url": "https://www.youtube.com/watch?v=jW86VFuSWsA", "video_title": "Govardhan Special: Govardhan Puja ki Katha गिरिराज जी की कथा", "channel": "Bhakti Bhajan Sagar", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 14. Krishna Sudama
    {"record_id": "katha-krishna-sudama-charitra", "katha_title": "सच्चे मित्र का सम्मान: सुदामा चरित्र प्रसंग", "deity_id": "krishna", "media_type": "Audio", "youtube_id": "rYnXsVOfG_A", "youtube_url": "https://www.youtube.com/watch?v=rYnXsVOfG_A", "video_title": "सुदामा चरित्र सम्पूर्ण कथा | Sudama Charitra", "channel": "Bhagwat Kalpadrum", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-krishna-sudama-charitra", "katha_title": "सच्चे मित्र का सम्मान: सुदामा चरित्र प्रसंग", "deity_id": "krishna", "media_type": "Video", "youtube_id": "wt2oI054Egg", "youtube_url": "https://www.youtube.com/watch?v=wt2oI054Egg", "video_title": "कृष्ण-सुदामा मिलन की अद्भुत कथा", "channel": "Bhagwat Kalpadrum", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 15. Bhagirath Gangavataran
    {"record_id": "katha-pauranik-bhagirath-gangavataran", "katha_title": "महाराज भगीरथ की घोर तपस्या एवं गंगावतरण कथा", "deity_id": "ganga", "media_type": "Audio", "youtube_id": "t0BlmTjIcdQ", "youtube_url": "https://www.youtube.com/watch?v=t0BlmTjIcdQ", "video_title": "Bhagirath Ki Tapasya Aur Ganga Avtaran", "channel": "Bhakti Gyan Sharma", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-pauranik-bhagirath-gangavataran", "katha_title": "महाराज भगीरथ की घोर तपस्या एवं गंगावतरण कथा", "deity_id": "ganga", "media_type": "Video", "youtube_id": "Je5w8zn4BE8", "youtube_url": "https://www.youtube.com/watch?v=Je5w8zn4BE8", "video_title": "जय गंगा मैया कथा | भगीरथ की भक्ति", "channel": "Tilak", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 16. Gajendra Moksha
    {"record_id": "katha-pauranik-gajendra-moksha", "katha_title": "श्रीमद्भागवत गजेंद्र मोक्ष कथा (आर्त पुकार पर श्री हरि आगमन)", "deity_id": "vishnu", "media_type": "Audio", "youtube_id": "9Y8iRf7w76U", "youtube_url": "https://www.youtube.com/watch?v=9Y8iRf7w76U", "video_title": "गजेंद्र मोक्ष की कथा | Gajendra Moksha Katha", "channel": "Smunni TV Dharmik Stories", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 17. Markandeya
    {"record_id": "katha-pauranik-markandeya-shiva-kripa", "katha_title": "महर्षि मार्कण्डेय शिव कृपा: यमराज पर महामृत्युंजय की विजय", "deity_id": "shiva", "media_type": "Audio", "youtube_id": "Fp4NyEXQN0U", "youtube_url": "https://www.youtube.com/watch?v=Fp4NyEXQN0U", "video_title": "Amrit Gaathayein: Rishi Markandeya", "channel": "T-Series Bhakti Sagar", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-pauranik-markandeya-shiva-kripa", "katha_title": "महर्षि मार्कण्डेय शिव कृपा: यमराज पर महामृत्युंजय की विजय", "deity_id": "shiva", "media_type": "Video", "youtube_id": "98VX9VbXzhk", "youtube_url": "https://www.youtube.com/watch?v=98VX9VbXzhk", "video_title": "Mahamrityunjay Mantra Story with Lyrics", "channel": "T-Series Bhakti Sagar", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 18. Samudra Manthan 14 Ratna
    {"record_id": "katha-pauranik-samudra-manthan-14-ratna", "katha_title": "समुद्र मंथन से निकले 14 दिव्य रत्नों का आध्यात्मिक रहस्य", "deity_id": "vishnu", "media_type": "Audio", "youtube_id": "iqjT3lulmbo", "youtube_url": "https://www.youtube.com/watch?v=iqjT3lulmbo", "video_title": "समुद्र मंथन से निकले 14 रत्नों का रहस्य", "channel": "Divine Blessings", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-pauranik-samudra-manthan-14-ratna", "katha_title": "समुद्र मंथन से निकले 14 दिव्य रत्नों का आध्यात्मिक रहस्य", "deity_id": "vishnu", "media_type": "Video", "youtube_id": "vm3jN4FtzdM", "youtube_url": "https://www.youtube.com/watch?v=vm3jN4FtzdM", "video_title": "समुद्र मंथन से निकले 14 अनमोल रत्न", "channel": "Mr MaNish SanKhla", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 19. Garuda Purana
    {"record_id": "katha-purana-garuda", "katha_title": "गरुड़ पुराण सार: मृत्यु उपरांत जीव की गति व मोक्ष", "deity_id": "vishnu", "media_type": "Audio", "youtube_id": "OLj0s8Amxmw", "youtube_url": "https://www.youtube.com/watch?v=OLj0s8Amxmw", "video_title": "Garuda Purana Complete in Hindi", "channel": "Bhajan Sansar", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-purana-garuda", "katha_title": "गरुड़ पुराण सार: मृत्यु उपरांत जीव की गति व मोक्ष", "deity_id": "vishnu", "media_type": "Video", "youtube_id": "nXSQzScMf_s", "youtube_url": "https://www.youtube.com/watch?v=nXSQzScMf_s", "video_title": "गरुड़ पुराण सार Garud Puran Saar", "channel": "T-Series Bhakti Sagar", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    # 20. Shiva Purana
    {"record_id": "katha-purana-shiva", "katha_title": "शिव पुराण सार: सदाशिव स्वरूप व 12 ज्योतिर्लिंग", "deity_id": "shiva", "media_type": "Audio", "youtube_id": "M9innkB3CdQ", "youtube_url": "https://www.youtube.com/watch?v=M9innkB3CdQ", "video_title": "शिव पुराण: सभी 12 ज्योतिर्लिंगों की सम्पूर्ण कथा", "channel": "BhaktiSagar Animation", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"},
    {"record_id": "katha-purana-shiva", "katha_title": "शिव पुराण सार: सदाशिव स्वरूप व 12 ज्योतिर्लिंग", "deity_id": "shiva", "media_type": "Video", "youtube_id": "CkEOQe1igag", "youtube_url": "https://www.youtube.com/watch?v=CkEOQe1igag", "video_title": "द्वादश ज्योतिर्लिंग दर्शन कथा", "channel": "Trimurti Bhakti", "verification_status": "VERIFIED_HIGH", "safety_verdict": "SAFE_TO_APPLY"}
]

EXCLUDED_7_MANIFEST = [
    {"record_id": "katha-dashavatara-varaha", "katha_title": "वराह अवतार: हिरण्याक्ष वध एवं पृथ्वी उद्धार", "media_type": "Audio", "youtube_id": "Wbway6iejXc", "verdict": "REVIEW", "reason": "Contains Varuthini Ekadashi Vrat Katha with embedded Varaha episode."},
    {"record_id": "katha-dashavatara-vamana", "katha_title": "वामन अवतार: राजा बलि का उद्धार एवं तीन पग भूमि", "media_type": "Audio", "youtube_id": "I8gufj7FQqE", "verdict": "REVIEW", "reason": "Marked explicitly as Part-1 of a multi-part series."},
    {"record_id": "katha-dashavatara-parashurama", "katha_title": "भगवान परशुराम अवतार: 21 बार आततायी क्षत्रियों का दमन", "media_type": "Video", "youtube_id": "baQqZdiXunQ", "verdict": "REVIEW", "reason": "Spoken discourse in Telugu language."},
    {"record_id": "katha-dashavatara-rama", "katha_title": "मर्यादा पुरुषोत्तम श्री राम अवतार: रावण संहार व धर्म स्थापना", "media_type": "Audio", "youtube_id": "8XSeD3buZyw", "verdict": "REJECT", "reason": "Devotional Stuti song rather than a spoken Katha narrative."},
    {"record_id": "katha-dashavatara-krishna", "katha_title": "लीला पुरुषोत्तम भगवान श्री कृष्ण अवतार: गीता ज्ञान", "media_type": "Video", "youtube_id": "PIwZ7ugXfjI", "verdict": "REJECT", "reason": "Musical bhajan ('Achyutam Keshavam') rather than a dedicated Katha video."},
    {"record_id": "katha-dashavatara-buddha", "katha_title": "भगवान बुद्ध अवतार: अहिंसा, करुणा व दया का संदेश", "media_type": "Audio", "youtube_id": "t1wunxsiruw", "verdict": "REVIEW", "reason": "Broad Dashavatara overview compilation."},
    {"record_id": "katha-pauranik-gajendra-moksha", "katha_title": "श्रीमद्भागवत गजेंद्र मोक्ष कथा (आर्त पुकार पर श्री हरि आगमन)", "media_type": "Video", "youtube_id": "i6tD1LTsCko", "verdict": "REVIEW", "reason": "Sanskrit Stotram chant with textual verses rather than narrative Katha."}
]

manifest_data = {
    "manifest_version": "1.0",
    "phase": "Phase 2H - Transaction-Safe Apply Manifest",
    "timestamp": "2026-08-31",
    "total_approved_mappings": len(APPROVED_33_MANIFEST),
    "audio_approved_count": 16,
    "video_approved_count": 17,
    "total_excluded_count": len(EXCLUDED_7_MANIFEST),
    "approved_mappings": APPROVED_33_MANIFEST,
    "excluded_candidates": EXCLUDED_7_MANIFEST
}

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest_data, f, ensure_ascii=False, indent=2)

print(f"✓ Generated Verified Apply Manifest: {manifest_path}")
