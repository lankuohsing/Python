# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:40:15 2019

@author: lankuohsing
"""

# In[]
import matplotlib.pyplot as plt
# In[]
# 1、基本柱状图
import matplotlib.pyplot as plt

num_list = [1.5,0.6,7.8,6]
plt.bar(range(len(num_list)), num_list)
plt.show()

# In[]
# 2、设置颜色
num_list = [1.5,0.6,7.8,6]
plt.bar(range(len(num_list)), num_list,fc='r')
plt.show()
# In[]
#3、设置标签
name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5,0.6,7.8,6]
plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
plt.show()

# In[]
#4、堆叠柱状图

name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5,0.6,7.8,6]
num_list1 = [1,2,3,1]
plt.bar(range(len(num_list)), num_list, label='boy',fc = 'y')
plt.bar(range(len(num_list)), num_list1, bottom=num_list, label='girl',tick_label = name_list,fc = 'r')
plt.legend()
plt.show()
# In[]
# 5、并列柱状图
name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5,0.6,7.8,6]
num_list1 = [1,2,3,1]
x =list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n

plt.bar(x, num_list, width=width, label='boy',fc = 'y')

for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list1, width=width, label='girl',fc = 'r')
plt.legend()
plt.show()
# In[]
# 6、条形柱状图
name_list = ['Monday','Tuesday','Friday','Sunday']
num_list = [1.5,0.6,7.8,6]
plt.barh(range(len(num_list)), num_list,tick_label = name_list)
plt.show()
