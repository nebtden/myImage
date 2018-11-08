import numpy as np
from pandas import *
import cv2
import os, sys
from core.simple_color import getcolorindex

# img = cv2.imread('red.jpg')
img = cv2.imread('sources/mickey2.jpg')
rgb_img = img[..., ::-1]
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
ret,thresh = cv2.threshold(imgray,127,255,0)


for x in list(range(10)):
    old = x
    x = old+562
    y = old+665
    print(img[y,x])
    print(rgb_img[y,x])
    print(hsv_img[y,x])
    print("\n")