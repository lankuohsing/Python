# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:12:21 2017

@author: lankuohsing
"""
import os as os 

import shutil

def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.xml':  
                L.append(file)  
    return L   
def copyFile(soureFileFullName, destinationPath):
    if not os.path.isdir(destinationPath):
        os.makedirs(destinationPath)
    shutil.copy(soureFileFullName, destinationPath)   
file_dir='.\\A'
filelist=file_name(file_dir)
for xmlname in filelist:
    xml_len=len(xmlname)
    jpgname=xmlname[:xml_len-3]+'jpg'
    soureFileFullName='.\\B\\'+jpgname
    destinationPath='.\\C'
    copyFile(soureFileFullName,destinationPath)