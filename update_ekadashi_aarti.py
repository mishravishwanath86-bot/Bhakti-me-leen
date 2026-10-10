import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read the JSON
with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# The complete Ekadashi Aarti - "ॐ जय एकादशी" 
# Full canonical text of this famous aarti
EKADASHI_AARTI = """॥ एकादशी माता आरती ॥
॥ ॐ जय एकादशी, जय एकादशी ॥

ॐ जय एकादशी, जय एकादशी।
ब्रह्मा, विष्णु, सदाशिव, तीनों ने ध्याई।
विष्णु-प्रिया तुम जगत-तारिणी, जय जय जगदम्बे ।
भक्तजनों के संकट, क्षण में दूर करे ॥
ॐ जय एकादशी॥

मुनि व्यासजी ने सुनाई, पापनाशिनी तेरी कथा।
नारद जी नें ब्रह्मा से पाई, जग को दी है यह कथा।
एकादशी के पुण्यव्रत से, मोक्ष मिले जन को ।
भक्तजनों के संकट, क्षण में दूर करे ॥
ॐ जय एकादशी॥

तुमने कहा हरि से जाकर, मुझको व्रत दे दो।
मुझ पर कृपा करो हे माते, यह वरदान दे दो।
हरि ने तुमको शक्ति दी, पाप नाश करन को ।
भक्तजनों के संकट, क्षण में दूर करे ॥
ॐ जय एकादशी॥

भाद्र पक्ष शुक्ल एकादशी, पहली बार आई।
मुर दैत्य को हरि से पाकर, मारा था तुमने।
तब से जग में यह तिथि, पावन हुई जग को ।
भक्तजनों के संकट, क्षण में दूर करे ॥
ॐ जय एकादशी॥

जो जन आरती प्रेम सहित नित गावे।
सुख-सम्पत्ति और परम शान्ति पावे।
पुत्र, धन, मान-बड़ाई, घर में नित आवे ।
भक्तजनों के संकट, क्षण में दूर करे ॥
ॐ जय एकादशी॥"""

# Update the item in lakshmi collection
for item in data['lakshmi']['items']:
    if item.get('id') == 'drik_goddesses_10':
        item['title'] = 'एकादशी माता आरती'
        item['title_en'] = 'Ekadashi Mata Aarti'
        item['hi_line'] = 'ॐ जय एकादशी, जय एकादशी'
        item['en_line'] = 'Om Jai Ekadashi, Jai Ekadashi'
        item['sub'] = 'ॐ जय एकादशी, जय एकादशी • एकादशी माता की पावन आरती'
        item['drik_url'] = 'https://www.drikpanchang.com/lyrics/aarti/ekadashi/ekadashi-aarti.html?lang=hi&ck=1'
        item['source'] = 'Drik Panchang'
        item['originalHindi'] = 'ॐ जय एकादशी, जय एकादशी'
        item['content'] = EKADASHI_AARTI
        print("Updated Ekadashi item successfully!")
        print("Title:", item['title'])
        print("Content length:", len(item['content']))
        break

# Save back
with open('final_granular_aarti_collections.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved final_granular_aarti_collections.json")
