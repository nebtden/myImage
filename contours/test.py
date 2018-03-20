import cv2

img = cv2.imread("../sources/wu.jpg")
win = cv2.namedWindow('test',flags=0)
# win = cv2.namedWindow('test win', flags=1)

cv2.imshow('test', img)

cv2.waitKey(0)