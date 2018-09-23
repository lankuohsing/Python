# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 15:59:05 2018

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
"""dumps：将python中的 字典 转换为 字符串"""
json_str = json.dumps(test_dict)
print("data type:",type(json_str))
print("print str:",json_str)
# In[]
"""loads: 将 字符串 转换为 字典"""
new_dict = json.loads(json_str)
print("data type:",type(new_dict))
print(new_dict)
# In[]
"""dump: 将数据写入json文件中"""
with open("json_data.json","w") as f:
    json.dump(new_dict,f)
    print("加载入文件完成...")
    
# In[]
with open("json_data.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)

# In[]
load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
print(load_dict)
