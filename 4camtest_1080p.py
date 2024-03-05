import cv2
from datetime import datetime

def main():
    # 使用网络摄像机的默认索引（通常为0）
    camera_index = 0
    # 建立VideoCapture对象，指定网络摄像机的索引
    cap = cv2.VideoCapture(10)
    cap1 = cv2.VideoCapture(4)
    cap2 = cv2.VideoCapture(6)
    cap3 = cv2.VideoCapture(8)
    # 检查摄像机是否成功开启
    if not cap.isOpened():
        print("无法开启摄像机")
        exit()
    # 设置摄像机属性，例如帧宽度和帧高度
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap3.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    # 获取摄像机属性值，例如帧宽度和帧高度
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("摄像机帧宽度:", width)
    print("摄像机帧高度:", height)

    # 定义保存视频的参数
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(width), int(height)))
    out1 = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(width), int(height)))
    out2 = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(width), int(height)))
    out3 = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(width), int(height)))

    recording = False

    while True:
        # 读取当前帧的图像
        ret, frame = cap.read()

        # 显示当前帧的图像
        cv2.imshow("Webcam", frame)

        if recording:
            # 将当前帧写入输出视频
            out.write(frame)

        # 检查是否成功读取图像
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # 开始/停止录制
            recording = not recording
        elif key == ord('q'):  # 停止录制并退出循环
            break

    # 释放摄像机资源、关闭窗口和输出视频
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
