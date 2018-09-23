# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 17:00:43 2018

@author: l00467141
"""

# In[]
import json
# In[]
test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
print("data type:",type(test_dict))
print("print dict:",test_dict)
print("\n")
# In[]
#dumps 将数据转换成字符串
json_str = json.dumps(test_dict)
print("data type:",type(json_str))
print("print str:",json_str)
