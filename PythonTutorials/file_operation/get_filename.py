# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 19:39:34 2017

@author: lankuohsing
"""

import os
 
def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList
dir='D:\\Projects\\Github\\Python\\PythonTutorials\\file_operation\\anno3'
list = GetFileList(dir, [])
for e in list:
    print e