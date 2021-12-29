import os
import cv2 as cv
import pandas as pd
from pyzbar import pyzbar
import time
import numpy as np

def scan_qrcode(qrcode):
    data = pyzbar.decode(qrcode)
    return data[0].data.decode('utf-8')
