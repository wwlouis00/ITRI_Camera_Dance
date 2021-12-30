import cv2 as cv

img = cv.imread("C:\python\opencv\Photos\cat_large.jpg")

cv.imshow('CAT',img)

capture = cv.VideoCapture("C:\python\opencv\Videos\dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("video",frame)

    if cv.waitKey(20) & 0xFF==ord("d"): #等待20秒後 或 按d鍵則執行這個此動作
        break

capture.release()

cv.destroyAllWindows()

# cv.waitKey(0)

