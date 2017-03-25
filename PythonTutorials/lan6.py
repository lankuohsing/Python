# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:29:19 2017

@author: lankuohsing
"""
#!/usr/bin/python3
import os
BASE_DIR = os.getcwd() #获取当前文件夹的绝对路径
print(BASE_DIR)
# 打开一个文件
f = open(BASE_DIR+"/tmp/foo.txt", "w")

f.write( "Python 是一个非常好的语言吗?\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()
