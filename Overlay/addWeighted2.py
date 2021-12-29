import cv2
import numpy as np

def nothing(x):
    pass

img1 = cv2.imread('ROI.bmp')
img2 = cv2.imread('well.png')
# 創建一個黑色背景的窗口
img = np.zeros((500,500,3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('a','image',0,100,nothing)


while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv2.getTrackbarPos('a','image')
    r=float(r)/100.0

    img=cv2.addWeighted(img1,r,img2,1.0-r,0)

cv2.destroyAllWindows()