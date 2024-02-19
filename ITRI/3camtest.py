import cv2

def main():
    # 開啟第一個webcam
    cap1 = cv2.VideoCapture(4)
    
    # 開啟第二個webcam（通常是1，如果不行可以試試其他數字）
    cap2 = cv2.VideoCapture(6)
    # 開啟第二個webcam（通常是1，如果不行可以試試其他數字）
    cap3 = cv2.VideoCapture(8)

    # 設定影片寫入器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 或者使用 'H264'
    out1 = cv2.VideoWriter('testcam1.mp4', fourcc, 30.0, (640, 480))
    out2 = cv2.VideoWriter('testcam2.mp4', fourcc, 30.0, (640, 480))
    out3 = cv2.VideoWriter('testcam3.mp4', fourcc, 30.0, (640, 480))



    recording = False  # 是否正在錄影

    while True:
        # 讀取第一個webcam的影像
        ret1, frame1 = cap1.read()
        
        # 讀取第二個webcam的影像
        ret2, frame2 = cap2.read()

        # 讀取第二個webcam的影像
        ret3, frame3 = cap3.read()

        # 顯示第一個webcam的影像
        cv2.imshow('Webcam 1', frame1)
        
        # 顯示第二個webcam的影像
        cv2.imshow('Webcam 2', frame2)

        # 顯示第二個webcam的影像
        cv2.imshow('Webcam 3', frame3)

        # 鍵盤事件處理
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # 開始錄影
            recording = True
        elif key == ord('q'):  # 停止錄影並退出迴圈
            break

        # 如果正在錄影，將影像寫入影片檔案
        if recording:
            out1.write(frame1)
            out2.write(frame2)
            out3.write(frame3)

    # 釋放webcam資源
    cap1.release()
    cap2.release()
    cap3.release()

    # 釋放影片寫入器
    out1.release()
    out2.release()
    out3.release()

    # 關閉所有OpenCV視窗
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
