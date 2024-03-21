import cv2
from ultralytics import YOLO


model = YOLO('C:\project\Tool\pose_20240321_second.pt')

video_path = "testcam4_20240306110154.mp4"
# 打开摄像头
cap = cv2.VideoCapture(video_path)

while True:
    # 读取一帧视频
    ret, frame = cap.read()

    # 在帧上添加文本
    text = "ITRT Dance"
    person = "person"
    cv2.putText(frame, text, (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(frame, person, (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    results = model.track(frame, persist=True)

    annotated_frame = results[0].plot()
    # 显示帧
    cv2.imshow('Camera', annotated_frame)

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频捕获对象并关闭窗口
cap.release()
cv2.destroyAllWindows()
