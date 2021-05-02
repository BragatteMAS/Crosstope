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
#plt.imshow(img)

#Plot images variations with matplotlib
###Colormaps...  https://matplotlib.org/tutorials/colors/colormaps.html
plt.imshow(img, cmap="hot")
#Not going to do anything as the input image is RGB

img_gray = io.imread("/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg", as_gray=True)
plt.imshow(img_gray, cmap="hot")
plt.imshow(img_gray, cmap="jet") #att neutral areas


#Multiple plots using pyplot
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img_gray, cmap='hot')
ax1.title.set_text('1st')

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_gray, cmap='jet')
ax2.title.set_text('2nd')

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img_gray, cmap='gray')
ax3.title.set_text('3rd')

ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_gray, cmap='nipy_spectral')
ax4.title.set_text('4th')
plt.show()

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
plt.imshow(img2, cmap="bwr") #bwr,RdBu,coolwarm,seismic
###WHY CAN APPLY COLOR MAPS INTO FIGS WITH NO 0 FLAG?

##Histogram of RGB
plt.hist(eletro_img.flat, bins=100, range=(0,255))


import numpy as np
img = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg',0)
#DFT=Discrete Fourier Transform
dft = cv2.dft(np.float32(img2), flags=cv2.DFT_COMPLEX_OUTPUT)

#Shift DFT. First check the output without the shift
#Without shifting the data would be centered around origin at the top left
#Shifting it moves the origin to the center of the image. 
dft_shift = np.fft.fftshift(dft)

#Calculate magnitude spectrum from the DFT (Real part and imaginary part)
#Added 1 as we may see 0 values and log of 0 is indeterminate
magnitude_spectrum = 20 * np.log((cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))+1)

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img)
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(magnitude_spectrum)
ax2.title.set_text('FFT of image')
plt.show()


