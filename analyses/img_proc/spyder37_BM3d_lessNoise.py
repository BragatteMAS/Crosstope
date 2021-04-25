#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:59:53 2021
[REF](watch?v=HAOeYCGFGaE&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=38)actor by
@author: bragatte

http://www.cs.tut.fi/~foi/papers/ICIP2019_Ymir.pdf
"""
from skimage import io, img_as_float
import bm3d
import cv2

noisy_img = img_as_float(io.imread("/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K_noise.png", as_gray=False))

BM3D_denoised_image = bm3d.bm3d(noisy_img, sigma_psd=0.05, stage_arg=bm3d.BM3DStages.HARD_THRESHOLDING)

"""
Best Denoising pack:
    Could use in color img
    0.5 sigma great results
    
Requeriments OpenBlas lib:
    conda install -c jasonb857 libopenblas
    
bm3d library is not well documented yet, but looking into source code....
sigma_psd - noise standard deviation
stage_arg: Determines whether to perform hard-thresholding or Wiener filtering.
stage_arg = BM3DStages.HARD_THRESHOLDING or BM3DStages.ALL_STAGES (slow but powerful)
All stages performs both hard thresholding and Wiener filtering. 
"""

cv2.imshow("Original", noisy_img)
cv2.imshow("Denoised", BM3D_denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
