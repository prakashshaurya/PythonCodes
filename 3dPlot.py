# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 12:55:04 2022

@author: shaurya
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')
x = np.arange(-5,5,.001)
y = np.arange(-5,5,.001)
z=((100*(y-x**2)**2))+(1-x)**2

ax.scatter3D(x,y, z, c=z, cmap='cividis');

plt.show()