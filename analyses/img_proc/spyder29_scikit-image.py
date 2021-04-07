#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:46:35 2021
[REF](watch?v=mQkcf8kgit8&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=30)actor by
@author: bragatte
"""
from matplotlib import pyplot as plt
from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean

#img = io.imread("/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg")
#io.imshow(img) #skimage
img = io.imread("/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg", as_gray=True) #float conversion
plt.imshow(img) #matplotlib


