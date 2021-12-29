import cv2 as cv
import numpy as np
# 加載圖像
img1 = cv.imread('well.png')
img2 = cv.imread('ROI.bmp')

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)      # 將圖片灰度化
ret, mask = cv.threshold(img2gray, 175, 255, cv.THRESH_BINARY)#ret是閾值（175）mask是二值化圖像
mask_inv = cv.bitwise_not(mask)#獲取把logo的區域取反 按位運算

img1_bg = cv.bitwise_and(roi,roi,mask = mask)#在img1上面，將logo區域和mask取與使值爲0

# 取 roi 中與 mask_inv 中不爲零的值對應的像素的值，其他值爲 0 。
# 把logo放到圖片當中
img2_fg = cv.bitwise_and(img2,img2,mask = mask_inv)#獲取logo的像素信息

dst = cv.add(img1_bg,img2_fg)#相加即可
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img2_fg)
cv.waitKey(0)
cv.destroyAllWindows()