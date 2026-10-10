import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

file = 'final_granular_aarti_collections.json'
with open(file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find and update drik_gods_2 in surya section
surya = data['surya']
for item in surya['items']:
    if item['id'] == 'drik_gods_2':
        print("OLD content:")
        print(repr(item['content'][:100]))
        item['content'] = (
            "॥ सूर्यदेव आरती ॥\n"
            "(जय कश्यप-नन्दन, ॐ जय अदिति नन्दन)\n\n"
            "जय कश्यप-नन्दन, ॐ जय अदिति नन्दन।\n"
            "त्रिभुवन - तिमिर - निकन्दन, भक्त-हृदय-चन्दन॥\n"
            "जय कश्यप-नन्दन, ॐ जय अदिति नन्दन।\n\n"
            "सप्त-अश्वरथ राजित, एक चक्रधारी।\n"
            "दुःखहारी, सुखकारी, मानस-मल-हारी॥\n"
            "जय कश्यप-नन्दन, ॐ जय अदिति नन्दन।\n\n"
            "सुर - मुनि - भूसुर - वन्दित, विमल विभवशाली।\n"
            "अघ-दल-दलन दिवाकर, दिव्य किरण माली॥\n"
            "जय कश्यप-नन्दन, ॐ जय अदिति नन्दन।\n\n"
            "सकल - सुकर्म - प्रसविता, सविता शुभकारी।\n"
            "विश्व-विलोचन मोचन, भव-बन्धन भारी॥\n"
            "जय कश्यप-नन्दन, ॐ जय अदिति नन्दन।\n\n"
            "कमल-समूह विकासक, नाशक त्रय तापा।\n"
            "सेवत साहज हरत अति मनसिज-संतापा॥\n"
            "जय कश्यप-नन्दन, ॐ जय अदिति नन्दन।\n\n"
            "नेत्र-व्याधि हर सुरवर, भू-पीड़ा-हारी।\n"
            "वृष्टि विमोचन संतत, परहित व्रतधारी॥\n"
            "जय कश्यप-नन्दन, ॐ जय अदिति नन्दन।\n\n"
            "सूर्यदेव करुणाकर, अब करुणा कीजै।\n"
            "हर अज्ञान-मोह सब, तत्त्वज्ञान दीजै॥\n"
            "जय कश्यप-नन्दन, ॐ जय अदिति नन्दन।"
        )
        print("NEW content updated.")
        break

with open(file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("File saved successfully.")
