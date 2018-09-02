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