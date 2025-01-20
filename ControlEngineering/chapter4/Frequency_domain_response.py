from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
from PredefinedFunction import *


def test4_15():
    k = 1
    t = [1, 0.5, 0.1]
    lsg = line_style_generator()
    fig, ax = plt.subplots(2, 1)
    for i in range(len(t)):
        p = tf([0, k], [t[i], 1])
        gain, phase, w = bode(p, logspace(-2, 2), plot=False)
        plt_args = {'ls': next(lsg), 'label': 'T = '+str(t[i])}
        ax[0].semilogx(w, 20 * np.log10(gain), **plt_args)
        ax[1].semilogx(w, phase * 180 / np.pi, **plt_args)
    bode_plot_set(ax, 3, 3)
    fig.suptitle("First-order lag bode")


def test4_15_new():
    k = 1
    t = [1, 0.5, 0.1]
    lsg = line_style_generator()
    fig, ax = plt.subplots(2, 1)
    for i in range(len(t)):
        p = tf([0, k], [t[i], 1])
        gain, phase, w = frequency_response(p, logspace(-2, 2))
        plt_args = {'ls': next(lsg), 'label': 'T = '+str(t[i])}
        ax[0].semilogx(w, 20 * np.log10(gain), **plt_args)
        ax[1].semilogx(w, phase * 180 / np.pi, **plt_args)
    bode_plot_set(ax, 3, 3)
    fig.suptitle("First-order lag bode")


def test4_16():
    zeta = [1, 0.7, 0.4]
    omega_n = 1
    lsg = line_style_generator()
    fig, ax = plt.subplots(2, 1)
    for i in range(len(zeta)):
        p = tf()


if '__main__' == __name__:
    test4_15_new()
    plt.show()
