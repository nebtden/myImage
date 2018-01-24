#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import numpy as np

x = (1,1,1)
y = (2,2,2)
var = np.var([x,y])
x = (1,1,1)
y = (1,2,1)
var = np.var([x,y])
min = np.argmin([1,5,-1,4],axis=0)
print(min)