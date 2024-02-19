
import cv2

def main():
    # 開啟第一個webcam
    cap1 = cv2.VideoCapture(0)
    
    # 開啟第二個webcam（通常是1，如果不行可以試試其他數字）
    cap2 = cv2.VideoCapture(2)

    # 開啟第二個webcam（通常是1，如果不行可以試試其他數字）
    cap3 = cv2.VideoCapture(3)
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

        # 按下 'q' 鍵退出迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 釋放webcam資源
    cap1.release()
    cap2.release()
    cap3.release()
    # 關閉所有OpenCV視窗
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
