初始化数据

listA = ['zhangsan', 'lisi', 'wangwu']
listB = ['zhangsan', 'lisi', 'zhaoliu']
#1、取差集
#1.1、listA对应listB的差集

set(listA).difference(set(listB))
#-----
#set(['wangwu'])
#1.2、listB对应listB的差集

set(listB).difference(set(listA))
#-----
#set(['zhaoliu'])
#2、取交集

set(listA).intersection(set(listB))
#-----
#set(['lisi', 'zhangsan'])
#3、取并集

set(listA).union(set(listB))
#-----
#set(['lisi', 'zhaoliu', 'zhangsan', 'wangwu'])
