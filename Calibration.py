from camera import Camera
import camera
from numpy.lib.type_check import imag
# from public_method import *
from datetime import datetime
import numpy as np
import cv2 as cv
import math
import csv


#Erosion 影像侵蝕 
#cv2.erode() 的第一個參數為二值化的影像， 第二個參數為使用的捲積 kernel，第三個參數為迭代次數(預設為1)，
#範例中的 kernel 捲積大小為 3x3，可以改成 5x5 或 7x7 較為常見，預設值為 3x3
def erode(image, kernel_para=3, iterations=1):
    kernel = np.ones((kernel_para, kernel_para), np.uint8)
    image_ero =cv.erode(image,kernel,iterations=iterations)
    return image_ero

def dilate(image, kernerl_para = 3, iterations=1):
    kernerl = np.ones((kernerl_para,kernerl_para),np.unit8)
    image_dil = cv.dilate(image, kernerl ,iterations=iterations)
    return image_dil

def binarize(image):
    ret , mask =cv.threshold(image,0,255, cv.THRESH_OTSU)
    return mask

class Calibration:
    def __init__(self):
        pass
    def generate_mask():
        """
        :return image 回傳影像
        :return mask  
        """
        cam =camera()
        try:
            imag = cam.shot()
        finally:
            cam.close()