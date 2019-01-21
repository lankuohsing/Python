# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:03:40 2018

@author: lankuohsing
"""

# In[]
import xlrd
"""
#这也是一种方式
filename="test.xlsx"
f=open(filename,'r',)
workbook = xlrd.open_workbook(filename)
"""
workbook = xlrd.open_workbook(r'English Words Notes.xlsx')
# In[]
print(workbook.sheet_names()) # [u'sheet1', u'sheet2']

# In[]
#获取sheet2
sheet2_name= workbook.sheet_names()[1]
print(sheet2_name)
# 根据sheet索引或者名称获取sheet内容
# In[]
sheet2 = workbook.sheet_by_name("M")
# sheet的名称，行数，列数
print(sheet2.name,sheet2.nrows,sheet2.ncols)
# In[]
rows = sheet2.row_values(3) # 获取第四行内容
cols = sheet2.col_values(2) # 获取第三列内容
print(rows)
print(cols)
# In[]
#获取单元格内容的三种方法
print(sheet2.cell(1,0).value.encode('utf-8'))
print(sheet2.cell_value(1,0).encode('utf-8'))
print(sheet2.row(1)[0].value.encode('utf-8'))
# 获取单元格内容的数据类型
print(sheet2.cell(1,3).ctype)
