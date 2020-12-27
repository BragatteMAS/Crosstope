!pip install opencv-python

import numpy as np
import cv2

img = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/*.jpg')

img1 = cv2.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')

img1r = img1.reshape((-1,3))

#convert into float32
img1r = np.float32(img1r)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0) 

#ClustersMas
k=4

attempts=10

ret,label,center=cv2.kmeans(img1r,None, criteria, attempts, cv2.KMEANS_PP_CENTERS)