#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:06:27 2020

@author: bragatte

#working directory
##Win10: C:\Users\marce\Documents\GitHub\Crosstope
##PopOS: ~/Documents/GitHub/Crosstope

scikit-image: pip install scikit-image
opencv: pip install opencv-python
"""

#scikit-learn
from skimage import io #read RGB
img1 = io.imread('data\images\grasp\A0201_0001_V5.jpg') #win
#img1 = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
#imgt1= io.imread('/home/bragatte/Documentos/GitHub/html-css/Estudos/html-css/ex000/cross200.png')

import cv2 #read BRG
img2 = cv2.imread('data\images\grasp\A0201_0001_V5.jpg')
#img2 = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
#imgt2= cv2.imread('/home/bragatte/Documentos/GitHub/html-css/Estudos/html-css/ex000/cross200.png')

import numpy as np
a=np.ones((5,5))

import pandas as pd
df = pd.read_csv(...)
print(df.head(...))

from matplotlib import pyplot as plt
plt.imshow(img2)
