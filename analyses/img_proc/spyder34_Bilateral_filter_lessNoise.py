#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:34:50 2021
[REF](watch?v=CQPZhAVHsXg&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=36)actor by
@author: bragatte

[cv2.cv2.bilateralFilter](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html)
[skimage bilateral](https://scikit-image.org/docs/dev/auto_examples/filters/plot_denoise.html)
h
ttps://people.csail.mit.edu/sparis/bf_course/course_notes.pdf

Bilateral is slow and not very efficient at salt and pepper
"""

import cv2

img_gaussian_noise = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K_noise.png', 0)
img_salt_pepper_noise = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K_noise.png', 0)

img = img_gaussian_noise

bilateral_using_cv2 = cv2.bilateralFilter(img, 5, 20, 100, borderType=cv2.BORDER_CONSTANT)

###d - diameter of each pixel neighborhood used during filtering
###sigmaCOlor - Sigma of grey/color space. 
###sigmaSpace - Large value means farther pixels influence each other (as long as the colors are close enough)

cv2.imshow("Original", img)
cv2.imshow("cv2 bilateral", bilateral_using_cv2)
cv2.waitKey(0)          
cv2.destroyAllWindows() 

'''
## Slower than OPEN-CV
from skimage.restoration import denoise_bilateral
bilateral_using_skimage = denoise_bilateral(img, sigma_color=0.05, sigma_spatial=15,multichannel=False)

##sigma_color = float - Sigma for grey or color value. 
##For large sigma_color values the filter becomes closer to gaussian blur.
##sigma_spatial: float. Standard ev. for range distance. Increasing this smooths larger features.

cv2.imshow("Original", img)
cv2.imshow("Using skimage bilateral", bilateral_using_skimage)
cv2.waitKey(0)          
cv2.destroyAllWindows() 
'''