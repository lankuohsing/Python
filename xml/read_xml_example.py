# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:42:25 2018

@author: lankuohsing
"""
from xml.dom.minidom import parse
import xml.dom.minidom
import os,sys
path = 'D:\\Projects\\Github\\Python\\xml'

#查看当前工作目录
print("当前的工作目录为：%s" %os.getcwd())

#修改当前工作目录
os.chdir(path)

# In[]
# 使用minidom解析器打开 XML 文档
DOMTree1 = xml.dom.minidom.parse("xml_example.xml")
collection = DOMTree1.documentElement
# In[]
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))
# In[]
Fixes = collection.getElementsByTagName("Fix")
# 打印每部电影的详细信息
for Fix in Fixes:
   print ("*****Fix*****")
   if Fix.hasAttribute("title"):
      print ("Title: %s" % Fix.getAttribute("title"))

   num = Fix.getElementsByTagName('num')[0]
   print ("num: %s" % num.childNodes[0].data)
   h = Fix.getElementsByTagName('h')[0]
   print ("h: %s" % num.childNodes[0].data)
   stats = Fix.getElementsByTagName('stat')
   for stat in stats:
       print ("    *****stat*****")
       mach = Fix.getElementsByTagName('mach')[0]
       print ("    mach: %s" % num.childNodes[0].data)
       fuelFlow = Fix.getElementsByTagName('fuelFlow')[0]
       print ("    fuelFlow: %s" % num.childNodes[0].data)