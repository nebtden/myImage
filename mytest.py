#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from core.simple_color import  getcolorindex
import numpy as np

x = [0,45,100]
index = getcolorindex(x)
print(index)

x = [-1,45,100]
result = x>[0,46,100]
print(result)
