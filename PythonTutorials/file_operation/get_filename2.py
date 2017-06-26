# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 19:51:34 2017

@author: lankuohsing
"""

import os as os 
  
def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.xml':  
                L.append(file)  
    return L  
        
file_dir='D:\\Projects\\Github\\Python\\PythonTutorials\\file_operation\\anno3'
filename=file_name(file_dir)
