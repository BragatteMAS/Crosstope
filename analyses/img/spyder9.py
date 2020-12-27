#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:06:27 2020
!pip install scikit-image
!pip install opencv-python
!pip install tifffile

*If want to use Pillow library = does not import images as numpy array
You can convert using numpy.asarray(img)
@author: bragatte
"""
#scikit-learn
from skimage import io #read RGB
imgsG1 = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
imgsP2 = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/pymol/A0201_0002.png')
imgsCt = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg')
imgst = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/mas.jpeg')
imgt  =  io.imread('/home/bragatte/Documentos/GitHub/html-css/Estudos/html-css/ex000/cross200.png')

import cv2 #read BRG
imgcG1 = cv2.imread_color('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
imgcP2 = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/pymol/A0201_0002.png')
imgcCt = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg')
imgct = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/mas.jpeg')

import numpy as np
a=np.ones((5,5))

import pandas as pd
df = pd.read_csv()
print(df.head())

from matplotlib import pyplot as plt
plt.imshow(img2)

