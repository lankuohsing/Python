# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:02:38 2017

@author: languoxing


read json files
"""
# In[]
import json
import codecs
# In[]
ticket_image_list=[]
for line in codecs.open("725火车票-486标注结果.txt",encoding="utf-8-sig"):
    dict_486=json.loads(line)
    ticket_image_list.append(dict_486)

for line in codecs.open("726火车票-901标注结果.txt",encoding="utf-8-sig"):
    dict_901=json.loads(line)
    ticket_image_list.append(dict_901)
#image_name_901=list(set(image_name_486))

