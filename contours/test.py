import cv2 as cv
import numpy as np
width = 200
height = 200

image = np.ones((height, width, 3), dtype=np.uint8)
d=np.array((0,255,0))
c = image*d
print(c.shape)
print('--------------')
image[:, :] = (0, 255, 0)
# print(image)
print(image.shape)
#创建显示窗口

win_name = "test"
cv.namedWindow("test",cv.WINDOW_AUTOSIZE)
cv.imshow(win_name, image)

#draw a line

start_point = (10,10)
end_point = (100,100)
#line attribute
color = (0,255,0)
line_width = 4
line_type = 8
cv.line(image, start_point, end_point, color, line_width, line_type)

#画一个矩形，只需定义矩形的左上顶点和右下顶点位置，以及线的颜色和宽度

x = 30
y = 30
rect_start = (x,y)
x1 = 90
y1 = 90
rect_end = (x1,y1)
cv.rectangle(image, rect_start, rect_end, color, 1, 0)

#画一个圆，只需定义圆的中心点坐标和圆的半径，以及线的颜色和宽度

x = 100
y = 100
radius = 60
circle_center = (x,y)
cv.circle(image, circle_center, radius, color)

cv.imshow(win_name, image)
cv.imshow('c', c)

cv.waitKey()