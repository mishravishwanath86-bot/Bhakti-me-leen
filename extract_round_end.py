import cv2
import os

video_path = r"C:\Users\vishw\Downloads\WhatsApp Video 2026-09-27 at 17.16.59.mp4"
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

frames_dir = os.path.join(os.getcwd(), "video_frames_round_end")
os.makedirs(frames_dir, exist_ok=True)

targets = [61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0]
for t in targets:
    f_num = int(t * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, f_num)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(os.path.join(frames_dir, f"frame_{int(t)}s.jpg"), frame)

cap.release()
print("Extracted round end frames!")
