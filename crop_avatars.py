import cv2, os

assets_dir = os.path.join(os.getcwd(), "assets", "games")

def crop(path, box, name):
    im = cv2.imread(path)
    if im is not None:
        c = im[box[1]:box[3], box[0]:box[2]]
        cv2.imwrite(os.path.join(assets_dir, name), c)
        print("Cropped", name)

# from frame_57s.jpg:
crop("video_frames_round_end/frame_57s.jpg", (130, 725, 235, 835), "avatar_kaushalya.jpg")
crop("video_frames_round_end/frame_57s.jpg", (250, 725, 355, 835), "avatar_sumitra.jpg")

# from frame_018_71s.jpg:
crop("video_frames/frame_018_71s.jpg", (265, 725, 370, 835), "avatar_mandavi.jpg")
crop("video_frames/frame_018_71s.jpg", (150, 725, 255, 835), "avatar_kaikeyi.jpg")
crop("video_frames/frame_018_71s.jpg", (35, 725, 140, 835), "avatar_manthara.jpg")

# from frame_020_79s.jpg:
crop("video_frames/frame_020_79s.jpg", (35, 725, 140, 835), "avatar_shrutakirti.jpg")
crop("video_frames/frame_020_79s.jpg", (150, 725, 255, 835), "avatar_janak.jpg")
crop("video_frames/frame_020_79s.jpg", (265, 725, 370, 835), "avatar_kushadhwaja.jpg")

# from frame_68s.jpg:
crop("video_frames_extra/frame_68s.jpg", (35, 725, 140, 835), "avatar_sita.jpg")
crop("video_frames_extra/frame_68s.jpg", (150, 725, 255, 835), "avatar_urmila.jpg")

# Background temple from frame 002
crop("video_frames/frame_002_7s.jpg", (0, 0, 400, 880), "bg_vedic_temple.jpg")

print("All avatar crops complete!")
