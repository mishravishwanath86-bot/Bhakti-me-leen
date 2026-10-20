import os
import sys
from PIL import Image
import numpy as np
from scipy.ndimage import binary_dilation

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

UPLOAD_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\brain\6b9a217f-950d-4540-a0f0-1f4ff949f487\.user_uploaded"
APP_DIR = r"C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
GAMES_DIR = os.path.join(APP_DIR, "assets", "games")
os.makedirs(GAMES_DIR, exist_ok=True)

im2_path = os.path.join(UPLOAD_DIR, "media_1792427703194.jpg") # Image 2 (Winged Gold Frame)
im3_path = os.path.join(UPLOAD_DIR, "media_1792427703313.png") # Image 3 (Fiery Demon Right Portal)
im4_path = os.path.join(UPLOAD_DIR, "media_1792427703341.jpg") # Image 4 (Sun Purple Left Portal)
im5_path = os.path.join(UPLOAD_DIR, "media_1792427703388.jpg") # Image 5 (Vedic Temple Arena Background)

print("1. Processing Image 5 -> swipe_arena_bg.jpg...")
im5 = Image.open(im5_path).convert("RGB")
bg_dest = os.path.join(GAMES_DIR, "swipe_arena_bg.jpg")
im5.save(bg_dest, "JPEG", quality=92)
# Also overwrite bg_vedic_temple.jpg so any legacy reference gets the clean background
im5.save(os.path.join(GAMES_DIR, "bg_vedic_temple.jpg"), "JPEG", quality=92)
print("✓ Saved swipe_arena_bg.jpg & updated bg_vedic_temple.jpg")

print("\n2. Processing Image 2 -> card_gold_winged_frame.png...")
im2 = Image.open(im2_path).convert("RGBA")
arr2 = np.array(im2)

# Outer black background removal
outer_mask = np.zeros((1024, 764), dtype=bool)
outer_mask[0:135, :] = True
outer_mask[885:1024, :] = True
outer_mask[:, 0:122] = True
outer_mask[:, 642:764] = True
is_black = (arr2[:, :, 0] < 22) & (arr2[:, :, 1] < 22) & (arr2[:, :, 2] < 22) & outer_mask

# Inner light-blue window removal:
# Inner window is roughly between x in [124, 640] and y in [135, 860]
inner_mask = np.zeros((1024, 764), dtype=bool)
inner_mask[135:860, 124:640] = True
is_blue = (arr2[:, :, 2].astype(int) > arr2[:, :, 0].astype(int) + 18) & (arr2[:, :, 2].astype(int) > arr2[:, :, 1].astype(int) + 8) & (arr2[:, :, 2] > 175)
cutout_blue = is_blue & inner_mask
cutout_blue = binary_dilation(cutout_blue, iterations=2)

arr2[is_black, 3] = 0
arr2[cutout_blue, 3] = 0

frame_img = Image.fromarray(arr2)
frame_dest = os.path.join(GAMES_DIR, "card_gold_winged_frame.png")
frame_img.save(frame_dest, "PNG")
print("✓ Saved card_gold_winged_frame.png")

print("\n3. Processing Image 4 -> portal_left_sun.png...")
im4 = Image.open(im4_path).convert("RGBA")
arr4 = np.array(im4)
is_black4 = (arr4[:, :, 0] < 22) & (arr4[:, :, 1] < 22) & (arr4[:, :, 2] < 22)
arr4[is_black4, 3] = 0
portal_left = Image.fromarray(arr4)
portal_left_dest = os.path.join(GAMES_DIR, "portal_left_sun.png")
portal_left.save(portal_left_dest, "PNG")
print("✓ Saved portal_left_sun.png")

print("\n4. Processing Image 3 -> portal_right_demon.png...")
im3 = Image.open(im3_path).convert("RGBA")
portal_right_dest = os.path.join(GAMES_DIR, "portal_right_demon.png")
im3.save(portal_right_dest, "PNG")
print("✓ Saved portal_right_demon.png")

print("\n=== All 4 Assets Processed & Saved Successfully ===")
