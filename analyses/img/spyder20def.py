#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:54:49 2020
@author: bragatte
"""
from skimage import io, filters
from matplotlib import pyplot as plt

def gaussian_of_img(img, sigma=1):
    gaussian_img = filters.gaussian(img, sigma)
    return(gaussian_img)

my_image = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/pymol/A0201_0002.png')
filtered = gaussian_of_img(my_image, 2)

a = plt.imshow(my_image)
b = plt.imshow(filtered)

