# -*- coding: utf-8 -*-
"""
图像分水岭分割图像
分水岭算法可以参考：http://baike.baidu.com/item/%E5%88%86%E6%B0%B4%E5%B2%AD%E7%AE%97%E6%B3%95
"""


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../sources/mickey2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# 降噪处理
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# 确定背景
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# 查找前景
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# 查找未确定区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# 标注
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1

# 将未确定区域置为0
markers[unknown==255] = 0

# 执行分水岭
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

cv2.imshow("img2",img)

cv2.waitKey()
cv2.destroyAllWindows()