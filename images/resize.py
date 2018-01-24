#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from PIL import  Image

def resize(img,maxwidth=1000, maxheight=1000):
    """
    基于最大宽高按比例重设图片大小，
    注意：这可能影响检测算法的结果

    如果没有变化返回 0
    原宽度大于 maxwidth 返回 1
    原高度大于 maxheight 返回 2
    原宽高大于 maxwidth, maxheight 返回 3

    maxwidth - 图片最大宽度
    maxheight - 图片最大高度
    传递参数时都可以设置为 False 来忽略
    """
    width,height = img.size
    # 存储返回值

    if maxwidth:
        if width > maxwidth:
            wpercent = (maxwidth / width)
            hsize = int((height * wpercent))
            fname = img.filename
            # Image.LANCZOS 是重采样滤波器，用于抗锯齿
            img = img.resize((maxwidth, hsize), Image.LANCZOS)

    if maxheight:
        if height > maxheight:
            hpercent = (maxheight / float(height))
            wsize = int((float(width) * float(hpercent)))
            fname = img.filename
            img = img.resize((wsize, maxheight), Image.LANCZOS)

    return img