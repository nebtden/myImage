import numpy as np
from pandas import *
import cv2
import os, sys
from core.simple_color import getcolorindex

# img = cv2.imread('red.jpg')
img = cv2.imread('sources/mickey2.jpg')
rgb_img = img[..., ::-1]
print(type(img))
print(img.shape)
# size = img.shape
# a = img.reshape(size[0]*size[1],3)
# print(a.shape)
# # 对python进行分块处理
# b = DataFrame(a).drop_duplicates().values
# print(type(b))
# print(b.shape)
# print(b)
# # print(b)


imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
ret,thresh = cv2.threshold(imgray,127,255,0)
image ,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.contourArea
#绘制独立轮廓，如第四个轮廓
#imag = cv2.drawContour(img,contours,-1,(0,255,0),3)
#但是大多数时候，下面方法更有用


black = np.ones(img.shape)
print(type(contours))
print(type(contours[0]))
print(len(contours))
black = np.ones(img.shape)
black[:] = [255,255,255]
white = np.ones(img.shape)
white[:] = [255,255,255]
for x in range(len(contours)):



    #根据不同的类型，选择不同的颜色

    M = cv2.moments(contours[x])
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    # print(M)
    # print(cx,cy)


    #根据中心点的坐标，获取颜色
    color = hsv_img[cy,cx]
    bgr = img[cy,cx]
    rgb = rgb_img[cy,cx]

    # print(index)
    index = getcolorindex(color)

    with open("output.txt", 'a') as f:
        f.write(str(cx)+' ' + str(cy) +' '+ "\n")
        f.write(str(x)+ "\n")
        f.write(str(index) + "\n")
        f.write(str(rgb) + "\n")
        f.write(str(bgr) + "\n")
        f.write(str(color) + "\n")
        f.write("\n")

    # 计算轮廓所包含的面积
    area = cv2.contourArea(contours[x])
    if area < 400:
        continue
    # print(area)
    # cv2.circle(image, (cx, cy), 7, (0, 255, 0), -1)
    cv2.putText(black, str(index), (cx, cy),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(white, str(x), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    black_img = cv2.drawContours(black, contours, x, (0, 0, 0), 1)
    white_img = cv2.drawContours(white, contours, x, (0, 0, 0), 1)





cv2.imwrite('./result/black.jpg', black_img)
cv2.imwrite('./result/white.jpg', white_img)

print(len(contours))
cnt = contours[1]
area = cv2.contourArea(cnt)#计算面积
print(area)

while(1):
    # cv2.imshow('img',img)
    # cv2.imshow('imgray',imgray)
    # cv2.imshow('image',image)
    # cv2.imshow('imag',imag)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
cv2.imshow('src',thresh)
# cv2.imwrite('img_cv2.jpg', imggray)
cv2.startWindowThread() #加在这个位置

cv2.imshow('src',img)

cv2.waitKey()
cv2.destroyAllWindows()