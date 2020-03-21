# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:28:25 2020

@author: MarkkuLeino
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

np.random.seed(1234)
x_values = [4, 8, 16, 32, 4, 8, 16, 32, 4, 8, 16, 32, 4, 8, 16, 32]
y_values = [64, 64, 64, 64, 256, 256, 256, 256, 512, 512, 512, 512, 1024, 1024, 1024, 1024]
z_values = np.random.rand(16)

x_labels, x_pos = np.unique(x_values, return_inverse=True)
y_labels, y_pos = np.unique(y_values, return_inverse=True)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(x_pos-0.5, y_pos-0.5, np.zeros_like(z_values), 1, 1, z_values)
ax.set_xticks(np.arange(len(x_labels)))
ax.set_xticklabels(x_labels)
ax.set_yticks(np.arange(len(y_labels)))
ax.set_yticklabels(y_labels)
plt.show()