import  cv2 as cv
import numpy as np

def Picture_setup():
    
    blank = np.zeros((500,500,3),dtype='uint8')
    #cv.imshow('Blank', blank)

    #1. Paint the image a certain color
    blank[200:300,300:400] = 0,0,255
    cv.imshow('Green', blank)

    #2. 畫矩形

    #cv.rectangle(blank, (0,0), (250,500),(0,255,0), thickness=cv.FILLED)
    cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[1]//2), (0,255,0),thickness=-1)
    cv.imshow('Rectangle',blank)

    #3. 畫圓
    cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40,(0,0,255), thickness=-1)
    cv.imshow('Circle',blank)

    #4. 畫線
    #cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2), (255,255,255),thickness=3)
    #cv.line(blank,(100,250),(blank.shape[1]//2,blank.shape[0]//2), (255,255,255),thickness=3)
    cv.line(blank,(100,250),(300,400),(255,255,255), thickness=3)
    cv.imshow('Line',blank)

    #5. Write text
    cv.putText(blank,"Opencv Learn",(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
    cv.imshow('Text',blank)

while True:
    Picture_setup()
    if cv.waitKey(20) & 0xFF==ord('D'):
        break

cv.waitKey(0) #waitKey()函數是一個給定時間內等待使用者案件觸發；如果使用者