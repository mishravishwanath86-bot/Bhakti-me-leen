import shutil
import os

src = r"C:\Users\vishw\.gemini\antigravity-ide\brain\3b88eaf3-1c95-41f0-845b-726a512c06a7\gita_upadesh_card_1790482098473.jpg"
dst1 = r"assets\gallery\gita_upadesh_card.jpg"
dst2 = r"assets\gita_upadesh_hero.jpg"

shutil.copyfile(src, dst1)
shutil.copyfile(src, dst2)
print("Copied gita_upadesh_card to assets/gallery/ and assets/ successfully!")
print("dst1 size:", os.path.getsize(dst1))
