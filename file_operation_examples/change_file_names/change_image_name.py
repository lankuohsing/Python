# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:04:23 2017

@author: languoxing
"""
#In []
import os
import json
# In[]
file_name_list=os.listdir()
# In[]
file_name_list_split=list(map(lambda x:x.split("."),file_name_list))
# In[]
# In[]
image_type_list=["jpg","png"]
i=0
j=0
# In[]
image_name_list=[]
for file_name_temp in file_name_list_split:
    for image_type_temp in image_type_list:
        if(image_type_temp==file_name_temp[1]):
            image_name_list.append(file_name_temp[0])
            file_name_temp[1]="jpg"
            os.rename(file_name_list[i],str(j+1)+".jpg")
            j=j+1
            break
    i=i+1
            
# In[]
image_name_list_index=list(range(1,j+1))
image_name_dict=dict(zip(image_name_list_index,image_name_list))
with open('index_name.json', 'w') as json_file:
        json_file.write(json.dumps(image_name_dict))
# In[]

# In[]

# In[]

# In[]

# In[]

# In[]

