import cv2

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
    # 開啟Webcam（可以嘗試不同的數字）
    cap = cv2.VideoCapture(4)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print_camera_properties(cap, 0)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow('Webcam', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
