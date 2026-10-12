import sys
import json
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

types = ['sundarkand', 'mantra', 'chalisa', 'aarti']
print("=" * 60)
print("1. VERIFYING CONTENT API FOR ALL 4 TYPES")
print("=" * 60)

for t in types:
    url = f"http://localhost:8000/api/content?type={t}&limit=3"
    try:
        with urllib.request.urlopen(url) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('items', [])
            total = data.get('total', len(items))
            print(f"[OK] Type: {t:12} | Returned: {len(items)} | Total in DB: {total}")
            if items:
                print(f"     Sample ID: {items[0]['id']}")
                print(f"     Title: {items[0]['title'][:50]}")
    except Exception as e:
        print(f"[FAIL] Type: {t} failed: {e}")

print("\n" + "=" * 60)
print("2. VERIFYING AI AUDIO GENERATION ENDPOINT FOR ALL 4 TYPES")
print("=" * 60)

test_cases = [
    {
        "content_type": "sundarkand",
        "content_id": "sundarkand-doha-1",
        "text": "शान्तं शाश्वतमप्रमेयमनघं मोक्षप्रदं शान्तिदं ब्रह्माशम्भुफणीन्द्रसेव्यमनिशं वेदान्तवेद्यं विभुम्।",
        "title": "सुन्दरकाण्ड दोहा 1 मंगलाचरण",
        "deity": "hanuman"
    },
    {
        "content_type": "mantra",
        "content_id": "mantra-gayatri-test",
        "text": "ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात्॥",
        "title": "गायत्री महामंत्र",
        "deity": "surya"
    },
    {
        "content_type": "chalisa",
        "content_id": "chalisa-hanuman-test",
        "text": "जय हनुमान ज्ञान गुन सागर। जय कपीस तिहुँ लोक उजागर॥ रामदूत अतुलित बल धामा। अंजनि-पुत्र पवनसुत नामा॥",
        "title": "श्री हनुमान चालीसा",
        "deity": "hanuman"
    },
    {
        "content_type": "aarti",
        "content_id": "aarti-om-jai-jagdish-test",
        "text": "ॐ जय जगदीश हरे, स्वामी जय जगदीश हरे। भक्त जनों के संकट, दास जनों के संकट, क्षण में दूर करे॥",
        "title": "श्री जगदीश आरती",
        "deity": "vishnu"
    }
]

for tc in test_cases:
    url = "http://localhost:8000/api/ai-audio/generate"
    payload = json.dumps(tc).encode('utf-8')
    req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as resp:
            res_data = json.loads(resp.read().decode('utf-8'))
            print(f"[OK] Audio Generated: {tc['content_type']:12}")
            print(f"     URL: {res_data.get('audio_url')}")
            print(f"     Cached: {res_data.get('cached')}")
            print(f"     Cadence: {res_data.get('cadence')}")
    except Exception as e:
        print(f"[FAIL] Audio generation failed for {tc['content_type']}: {e}")
