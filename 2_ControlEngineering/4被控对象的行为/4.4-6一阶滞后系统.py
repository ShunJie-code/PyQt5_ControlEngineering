"""
阶跃响应，用step函数
"""
from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
from PredefinedFunction import *


def code4_4():
    T = 0.5
    K = 1
    P = tf([0, K], [T, 1])
    y, t = step(P, np.arange(0, 5, 0.01))

    fig, ax = plt.subplots()
    ax.plot(t, y)
    plot_set(ax, 't', 'y')


def code4_5():
    fig, ax = plt.subplots()
    lsg = line_style_generator()
    k = 1
    t = (1, 0.5, 0.1)

    for i in range(len(t)):
        p = tf([0, k], [t[i], 1])
        y, t = step(p, np.arange(0, 5, 0.01))
        ax.plot(t, y, ls=next(lsg), label='T='+str(t[i]))
        plot_set(ax, 't', 'y', 'best')


code4_5()
plt.show()
