import cv2
from datetime import datetime

def print_camera_properties(cap, camera_index):
    print(f"Camera {camera_index} Properties:")
    print(f"  Width: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
    print(f"  Height: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
    print(f"  FPS: {cap.get(cv2.CAP_PROP_FPS)}")
    print(f"  Brightness: {cap.get(cv2.CAP_PROP_BRIGHTNESS)}")
    print(f"  Contrast: {cap.get(cv2.CAP_PROP_CONTRAST)}")
    print(f"  Saturation: {cap.get(cv2.CAP_PROP_SATURATION)}")
    print(f"  Hue: {cap.get(cv2.CAP_PROP_HUE)}")
    print(f"  Gain: {cap.get(cv2.CAP_PROP_GAIN)}")
    print(f"  Exposure: {cap.get(cv2.CAP_PROP_EXPOSURE)}")

def main():
    # 開啟第一個webcam
    cap1 = cv2.VideoCapture(2)
    
    # 開啟第二個webcam（通常是1，如果不行可以試試其他數字）
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # 設定影片寫入器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 或者使用 'H264'
    out1 = cv2.VideoWriter(f'./video_all/testcam1_{timestamp}.mp4', fourcc, 20.0, (1920, 1080))

    recording = False  # 是否正在錄影

    print_camera_properties(cap1, 2)

    while True:
        # 讀取第一個webcam的影像
        ret1, frame1 = cap1.read()
        
        cv2.imshow('Webcam 1', frame1)
    
        # 鍵盤事件處理
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # 開始錄影
            recording = True
        elif key == ord('q'):  # 停止錄影並退出迴圈
            break

        # 如果正在錄影，將影像寫入影片檔案
        if recording:
            out1.write(frame1)

    # 釋放webcam資源
    cap1.release()

    # 釋放影片寫入器
    out1.release()

    # 關閉所有OpenCV視窗
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
