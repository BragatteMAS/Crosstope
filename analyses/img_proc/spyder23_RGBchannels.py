#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:27:58 2020
[REF](/watch?v=YuHaD-yG_D4&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=24)actor by
@author: bragatte
"""
from skimage import io
img = io.imread('data/images/grasp/zikv/ALPVYLMTL_5K.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/pymol/A0201_0002.png')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/mas.jpeg') #works on photos

img1=img[:, :, :]
print(img1.shape)

###Next, let us extract each channel image.
img2=img1[0,:,:]  #First channel, Red
img3=img1[1,:,:] #Second channel, Green
img4=img1[2,:,:] #Third channel, Blue DAPI

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img2, cmap='hot')
ax1.title.set_text('1st channel')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img3, cmap='hot')
ax2.title.set_text('2nd channel')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img4, cmap='hot')
ax3.title.set_text('3rd channel')
plt.show()