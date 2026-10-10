import cv2
import os

video_path = r"C:\Users\vishw\Downloads\WhatsApp Video 2026-09-27 at 17.16.59.mp4"
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

# Card name is around y: 530 to 570, x: 120 to 280
assets_dir = os.path.join(os.getcwd(), "assets", "games")

# Let's sample frames every 2 seconds
for sec in range(2, 60, 2):
    f_num = int(sec * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, f_num)
    ret, frame = cap.read()
    if ret:
        card_crop = frame[245:575, 75:325]
        cv2.imwrite(os.path.join(assets_dir, f"sample_{sec}s.jpg"), card_crop)

cap.release()
print("Saved 2s interval card samples!")
