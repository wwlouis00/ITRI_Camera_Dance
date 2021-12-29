import numpy as np
import os
import cv2 as cv
import pandas as pd
from pyzbar import pyzbar
import time
import pandas as pd




def scan_qrcode(qrcode):
    data = pyzbar.decode(qrcode)
    return data[0].data.decode('utf-8')

def show_camera():
    global show
    show = cv.resize

def main():
    global timer_camera,cap
    cap = cv.VideoCapture()


if __name__ == "__main__":
    main()