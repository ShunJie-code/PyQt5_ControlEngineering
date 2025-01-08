"""
绘制 nyquist 轨迹
"""
import control as ct
import numpy as np
import matplotlib.pyplot as plt
from ControlEngineering.chapter4.PredefinedFunction import *


def test():
    fig, ax = plt.subplots(1, 2)
    p = ct.tf([0, 1], [1, 1, 1.5, 1])
    x, y, _ = ct.nyquist(p, np.logspace(-3, 5, 1000), plot=False)
    ax[0].plot(x, y, color='k')
    ax[0].plot(x, -y, ls='--', color='k')
    ax[0].scatter(-1, 0, color='k')
    plot_set(ax[0], 'Re', 'Im')

    p = ct.tf([0, 1], [1, 2, 2, 1])
    x, y, _ = ct.nyquist(p, np.logspace(-3, 5, 1000), Plot=False)
    ax[1].plot(x, y, color='k')
    ax[1].plot(x, -y, ls='--', color='k')
    ax[1].scatter(-1, 0, color='k')
    plot_set(ax[1], 'Re', 'Im')
    plt.show()


test()
