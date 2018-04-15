# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:22:12 2018

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
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))
# In[]

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
   print ("*****Movie*****")
   if movie.hasAttribute("title"):
      print ("Title: %s" % movie.getAttribute("title"))

   type = movie.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   format = movie.getElementsByTagName('format')[0]
   print ("Format: %s" % format.childNodes[0].data)
   rating = movie.getElementsByTagName('rating')[0]
   print ("Rating: %s" % rating.childNodes[0].data)
   description = movie.getElementsByTagName('description')[0]
   print( "Description: %s" % description.childNodes[0].data)
