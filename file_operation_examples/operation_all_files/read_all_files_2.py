# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:59:18 2018

@author: l00467141
"""

# In[]
# -*- coding: utf-8 -*-

import os
# In[]
import os
def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        print("root",root) #当前目录路径
        print("dirs",dirs) #当前路径下所有子目录
        print("files",files) #当前路径下所有非目录子文件
        for file in files:
            if os.path.splitext(file)[1] == '.py':#找出扩展名为py的所有文件
                L.append(os.path.join(root, file))
    return L


#其中os.path.splitext()函数将路径拆分为文件名+扩展名
# In[]
file_dir="./"
L=file_name(file_dir)