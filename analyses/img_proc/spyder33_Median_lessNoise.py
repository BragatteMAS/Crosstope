#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 21:24:18 2021
[REF](watch?v=MTaCVDll9Iw&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=35)actor by
@author: bragatte

cv2.medianBlur - https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
skimage.filters.median - https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.median
See how median is much better at cleaning salt and pepper noise compared to Gaussian
"""
import cv2
from skimage.filters import median

#Needs 8 bit, not float.
img_gaussian_noise = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K_noise.png', 0)
img_salt_pepper_noise = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K_noise.png', 0)

img = img_salt_pepper_noise

median_using_cv2 = cv2.medianBlur(img, 3) #3 kernel size

from skimage.morphology import disk  
###
disc_example =  disk(2)
disc_example
###
#Disk creates a circular structuring element, similar to a mask with specific radius
median_using_skimage = median(img, disk(3), mode='constant', cval=0.0)

cv2.imshow("Original", img)
cv2.imshow("cv2 median", median_using_cv2)
cv2.imshow("Using skimage median", median_using_skimage)

cv2.waitKey(0)          
cv2.destroyAllWindows() 