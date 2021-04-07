#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:46:35 2021
[REF](watch?v=mQkcf8kgit8&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=30)actor by
@author: bragatte
"""
from matplotlib import pyplot as plt
from skimage import io
from skimage.transform import rescale, resize, downscale_local_mean

#img = io.imread("/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg")
#io.imshow(img) #skimage
img = io.imread("data/images/grasp/zikv/ALPVYLMTL_5K.jpg") #float conversplt.imshow(img) #matplotlib
io.imshow(img)

#Rescale, resize image by a given factor. While rescaling image
#gaussian smoothing can performed to avoid anti aliasing artifacts.
img_rescaled = rescale(img, 1.0 / 4.0, anti_aliasing=False)  #Check rescales image size in variable explorer

#Resize, resize image to given dimensions (shape)
img_resized = resize(img, (200, 200),               #Check dimensions in variable explorer
                       anti_aliasing=True)

#Downscale, downsample using local mean of elements of each block defined by user
img_downscaled = downscale_local_mean(img, (4, 3))
plt.imshow(img_downscaled)


################################################

#A quick look at a few skimage functions
from skimage.filters import gaussian, sobel
img = io.imread("data/images/grasp/zikv/ALPVYLMTL_5K_noise.png")
plt.imshow(img)
gaussian_using_skimage = gaussian(img, sigma=1, mode='constant', cval=0.0)
#sigma means input = output#
plt.imshow(gaussian_using_skimage)

img_gray = io.imread("data/images/grasp/zikv/ALPVYLMTL_5K.jpg", as_gray=True)
sobel_img = sobel(img_gray)  #Works only on 2D (gray) images
plt.imshow(sobel_img, cmap='gray')
