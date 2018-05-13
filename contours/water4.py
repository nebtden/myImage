import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread("../sources/wu.jpg")
cv2.imshow('img',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations= 2)
sure_bg = cv2.dilate(opening, kernel,iterations=3)
dist_transform =cv2.distanceTransform(opening, 1, 5)
ret,sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)


ret,markers1 = cv2.connectedComponents(sure_fg)
markers = markers1 + 1
markers[unknown == 255] = 0

# blank_image = np.zeros((200,200,3), np.uint8)
# markers4 = cv2.watershed(blank_image, markers)
# cv2.imshow('blank_image',blank_image)

markers3 = cv2.watershed(img, markers)
# cv2.imshow('markers3',markers3)
img[markers3 == -1] = [255,0,0]


# cv2.imshow('thresh',thresh)
# cv2.imshow('ret',ret)
cv2.imshow('img',img)
cv2.waitKey(0)