#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import sys
import cv2 as cv
import xlwt
import xlrd
from xlutils.copy import copy
from pyzbar import pyzbar
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import os

global  test
test = 1
def scan_qrcode(qrcode):
    data = pyzbar.decode(qrcode)
    return data[0].data.decode('utf-8')

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        self.timer_camera = QtCore.QTimer()
        self.cap = cv.VideoCapture()
        self.CAM_NUM = 0