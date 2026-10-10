import cv2
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

assets_dir = os.path.join(os.getcwd(), "assets", "games")
os.makedirs(assets_dir, exist_ok=True)

# Let's inspect coordinates of card and portals on a 400x880 frame
# Resolution: 400 x 880
# Card in frame_002_7s.jpg:
# Center card is roughly: x: 75 to 325, y: 245 to 575
# Left portal: x: 30 to 175, y: 590 to 760
# Right portal: x: 225 to 370, y: 590 to 760

def crop_and_save(img_path, box, out_name):
    img = cv2.imread(img_path)
    if img is None:
        print(f"Failed to read {img_path}")
        return
    x1, y1, x2, y2 = box
    crop = img[y1:y2, x1:x2]
    out_path = os.path.join(assets_dir, out_name)
    cv2.imwrite(out_path, crop)
    print(f"Saved {out_name} ({crop.shape[1]}x{crop.shape[0]})")

# Card box: [75, 245, 325, 575]
card_box = (75, 245, 325, 575)

# Characters from extracted frames:
crop_and_save("video_frames/frame_002_7s.jpg", card_box, "char_sunaina.jpg")
crop_and_save("video_frames/frame_004_15s.jpg", card_box, "char_janak.jpg")
crop_and_save("video_frames/frame_006_23s.jpg", card_box, "char_manthara.jpg")
crop_and_save("video_frames/frame_008_31s.jpg", card_box, "char_sita.jpg")
crop_and_save("video_frames/frame_010_39s.jpg", card_box, "char_shatrughna.jpg")
crop_and_save("video_frames/frame_014_55s.jpg", card_box, "char_urmila.jpg")
crop_and_save("video_frames_round_end/frame_64s.jpg", (45, 140, 355, 570), "card_kaikeyi_review.jpg")
crop_and_save("video_frames/frame_018_71s.jpg", (45, 140, 355, 570), "card_kaikeyi.jpg")

# Portals:
crop_and_save("video_frames/frame_004_15s.jpg", (30, 590, 175, 765), "portal_ayodhya.jpg")
crop_and_save("video_frames/frame_004_15s.jpg", (225, 590, 370, 765), "portal_mithila.jpg")

# Background:
crop_and_save("video_frames/frame_000_0s.jpg", (0, 0, 400, 880), "epic_games_menu_ref.jpg")

print("All game assets cropped successfully!")
