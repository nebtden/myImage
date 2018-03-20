# encoding: utf-8

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
import random
import cv2
import scipy.misc
import scipy.signal
import scipy.ndimage



def convert_2d(r):
    n = 3
    # 3*3 滤波器, 每个系数都是 1/9
    window = np.ones((n, n)) / n ** 2
    # 使用滤波器卷积图像
    # mode = same 表示输出尺寸等于输入尺寸
    # boundary 表示采用对称边界条件处理图像边缘
    s = scipy.signal.convolve2d(r, window, mode='same', boundary='symm')
    return s.astype(np.uint8)



def add_salt_noise(img):
    rows, cols, dims = img.shape
    R = np.mat(img[:, :, 0])
    G = np.mat(img[:, :, 1])
    B = np.mat(img[:, :, 2])

    Grey_sp = R * 0.299 + G * 0.587 + B * 0.114

    snr = 0.9


    noise_num = int((1 - snr) * rows * cols)
    print(noise_num)

    for i in range(noise_num):
        rand_x = random.randint(0, rows - 1)
        rand_y = random.randint(0, cols - 1)
        if random.randint(0, 1) == 0:
            Grey_sp[rand_x, rand_y] = 0
        else:
            Grey_sp[rand_x, rand_y] = 255


    # 中值滤波
    Grey_sp_mf = scipy.ndimage.median_filter(Grey_sp, (8, 8))



    plt.title('Grey salt and pepper noise (medium)')
    plt.imshow(Grey_sp_mf, cmap='gray')
    plt.imsave('result.jpg',Grey_sp_mf)
    plt.show()

    # cv2.imshow("Result", Grey_sp_mf)
    # # cv2.imwrite("coutours.jpg", dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def main():
    img = np.array(Image.open("../sources/contours_wu.jpg"))
    add_salt_noise(img)


if __name__ == '__main__':
    main()