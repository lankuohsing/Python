# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:06:11 2020

@author: lankuohsing
"""

import matplotlib.pyplot as plt
import numpy as np

# 传入顶点的x坐标，y坐标，生成的点个数num
def pltShow(xx, yy, num):
    z = np.random.random(size=[xx.size, num])

    x = (z / sum(z)).T.dot(xx)
    y = (z / sum(z)).T.dot(yy)

    # 绘制点：黄色
    plt.plot(x, y, 'yo')
    plt.grid(True)

    # 绘制顶点：绿色
    for i in range(xx.size):
        plt.plot(xx[i], yy[i], 'go')

    plt.show()


# 随机生成N边形的N个顶点
def createPolygon(n):
    xx = np.random.randint(1, 500, n)
    yy = np.random.randint(1, 500, n)
    return xx, yy


if __name__ == '__main__':
    # 生成多边形，四边形
    xx, yy = createPolygon(4)
    # 多边形内随机生成点
    pltShow(xx, yy, 1000)
