import cv2
import numpy as np


def get_countoures(img):
    x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

    absx = cv2.convertScaleAbs(x)  # 转回uint8
    absy = cv2.convertScaleAbs(y)

    dst = cv2.addWeighted(absx, 1, absy, 1, 0)

    return dst
