#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 2021
[REF]()actor by
@author: bragatte
# sections
## tips
### comments
"""

#Import img
from matplotlib import pyplot as plt
from skimage import io

#Plot images
img = io.imread("data/images/grasp/zikv/ALPVYLMTL_5K.jpg") #float conversplt.imshow(img) #matplotlib
### skimage
io.imshow(img) 
### matplot
plt.imshow(img)


#Rescale
from skimage.transform import rescale
##Always Rescale, Not resize##
###gaussian smoothing can performed to avoid anti aliasing artifacts.
img_rescaled = rescale(img, 1.0 / 4.0, anti_aliasing=False)
###Check rescales image size in variable explorer
io.imshow(img_rescaled) 

#Contrast img 
###A quick look at a few skimage functions
from skimage.filters import gaussian, sobel
### gaussian
gaussian_using_skimage = gaussian(img, sigma=1, mode='constant', cval=0.0)
plt.imshow(gaussian_using_skimage)
### sobel
img_gray = io.imread("data/images/grasp/zikv/ALPVYLMTL_5K.jpg", as_gray=True)
sobel_img = sobel(img_gray)  #Works only on 2D (gray) images
plt.imshow(sobel_img, cmap='gray')


#Histogram
import cv2
img2 = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg')#,0)
plt.imshow(img2)
eletro_img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) #bgr2rgb
plt.imshow(eletro_img)

from skimage import img_as_ubyte
eletro_img_8bit = img_as_ubyte(eletro_img) #floatto8bit
cv2.imwrite("/home/bragatte/Documentos/GitHub/Crosstope/data/images/eletro_img_opencvBGR.jpg", eletro_img_8bit) #save output
plt.imshow(eletro_img, cmap="bwr") #bwr,RdBu,coolwarm,seismic
###WHY CAN APPLY COLOR MAPS INTO FIGS WITH NO 0 FLAG?

##Histogram of RGB
plt.hist(eletro_img.flat, bins=100, range=(0,255))

#