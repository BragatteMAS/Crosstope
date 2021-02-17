#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:31:55 2020
REFs.:
watch?v=Z90KEqJoC3w&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=28
watch?v=j6GNtqrwcNE&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=29
@author: bragatte

#The glob module finds all the path names 
#matching a specified pattern according to the rules used by the Unix shell
#The glob.glob returns the list of files with their full path 
"""
##########
img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/zikv/ALPVYLMTL_5K.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/grasp/A0201_0001_V5.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/pymol/A0201_0002.png')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/chimeraX/YLKPTTFML_A0201.jpg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/bragatte.jpeg')
#img = io.imread('/home/bragatte/Documentos/GitHub/Crosstope/data/images/mas.jpeg')
##########

#import the library opencv
import cv2, glob, os 

file_list = glob.glob('data/images/grasp/zikv/*.*') #Returns a list of file names
print(file_list)  #Prints the list containing file names

#Now let us load each file at a time...
my_list=[]  #Empty list to store images from the folder.
path = "data/images/grasp/zikv/*.*"
for file in glob.glob(path):   #Iterate through each file in the list using for
    print(file)     #just stop here to see all file names printed
    imgs= cv2.imread(file)  #now, we can read each file since we have the full path
    my_list.append(imgs)  #Create a list of images (not just file names but full images)
    
#View images from the stored list
from matplotlib import pyplot as plt
plt.imshow(my_list[2])  #View the 3rd image in the list.

########################################################################
#for file in path:
#    i = 0
#    for filename in os.listdir(path):
#        os.rename(os.path.join(path,filename), os.path.join(path,'captured'+str(i)+'.jpg'))    i = i +1

#name for file
#for file in my_list:
#    img_name = file
#    if ".jpg" in img_name:       
#        img_name = img_name.split('zikv/',1)[1]
#        with open(img_name, "wb") as img_name:
#            img_name.write(img_name)
########################################################################


img_name = 1  #Start an iterator for image number. VERIFICAR SCRIPT NOME
#This number can be later added to output image file names.

#let us look at each file
#    cv2.imshow('Original Image', a)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    
#process each image - change color from BGR to RGB.
    trgb = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)  #Change color space from BGR to RGB
    cv2.imwrite("data/images/grasp/zikv/"+str(img_name)+".jpg", trgb)
    img_name +=1 #FALTANDO ITERAÇÃO FUNCIONAR
    cv2.imshow('zikv', trgb)
    cv2.waitKey(1000)  #Display each image for 1 second
    cv2.destroyAllWindows()

#######################################################################################