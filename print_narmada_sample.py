import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('final_granular_aarti_collections.json', 'r', encoding='utf-8') as f:
    fg = json.load(f)

for item in fg['ganga']['items']:
    if item['id'] == 'drik_goddesses_23':
        print("=== NARMADA ITEM KEYS & SAMPLES ===")
        print("title:", item.get('title'))
        print("title_en:", item.get('title_en'))
        print("en_line:", item.get('en_line'))
        print("hi_line:", item.get('hi_line'))
        print("sub:", item.get('sub'))
        print("source:", item.get('source'))
        print("\n--- CONTENT ---")
        print(item.get('content'))
        print("\n--- MEANING ---")
        print(item.get('meaning')[:500])
        print("\n--- VIDHI ---")
        print(item.get('vidhi')[:500])
        print("\n--- SIGNIFICANCE ---")
        print(item.get('significance')[:500])
        print("\n--- ENGLISH LYRICS ---")
        print(item.get('english_lyrics')[:400])
        break
