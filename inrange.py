import numpy as np
from pandas import *
import cv2
import colorsys

img = cv2.imread('sources/mickey2.jpg')
print(type(img))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 254,194,62  黄颜色
# 252,25,34  黄颜色


# 下面是红色
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask0 = cv2.inRange(hsv, lower_red, upper_red)

# upper mask (170-180)
lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)
red = mask0+mask1



cheng1 = np.array([11, 50, 50])
cheng2 = np.array([25, 255, 255])
cheng = cv2.inRange(hsv, cheng1, cheng2)

huang1 = np.array([26, 43, 50])
huang2 = np.array([34, 255, 255])
huang = cv2.inRange(hsv, huang1, huang2)
# join my masks
kernel = np.ones((2,2),np.uint8)
cv2.imshow('red1',red)

red = cv2.morphologyEx(red, cv2.MORPH_OPEN, kernel)
cheng = cv2.morphologyEx(cheng, cv2.MORPH_OPEN, kernel)
huang = cv2.morphologyEx(huang, cv2.MORPH_OPEN, kernel)



cv2.imshow('src',img)
cv2.imshow('red',red)
cv2.imshow('cheng',cheng)
cv2.imshow('huang',huang)

# cv2.waitKey()
while(1):
    # cv2.imshow('newimg', newimg)
    if cv2.waitKey(1) == ord('q'):
        break
