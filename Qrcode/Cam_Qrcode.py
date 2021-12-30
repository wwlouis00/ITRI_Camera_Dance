from matplotlib.pyplot import grid
import numpy as np
import os
import sys
import cv2 as cv
import pandas as pd
from pyzbar import pyzbar
import time
import pandas as pd

def scan_qrcode(qrcode):
    data = pyzbar.decode(qrcode)
    return data[0].data.decode('utf-8')

def show_camera():
    flag,image = cap.read()
    show = cv.resize(image, (640, 480))
    show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
    gray = cv.cvtColor(show, cv.COLOR_BGR2GRAY)
    global fm
    fm = cv.Laplacian(gray,cv.CV_64F).var()
    fm = int(fm)
    global fm1
    if(fm>100):
        print('焦距檢測:對焦成功')
        fm1 = "Pass"
    else:
        print('焦距檢測:對焦失敗')
        fm1 = "Fail"

def main():
    global timer_camera,cap,number1
    number1 = 1
    cap = cv.VideoCapture()
    show_camera()

if __name__ == "__main__":
    main()
