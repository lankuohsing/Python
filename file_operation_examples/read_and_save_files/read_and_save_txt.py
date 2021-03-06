# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:46:18 2018

@author: l00467141
"""
# In[]
"""将整个文件读取到字符串中"""
#f1 = open("txt_data.txt","r",encoding='UTF-8')  
f1 = open("txt_data.txt","r")   #设置文件对象
str1 = f1.read()
f1.close() #关闭文件

# In[]

#为了方便，避免忘记close掉这个文件对象，可以用下面这种方式替代
with open('txt_data.txt',"r") as f2:    #设置文件对象
    str2 = f2.read()    #可以是随便对文件的操作

# In[]
"""逐行读取"""
#第一种方法
str3_list=[]
f3 = open("txt_data.txt","r")   #设置文件对象
line = f3.readline()
line = line[:-1]#去掉换行符，也可以不去
str3_list.append(line)
while line:             #直到读取完文件
    line = f3.readline()  #读取一行文件，包括换行符
    line = line[:-1]     #去掉换行符，也可以不去
    str3_list.append(line)
f3.close() #关闭文件

# In[]
#第二种方法
data = []
for line in open("txt_data.txt","r"): #设置文件对象并读取每一行文件
    data.append(line)               #将每一行文件加入到list中

# In[]
#第三种方法
f4 = open("txt_data.txt","r")   #设置文件对象
data4 = f4.readlines()  #直接将文件中按行读到list里，效果与方法2一样
f4.close()             #关闭文件
"""
三、清空文件内容

f.truncate()

注意：仅当以 "r+"   "rb+"    "w"   "wb" "wb+"等以可写模式打开的文件才可以执行该功能。
"""
# In[]
#若文件不存在，系统自动创建。'a'表示可连续写入到文件，保留原内容，在原内容之后写入。可修改该模式（'w+','w','wb'等）
f = open("./txt_write.txt",'a')
f.write("hello,sha")
f.write("\n")
f.close()