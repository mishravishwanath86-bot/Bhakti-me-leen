import cv2
import os

video_path = r"C:\Users\vishw\Downloads\WhatsApp Video 2026-09-27 at 17.16.59.mp4"
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

frames_dir = os.path.join(os.getcwd(), "video_frames_extra")
os.makedirs(frames_dir, exist_ok=True)

# check timestamps: 1s, 2s, 3s, 65s, 66s, 68s, 70s
targets = [1.0, 2.0, 3.0, 65.0, 68.0, 70.0, 72.0]
for t in targets:
    f_num = int(t * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, f_num)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(os.path.join(frames_dir, f"frame_{int(t)}s.jpg"), frame)
        print(f"Saved frame at {t}s")

cap.release()
