import os
import cv2 as cv
import numpy as np

img1 = cv.imread('Photos/cat_large.jpg')
img2 = cv.imread('Photos/cat.jpg')

res = cv.add(img1,img2)

def nothing(x):
    pass

# 創建一個黑色背景的窗口
img = np.zeros((500,500,3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('a','image',0,100,nothing)


while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    r = cv.getTrackbarPos('a','image')
    r= float(r)/100.0

    img=cv.addWeighted(img1,r,img2,1.0-r,0)

cv.destroyAllWindows()