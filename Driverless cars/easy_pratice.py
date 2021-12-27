import cv2 as cv
img = cv.imread("./test.png") #讀取圖片
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #灰階處理 
cv.imshow('Normal',img)    #顯示原始圖片
cv.imshow('Gray',gray)
cv.waitKey(0)
cv.destroyAllWindows()