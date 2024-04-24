from ultralytics import YOLO
import glob

model = YOLO("your_model")
model.info()

# Detecting images(.jpg or .png) in an entire folder.
for image_path in glob.glob(f'your_video'):
      results = model.predict(source=image_path,project="your_save_dir",save=True)
      print("\n")
