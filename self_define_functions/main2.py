# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:57:43 2018

@author: lankuohsing
"""
# In[]
import os,sys
import pandas as pd
# In[]
path = 'D:\\Projects\\Github\\Python\\pandas\\read_and_write_file\\Excel'

#查看当前工作目录
print("当前的工作目录为：%s" %os.getcwd())

#修改当前工作目录
os.chdir(path)

#查看修改后的工作目录
print("目录修改成功： %s" %os.getcwd())
xlsx_file1=pd.read_excel("excel_sample1.xlsx",sheetname=1,header=None)
