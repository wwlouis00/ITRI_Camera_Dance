import cv2 as cv

img = cv.imread("C:\python\opencv\Photos\cat_large.jpg")
cv.imshow('CAT',img)
#定義重新調整畫面的功能----------------------------------------------------------
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)  # dimensions 方面

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow("Image",resized_image)
# Reading Videos--------------------------------------------------------------
capture = cv.VideoCapture("C:\python\opencv\Videos\dog.mp4")
while True:
    
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=.2)
    #顯示Video
    cv.imshow("video",frame)
    #顯示Video Resized
    cv.imshow("Video Resized", frame_resized)
    # 若按下 D 鍵則離開迴圈
    if cv.waitKey(20) & 0xFF==ord("D"): 
        break

# 釋放攝影機
capture.release()

# 關閉所有 OpenCV 視窗
cv.destroyAllWindows()

cv.waitKey(0)  