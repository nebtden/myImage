#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from core.simple_color import  getcolorindex
import numpy as np
import cv2

img = np.zeros((300,512,3),np.uint8)

img[:] = [255,255,255]
cv2.imshow('src',img)
while(1):
    # cv2.imshow('img',img)
    # cv2.imshow('imgray',imgray)
    # cv2.imshow('image',image)
    # cv2.imshow('imag',imag)
    if cv2.waitKey(1) == ord('q'):
        break