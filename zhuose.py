import cv2

imgfile = "red.jpg"
img = cv2.imread(imgfile)
h, w, _ = img.shape

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find Contour
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 需要搞一个list给cv2.drawContours()才行！！！！！
c_max = []
max_area = 0
max_cnt = 0
for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    # find max countour
    if (area > max_area):
        if (max_area != 0):
            c_min = []
            c_min.append(max_cnt)
            cv2.drawContours(img, c_min, -1, (0, 0, 0), cv2.FILLED)
        max_area = area
        max_cnt = cnt
    else:
        c_min = []
        c_min.append(cnt)
        cv2.drawContours(img, c_min, -1, (0, 0, 0), cv2.FILLED)

c_max.append(max_cnt)

cv2.drawContours(img, c_max, -1, (255, 255, 255), thickness=-1)

cv2.imwrite("mask.png", img)
cv2.imshow('mask', img)
cv2.waitKey(0)