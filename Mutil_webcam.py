

import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
# model = YOLO('/home/itri/project/camtest/camera/pose_20240320_first.pt')
model = YOLO('C:\project\Tool\pose_20240321_second.pt')
model2 = YOLO('C:\project\Tool\pose_20240320_first.pt')
# Open the video file
video_path = "testcam4_20240306110154.mp4"
# video_path2 = 0
cap = cv2.VideoCapture(video_path)
cap2 = cv2.VideoCapture(video_path)
# cap2 = cv2.VideoCapture(video_path2)
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    success, frame2 = cap.read(2)
    # success2, frame2 = cap2.read()
    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)
        results2 = model2.track(frame2, persist=True)
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        annotated_frame2 = results2[0].plot()
        # Display the annotated frame
        cv2.imshow("Web Tracking", annotated_frame)
        cv2.imshow("YOLOv8 Tracking2", annotated_frame2)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
# cap2.release()
cv2.destroyAllWindows()