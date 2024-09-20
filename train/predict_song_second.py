from ultralytics import YOLO
import glob

model = YOLO("/root/Work/itri_dance/model/pose_20240321_second.pt")
model.info()

# Detecting images(.jpg or .png) in an entire folder.
for image_path in glob.glob(f'/root/Work/itri_dance/video/20240221/*mp4'):
      results = model.predict(source=image_path,project="/root/Work/itri_dance/result/song_first/20240221",save=True)
      print("\n")
