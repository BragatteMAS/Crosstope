# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:00 2020
Spyder Editor
This is a temporary script file.
REF.:/playlist?list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG #51
@author: bragatte
"""
#!pip install scikit-image
from skimage import io, filters
from matplotlib import pyplot as plt

img = io.imread('A0201_0001_V5.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/bragatte.jpeg')

gaussian_img = filters.gaussian(img, sigma=2)

plt.show(gaussian_img)
plt.show(img)