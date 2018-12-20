import json
"""加载dict_rawtext_label_filename中的ratext和domain以及intent的对应关系字典"""
with open("dict_1.json",'r',encoding='UTF-8') as load_f:
    load_dict = json.load(load_f)
dict_1=load_dict
