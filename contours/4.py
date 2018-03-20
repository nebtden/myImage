# -*- coding: utf-8 -*-
import cv2
import numpy as np

# filter2D

img = cv2.imread("../sources/wu.jpg")
cv2.imshow('src', img)

kernel = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])

dst = cv2.filter2D(img, -1, kernel)
cv2.imshow('dst', dst)

cv2.waitKey()