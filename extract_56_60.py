import cv2, os
video_path = r"C:\Users\vishw\Downloads\WhatsApp Video 2026-09-27 at 17.16.59.mp4"
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
for t in [56.0, 57.0, 58.0, 59.0, 60.0]:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(t * fps))
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"video_frames_round_end/frame_{int(t)}s.jpg", frame)
cap.release()
print("Saved 56-60s")
