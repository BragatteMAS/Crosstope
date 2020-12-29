#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:03:59 2020
REF.:watch?v=67ylv7ldPj0&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=27 #plots
@author: bragatte
"""
##########
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/pymol/A0201_0002.png')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/bragatte.jpeg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/mas.jpeg')
##########
from skimage import io
img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg')
plt.imshow(img)

from matplotlib import pyplot as plt
x=[1,2,3,4,5,6]
y=[1,4,9,16,25,36]
plt.plot(x,y)

import numpy as np
#transform ino array
a = np.array(x)
b = np.array(y)
plt.plot(a,b)
#plt.plot(a, b, 'g^')  #Blue dots. Also try: 'r--' 'g^' 'bs'
#plt.axis([0, 6, 0, 50]) #Define range for x and y axes [xmin, xmax, ymin, ymax] 

import cv2
img2 = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg')#,0)
plt.imshow(img2)
eletro_img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) #bgr2rgb
plt.imshow(eletro_img)

from skimage import img_as_ubyte
eletro_img_8bit = img_as_ubyte(eletro_img) #floatto8bit
cv2.imwrite("/home/bragatte/Documentos/GitHub/Crosstope/data/images/eletro_img_opencvBGR.jpg", eletro_img_8bit) #save output

plt.imshow(eletro_img, cmap="bwr") #bwr,RdBu,coolwarm,seismic
WHY CAN APPLY COLOR MAPS INTO FIGS WITH NO 0 FLAG?

#Histogram of RGB
plt.hist(gray_img.flat, bins=100, range=(0,255))
