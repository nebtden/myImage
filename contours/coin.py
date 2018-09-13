import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('water_coins.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

cv.imshow('thresh',thresh)
# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
cv.imshow('opening',opening)

# sure background area
sure_bg = cv.dilate(opening,kernel,iterations=3)
cv.imshow('bg',sure_bg)


# Finding sure foreground area
dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
cv.imshow('dist_transform',dist_transform)

ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
cv.imshow('fg',sure_fg)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)
print(unknown)

# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)


print(markers.shape)
# for x in markers:
#     print(x)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
print(markers[unknown==255])
markers[unknown==255] = 0
new_img =    np.zeros((312,252,3), np.uint8)
new_img[:] = (255,255,255)

cv.imshow('img1',img)
print(markers)
markers = cv.watershed(img,markers)
markers2 = cv.watershed(new_img,markers)
# print(markers)
img[markers == -1] = [255,0,0]
new_img[markers == -1] = [255,0,0]
cv.imshow('img',img)
cv.imshow('new_img',new_img)
# cv2.waitKey()
while(1):
    # cv2.imshow('newimg', newimg)
    if cv.waitKey(1) == ord('q'):
        break