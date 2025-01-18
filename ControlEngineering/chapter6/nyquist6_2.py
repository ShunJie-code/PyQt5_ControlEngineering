"""
绘制 nyquist 轨迹
通过开环系统幅值和相位信息来判断闭环系统是否稳定
"""
import control as ct
import numpy as np
import matplotlib.pyplot as plt
# from ControlEngineering.chapter4.PredefinedFunction import *


def test():
    # 定义开环传递函数
    p1 = ct.tf([0, 1], [1, 1, 1.5, 1])  # 闭环系统不稳定，包围（-1， 0）
    p2 = ct.tf([0, 1], [1, 2, 2, 1])    # 闭环系统稳定
    p_list = [p1, p2]
    ct.nyquist(p_list, np.logspace(-3, 5, 10000))
    plt.show()


test()
