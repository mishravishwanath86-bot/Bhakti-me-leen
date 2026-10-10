import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# run parse_all_chalisas logic to get list
from parse_all_chalisas import chalisas

existing = [
   'chalisa_bajrang_baan', 'chalisa_ganga', 'chalisa_santoshi', 'chalisa_khatushyam',
   'chalisa_saibaba', 'chalisa_hanuman', 'chalisa_ganesh', 'chalisa_durga',
   'chalisa_shiv', 'chalisa_ram', 'chalisa_krishna', 'chalisa_shani',
   'chalisa_gopal', 'chalisa_lakshmi', 'chalisa_surya', 'chalisa_vishnu',
   'chalisa_brahma', 'chalisa_bhairav', 'chalisa_bhairav2', 'chalisa_navagraha',
   'chalisa_vishwakarma', 'chalisa_parashurama', 'chalisa_balaji', 'chalisa_giriraj',
   'chalisa_ramdev', 'chalisa_kubera', 'chalisa_narasimha'
]

print(f"Total Drik Chalisas: {len(chalisas)}")
for idx, c in enumerate(chalisas):
    print(f"{idx+1}. {c['title']} ({c['hi_line']}) -> {c['drik_url']}")
