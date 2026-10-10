import cv2, os
video_path = r"C:\Users\vishw\Downloads\WhatsApp Video 2026-09-27 at 17.16.59.mp4"
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
for t in [76.0, 78.0, 80.0, 82.0, 84.0, 86.0]:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(t * fps))
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"video_frames_round_end/frame_{int(t)}s.jpg", frame)
cap.release()
print("Saved 76-86s")
