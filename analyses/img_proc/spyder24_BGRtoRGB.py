#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:05:00 2020
[REF](/watch?v=E_XZHQkQBBU&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=25)actor by
@author: bragatte
"""

from skimage import io
img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/pymol/A0201_0002.png')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/bragatte.jpeg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/mas.jpeg')

###Do something to the image
###e.g. let us apply gaussian smoothing
from skimage import filters
gaussian_img = filters.gaussian(img, sigma=1) #strong blur when <3

##Save image using skimage
##Best way as it converts float images to RGB and scales them accordingly
io.imsave("data/images/saved_using_skimage.jpg", gaussian_img)

###File autoamtically gets saved to right format based on the extension.
###We can define the exact library to be used to save files but defaults work ok.
###For tiff extensions it uses tifffile library to save images, in the background.
###First, image needs to be converted to 8 bit unsigned integer.
##############################################################################
#save image using opencv
import cv2
cv2.imwrite("data/images/saved_using_opencv.jpg", gaussian_img)

###Will succeed writing an image but rounds off flaot
###final image may not look good if saving float 
##so first convert float to 8 bit
from skimage import img_as_ubyte
gaussian_img_8bit = img_as_ubyte(gaussian_img)
cv2.imwrite("data/images/saved_using_opencvBGR.jpg", gaussian_img_8bit)

###This saves fine and the image should be fine but ...
###The colors may be weird, if you are saving color images.
###This is because opencv uses BGR instead of RGB.
###If scolors are important then try working fully within opencv,
###This saves fine and the image should be fine but ...
###The colors may be weird, if you are saving color images.
###This is because opencv uses BGR instead of RGB.
###If scolors are important then try working fully within opencv, 
###including reading and writing images.
###Or, convert images from BGR to RGB when necessary.

gaussian_img_8bit_RGB = cv2.cvtColor(gaussian_img_8bit, cv2.COLOR_BGR2RGB)
cv2.imwrite("data/images/saved_using_opencv3.jpg", gaussian_img_8bit_RGB) 
###including reading and writing images.
###Or, convert images from BGR to RGB when necessary.

gaussian_img_8bit_RGB = cv2.cvtColor(gaussian_img_8bit, cv2.COLOR_BGR2RGB)
cv2.imwrite("data/images/saved_using_opencvRGB.jpg", gaussian_img_8bit_RGB)
