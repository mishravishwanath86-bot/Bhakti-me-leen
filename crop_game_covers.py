import cv2
import os

img = cv2.imread("video_frames/frame_000_0s.jpg")
# Resolution: 400 x 880
# Grid starts around y: 120, x: 15 to 385
# Card 1 (Match): x: 15 to 195, y: 120 to 380
# Card 2 (Swipe): x: 205 to 385, y: 120 to 380
# Card 3 (JigSaw): x: 15 to 195, y: 400 to 660
# Card 4 (PadaBandham): x: 205 to 385, y: 400 to 660

assets_dir = os.path.join(os.getcwd(), "assets", "games")
cv2.imwrite(os.path.join(assets_dir, "cover_match.jpg"), img[120:385, 15:195])
cv2.imwrite(os.path.join(assets_dir, "cover_swipe.jpg"), img[120:385, 205:385])
cv2.imwrite(os.path.join(assets_dir, "cover_jigsaw.jpg"), img[400:665, 15:195])
cv2.imwrite(os.path.join(assets_dir, "cover_padabandham.jpg"), img[400:665, 205:385])

print("Cropped 4 game covers from frame 0!")
