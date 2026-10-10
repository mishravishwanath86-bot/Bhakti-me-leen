import cv2
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

video_path = r"C:\Users\vishw\Downloads\WhatsApp Video 2026-09-27 at 17.16.59.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file")
    sys.exit(1)

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
duration_sec = total_frames / fps if fps > 0 else 0

print(f"Video Properties:")
print(f"  Resolution: {width} x {height}")
print(f"  FPS: {fps:.2f}")
print(f"  Total Frames: {total_frames}")
print(f"  Duration: {duration_sec:.2f} seconds ({duration_sec/60:.2f} minutes)")

# Create frames directory
frames_dir = os.path.join(os.getcwd(), "video_frames")
os.makedirs(frames_dir, exist_ok=True)

# Extract 1 frame every 3-5 seconds to understand the progression
step_sec = 4
step_frames = int(fps * step_sec) if fps > 0 else 100

extracted = 0
frame_idx = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_idx % step_frames == 0:
        time_pos = frame_idx / fps if fps > 0 else 0
        frame_name = f"frame_{extracted:03d}_{int(time_pos)}s.jpg"
        out_path = os.path.join(frames_dir, frame_name)
        cv2.imwrite(out_path, frame)
        print(f"Extracted {frame_name} at {time_pos:.1f}s")
        extracted += 1
    frame_idx += 1

cap.release()
print(f"\nTotal frames extracted: {extracted}")
