import numpy as np
import cv2
import os

img = cv2.imread("../sources/wu.jpg")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.namedWindow("result",0)
cv2.imshow("result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0,len(contours)):
  x, y, w, h = cv2.boundingRect(contours[i])
  cv2.rectangle(image, (x,y), (x+w,y+h), (153,153,0), 5)

newimage=image[y+2:y+h-2,x+2:x+w-2]
nrootdir=("../result/")
if not os.path.isdir(nrootdir):
  os.makedirs(nrootdir)
cv2.imwrite( nrootdir+str(i)+".jpg",newimage)
print(i)