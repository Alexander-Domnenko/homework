#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:08:51 2020

@author: user
"""

import numpy as np
import cv2, PIL
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

frame = cv2.imread("photo.jpg")

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#blurred = cv2.bilateralFi(thresh,9,100,100)lter
blurred = cv2.bilateralFilter(gray,20,100,100)
ret,thresh = cv2.threshold(blurred,120,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Edges', thresh)
cv2.waitKey(0)