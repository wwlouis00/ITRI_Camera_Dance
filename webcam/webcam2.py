import cv2

def main():
    # 开启第一个webcam
    cap1 = cv2.VideoCapture(1)
    if not cap1.isOpened():
        print("Error: Could not open webcam 1.")
        exit()

    # 开启第二个webcam（通常是1，如果不行可以尝试其他数字）
    cap2 = cv2.VideoCapture(2)
    if not cap2.isOpened():
        print("Error: Could not open webcam 2.")
        exit()

    # 开启第三个webcam（通常是2，如果不行可以尝试其他数字）
    cap3 = cv2.VideoCapture(3)
    if not cap3.isOpened():
        print("Error: Could not open webcam 3.")
        exit()

    while True:
        # 读取第一个webcam的影像
        ret1, frame1 = cap1.read()
        if ret1 and frame1 is not None and frame1.shape[0] > 0 and frame1.shape[1] > 0:
            cv2.imshow('Webcam 1', frame1)
        
        # 读取第二个webcam的影像
        ret2, frame2 = cap2.read()
        if ret2 and frame2 is not None and frame2.shape[0] > 0 and frame2.shape[1] > 0:
            cv2.imshow('Webcam 2', frame2)

        # 读取第三个webcam的影像
        ret3, frame3 = cap3.read()
        if ret3 and frame3 is not None and frame3.shape[0] > 0 and frame3.shape[1] > 0:
            cv2.imshow('Webcam 3', frame3)

        # 按下 'q' 键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放webcam资源
    cap1.release()
    cap2.release()
    cap3.release()
    # 关闭所有OpenCV窗口
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



# import cv2

# def main():
#     # 開啟第一個webcam
#     cap1 = cv2.VideoCapture(1)
    
#     # 開啟第二個webcam（通常是1，如果不行可以試試其他數字）
#     cap2 = cv2.VideoCapture(2)

#     # 開啟第二個webcam（通常是1，如果不行可以試試其他數字）
#     cap3 = cv2.VideoCapture(0)
#     while True:
#         # 讀取第一個webcam的影像
#         ret1, frame1 = cap1.read()
        
#         # 讀取第二個webcam的影像
#         ret2, frame2 = cap2.read()

#         # 讀取第二個webcam的影像
#         ret3, frame3 = cap3.read()

#         # 顯示第一個webcam的影像
#         cv2.imshow('Webcam 1', frame1)
        
#         # 顯示第二個webcam的影像
#         cv2.imshow('Webcam 2', frame2)

#         # 顯示第二個webcam的影像
#         cv2.imshow('Webcam 3', frame3)

#         # 按下 'q' 鍵退出迴圈
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # 釋放webcam資源
#     cap1.release()
#     cap2.release()
#     cap3.release()
#     # 關閉所有OpenCV視窗
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()
