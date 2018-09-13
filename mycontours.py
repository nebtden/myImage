import numpy as np
from pandas import *
import cv2

img = cv2.imread('red.jpg')
# print(type(img))
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
ret,thresh = cv2.threshold(imgray,127,255,0)
image ,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.contourArea
#绘制独立轮廓，如第四个轮廓
#imag = cv2.drawContour(img,contours,-1,(0,255,0),3)
#但是大多数时候，下面方法更有用


black = np.ones(img.shape)
imag = cv2.drawContours(black,contours,-1,(0,255,0),1)
#划分颜色区块，从左上角划线起。按颜色，一个个画。如果左上角有一个颜色，则不再区分
#默认所有颜色为黑色，黑色做两次区分


print(len(contours))
cnt = contours[1]
area = cv2.contourArea(cnt)#计算面积
print(area)

while(1):
    # cv2.imshow('img',img)
    # cv2.imshow('imgray',imgray)
    # cv2.imshow('image',image)
    cv2.imshow('imag',imag)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
cv2.imshow('src',thresh)
# cv2.imwrite('img_cv2.jpg', imggray)
cv2.startWindowThread() #加在这个位置

# cv2.imshow('src',img)

cv2.waitKey()
cv2.destroyAllWindows()