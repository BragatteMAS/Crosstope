#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:13:46 2021
[REF](watch?v=j6GNtqrwcNE&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=29&t=14s)actor by
@author: bragatte

scikit-image: pip install scikit-image
opencv: pip install opencv-python
"""
"""
os.listdir:
returns a list containing the names of the entries in the directory given by path
"""
import os 

path = 'data/images/grasp/zikv/'
print(os.listdir(path)) #Similar to glob

for image in os.listdir(path): #iterate through file to perform some action
    print(image)

#############################
"""
#os.walk --     
returns a generator, that creates a tuple of values 
(current_path, directories in current_path, files in current_path).   
Every time the generator is called it will follow each directory recursively 
until no further sub-directories are available from the initial directory 
that walk was called upon.

os.path.join() method in Python join one or more path components intelligently.
""" 

import os
print(os.walk(".")) #Nothing to see here as this is just a generator object

#Nothing to see here as this is just a generator object
for root, dirs, files in os.walk("."):
    #print (root) #print root dir names
    
    path = root.split(os.sep) #Split at separator (/ or \)
    #print(path)  #Gives names of directories for easy location of files
    #print(files)   #Prints all file names in all directories
    
#Let us now visualize directories and files within them
    print((len(path))-1) * '