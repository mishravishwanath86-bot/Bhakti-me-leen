import json
import os

p = 'assets/cards/swipe_game_data.json'
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

cat_i18n = {
    'cat_1_ramayana': {
        'thumb': 'assets/games/cat_split_ayodhya.jpg',
        'title_en': 'Ayodhya or Mithila',
        'title_hi': 'अयोध्या या मिथिला',
        'title_te': 'అయోధ్య లేదా మిథిల',
        'instruction_en': 'Swipe towards Ayodhya or Mithila',
        'instruction_hi': 'अयोध्या या मिथिला के पक्ष की ओर स्वाइप करें',
        'instruction_te': 'అయోధ్య లేదా మిథిల వైపు స్వైప్ చేయండి',
        'vs_en': 'Ayodhya VS Mithila',
        'vs_hi': 'अयोध्या VS मिथिला',
        'vs_te': 'అయోధ్య VS మిథిల',
        'left_en': 'Ayodhya',
        'left_hi': 'अयोध्या',
        'left_te': 'అయోధ్య',
        'right_en': 'Mithila',
        'right_hi': 'मिथिला',
        'right_te': 'మిథిల'
    },
    'cat_2_lanka_war': {
        'thumb': 'assets/games/cat_split_lanka.jpg',
        'title_en': 'Rama Army or Ravana Army',
        'title_hi': 'राम सेना या रावण सेना',
        'title_te': 'రామ సైన్యం లేదా రావణ సైన్యం',
        'instruction_en': 'Swipe towards Rama Army or Ravana Army',
        'instruction_hi': 'राम सेना या रावण सेना की ओर स्वाइप करें',
        'instruction_te': 'రామ సైన్యం లేదా రావణ సైన్యం వైపు స్వైప్ చేయండి',
        'vs_en': 'Vanaras VS Rakshasas',
        'vs_hi': 'वानर सेना VS राक्षस सेना',
        'vs_te': 'వానర సైన్యం VS రాక్షసులు',
        'left_en': 'Rama Army',
        'left_hi': 'राम सेना',
        'left_te': 'రామ సైన్యం',
        'right_en': 'Ravana Army',
        'right_hi': 'रावण सेना',
        'right_te': 'రావణ సైన్యం'
    },
    'cat_3_mahabharat': {
        'thumb': 'assets/games/cat_split_mahabharata.jpg',
        'title_en': 'Pandavas or Kauravas',
        'title_hi': 'पाण्डव या कौरव',
        'title_te': 'పాండవులు లేదా కౌరవులు',
        'instruction_en': 'Swipe towards Pandavas or Kauravas',
        'instruction_hi': 'पाण्डव या कौरव पक्ष की ओर स्वाइप करें',
        'instruction_te': 'పాండవులు లేదా కౌరవుల వైపు స్వైప్ చేయండి',
        'vs_en': 'Pandavas VS Kauravas',
        'vs_hi': 'पाण्डव VS कौरव',
        'vs_te': 'పాండవులు VS కౌరవులు',
        'left_en': 'Pandavas',
        'left_hi': 'पाण्डव',
        'left_te': 'పాండవులు',
        'right_en': 'Kauravas',
        'right_hi': 'कौरव',
        'right_te': 'కౌరవులు'
    }
}

for cat in data['categories']:
    cid = cat['id']
    if cid in cat_i18n:
        cinfo = cat_i18n[cid]
        cat['thumb'] = cinfo['thumb']
        cat['title_en'] = cinfo['title_en']
        cat['title_hi'] = cinfo['title_hi']
        cat['title_te'] = cinfo['title_te']
        cat['instruction_en'] = cinfo['instruction_en']
        cat['instruction_hi'] = cinfo['instruction_hi']
        cat['instruction_te'] = cinfo['instruction_te']
        cat['vs_en'] = cinfo['vs_en']
        cat['vs_hi'] = cinfo['vs_hi']
        cat['vs_te'] = cinfo['vs_te']
        cat['leftSide']['name_en'] = cinfo['left_en']
        cat['leftSide']['name_hi'] = cinfo['left_hi']
        cat['leftSide']['name_te'] = cinfo['left_te']
        cat['rightSide']['name_en'] = cinfo['right_en']
        cat['rightSide']['name_hi'] = cinfo['right_hi']
        cat['rightSide']['name_te'] = cinfo['right_te']

with open(p, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated category i18n metadata successfully!')
