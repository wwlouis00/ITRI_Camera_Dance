# import cv2

# def print_supported_resolutions(cap, cap_name):
#     resolutions = [(int(cap.get(9)), int(cap.get(16))) for _ in range(10)]
#     resolutions = list(filter(lambda x: x[0] > 0 and x[1] > 0, resolutions))  # 移除无效的分辨率
#     print(f'{cap_name} supported resolutions:', resolutions)

# def main():
#     # 開啟第一個webcam
#     cap1 = cv2.VideoCapture(0)
    
#     # 開啟第二個webcam（通常是1，如果不行可以試試其他數字）
#     cap2 = cv2.VideoCapture(2)
    
#     # 開啟第三個webcam（通常是1，如果不行可以試試其他數字）
#     cap3 = cv2.VideoCapture(3)

#     # 打印每个摄像头支持的分辨率
#     print_supported_resolutions(cap1, 'Cap1')
#     print_supported_resolutions(cap2, 'Cap2')
#     print_supported_resolutions(cap3, 'Cap3')

#     # 释放webcam资源
#     cap1.release()
#     cap2.release()
#     cap3.release()

# if __name__ == "__main__":
#     main()


import cv2

def list_available_cameras():
    # 尋找所有可用的 webcam 設備
    index = 0
    while True:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if not cap.isOpened():
            break
        print(f"Webcam {index}: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
        cap.release()
        index += 1

if __name__ == "__main__":
    list_available_cameras()
