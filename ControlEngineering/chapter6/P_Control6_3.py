"""
PID 控制
以垂直机械臂为例
"""
import numpy as np
import control as ct
import matplotlib.pyplot as plt
from ControlEngineering.chapter4.PredefinedFunction import *


def test1():
    # 机械臂模型
    g = 9.81            # 重力加速度
    length = 0.2        # 长度
    m = 0.5             # 质量
    mu = 1.5e-2         # 粘性阻尼
    j = 1.0e-2          # 转动惯量
    p = ct.tf([0, 1], [j, mu, m * g * length])
    # ref = 30            # 目标角度
    kp = (0.5, 1, 2)
    ls = line_style_generator()
    fig, ax = plt.subplots(2, 1)
    for i in range(len(kp)):
        k = ct.tf([0, kp[i]], [0, 1])
        h = p * k       # 开环传递函数
        gain, phase, w = ct.frequency_response(h, np.logspace(-1, 2))
        plt_args = {'ls': next(ls), 'label': '$k_p$='+str(kp[i])}
        ax[0].semilogx(w, 20 * np.log10(gain), **plt_args)
        ax[1].semilogx(w, phase * 180 / np.pi, **plt_args)
        print('kp = {}, (GM, PM, wpc, wgc)'.format(kp[i]))
        print(ct.margin(h))
        print("-" * 50)
    bode_plot_set(ax, 3)


if __name__ == "__main__":
    test1()
    plt.show()
