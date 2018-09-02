import numpy as np
from pandas import *
import cv2
import colorsys

img = cv2.imread('sources/mickey2.jpg')
print(type(img))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 254,194,62  黄颜色
# 252,25,34  黄颜色



lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask0 = cv2.inRange(hsv, lower_red, upper_red)

# upper mask (170-180)
lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([11, 50, 50])
upper_red = np.array([34, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

# join my masks
red = mask0+mask1


cv2.imshow('src',img)
cv2.imshow('red',red)
cv2.imshow('show2',mask2)
# cv2.waitKey()
while(1):
    # cv2.imshow('newimg', newimg)
    if cv2.waitKey(1) == ord('q'):
        break
