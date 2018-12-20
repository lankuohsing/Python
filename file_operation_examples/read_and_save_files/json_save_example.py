import json
dict_1={"1":"a","2":"b"}
json_str = json.dumps(dict_1, indent=4,ensure_ascii=False)
# In[]


with open("dict_1.json", 'w',encoding='UTF-8') as json_file:
    json_file.write(json_str)
