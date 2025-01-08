"""
第六章，关注开环系统的控制系统设计
开环系统设计规格
6.1.1 稳定性

"""
import matplotlib.pyplot as plt
import control as ct
import numpy as np
from ControlEngineering.chapter4.PredefinedFunction import *


def test1(tf_p):
    """
    :param tf_p:  输入参数为传递函数
    :return: none
    """
    # 可以获取四个返回值，这里只用了相位穿越频率
    _, _, wpc, _ = ct.margin(tf_p)
    t = np.arange(0, 30, 0.1)
    u = np.sin(wpc * t)
    # 等长的全零数组
    y = 0 * u
    fig, ax = plt.subplots(2, 2)
    for i in range(2):
        for j in range(2):
            u = np.sin(wpc * t) - y
            t, y = ct.forced_response(tf_p, t, u)
            ax[i, j].plot(t, u, ls='--', label='u')
            ax[i, j].plot(t, y, label='y')
            plot_set(ax[i, j], 't', 'u, y')
    # fig.tight_layout() 是 matplotlib 库中的一个函数，
    # 用于自动调整子图参数，使之填充整个图像区域，
    # 使得子图之间的间距、子图与图像边缘之间的间距以及子图内部的标题和轴标签等元素的布局更加紧凑和美观。
    fig.tight_layout()


if __name__ == "__main__":
    # 不稳定传函
    p1 = ct.tf([0, 1], [1, 1, 1.5, 1])
    # 稳定传函
    p2 = ct.tf([0, 1], [1, 2, 2, 1])
    test1(p1)
    test1(p2)
    plt.show()  # 这是阻塞函数，只在程序最后执行可以现实多张图片
