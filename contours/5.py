import cv2
import numpy as np
import matplotlib.pyplot as plt

# 使用2g-r-b分离土壤与背景

src = img = cv2.imread("../sources/wu.jpg")
cv2.imshow('src', src)

# 转换为浮点数进行计算
fsrc = np.array(src, dtype=np.float32) / 255.0
(b, g, r) = cv2.split(fsrc)
gray = 2 * g - b - r

# 求取最大值和最小值
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

# 计算直方图
hist = cv2.calcHist([gray], [0], None, [256], [minVal, maxVal])
plt.plot(hist)
plt.show()



gray_u8 = np.array((gray - minVal) / (maxVal - minVal) * 255, dtype=np.uint8)
(thresh, bin_img) = cv2.threshold(gray_u8, -1.0, 255, cv2.THRESH_OTSU)
cv2.imshow('bin_img', bin_img)

cv2.waitKey()