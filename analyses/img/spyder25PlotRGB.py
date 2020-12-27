#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:58:33 2020
REF.:playlist?list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG
@author: bragatte

display of images
pyplot (edit mode) and opencv
skimage can also be used.. io.imshow
"""
from skimage import io
img = io.imread('/home/bragatte/Documentos/GitHub//Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/pymol/A0201_0002.png')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/bragatte.jpeg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/mas.jpeg')
io.imshow(img)

#MATPLOTLIB.PYPLOT
import matplotlib.pyplot as plt
plt.imshow(img)  

#Colormaps...  https://matplotlib.org/tutorials/colors/colormaps.html
plt.imshow(img, cmap="hot")
#Not going to do anything as the input image is RGB

img_gray = io.imread("Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg", as_gray=True)
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



############################################
#Using opencv

import cv2

gray_img = cv2.imread("Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg", 0)
color_img = cv2.imread("Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg", 1)


# Use the function cv2.imshow() to display an image in a window. 
# First argument is the window name which is a string. second argument is our image. 

cv2.imshow("pic from skimage import", img)  #Shows weird colors as R and B channels are swapped
cv2.imshow("color pic from opencv", color_img)
cv2.imshow("gray pic from opencv", gray_img)

# Maintain output window until 
# user presses a key or 1000 ms (1s)
cv2.waitKey(0)          

#destroys all windows created
cv2.destroyAllWindows() 


