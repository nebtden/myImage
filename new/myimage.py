import numpy as np
import matplotlib.pylab as plt
from scipy.signal import convolve2d
from scipy.ndimage.interpolation import zoom

im = plt.imread("man.jpg") # 加载当前文件夹中名为BTD.jpg的图片

def plti(im, **kwargs):
    """
    画图的辅助函数
    """
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('off') # 去掉坐标轴
    plt.show() # 弹窗显示图像



im_small = zoom(im, (0.2,0.2,1))
im = plt.imread("BTD.jpg") # 加载当前文件夹中名为BTD.jpg的图片
one= im[100:200,100:300,:]
plt.imshow(im, interpolation="none")
print(im.shape)
print(one.shape)
# print(im)
n=100
sobel_x = np.c_[
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
]

sobel_y = np.c_[
    [1,2,1],
    [0,0,0],
    [-1,-2,-1]
]
# 或者使用sobel_y = sobel_x.transpose()

ims = []
for d in range(3):
    sx = convolve2d(im_small[:,:,d], sobel_x, mode="same", boundary="symm")
    sy = convolve2d(im_small[:,:,d], sobel_y, mode="same", boundary="symm")
    ims.append(np.sqrt(sx*sx + sy*sy)) # 平方和再开根号，叠加两次处理效果

im_conv = np.stack(ims, axis=2).astype("uint8")

from sklearn.cluster import KMeans

h,w = im_small.shape[:2]
# 获取图像的高和宽
im_small_long = im_small.reshape((h * w, 3))
# 将图像转化为 RGB三值表示的三维空间坐标点 的列表
im_small_wide = im_small_long.reshape((h,w,3))
# 可以将im_small_long恢复为原尺寸

km = KMeans(n_clusters=3)
# 分3个聚类
km.fit(im_small_long)
# 对所有RGB三维空间点分类，每个点获得一个分类标签

cc = km.cluster_centers_.astype(np.uint8)
# 得到每个聚类的中心点坐标，并保证在np.uint8范围内
out = np.asarray([cc[i] for i in km.labels_]).reshape((h,w,3))
# 以每一类的中心点坐标所映射的RGB色彩 替代该类中所有点的色彩，并转换为原始尺寸
# km.labels_是所有空间点的标签列表，列表中元素的值（即标签）为0,1或2，表示3个不同类

# plti(out)

from skimage import measure

seg = np.asarray([(1 if i == 1 else 0)
                  for i in km.labels_]).reshape((h,w))
# 由聚类结果得到0,1二值单通道图像

contours = measure.find_contours(seg, 0.5, fully_connected="high")
# 找到轮廓，返回每个连续轮廓的列表，每个连续轮廓是一组坐标点

simplified_contours = [measure.approximate_polygon(c, tolerance=5) for c in contours]
# 简化轮廓，近似为多边形，tolerance决定精度

plt.figure(figsize=(5,10))

for n, contour in enumerate(simplified_contours):
    plt.plot(contour[:, 1], contour[:, 0], linewidth=2)
    # 连点成线，循环画出每个轮廓

plt.ylim(h,0) # 设置y轴显示范围
plt.axes().set_aspect('equal') # 设置x,y轴对数据的比例相同
plt.show()

from matplotlib.patches import PathPatch
from matplotlib.path import Path

# 先翻转轮廓的坐标（交换x,y的位置），使其和matplotlib一致
paths = [[[v[1], v[0]] for v in vs] for vs in simplified_contours]

def get_path(vs):
    codes = [Path.MOVETO] + [Path.LINETO] * (len(vs)-2) + [Path.CLOSEPOLY]
    return PathPatch(Path(vs, codes))
    # 返回当前轮廓绕出的图块补丁对象
    # [Path.MOVETO] + [Path.LINETO] + [Path.CLOSEPOLY] = [1, 2, 79]
    # [Path.LINETO] *3 = [2, 2, 2]

plt.figure(figsize=(5,10))

ax = plt.gca()
# gca获取当前坐标轴

for n, path in enumerate(paths):
    ax.add_patch(get_path(path))

plt.ylim(h,0)
plt.xlim(0,w)

plt.axes().set_aspect('equal')


