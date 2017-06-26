# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:07:38 2017

@author: lankuohsing
"""

import os

import shutil

def copyFile(soureFileFullName, destinationPath):
    if not os.path.isdir(destinationPath):
        os.makedirs(destinationPath)
    shutil.copy(soureFileFullName, destinationPath)
soureFileFullName='D:\\Projects\\Python\\kaggle\\train_image'+'\\1.jpg'
destinationPath='D:\\Projects\\Github\Python\\PythonTutorials\\file_operation\\training3'
copyFile(soureFileFullName,destinationPath)