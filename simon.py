from PIL import Image
from images import resize
import os

image = Image.open('sources/zhanqian.png')
pixels = image.load()
width, height = image.size
print(width)
print(height)

#存储相对应的色彩值
colors = [];

#对于对应的色彩值
r, g, b = 0, 0, 0
for x in range(9):
    if x==0:
        r,g,b = 0,0,0
    else:
        r, g, b = 32 * x - 1, 32 * x - 1, 32 * x - 1
    print(r,g,b)
    colors.append((r,g,b))

print(colors)

#处理逻辑
def getPixels(r,g,b):
    rgb_classifier = r > 95 and \
                     g > 40 and g < 100 and \
                     b > 20 and \
                     max([r, g, b]) - min([r, g, b]) > 15 and \
                     abs(r - g) > 15 and \
                     r > g and \
                     r > b
    return rgb_classifier

new_image = image

new_image_data = new_image.load()

for x in range(width):
    for y in range(height):
        r = pixels[x, y][0]  # red
        g = pixels[x, y][1]  # green
        b = pixels[x, y][2]  # blue
        is_skin = getPixels(r,g,b)
        if is_skin :
            new_image_data[x, y] = 0,0,0
        else:
            new_image_data[x, y] = 255,255,255

# 源文件绝对路径
filePath = os.path.abspath(image.filename)
# 源文件所在目录
fileDirectory = os.path.dirname(filePath) + '/'
print(fileDirectory)
# 源文件的完整文件名
fileFullName = os.path.basename(filePath)
# 分离源文件的完整文件名得到文件名和扩展名
fileName, fileExtName = os.path.splitext(fileFullName)
# 保存图片
print(fileName)
new_image.save('{}{}_{}{}'.format(fileDirectory, fileName, 'new', fileExtName))


# if __name__ == '__main__':
#     print('begin')