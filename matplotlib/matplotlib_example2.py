import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
import numpy as np
from numpy import pi as PI

# 用于正常显示中文标签
plt.rcParams["font.sans-serif"]=['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus']=False
#再论柱状图
#创建一个画板
plt.figure(figsize=(8,6))

#为画板划分多个Axes
ax = plt.subplot(111)  #假如设置为221，则表示创建两行两列也就是4个子画板,ax为第一个子画板

#数据准备
#y轴数据
data = np.array([15,20,18,25])

#柱状图的宽度
width = 0.5
#x轴数据
x_bar = np.arange(4)

#绘制柱状图
rects = ax.bar(x_bar,data,width=width,color='lightblue')

#为柱状图添加高度值
for rect in rects:
    x = rect.get_x()
    height = rect.get_height()
    ax.text(x+0.2,1.01*height,str(height)+'W')
#     print(x,height)

# 字体
font_ticks = {
#    'family' : 'serif',
    'color'  : 'black',
    'weight' : 'normal',
    'size'   : 10,
    }
font_label = {
#            'family' : 'serif',
    'color'  : 'black',
    'weight' : 'normal',
    'size'   : 20,
    }
#设置x轴的刻度

ax.set_xticks(x_bar)
x_ticks=["第一季度","第二季度","第三季度","第四季度"]
ax.set_xticklabels(x_ticks,fontdict=font_ticks)
y_ticks=list(range(0,int(max(data)*1.1),5))
ax.set_yticklabels(y_ticks,fontdict=font_ticks)
#设置y轴的刻标注
ax.set_ylabel("销量（单位：万件）",fontdict=font_label)
ax.set_xlabel("季度",fontdict=font_label)

#是否显示网格
ax.grid(True)

#拉伸y轴
ax.set_ylim(0,28)

#设置标题
ax.set_title("2017年季度销售量统计",fontdict=font_label)
#保存图片
plt.savefig("./"+"test"+".png",dpi=100)
#显示图表
plt.show()
plt.close('all')

