
import cv2
import random
import numpy as np
from core.simple_color import getcolorindex

image = cv2.imread("sources/color.jpeg")
# cv2.imshow("Source", image)

# 灰度化，滤波，Canny边缘检测
imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
blurred = cv2.GaussianBlur(imgray, (5, 5), 2)

edges = cv2.Canny(blurred, 80, 150)

edges, contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
black = np.ones(image.shape)
black[:] = [255,255,255]
# empty_img1 =cv2.drawContours(black,contours,-1,(0,255,0),1)

for x in range(len(contours)):



    #根据不同的类型，选择不同的颜色
    black_img = cv2.drawContours(black, contours, x, (0, 0, 0), 1)

    # temp = np.ones(image.shape)
    # temp[:] = [255, 255, 255]
    # temp_img = cv2.drawContours(temp, contours, x, (0, 0, 0), 1)
    # cv2.imwrite('./result/'+str(x)+ '.jpg', temp_img)

    M = cv2.moments(contours[x])
    if(M['m00']==0.0):

        continue
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    # print(M)
    # print(cx,cy)


    #根据中心点的坐标，获取颜色
    color = hsv_img[cy,cx]

    # print(index)
    index = getcolorindex(color)

    with open("output.txt", 'a') as f:
        f.write(str(cx)+' ' + str(cy) +' '+ "\n")
        f.write(str(x)+ "\n")
        f.write(str(index) + "\n")
        f.write(str(color) + "\n")
        f.write("\n")

    # 计算轮廓所包含的面积
    area = cv2.contourArea(contours[x])
    if area < 400:
        continue
    # print(area)
    # cv2.circle(image, (cx, cy), 7, (0, 255, 0), -1)
    cv2.putText(black, str(index), (cx, cy),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)








cv2.imwrite('./result/color.jpg', black_img)



while(1):
    # cv2.imshow('img',img)
    # cv2.imshow('imgray',imgray)
    # cv2.imshow('image',image)
    # cv2.imshow('imag',imag)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()




