#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:54:31 2021
[REF](watch?v=_Ybek8eMGKU&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=37)actor by
@author: bragatte

Works well for random gaussian noise but not as good for salt and pepper
https://hal.archives-ouvertes.fr/hal-00437581/document
"""
import cv2
from skimage import io, img_as_float
from skimage.restoration import denoise_tv_chambolle
from matplotlib import pyplot as plt

img = img_as_float(io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K_noise.png', as_gray=True))
io.imshow(img)
plt.hist(img.flat, bins=100, range=(0,1))  #.flat returns the flattened numpy array (1D)

denoise_img = denoise_tv_chambolle(img, weight=0.1, eps=0.0002, n_iter_max=200, multichannel=False)

"""
denoise_tv_chambolle(image, weight=0.1, eps=0.0002, n_iter_max=200, multichannel=False)
weight: The greater weight, the more denoising (at the expense of fidelity to input).
eps: Relative difference of the value of the cost function that determines the stop criterion. 
n_iter_max: Max number of iterations used for optimization
"""

plt.hist(denoise_img.flat, bins=100, range=(0,1))  #.flat returns the flattened numpy array (1D)

cv2.imshow("Original", img)
cv2.imshow("TV Filtered", denoise_img)
cv2.waitKey(0)          
cv2.destroyAllWindows() 