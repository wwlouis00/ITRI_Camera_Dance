import csv
import cv2 as cv
from ultralytics import YOLO
from datetime import datetime
import numpy as np

def calculate_iou(box1, box2):
    # Calculate intersection coordinates
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    # Calculate intersection area
    intersection_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)

    # Calculate areas of both boxes
    box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)

    # Calculate IoU
    iou = intersection_area / float(box1_area + box2_area - intersection_area)

    return iou

model = YOLO("model/pose_20240320_first.pt")
model2 = YOLO("yolov8s.pt")
print(model.names)

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# Open video file
video_path = "dance_video/20240131\原始影片/testcam3_20240131105545.mp4"
cap = cv.VideoCapture(video_path)
cap2 = cv.VideoCapture(video_path)

# Video resolution
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))    # Get the width of the frame
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))  # Get the height of the frame

# print("width:"+str(width)+"  height:"+str(height))
fourcc = cv.VideoWriter_fourcc(*'MJPG') 
out = cv.VideoWriter("result_first_song/"+str(timestamp)+'_predict.mp4', fourcc, 20.0, (width,  height))  # Create an empty video
out2 = cv.VideoWriter("result_first_song/"+str(timestamp)+'_person.mp4', fourcc, 20.0, (width,  height))  # Create an empty video
csv_file_path = 'result_first_song/第一首歌_'+str(timestamp)+'_results.csv'
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Frame", "Person ID", "人的位置", "動作位置", "動作類別", "動作分數"])
    
    frame_number = 0
    while True:
        ret, frame = cap.read()
        ret, frame2 = cap2.read()
        if not ret:
            print("End of video file reached")
            break
        
        detect_params = model.predict(frame, device=0)
        detect_params2 = model2.track(frame,classes=0, persist=True)
        boxes = detect_params[0].boxes
        boxes2 = detect_params2[0].boxes
       
        boxes2_xyxy = detect_params2[0].boxes.xyxy.cpu().numpy().astype(int)
        ids2_id = detect_params2 [0].boxes.id.cpu().numpy().astype(int)

        for box, id in zip(boxes2_xyxy, ids2_id):
            cv.rectangle(frame2, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
            cv.putText(
                frame2,
                f"Person: {id}",
                (box[0], 50),
                cv.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                2,
            )
        for box2, id2 in zip(boxes2, ids2_id):
            clsID = box2.cls.cpu().numpy()[0]
            conf = box2.conf.cpu().numpy()[0]
            bb = box2.xyxy.cpu().numpy()[0]
            
            # Find the closest box from model1
            closest_box = None
            closest_confidence = 0
            closest_class = ""
            for box1 in boxes:
                iou = calculate_iou(box1.xyxy.cpu().numpy()[0], bb)
                if iou > 0.5 and box1.conf.cpu().numpy()[0] > closest_confidence:
                    closest_confidence = box1.conf.cpu().numpy()[0]
                    closest_box = box1.xyxy.cpu().numpy()[0]
                    closest_class = model.names[box1.cls.cpu().numpy()[0]]
            
            # Write data to CSV
            if closest_box is not None:
                writer.writerow([frame_number, id2, bb, closest_box, closest_class, closest_confidence])

            
        annotated_frame = detect_params[0].plot()

        out.write(annotated_frame)
        out2.write(frame2)
        cv.imshow("first song",annotated_frame)
        cv.imshow("first song person", frame2) # Add this line to show boxes2 in a separate window
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
        frame_number += 1

cap.release()
out.release()
out2.release()
cv.destroyAllWindows()
