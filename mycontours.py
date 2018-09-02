import numpy as np
from pandas import *
import cv2

img = cv2.imread('sources/mickey2.jpg')
print(type(img))
newimg = np.ones(img.shape)
size = img.shape


kernel = np.ones((10,10),np.uint8)
erosion = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

a = img.reshape(size[0]*size[1],3)
# print(a.shape)
# # 对python进行分块处理
b = DataFrame(a).drop_duplicates().values
print( type(b))
print(b.shape)

c = erosion.reshape(size[0]*size[1],3)
# print(a.shape)
# # 对python进行分块处理
d = DataFrame(c).drop_duplicates().values
print( type(d))
print(d.shape)
# 11143,
cv2.imshow('src',img)
cv2.imshow('show',erosion)
cv2.waitKey()

while(1):
    # cv2.imshow('newimg', newimg)
    if cv2.waitKey(1) == ord('q'):
        break

# shape = []
# for x in range(size[0]):
#     for y in range(size[1]):
#         a,b,c = newimg[x][y]
#         # a = b = c = 255
#         if
#         newimg[x,y] = [255,255,255]
#
#
#
#
# while(1):
#     cv2.imshow('newimg', newimg)
#     if cv2.waitKey(1) == ord('q'):
#         break

# for x in img:
#     break
#     for y in x:
#        pass


# a = img.reshape(800*733,3)
# print(a.shape)
# # 对python进行分块处理
# b = DataFrame(a).drop_duplicates().values
#
# print( type(b))
# print(b.shape)


imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image ,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#绘制独立轮廓，如第四个轮廓
#imag = cv2.drawContour(img,contours,-1,(0,255,0),3)
#但是大多数时候，下面方法更有用
imag = cv2.drawContours(img,contours,-1,(0,255,0),1)

# while(1):
#     cv2.imshow('img',img)
#     cv2.imshow('imgray',imgray)
#     cv2.imshow('image',image)
#     cv2.imshow('imag',imag)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cv2.destroyAllWindows()
# cv2.imshow('src',thresh)
# # cv2.imwrite('img_cv2.jpg', imggray)
# cv2.startWindowThread() #加在这个位置
#
# # cv2.imshow('src',img)
#
# cv2.waitKey()
# cv2.destroyAllWindows()