import cv2 as cv
from datetime import datetime

def main():
    cap = cv.VideoCapture(0)

    recording = False  # 是否正在錄影
    out1 = None  # 初始化cam1的影片寫入器

    while True:
        ret, frame = cap.read()
        cv.imshow('Webcam 1', frame)
        # 鍵盤錄製處理
        key = cv.waitKey(1) & 0xFF
        if key == ord('s') and not recording:  # 按下s開始錄影
            recording = True
            print("開始錄影")
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            # 設定影片寫入器
            fourcc = cv.VideoWriter_fourcc(*'mp4v') 
            out = cv.VideoWriter(f'./video_all/testcam1_{timestamp}.mp4', fourcc, 20.0, (640, 480))
            
        elif key == ord('q'):  # 按下q停止錄影並退出迴圈
            print("結束程式")
            break

        # 如果正在錄影，將影像寫入影片檔案
        if recording:
            out.write(frame)
    # 釋放webcam資源
    cap.release()


    # 釋放影片寫入器
    if  out is not None:
        out.release()
    # 關閉所有OpenCV視窗
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
