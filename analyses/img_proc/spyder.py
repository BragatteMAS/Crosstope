#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:06:27 2020
[REF](/playlist?list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG)actor by
@author: bragatte
<<<<<<< HEAD
# sections || code
## tips
### comments

##Win10: C:\Users\marce\Documents\GitHub\Crosstope
##PopOS: ~/Documents/GitHub/Crosstope

scikit-image: pip install scikit-image
opencv: pip install opencv-python
"""

#scikit-learn
from skimage import io ##read RGB
#img1 = io.imread('data\images\grasp\A0201_0001_V5.jpg') #win
img1 = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
imgt1= io.imread('/home/bragatte/Documentos/GitHub/html-css/Estudos/html-css/ex000/cross200.png')
img1_noise= io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K_noise.png')
io.imshow(img1_noise)

import cv2 ##read BRG
#img2 = cv2.imread('data\images\grasp\A0201_0001_V5.jpg') #win
img2 = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
imgt2= cv2.imread('/home/bragatte/Documentos/GitHub/html-css/Estudos/html-css/ex000/cross200.png')
img2_noise= cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K_noise.png')

from matplotlib import pyplot as plt
plt.imshow(img2_noise)
