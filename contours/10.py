import cv2
import numpy as np

def get_hsv_hist_feature(image_name):
    hist_feature = []
    img = cv2.imread(image_name)
    img = cv2.resize(img, (256, 256))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hist_h = cv2.calcHist([hsv], [0], None, [180], [0, 180])
    hist_h = cv2.normalize(hist_h, hist_h)
    hist_feature[0:180] = hist_h[:, 0]

    hist_s = cv2.calcHist([hsv], [1], None, [256], [0, 256])
    hist_s = cv2.normalize(hist_s, hist_s)
    hist_feature[180:436] = hist_s[:, 0]

    hist_v = cv2.calcHist([hsv], [2], None, [256], [0, 256])
    hist_v = cv2.normalize(hist_v, hist_v)
    hist_feature[436:692] = hist_v[:, 0]

    return list(np.array(hist_feature).ravel())

result= get_hsv_hist_feature("../sources/wu.jpg")
print(result)