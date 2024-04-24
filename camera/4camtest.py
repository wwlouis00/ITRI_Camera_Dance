import cv2
from datetime import datetime

def main():
    cap1 = cv2.VideoCapture(10)
    cap2 = cv2.VideoCapture(4)
    cap3 = cv2.VideoCapture(6)
    cap4 = cv2.VideoCapture(8)

    recording = False  # 是否正在錄影
    out1 = None  # 初始化cam1的影片寫入器

    while True:
        ret1, frame1 = cap1.read()
        
        ret2, frame2 = cap2.read()

        ret3, frame3 = cap3.read()

        ret4, frame4 = cap4.read()
        cv2.imshow('Webcam 1', frame1)
        cv2.imshow('Webcam 2', frame2)
        cv2.imshow('Webcam 3', frame3)
        cv2.imshow('Webcam 4', frame4)

        # 鍵盤錄製處理
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s') and not recording:  # 按下s開始錄影
            recording = True
            print("開始錄影")
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            # 設定影片寫入器
            fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
            out1 = cv2.VideoWriter(f'./video_all/testcam1_{timestamp}.mp4', fourcc, 30.0, (640, 480))
            out2 = cv2.VideoWriter(f'./video_all/testcam2_{timestamp}.mp4', fourcc, 30.0, (640, 480))
            out3 = cv2.VideoWriter(f'./video_all/testcam3_{timestamp}.mp4', fourcc, 30.0, (640, 480))
            out4 = cv2.VideoWriter(f'./video_all/testcam4_{timestamp}.mp4', fourcc, 30.0, (640, 480))
        elif key == ord('q'):  # 按下q停止錄影並退出迴圈
            print("結束程式")
            break

        # 如果正在錄影，將影像寫入影片檔案
        if recording:
            out1.write(frame1)
            out2.write(frame2)
            out3.write(frame3)
            out4.write(frame4)

    # 釋放webcam資源
    cap1.release()
    cap2.release()
    cap3.release()
    cap4.release()

    # 釋放影片寫入器
    if  out1 is not None:
        out1.release()
        out2.release()
        out3.release()
        out4.release()

    # 關閉所有OpenCV視窗
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
